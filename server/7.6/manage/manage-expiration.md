---
title: Manage Expiration
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-expiration.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:manage:manage-expiration.adoc[]
---

[View original HTML](/server/7.6/manage/manage-expiration.html)

# Manage Expiration

You can have documents in your Couchbase Server Enterprise Edition automatically expire after a period of time. See [Expiration](../learn/data/expiration.md) for an overview of this feature.

## [](#set-expiration-at-the-document-level)Set Expiration at the Document Level

You can set a document to expire either when you create it or when you mutate it. The expiration value is the number of seconds in the future from the time of creation or mutation when you want the document to expire. When this period of time elapses, Couchbase Server deletes the document unless you mutate the document beforehand.

The expiration is part of the [document’s metadata](../learn/views/views-store-data.md#document-metadata). You can set the expiration when creating a document. This example uses SQL++ to create a new document in the `user_sessions` bucket and sets it to expire in one hour:

```sql++
INSERT INTO user_sessions (KEY, VALUE, OPTIONS) VALUES (
    "123456",
    {
        "username": "jsmith@example.com",
        "ip_address" : "192.168.10.20",
        "cart" : []
    },
    {
        "expiration": 3600
    }
);
```

To view the expiration of a document, query its metadata to find its `expiration` setting. This SQL++ example queries the document created by the prior example using its id.

```sql++
SELECT meta().expiration
    FROM user_sessions
    USE KEYS '123456';
```

The result of running the previous looks like this:

```json
[
  {
    "expiration": 1704819228
  }
]
```

The expiration value is the UNIX-epoch timestamp when the document expires.

You can change the document’s expiration by setting its expiration value during a mutation. The following example updates the document with new values and also resets its expiration so it expires one hour after the statement executes.

```sql++
UPDATE user_sessions AS U
    USE KEYS "123456"
    SET meta(U).expiration = 3600, cart = [{"item": "9999", "quantity": "3"}]
```

Querying the document’s metadata shows that the expiration timestamp is now later than before:

```json
[
  {
    "expiration": 1704829288
  }
]
```

### [](#mutation-expiration)Mutation’s Effect on Expiration

By default, if you mutate a document without setting its expiration, Couchbase Server automatically sets the value to 0\. This value prevents the document from expiring unless the collection or bucket has a non-zero `maxTTL` setting. For example, suppose you execute the following SQL++ statement to update the document from the previous examples:

```sql++
UPDATE user_sessions
    USE KEYS "123456"
    SET cart = [{"item": "9999", "quantity": "3"}, {"item" : "3423", "quantity" : 1}];
```

If you then query the document’s expiration metadata, you’ll find that it’s now 0:

```json
[
  {
    "expiration": 0
  }
]
```

You can prevent Couchbase Server from clearing the expiration value by using the [preserve\_expiry](../n1ql/n1ql-manage/query-settings.md#preserve%5Fexpiry) request-level parameter.

You can directly preserve a document’s expiration when mutating it. To preserve the expiration, set the expiration metadata to the document’s current expiration value. For example, you can alter the previous example statement to preserve the existing expiration value:

```sqlpp
UPDATE user_sessions AS u
    USE KEYS "123456"
    SET cart = [{"item": "9999", "quantity": "3"}, {"item" : "3423", "quantity" : 2}],
        meta(u).expiration = meta(u).expiration;
```

### [](#set-document-expiration-using-the-sdks)Set Document Expiration Using the SDKs

All SDKs let you set the document’s expiration when creating it. The SDKs have an option named `expiry` to set the expiration for a document. For example, to set the expiration of when creating a document using the Python SDK, use the `insert` method’s `expiry` parameter. The following example creates a document and sets its expiration to 1 hour.

```python
from datetime import timedelta
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import (ClusterOptions, InsertOptions)

auth = PasswordAuthenticator(
    "Administrator",
    "password",
)

cluster = Cluster('couchbase://localhost', ClusterOptions(auth))
cluster.wait_until_ready(timedelta(seconds=5))

# Prepare to insert document into the live_site collection, of the store scope in the
# user_sessions bucket.
cb = cluster.bucket("user_sessions")
live_site = cb.scope("store").collection("live_site")

# Create a document ot insert, set options.
document = {"username": "jdoe@example.com",
            "ip_address": "192.168.10.54",
            "cart": [ {"item": "4321", "quantity": "1"}]
           }
opts = InsertOptions(timeout=timedelta(seconds=5))

# Insert document and set expiration to 1 hour.
result = live_site.insert("jdoe_example_com",
                           document,
                           opts,
                           expiry=timedelta(seconds=3600))

# Normally, you'd do something useful with the response. This example
# just prints it.
print(result)
```

See the SDK documentation for more information about setting and getting the expiration of documents.

## [](#set-buckets-and-collections-to-automatically-expire-documents)Set Buckets and Collections to Automatically Expire Documents

By default, documents expire only if you explicitly set their expiration values. You can have collections and buckets set their documents to automatically expire by changing their `maxTTL` setting. Setting `maxTTL` to a non-zero value has two effects:

* Couchbase Server sets a default expiration for all documents you create or mutate in the collection or bucket unless you explicitly set the expiration to a smaller value.
* You cannot explicitly set a document’s expiration to be longer than the `maxTTL` setting. If you try to set the expiration to a value larger than the collection or bucket’s `maxTTL` setting, Couchbase Server uses the `maxTTL` value instead.

### [](#set-maxttl-using-couchbase-server-web-console)Set maxTTL Using Couchbase Server Web Console

When you create a new bucket or collection using the Web Console, you can enable the `maxTTL` setting.

To change a bucket’s `maxTTL` setting when creating or editing it:

1. When editing or adding a bucket, expand the **Advanced bucket settings** section.
2. Under **Bucket Max Time-To-Live** select **Enable**.
3. Under **Bucket Max Time-To-Live**, select or clear the **Enable** box to enable or turn off automatic expiration.
4. If you’re enabling automatic expiration, enter the number of seconds the documents should exist before expiring in the text field.

To enable expiration when creating a collection using the Web Console, enter a non-zero value in the **Add Collection to _scope name_ Scope** dialog’s **Collection Max Time-To-Live** field.

Once created, you can edit the `maxTTL` setting by clicking **Edit TTL** in the list of collections on the **Scopes & Collections** page.

### [](#set-maxttl-using-the-rest-api)Set maxTTL Using the REST API

The REST API has endpoints for creating and editing collections and buckets. These endpoints let you set a collection or bucket’s the `maxTTL` setting on creation.

The following example gets the value of `maxTTL` of a bucket named `user_sessions`, then sets it using the `/pools/default/buckets` endpoint:

```shell
curl -s -X GET -u Administrator:password \
      http://localhost:8091/pools/default/buckets/user_sessions  \
      | jq '{maxTTL: .maxTTL}'
{
  "maxTTL": 0
}

curl -X PATCH -u Administrator:password \
      http://localhost:8091/pools/default/buckets/user_sessions \
      -d maxTTL=7200

curl -s -X GET -u Administrator:password \
      http://localhost:8091/pools/default/buckets/user_sessions \
      | jq '{maxTTL: .maxTTL}'
{
  "maxTTL": 7200
}
```

See [Creating and Editing Buckets](../rest-api/rest-bucket-create.md) for more about editing buckets.

The following example creates a collection named `test_site` in the `store` scope of the `user_sessions` bucket and sets its `maxTTL` to 1 hour:

```shell
curl -s -X POST -u Administrator:password \
     http://localhost:8091/pools/default/buckets/user_sessions/scopes/store/collections \
     -d name=test_site \
     -d maxTTL=3600

{"uid":"5"}

curl -s -X GET -u Administrator:password \
     http://localhost:8091/pools/default/buckets/user_sessions/scopes \
     | jq ' .scopes[].collections | map(select(.name == "test_site"))'

[
  {
    "name": "test_site",
    "uid": "a",
    "maxTTL": 3600,
    "history": false
  }
]
[]
```

See [Creating and Editing a Collection](../rest-api/creating-a-collection.md) for more information about creating collections via the REST-API.

### [](#set-maxttl-using-the-command-line-tools-and-sdks)Set maxTTL Using the Command Line Tools and SDKs

You can set `maxTTL` for collections and buckets using the CLI and SDK.

With the couchbase-cli tool, you can set `maxTTL` using the [bucket-create](../cli/cbcli/couchbase-cli-bucket-create.md), [bucket-edit](../cli/cbcli/couchbase-cli-bucket-edit.md), and [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) commands.

When using the SDKs, look for `maxTTL` or `maxExpiry` options. For example, the NodeJS SDK `IBucketSettings` interface has a [maxExpiry](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/IBucketSettings.html#maxExpiry) property.