---
title: Query Service
description: The Query Service supports the querying of data by means of SQL++.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/services-and-indexes/services/query-service.adoc
  xref: xref:7.2@server:learn:services-and-indexes/services/query-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/services-and-indexes/services/query-service.html)

# Query Service

> The Query Service supports the querying of data by means of SQL++. The Query Service depends on both the _Index Service_ and the _Data Service_. 

## [](#query-service-architecture)Query Service Architecture

The architecture of the _Query Service_ is shown by the following illustration:

![queryServiceArchitecture](../../_images/services-and-indexes/services/queryServiceArchitecture.png) 

Figure 1\. Query Service Architecture

The principal components are:

* **Listeners**: Concurrent query requests are received on ports 8093 and 18093 (for more information on port-allocation, see [Network and Firewall Requirements](../../../install/install-ports.md)).
* **Query Processor**: Responsible for applying the **Parser** to incoming queries, in order to determine whether each is a valid statement. Also employs the **Optimizer**, which evaluates available execution paths, so determining the path of lowest latency; generates a query-execution plan that uses the lowest-latency path; and assembles the plan into a series of operators. The **Execution Engine** receives the operators, and executes them — in parallel where possible.
* **Data Stores**: Provides access to various data-sources. The **Couchbase Server** store is used to access the data and indexes on Couchbase Server, and to handle authentication. Other data stores are also included, such as the store for the local filesystem.

## [](#query-execution)Query Execution

The following diagram shows the sequence of operations during query execution.

Query Execution Sequence

Unresolved include directive in modules/learn/pages/services-and-indexes/services/query-service.adoc - include::indexes:partial$diagrams/query-service.puml[]

When the Query Service receives the client's SQL++ query, it immediately passes it to the Query Processor. The Query Processor first parses the query to validate the statement and then creates an execution plan for the request.

The Execution Engine then begins executing the plan. It performs Scan operations on the relevant index, using either the Index Service or the Search Service. Next, it performs Fetch operations to get the actual data from the Data Service, and then uses this data for Join operations.

The Query Service processes the data further by applying Filter, Aggregate, Project, and Sort operations. These operations can run in parallel. In the diagram, the number of boxes within an operation block represents the degree of parallelism for that operation.

Finally, the service executes Offset and Limit operations to set the result size and starting point, and then streams the results back to the client. For more information about each of these operations, see [Query Phases](../../../n1ql/n1ql-language-reference/selectintro.md#query-execution-phases).

## [](#using-sql)Using SQL++

The Query Service supports queries made in SQL++. As well as providing a rich variety of query-options, SQL++ allows statements to be _prepared_, so that the parsing and compiling of plans is completed prior to execution; and permits _consistency-levels_ to be configured. For detailed information, see [SQL++ Language Reference](../../../n1ql/n1ql-language-reference/index.md).