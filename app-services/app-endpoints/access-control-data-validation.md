---
title: Configure Access Control and Data Validation
description: Access Control and Data Validation is vital to the security of your
  App Endpoint.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/access-control-data-validation.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:app-services::app-endpoints/access-control-data-validation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/access-control-data-validation.html)

# Configure Access Control and Data Validation

> Access Control and Data Validation is vital to the security of your App Endpoint. 

## [](#concepts)Concepts

The Access Control and Data Validation function allows you to configure document access or validate document data with [Scopes and Collections](../../cloud/clusters/data-service/scopes-collections.md), facilitating Role-based access control (RBAC).

You can customize the Access Control and Data Validation function for every linked collection within a given scope.

The Access Control and Data Validation function is performed on every document write to the associated linked collection.

## [](#prerequisites)Prerequisites

The examples used on this page will make use of the `channel()` API call. Channels allow you to assign access rights at the document level by allocating documents to a channel. Users who have access to the channel can then access the document. For more information on `channels` see [Add Security with Channels](../security/channels.md).

## [](#procedure)Procedure

You can access the Access Control and Data Validation function for an App Endpoint through the App Endpoint's configuration screen:

1. From the App Services screen, select an App Service, and click the **App Endpoints** tab.  
In the **App Endpoints** page, select an App Service Endpoint.
2. Select the App Endpoint you wish to configure the Access Control and Data Validation function for.  
![Select Linked Collections](../_images/app-endpoint/linked-collection-list-access-control-data-validation.png)  
Figure 1\. Select Linked Collections
3. Select the linked collection you wish to configure the Access Control and Data Validation function for.
4. Define your Access Control and Data Validation function.  
![Updating the Access Control and Data Validation function](../_images/app-endpoint/access-control-data-validation.png)  
Figure 2\. Updating the Access Control and Data Validation Function  
The provided JavaScript function executes every time a new revision/update is made to a document.  
> [!NOTE]  
> Couchbase recommends thoroughly checking the validity of the function as it will affect each document's operations that are passing through an App Endpoint. You can restore the function to its original default by clicking **Restore to Default**.

## [](#the-access-control-and-data-validation-function)The Access Control and Data Validation Function

The default function performs no validation; it simply assigns the document to the channels specified in its `channels` attribute.

```javascript
function (doc, oldDoc, meta) {
    channel(doc.channels);
}
```

The function arguments are:

| Name              | Description                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doc               | This object references the content of the document that is being saved. It matches the JSON saved by the Couchbase Lite application and replicated to the App Service. The document's \_id property contains the document ID. The document's \_rev property is the new revision ID. If the document is being deleted, it will have a \_deleted property with the value true. |
| oldDoc (optional) | If the document has been saved before, this object references the revision being replaced; otherwise it is null. In the case of a document with conflicts, the current provisional winning revision is passed in oldDoc.                                                                                                                                                     |
| meta (optional)   | This argument references the user-defined XATTR that you can use to hold access grant data. The referenced object can include items such as channels or roles. So, instead of embedding channel information directly within the document body, users can specify the user-defined XATTR associated with the document.                                                        |

> [!IMPORTANT]
> The default function differs depending on the following situations:
> 
> * For the default collection: `(_default._default)` \- `channel(doc.channels)` will be used.
> * For non-default collections - `channel(collectionName)` will be used.

## [](#writing-a-custom-access-control-and-data-validation-function)Writing a Custom Access Control and Data Validation Function

Consider your access control and document distribution requirements. For example:

* The document types it will process.
* The users it will serve.
* Which users need to access which document types.
* What constraints are to be placed on creating, updating and/or deleting documents.

Access Control Function Example

This example demonstrates a number of possible use-cases that may be useful to you. Start by creating your function as usual:

```javascript
function (doc, oldDoc, meta) {
    // ...
}
```

The following example defines channel settings with the content of an XATTR:

```javascript
function (doc, oldDoc, meta) {

  if (meta.xattrs.channelXattr === undefined)
    {
      console.log("no user_xattr_key defined")
      channel(null)
    } else {
      channel(meta.xattrs.channelXattr)

    }
```

The meta-parameter exposes the user defined `user_xattr_key` if it is defined, and uses the content of the XATTR to define the `channels` setting for the document.

### [](#handling-deletion)Handling Deletion

In this example, we require the user to:

* have the Editor role
* be one of the original writers of the document.

```javascript
    if (doc._deleted) {
        requireRole("role:editor");
        requireUser(oldDoc.writers);

        // Skip other validation because a deletion has no other properties:
        return;
    }
```

### [](#handling-required-properties)Handling Required Properties

In this example, we:

* require the properties: `title`, `creator`, `channels`, `writers`
* expect the `channels` and `writers` properties to be lists, and require the `writers` list to be non-empty.

```javascript
    if (!doc.title ||
        !doc.creator ||
        !doc.channels ||
        !doc.writers)
    {
        throw({forbidden: "Missing required properties"});
    }
    else if (doc.writers.length == 0) {
        throw({forbidden: "No writers"});
    }
```

### [](#handling-creation)Handling Creation

If `oldDoc` is not passed to the function, then a new document is being created. In this example, we:

* require the user to have the 'editor' role
* require the user to match the original 'creator' of the document.

```javascript
    if (! oldDoc) {
        requireRole("role:editor");
        requireUser(doc.creator)
    }
```

### [](#handling-modification)Handling Modification

If `oldDoc` is passed to the function, we know that document is being modified. In this example:

* Only users in the existing doc's writers list can change a document.
* The 'creator' property is immutable.

```javascript
    if (oldDoc) {
        requireUser(oldDoc.writers);

        if (doc.creator != oldDoc.creator) {
                throw({forbidden: "Can't change creator"});
        }
    }
```

### [](#assigning-the-document-to-channels)Assigning the Document to Channels

In this example, we assign the document to the channels in the list:

```javascript
    channel(meta.xattrs.[xattrName]);
```

## [](#test-your-access-control-and-data-validation-function)Test Your Access Control and Data Validation Function

Use the Test Function panel to simulate a document write and validate your Access Control and Data Validation function without affecting production data.

To open the Test Function panel, click **Run Test** on the Access Control and Data Validation function page.

![Test Function panel](../_images/app-endpoint/test-function-panel.png) 

Figure 3\. Test Function Panel

The panel provides the following inputs:

### [](#document-doc)Document (doc)

Provide the document that the function will process. You can fetch an existing document from the database by ID or provide a JSON document body directly.

Select **Document ID** to enter a document ID and click **Fetch**, or select **JSON** to paste a JSON document body.

### [](#old-document-olddoc)Old Document (oldDoc)

_Optional._

Provide the previous version of the document to simulate an update. Leave this field empty to simulate a new document creation.

Select **Document ID** to enter a document ID and click **Fetch**, or select **JSON** to paste a JSON document body.

### [](#user-context)User Context

_Optional._

Specify the user context under which the function runs to test access control behavior. Leave this field empty to simulate an Admin role with full access.

Select one of the following:

* **Mock User** — Enter a username, comma-separated roles, and comma-separated channels to define a test user.
* **App Service User** — Enter an existing App Service username and click **Fetch** to retrieve that user's roles and channels.

### [](#extended-attributes-xattr)Extended Attributes (XATTR)

_Optional._

Provide XATTR properties to simulate metadata changes. Leave this field empty to use the existing XATTR values as-is.

Enter the target XATTR name in the **Target XATTR Name** field. Define properties using **Simplified Builder** or **JSON**.

### [](#run-the-test)Run the Test

After configuring your inputs, click **Run Test**.

The results panel displays the outcome of the function execution. No production data is affected.

## [](#see-also)See Also

* [Resync your App Endpoint](resync.md)
* [Create App Endpoints](creating-an-app-endpoint.md)
* [Advanced Settings for App Endpoints](advanced-settings.md)
* [Add Security with Channels](../security/channels.md)