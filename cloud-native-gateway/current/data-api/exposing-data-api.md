---
title: Exposing the Data API
description: Options for exposing Data API served by Cloud Native Gateway to
  different network environments, including public endpoints, VPC peering, and
  private networking.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/data-api/pages/exposing-data-api.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:data-api:exposing-data-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/data-api/exposing-data-api.html)

# Exposing the Data API

> Options for exposing Data API served by Cloud Native Gateway to different network environments, including public endpoints, VPC peering, and private networking. 

Cloud Native Gateway serves the Data API over HTTPS. It's compatible with standard HTTP infrastructure. How you expose it depends on your deployment environment and security requirements.

## [](#public-endpoints)Public Endpoints

Expose Cloud Native Gateway through a cloud load balancer or Kubernetes Ingress so applications can use the Data API on the public Internet.

### [](#managed-load-balancer-on-eks-gke-or-aks)Managed Load Balancer on EKS, GKE, or AKS

Create a Kubernetes `LoadBalancer` service that targets the Data API port:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: cng-data-api-public
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
spec:
  type: LoadBalancer
  selector:
    app: cloud-native-gateway
  ports:
    - name: data-api
      protocol: TCP
      port: 443
      targetPort: 18099
```

> [!IMPORTANT]
> Public exposure of the Data API requires strict security controls. Always enforce TLS, require strong authentication credentials, and implement IP allow-listing or Web Application Firewall (WAF) rules to restrict unauthorized access.

### [](#https-ingress)HTTPS Ingress

Use a Kubernetes Ingress controller with HTTPS backend support. The Ingress handles TLS and proxies to the Data API over HTTPS:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cng-data-api-ingress
  annotations:
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
spec:
  tls:
    - hosts:
        - data-api.example.com
      secretName: ingress-tls
  rules:
    - host: data-api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: cng-data-api-service
                port:
                  number: 18099
```

The Data API uses standard HTTPS rather than gRPC. It works with standard Ingress controllers such as nginx, Traefik, and HAProxy.

## [](#vpc-peering)VPC Peering

VPC peering links the VPC hosting Couchbase with the VPC hosting your client applications. With VPC peering:

* The Cloud Native Gateway Data API service is reachable by its private IP address or DNS name across the peered VPCs.
* Traffic stays within the cloud provider's network and does not traverse the public Internet.
* Use standard Kubernetes `ClusterIP` or `NodePort` services, as the peered VPC provides routing.

Configure VPC peering at the cloud infrastructure level using AWS VPC Peering, GCP VPC Network Peering, or Azure VNet Peering. Cloud Native Gateway needs no special configuration. Once peered, applications in the client VPC can reach the Cloud Native Gateway service directly.

> [!NOTE]
> VPC peering exposes all services in the peered network to each other. For more granular control, consider Private Endpoints.

## [](#private-endpoints)Private Endpoints

Private endpoints provide the most secure way to expose the Data API across org boundaries without VPC peering. Examples include AWS PrivateLink, GCP Private Service Connect, and Azure Private Link.

### [](#aws-privatelink)AWS PrivateLink

Cloud Native Gateway's single-endpoint architecture suits AWS PrivateLink well, which expects a Network Load Balancer in front of the service:

1. Create a Network Load Balancer targeting the Cloud Native Gateway Data API service.
2. Create a VPC Endpoint Service backed by the load balancer.
3. Consumer accounts create a VPC Endpoint that connects to your Endpoint Service.

Consumer applications connect to the VPC Endpoint's DNS name. Traffic routes through PrivateLink to the NLB and then to Cloud Native Gateway, all within the AWS network.

### [](#gcp-private-service-connect)GCP Private Service Connect

Similarly, for GCP:

1. Create a service attachment backed by the Internal Load Balancer fronting Cloud Native Gateway.
2. Consumer projects create a Private Service Connect endpoint targeting the service attachment.
3. Applications connect to the Private Service Connect endpoint.

### [](#azure-private-link)Azure Private Link

For Azure:

1. Create a Private Link Service backed by the Standard Load Balancer fronting Cloud Native Gateway.
2. Consumer subscriptions create a Private Endpoint that connects to the Private Link Service.
3. Applications connect to the Private Endpoint's network interface.

### [](#why-cloud-native-gateway-enables-private-endpoints)Why Cloud Native Gateway Enables Private Endpoints

Traditional Couchbase deployments require connectivity to multiple ports across multiple nodes, which is incompatible with private endpoint services that expose a single network endpoint. Because Cloud Native Gateway consolidates all services behind a single HTTPS port, it works naturally with all major cloud private endpoint technologies.

This is a primary motivation for Cloud Native Gateway's architecture and is a significant advantage for enterprise deployments that require network isolation.