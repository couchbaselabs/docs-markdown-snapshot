---
title: Couchbase Resource RBAC
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/concept-rbac.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:operator::concept-rbac.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/concept-rbac.html)

# Couchbase Resource RBAC

> The Kubernetes Operator manages many different types of Kubernetes custom resources, giving you the ability to control access to your Couchbase deployments based on which resource type each user should have access to. 

## [](#overview)Overview

Since `CouchbaseCluster` deployments are logical aggregations of other resource types, you can achieve fine grained access control using Kubernetes RBAC.

Consider the following conceptual diagram:

![resources rbac](_images/resources-rbac.png) 

Figure 1\. Example resource type security model

In [Figure 1](#image-example-security-model), an example security model with five different roles is depicted (Cluster Administrator, User Administrator, Data Scientist, XDCR Administrator, and Backup Administrator). These roles are arbitrary, and are simply an example of how a user might describe who in their organization would be allowed to modify a given resource type. For example, in the diagram above, the user has given a Backup Administrator the rights to modify `CouchbaseBackup` resources, and a XDCR Administrator the rights to modify `CouchbaseReplication` resources.

Using the flexibility of Kubernetes RBAC, you can group access to resource types however you want. In the example above, the user’s organization might change to where a single individual is responsible for both backups _and_ XDCR, in which case, that individual would need to be given access to both `CouchbaseBackup` and `CouchbaseReplication` resource types.

## [](#example-roles)Example Roles

The following are some example roles that might help guide you in how to distribute access to different resource types:

| Role                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   | Potential Resource Types                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Cluster Administrator** | Responsible for the overall scaling and operation of the cluster. Cluster administrators ensure correct sizing during maintenance windows. They have the ability to explicitly select the resources that are managed by the cluster. They are also responsible for XDCR remote clusters (this requires a secret, so by limiting to the cluster administrator only, no other role has access to secrets, especially the cluster root account). | CouchbaseCluster                                                    |
| **User Administrator**    | Responsible for creating users, Couchbase roles, and binding the user/role to a bucket.                                                                                                                                                                                                                                                                                                                                                       | CouchbaseUser, CouchbaseGroup, CouchbaseRoleBinding                 |
| **XDCR Administrator**    | Responsible for the management of XDCR replications. XDCR administrators may audit required bandwidth, storage, etc. that may impact the network or a remote cluster.                                                                                                                                                                                                                                                                         | CouchbaseReplication                                                |
| **Backup Administrator**  | Responsible for the management of bucket backups. Backup administrators may audit storage requirements and other legislation related to data retention.                                                                                                                                                                                                                                                                                       | CouchbaseBackup                                                     |
| **Data Scientist**        | Responsible for creating buckets in order to process data. Provided that the necessary Couchbase RBAC rules are established beforehand, data scientists can essentially have access to a pseudo database-as-a-service.                                                                                                                                                                                                                        | CouchbaseBucket, CouchbaseEphemeralBucket, CouchbaseMemcachedBucket |