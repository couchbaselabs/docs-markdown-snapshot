---
title: Cascade Delete Documents
description: Use the Eventing Service to perform cascade delete operations on
  your documents.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-cascade-delete.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:eventing:eventing-examples-cascade-delete.adoc[]
---

[View original HTML](/cloud/eventing/eventing-examples-cascade-delete.html)

# Cascade Delete Documents

> Use the Eventing Service to perform cascade delete operations on your documents. 

When you delete a user from Couchbase Capella, you can use Eventing Functions to delete all documents associated with that deleted user.

The `OnDelete` handler listens to mutations or data changes within a specified user’s source collection. When you delete a user, the Eventing Function executes its JavaScript code to remove the deleted user and all of their associated data.

Unlike the similar scriptlet [cascadeKvDeleteWithDoc](eventing-handler-cascadeKvDeleteWithDoc.md), which uses KV or the Data Service, the example on this page uses SQL++.

## [](#prerequisites)Prerequisites

Before trying out the example on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.users` and `bulk.data.transactions`.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#example-cascade-delete-documents)Example: Cascade Delete Documents

This example walks you through how to create an Eventing Function to cascade delete documents. Whenever you delete a user from your `users` collection, the Function automatically deletes all transactions in the `transactions` collection that are associated with the deleted user.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **delete\_orphaned\_txns** under **Name**.
  * **Delete orphaned transactions from the `bulk.data.transactions` collection when the `user_id` is greater than or equal to 100.** under **Description**.
  * The keyspace `bulk.data.users` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create the following binding:

  * Select **Bucket**.
  * Enter **src\_user** as the **Alias Name**.
  * Enter the keyspace `bulk.data.users` under **Bucket**, **Scope**, and **Collection**.
  * Select **Read Only** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function OnUpdate(doc, meta) {  
    log('OnUpdate NOOP id: ' + meta.id + ' document:',doc);  
}  
function OnDelete(meta) {  
    // Ignores all keys not matching "user_#" and allows other types in the source collection  
    if ((meta.id).startsWith("user_") == false) return;  
    // Implements a contrived filter and keeps all user transactions where the user_id > 100  
    var id = meta.id;  
    var numeric_id = parseInt(id.substring(5));  
    if(!isNaN(numeric_id) && numeric_id >= 100) {  
       try  {  
            DELETE FROM bulk.data.transactions WHERE user_id = $numeric_id;  
            log('OnDelete: removed orphaned transactions for:', id);  
       } catch(e) {  
           log('OnDelete: Exception:', e)  
       }  
    } else {  
        log('OnDelete: user_id < 100, kept orphaned transactions for:', id);  
    }  
}  
```
8. Click **Create function** to create your Eventing Function.

The `OnDelete` handler checks if the `user_id` is greater than or equal do 100, and then triggers a SQL++ query to delete all user-related information.

The `OnDelete` handler also checks if the orphaned transactions have been removed and logs the result to the Function log file.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **delete\_orphaned\_txns**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

### [](#create-users-transactions-and-indexes)Create Users, Transactions, and Indexes

To create new users and transactions:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket and **data** as the scope.
3. In the code editor, enter the following query to create users:  
```sqlpp  
INSERT INTO `bulk`.`data`.`users` (KEY,VALUE)  
    VALUES ( "user_50",  { "user_id":  50, "name": "jeff shoemaker", "age": "77"} ),  
    VALUES ( "user_100", { "user_id": 100, "name": "john doe",       "age": "30"} ),  
    VALUES ( "user_101", { "user_id": 101, "name": "frank smith",    "age": "20"} ),  
    VALUES ( "user_102", { "user_id": 102, "name": "jenny jones",    "age": "47"} ),  
    VALUES ( "user_103", { "user_id": 103, "name": "jerry springer", "age": "28"} );  
```
4. Click **Run** to run the query and insert the new users into the `users` collection.
5. In the code editor, replace the previous query with the following query to create transactions:  
```sqlpp  
INSERT INTO  `bulk`.`data`.`transactions` (KEY,VALUE)  
    VALUES ( "txid_999",  { "user_id":  50, "item": "vitamins", "price": 2.99} ),  
    VALUES ( "txid_1000", { "user_id": 100, "item": "milk", "price": 3.50} ),  
    VALUES ( "txid_1001", { "user_id": 100, "item": "cheese", "price": 2.50} ),  
    VALUES ( "txid_1002", { "user_id": 100, "item": "beer", "price": 7.89} ),  
    VALUES ( "txid_1003", { "user_id": 100, "item": "pizza", "price": 12.53} ),  
    VALUES ( "txid_1004", { "user_id": 101, "item": "lettuce", "price": 1.30} ),  
    VALUES ( "txid_1005", { "user_id": 101, "item": "salad dressing", "price": 4.15} ),  
    VALUES ( "txid_1006", { "user_id": 102, "item": "chicken", "price": 4.32} ),  
    VALUES ( "txid_1007", { "user_id": 103, "item": "steak", "price": 6.53} );  
```
6. Click **Run** to run the query and insert the new transactions into the `transactions` collection.
7. In the code editor, replace the previous query with the following query to create indexes:  
```sqlpp  
CREATE PRIMARY INDEX `def_primary` ON  `bulk`.`data`.`users`;  
CREATE PRIMARY INDEX `transactions` ON  `bulk`.`data`.`transactions`;  
```
8. Click **Run** to run the query and create a `def_primary` index and a `transactions` index.

Before testing the Eventing Function against your data, you can check if your users and transactions have been created correctly:

1. In the query code editor, enter the following query and click **Run** to return the list of users:  
```sqlpp  
SELECT * FROM  `bulk`.`data`.`users` ORDER BY user_id;  
```
2. Replace the previous query with the following query and click **Run** to return the list of transactions:  
```sqlpp  
SELECT * FROM  `bulk`.`data`.`transactions` ORDER BY user_id;  
```
3. Replace the previous query with the following query and click **Run** to count the number of users and transactions in your `data` scope:  
```sqlpp  
SELECT count(*) FROM `bulk`.`data`.`users`;  
SELECT count(*) FROM `bulk`.`data`.`transactions`;  
```

### [](#delete-a-user)Delete a User

To delete a user:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.users` in the **Get documents from** list to return the users you created in the previous step.
3. Click the **Delete** icon next to **user\_100**.
4. In the **Delete Document** dialog, enter **delete** and click **Delete document**.

The list of users no longer includes **user\_100**.

### [](#check-the-eventing-function-log)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **delete\_orphaned\_txns** Eventing Function. You should see the line `"OnDelete: removed orphaned transactions for:" "user_100"`.

### [](#delete-all-users)Delete All Users

To delete all users:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket and **data** as the scope.
3. In the code editor, enter the following query to delete all users:  
```sqlpp  
DELETE FROM `bulk`.`data`.`users`;  
```
4. Click **Run** to run the query and delete all users.

To confirm that all users and all data associated with the users have been deleted, enter the following query in the code editor and click **Run**:

```sqlpp
SELECT count(*) FROM `bulk`.`data`.`users`;
SELECT count(*) FROM `bulk`.`data`.`transactions`;
```

This query returns no users and but it returns one transaction.

To find out which user this one transaction is associated with, enter the following query in the code editor and click **Run**:

```sqlpp
SELECT * FROM `bulk`.`data`.`transactions`;
```

This query returns information related to the transaction, which is associated with `user_50`.

### [](#check-the-eventing-function-log-again)Check the Eventing Function Log Again

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **delete\_orphaned\_txns** Eventing Function. You should see the following lines:

2024-05-06T22:35:03.958+00:00 [INFO] "OnDelete: user_id < 100, kept orphaned transactions for:" "user_50"
2024-05-06T22:35:03.958+00:00 [INFO] "OnDelete: removed orphaned transactions for:" "user_103"
2024-05-06T22:35:03.953+00:00 [INFO] "OnDelete: removed orphaned transactions for:" "user_102"
2024-05-06T22:35:03.953+00:00 [INFO] "OnDelete: removed orphaned transactions for:" "user_101"

The log shows that all transactions from `user_103`, `user_102`, and `user_101` have been removed because of the Eventing Function business logic, which deletes orphaned transactions from users with IDs greater than or equal to 100\. One transaction from `user_50` has been kept due to the user ID being less than 100.