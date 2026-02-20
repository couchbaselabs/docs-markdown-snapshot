---
title: Import Filters
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/import-filters.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:app-services::app-endpoints/import-filters.adoc[]
---

[View original HTML](/app-services/app-endpoints/import-filters.html)

# Import Filters

![Delta Sync](../_images/app-endpoint/import-filters.png) 

## [](#about-import-filters)About Import Filters

Import Filters identify the subset of documents eligible to be replicated by App services based on user-defined requirements. This subset is applied to all future mutations.

Couchbase recommends using Import Filters. Without a filter (the default), the App Service imports all documents that are inserted or mutated within the associated linked collection of a scope in a given bucket.

## [](#basics)Basics

You can enable Import Filters per App Endpoint. You can manage Import Filters at a collection level per App Endpoint. You can apply Import Filters to any Linked Collection.

To access Import Filters:

1. Select your desired App Endpoint.
2. Navigate to the `Settings` tab within App Endpoint settings.
3. Select the 'Import Filter' configuration option.
4. Clink on an available linked collection from the **Linked Collections** table.
5. Click the `Enable Import Filter` checkbox.
6. Add your Import Filter function.
7. Click the **Save** button to confirm your choice and apply the filter.
8. You should see the **Import Filter Status** of the relevant linked collection change to enabled within the **Linked Collections** table.

You can switch to another linked collection within the same App Endpoint to quickly and conveniently apply an existing Import Filter to a different collection.

> [!CAUTION]
> You must save and enable any changes to your Import Filter function before switching linked collections, or your changes will be lost.

### [](#working-with-import-filters)Working with Import Filters

To add an Import Filter, first enable it, then enter or import a simple Javascript function into the code editor.

The function accepts a "Document", which is a JavaScript object representing the value stored in the cluster. You should return a Boolean (true or false) to determine whether to import a document.

For example, if you have stored the document:

```json
{
    "id": "0001",
    "type": "mobile",
    "value": "example"
}
```

The following Import Filter would select this record based on doc type and makes it available for the endpoint:

```javascript
function (doc) {
    return doc.type == 'mobile'; // returns `true` or `false`
}
```

> [!NOTE]
> The Javascript function is executed with [Otto](https://github.com/robertkrimen/otto)and has no access to any Capella data or features other than the `doc` argument.

Once the document has been imported and processed by the App Endpoint, changing the Import Filter will not remove it, even if the updated import filters would prevent newer mutations or iterations of the document from getting imported. The Import Filter is designed for a coarse-grained filter only. Look instead to the [Access Control & Data Validation function](access-control-data-validation.md) support for fine-grained read/write access control.

## [](#see-also)See Also

* [Delta Sync](delta-sync.md)
* [Extended Attributes (XATTRs)](xattrs-for-app-services.md)
* [Cross-Origin Resource Sharing (CORS) Configuration](cors-configuration-for-app-services.md)
* [Configure App Endpoints](advanced-settings.md)
* [Create App Endpoints](creating-an-app-endpoint.md)
* [Configure Access Control and Data Validation](access-control-data-validation.md)