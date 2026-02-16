[View original HTML](/sync-gateway/current/access-control/access-control-how-use-xattrs-for-access-grants.html)

> How to set access grants using extended attributes (xattrs).  
> Here we introduce the concept of _XATTRS_ for access grants and their role in assuring secure access control within _Sync Gateway_.

_Related Topics_: [Concepts](access-control-concepts.md) | [How-to](access-control-how.md) | [Sync Function](sync-function/sync-function.md) | [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

_Related Concepts_: [Access control Model](access-control-model.md) | [Control Document Access](access-control-how-control-document-access.md)

## [](#introduction)Introduction

Access grant information such as [Channels](channels.md) and [Roles](roles.md) can be derived or specified as a property within the document body. In this case, the document content itself is used to govern access and routing.

Alternatively, a more secure option is to store this information in user XATTRs for specifying channels and roles.

## [](#why-use-xattrs)Why use XATTRS

XATTRs can be used to hold data used for document routing and access control \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. When retrieved by the Sync Function, this data can be used to drive access grants. This approach has a few benefits:

* It provide an added level of security, users can no longer identify the channels and users a document is available to by reading its contents, because the information is in metadata that is inaccessible to them
* Separation of concerns. By separating access grant metadata from document contents, changes to access grants will not create a new document revision that is subsequently pushed to a client

Sync Gateway exposes a single user-definable XATTR for this purpose. Learn how to configure it in [Configuration](#lbl-config) and how to use it in [Setting](#lbl-set) and [Use XATTRs in a Sync Function](#lbl-using).

## [](#lbl-config)Configuration

Name the XATTR (see: [user\_xattr\_key](../configuration/configuration-schema-database.md#databases-this%5Fdb-user%5Fxattr%5Fkey)) to be used for channel routing by defining it using the Admin REST API’s [Database Configuration](../configuration/configuration-schema-database.md) — see: [Example 1](#ex-config).

The actual value of this XATTR can be anything that enables the Sync Function to make an appropriate access grant. Its data type can be string, array, object — any valid JSON that meets the required use case.

Example 1\. Define the User Extended Attribute Key

This example uses the Admin REST API to specify the required XATTR name as `channelXattr` on the database `hotels`.

* CURL
* HTTP

```json
curl -X POST 'http://localhost:4985/hotels/_config' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_xattr_key": "channelXattr" (1)
    }
}'
```

```http
POST /hotels/_config HTTP/1.1
Host: http://localhost:4985
Accept: application/json
Content-Type: application/json
Content-Length: 999

{
  “user_xattr_key”: “channelXattr” (1)
}
```

| **1** | Here _channelXattr_ is set as the name of the XATTR designated to hold channel routing information. |
| ----- | --------------------------------------------------------------------------------------------------- |

## [](#lbl-set)Setting

You can set and maintain the value of the XATTR using a Couchbase Server SDK API. You cannot set it using the Sync Gateway REST API.

For an example of setting the value of the XATTR using the C# SDK, see [Example 2](#ex-cbs-metadata-setting), this can be easily translated to any of the available SDK languages. See [Example 3](#ex-cbs-metadata) for an example of the metadata model.

Example 2\. Set XATTR using Couchbase Server SDK

```C#
using System;
using System.Threading.Tasks;
using Couchbase;
using Couchbase.KeyValue; (1)


namespace examples
{

    class Program
    {
        static async Task Main(string[] args)
        {
            // Set scope - cluster, bucket and collection
            var cluster =
                    await Cluster.ConnectAsync(
                                    "couchbase://localhost",
                                    "Administrator",
                                    "password");


            var bucket = await cluster.BucketAsync("travel-sample");
            var collection = bucket.DefaultCollection();

            // Set required  user_xattr_key name and value
            var our_user_xattr_key_name = "channelXattr"; (2)
            String[] channelXattrValue =
                {"channel1","channel3", "useradmin" }; (3)

            var ourDocumentType = "hotel";
            var documentKey = "";

            // Find our documents and get their ids
            var queryResult =
               await cluster.QueryAsync<dynamic>(
                   "select meta().id from `travel-sample`.`_default`.`_default` h where h.type = $1",
                        new Couchbase.Query.QueryOptions().Parameter(ourDocumentType)); (4)
            await foreach (var row in queryResult)
            {
                documentKey = row.id;
                Console.WriteLine("Working with document id: {0} ",
                                    documentKey);

                // Check if the document has an existing
                // user_xattr_key and update or insert new value
                var result =
                    await collection.LookupInAsync(
                            documentKey,
                            specs => specs.Exists(
                                path: our_user_xattr_key_name,
                                isXattr: true)
                            ); (5)

                if (result.Exists(0))
                {
                    // Update xattr for retrieved Id
                    await collection.MutateInAsync(
                            documentKey,
                            specs => specs.Upsert(
                                path: our_user_xattr_key_name, (6)
                                value: channelXattrValue, (7)
                                isXattr: true)); (8)

                    Console.Write("Updated Existing user_xattr_key: {0} to this value: {1}\n",
                        our_user_xattr_key_name,
                        string.Join(", ", channelXattrValue));

                }
                else
                {
                    // Insert xattr for retrieved id
                    await collection.MutateInAsync(
                            documentKey,
                            specs => specs.Insert(
                                path: our_user_xattr_key_name, (9)
                                value: channelXattrValue, (10)
                                isXattr: true)); (11)

                    Console.Write("Inserted New user_xattr_key: {0} with value {1}\n",
                        our_user_xattr_key_name,
                        string.Join(", ", channelXattrValue));

                }

            }
            Console.WriteLine("Completed Changes\n");
        }
    }
}
```

| **1**  | This is required to make the MutateInSpec class available, providing access to sub-documents, of which metadata is a special class |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | This string’s value is what we want this document’s XATTR to be called                                                             |
| **3**  | This array contains the channels we want to include as the XATTR value                                                             |
| **4**  | Here we get all documents that we want to set the XATTR on (type = 'hotel' in this instance)                                       |
| **5**  | Check if the XATTR has been defined yet                                                                                            |
| **6**  | Update the XATTR — specify the item to update                                                                                      |
| **7**  | Update the XATTR — set the required value                                                                                          |
| **8**  | Update the XATTR — specify the item is an XATTR                                                                                    |
| **9**  | Insert the XATTR — specify the item to add (channelXattr)                                                                          |
| **10** | Insert the XATTR — set the required value using channelXattrValue                                                                  |
| **11** | Insert the XATTR — specify the item is an XATTR                                                                                    |

Running the code produces the following output:

```bash
Working with document id: 1000
Updated Existing user_xattr_key:
  channelXattr to this value: channel1, channel3, useradmin

Working with document id: 1001
Inserted New user_xattr_key:
  channelXattr with this value: channel1, channel3, useradmin

Completed Changes
```

Example 3\. Metadata on Couchbase Server document

```json
{
  "meta": { (1)
    "id": "1000",
    "rev": "7-1680c88cbce700000000000002000006",
    "expiration": 0,
    "flags": 33554438,
    "type": "json"
  },
  "xattrs": { (2)
    "channelXattr": [ (3)
      "channel1",
      "channel3",
      "useradmin"
    ]
  }
}
```

| **1** | This is the Fixed (or System) metadata                                                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is the User metadata, where you can define extended attributes                                                                                                                                                                   |
| **3** | Here _channelXattr_ is the name of the designated xattr holding the channel routing information to be passed to the Sync Function. You will set the value of the xattr using the SDK API when the document is created and-or updated. |

For more on Couchbase Server metadata and extended attributes — see Couchbase Server topics: [Metadata](../../../server/current/learn/data/data.md#metadata) | [Extended Attributes](../../../server/current/learn/data/extended-attributes-fundamentals.md)

## [](#lbl-using)Use XATTRs in a Sync Function

The designated XATTR is exposed to the [Sync Function](sync-function/sync-function.md) as an additional argument `meta.xattrs.<xattr name>`

Example 4\. Sync Function Arguments

```javascript
function (doc, oldDoc, meta) { (1)

  if (meta.xattrs.channelXattr === undefined) (2)
    {
      console.log("no user_xattr_key defined")
      channel(null)
    } else {
      channel(meta.xattrs.channelXattr) (3)


    }

  // Further processing as required ../
```

| **1** | The meta parameter exposes the user defined user\_xattr\_key if defined. The item takes the name configured for the database |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | Access the meta parameter object to check an xattr exists on this document                                                   |
| **3** | Use the content of the xattr to define the channels setting for this document                                                |

See: [Sync Function](sync-function/sync-function.md) topic for more information.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). From release 3.0