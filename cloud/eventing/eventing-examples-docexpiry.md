---
title: Create Documents After Expiration
description: When a document in an existing collection is about to expire, use
  the Eventing Service to create a new document in a different collection.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-docexpiry.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-examples-docexpiry.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-examples-docexpiry.html)

# Create Documents After Expiration

> When a document in an existing collection is about to expire, use the Eventing Service to create a new document in a different collection. 

The `OnUpdate` JavaScript handler listens to mutations or data changes within a specified source collection. The Eventing Function calls a Timer, which executes a callback function before a document expires and retrieves a value from that document. This function then stores a document with the same key in a specified target collection.

The original document in the source collection does not change when its value is copied. The document is then deleted folowing the bucket’s expiration date.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.source` and `bulk.data.target`.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#example-create-a-new-document-when-a-document-expires)Example: Create a New Document When a Document Expires

This example walks you through how to create a new document whenever another document expires.

### [](#create-a-new-document)Create a New Document

You can create a test document with an expiration time in one of the following ways:

* Using a SQL++ statement in the Query Workbench
* Using the command line KV client (`cbc`)
* Using a Python or Java SDK script

* SQL++ statement
* KV client
* Python SDK script
* Java SDK script

To use a SQL++ statement in the Query Workbench:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket and **data** as the scope.
3. In the code editor, enter the following query:

```sqlpp
UPSERT INTO `bulk`.`data`.`source` (KEY, VALUE) VALUES ("SampleDocument2", {"a_key":"a_value"}, {"expiration":600});
```

For information about setting a document’s expiration time with SQL++, see [Insert a document with expiration](../n1ql/n1ql-language-reference/insert.md#insert-document-with-expiration).

The KV client method depends on your operating system.

On Linux, run the following command:

```console
/opt/couchbase/bin/cbc \
    create SampleDocument2 -V '{"a_key": "a_value"}' \
    -U couchbase://localhost/source \
    --scope=data --collection=source \
    -u Administrator -P password \
    --expiry=600
```

On macOS, run the following command:

```console
/Applications/Couchbase\ Server.app/Contents/Resources/couchbase-core/bin/cbc \
    create SampleDocument2 -V '{"a_key": "a_value"}' -U couchbase://localhost/source \
    --scope=data --collection=source \
    -u Administrator -P password \
    --expiry=600
```

If you get the error `dyld: Library not loaded` when running `cbc` on macOS, follow the instructions on the Jira ticket [MB-37768](https://issues.couchbase.com/browse/MB-37768).

On Windows, run the following command:

```console
"C:\Program Files\Couchbase\Server\bin\cbc" ^
    create SampleDocument2 -V "{'a_key': 'a_value'}" -U couchbase://localhost/source ^
    --scope=data --collection=source ^
    -u Administrator -P password ^
    --expiry=600
```

For more information about the `cbc` tool, see [Command Line Tools](../reference/command-line-tools.md).

Copy and paste the following code sample inside an executable SDK script.

Alternatively, you can:

1. Run the command `python3` to start a Python session.
2. Run the code sample without the line `#!/usr/bin/python3` to create the sample document.
3. Enter ^D to close the Python session.

```python
#!/usr/bin/python3
import sys
import couchbase.collection
import couchbase.subdocument as SD
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase.durability import ServerDurability, Durability
from datetime import timedelta

pa = PasswordAuthenticator('Administrator', 'password')
cluster = Cluster('couchbase://127.0.0.1', ClusterOptions(pa))
bucket = cluster.bucket('bulk')
collection = bucket.scope('data').collection('source')

try:
  document = dict( a_key="a_value" )
  result = collection.upsert(
    'SampleDocument2',
    document,
    expiry=timedelta(minutes=10)
  )
  print("UPSERT SUCCESS")
  print("cas result:", result.cas)
except:
  print("exception:", sys.exc_info())
```

For information about the Couchbase Python SDK, see [Start Using the Python SDK](../../python-sdk/current/hello-world/start-using-sdk.md).

Copy and paste the following code sample inside an executable SDK script.

```java
// Must use the Collections API
package com.jonstrabala;
import java.time.Duration;
import com.couchbase.client.java.*;
import com.couchbase.client.java.json.JsonObject;
import static com.couchbase.client.java.kv.UpsertOptions.upsertOptions;
public class DocExpiryTestCC {
    public static void main(String... args) throws Exception {
    	// Note, if not on the server you need to change "localhost" to your DNS name or IP
    	Cluster cluster = Cluster.connect("localhost", "Administrator", "password");
    	Bucket bucket = cluster.bucket("bulk");
    	// Collection collection = bucket.defaultCollection();
    	Collection collection = bucket.scope("data").collection("source");
    	String docID = "SampleDocument2";
    	Duration dura = Duration.ofMinutes(10);
    	try {
    		collection.upsert(
    			docID, JsonObject.create().put("a_key", "a_value"),
    			upsertOptions().expiry(dura) );
    		System.out.println("docID: " + docID + " expires in " + dura.getSeconds());
    	} catch (Exception e) {
    		System.out.println("upsert error for docID: " + docID + " " + e);
    	}
        bucket = null;
        collection = null;
    	cluster.disconnect(Duration.ofSeconds(2000));
    }
}
```

For more information about the Couchbase Java SDK, see [Start Using the Java SDK](../../java-sdk/current/hello-world/start-using-sdk.md).

You now have a document in the `source` collection with a set expiration date. This document is deleted after 600 seconds.

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **add\_timer\_before\_expiry** under **Name**.
  * **Fire a Timer before a document expires.** under **Description**.
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
    // Only processes for those documents that have a non-zero TTL  
    if (meta.expiration == 0 ) return;  
    // Gets the TTL and computes 2 minutes prior to the TTL. JavaScript Date() takes msec.  
    var twoMinsPrior = new Date((meta.expiration - 2*60) * 1000);  
    // Creates a context and then creates a timer with the context  
    var context = { docID : meta.id, expiration : meta.expiration };  
    createTimer(DocTimerCallback, twoMinsPrior , meta.id, context);  
    log('OnUpdate add Timer 2 min. prior to TTL to DocId:',  meta.id);  
}  
function DocTimerCallback(context) {  
    log('DocTimerCallback 1 on DocId:', String(context.docID));  
    // Creates a new document with the same ID, but in the target collection  
    tgt[context.docID] = "To Be Expired in 2 min., Key's Value is:" + JSON.stringify(src[context.docID]);  
    log('DocTimerCallback 2 src expiry:', new Date(context.expiration  * 1000));  
    log('DocTimerCallback 3 tgt archive via Key:', String(context.docID));  
}  
```
8. Click **Create function** to create your Eventing Function.

The `OnUpdate` handler creates a Timer that fires 2 minutes before the document’s expiration time.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

Deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **add\_timer\_before\_expiry**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

### [](#check-the-eventing-function-log)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **add\_timer\_before\_expiry** Eventing Function. You should see the line `"OnUpdate add Timer 2 min. prior to TTL to DocId:" "SampleDocument2"`.

Wait a few minutes and check the Eventing Function log again. The Timer has fired and executed the `DocTimerCallback` function 2 minutes before the TTL was scheduled. You should see the following lines in the log:

2024-05-07T21:01:15.386+00:00 [INFO] "DocTimerCallback 3 tgt archive via Key:" "SampleDocument2"
2024-05-07T21:01:15.386+00:00 [INFO] "DocTimerCallback 2 src expiry:" "2024-05-07T21:02:05.000Z"
2024-05-07T21:01:15.236+00:00 [INFO] "DocTimerCallback 1 on DocId:" "SampleDocument2"
2024-05-07T21:01:06.821+00:00 [INFO] "OnUpdate add Timer 2 min. prior to TTL to DocId:" "SampleDocument2"

> [!NOTE]
> The document had an expiration time of 600 seconds, or 10 minutes. The `DocTimerCallback` function fires a Timer 2 minutes before the initial expiration time.

The final result is a new document named `SourceDocument2` which contains a copy of the data from the original document. This new document is written to the `target` collection.

The original document in the `source` collection is deleted after it reaches its expiration time of 10 minutes. The new document in the `target` collection is not deleted.