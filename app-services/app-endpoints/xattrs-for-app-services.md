---
title: Extended Attributes (XATTRs)
description: Use Extended Attributes (XATTRs) to manage access control in App Services.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/xattrs-for-app-services.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/app-services/app-endpoints/xattrs-for-app-services.html)

# Extended Attributes (XATTRs)

> Use Extended Attributes (XATTRs) to manage access control in App Services. 

## [](#understanding-access-grant-properties)Understanding Access Grant Properties

To manage access control in App Services, you can use:

The Document Body

You can embed channels and roles directly within the document’s content. This method allows the document itself to govern access and routing.

Extended Attributes (XATTRs)

You can store channels and roles as user extended attributes (XATTRs). This is a more secure alternative that uses metadata, outside of the document content, to grant access.

## [](#advantages-of-using-xattrs)Advantages of Using XATTRs

Use XATTRs as a secure repository for data to drive document routing and access control. Some benefits of using XATTRs include:

Enhanced Security with Metadata Isolation

Since XATTRs are metadata and not part of the document’s main content, they are inaccessible to users. This prevents users from identifying the channels and roles a document is associated with by reading its content.

Separation of Concerns with Access Grant Independence

Storing access grants as XATTRs means that changes to this metadata do not affect the document’s revision history. Modifications to access grants do not result in new document revisions being pushed to clients. This maintains a separation between document content and access control metadata.

## [](#configure-an-xattr-property)Configure an XATTR Property

You can enable and define XATTR properties through your endpoint settings in the Capella UI.

**To configure your XATTR property:**

1. Navigate to the App Endpoint Settings.
2. Click the checkbox to enable using XATTRs for storing access grants.
3. Define the XATTR property name as a string value.

This property name will be used to associate access grant metadata with your documents.

## [](#setting-xattr-property-values)Setting XATTR Property Values

Assign values to your XATTR property, with the [Couchbase SDKs.](#cloud:home::sdk.adoc)

* **SDK API**: The Couchbase Server SDK API provides the necessary functions to set XATTR values.

> [!NOTE]
> You can’t set XATTR values using the APP Services REST API.

This example shows how XATTR values can be set and maintained using the Couchbase Server .Net SDK.

Example 1\. Set XATTR using Couchbase Server SDK

```C#
using System;
using System.Threading.Tasks;
using Couchbase;
using Couchbase.KeyValue;

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
            var our_user_xattr_key_name = "channelXattr";
            String[] channelXattrValue =
                {"channel1","channel3", "useradmin" };

            var ourDocumentType = "hotel";
            var documentKey = "";

            // Find our documents and get their ids
            var queryResult =
               await cluster.QueryAsync<dynamic>(
                   "select meta().id from `travel-sample`.`_default`.`_default` h where h.type = $1",
                        new Couchbase.Query.QueryOptions().Parameter(ourDocumentType));
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
                            );

                if (result.Exists(0))
                {
                    // Update xattr for retrieved Id
                    await collection.MutateInAsync(
                            documentKey,
                            specs => specs.Upsert(
                                path: our_user_xattr_key_name,
                                value: channelXattrValue,
                                isXattr: true));

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
                                path: our_user_xattr_key_name,
                                value: channelXattrValue,
                                isXattr: true));

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

* Couchbase.KeyValue provides access to the `MutateInSpec` class.

  * The `MutateInSpec` class provides access to sub-documents, of which metadata is a special class.
* You can store the name of your XATTR in a `String` such as `our_user_xattr_key_name`.

  * You can store channels you want to include as the XATTR value via a `String Array` as shown in `channelXattrValue`.
* You can then get all documents that you want to set the XATTR on (type = 'hotel' in this instance).

> [!NOTE]
> It is best practice to check if the XATTR has been defined before performing operations on it.

* Once the documents have been retrieved, you can perform operations on them asynchronously.

  * If an XATTR exists, you can update the XATTR, specifying the item to update.
  * You can set the XATTR value required.
  * You can specify the item is an XATTR.
* If no XATTR exists in target documents (`hotel`), you can insert an XATTR, specifying the item to add (`channelXattr`).

  * You can set the required value using `channelXattrValue`.
  * You can then specify the item is an XATTR.

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

## [](#using-your-xattrs)Using Your XATTRs

You can use your user defined XATTRs within the Access Control and Data Validation function to set access grants.

In the following example [Access Control and Data Validation](access-control-data-validation.md) function, the XATTRs defines channel settings. The provided Javascript function executes every time a new revision or update is made to a document.

The function shown performs validation for an existing user defined XATTR or creates one suitable for your needs.

```javascript
function (doc, oldDoc, meta) {

  if (meta.xattrs.channelXattr === undefined)
    {
      console.log("no user_xattr_key defined")
      channel(null)
    } else {
      channel(meta.xattrs.channelXattr)
    }
}
```

The meta parameter exposes the user defined user\_xattr\_key if defined and uses the content of the XATTR to define the `channels` setting for the document.

You can navigate to the Access Control and Data Validation Function with the Capella UI:

1. From the App Services screen, go to **App Endpoints**.  
![Select app endpoint](../_images/user-management/select-app-endpoint.png)  
Figure 1\. Select App Endpoint
2. Go to **Security** **Access and Validation**.  
![Updating the Access Control and Data Validation function](../_images/app-endpoint/xattr-access-control-data-validation.png)  
Figure 2\. Updating the Access Control and Data Validation Function  
> [!NOTE]  
> The Capella UI checks that the JavaScript function is valid when you click **Apply**. You can restore the function to its original default by clicking **Restore to Default**. The default function performs no validation.

## [](#see-also)See Also

* [Delta Sync](delta-sync.md)
* [Import Filters](import-filters.md)
* [Cross-Origin Resource Sharing (CORS)](cors-configuration-for-app-services.md)
* [Advanced Settings for App Endpoints](advanced-settings.md)
* [Create App Endpoints](creating-an-app-endpoint.md)