---
title: Configure Node Port Networking
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/howto-nodeport-networking.adoc
  xref: xref:2.6@operator::howto-nodeport-networking.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/howto-nodeport-networking.html)

# Configure Node Port Networking

> This guide shows you how to configure node port networking. 

Node port networking allows connection to a Couchbase cluster when you have access to the Kubernetes node network. It cannot be secured and has no stable client connection method. Its use is highly discouraged.

## [](#couchbase-cluster-configuration)Couchbase Cluster Configuration

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  networking:
    exposeAdminConsole: true (1)
    adminConsoleServiceTemplate:
      spec:
        type: NodePort
    exposedFeatures: (2)
    - client
    exposedFeatureServiceTemplate:
      spec:
        type: NodePort
```

| **1** | [couchbaseclusters.spec.networking.exposeAdminConsole](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposeadminconsole) is enabled to allow the creation of a service pointing to the Couchbase admin port. The node port can be accessed on any Kubernetes node and will provide a degree of high-availability to a client connecting to it. However as node IP addresses may vary during the life cycle of a Kubernetes cluster it is considered unstable and may cause clients to fail. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | [couchbaseclusters.spec.networking.exposedFeatures](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatures) defines the client feature set, meaning all enabled services are exposed. This also causes a per-pod service to be created allowing direct access by a client to each pod as required.                                                                                                                                                                                   |