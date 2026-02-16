[View original HTML](/sync-gateway/current/access-control/sync-function/sync-function-api-expiry-cmd.html)

> Setting an expiry value on a document in a local database  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

expiry(value)

## [](#purpose)Purpose

Use `expiry(value)` to set the expiry value (TTL) on the document.

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| value    | The value can be specified in two ways: As an **ISO-8601 format:** date string — or example the 6th of July 2016 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; As a numeric Couchbase Server expiry value 1 |

1 Couchbase Server expiries are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server).

## [](#context)Context

Under the hood, the expiration time is set and managed on the Couchbase Server document (TTL is not supported for databases in walrus mode).

### [](#impact)Impact

The impact on the resulting document when the expiry value is reached depends on the setting of shared-bucket-access:

Enabled

The **active** revision of the document is tombstoned.

If there is another non-tombstoned revision for this document (i.e a conflict) it will become the active revision.

The tombstoned revision will be purged when the server’s metadata purge interval is reached.

Disabled

The document will be purged from the database.

As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication.

This expiration time is not propagated when the document is replicated.

The purge of the document does not cause it to be deleted on any other database.

### [](#inspect-a-document-expiry-value)Inspect a Document Expiry Value

You can retrieve a document’s expiration time, as it is returned in the response of GET [/{keyspace}/{docid}](../../rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-docid) using `show_exp=true` as the querystring.

```bash
curl -X GET "http://localhost:4985/ourdb/ourdoc?show_exp=true" -H "accept: application/json"
```

## [](#use)Use

Example 1\. expiry(value)

```javascript
expiry("2022-06-23T05:00:00+01:00") (1)
```

| **1** | Sets the expiry date to 5am on the 23rd June 2022. |
| ----- | -------------------------------------------------- |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function.md)
* [Import filter](../../sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](../../rest-api/rest-api.md)
* [Admin REST API](../../rest-api/rest-api-admin.md)
* [Metrics REST API](../../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)