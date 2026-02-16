[View original HTML](/cloud/projects/projects.html)

> Projects contain and allow access to Couchbase clusters. 

Within [organizations](../organizations/organizations.md), projects are used to organize and manage groups of Couchbase [clusters](../clusters/databases.md). An organization can contain any number of projects, and a project can contain any number of clusters.

A cluster must be contained within a single project. Therefore, you must create at least one project before you can create a cluster. When you create a cluster, you’ll be required to select a project for it to be contained in.

The main purpose of a project is to manage access to a particular set of clusters. Organization users can access the clusters within a project once they have been added as members of the project.

Members of a project are assigned [_project roles_](project-roles.md) which determine the privileges those users have within the scope of the project. These privileges determine whether a project member can perform activities such as creating and managing clusters in the project, or simply accessing and monitoring those clusters.

By using projects to organize your clusters, you have the flexibility to do things like:

* Create separate environments for production and development
* Group clusters by application or geo-locality
* Apply different security and data management policies to different groups of clusters.

## [](#administering-projects)Administering Projects

* For information on how to create and delete projects, refer to [Manage Projects](manage-projects.md).
* For information on how to manage the members of a project, refer to [Manage Project Users](manage-project-users.md)