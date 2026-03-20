---
title: Cancel or Overwrite a Timer
description: Create, cancel, and overwrite Timers.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-cancel-overwrite-timer.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-examples-cancel-overwrite-timer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-examples-cancel-overwrite-timer.html)

# Cancel or Overwrite a Timer

> Create, cancel, and overwrite Timers. 

The `OnUpdate` JavaScript handler listens to mutations or data changes within a specified source collection. When you create or modify data in the source collection, the Eventing Function executes its JavaScript code.

The Timer callback function relies on a control document which, if mutated, controls whether a Timer is created, cancelled, or overwritten.

This page contains the following:

* An example where a control document is created or mutated, which creates a Timer. This Timer fires every 60 seconds and writes a document to another collection. The original document in the source collection does not change.
* An example where a control document is mutated, which cancels any existing Timer with a reference that matches the control document’s `meta.id`.
* An example where a control document is mutated, which overwrites any existing Timer with a reference that matches the control document’s `meta.id`. This is similar to cancelling a Timer that already exists, and then creating a new Timer that fires 60 seconds after it has been overwritten.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.source` and `bulk.data.target`.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#setup)Setup

Before following the examples on this page, you must set up a control document and an Eventing Function.

### [](#create-the-control-document)Create the Control Document

To create the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click **Create Document**.
4. In the **Document ID** field, enter **type\_of\_interest::1**.
5. Replace the JSON text with the following:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": false,  
  "cancel_timer": false,  
  "overwrite_timer": false,  
  "a_number": 1  
}  
```
6. Click **Save** to create the document.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **cancel\_overwrite\_timer** under **Name**.
  * **Create, cancel, and overwrite Timers.** under **Description**.
  * The keyspace `bulk.data.source` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create the following binding:

  * Select **Bucket**.
  * Enter **tgt\_col** as the **Alias Name**.
  * Enter the keyspace `bulk.data.target` under **Bucket**, **Scope**, and **Collection**.
  * Select **Read and Write** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function DocTimerCallback(context) {  
   log('From DocTimerCallback: timer fired', context);  
   // Creates a new document in another collection  
   tgt_col[context.docId] = context; // upserts the context as our new document  
}  
function OnUpdate(doc,meta) {  
   // Filters mutations of interest  
   if (doc.type != 'type_of_interest') return;  
   // Looks at key conditions to decide what to do  
   if (doc.needed_condition === true && doc.cancel_timer === false) {  
       if (doc.overwrite_timer === true) {  
         log('From OnUpdate: overwriting timer with same reference', meta.id);  
       } else {  
         log('From OnUpdate: creating timer', meta.id);  
       }  
       // Creates a timestamp 60 seconds from now  
       var oneMinuteFromNow = new Date(); // Gets current time & add 60 seconds to it  
       oneMinuteFromNow.setSeconds(oneMinuteFromNow.getSeconds() + 60);  
       // Creates a document to use as the context  
       var context = {docId : meta.id, random_text : "arbitrary text", "tmr_time_to_fire": oneMinuteFromNow};  
       createTimer(DocTimerCallback, oneMinuteFromNow, meta.id, context);  
    }  
    if (doc.cancel_timer === true && doc.overwrite_timer === false) {  
       // Cancels an existing timer (if it is active) by reference meta.id  
       if (cancelTimer(DocTimerCallback, meta.id)) {  
           log('From OnUpdate: cancel request, timer was canceled',meta.id);  
       } else {  
           log('From OnUpdate: cancel request, no such timer may have fired',meta.id);  
       }  
    }  
    if (doc.cancel_timer === true && doc.overwrite_timer === true) {  
        log('From OnUpdate: both cancel and overwrite, will ignore',meta.id);  
    }  
}  
```
8. Click **Create function** to create your Eventing Function.

When a change happens to the data inside the source collection, the `OnUpdate` handler targets the control document by ignoring all documents that do not have a `doc.type` of `type_of_interest`. It then uses the fields `needed_condition`, `cancel_timer`, and `overwrite_timer` to determine which action to take:

* If `needed_condition` is true but both `cancel_timer` and `overwrite_timer` are false, the Eventing Function creates a Timer that fires 60 seconds into the future.
* If both `needed_condition` and `cancel_timer` are true, the Eventing Function cancels the existing Timer.
* If both `needed_condition` and `overwrite_timer` are true, the Eventing Function overwrites the existing Timer with a new Timer that fires 60 seconds into the future.
* If both `cancel_timer` and `overwrite_timer` are true, the Eventing Function throws an error and nothing happens.

When a Timer created by the Eventing Function fires, the callback `DocTimerCallback` executes and writes a new document in the target collection with the same key as the document in the source collection.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **cancel\_overwrite\_timer**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

## [](#example-create-a-timer-and-allow-the-timer-to-fire)Example: Create a Timer and Allow the Timer to Fire

This example walks you through how to create a Timer and have the Timer fire.

### [](#edit-the-control-document)Edit the Control Document

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **type\_of\_interest::1** to open the **Edit Document** dialog.
4. Change `needed_condition` to `true`:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": true,  
  "cancel_timer": false,  
  "overwrite_timer": false,  
  "a_number": 1  
}  
```
5. Click **Save** to create a mutation.

The document mutation causes the Eventing Function to create a Timer.

### [](#check-the-eventing-function-log)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **cancel\_overwrite\_timer** Eventing Function. You should see the line `"From OnUpdate: creating timer" "type_of_interest::1"` in the debug log.
3. Wait a few minutes and click the **Log** icon again. The Timer should have fired and executed the `DocTimerCallback` callback, and you should see the line `"From DocTimerCallback: timer fired" {"docId":"type_of_interest::1 ","random_text":"arbitrary text","tmr_time_to_fire":"2022-05-10T23:07:54.226Z"}` in the debug log.

### [](#check-the-results-in-the-target-collection)Check the Results in the Target Collection

To check that a new document has been created in the target collection:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.target` in the **Get documents from** list.
3. Click **type\_of\_interest::1** to open the **Edit Document** dialog. The JSON document includes data written by the Timer’s callback.  
```json  
{  
  "docId": "type_of_interest::1",  
  "random_text": "arbitrary text",  
  "tmr_time_to_fire": "2022-05-10T23:07:54.226Z"  
}  
```
4. Close the **Edit Document** dialog.
5. Click the **Delete** icon next to **type\_of\_interest::1**.
6. In the **Delete Document** dialog, enter **delete** and click **Delete document**.

## [](#example-create-a-timer-and-cancel-the-timer)Example: Create a Timer and Cancel the Timer

This example walks you through how to create a Timer and cancel the Timer.

### [](#edit-the-control-document-2)Edit the Control Document

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **type\_of\_interest::1** to open the **Edit Document** dialog.
4. Change `a_number` to `2`:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": true,  
  "cancel_timer": false,  
  "overwrite_timer": false,  
  "a_number": 2  
}  
```
5. Click **Save** to create a mutation.

The document mutation causes the Eventing Function to create a Timer.

### [](#check-the-eventing-function-log-2)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **cancel\_overwrite\_timer** Eventing Function. You should see the line `"From OnUpdate: creating timer" "type_of_interest::1"` in the debug log.

### [](#edit-the-control-document-again)Edit the Control Document Again

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **type\_of\_interest::1** to open the **Edit Document** dialog.
4. Change `cancel_timer` to `true`:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": true,  
  "cancel_timer": true,  
  "overwrite_timer": false,  
  "a_number": 2  
}  
```
5. Click **Save** to create a mutation.

### [](#check-the-eventing-function-log-again)Check the Eventing Function Log Again

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **cancel\_overwrite\_timer** Eventing Function. You should see the line `"From OnUpdate: cancel request, timer was canceled" "type_of_interest::1"` in the debug log.

The Timer has been cancelled and did not fire.

## [](#example-create-a-timer-and-overwrite-the-timer)Example: Create a Timer and Overwrite the Timer

This example walks you through how to create a Timer and overwrite the Timer.

### [](#edit-the-control-document-3)Edit the Control Document

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **type\_of\_interest::1** to open the **Edit Document** dialog.
4. Change `cancel_timer` to `false`:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": true,  
  "cancel_timer": false,  
  "overwrite_timer": false,  
  "a_number": 2  
}  
```
5. Click **Save** to create a mutation.

The document mutation causes the Eventing Function to create a Timer.

### [](#check-the-eventing-function-log-3)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **cancel\_overwrite\_timer** Eventing Function. You should see the line `"From OnUpdate: creating timer" "type_of_interest::1"` in the debug log.

### [](#edit-the-control-document-again-2)Edit the Control Document Again

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **type\_of\_interest::1** to open the **Edit Document** dialog.
4. Change `overwrite_timer` to `true`:  
```json  
{  
  "type": "type_of_interest",  
  "id": 1,  
  "needed_condition": true,  
  "cancel_timer": true,  
  "overwrite_timer": true,  
  "a_number": 2  
}  
```
5. Click **Save** to create a mutation.

### [](#check-the-eventing-function-log-again-2)Check the Eventing Function Log Again

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **cancel\_overwrite\_timer** Eventing Function. You should see the line `"From OnUpdate: overwriting timer with same reference" "type_of_interest::1"` in the debug log.
3. Wait a few minutes and click the **Log** icon again. The Timer should have fired and executed the `"From DocTimerCallback: timer fired" {"docId":"type_of_interest::1","random_text":"arbitrary text","tmr_time_to_fire":"2022-05-10T23:13:57.125Z"}` in the debug log.

### [](#check-the-results-in-the-target-collection-2)Check the Results in the Target Collection

To check that a new document has been created in the target collection:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.target` in the **Get documents from** list.
3. Click **type\_of\_interest::1** to open the **Edit Document** dialog. The JSON document includes data written by the Timer’s callback.  
```json  
{  
  "docId": "type_of_interest::1 ",  
  "random_text": "arbitrary text",  
  "tmr_time_to_fire": "2022-05-10T23:13:57.125Z"  
}  
```
4. Close the **Edit Document** dialog.
5. Click the **Delete** icon next to **type\_of\_interest::1**.
6. In the **Delete Document** dialog, enter **delete** and click **Delete document**.