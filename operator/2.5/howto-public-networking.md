---
title: Configure Public Networking
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-public-networking.adoc
  xref: xref:2.5@operator::howto-public-networking.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-public-networking.html)

# Configure Public Networking

> This guide shows you how to configure Couchbase Server to be accessible from the public internet. 

Public networking leverages public cloud provider load-balancer services. These by default are allocated a public IP address which allows them to be accessed from anywhere with an internet connection. This may be the best option if connecting another public cloud service to your Couchbase cluster.

Due to the public nature of connections the Operator enforces the use of TLS to keep data private. Please see the [TLS configuration how-to](howto-tls.md) for more information.

## [](#couchbase-cluster-configuration)Couchbase Cluster Configuration

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  networking:
    exposeAdminConsole: true (1)
    adminConsoleServiceTemplate:
      spec:
        type: LoadBalancer (2)
    exposedFeatures: (3)
    - client
    exposedFeatureServiceTemplate:
      spec:
        type: LoadBalancer (4)
    dns:
      domain: my-cluster.example.com (5)
    tls:
      secretSource:
        serverSecretName: my-server-secret (6)
```

| **1** | [couchbaseclusters.spec.networking.exposeAdminConsole](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposeadminconsole) is enabled to allow the creation of a service pointing to the Couchbase admin port.                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.networking.adminConsoleServiceTemplate](resource/couchbasecluster.md#couchbaseclusters-spec-networking-adminconsoleservicetemplate) type is set to LoadBalancer causing the admin console service to use a load balancer. Combining the two attributes means a client can connect to a stable and highly-available public DNS endpoint that is load balanced across the entire cluster.                                                                                                                                                                                                                          |
| **3** | [couchbaseclusters.spec.networking.exposedFeatures](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatures) defines the client feature set, meaning all enabled services are exposed. This also causes a per-pod service to be created allowing direct access by a client to each pod as required.                                                                                                                                                                                                                                                                                                               |
| **4** | [couchbaseclusters.spec.networking.exposedFeatureServiceTemplate](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatureservicetemplate) type is set to LoadBalanacer meaning each per-pod service is created with a load balancer and allocated a public IP address.                                                                                                                                                                                                                                                                                                                                             |
| **5** | [couchbaseclusters.spec.networking.dns.domain](resource/couchbasecluster.md#couchbaseclusters-spec-networking-dns-domain) defines the domain DDNS entries will be created under. A separate [External DNS](https://github.com/kubernetes-sigs/external-dns) service needs to be created to actually replicate DNS names and IP addresses into a public DDNS server. The Operator will create annotations for the admin console as console.my-cluster.example.com for example. Annotations are attached to the admin console and per-pod services. The External DNS controller needs to create DNS A records for these service endpoints. |
| **6** | [couchbaseclusters.spec.networking.tls.secretSource.serverSecretName](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource-serversecretname) specifies the Couchbase server certificate. Mandatory subject alternative names (SANs) are described in the [TLS certificate tutorial](tutorial-tls.md). An additional SAN is required for the public DNS names, in this case DNS:\*.my-cluster.example.com.                                                                                                                                                                                                     |