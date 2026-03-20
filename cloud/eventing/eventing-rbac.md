---
title: Eventing Access Control
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-rbac.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-rbac.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-rbac.html)

# Eventing Access Control

> To create and manage Eventing Functions, you need the proper Organization Role, Project Role, or Cluster Access Credentials. 

To be able to use the Eventing service through the Capella UI, you need to have one of the following organization or project roles:

* The Organization Owner, Project Creator, or Organization Member role, as described in [Organization Roles](../organizations/organization-user-roles.md).
* The Project Owner or Data Writer role, as described in [Project Roles](../projects/project-roles.md).

To be able to use the Eventing service, via an SDK or a REST API, your client application must have cluster access credentials with Read or Read/write access to the buckets, scopes, and collections that your Eventing functions listen to. Also, you need Write or Read/Write access to the buckets, scopes, and collections that the Eventing functions write to, as described in [Manage Cluster Access Credentials](../clusters/manage-database-users.md).