---
title: Integrating External Stores
description: Introducing Sync Gateway integration with external data stores
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/integrating-external-stores.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::integrating-external-stores.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/integrating-external-stores.html)

# Integrating External Stores

> Introducing Sync Gateway integration with external data stores  

Related _integration_ topics: [Changes Feed](server-integration.md) | [Event Handling](../current/deploy/webhooks.md) | [Prometheus Integration](../current/deploy/stats-prometheus.md)

## [](#introduction)Introduction

In this guide, you will learn how to run the following operations using the Admin REST API:

* Bulk importing of documents.
* Exporting via the changes feed.
* Importing attachments.

## [](#external-store)External Store

In this guide, you will use a simple movies API as the external data store. [Download the stub data and API server](https://cl.ly/140P313l0p23/external-store.zip) and unzip the content into a new directory. To start the server of the external store run the following commands:

```bash
cd external-store
npm install
node server.js
```

You can open a browser window at `http://localhost:8000/movies` to view the JSON data.

The external store supports two endpoints:

GET `/movies`

Retrieves all movies (from **movies.json**).

POST `/movies`

Takes one movie as the request body and updates the item with the same `_id` in **movies.json**.

## [](#importing-documents)Importing Documents

The Sync Gateway Swagger JS library is a handy tool to send HTTP requests without having to write your own HTTP API wrapper. It relies on the Couchbase Mobile Swagger specs.

> [!NOTE]
> We do not guarantee that the swagger spec will be aligned with the latest version of the REST API. The REST API must be considered as the source of truth and in case of any deviations, the REST API will override the swagger spec. So please consider the spec as a starting point and make any relevant changes as needed to ensure that it is in conformance with the REST API.

In this case, you will use the [Admin REST API](../current/rest-api/rest-api-admin.md).

1. Get Dependencies  
In the same directory, install the following dependencies.  
```bash  
npm install swagger-client && request-promise  
```
2. Get Sync Gateway  
[Download Sync Gateway](https://www.couchbase.com/downloads#couchbase-mobile) and start it from the command line with a database called `movies_lister`.  
```bash  
~/Downloads/couchbase-sync-gateway/bin/sync_gateway -dbname movies_lister  
```  
The Sync Gateway database is now available at `http://localhost:4985/movies_lister/`.
3. Create import function  
Create a new file called `import.js` with the following to retrieve the movies and insert them in the Sync Gateway database.  
Example 1\. Importing to Sync Gateway  
```javascript  
var request = require('request-promise')  
  , Swagger = require('swagger-client');  
var api = 'http://localhost:8000/movies'  
  , db = 'movies_lister';  
var client = new Swagger({  
  url: 'https://docs.couchbase.com/sync-gateway/current/_attachments/sync-gateway-public.yaml',  
  usePromise: true  
}).then(function (client) {  
  var data = [];  
  request({uri: api, json: true}) (1)  
    .then(function (movies) {  
      data = movies;  
      return client.database.post_db_bulk_docs({db: db, BulkDocsBody: {docs: movies}}); (2)  
    })  
    .then(function (res) {  
      return res.obj;  
    })  
    .each(function (row) { (3)  
      var movie = data.filter(function (movie) {  
        return movie._id == row.id ? true : false  
      })[0];  
      movie._rev = row.rev;  
      var options = {  
        method: 'POST',  
        uri: api,  
        body: movie,  
        headers: {  
          'Content-Type': 'application/json'  
        },  
        json: true  
      };  
      return request(options);  
    })  
    .then(function (res) {  
      console.log('Revs of ' + res.length + ' imported');  
    });  
});  
```  
Here’s what the code above is doing:

| **1** | Use the [request-promise](https://github.com/request/request-promise) library to retrieve the movies from the external store.                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Save the movies to Sync Gateway. The post\_db\_bulk\_docs method takes a db name (movies\_lister) and the documents to save in the request body. Notice that the response from the external store is an array and must be wrapped in a JSON object of the form {docs: movies}. |
| **3** | The response of the /{db}/\_bulk\_docs request contains the generated revision numbers which are written back to the external store.                                                                                                                                           |  
> [!TIP]  
> The Admin REST API Swagger spec is dynamically loaded. You can use the `.help()` method to query the available object and methods. This method is very helpful during development as it offers the documentation on the fly in the console.  
Example 2\. Getting Help Information  
```javascript  
client.help(); // prints all the tags to the console  
client.database.help(); // prints all the database methods to the console  
client.database.post_db_bulk_docs.help(); // prints all the parameters (querystring and request body)  
```
4. Start the program  
From the command line, use:  
```bash  
node import.js  
```
5. Verify the import  
To verify that the movie documents have been imported, you can:

  * Monitor the Sync Gateway sequence number returned by the database endpoint ([GET /{db}/](../current/rest-api/rest-api.md#/database/get%5F%5Fdb%5F%5F)). The sequence number increments for every change that happens on the Sync Gateway database.
  * Query a document by ID on the Sync Gateway REST API ([GET /{db}/{id}](../current/rest-api/rest-api.md#/document/get%5F%5Fdb%5F%5F%5Fdoc%5F)).
  * Query a document from the Query Workbench on the Couchbase Server Console.  
Notice that the `_rev` property is also stored on each record on the external store, `movies.json`.
6. Run the program again  
You will see the same number of documents are visible in Sync Gateway. This time with a 2nd generation revision number. This update operation was successful because the parent revision number was sent as part of the request body.

## [](#exporting-documents)Exporting Documents

To export documents from Couchbase Mobile to the external system you will use a changes feed request to subscribe to changes and persist them to the external store.

Install the following modules:

```bash
npm install swagger-client && request
```

Create a new file called `export.js` with the following:

Example 3\. Exporting from Sync Gateway

```javascript
var request = require('request')
  , Swagger = require('swagger-client');

var api = 'http://localhost:8000/movies'
  , db = 'movies_lister';

var client = new Swagger({
  url: 'https://docs.couchbase.com/sync-gateway/current/_attachments/sync-gateway-admin.yaml',
  success: function () {

    client.database.get_db({db: db}, function (res) { (1)

      getChanges(res.obj.update_seq); (2)
    });

    function getChanges(seq) {(3)
      var options = {db: db, feed: 'longpoll', since: seq, include_docs: true};
      client.database.get_db_changes(options, function (res) {

        var results = res.obj.results;
        for (var i = 0; i < results.length; i++) {
          var row = results[i];
          console.log("Document with ID " + row.id);

          var options = { (4)
            url: api,
            method: 'POST',
            body: JSON.stringify(row.doc),
            headers: {
              'Content-Type': 'application/json'
            }
          };
          request(options, function (error, response, body) {
            if (!error && response.statusCode == 200) {
              var json = JSON.parse(body);
              console.log(json);
              console.log("Wrote update for doc " + json.id + " to external store.");
            }
          });
        }

        getChanges(res.obj.last_seq);
      });
    }

  }
});
```

Here’s what the code above is doing:

| **1** | Gets the last sequence number of the database.                                                                                                 |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Calls the getChanges method with the last sequence number.                                                                                     |
| **3** | Sends changes request to Sync Gateway with the following parameters: feed=longpoll include\_docs=true since=X (where X is the sequence number) |
| **4** | Write the document to the external store.                                                                                                      |

Run the program from the command line:

```bash
node export.js
```

Update a document through the Sync Gateway REST API. Notice that the change is also updated in the external store.

![export update](_images/export-update.gif) 

## [](#importing-attachments)Importing Attachments

Every movie in the stub API has a link to a thumbnail (in the `posters.thumbnail` property). Before sending the `_bulk_docs` request, you will fetch the thumbnail for each movie and embed it as a base64 string under the `_attachments` property.

Install the following dependencies:

```bash
npm install request-promise && swagger-client
```

Create a new file called `attachments.js` with the following to retrieve the movies, their thumbnails and insert them in the Sync Gateway database.

Example 4\. Importing Attachments

```javascript
var request = require('request-promise')
  , Swagger = require('swagger-client');

var api = 'http://localhost:8000/movies'
  , db = 'movies_lister';

var movies = [];

var client = new Swagger({
  url: 'https://docs.couchbase.com/sync-gateway/current/_attachments/sync-gateway-admin.yaml',
  usePromise: true
}).then(function (client) {
  // Get movies from stub API
  request({uri: api, json: true})
    .then(function (res) {
      movies = res;
      // return array of links
      return movies.map(function (movie) {
        return movie.posters.thumbnail;
      });
    })
    .map(function (link) {
      // Fetch each thumbnail, the program continues once
      // all 24 thumbnails are downloaded
      return request({uri: link, encoding: null});
    })
    .then(function (thumbnails) {
      // Save the attachment on each document
      for (var i = 0; i < movies.length; i++) {
        var base64 = thumbnails[i].toString('base64');
        movies[i]._attachments = {
          image: {
            content_type: 'image\/jpg',
            data: base64
          }
        };
      }
      return movies;
    })
    .then(function (movies) {
      // Save the documents and attachments in the same request
      return client.database.post_db_bulk_docs({db: db, BulkDocsBody: {docs: movies}});
    })
    .then(function (res) {
      console.log(res);
    });
});
```

Restart Sync Gateway to have an empty database and run the program. The documents are saved with the attachment metadata.

![admin ui attachment](_images/admin-ui-attachment.png) 

You can view the thumbnail at `http://localhost:4984/movies_lister/{db}/{doc}/{attachment}/` (note it’s on the public port 4984).

![sg attachment](_images/sg-attachment.png) 

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)