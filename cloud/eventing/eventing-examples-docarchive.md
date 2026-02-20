---
title: Archive Documents After Expiration
description: When a document in an existing collection is about to expire, use
  the Eventing Service to create an archived copy of that document in a
  different collection.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-docarchive.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:eventing:eventing-examples-docarchive.adoc[]
---

[View original HTML](/cloud/eventing/eventing-examples-docarchive.html)

# Archive Documents After Expiration

> When a document in an existing collection is about to expire, use the Eventing Service to create an archived copy of that document in a different collection. 

This example is similar to the [Create Documents After Expiration](eventing-examples-docexpiry.md) example, but has the following differences:

* It archives a perfect copy in the target collection
* It does not log errors unless a document is missing when the callback function to archive the document is triggered
* Does not rely on a Couchbase SDK - instead, it relies on the expiry set on the source collection, where all documents have an expiration of 10 minutes from the time of their first mutation

The `OnUpdate` JavaScript handler runs whenever a document is created or mutated. The Eventing Function calls a Timer, which executes a callback function 2 minutes before a document expires and archives an identical document with the same key in a specified target bucket.

The original document in the source bucket does not change, but is deleted following the bucket’s expiration date.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Import the `tavel-sample` sample bucket.
* Create two new buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.source` and `bulk.data.target`.
* Update the `source` collection’s TTL (Time-to-Live) to **600**.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#example-archive-documents-after-expiration)Example: Archive Documents After Expiration

This example walks you through how to archive documents after they have expired.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **archive\_before\_expiry** under **Name**.
  * **Archive all documents in a collection before a document expires.** under **Description**.
  * The keyspace `bulk.data.source` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create two bindings.

  * For the first binding:

    * Select **Bucket**.
    * Enter **src** as the **Alias Name**.
    * Enter the keyspace `bulk.data.source` under **Bucket**, **Scope**, and **Collection**.
    * Select **Read Only** under **Permission**.
  * For the second binding:

    * Select **Bucket**.
    * Enter **tgt** as the **Alias Name**.
    * Enter the keyspace `bulk.data.target` under **Bucket**, **Scope**, and **Collection**.
    * Select **Read and Write** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function OnUpdate(doc, meta) {  
    // Only processes documents that have a non-zero TTL  
    if (meta.expiration == 0 ) return;  
    // Note: JavaScript Data() is in milliseconds and meta.expiration is in seconds  
    if (new Date().getTime()/1000 > (meta.expiration - 120)) {  
        // If within the 120 second limit for expiry, creates a copy now  
        // Creates a new document with the same ID in the target collection  
        // log('OnUpdate: copy src to tgt for DocId:', meta.id);  
        tgt[meta.id] = doc;  
    } else {  
        // Computes 120 seconds before the TTL (note that JavaScript Date() is in milliseconds)  
        var twoMinsPrior = new Date((meta.expiration - 120) * 1000);  
        // Creates a Timer with a context to run in the future, 120 seconds before the expiry  
        // log('OnUpdate: create Timer '+meta.expiration+' - 120, for  DocId:',  meta.id);  
        createTimer(DocTimerCallback, twoMinsPrior , meta.id, meta.id);  
    }  
}  
function DocTimerCallback(context) {  
    // This context is the key to the document that expires in 120 seconds  
    var doc = src[context];  
    if (doc) {  
        // Creates a new document with the same ID in the target collection  
        // log('DocTimerCallback: copy src to tgt for DocId:', context);  
        tgt[context] = doc;  
    } else {  
        log('DocTimerCallback: issue missing value for DocId:', context);  
    }  
}  
```
8. Click **Create function** to create your Eventing Function.

The `OnUpdate` handler creates a Timer that fires 2 minutes before the document’s expiration time.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **archive\_before\_expiry**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

### [](#insert-documents-into-source-bucket)Insert Documents into Source Bucket

To insert documents into your **source** bucket:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **travel-sample** as the bucket and **\_default** as the scope.
3. In the code editor, enter the following query to locate a large set of data in the sample bucket:  
```sqlpp  
SELECT COUNT(*) FROM `travel-sample`.`_default`.`_default` where type = 'airport'  
```
4. Click **Run** to run the query.
5. In the code editor, replace the previous query with the following query to insert documents from the **\_default** collection of the **travel-sample** bucket into the **source** collection you created earlier:  
```sqlpp  
INSERT INTO `bulk`.`data`.`source`(KEY _k, VALUE _v)  
    SELECT META().id _k, _v FROM `travel-sample`.`_default`.`_default` _v WHERE type="airport";  
```
6. Click **Run** to run the query.
7. Go to **Data Tools** **Eventing**.
8. Click the **archive\_before\_expiry** function. The number under **Successes** should be 1968, which is the same number of documents inserted into the **source** collection from the **\_default** collection of the **travel-sample** bucket.

### [](#check-document-archival)Check Document Archival

To check that your Eventing Function is running properly and archiving documents:

1. Go to **Data Tools** **Documents**.
2. Expand the **rr100** bucket and the **eventing** scope. The **metadata** collection should have 1280 documents in it that are related to your Eventing Function, and 4192 documents that are related to active Timers.
3. Expand the **bulk** bucket and the **data** scope. The **source** collection should have 1968 documents in it, inserted through the SQL++ query earlier.
4. Wait a few minutes and check the **Documents** tab again. The Timer has fired and executed the `DocTimerCallback` function, which archives the documents from the **source** collection into the **target** collection. You should see the following:

  * 1968 documents in the **source** collection.
  * 1968 documents in the **target** collection.
5. Go to **Data Tools** **Eventing**.
6. Click the **archive\_before\_expiry** function. The number under **Successes** should have doubled to 3936.

If you wait a few more minutes until the 120 second expiry window is reached, the documents inside the **source** collection are no longer accessible because of the collection’s pre-defined TTL. The 1968 archived documents are still in the **target** collection, but the original documents in the **source** collection have expired.