---
title: CONNECT Statements
description: This topic describes how you use <code>CONNECT</code> statements to
  connect all of the remote collections on a given link or links to their
  specified data sources, and start data ingestion.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_connect.adoc
  xref: xref:2.1@enterprise-analytics:sqlpp:5_ddl_connect.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_connect.html)

# CONNECT Statements

> This topic describes how you use `CONNECT` statements to connect all of the remote collections on a given link or links to their specified data sources, and start data ingestion. 

You incur charges when you connect a remote link.

The `CONNECT` statement applies only to remote links, and is not applicable to external links.

> [!NOTE]
> `CONNECT` statements cannot execute while the cluster is in a scaling state. The evaluation of such DDL statements fails. You can reattempt the action after scaling is complete.

## [](#syntax)Syntax

**ConnectStmnt EBNF** 

```EBNF
ConnectStmnt  ::= "CONNECT" "LINK" LinkSpecification
                  ( "WITH" ObjectConstructor )
```

**ConnectStmnt Diagram** 

!["CONNECT" "LINK" LinkSpecification ( "WITH" ObjectConstructor )](_images/ConnectStmnt.png) 

The `LinkSpecification` is a comma-separated list of one or more link names to connect.

**Show LinkSpecification** 

![LinkName ( "," LinkName )*](_images/LinkSpecification.png) 

LinkSpecification

## [](#example)Example

The following example connects the remote link called `myCbLink` and starts receiving data for all of the remote collections on that link.

CONNECT LINK myCbLink;

After you use `CONNECT` and have completed your initial data ingest, you can run `ANALYZE COLLECTION` on each collection associated with the link. The `ANALYZE` statement samples data in the collection so that cost-based optimization (CBO) can be applied instead of rule-based optimization. As data in the collections changes, you can run `ANALYZE COLLECTION` periodically to refresh the samples. See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

## [](#arguments)Arguments

WITH

The **`WITH`** clause enables you to provide parameters for the connection. The `ObjectConstructor` represents a JSON object containing key-value pairs, one for each parameter. You can define the following parameter.

| Name              | Description                                                                                                                                                                                                                                                                                                                                                 | Schema  |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **force**Optional | Applies to remote links for a Couchbase data service only. The metadata for remote Couchbase links includes the UUID of the remote Capella database or Coucbase Server cluster. If the UUID changes, connecting the link fails to prevent unintentional ingestion of data from a different cluster. To connect a link in this situation, set force to true. | Boolean |

## [](#see-also)See Also

* [CREATE a Remote Collection](5%5Fddl%5Fremote.md)
* [Entities in Enterprise Analytics](1a%5Fentities.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)