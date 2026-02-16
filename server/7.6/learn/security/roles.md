[View original HTML](/server/7.6/learn/security/roles.html)

> A Couchbase role permits one or more resources to be accessed according to defined privileges. 

## [](#roles-and-privileges)Roles and Privileges

Couchbase roles each have a fixed association with a set of one or more privileges. Each privilege is associated with a resource. Privileges are actions such as **Read**, **Write**, **Execute**, **Manage**, **Flush**, and **List**; or a combination of some or all of these.

Roles are of the following kinds:

* Administative: Associated with cluster-wide privileges. Some of these roles are for administrators; who might manage cluster-configurations; or read statistics; or enforce security. Others are for users and user-defined applications that require access to specific, cluster-wide resources.
* Bucket: Associated with bucket administration, collection management, and application access. Roles in this category can each be applied to one, to multiple, or to all buckets on the cluster.
* Data, Views, and XDCR: Associated with the Data Service. This includes the reading, writing, monitoring, backing-up, and restoring of data; the administration of Views; and the administration of Cross Data-Center Replication (XDCR).
* Other Services: Roles for the administration of services other than the Data Service. These roles are organized under the following categories: Query & Index, Search, Analytics, and Backup. (Eventing administration is covered within the Administrative category.)
* Mobile: Associated with the administration of Sync Gateway.

When a user (meaning either an administrator or an application) attempts to access a resource, they must authenticate. The roles and privileges associated with the user-credentials thereby presented are checked by Couchbase Server. If the associated roles contain privileges that support the kind of access that is being attempted, access is granted; otherwise, it is denied.

### [](#roles-in-relation-to-buckets)Roles in Relation to Buckets

All data within a bucket is contained within some collection, within some scope. Permissions conveyed by bucket-related roles may be restricted in any of the following ways:

* By Bucket: Permissions apply to all data in the specified bucket: all scopes and collections are thus covered by the permissions.
* By Bucket and Scope: Permissions apply only to the collections within the specified scope (or scopes), within the specified bucket.
* By Bucket, Scope, and Collection: Permissions apply only to the data within the specified collection (or collections), within the specified scope (or scopes), within the specified bucket.

For detailed information on scopes and collections, see [Scopes and Collections](../data/scopes-and-collections.md).

### [](#commonly-used-roles)Commonly Used Roles

Couchbase Server users can largely be categorized as administrators, developers, and applications. Each user-category is supported by a different subset of roles.

* Administrators. Able to log into Couchbase Web Console and perform administrative tasks; but unable to read or write data.  
The administrative tasks available are divided into multiple `admin` roles. For example, the **Cluster Admin** role allows the management of all cluster features except security; while the **Read-Only Admin** role allows only the reading of statistics; and the **Bucket Admin** role allows management only of one or more buckets. See the **Admin** roles listed below for full details. Note that depending on the administrator’s assigned roles, the content of Couchbase Web Console changes: for example, the entire **Security** screen is only visible to **Full Admin** administrators; and to administrators who possess both the **Local User Security Admin** and the **External User Security Admin** roles.
* Applications. Able to read or write data; but unable to log into Couchbase Web Console, or in any way modify cluster-settings. For example, the **Data Reader** and **Data Writer** roles allows data to be respectively read and written to one or more collections, within one or more scopes, within one or more buckets. Other application-intended roles are **Application Access**, **Data Writer**, **Data Backup & Restore**, and **Data Monitor**. See below for details on each.
* Developers. Can be given a selection of roles, allowing the right degree of data and console access. For example, the **Read-Only Admin** role allows the reading of cluster-statistics, while the **Data Read** and **Data Write** roles allow access to data on one or more buckets.

The following list contains all roles supported by Couchbase Server, Enterprise Edition. Each role is explained by means of a description and (in most cases) a table: the table lists the privileges in association with resources. The header of each table states the role’s **name**, followed by its alias name in parentheses: alias names are used in commands and queries. In each table-body, where a privilege is associated with a resource, this is indicated with a check-mark. Where a privilege is not associated with a resource (or where association would not be applicable), this is indicated with a cross. Resources not referred to in a particular table have no privileges associated with them in the context of the role being described.

Note that some roles grant access to Couchbase Web Console; while others do not. The set of features displayed within the console varies, according to role.

Note also that any authentication failure will be logged in the log file for the resource on which access was attempted. See [Manage Logging](../../manage/manage-logging/manage-logging.md), for detailed information on using log files.

## [](#full-admin)Full Admin

The **Full Admin** role (an Administrative role) supports full access to all Couchbase-Server features and resources, including those of security. The role allows access to Couchbase Web Console, and allows the reading and writing of bucket-data.

This role is also available in Couchbase Server Community Edition.

## [](#cluster-admin)Cluster Admin

The **Cluster Admin** role (an Administrative role) allows the management of all cluster features except security. The role allows access to Couchbase Web Console, but does not permit the writing of data.

| Role: Cluster Admin (cluster\_admin) |                                         |                                         |                                         |                                         |
| ------------------------------------ | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                            | Privileges                              |                                         |                                         |                                         |
| **Read**                             | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Cluster (except Passwords)           | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI (except Passwords)                | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Security (except Passwords)          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Data                          | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#local-user-security-admin)Local User Security Admin

The **Local User Security Admin** role (an Administrative role) allows the management of local user roles and the reading of all cluster statistics. The role does not permit the granting of the **Full Admin**, the **Read-Only Admin**, the **Local User Security Admin**, or the **External User Security Admin** role; and does not permit the administrator to change their own role (which therefore remains **Local User Security Admin**). The role supports access to Couchbase Web Console, but does not support the reading of data.

| Role: Local User Security Admin (security\_admin\_local) |                                         |                                         |                                         |                                         |
| -------------------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                                | Privileges                              |                                         |                                         |                                         |
| **Read**                                                 | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Cluster                                                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| UI (except Local User and Group Security)                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Local User and Group Security (including UI)             | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data                                              | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#external-user-security-admin)External User Security Admin

The **External User Security Admin** role (an Administrative role) allows the management of external user roles and the reading of all cluster statistics. The role does not permit the granting of the **Full Admin**, the **Read-Only Admin**, the **Local User Security Admin**, or the **External User Security Admin** role; and does not permit the administrator to change their own role (which therefore remains **External User Security Admin**). The role supports access to Couchbase Web Console, but does not support the reading of data.

| Role: External User Security Admin (security\_admin\_external) |                                         |                                         |                                         |                                         |
| -------------------------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                                      | Privileges                              |                                         |                                         |                                         |
| **Read**                                                       | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Cluster                                                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| UI (except External User Security)                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Security (including UI)                                        | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data                                                    | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#read-only-admin)Read-Only Admin

The **Read-Only Admin** role (an Administrative role) supports the reading of Couchbase Server statistics. This information includes registered usernames with roles and authentication domains, but excludes passwords. Since Couchbase Server version 7.6.2, users with this role can also read Backup Service data to monitor backup plans and tasks. The role allows access to Couchbase Server Web Console.

This role is also available in Couchbase Server Community Edition.

| Role: Read-Only Admin (ro\_admin)                       |                                         |                                       |                                       |                                       |
| ------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                                               | Privileges                              |                                       |                                       |                                       |
| **Read**                                                | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Cluster                                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| UI (except Passwords)                                   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Security (except Passwords)                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket Data                                             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Backup Service (tasks and plans) Couchbase Server 7.6.2 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#external-stats-reader)External Stats Reader

The **External Stats Reader** role (an Administrative role) grants access to the `/metrics` and `/prometheus_sd_config` endpoints for Prometheus integration. All statistics for all services can be read. The role does not allow access to Couchbase Web Console.

| Role: External Stats Reader (external\_stats\_reader) |                                         |                                       |                                       |                                       |
| ----------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                                             | Privileges                              |                                       |                                       |                                       |
| **Read**                                              | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Admin : stats\_export                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#xdcr-admin)XDCR Admin

The **XDCR Admin** role (an XDCR role) allows use of XDCR features, to create cluster references and replication streams. The role allows access to Couchbase Web Console and allows the reading of data.

| Role: XDCR Admin (replication\_admin) |                                         |                                         |                                         |                                         |
| ------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                             | Privileges                              |                                         |                                         |                                         |
| **Read**                              | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| XDCR for Cluster and Bucket           | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Settings                       | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Statistics                     | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| UI (XDCR)                             | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI (Other)                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#query-curl-access)Query Curl Access

The **Query Curl Access** role (a Query & Index role) allows the SQL++ CURL function to be executed by an externally authenticated user. The user can access Couchbase Web Console, but cannot read data, other than that returned by the SQL++ CURL function.

Note that the **Query Curl Access** role should be assigned with caution, since it entails risk: CURL runs within the local Couchbase Server network; therefore, the assignee of the **Query Curl Access** role is permitted to run GET and POST requests on the internal network, while being themselves externally located.

For an account of limitations on CURL, see [CURL Function](../../n1ql/n1ql-language-reference/curl.md).

In versions of Couchbase Server prior to 5.5, this role was referred to as **Query External Access**.

| Role: Query Curl Access (query\_external\_access) |                                         |                                       |                                         |                                       |
| ------------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                         | Privileges                              |                                       |                                         |                                       |
| **Read**                                          | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket : SQL++, curl                              | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket settings                                   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-system-catalog)Query System Catalog

The **Query System Catalog** role (a Query & Index role) allows information to be looked up by means of SQL++ in the system catalog: this includes `system:indexes`, `system:prepareds`, and tables listing current and past queries. This role is designed for troubleshooters, who need to debug queries. The role allows access to Couchbase Web Console, but does not permit the reading of bucket-items.

| Role: Query System Catalog (query\_system\_catalog) |                                         |                                       |                                       |                                       |                                         |
| --------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                           | Privileges                              |                                       |                                       |                                       |                                         |
| **Read**                                            | **Write**                               | **Execute**                           | **Manage**                            | **List**                              |                                         |
| Bucket : SQL++, INDEX                               | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : SQL++, Meta                                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Bucket Settings                                     | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| UI                                                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#manage-global-functions)Manage Global Functions

The **Manage Global Functions** role (a Query & Index role) allows global SQL++ functions to be managed. The user can access Couchbase Web Console, but cannot read data.

| Role: Manage Global Functions (query\_manage\_global\_functions) |                                         |                                       |                                       |                                         |
| ---------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                                        | Privileges                              |                                       |                                       |                                         |
| **Read**                                                         | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| SQL++, udf                                                       | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| UI                                                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#execute-global-functions)Execute Global Functions

The **Execute Global Functions** role (a Query & Index role) allows global SQL++ functions to be executed. The user can access Couchbase Web Console, but cannot read data.

| Role: Execute Global Functions (query\_execute\_global\_functions) |                                         |                                       |                                         |                                       |
| ------------------------------------------------------------------ | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                          | Privileges                              |                                       |                                         |                                       |
| **Read**                                                           | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| SQL++, udf                                                         | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#manage-scope-functions)Manage Scope Functions (Query and Index)

The **Manage Scope Functions** role (a Query & Index role) allows SQL++ and user defined functions to be managed for a given scope, given corresponding specification of bucket. The user can access Couchbase Web Console, but cannot read data.

| Role: Manage Scope Functions (query\_manage\_functions) |                                         |                                       |                                       |                                         |
| ------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                               | Privileges                              |                                       |                                       |                                         |
| **Read**                                                | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| Bucket, Scope: SQL++, udf                               | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| UI                                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                                   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#execute-scope-functions)Execute Scope Functions

The **Execute Scope Functions** role (a Query & Index role) allows SQL++ and user defined functions to be executed for a given scope, given corresponding specification of bucket. The user can access Couchbase Web Console, but cannot read data.

| Role: Execute Scope Functions (query\_execute\_functions) |                                         |                                       |                                         |                                       |
| --------------------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                 | Privileges                              |                                       |                                         |                                       |
| **Read**                                                  | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Collection, Bucket, Scope: SQL++, udf                     | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                                     | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#manage-global-external-functions)Manage Global External Functions

The **Manage Global External Functions** role (a Query & Index role) allows global external language functions to be managed. The user can access Couchbase Web Console, but cannot read data.

| Role: Manage Global External Functions (query\_manage\_global\_external\_functions) |                                         |                                       |                                       |                                         |
| ----------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                                                           | Privileges                              |                                       |                                       |                                         |
| **Read**                                                                            | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| SQL++, udf\_external                                                                | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| UI                                                                                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                                                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#execute-global-external-functions)Execute Global External Functions

The **Execute Global External Functions** role (a Query & Index role) allows global SQL++ functions to be executed. The user can access Couchbase Web Console, but cannot read data.

| Role: Execute Global External Functions (query\_execute\_global\_external\_functions) |                                         |                                       |                                         |                                       |
| ------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                                             | Privileges                              |                                       |                                         |                                       |
| **Read**                                                                              | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| SQL++, udf\_external                                                                  | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                                                                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                                                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#manage-scope-external-functions)Manage Scope External Functions

The **Manage Scope External Functions** role (a Query & Index role) allows external language functions to be managed for a given scope, given corresponding specification of bucket. The user can access Couchbase Web Console, but cannot read data.

| Role: Manage Scope External Functions (query\_manage\_external\_functions) |                                         |                                       |                                       |                                         |
| -------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                                                  | Privileges                              |                                       |                                       |                                         |
| **Read**                                                                   | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| Collection, Bucket, Scope: SQL++, udf\_external                            | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| UI                                                                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#execute-scope-external-functions)Execute Scope External Functions

The **Execute Scope External Functions** role (a Query & Index role) allows external language functions to be executed for a given scope, given corresponding specification of bucket. The user can access Couchbase Web Console, but cannot read data.

| Role: Execute Scope External Functions (query\_execute\_external\_functions) |                                         |                                       |                                         |                                       |
| ---------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                                    | Privileges                              |                                       |                                         |                                       |
| **Read**                                                                     | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Collection, Bucket, Scope: SQL++, udf\_external                              | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                                                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                                                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#analytics-reader)Analytics Reader

The **Analytics Reader** role (an Analytics role) allows querying of shadow data-sets. The role allows access to Couchbase Web Console, and permits the reading of data.

| Role: Analytics Reader (analytics\_reader) |                                         |                                       |                                         |                                       |
| ------------------------------------------ | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                  | Privileges                              |                                       |                                         |                                       |
| **Read**                                   | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket : Analytics                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#analytics-admin)Analytics Admin

The **Analytics Admin** role (an Analytics role) allows management of dataverses; management of all Analytics Service links; and management of all datasets. The role allows access to Couchbase Web Console, but does not permit the reading of data.

| Role: Analytics Admin (analytics\_admin) |                                         |                                       |                                       |                                         |
| ---------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                | Privileges                              |                                       |                                       |                                         |
| **Read**                                 | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| Dataverse : Analytics                    | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : Analytics                       | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : UI                              | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Other : UI                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#bucket-admin)Bucket Admin

The **Bucket Admin** role (which is a Bucket role) allows the management of all per bucket features (including starting and stopping XDCR). The role allows access to Couchbase Web Console, but does not permit the reading or writing of data.

| Role: Bucket Admin (bucket\_admin) |                                         |                                         |                                         |                                         |
| ---------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                          | Privileges                              |                                         |                                         |                                         |
| **Read**                           | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Cluster                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket (including XDCR)            | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data                        | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket UI                          | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Other UI                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#manage-scopes)Manage Scopes

The **Manage Scopes** role (a Bucket role) allows the creation and deletion of scopes, and the creation and deletion of collections per scope, given the corresponding specification of bucket. The role allows no access to data, and does not permit access to Couchbase Web Console. The role is intended for application use only.

| Role: Manage Scopes (scope\_admin) |                                         |                                         |                                         |                                         |
| ---------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                          | Privileges                              |                                         |                                         |                                         |
| **Read**                           | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Manage Scopes                      | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI                                 | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#application-access)Application Access

The **Application Access** role (a Bucket role) provides read and write access to data, per bucket. The role does not allow access to Couchbase Web Console: it is intended for applications, rather than users. Note that this role is also available in the Community Edition of Couchbase Server.

The role is provided in support of buckets that were created on versions of Couchbase Server prior to 5.0\. Such buckets were accessed by specifying bucket-name and bucket-password: however, bucket-passwords are not recognized by Couchbase Server 5.0 and after. Therefore, for each pre-existing bucket, the upgrade-process for 5.0 and after creates a new user, whose username is identical to the bucket-name; and whose password is identical to the former bucket-password, if one existed. If no bucket-password existed, the user is created with no password. This migration-process allows the same name-combination as before to be used in authentication. To ensure backwards compatibility, each system-created user is assigned the **Application Access** role, which authorizes the same read-write access to bucket-data as was granted before 5.0.

Use of the **Application Access** role is deprecated for buckets created on Couchbase Server 5.0 and after: use the other bucket-access roles provided. Note that in versions of Couchbase Server prior to 5.5, this role was referred to as **Bucket Full Access**.

| Role: Application Access (bucket\_full\_access) |                                         |                                         |                                         |                                         |                                         |
| ----------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                       | Privileges                              |                                         |                                         |                                         |                                         |
| **Read**                                        | **Write**                               | **Execute**                             | **Manage**                              | **Flush**                               |                                         |
| Bucket Data                                     | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| Bucket Views                                    | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| SQL++: Index                                    | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| SQL++: Other                                    | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket                                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |
| Pools                                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#xdcr-inbound)XDCR Inbound

The **XDCR Inbound** role (which is an XDCR role) allows the creation of inbound XDCR streams, per bucket. It does not allow access to Couchbase Web Console, and does not permit the reading of data.

In versions of Couchbase Server prior to 5.5, this role was referred to as **Replication Target**.

| Role: XDCR Inbound (replication\_target) |                                         |                                         |                                       |                                       |
| ---------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                                | Privileges                              |                                         |                                       |                                       |
| **Read**                                 | **Write**                               | **Execute**                             | **Manage**                            |                                       |
| Bucket : Settings                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Meta                            | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Stats                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#sync-gateway)Sync Gateway

The **Sync Gateway** role (which is a Mobile role) allows full access to data per bucket, as required by Sync Gateway. The role does not allow access to Couchbase Web Console. The user can, by means of Sync Gateway, read and write data, manage indexes and views, and read some cluster information.

| Role: Sync Gateway (mobile\_sync\_gateway) |                                         |                                         |                                         |                                         |
| ------------------------------------------ | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                  | Privileges                              |                                         |                                         |                                         |
| **Read**                                   | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| UI                                         | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket : Data                              | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : Views                             | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : Indexes                           | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket : Query                             | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| Bucket : Flush                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| Bucket : Settings                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Auto-compaction                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Admin: Memcached: Idle                     | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Pools                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#sync-gateway-configurator)Sync Gateway Architect

The **Sync Gateway Architect** role (which is a Mobile role) allows management of Sync Gateway databases; and of Sync Gateway users and roles; and allows access to Sync Gateway’s `/metrics` endpoint. The role does not allow access to Couchbase Web Console; and does not allow reading of application data. For information on Sync Gateway users and roles, see [Access Control Concepts](http://docs.couchbase.com/sync-gateway/3.0/access-control-concepts.html).

| Role: Sync Gateway Architect (sync\_gateway\_configurator) |                                         |                                         |                                         |                                         |
| ---------------------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                                  | Privileges                              |                                         |                                         |                                         |
| **Read**                                                   | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| UI                                                         | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Collection: Data                                           | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Collection: Sync Gateway Users and Roles                   | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Metrics: Sync Gateway                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#sync-gateway-app)Sync Gateway Application

The **Sync Gateway Application** role (which is a Mobile role) allows management of Sync Gateway users and roles; and allows application data to be read and written through Sync Gateway. The role does not allow access to Couchbase Web Console. For information on Sync Gateway users and roles, see [Access Control Concepts](http://docs.couchbase.com/sync-gateway/3.0/access-control-concepts.html).

| Role: Sync Gateway Application (sync\_gateway\_app) |                                         |                                         |                                       |                                         |
| --------------------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                           | Privileges                              |                                         |                                       |                                         |
| **Read**                                            | **Write**                               | **Execute**                             | **Manage**                            |                                         |
| UI                                                  | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Collection: Sync Gateway Users and Roles            | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Collection: Sync Gateway Application Data           | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |

## [](#sync-gateway-application-read-only)Sync Gateway Application Read Only

The **Sync Gateway Application Read Only** role (which is a Mobile role) allows reading of Sync Gateway users and roles; and allows application data to be read through Sync Gateway. The role does not allow access to Couchbase Web Console. For information on Sync Gateway users and roles, see [Access Control Concepts](http://docs.couchbase.com/sync-gateway/3.0/access-control-concepts.html).

| Role: Sync Gateway Application Read Only (sync\_gateway\_app\_ro) |                                         |                                       |                                       |                                       |
| ----------------------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                                                         | Privileges                              |                                       |                                       |                                       |
| **Read**                                                          | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| UI                                                                | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Collection: Sync Gateway Users and Roles                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Collection: Sync Gateway Application Data                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#sync-gateway-replicator)Sync Gateway Replicator

The **Sync Gateway Replicator** role (which is a Mobile role) allows management of Sync Gateway replications. The role does not allow access to Couchbase Web Console.

| Role: Sync Gateway Replicator (sync\_gateway\_replicator) |                                         |                                         |                                         |                                         |
| --------------------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                                 | Privileges                              |                                         |                                         |                                         |
| **Read**                                                  | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| UI                                                        | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Collection: Sync Gateway Replications                     | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |

## [](#sync-gateway-dev-ops)Sync Gateway Dev Ops

The **Sync Gateway Dev Ops** role (which is a Mobile role) allows management of Sync Gateway node-level configuration; and allows access to Syn Gateway’s `/metrics` endpoint, for Prometheus integration. The role does not allow access to Couchbase Web Console.

| Role: Sync Gateway Dev Ops (sync\_gateway\_dev\_ops) |                                         |                                         |                                         |                                         |
| ---------------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                            | Privileges                              |                                         |                                         |                                         |
| **Read**                                             | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| UI                                                   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Dev Ops: Sync Gateway                                | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Metrics: Sync Gateway                                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#data-reader)Data Reader

The **Data Reader** role (which is a Data role) allows data to be read per collection, given corresponding specifications for bucket and scope. Note that the role does not permit the running of SQL++ queries (such as SELECT) against data. The role does not allow access to Couchbase Web Console: it is intended to support applications, rather than users.

| Role: Data Reader (data\_reader) |                                         |                                       |                                       |                                       |
| -------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                        | Privileges                              |                                       |                                       |                                       |
| **Read**                         | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Bucket Docs                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Meta                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Xattr                   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#data-writer)Data Writer

The **Data Writer** role (which is a Data role) allows data to be written per collection, given corresponding specifications for bucket and scope. The role does not allow access to Couchbase Web Console: it is intended to support applications, rather than users.

| Role: Data Writer (data\_writer) |                                         |                                         |                                       |                                       |
| -------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                        | Privileges                              |                                         |                                       |                                       |
| **Read**                         | **Write**                               | **Execute**                             | **Manage**                            |                                       |
| Bucket : Docs                    | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Xattr                   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#data-dcp-reader)Data DCP Reader

The **Data DCP Reader** role (which is a Data role) allows DCP streams to be initiated per collection, given corresponding specifications for bucket and scope. The role does not allow access to Couchbase Web Console: it is intended to support applications, rather than users. The role does allow the reading of data.

| Role: Data DCP Reader (data\_dcp\_reader) |                                         |                                         |                                       |                                       |
| ----------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                                 | Privileges                              |                                         |                                       |                                       |
| **Read**                                  | **Write**                               | **Execute**                             | **Manage**                            |                                       |
| Bucket: : Data                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket: : DCP                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket: : Sxattr                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Admin: Memcached: Idle                    | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                                     | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#data-backup-and-restore)Data Backup & Restore

The **Data Backup & Restore** role (which is a Data role) allows data to be backed up and restored, per bucket. The role supports the reading of data. The role does not allow access to Couchbase Web Console: it is intended to support applications, rather than users.

The privileges represented in this table are, from left to right, Read, Write, Execute, Manage, Select, Backup, Create, List, and Build.

| Role: Data Backup & Restore (data\_backup) |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |
| ------------------------------------------ | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                  | Privileges                              |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |
| **Rd**                                     | **Wrt**                                 | **Exec**                                | **Mng**                                 | **Slct**                                | **Bckp**                                | **Crt**                                 | **Lst**                                 | **Bld**                                 |                                         |
| Bucket: : Data                             | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket: : Views                            | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket: : FTS                              | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket: : Stats                            | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket: : Settings                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket: : SQL++, Index                     | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket: : SQL++, Meta                      | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket: : Analytics                        | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Analytics:                                 | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Pools                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#data-monitor)Data Monitor

The **Data Monitor** role (which is a Data role) allows statistics to be read for a given bucket, scope, or collection. It does not allow access to Couchbase Web Console, and does not permit the reading of data. This role is intended to support application-access, rather than user-access.

In versions of Couchbase Server prior to 5.5, this role was referred to as **Data Monitoring**.

| Role: Data Monitor (data\_monitoring) |                                         |                                       |                                       |                                       |
| ------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                             | Privileges                              |                                       |                                       |                                       |
| **Read**                              | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Bucket : Stats                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#views-admin)Views Admin

The **Views Admin** role (which is a Views role) allows the management of views, per bucket. The role allows access to Couchbase Web Console.

| Role: Views Admin (views\_admin) |                                         |                                         |                                         |                                         |
| -------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                        | Privileges                              |                                         |                                         |                                         |
| **Read**                         | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Bucket Data (Views)              | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data (Other)              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Statistics                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Settings                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket (SQL++)                   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   |
| UI (Views)                       | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI (Other)                       | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#views-reader)Views Reader

The **Views Reader** role (which is an Administrative role) allows data to be read from views, per bucket. This role does not allow access to Couchbase Web Console, and is intended to support applications, rather than users.

| Role: Views Reader (views\_reader) |                                         |                                       |                                       |                                       |
| ---------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                          | Privileges                              |                                       |                                       |                                       |
| **Read**                           | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Bucket : Docs                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Bucket : Views                     | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#query-select)Query Select

The **Query Select** role (which is a Query & Index role) allows the SELECT statement to be executed per collection, given corresponding specifications for bucket and scope. This role allows access to Couchbase Web Console; it also supports the reading of data, and of bucket settings.

| Role: Query Select (query\_select) |                                         |                                       |                                         |                                       |
| ---------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                          | Privileges                              |                                       |                                         |                                       |
| **Read**                           | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket : SQL++, SELECT             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket : Docs                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Bucket Settings                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-update)Query Update

The **Query Update** role (which is a Query & Index role) allows the UPDATE statement to be executed per collection, given corresponding specifications for bucket and scope. The role supports access to Couchbase Web Console, and allows the writing (but not the reading) of data. It allows the reading of bucket settings.

| Role: Query Update (query\_update) |                                         |                                         |                                         |                                       |
| ---------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                          | Privileges                              |                                         |                                         |                                       |
| **Read**                           | **Write**                               | **Execute**                             | **Manage**                              |                                       |
| Bucket : SQL++, UPDATE             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket : Docs                      | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Bucket Settings                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-insert)Query Insert

The **Query Insert** role (which is a Query & Index role) allows the INSERT statement to be executed per collection, given corresponding specifications for bucket and scope. The role supports access to Couchbase Web Console, and allows the writing (but not the reading) of data. It allows the reading of bucket settings.

| Role: Query Insert (query\_insert) |                                         |                                         |                                         |                                       |
| ---------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                          | Privileges                              |                                         |                                         |                                       |
| **Read**                           | **Write**                               | **Execute**                             | **Manage**                              |                                       |
| Bucket : SQL++, INSERT             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket : Docs                      | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Bucket Settings                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-delete)Query Delete

The **Query Delete** role (which is a Query & Index role) allows the DELETE statement to be executed per collection, given corresponding specifications for bucket and scope. The role supports access to Couchbase Server Web Console, and allows the deletion of data. It allows the reading of bucket settings.

| Role: Query Delete (query\_delete) |                                         |                                       |                                         |                                       |
| ---------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                          | Privileges                              |                                       |                                         |                                       |
| **Read**                           | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket : SQL++, DELETE             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket : Docs Delete               | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket Settings                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-sequential-scan)Query Use Sequential Scan

The **Query Use Sequential Scan** role, located under Query & Index in the Web Console’s roles list, allows users' queries to perform a sequential scan of a keyspace. The query planner only decides to use a sequential scan when there is no suitable index for the keyspace. Only queries by users with this role can use a sequential scan to access data because scanning a large unindexed keyspace can be expensive. This role does not grant the user the ability to read or mutate data or access to the Web Console. Administrators' queries automatically have permission to perform sequential scans when necessary.

| Role: Query Use Sequential Scan (query\_use\_sequential\_scans) |                                       |                                       |                                         |                                       |
| --------------------------------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                       | Privileges                            |                                       |                                         |                                       |
| **Read**                                                        | **Write**                             | **Execute**                           | **Manage**                              |                                       |
| Sequential Scans                                                | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket : Docs                                                   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Bucket Settings                                                 | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                                              | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                                           | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-use-sequences)Use Sequences

The **Use Sequences** role allows users to use sequences within a specific scope. Users with this role can execute SQL++ NEXTVAL and PREVVAL functions. This role does not allow creating or managing sequences. It does allow access to Couchbase Server Web Console.

| Role: Use Sequences (query\_use\_sequences) |                                         |                                       |                                         |                                       |
| ------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                   | Privileges                              |                                       |                                         |                                       |
| **Read**                                    | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket, Scope: SQL++, Sequences             | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket, Scope: Collections                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                       | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#query-manage-sequences)Manage Sequences

The **Manage Sequences** role allows users to manage sequences for a given scope. Manage these sequences with CREATE, ALTER, and DROP statements. This role does not allow executing sequences. It does allow access to Couchbase Server Web Console.

| Role: Manage Sequences (query\_manage\_sequences) |                                         |                                       |                                       |                                         |
| ------------------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                                         | Privileges                              |                                       |                                       |                                         |
| **Read**                                          | **Write**                               | **Execute**                           | **Manage**                            |                                         |
| Bucket, Scope: SQL++, Sequences                   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Bucket, Scope: Collections                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| UI                                                | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                                             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#query-manage-index)Query Manage Index

The **Query Manage Index** role (which is a Query & Index role) allows indexes to be managed per collection, given corresponding specifications for bucket and scope. The role allows access to Couchbase Web Console, but does not permit the reading of data.

| Role: Query Manage Index (query\_manage\_index) |                                         |                                         |                                         |                                         |
| ----------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                       | Privileges                              |                                         |                                         |                                         |
| **Read**                                        | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Bucket : SQL++, INDEX                           | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Settings                                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Bucket Statistics                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Index Settings                                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| UI                                              | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Pools                                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |

## [](#eventing-full-admin)Eventing Full Admin

The **Eventing Full Admin** role (which is an Eventing role) allows creation and management of eventing functions. The role allows access to Couchbase Web Console.

| Role: Eventing Full Admin (eventing\_admin) |                                         |                                         |                                         |                                         |
| ------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                   | Privileges                              |                                         |                                         |                                         |
| **Read**                                    | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Data                                        | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| SQL++                                       | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Eventing                                    | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| Analytics                                   | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI                                          | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |

## [](#eventing-manage-functions)Manage Scope Functions (Eventing)

The **Manage Scope Functions** role (which is an Eventing role) allows eventing functions for a given scope to be managed. The role allows access to Couchbase Web Console.

| Role: Manage Scope Functions (eventing\_manage\_functions) |                                         |                                       |                                         |                                       |
| ---------------------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                                  | Privileges                              |                                       |                                         |                                       |
| **Read**                                                   | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket, Collection: Functions for Scope                    | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| Bucket Statistics                                          | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| UI                                                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#backup-full-admin)Backup Full Admin

The **Backup Full Admin** role (which is a Backup role) allows performance of backup-related tasks. The role allows access to Couchbase Web Console.

| Role: Backup Full Admin (backup\_admin) |                                         |                                         |                                         |                                         |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                               | Privileges                              |                                         |                                         |                                         |
| **Read**                                | **Write**                               | **Execute**                             | **Manage**                              |                                         |
| Data                                    | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |
| Cluster Settings                        | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |
| Bucket Settings                         | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |
| Backup Service                          | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI                                      | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![yes](../_images/introduction/yes.png) |

## [](#search-admin)Search Admin

The **Search Admin** role (which is a Search role) allows management of all features of the Search Service, per bucket. The role allows access to Couchbase Web Console.

In versions of Couchbase Server prior to 5.5, this role was referred to as **FTS Admin**.

| Role: Search Admin (fts\_admin) |                                         |                                         |                                       |                                         |
| ------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- |
| Resources                       | Privileges                              |                                         |                                       |                                         |
| **Read**                        | **Write**                               | **Execute**                             | **Manage**                            |                                         |
| Bucket Data (Search)            | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| Bucket Data (Other)             | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Bucket Settings                 | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Search Settings                 | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) |
| UI (Other)                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |
| Pools                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   |

## [](#search-reader)Search Reader

The role **Search Reader** (which is a Search role) allows Full Text Search indexes to be searched for bucket, scope, and collection. The role allows access to Couchbase Web Console, and supports the reading of data.

In versions of Couchbase Server prior to 5.5, this role was referred to as **FTS Searcher**.

| Role: Search Reader (fts\_searcher) |                                         |                                       |                                       |                                       |
| ----------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Resources                           | Privileges                              |                                       |                                       |                                       |
| **Read**                            | **Write**                               | **Execute**                           | **Manage**                            |                                       |
| Bucket : FTS                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Settings: FTS                       | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| UI                                  | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |
| Pools                               | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png) |

## [](#analytics-select)Analytics Select

The **Analytics Select** role (which is an Analytics role) allows the querying of datasets for bucket, scope. and collection. The role allows access to Couchbase Web Console, and permits the reading of some data.

| Role: Analytics Select (analytics\_select) |                                         |                                       |                                         |                                       |
| ------------------------------------------ | --------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------------------------- |
| Resources                                  | Privileges                              |                                       |                                         |                                       |
| **Read**                                   | **Write**                               | **Execute**                           | **Manage**                              |                                       |
| Bucket : Analytics                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) |
| UI                                         | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |
| Pools                                      | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png) |

## [](#analytics-manager)Analytics Manager

The **Analytics Manager** role (which is an Analytics role) allows the management and querying of datasets created per bucket; and the management of Analytics Service local links. The role allows access to Couchbase Web Console, and permits the reading of some data.

| Role: Analytics Manager (analytics\_manager) |                                         |                                       |                                         |                                         |
| -------------------------------------------- | --------------------------------------- | ------------------------------------- | --------------------------------------- | --------------------------------------- |
| Resources                                    | Privileges                              |                                       |                                         |                                         |
| **Read**                                     | **Write**                               | **Execute**                           | **Manage**                              |                                         |
| Bucket : Analytics                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![yes](../_images/introduction/yes.png) | ![yes](../_images/introduction/yes.png) |
| UI                                           | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |
| Pools                                        | ![yes](../_images/introduction/yes.png) | ![no](../_images/introduction/no.png) | ![no](../_images/introduction/no.png)   | ![no](../_images/introduction/no.png)   |