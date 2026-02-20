---
title: Projects Overview
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/projects/pages/projects.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:projects:projects.adoc[]
---

[View original HTML](/cloud/projects/projects.html)

# Projects Overview

> Use projects to organize and manage access to [clusters](../clusters/databases.md). An organization can have up to 50 projects. 

All clusters must exist within a project. When you create a cluster, you must choose a project where you want to create the cluster.

Organization users can only access clusters in a project if they’re a member of the project. When you add a user to a project, you assign them 1 or more [project roles](project-roles.md). Project roles determine the privileges those users have within the scope of the project, including any clusters within that project. For example, project roles determine if a project member can create and manage clusters, or access and monitor those clusters.

By using projects to organize your clusters, you can:

* Create separate environments for production and development
* Group clusters by application or geo-locality
* Apply different security and data management policies to different groups of clusters.

## [](#administering-projects)Administering Projects

* For information about creating and deleting projects, see [Manage Projects](manage-projects.md).
* For information about managing the members of a project, see [Manage Project Users](manage-project-users.md).