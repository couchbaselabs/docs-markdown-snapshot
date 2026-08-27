---
title: TLS Behavior
description: Cloud Native Gateway supports TLS on the client and server side.
  Cloud Native Gateway acts as a proxy that terminates the incoming client TLS
  connection and forms a separate connection to the Cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/advanced-use-cases/pages/tls-behaviour.adoc
  xref: xref:cloud-native-gateway:advanced-use-cases:tls-behaviour.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/advanced-use-cases/tls-behaviour.html)

# TLS Behavior

> Cloud Native Gateway supports TLS on the client and server side. Cloud Native Gateway acts as a proxy that terminates the incoming client TLS connection and forms a separate connection to the Cluster. 

## [](#mtls-client-cert-authentication)mTLS - Client-Cert Authentication

* You can use any cert used for client cert auth against the Couchbase Cluster for mTLS against Cloud Native Gateway.
* A trusted Certificate Authority must sign the client cert presented to Cloud Native Gateway, or you must provide the Certificate Authority to Cloud Native Gateway using `--client-ca-cert`. Otherwise the TLS handshake fails.
* Cloud Native Gateway presents its own cert and key to the client. A Certificate Authority that the client application trusts must sign these.
* On a gRPC connection, Cloud Native Gateway presents the cert/key configured with the `--grpc-cert/--grpc-key` flags.
* On the RESTful Data API service, Cloud Native Gateway presents the cert/key configured with `--dapi-cert/--dapi-key`.
* To use the same cert and key for both the gRPC and Data API services, set the `--cert/--key` flags and omit the gRPC- and dapi-specific flags.
* After the TLS handshake with the client succeeds, Cloud Native Gateway forwards the client certificate to the Couchbase Cluster.
* Therefore the Certificate Authority used to sign the cert from the client application must be in the Couchbase Server's trust store.
* If a trusted Certificate Authority signed the cert, the Couchbase Server extracts the Username from the configured field the same as when using mTLS directly against the cluster: see <https://docs.couchbase.com/server/current/learn/security/certificates.html> for details.
* Cloud Native Gateway then forms a new connection to the Couchbase Cluster and attempts to service the request on behalf of the user extracted from the certificate.

If you're struggling with mTLS against Cloud Native Gateway:

* Check that your client certificate works directly against the Couchbase Server cluster. If not see the linked docs on client cert authentication.
* Check that your networking setup is not the issue.

## [](#tls-communication-with-the-cluster)TLS Communication with the Cluster

* When using a `couchbases://` connection string, Cloud Native Gateway communicates with the Cluster using TLS.
* Cloud Native Gateway must trust the Couchbase Cluster Certificate Authority, or you can pass it in using the `--cluster-ca-cert` flag.
* Cloud Native Gateway does not support mTLS between itself and the Couchbase Server Cluster at this time.

## [](#strict-firewall-rules-and-proxies)Strict Firewall Rules and Proxies

* Consider load balancers or proxies that perform SSL inspection when deploying Cloud Native Gateway.
* Deploy Cloud Native Gateway inside the firewall or proxy.
* The proxy does not affect Cloud Native Gateway to Server communication.
* If using TLS between Cloud Native Gateway and the client application, the firewall or proxy stops the TLS connection and creates a new connection to Cloud Native Gateway.
* You must configure Cloud Native Gateway to trust the Certificate Authority that signed the certificate the firewall or proxy presents.
* If using mTLS, configure the firewall or proxy with a client certificate that contains an appropriate username. A Certificate Authority trusted by both Cloud Native Gateway and the Couchbase Server Cluster must sign this certificate.
* See the mTLS — Client-Cert Authentication section earlier in this topic for details.