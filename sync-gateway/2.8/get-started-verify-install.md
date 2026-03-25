---
title: Verify a Sync Gateway Install
description: Configure and verify your <em>Sync Gateway</em> installation;
  securely sync enterprise data from cloud to edge!
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/get-started-verify-install.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::get-started-verify-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/get-started-verify-install.html)

# Verify a Sync Gateway Install

> Configure and verify your _Sync Gateway_ installation; securely sync enterprise data from cloud to edge!  
> This is **Step 4** in the _Start Here!_ topic group. Here we will verify that you can connect your _Sync Gateway_ to a _Couchbase Server_ and synchronize changes whether made in Couchbase Server or through Sync Gateway’s REST API.

Related _Start Here!_ topics: [Introduction](../current/introduction.md) | [Prepare](#sync-gateway::get-started-prepare.adoc) | [Install](#sync-gateway::get-started-install.adoc)

> [!NOTE]
> Preparatory Steps
> 
> Before following the steps in this topic you must have read, and acted-upon, the information and steps in [Prepare](#sync-gateway::get-started-prepare.adoc) and [Install](#sync-gateway::get-started-install.adoc).

## [](#introduction)Introduction

Steps in Getting Started

[Introduction](../current/introduction.md)| [Prepare](#sync-gateway::get-started-prepare.adoc)| [Install](#sync-gateway::get-started-install.adoc)| **Verify**

In this final step of the Getting Started topic we will look to link your Sync Gateway to a Couchbase Server bucket and verify that sync is taking place by executing a CRUD cycle. You will need to edit the configuration file used in the [Install](#sync-gateway::get-started-install.adoc) step to point to a bucket on your Couchbase Server — see [Configure Sync Gateway](#lbl-config).

On completion of this topic you will have a working Sync Gateway instance that you know syncs with a Couchbase Server. You will have successfully completed installation and can now build on this with confidence.

## [](#lbl-config)Configure Sync Gateway

To configure Sync Gateway to connect to a Couchbase Server:

1. Ensure your Sync Gateway service is stopped/unloaded
2. Edit the configuration file you used in [Install](#sync-gateway::get-started-install.adoc) and replace the contents with those shown in [Example 1](#sample-cfg).  
The configuration points to the `get-started-bucket` which we will use to verify that you can synchronize changes made through the Sync Gateway API with those made through Couchbase Server.
3. Ensure you start Couchbase Server
4. Restart/Load your Sync Gateway to pick-up the changed configuration

Example 1\. Simple Sync Gateway-Couchbase Server Config

```json
{
  "adminInterface": "127.0.0.1:4985",
  "interface": "0.0.0.0:4984",
  "databases": {
    "get-started-bucket": {
      "server": "http://127.0.0.1:8091",
      "bucket": "get-started-bucket", (1)
      "username": "sync_gateway", (2)
      "password": "password",
      "enable_shared_bucket_access": true, (3)
      "import_docs": true, (4)
      "num_index_replicas": 0, (5)
      "users": {
        "GUEST": { "disabled": false, "admin_channels": ["*"] } (6)
      }
    }
  },
  "logging": { (7)
    "console": {
      "log_level": "debug",
      "log_keys": ["*"]
    }
  }
}
```

About the Configuration Properties

| **1** | Here we point to the Couchbase Server bucket you created in [Configure Server for Sync Gateway](#sync-gateway::get-started-prepare.adoc#configure-server)                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Provided the credentials for the RBAC user that you created on the Couchbase Server Admin Console — see [Configure Server for Sync Gateway](#sync-gateway::get-started-prepare.adoc#configure-server)                                                                                                           |
| **3** | Set enable\_shared\_bucket\_access true to allow both Sync Gateway and Couchbase Server to make changes to the same bucket. This works in conjunction with import\_docs to facilitate the replication of changes whether made through Sync Gateway or externally by an App or Couchbase Server SDK for example. |
| **4** | Set import\_docs true to allow import processing to take place on this Sync Gateway node, thereby integrating document changes made outside of Sync Gateway                                                                                                                                                     |
| **5** | num\_index\_replicas is the number of index replicas stored in Couchbase Server — see [Indexing versus Views](../current/deploy/indexing.md). **NOTE:** If you’re running a single Couchbase Server node for development purposes the num\_index\_replicas must be set to 0.                                    |
| **6** | Here users introduces a guest user with access to all channels and all documents                                                                                                                                                                                                                                |
| **7** | Define your logging requirements:Here we set general diagnostic console logs on. If you’re having issues then refer to [Logging](../current/manage/logging.md) for how to tune diagnostics to provide additional troubleshooting help                                                                           |

## [](#connect-to-sync-gateway)Connect to Sync Gateway

> [!TIP]
> You can use [Console Logs](logging.md#lbl-console-logs) to aid diagnosis of connection issues

1. With Sync Gateway and Couchbase Server started, point your browser to the Sync Gateway url, typically on port 4984, but this can be changed — see: [REST API Access](../current/rest-api/rest-api-access.md).  
So, for example:  
```bash  
http://localhost:4984  
```
2. Check that you receive a response similar to this:  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"2.8"},"version":"Couchbase Sync Gateway/{version-full}(376;e2e7d42) EE"}  
```  
If there are issues then check the [Console Logs](logging.md#lbl-console-logs) for more information. Where necessary you can redirect console output to a file — see: [Redirect Console Logs](logging.md#lbl-log-redirect).

> [!TIP]
> If Sync Gateway is behind a load balancer then check the websockets configuration — see [Load Balancer](../current/deploy/load-balancer.md).

## [](#verify-the-crud-cycle)Verify the CRUD Cycle

Here we will use CURL and Sync Gateway’s REST API to

1. [Create a New Document:](#lbl-crud-crt) Use the API to add a document and check the document on Couchbase Server
2. [Get a Document Using the API:](#lbl-crud-get) Read the document back from Couchbase Server using the Sync Gateway API
3. [Update a Document using API:](#lbl-crud-upd) Update the newly created document and observe the changes in Couchbase Server
4. [Sync a Couchbase Server Change](#lbl-crud-upd-svr) Update the document in Couchase Server and check the change in Sync Gateway
5. [Delete a Document Using API](#lbl-crud-del) Delete our document and check its state on Couchbase Server and Sync Gateway.

### [](#lbl-crud-crt)Create a New Document:

Within a terminal use CURL to issue the following POST request, which adds a new document to the Couchbase Server bucket `get-started-bucket` by way of the Sync Gateway database `get-started-bucket` we configured in [Configure Sync Gateway](#lbl-config)

Request

```bash
curl --location -g --request POST 'http://localhost:4984/get-started-bucket/' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "_id": "first-doc",
  "name": "Verify-Install Topic",
  "type": "get-started",
  "data": "any random string"
}'
```

Response

```bash
{"id":"first-doc","ok":true,"rev":"1-a46e9c2f8ff4581e5662c47ae8519b0e"}%
```

Check

View the document in Couchbase Server Admin Console to verify it syncs from Sync Gateway database.

1. Within the Admin Console, select **Buckets** and hit the **Documents** button to open the _Document Editor_ tab.
2. Within the _Document Editor_ tab:

  1. Enter `get-started-bucket` as _Bucket_
  2. Enter `first` as _Document ID_
  3. Enter  
  You will see the response shown in [Figure 1](#img-cbs-view). The document should include any changes made through Sync Gateway, including the initial create.  
  ![cbs view first doc](_images/cbs-view-first-doc.png)  
  Figure 1\. Couchbase Server Document Editor

### [](#lbl-crud-get)Get a Document Using the API:

Request

```bash
curl --location --request GET 'http://localhost:4984/get-started-bucket/first-doc'
```

Response

```bash
{"_id":"first-doc","_rev":"1-a46e9c2f8ff4581e5662c47ae8519b0e","data":"any random string","name":"Verify-Install Topic","type":"get-started"}%
```

### [](#lbl-crud-upd)Update a Document using API:

Request

```bash
curl --location -g --request PUT 'http://localhost:4984/get-started-bucket/first-doc' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "_id": "first-doc",
  "_rev": "1-a46e9c2f8ff4581e5662c47ae8519b0e", (1)
  "name": "Verify-Install Topic",
  "type": "get-started",
  "data": "an edited string" (2)
}'
```

| **1** | This revision is the one returned by the response to the initial POST request — see: [Response to Add Document Request](#lbl-crud-add-resp) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we change the text of the _data_ field.                                                                                                |

Response

```bash
{"id":"first-doc","ok":true,"rev":"2-ecbdda61df3290beff4d0e433af8d745"}%  (1)
```

| **1** | Here the "ok":true indicates success, whilst the revision shows it is the second change to this document. |
| ----- | --------------------------------------------------------------------------------------------------------- |

Check

[Check Document on Couchbase Server](#lbl-check-cbs). Does the document contain the changed _data_ value?

### [](#lbl-crud-upd-svr)Sync a Couchbase Server Change

This will show that changes made using Couchbase Server are replicated to Sync Gateway.

1. Within the Couchbase Server Document Editor

  1. Retrieve `first_doc` if it is not currently displayed
  2. Edit the _data_ value to contain `"an edited string also changed in server"`
  3. **Save** the change.
2. In your terminal, use the API to get the document again — see [Get a Document Using the API:](#lbl-crud-get)  
You should see the change you made in Couchbase Server reflected in the response. For example:  
```bash  
{"_id":"first-doc","_rev":"3-cc2e758ef63b0daf5b01b2baf98c72b6", (1)  
"data":"an edited string also changed in server", (2)  
"name":"Verify-Install Topic","type":"get-started"}  
```

| **1** | Note that the revision sequence is now 3, up from the 2 returned in our [Response to Update Document Request](#lbl-crud-upd-resp)                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Note that the data field now contains both the change made in Sync Gateway ("an edited string") and that made in Couchbase Server ("also changed in server") |

### [](#lbl-crud-del)Delete a Document Using API

Request

```bash
curl --location -g --request DELETE 'http://localhost:4984/get-started-bucket/first-doc?rev=3-cc2e758ef63b0daf5b01b2baf98c72b6' (1)
```

| **1** | Note that we provide here the revision ID of the latest revision (3), as returned in the response to the last GET request. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |

Response

You should see the following response:

```bash
{"id":"first-doc","ok":true,"rev":"4-03f1ba127340e8c50c31a36279298e60"}%  (1)
```

| **1** | You can see here that the delete counts as the fourth change/revision. Again "ok":true indicates the delete was successful. |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |

Check

* [Check Document on Couchbase Server](#lbl-check-cbs) and you should now see "No Results"
* Use the API to get the document — see: [Get a Document Using the API:](#lbl-crud-get). Assuming the delete worked you should see the following response:  
```bash  
{"error":"not_found","reason":"deleted"}%  
```

## [](#ways-to-verify-sync)Ways to Verify Sync

To verify that document changes have been replicated, you can:

* Monitor the Sync Gateway revision number returned by the database endpoint ([GET /{db}/](rest-api.md#/database/get%5F%5Fdb%5F%5F)). The revision number increments for every change that happens on the Sync Gateway database.
* Query a document by ID on the Sync Gateway REST API as shown in [Check Document on Couchbase Server](#lbl-check-cbs). Use ([GET /{db}/{id}](rest-api.md#/document/get%5F%5Fdb%5F%5F%5Fdoc%5F)) — see: [REST API Access](../current/rest-api/rest-api-access.md) for more.
* Query a document from the Query Workbench on the Couchbase Server Console.

## [](#next-steps)Next Steps

Now you know Sync Gateway is deployed and operational. So, you can explore more complex scenarios with confidence.

Maybe you want to learn more about Sync Gateway’s [Configuration Schema](../current/configuration/configuration-properties-legacy.md) or how to [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md). Or perhaps you want to explore how to:

* Implement access controls for users and data — see: [Users](../current/access-control/users.md), [Roles](../current/access-control/roles.md) and the [Sync Function](../current/access-control/sync-function/sync-function.md) that ties it all together.
* Implement secure connectivity using TLS/SSL, which is described in [User Authentication](../current/security/authentication-users.md) and [TLS Certificate Authentication](../current/security/authentication-certs.md)
* Build more complex syncs, such as those that sync with:

  * Other Sync Gateway nodes, for which see [Inter Sync Gateway Sync - Overview](../current/sync/sync-inter-syncgateway-overview.md)
  * Apps on mobile devices using Couchbase Lite — see [Sync Using App](../current/sync/sync-using-app.md)

## [](#related-content)Related Content

###### [](#)

Getting Started

* [Prepare](#sync-gateway::get-started-prepare.adoc)
* [Install](#sync-gateway::get-started-install.adoc)
* [Verify](#sync-gateway::get-started-verify-install.adoc)

###### [](#-2)

Product Information

* [Release Notes](../current/product-notes/release-notes.md)
* [Compatibility Matrix](#sync-gateway::compatibility.adoc)
* [Supported OS](#sync-gateway::pn-supported-os.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)