---
title: Eventing Access Control
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-rbac.adoc
  xref: xref:cloud:eventing:eventing-rbac.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-rbac.html)

# Eventing Access Control

> To create and manage Eventing Functions, you need the proper Organization Role, Project Role, or Cluster Access Credentials. 

## [](#description)Access Eventing with the Capella UI

To be able to use the Eventing service through the Capella UI, you must have one of the following project roles:

* Data Reader
* Data Writer
* Project Owner

For more information about the project roles and their privileges, see [Project Roles](../projects/project-roles.md).

The following table summarizes the actions that you can perform with the Eventing Service using each of these project roles.

| Action                           | Data Reader | Data Writer | Project Owner |
| -------------------------------- | ----------- | ----------- | ------------- |
| Create / Import / Edit Function  | No          | Yes         | Yes           |
| Deploy / Undeploy                | No          | Yes         | Yes           |
| View Logs / JavaScript/ Settings | Yes         | Yes         | Yes           |
| Delete Function                  | No          | Yes         | Yes           |
| Export Function                  | Yes         | Yes         | Yes           |

> [!NOTE]
> The Cluster Viewer and Cluster Manager roles do not grant Eventing privileges.

## [](#access-eventing-with-cluster-access-credentials)Access Eventing with Cluster Access Credentials

To access the Eventing Service programmatically via an SDK or API, your client must have the appropriate cluster access credentials, with access to the buckets, scopes, and collections that your Eventing functions use. For more information, see [Cluster Access](../clusters/cluster-rbac.md).

The following table summarizes the basic access levels or advanced access privileges that your cluster access credentials must have, for each of the target keyspaces that your Eventing functions read from or write to.

| Target Keyspace    | Basic Access Level   | Advanced Access Privilege     |
| ------------------ | -------------------- | ----------------------------- |
| Source / Mutation  | Read or Read / Write | Data Read and Eventing Manage |
| Metadata / Storage | Read / Write         | Data Read and Eventing Manage |
| Bindings           | Read or Read / Write | Data Read and Eventing Manage |

## [](#see-also)See Also

* [Organizations and Organization Users Overview](../organizations/organizations.md)
* [Projects Overview](../projects/projects.md)
* [Cluster Access](../clusters/cluster-rbac.md)