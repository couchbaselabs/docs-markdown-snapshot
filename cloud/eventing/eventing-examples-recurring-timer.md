---
title: Create a Recurring Timer
description: Create a Timer that continues to execute until you manually cancel it.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-recurring-timer.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/eventing/eventing-examples-recurring-timer.html)

# Create a Recurring Timer

> Create a Timer that continues to execute until you manually cancel it. 

The `OnUpdate` JavaScript handler listens to mutations or data changes within a specified source collection. When you create or modify data in the source collection, the Eventing Function executes its JavaScript code.

The Timer callback function relies on a control document which, if mutated, controls whether a recurring Timer is created or cancelled.

This page contains the following:

* An example where a control document is created or mutated, which creates a Timer. This Timer fires every 30 seconds and writes a document to the source collection. The original document in the source collection does not change. The Timer continues to execute until you cancel it.
* An example where a control document is mutated, which cancels any existing Timer with a reference that matches the control document’s `meta.id`. This has no effect if the Timer created has already fired.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create one keyspace called `bulk.data.source`.
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
4. In the **Document ID** field, enter **recurring\_timer::1**.
5. Replace the JSON text with the following:  
```json  
{  
  "type": "recurring_timer",  
  "id": 1,  
  "active": false  
}  
```
6. Click **Save** to create the document.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **recurring\_timer** under **Name**.
  * **Test recurring timers.** under **Description**.
  * The keyspace `bulk.data.source` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create the following binding:

  * Select **Bucket**.
  * Enter **src\_col** as the **Alias Name**.
  * Enter the keyspace `bulk.data.source` under **Bucket**, **Scope**, and **Collection**.
  * Select **Read and Write** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function CreateRecurringTimer(context) {  
    log('From CreateRecurringTimer: creating timer', context.mode, context.id);  
    // Creates a timestamp 30 seconds from now  
    var thirtySecFromNow = new Date(); // Gets current time & adds 30 seconds to it  
    thirtySecFromNow.setSeconds(thirtySecFromNow.getSeconds() + 30);  
    // Creates a document to use as the context  
    createTimer(RecurringTimerCallback, thirtySecFromNow, context.id, context);  
}  
function RecurringTimerCallback(context) {  
    log('From RecurringTimerCallback: timer fired', context);  
    // Re-executes the timer ASAP to ensure the Timer keeps running in case  
    // errors or script timeouts happen in later "recurring work"  
    CreateRecurringTimer({ "id": context.id, "mode": "via_callback" });  
    // Any sort of recurring work happens here and updates a date_stamp in a document  
    src_col["cur_" + context.id] = { "last_update": new Date() };  
}  
function OnUpdate(doc, meta) {  
    // Filters mutations of interest  
    if (doc.type !== 'recurring_timer') return;  
    if (doc.active === false) {  
        if (cancelTimer(RecurringTimerCallback, meta.id)) {  
            log('From OnUpdate: canceled active Timer, doc.active',  
                doc.active, meta.id);  
        } else {  
            log('From OnUpdate: no active Timer to cancel, doc.active',  
                doc.active, meta.id);  
        }  
    } else {  
        log('From OnUpdate: create/overwrite doc.active', doc.active, meta.id);  
        CreateRecurringTimer({  "id": meta.id, "mode": "via_onupdate" });  
    }  
}  
```
8. Click **Create function** to create your Eventing Function.

When a change happens to the data inside the source collection, the `OnUpdate` handler targets the control document by ignoring all documents that do not have a `doc.type` of `recurring_timer`. It then uses the field `active` to determine which action to take:

* If `active` is true, the Eventing Function creates a series of Timers that fire 30 seconds into the future.
* If `active` is false, the Eventing Function cancels any existing Timers.

When a Timer created by the Eventing Function fires, the callback `RecurringTimerCallback` executes and writes a new document in the source collection with a similar key as another document in the source collection.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **recurring\_timer**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

## [](#example-create-a-recurring-timer-and-allow-the-timer-to-fire-and-rearm)Example: Create a Recurring Timer and Allow the Timer to Fire and Rearm

This example walks you through how to create a Timer, have the Timer fire, and then have the Timer rearm.

### [](#edit-the-control-document)Edit the Control Document

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **recurring\_timer::1** to open the **Edit Document** dialog.
4. Change `active` to `true`:  
```json  
{  
  "type": "recurring_timer",  
  "id": 1,  
  "active": true  
}  
```
5. Click **Save** to create a mutation.

The document mutation causes the Eventing Function to create a Timer.

### [](#check-the-eventing-function-log)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **recurring\_timer** Eventing Function. You should see the following in the debug log:  
2021-07-18T10:50:37.879-07:00 [INFO] "From OnUpdate: create/overwrite doc.active" true "recurring_timer::1"  
2021-07-18T10:50:37.879-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_onupdate" "recurring_timer::1"  
2021-07-18T10:50:06.147-07:00 [INFO] "From OnUpdate: no active Timer to cancel, doc.active" false "recurring_timer::1"
3. Wait a few minutes and click the **Log** icon again. The Timer should have fired and executed the `RecurringTimerCallback` callback, and you should see the following in the debug log:  
2021-07-18T10:54:04.705-07:00 [INFO] "From RecurringTimerCallback: timer fired" {"id":"recurring_timer::1","mode":"via_callback"}  
2021-07-18T10:54:04.705-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_callback" "recurring_timer::1"  
2021-07-18T10:53:22.712-07:00 [INFO] "From RecurringTimerCallback: timer fired" {"id":"recurring_timer::1","mode":"via_callback"}  
2021-07-18T10:53:22.712-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_callback" "recurring_timer::1"  
2021-07-18T10:52:40.708-07:00 [INFO] "From RecurringTimerCallback: timer fired" {"id":"recurring_timer::1","mode":"via_callback"}  
2021-07-18T10:52:40.708-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_callback" "recurring_timer::1"  
2021-07-18T10:51:58.703-07:00 [INFO] "From RecurringTimerCallback: timer fired" {"id":"recurring_timer::1","mode":"via_callback"}  
2021-07-18T10:51:58.703-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_callback" "recurring_timer::1"  
2021-07-18T10:51:16.713-07:00 [INFO] "From RecurringTimerCallback: timer fired" {"id":"recurring_timer::1","mode":"via_onupdate"}  
2021-07-18T10:51:16.713-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_callback" "recurring_timer::1"  
2021-07-18T10:50:37.879-07:00 [INFO] "From OnUpdate: create/overwrite doc.active" true "recurring_timer::1"  
2021-07-18T10:50:37.879-07:00 [INFO] "From CreateRecurringTimer: creating timer" "via_onupdate" "recurring_timer::1"  
2021-07-18T10:50:06.147-07:00 [INFO] "From OnUpdate: no active Timer to cancel, doc.active" false "recurring_timer::1"

### [](#check-the-results-in-the-source-collection)Check the Results in the Source Collection

To check that a new document has been created in the source collection:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the new document **cur\_recurring\_timer::1** to open the **Edit Document** dialog. The JSON document includes data written by the Timer’s callback.  
```json  
{  
  "last_update": "2021-07-18T17:56:10.707Z"  
}  
```
4. Click **Cancel** to close the editor.

The Eventing Function you created writes a timestamp to the **cur\_recurring\_timer::1** document every 30 seconds.

## [](#example-cancel-the-recurring-timer)Example: Cancel the Recurring Timer

This example walks you through how to cancel the recurring Timer.

### [](#edit-the-control-document-2)Edit the Control Document

To edit the control document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click the control document **recurring\_timer::1** to open the **Edit Document** dialog.
4. Change `active` to `false`:  
```json  
{  
  "type": "recurring_timer",  
  "id": 2,  
  "active": false  
}  
```
5. Click **Save** to create a mutation.

The document mutation causes the Eventing Function to create a Timer.

### [](#check-the-eventing-function-log-2)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **recurring\_timer** Eventing Function. You should see the line `"From OnUpdate: canceled active Timer, doc.active" false "recurring_timer::1"` in the debug log.

The recurring Timer has been cancelled.