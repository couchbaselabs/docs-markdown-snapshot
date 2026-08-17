---
title: Configure Multi-Dimensional Scaling
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/howto-mds.adoc
  xref: xref:2.6@operator::howto-mds.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/howto-mds.html)

# Configure Multi-Dimensional Scaling

> How-to independently scale cluster services. 

Couchbase server allows different services to be run on different hosts. This allows independent scaling of services as needs dictate.

## [](#couchbase-cluster-configuration)Couchbase Cluster Configuration

MDS is modeled with the [couchbaseclusters.spec.servers](resource/couchbasecluster.md#couchbaseclusters-spec-servers) configuration attribute:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  servers: (1)
  - name: data (2)
    size: 3 (3)
    services: (4)
    - data
  - name: index
    size: 2
    services:
    - index
  - name: query
    size: 4
    services:
    - query
```

| **1** | [couchbaseclusters.spec.servers](resource/couchbasecluster.md#couchbaseclusters-spec-servers) is a list of different classes of server. Each is independently configurable and can be used to run different services on different classes. Different classes may have different scales to handle different workloads on different services. The [couchbaseclusters.spec.servers.pod](resource/couchbasecluster.md#couchbaseclusters-spec-servers-pod) template can even allow execution on different hardware types. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.servers.name](resource/couchbasecluster.md#couchbaseclusters-spec-servers-name) must be a unique per-server class.                                                                                                                                                                                                                                                                                                                                                                           |
| **3** | [couchbaseclusters.spec.servers.size](resource/couchbasecluster.md#couchbaseclusters-spec-servers-size) is the number of pods to create per-server class. This can be independently scaled per-server class.                                                                                                                                                                                                                                                                                                         |
| **4** | [couchbaseclusters.spec.servers.services](resource/couchbasecluster.md#couchbaseclusters-spec-servers-services) can be independently defined per-server class. Services are immutable and cannot be changed once provisioned. It is highly recommended that each service only appear in one class — this simplifies memory allocation.                                                                                                                                                                               |