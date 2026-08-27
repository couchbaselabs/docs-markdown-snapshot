---
title: Couchbase Node.js SDK 4.3
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/hello-world/pages/overview.adoc
  xref: xref:4.3@nodejs-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/hello-world/overview.html)

# Couchbase Node.js SDK 4.3

# Couchbase Node.js SDK 4.3

```javascript
const queryResult = await cluster.query(
    "SELECT * FROM `travel-sample`.inventory.hotel WHERE city=$1 LIMIT 10",
    { parameters: ['Paris']}
);
queryResult.rows.forEach((row)=>{
   console.log(row);
});
```

The Node.js SDK allows you to connect to a Couchbase Server cluster from Node.js. The Node.js SDK is a native Node.js module that uses the very fast Couchbase++ library to handle communicating with the cluster over the Couchbase binary protocol.

  
##  Using Your Database

How-to guides and tutorials to help you start your development journey with Couchbase and the Node.js SDK.

Getting Started

* [Start Using the Node.js SDK](start-using-sdk.md)
* [Start Using the Ottoman ODM](start-using-ottoman.md)
* [Data Operations](../howtos/kv-operations.md)
* [Query](../howtos/n1ql-queries-with-sdk.md)
* [Search](../howtos/full-text-searching-with-sdk.md)
* [Sample Application](sample-application.md)

Transactions

* [Using Couchbase Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)
* [Transaction Concepts](../concept-docs/transactions.md)

Working with Data

* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Analytics](../howtos/analytics-using-sdk.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Working with Collections](../howtos/working-with-collections.md)

Managing Couchbase

* [Managing Connections](../howtos/managing-connections.md)
* [Authentication](../howtos/sdk-authentication.md)
* [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md)
* [User Management](../howtos/sdk-user-management-example.md)

Errors & Diagnostics

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)

##  Learn

Take a deep-dive into the SDK concept material and learn more about Couchbase.

Data Concepts

* [Data Model](../concept-docs/data-model.md)
* [Service Selection](../concept-docs/data-services.md)
* [Field Level Encryption](../concept-docs/encryption.md)

Errors & Diagnostics Concepts

* [Errors and Diagnostics](../concept-docs/errors.md)
* [Tracing](../concept-docs/response-time-observability.md)
* [Failure Considerations](../concept-docs/durability-replication-failure-considerations.md)

##  Resources

Useful resources to help support your development experience with Couchbase and the Node.js SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/index.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [Couchbase Node.js Release Notes and Archives](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK API 3](../project-docs/migrating-sdk-code-to-3.n.md)
* [Full Installation](../project-docs/sdk-full-installation.md)