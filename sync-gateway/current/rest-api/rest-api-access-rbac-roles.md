---
title: RBAC Role&#8201;&#8212;&#8201;Endpoint Cross-reference
description: Server RBAC Role -- Rest API endpoint cross reference tabley
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/rest-api/pages/rest-api-access-rbac-roles.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:rest-api:rest-api-access-rbac-roles.adoc[]
---

[View original HTML](/sync-gateway/current/rest-api/rest-api-access-rbac-roles.html)

# RBAC Role&#8201;&#8212;&#8201;Endpoint Cross-reference

> Server RBAC Role — Rest API endpoint cross reference tabley  

Related _REST API_ topics: [Public REST API](rest-api.md) | [Admin REST API](rest-api-admin.md) | [Metrics REST API](rest-api-metrics.md)

## [](#admin)Admin

This table identifies the RBAC roles required by Sync Gateway to execute endpoint actions. **Couchbase Server 7.0.2 Developer Preview** introduces new roles offering fine-grained access control; existing roles will remain available.

For more on RBAC roles, see the Couchbase Server documentation: [Couchbase Server Authorization Roles](../../../server/current/learn/security/roles.md)

__Table 1\. REST API Admin Endpoints__
| Rest API Endpoint                        | Couchbase Server Roles |                                                                        |                                                                                      |
| ---------------------------------------- | ---------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Endpoint                                 | Method                 | All Versions                                                           | 7.0.2Developer Preview                                                               |
| {cluster}/\_all\_dbs                     | GET / HEAD             | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_config                       | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_config                       | PUT                    | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/fgprof                 | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/fgprof                 | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/block            | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/block            | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/cmdline          | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/cmdline          | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/goroutine        | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/goroutine        | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/heap             | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/heap             | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/mutex            | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/mutex            | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/profile          | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/profile          | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/symbol           | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/symbol           | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/threadcreate     | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/threadcreate     | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/trace            | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_debug/pprof/trace            | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_expvar                       | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops, External Stats Reader                                          |
| {cluster}/\_heap                         | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_logging                      | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_logging                      | PUT / POST             | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_post\_upgrade                | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_profile                      | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_profile/{profilename}        | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_sgcollect\_info              | DELETE                 | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_sgcollect\_info              | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_sgcollect\_info              | POST                   | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Dev Ops                                                                 |
| {cluster}/\_stats                        | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops, External Stats Reader                                          |
| {cluster}/\_status                       | GET                    | Cluster Admin Role, Full Admin Role, Read Only Admin,                  | Sync Gateway Dev Ops                                                                 |
| {cluster}/{db}/                          | DELETE                 | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Architect                                                               |
| {cluster}/{db}/                          | PUT                    | Cluster Admin Role, Full Admin Role,                                   | Sync Gateway Architect                                                               |
| {keyspace}/\_compact                     | POST                   | Sync Gateway Role. Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_config                            | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_config                            | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {keyspace}/\_config/import\_filter       | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_config/import\_filter       | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_config/import\_filter       | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_config/sync                 | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_config/sync                 | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_config/sync                 | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_dump/{view}                       | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only                         |
| {keyspace}/\_dumpchannel/{channel}       | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only                         |
| {db}/\_flush                             | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Dev Ops                                                                 |
| {db}/\_offline                           | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_online                            | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {keyspace}/\_purge                       | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                                             |
| {keyspace}/\_raw/{docid}                 | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only                         |
| {db}/\_repair                            | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_replication/                      | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replication/                      | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replication/{replicationID}       | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replication/{replicationID}       | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replication/{replicationID}       | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replicationStatus                 | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replicationStatus/{replicationID} | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_replicationStatus/{replicationID} | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Replicator                                                              |
| {db}/\_resync                            | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect                                                               |
| {db}/\_resync                            | POST                   |                                                                        | Sync Gateway Architect                                                               |
| {keyspace}/\_revtree/{docid}             | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only                         |
| {db}/\_role/                             | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_role/                             | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_role/{name}                       | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_role/{name}                       | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_role/{name}                       | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_session                           | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_session/{sessionid}               | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_session/{sessionid}               | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_user/                             | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_user/                             | POST                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_user/{name}                       | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_user/{name}                       | GET / HEAD             | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_user/{name}                       | PUT                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_user/{name}/\_session             | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_user/{name}/\_session/{sessionid} | DELETE                 | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Architect, Sync Gateway Application                                     |
| {db}/\_view/{view}                       | GET                    | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only                         |

## [](#common-endpoints)Common Endpoints

__Table 2\. Common Endpoints (with Admin)__
| Rest API Endpoint                  | Couchbase Server Release |                                                                        |                                                              |
| ---------------------------------- | ------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| Endpoint                           | Method                   | Pre 7.0.2                                                              | 7.0.2+                                                       |
| {cluster}/{db}/                    | GET / HEAD               | Cluster Admin Role, Full Admin Role Read Only Admin                    | Sync Gateway Dev Ops                                         |
| {cluster}/{db}/                    | POST                     | Cluster Admin Role, Full Admin Role                                    | Sync Gateway Application                                     |
| {keyspace}/\_all\_docs             | GET / HEAD / POST        | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/\_bulk\_docs            | POST                     | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {keyspace}/\_bulk\_get             | POST                     | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/\_changes               | GET / HEAD / POST        | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_design/{ddoc}               | GET / HEAD               | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_design/{ddoc}               | PUT                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {db}/\_design/{ddoc}               | DELETE                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {db}/\_design/{ddoc}/\_view/{view} | GET                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {db}/\_ensure\_full\_commit        | POST                     | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/\_revs\_diff            | POST                     | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {keyspace}/\_local/{docid}         | GET / HEAD               | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/\_local/{docid}         | PUT                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {keyspace}/\_local/{docid}         | DELETE                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {keyspace}/{docid}                 | GET / HEAD               | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/{docid}                 | PUT                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway ApplicationSync Gateway Application             |
| {keyspace}/{docid}                 | DELETE                   | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {keyspace}/{docid}/{attach}        | GET / HEAD               | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application, Sync Gateway Application Read Only |
| {keyspace}/{docid}/{attach}        | PUT                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |
| {db}/\_blipsync                    | GET                      | Sync Gateway Role, Bucket Admin, Bucket Application Access, Full Admin | Sync Gateway Application                                     |

## [](#metrics-endpoints)Metrics Endpoints

__Table 3\. REST API Admin Endpoints__
| Rest API Endpoint | Couchbase Server Release |                                                      |                                             |
| ----------------- | ------------------------ | ---------------------------------------------------- | ------------------------------------------- |
| Endpoint          | Method                   | Pre 7.0.2                                            | 7.0.2+                                      |
| {cluster}/metrics | GET                      | Cluster Admin Role, Full Admin Role, Read Only Admin | Sync Gateway Dev Ops, External Stats Reader |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)