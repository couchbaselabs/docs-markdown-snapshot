---
title: Couchbase Python SDK 4.2
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.2/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.2@python-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.2/hello-world/overview.html)

# Couchbase Python SDK 4.2

# Couchbase Python SDK 4.2

```python
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

cluster = Cluster('couchbase://your-ip', authenticator=PasswordAuthenticator('username', 'password'))
bucket = cluster.bucket('default')
coll = bucket.default_collection()


coll.upsert('key', 'value')
get_res = coll.get("key")
print('Get result - value: {}; CAS: {}'.format(get_res.content, get_res.cas))

# Output:
# Get result - value: value; CAS: 1617046112012992512
```

The Couchbase Python SDK allows Python applications to access a Couchbase cluster. The Python SDK uses the high-performance C++ library Couchbase++ to handle communicating to the cluster over Couchbase’s binary protocols.

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Python SDK.

Getting Started

* [Start Using the Python SDK](start-using-sdk.md)
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
* [Working with Collections](../howtos/working-with-collections.md)

Managing Couchbase

* [Managing Connections](../howtos/managing-connections.md)
* [Authentication](../howtos/sdk-authentication.md)
* [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md)
* [User Management](../howtos/sdk-user-management-example.md)

Errors & Diagnostics

* [Error Handling](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)

##  Learn

Take a deep-dive into the SDK concept material and learn more about Couchbase.

Data Concepts

* [Data Model](../concept-docs/data-model.md)
* [Service Selection](../concept-docs/data-services.md)

Errors & Diagnostics Concepts

* [Errors and Diagnostics](../concept-docs/errors.md)
* [Tracing](../concept-docs/response-time-observability.md)
* [Failure Considerations](../concept-docs/durability-replication-failure-considerations.md)

##  Resources

Useful resources to help support your development experience with Couchbase and the Python SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [Full Installation](../project-docs/sdk-full-installation.md)