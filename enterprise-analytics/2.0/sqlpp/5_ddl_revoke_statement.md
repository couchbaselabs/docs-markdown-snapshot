---
title: REVOKE Statement
description: The <code>REVOKE</code> statement supports the revocation of
  privileges on resources from users or roles as well as the removal of roles
  from users.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl_revoke_statement.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:sqlpp:5_ddl_revoke_statement.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_revoke_statement.html)

# REVOKE Statement

The REVOKE statement allows revoking previously granted RBAC privileges or roles from specific users. It's important to understand that REVOKE is the inverse of GRANT. Its purpose is to undo the effect of a prior GRANT.

You can use REVOKE statements to create the following Enterprise Analytics objects:

* Databases
* Scopes
* Collections
* Views
* Indexes
* Functions
* Links
* Roles
* Synonyms

## [](#grant-syntax-diagrams)Grant Syntax Diagrams

**Grant Database Diagram** 

![GRANT](_images/grantdatabase.png) 

**Grant Scope Diagram** 

![GRANT](_images/grantscope.png) 

**Grant Collection Diagram** 

![GRANT](_images/grantcollection.png) 

**Grant View Diagram** 

![GRANT](_images/grantview.png) 

**Grant Index Diagram** 

![GRANT](_images/grantindex.png) 

**Grant Function Diagram** 

![GRANT](_images/grantfunction.png) 

**Grant Link Diagram** 

![GRANT](_images/grantlink.png) 

**Grant Role Diagram** 

![GRANT](_images/grantrole.png) 

**Grant Synonym Diagram** 

![GRANT](_images/grantsynonym.png) 

### [](#revoke-syntax-diagrams)Revoke Syntax Diagrams

**Revoke Database Diagram** 

![REVOKE](_images/revokedatabase.png) 

**Revoke Scope Diagram** 

![REVOKE](_images/revokescope.png) 

**Revoke Collection Diagram** 

![REVOKE](_images/revokecollection.png) 

**Revoke View Diagram** 

![REVOKE](_images/revokeview.png) 

**Revoke Index Diagram** 

![REVOKE](_images/revokeindex.png) 

**Revoke Function Diagram** 

![REVOKE](_images/revokefunction.png) 

**Revoke Link Diagram** 

![REVOKE](_images/revokelink.png) 

**Revoke Role Diagram** 

![REVOKE](_images/revokerole.png) 

**Revoke Synonym Diagram** 

![REVOKE](_images/revokesynonym.png)