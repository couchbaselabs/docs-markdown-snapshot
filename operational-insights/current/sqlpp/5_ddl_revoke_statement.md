---
title: REVOKE Statement
description: The <code>REVOKE</code> statement supports the revocation of
  privileges on resources from users or roles as well as the removal of roles
  from users.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_revoke_statement.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_revoke_statement.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_revoke_statement.html)

# REVOKE Statement

The REVOKE statement allows revoking previously granted RBAC privileges or roles from specific users. It's important to understand that REVOKE is the inverse of GRANT. Its purpose is to undo the effect of a prior GRANT.

You can use REVOKE statements to manage privileges on the following Operational Insights objects:

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

**Revoke Database Diagram** 

![REVOKE](_images/revokedatabase.png) 

Example:

```sqlpp
REVOKE CREATE, DROP DATABASE FROM USER user1, ROLE role1;
```

## [](#scope)Scope

**Revoke Scope Diagram** 

![REVOKE](_images/revokescope.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SCOPE FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SCOPE IN DATABASE db FROM USER user1, ROLE role1;
```

## [](#collection)Collection

**Revoke Collection Diagram** 

![REVOKE](_images/revokecollection.png) 

Example:

```sqlpp
REVOKE SELECT, INSERT ON any COLLECTION FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON any COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON any COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON COLLECTION col1 FROM USER user1, ROLE role1;
REVOKE CREATE, DROP COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
```

## [](#view)View

**Revoke View Diagram** 

![REVOKE](_images/revokeview.png) 

Example:

```sqlpp
REVOKE SELECT ON any VIEW FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE SELECT ON VIEW view0 FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
```

## [](#index)Index

**Revoke Index Diagram** 

![REVOKE](_images/revokeindex.png) 

Example:

```sqlpp
REVOKE CREATE, DROP INDEX ON any COLLECTION FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON any COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON any COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON COLLECTION col1 FROM USER user1, ROLE role1;
```

## [](#function)Function

**Revoke Function Diagram** 

![REVOKE](_images/revokefunction.png) 

Example:

```sqlpp
REVOKE EXECUTE ON any FUNCTION FROM USER user1, ROLE role1;
REVOKE EXECUTE ON any FUNCTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE EXECUTE ON any FUNCTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE EXECUTE ON FUNCTION func FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION IN SCOPE db.dv FROM USER user1, ROLE role1;
```

## [](#library)Library

**Revoke Library Diagram** 

![REVOKE](_images/revokelibrary.png) 

Example:

```sqlpp
REVOKE USAGE ON any LIBRARY FROM USER user1, ROLE role1;
REVOKE USAGE ON any LIBRARY IN DATABASE db FROM USER user1, ROLE role1;
REVOKE USAGE ON any LIBRARY IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE USAGE ON LIBRARY db.dv.lib FROM USER user1, ROLE role1;
```

## [](#link)Link

**Revoke Link Diagram** 

![REVOKE](_images/revokelink.png) 

Example:

```sqlpp
REVOKE CREATE, DROP, ALTER LINK FROM USER user1, ROLE role1;
REVOKE CONNECT, DISCONNECT ON any LINK FROM USER user1, ROLE role1;
REVOKE DISCONNECT ON any LINK link0 FROM USER user1, ROLE role1;
```

## [](#role)Role

**Revoke Role Diagram** 

![REVOKE](_images/revokerole.png) 

Example:

```sqlpp
REVOKE CREATE, DROP ROLE FROM USER user1, ROLE role1;
```

## [](#synonym)Synonym

**Revoke Synonym Diagram** 

![REVOKE](_images/revokesynonym.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SYNONYM FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN SCOPE db.dv FROM USER user1, ROLE role1;
```