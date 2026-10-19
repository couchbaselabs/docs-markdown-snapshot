---
title: GRANT Statement
description: The <code>GRANT</code> statement supports the granting of
  privileges on resources to users or roles as well as the assignment of roles
  to users.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_grant_statement.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_grant_statement.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_grant_statement.html)

# GRANT Statement

The GRANT statement supports the granting of privileges on resources to users or roles as well as the assignment of roles to users.

You can use GRANT statements to manage privileges on the following Operational Insights objects:

* [Database](#database)
* [Scope](#scope)
* [Collection](#collection)
* [View](#view)
* [Index](#index)
* [Function](#function)
* [Library](#library)
* [Link](#link)
* [Role](#role)
* [Synonym](#synonym)

## [](#database)Database

**Grant Database Diagram** 

![GRANT](_images/grantdatabase.png) 

Example:

```sqlpp
GRANT CREATE, DROP DATABASE TO USER user1, ROLE role1;
```

## [](#scope)Scope

**Grant Scope Diagram** 

![GRANT](_images/grantscope.png) 

Example:

```sqlpp
GRANT CREATE, DROP SCOPE TO USER user1, ROLE role1;
GRANT CREATE, DROP SCOPE IN DATABASE db TO USER user1, ROLE role1;
```

## [](#collection)Collection

**Grant Collection Diagram** 

![GRANT](_images/grantcollection.png) 

Example:

```sqlpp
GRANT SELECT, INSERT ON any COLLECTION TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON any COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON any COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON COLLECTION col1 TO USER user1, ROLE role1;
GRANT CREATE, DROP COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
```

## [](#view)View

**Grant View Diagram** 

![GRANT](_images/grantview.png) 

Example:

```sqlpp
GRANT SELECT ON any VIEW TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT SELECT ON VIEW view0 TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
```

## [](#index)Index

**Grant Index Diagram** 

![GRANT](_images/grantindex.png) 

Example:

```sqlpp
GRANT CREATE, DROP INDEX ON any COLLECTION TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON any COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON any COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON COLLECTION col1 TO USER user1, ROLE role1;
```

## [](#function)Function

**Grant Function Diagram** 

![GRANT](_images/grantfunction.png) 

Example:

```sqlpp
GRANT EXECUTE ON any FUNCTION TO USER user1, ROLE role1;
GRANT EXECUTE ON any FUNCTION IN DATABASE db TO USER user1, ROLE role1;
GRANT EXECUTE ON any FUNCTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT EXECUTE ON FUNCTION func TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION IN SCOPE db.dv TO USER user1, ROLE role1;
```

## [](#library)Library

**Grant Library Diagram** 

![GRANT](_images/grantlibrary.png) 

Example:

```sqlpp
GRANT USAGE ON any LIBRARY TO USER user1, ROLE role1;
GRANT USAGE ON any LIBRARY IN DATABASE db TO USER user1, ROLE role1;
GRANT USAGE ON any LIBRARY IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT USAGE ON LIBRARY db.dv.lib TO USER user1, ROLE role1;
```

## [](#link)Link

**Grant Link Diagram** 

![GRANT](_images/grantlink.png) 

Example:

```sqlpp
GRANT CREATE, DROP, ALTER LINK TO USER user1, ROLE role1;
GRANT CONNECT, DISCONNECT ON any LINK TO USER user1, ROLE role1;
GRANT DISCONNECT ON any LINK link0 TO USER user1, ROLE role1;
```

## [](#role)Role

**Grant Role Diagram** 

![GRANT](_images/grantrole.png) 

Example:

```sqlpp
GRANT CREATE, DROP ROLE TO USER user1, ROLE role1;
```

## [](#synonym)Synonym

**Grant Synonym Diagram** 

![GRANT](_images/grantsynonym.png) 

Example:

```sqlpp
GRANT CREATE, DROP SYNONYM TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN SCOPE db.dv TO USER user1, ROLE role1;
```