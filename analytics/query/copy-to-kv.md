---
title: Copy Results to a Couchbase Collection
description: From Capella Analytics, you can write the results of an analytical
  query to a Capella or Couchbase Server collection.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/copy-to-kv.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:analytics:query:copy-to-kv.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/query/copy-to-kv.html)

# Copy Results to a Couchbase Collection

> From Capella Analytics, you can write the results of an analytical query to a Capella or Couchbase Server collection. 

To provide access from Capella Analytics to a Capella or Couchbase Server operational database, you use a remote link to supply credentials. See [Stream Data from Remote Sources](../sources/manage-remote.md).

You can designate either an empty collection or a collection with pre-existing documents as the destination for the result of an analytical query. If the Couchbase collection already has documents in it, the operation overwrites any document with a matching document key with the new incoming documents.

## [](#use-cases)Use Cases

Example uses of this feature include:

* Transferring any Capella Analytics collection in its entirety to Capella or Couchbase Server. Some examples of the data that a Capella Analytics collection might contain follow:

  * Operational data shadowed through a Kafka pipeline
  * Operational data shadowed from a Capella or Couchbase Server collection
  * Archives, logs, and other resources in multiple formats stored on Amazon S3
  * Local files in multiple formats uploaded into standalone collections
* Moving the results of analytical queries completed in Capella Analytics—​including complex joins and functions—​to operational databases for use by adaptive applications.
* Using Capella Analytics's ability to parse data in other formats into JSON documents for downstream use in your Capella operational databases.

## [](#copy-to-statements)COPY TO Statements

You use a SQL++ for Capella Analytics COPY TO statement to write Capella Analytics results to a Capella or Couchbase Server collection. When you copy to Capella or Couchbase Server, you specify a remote link, the source and destination collections, and a document key. Optionally, you can specify a WITH clause.

See [COPY TO Couchbase Data Service Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fkv.md).

## [](#see-also)See Also

* [Stream Data from Remote Sources](../sources/manage-remote.md)
* [Write and Run Queries](editor.md)
* [Import Data to a Standalone Collection](../sources/import-data-standalone.md)