---
title: Improve Document Searchability
description: Make searching documents easier by adding new attributes to existing documents.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-example-data-enrichment.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:eventing:eventing-example-data-enrichment.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-example-data-enrichment.html)

# Improve Document Searchability

> Make searching documents easier by adding new attributes to existing documents. 

Legacy document sets can contain attributes with formats that are difficult to search on. To make searching easier, you can use Eventing Functions to duplicate and add new attributes to your documents.

The `OnUpdate` JavaScript handler listens to mutations or data changes within a specified source collection. When you create or modify data in the source collection, the Eventing Function executes its JavaScript code.

In the examples on this page, you create a document with two named fields that contain IP addresses corresponding to the beginning and the end of an address range. You then create the Eventing Function routine `get_numip_first_3_octets(ip)`, which converts each of the IP addresses to an integer and upserts them as new fields in a new or existing document.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.source` and `bulk.data.target`.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#example-create-a-new-document-in-a-target-collection)Example: Create a New Document in a Target Collection

This example walks you through how to create a new document in a target collection. This new document is a copy of the original document in the source collection, but it includes two new additional fields that contain integers that correspond to IP addresses. The original document in the source collection does not change.

### [](#create-the-original-document-in-the-source-collection)Create the Original Document in the Source Collection

To create the original document:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click **Create Document**.
4. In the **Document ID** field, enter **SampleDocument**.
5. Replace the JSON text with the following:  
```json  
{  
  "country": "AD",  
  "ip_start": "5.62.60.1",  
  "ip_end": "5.62.60.9"  
}  
```
6. Click **Save** to create the document.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **case\_enrich\_ips** under **Name**.
  * **On mutation, create a new document in a different collection with additional fields** under **Description**.
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
  log('document', doc);  
  doc["ip_num_start"] = get_numip_first_3_octets(doc["ip_start"]);  
  doc["ip_num_end"]   = get_numip_first_3_octets(doc["ip_end"]);  
  tgt[meta.id]=doc;  
}  
function get_numip_first_3_octets(ip) {  
  var return_val = 0;  
  if (ip) {  
    var parts = ip.split('.');  
    // IP Number = A x (256*256*256) + B x (256*256) + C x 256 + D  
    return_val = (parts[0]*(256*256*256)) + (parts[1]*(256*256)) + (parts[2]*256) + parseInt(parts[3]);  
    return return_val;  
  }  
}  
```
8. Click **Create function** to create your Eventing Function.

The `OnUpdate` handler specifies that, when a change happens to the data inside the bucket, the routine `get_numip_first_3_octets` runs on each on each document that contains `ip_start` and `ip_end`. This routine creates a new document, copies the data and metadata of the original document, and adds the data fields `ip_num_start` and `ip_num_end`.

These data fields contain the numeric values returned by `get_numip_first_3_octets`, which splits the IP address, converts each fragment into a numeral, and adds the numerals together to form a single value. The Eventing Function then returns this single value.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **case\_1\_enrich\_ips**.
3. Click **Deploy** to deploy your Function.

After it's deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

### [](#check-the-results-in-the-target-collection)Check the Results in the Target Collection

To check that a new document has been created in the target collection:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.target` in the **Get documents from** list.
3. Click **SampleDocument** to open the **Edit Document** dialog. The JSON document is a copy of the **SampleDocument** document you created earlier in the keyspace `bulk.data.source`, but it includes two new calculated fields `ip_num_start` and `ip_num_end`.  
```json  
{  
  "country": "AD",  
  "ip_end": "5.62.60.9",  
  "ip_start": "5.62.60.1",  
  "ip_num_start": 87964673,  
  "ip_num_end": 87964681  
}  
```

### [](#test-the-eventing-function)Test the Eventing Function

To test that your Eventing Function runs on new mutations:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click **Create Document**.
4. In the **Document ID** field, enter **AnotherSampleDocument**.
5. Replace the JSON text with the following:  
```json  
{  
  "country": "RU",  
  "ip_start": "7.12.60.1",  
  "ip_end": "7.62.60.9"  
}  
```
6. Click **Save** to create the document.
7. Select the keyspace `bulk.data.target` in the **Get documents from** list.
8. Click **AnotherSampleDocument** to open the **Edit Document** dialog. The JSON document is a copy of the **AnotherSampleDocument** document you created earlier in the keyspace `bulk.data.source`, but it includes two new calculated fields `ip_num_start` and `ip_num_end`.  
```json  
{  
  "country": "RU",  
  "ip_end": "7.62.60.9",  
  "ip_start": "7.12.60.1",  
  "ip_num_start": 118242305,  
  "ip_num_end": 121519113  
}  
```

## [](#example-update-an-existing-document-in-the-source-collection)Example: Update an Existing Document in the Source Collection

> [!NOTE]
> This example assumes that you have already created all of the documents from the first example.

Before following the steps for this example, you must undeploy the Eventing Function **case\_enrich\_ips** from the first example. To undeploy the Function, go to **DataTools** **Eventing** and click **Undeploy** in **More Options (⋮)**.

Unlike the previous example in which you created a new document in a target collection, this example walks you through how to update an existing document in the source collection. This updated document includes two new additional fields that contain integers that correspond to IP addresses.

### [](#create-an-eventing-function-2)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **case\_2\_enrich\_ips** under **Name**.
  * **On mutation, create a new document in the same collection with additional fields** under **Description**.
  * The keyspace `bulk.data.source` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create the following binding:

  * Select **Bucket**.
  * Enter **src** as the **Alias Name**.
  * Enter the keyspace `bulk.data.source` under **Bucket**, **Scope**, and **Collection**.
  * Select **Read and Write** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function OnUpdate(doc, meta) {  
  log('document', doc);  
  doc["ip_num_start"] = get_numip_first_3_octets(doc["ip_start"]);  
  doc["ip_num_end"]   = get_numip_first_3_octets(doc["ip_end"]);  
  // Write back to the source bucket  
  src[meta.id]=doc;  
}  
function get_numip_first_3_octets(ip) {  
  var return_val = 0;  
  if (ip) {  
    var parts = ip.split('.');  
    // IP Number = A x (256*256*256) + B x (256*256) + C x 256 + D  
    return_val = (parts[0]*(256*256*256)) + (parts[1]*(256*256)) + (parts[2]*256) + parseInt(parts[3]);  
    return return_val;  
  }  
}  
```
8. Click **Create function** to create your Eventing Function.

The `OnUpdate` handler specifies that, when a change happens to the data inside the bucket, the routine `get_numip_first_3_octets` runs on each on each document that contains `ip_start` and `ip_end`. This routine creates a new document, copies the data and metadata of the original document, and adds the data fields `ip_num_start` and `ip_num_end`.

These data fields contain the numeric values returned by `get_numip_first_3_octets`, which splits the IP address, converts each fragment into a numeral, and adds the numerals together to form a single value. The Eventing Function then returns this single value.

### [](#deploy-the-eventing-function-2)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **case\_2\_enrich\_ips**.
3. Click **Deploy** to deploy your Function.

After it's deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

### [](#check-the-results-in-the-source-collection)Check the Results in the Source Collection

To check that the document in the source collection has been updated:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click **SampleDocument** to open the **Edit Document** dialog. The JSON document has been updated to include the two new calculated fields `ip_num_start` and `ip_num_end`.  
```json  
{  
  "country": "AD",  
  "ip_end": "5.62.60.9",  
  "ip_start": "5.62.60.1",  
  "ip_num_start": 87964673,  
  "ip_num_end": 87964681  
}  
```

The **AnotherSampleDocument** document has also been updated to include the two new fields.

### [](#test-the-eventing-function-2)Test the Eventing Function

To test that your Eventing Function runs on new mutations:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.source` in the **Get documents from** list.
3. Click **SampleDocument** to open the **Edit Document** dialog.
4. In the JSON text, change the value of `ip_start` to `6.12.60.1`.
5. Click **Save Document**.
6. Click **SampleDocument** to open the **Edit Document** dialog again. The value of `ip_num_start` has changed to reflect the new IP.  
```json  
{  
  "country": "AD",  
  "ip_start": "6.12.60.1",  
  "ip_end": "5.62.60.9",  
  "ip_num_start": 101465089,  
  "ip_num_end": 87964681  
}  
```