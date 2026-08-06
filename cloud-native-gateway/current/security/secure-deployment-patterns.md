---
title: Secure Deployment Patterns
description: Best practices for securely deploying Cloud Native Gateway,
  including secret management, network segmentation, and defense-in-depth
  strategies.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/security/pages/secure-deployment-patterns.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:security:secure-deployment-patterns.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/security/secure-deployment-patterns.html)

# Secure Deployment Patterns

> Best practices for securely deploying Cloud Native Gateway, including secret management, network segmentation, and defense-in-depth strategies. 

## [](#secret-management)Secret Management

Cloud Native Gateway requires several secrets for operation: cluster credentials, TLS certificates, and optionally CA certificates. Proper management of these secrets is critical.

### [](#kubernetes-secrets)Kubernetes Secrets

In Kubernetes deployments, store all sensitive configuration in Kubernetes Secrets:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cng-credentials
type: Opaque
data:
  username: <base64-encoded>
  password: <base64-encoded>
---
apiVersion: v1
kind: Secret
metadata:
  name: cng-server-tls
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded>
  tls.key: <base64-encoded>
```

Best practices:

* Use a secrets management solution (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault) with a Kubernetes secrets store CSI driver for production deployments.
* Enable encryption at rest for etcd to protect secrets stored in the Kubernetes API server.
* Limit RBAC access to Cloud Native Gateway secrets to only the service accounts that need them.
* Rotate TLS certificates at regular intervals. Cloud Native Gateway supports dynamic certificate rotation without restarts.

### [](#standalone-deployments)Standalone Deployments

For standalone (non-Kubernetes) deployments:

* Store credentials in environment variables or configuration files with restricted filesystem permissions such as\`0600\`.
* Do not pass credentials as command-line arguments, as they may be visible in process listings.
* Use a secrets management service to inject credentials at runtime.

## [](#network-segmentation)Network Segmentation

Network segmentation protects Cloud Native Gateway from unauthorized access and reduces the blast radius of security incidents. Proper segmentation limits which clients can reach the gateway and which backend services the gateway can access. These controls help enforce least-privilege networking and simplify security review and operations. The following sections describe recommended patterns for isolating Cloud Native Gateway at the network edge and restricting its access to the Couchbase cluster.

### [](#isolate-cloud-native-gateway-from-the-public-internet)Isolate Cloud Native Gateway from the Public Internet

Cloud Native Gateway should not be directly exposed to the public Internet. You can place it behind a load balancer, ingress controller, or API gateway that provides:

* TLS termination (or TLS pass-through).
* DDoS protection.
* IP allow-listing or WAF rules.
* Rate limiting at the network edge.

### [](#restrict-cloud-native-gateway-to-cluster-traffic)Restrict Cloud Native Gateway-to-Cluster Traffic

Cloud Native Gateway needs network access to the Couchbase cluster's KV, Query, Search, Analytics, and Management ports. In Kubernetes:

* Use NetworkPolicies to restrict Cloud Native Gateway's egress to only the Couchbase cluster pods.
* Restrict Cloud Native Gateway's ingress to only the load balancer or ingress controller.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: cng-network-policy
spec:
  podSelector:
    matchLabels:
      app: cloud-native-gateway
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              role: ingress
      ports:
        - port: 18098
        - port: 18099
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: couchbase
      ports:
        - port: 8091
        - port: 8093
        - port: 8094
        - port: 8095
        - port: 11210
        - port: 18091
        - port: 18093
        - port: 18094
        - port: 18095
        - port: 11207
```

### [](#enable-tls-between-cloud-native-gateway-and-the-cluster)Enable TLS Between Cloud Native Gateway and the Cluster

For production deployments, always use TLS between Cloud Native Gateway and the Couchbase cluster (`couchbases://` connection scheme). This ensures end-to-end encryption even if attackers intercept traffic between Cloud Native Gateway and the cluster.

## [](#defense-in-depth-recommendations)Defense-in-Depth Recommendations

A layered security approach provides multiple barriers against threats. The following recommendations implement defense-in-depth principles across your deployment.

### [](#layer-1-network-perimeter)Layer 1: Network Perimeter

* Place Cloud Native Gateway behind a load balancer with IP allow-listing.
* Use private endpoints (AWS PrivateLink, GCP Private Service Connect) for cross-organization access.
* Enable DDoS protection at the load balancer or WAF level.

### [](#layer-2-transport-security)Layer 2: Transport Security

* Enforce TLS on all Cloud Native Gateway interfaces. This is default and cannot be turned off.
* Use certificates signed by a trusted CA (not self-signed) in production.
* Enable TLS between Cloud Native Gateway and the Couchbase cluster.
* Consider mutual TLS (mTLS) for client authentication in high-security environments.

### [](#layer-3-authentication-and-authorization)Layer 3: Authentication and Authorization

* Use strong, unique passwords for each user.
* Apply the principle of least privilege when assigning RBAC roles.
* Use separate credentials for different applications or services.
* Disable the Data API passthrough for admin APIs (`ProxyBlockAdmin`) if administrative access through the Data API is not needed.

### [](#layer-4-rate-limiting-and-abuse-prevention)Layer 4: Rate Limiting and Abuse Prevention

* Configure Cloud Native Gateway's built-in rate limiter to protect against request floods.
* Monitor connection and request metrics for anomalous patterns.
* Set appropriate load balancer timeouts to prevent connection exhaustion.

### [](#layer-5-monitoring-and-audit)Layer 5: Monitoring and Audit

* Enable Couchbase Server audit logging to record all operations performed through Cloud Native Gateway.
* Monitor Cloud Native Gateway logs for authentication failures, which may indicate credential compromise.
* Track the `grpc_client_names` metric to detect unexpected client types.
* Set up alerts for unusual traffic patterns (spike in connections, elevated error rates).

## [](#disabling-debug-mode-in-production)Disabling Debug Mode in Production

Cloud Native Gateway's `--debug` flag enables additional features that are not appropriate for production:

* The hooks system allows intercepting and modifying requests, which could be exploited.
* Error responses include additional context that may expose internal system details.
* The `HooksService` gRPC endpoint is registered, providing a control plane for request manipulation.

Always ensure `--debug` is **not enabled** in production deployments.