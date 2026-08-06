---
title: Explore Sync Gateway
description: Add a database, create users, and run a CRUD cycle to explore your
  <em>Sync Gateway</em> installation end-to-end.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/start-here/pages/get-started-explore.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:start-here:get-started-explore.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/start-here/get-started-explore.html)

# Explore Sync Gateway

> Add a database, create users, and run a CRUD cycle to explore your _Sync Gateway_ installation end-to-end.  
> This is **Step 4** in the _Start Here!_ topic group. Here we add a database configuration, create a Sync Gateway user, and run a CRUD cycle to confirm sync is working end-to-end.

> [!NOTE]
> Preparatory Steps
> 
> Ensure you have completed all steps in [Prepare](get-started-prepare.md), [Install](get-started-install.md), and [Configure](get-started-configure.md) before proceeding.

Steps in Getting Started

[Introduction](../introduction.md)| [Prepare](get-started-prepare.md)| [Install](get-started-install.md)| [Configure](get-started-configure.md)

## [](#introduction)Introduction

In this step you will use the Sync Gateway Admin REST API to add a database configuration pointing to the `travel-sample` bucket, create a role and user scoped to the `inventory.hotel` collection, and then run a full CRUD cycle to confirm that sync is working between Sync Gateway and Couchbase Server.

On completion of this topic you will have confirmed end-to-end sync and will be ready to build on this foundation with confidence.

> [!NOTE]
> The `curl` commands on this page require basic authentication using the `sync_gateway` Couchbase Server RBAC user credentials created in [Create RBAC users](get-started-prepare.md#step-2create-rbac-user). You can create the Base64 digest from your credentials as follows:
> 
> ```console
> DIGEST=`echo -n sync_gateway:password | base64`
> echo $DIGEST
> # c3luY19nYXRld2F5OnBhc3N3b3Jk
> 
> curl --header "Authorization: Basic $DIGEST" ...
> ```

## [](#add-a-database-configuration)Add a Database Configuration

Use the Admin REST API to add a database to your Sync Gateway cluster.

The `curl` command shown in [Example 1](#ex-add-sgw-db) creates a `traveldb` database pointing to the Couchbase Server `travel-sample` bucket, scoped to the `inventory.hotel` collection.

Example 1\. Add a Sync Gateway Database

```bash
curl  --location --request PUT 'http://127.0.0.1:4985/traveldb/' \(1)
      --header "Authorization: Basic $DIGEST" \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "bucket": "travel-sample", (2)
          "scopes": {
            "inventory": {
              "collections": {
                "hotel": {} (3)
              }
            }
          },
          "index": {"num_replicas": 0} (4)
          }'
```

| **1** | Here we specify the name of the Sync Gateway database — traveldb                                                                                                     |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Now we point traveldb at the Couchbase Server bucket travel-sample, which we created in [Configure Server for Sync Gateway](get-started-prepare.md#configure-server) |
| **3** | We scope the database to the inventory.hotel collection in the travel-sample bucket                                                                                  |
| **4** | Suitable for single-node development clusters — remove or increase for production                                                                                    |

## [](#add-a-sync-gateway-user)Add a Sync Gateway User

Create a Sync Gateway role and user to allow secure access during replication on this Sync Gateway cluster.

### [](#add-a-role)Add a Role

The `curl` command shown in [Example 2](#ex-add-role) adds a role called `stdrole` with access to the `inventory.hotel` collection.

Example 2\. Add a Sync Gateway Role

```bash
curl  --location --request PUT 'http://127.0.0.1:4985/traveldb/_role/stdrole' \(1)
      --header "Authorization: Basic $DIGEST" \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "name": "stdrole",
          "collection_access": {
             "inventory": { (2)
                "hotel": {
                    "admin_channels": ["newrolechannel"] (3)
                 }
             }
           }
      }'
```

| **1** | Here we identify the Sync Gateway database — traveldb, the action \_role, and the role name stdrole.                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we scope the role to the inventory scope and hotel collection in the travel-sample bucket.                                  |
| **3** | Here we identify the channels accessible to users assigned this role; these will be used by the Sync Function to control access. |

### [](#add-the-user)Add the User

The `curl` command shown in [Example 3](#ex-add-user) adds a user called `sgwuser1`.

Example 3\. Add a Sync Gateway User

```bash
curl  --location -g --request POST 'http://localhost:4985/traveldb/_user/' \(1)
      --header 'Content-Type: application/json' \
      --header "Authorization: Basic $DIGEST" \(2)
      --data-raw '{
          "name": "sgwuser1", (3)
          "password": "passwordstring",
          "admin_roles": ["stdrole"], (4)
          "collection_access": {
             "inventory": { (5)
                "hotel": {
                    "admin_channels": ["public"]
                 }
             }
           }
      }'
```

| **1** | Here we identify the Sync Gateway database — traveldb and the required object \_user                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The credential in the Authorization header relates to the Sync Gateway admin user                                                                       |
| **3** | Here we provide the credentials of the user to create: name sgwuser1 and required password. If the password is omitted, a random password is generated. |
| **4** | Here we identify any roles assigned to this user; it will inherit any channels associated with those roles.                                             |
| **5** | Here we scope the user's access to the inventory scope and hotel collection in the travel-sample bucket.                                                |

## [](#verify-the-crud-cycle)Verify the CRUD Cycle

Here we will use curl and Sync Gateway's REST API to run a full CRUD cycle:

1. [Create a New Document](#lbl-crud-crt) — Add a document via the API and verify it appears in Couchbase Server
2. [Get a Document Using the API](#lbl-crud-get) — Read the document back from Couchbase Server using the Sync Gateway API
3. [Update a Document Using the API](#lbl-crud-upd) — Update the document and observe the change in Couchbase Server
4. [Sync a Couchbase Server Change](#lbl-crud-upd-svr) — Update the document in Couchbase Server and check the change in Sync Gateway
5. [Delete a Document Using the API](#lbl-crud-del) — Delete the document and verify its state in both Couchbase Server and Sync Gateway

### [](#lbl-crud-crt)Create a New Document

Use curl to add a new document to the `traveldb` database via the Sync Gateway public API.

Request

```console
DIGEST=`echo -n sgwuser1:passwordstring | base64`

curl  --location --request PUT 'http://localhost:4984/traveldb.inventory.hotel/hotel_88801' \(1)
      --header "Authorization: Basic $DIGEST" \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "_id": "hotel_88801",
          "id": "88801",
          "type": "hotel",
          "name": "Verify-Install Topic",
          "address": "The Shambles",
          "city": "Manchester",
          "country": "United Kingdom"
      }'
```

| **1** | The keyspace traveldb.inventory.hotel targets the hotel collection in the inventory scope of the traveldb database. |
| ----- | ------------------------------------------------------------------------------------------------------------------- |

Response

```bash
{"id":"hotel_88801",
"ok":true,
"rev":"1-f28b5cc13a38892f4f85913d4e654270"}
```

Check

View the document in the Couchbase Server Admin Console to verify it synced from Sync Gateway.

1. Within the Admin Console, select **Buckets** and select **Documents** to open the _Document Editor_ tab.
2. Within the _Document Editor_ tab:

  1. Enter `travel-sample` as _Bucket_
  2. Enter `inventory` as _Scope_
  3. Enter `hotel` as _Collection_
  4. Enter `id="88801"` as _SQL++ WHERE_ query
  5. Enter  
  You will see the response shown in [Figure 1](#img-cbs-view). The document should include any changes made through Sync Gateway, including the initial create.  
  ![cbs view first doc](../_images/cbs-view-first-doc.png)  
  Figure 1\. Couchbase Server Document Editor

### [](#lbl-crud-get)Get a Document Using the API

Request

```bash
curl  --location --request GET 'http://localhost:4984/traveldb.inventory.hotel/hotel_88801' \
      --header "Authorization: Basic $DIGEST"
```

Response

```bash
{
    "_id": "hotel_88801",
    "_rev": "1-f28b5cc13a38892f4f85913d4e654270",
    "address": "The Shambles",
    "city": "Manchester",
    "country": "United Kingdom",
    "id": "88801",
    "name": "Verify-Install Topic",
    "type": "hotel"
}
```

### [](#lbl-crud-upd)Update a Document Using the API

Request

```bash
curl  --location -g \
      --request PUT 'http://localhost:4984/traveldb.inventory.hotel/hotel_88801?new_edits=true&rev=1-f28b5cc13a38892f4f85913d4e654270' \(1)
      --header "Authorization: Basic $DIGEST" \
      --header 'Accept: application/json' \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "_id": "hotel_88801",
        "id": "88801",
        "type": "hotel",
        "name": "Verify-Install Topic Updated", (2)
        "address": "The Shambles",
        "city": "Manchester",
        "country": "United Kingdom",
        "email": "enquiries@hotel_88801.internet" (3)
      }'
```

| **1** | This revision is the one returned by the response to the initial PUT request — see: [Response to Add Document Request](#lbl-crud-add-resp) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Here we change the text of the _name_ field.                                                                                               |
| **3** | Here we add an _email_ field.                                                                                                              |

Response

```bash
{
    "id": "hotel_88801",
    "ok": true,
    "rev": "2-249366b198e81f203d7ae9eb54376210"  (1)
}
```

| **1** | The revision shows this is the second change to the document. "ok":true indicates success. |
| ----- | ------------------------------------------------------------------------------------------ |

Check

[Check Document on Couchbase Server](#lbl-check-cbs) — does the document contain the updated _name_ value?

### [](#lbl-crud-upd-svr)Sync a Couchbase Server Change

This confirms that changes made in Couchbase Server replicate back to Sync Gateway.

1. Within the Couchbase Server Document Editor:

  1. Retrieve `88801` if it is not currently displayed. Use `meta().id="hotel_88801"` as the query, with `travel-sample` as _Bucket_, `inventory` as _Scope_, and `hotel` as _Collection_.
  2. Edit the _email_ value to `reception@hotel_88801.internet`
  3. Edit the _name_ value to `Verify-Install Topic-Updated-In-Server`
  4. **Save** the change.
2. In your terminal, use the API to get the document again — see [Get a Document Using the API](#lbl-crud-get).  
You should see the change you made in Couchbase Server reflected in the response. For example:  
```bash  
{"_id":"hotel_88801","_rev":"3-cc2e758ef63b0daf5b01b2baf98c72b6", (1)  
"address":"The Shambles","city":"Manchester","country":"United Kingdom","email":"reception@hotel_88801.internet","id":"88801","name":"Verify-Install Topic-Updated-In-Server","type":"hotel"}  
```

| **1** | The revision sequence is now 3\. The _email_ and _name_ fields reflect both the Sync Gateway change and the Couchbase Server amendment. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |

### [](#lbl-crud-del)Delete a Document Using the API

Request

```bash
curl --location -g --request DELETE 'http://localhost:4984/traveldb.inventory.hotel/hotel_88801?rev=3-cc2e758ef63b0daf5b01b2baf98c72b6' \(1)
  --header "Authorization: Basic $DIGEST"
```

| **1** | Provide the revision ID of the latest revision (3), as returned in the response to the last GET request. |
| ----- | -------------------------------------------------------------------------------------------------------- |

Response

```bash
{
    "id": "hotel_88801",
    "ok": true,
    "rev": "4-03f1ba127340e8c50c31a36279298e60" (1)
}
```

| **1** | The delete counts as the fourth revision. "ok":true indicates success. |
| ----- | ---------------------------------------------------------------------- |

Check

* [Check Document on Couchbase Server](#lbl-check-cbs) — you should now see "No Results".
* Use the API to get the document — see: [Get a Document Using the API](#lbl-crud-get).  
You should see the following response:  
```bash  
{"error":"not_found","reason":"deleted"}%  
```

## [](#ways-to-verify-sync)Ways to Verify Sync

To verify that document changes have been replicated, you can:

* Monitor the Sync Gateway revision number returned by the database endpoint ([GET /{db}/](../rest-api/rest%5Fapi%5Fpublic.md#tag/Database-Management/operation/get%5Fdb-)). The revision number increments for every change on the Sync Gateway database.
* Query a document by ID on the Sync Gateway REST API — see [Check Document on Couchbase Server](#lbl-check-cbs). Use [GET /{keyspace}/{docid}](../rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-docid) — see: [REST API Access](../rest-api/rest-api-access.md) for more.
* Query a document from the Query Workbench on the Couchbase Server Console.

## [](#next-steps)Next Steps

Now you have confirmed Sync Gateway is deployed and syncing end-to-end. You can explore more complex scenarios with confidence.

* Learn more about Sync Gateway's [Bootstrap Configuration](../configuration/configuration-schema-bootstrap.md) or how to [Sync with Couchbase Server](../sync/sync-with-couchbase-server.md)
* Implement access controls for users and data — see: [Users](../access-control/users.md), [Roles](../access-control/roles.md), and the [Sync Function](../access-control/sync-function/sync-function.md)
* Implement secure connectivity — see: [User Authentication](../security/authentication-users.md) and [TLS Certificate Authentication](../security/authentication-certs.md)
* Build more complex syncs:

  * Other Sync Gateway nodes — see: [Inter Sync Gateway Sync - Overview](../sync/sync-inter-syncgateway-overview.md)
  * Mobile devices using Couchbase Lite — see: [Sync Using App](../sync/sync-using-app.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](get-started-prepare.md)
* [Install](get-started-install.md)
* [Configure](get-started-configure.md)

###### [](#-3)

Product Information

* [Release Notes](../product-notes/release-notes.md)
* [Compatibility Matrix](../product-notes/compatibility.md)
* [Supported OS](../product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)