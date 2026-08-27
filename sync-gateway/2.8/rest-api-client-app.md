---
title: REST API Client Application
description: Using the REST API to initiate Sync Gateway Replication
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/rest-api-client-app.adoc
  xref: xref:2.8@sync-gateway::rest-api-client-app.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/rest-api-client-app.html)

# REST API Client Application

> Using the REST API to initiate Sync Gateway Replication  

Related _Sync - REST API_ topics: [Public REST API](../current/rest-api/rest-api.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

Whether you're developing a web application getting data from the Sync Gateway API or integrating it with another system you will almost certainly need an HTTP library to consume the Public and Admin Sync Gateway REST APIs. The documentation for the Sync Gateway REST APIs is using Swagger which is a great toolkit for writing REST API documentation, and also to generate HTTP libraries. This guide will walk you through how to start using those libraries to display documents stored in Sync Gateway on a web page

> [!NOTE]
> We do not guarantee that the swagger spec will be aligned with the latest version of the REST API. The REST API must be considered as the source of truth and in case of any deviations, the REST API will override the swagger spec. So please consider the spec as a starting point and make any relevant changes as needed to ensure that it is in conformance with the REST API.

Follow the steps below to get Sync Gateway up and running.

1. [Download Sync Gateway](https://www.couchbase.com/downloads/?family=mobile#couchbase-mobile)
2. In a new working directory, open a new file called `sync-gateway-config.json` with the following  
```javascript  
{  
    "log": ["HTTP+"],  
    "CORS": {  
        "origin":["http://localhost:8000"],  
        "loginOrigin":["http://localhost:8000"],  
        "headers":["Content-Type"],  
        "maxAge": 1728000  
    },  
    "databases": {  
        "todo": {  
            "server": "http://localhost:8091",  
            "users": { "GUEST": {"disabled": false, "admin_channels": ["*"] } }  
        }  
    }  
}  
```  
Here, you're enabling CORS on `http://localhost:8000`, the hostname of the web server that will serve the web application.
3. Start Sync Gateway from the command line with the configuration file  
```bash  
~/Downloads/couchbase-sync-gateway/bin/sync_gateway sync-gateway-config.json  
```
4. Insert a few documents using the POST `/{db}/_bulk_docs` endpoint  
```bash  
curl -X POST http://localhost:4985/todo/_bulk_docs \
            -H "Content-Type: application/json" \
            -d '{"docs": [{"task": "avocados", "type": "task"}, {"task": "oranges", "type": "task"}, {"task": "tomatoes", "type": "task"}]}'  
```

## [](#a-simple-web-application)A Simple Web Application

In this section you will use Swagger JS in the browser to insert a few documents and display them in a list. Create a new file called **index.html** with the following.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Todos</title>
</head>
<body>
  <h2>Todos</h2>
  <ul id="list"></ul>
</body>
<script src="swagger-client.min.js"></script>
<script src="index.js"></script>
</html>
```

Install the [swagger-js](https://github.com/swagger-api/swagger-js) library in your working project.

Next, create a new file called **index.js** to start sending requests to Sync Gateway.

```javascript
// initialize swagger client, point to a swagger spec
window.client = new SwaggerClient({
  url: 'https://docs.couchbase.com/sync-gateway/current/_attachments/sync-gateway-public.yaml',
  usePromise: true
})
  .then(function (client) {
    client.help();
  });
```

Here you're initializing the Swagger library with the Sync Gateway public REST API spec and promises enabled. Promises are great because you can chain HTTP operations in a readable style.

In this working directory, start a web server with the command `python -m SimpleHTTPServer 8000` and navigate to http://localhost:8000/index.html in a browser. Open the dev tools to access the console and you should see the list of operations available on the `client` object.

![swagger browser](_images/swagger-browser.png) 

All the endpoints are grouped by tag. A tag represents a certain functionality of the API (i.e database, query, authentication).

The `client.help()` method is a helper function that prints all the tags available. In this case we'd like to query all documents in the database so we'll use the `get_db_all_docs` method on the database tag to perform this operation. The helper function is available on any node of the API, so you can write `client.database.get_db_all_docs.help()` to print the documentation for that endpoint as shown below.

![swagger all docs](_images/swagger-all-docs.png) 

Copy the following below the existing code in **index.js** to query all the documents in the database and display them in the list.

```javascript
client.query.get_db_all_docs({db: 'todo', include_docs: true})
  .then(function (res) {
    var rows = res.obj.rows;
    var list = document.getElementById('list');
    for (var i = 0; i < rows.length; i++) {
      var item = document.createElement('li');
      item.innerText = rows[i].doc.task;
      list.appendChild(item);
    }
  })
  .catch(function (err) {
    console.log(err);
  })
```

The **include\_docs** option is used to retrieve the document properties (the text to display on the screen is located on the `doc.task` field). A promise can either be fulfilled with a value (the successful response) or rejected with a reason (the error response). Reload the browser and you should see the list of tasks.

![task list](_images/task-list.png) 

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