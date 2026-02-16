[View original HTML](/c-sdk/current/hello-world/overview.html)

###### 

The Couchbase C client, _libcouchbase_ (LCB), enables you to interact with a Couchbase Server cluster from the C language. It is also used by the Node.js, PHP, and Python SDKs to communicate with the Couchbase Server.

```c++
const char *connection_string = "couchbase://192.168.56.101,192.168.56.102";

lcb_CREATEOPTS *options = NULL;
lcb_createopts_create(&options, LCB_TYPE_CLUSTER);
lcb_createopts_connstr(options, connection_string, strlen(connection_string));
```

###### 

## Couchbase C SDK 3.3

###### 

Getting Started

Dive right in with a [quick install and Hello World](start-using-sdk.md).

###### 

Practical Howto Docs

Connect to our services — [data (KV)](../howtos/kv-operations.md); [Query](../howtos/n1ql-queries-with-sdk.md) — and the [Sub-Document API](../howtos/subdocument-operations.md).

And follow the [Concurrent Document Mutations](../howtos/concurrent-document-mutations.md) howto guide.

###### 

Reference Guides

The documentation supplements the practical Howto docs with references and [concept guides](../concept-docs/concepts.md), for those who prefer a broader understanding before diving in and coding.

[API Docs](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/index.html)

###### 

What’s Hot?

Leverage the new Couchbase Server Scopes and Collection features to build multi-tenant micro-service application.

* [C++ Distributed ACID Transactions from the C SDK](#1.0@cxx-txns::distributed-acid-transactions-from-the-sdk.adoc)
* [LCB includes our command line tools](cbc.md)

###### 

About

Those useful nuts-and-bolts guides to [compatibility tables](../project-docs/compatibility.md); [release notes](../project-docs/sdk-release-notes.md); [contribution guide](../project-docs/get-involved.md).

###### 

Community

For community help, visit the [Couchbase forums](https://forums.couchbase.com/c/c-sdk/7).

Documentation on older, unsupported versions of the SDK — that have reached end-of-life — can be found in the [archive](https://docs-archive.couchbase.com/home/index.html).

This page covers using our operational C SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

|  | Analytics SDKs SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information. Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |