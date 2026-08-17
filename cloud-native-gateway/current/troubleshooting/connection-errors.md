---
title: Connection Errors
description: Diagnosing and resolving common connection errors when applications
  connect to Cloud Native Gateway.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/troubleshooting/pages/connection-errors.adoc
  xref: xref:cloud-native-gateway:troubleshooting:connection-errors.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/troubleshooting/connection-errors.html)

# Connection Errors

> Diagnosing and resolving common connection errors when applications connect to Cloud Native Gateway. 

## [](#common-connection-errors)Common Connection Errors

This section covers the most frequent connection failures seen when clients connect to Cloud Native Gateway. For each error, review the symptom, confirm the cause, and then apply the recommended resolution steps.

### [](#tls-handshake-failure)TLS Handshake Failure

**Symptoms:**

* SDK reports a TLS or SSL error on connect.
* `grpcurl` fails with `transport: authentication handshake failed`.
* Cloud Native Gateway logs show no incoming connection activity.

**Causes:**

* The client does not trust the Cloud Native Gateway server certificate (self-signed certificate without CA trust configured).
* Certificate hostname mismatch: the hostname in the connection string does not match the Subject Alternative Name (SAN) in the Cloud Native Gateway certificate.
* Expired certificate.
* TLS interception by a network appliance that presents a different certificate.

**Resolution:**

1. Verify the Cloud Native Gateway certificate is valid and not expired:  
```console  
$ openssl s_client -connect cng.example.com:18098 </dev/null 2>/dev/null | openssl x509 -noout -dates -subject -ext subjectAltName  
```
2. Ensure the client is configured to trust the CA that signed the Cloud Native Gateway certificate. For self-signed certificates in development, configure the SDK to use the self-signed certificate as the trusted CA.
3. Check that the hostname in the connection string matches one of the SANs in the certificate.
4. If a network appliance is intercepting TLS, either bypass it for Cloud Native Gateway traffic or configure the client to trust the appliance's CA certificate. For more information, see [advanced-use-cases:deployments-behind-firewalls.adoc](#advanced-use-cases:deployments-behind-firewalls.adoc).

### [](#connection-refused)Connection Refused

**Symptoms:**

* SDK reports `connection refused` or `no route to host`.
* `grpcurl` or `curl` reports `connection refused`.

**Causes:**

* Cloud Native Gateway is not running on the target host/port.
* Firewall or NetworkPolicy is blocking the connection.
* The Kubernetes Service or load balancer is not routing to Cloud Native Gateway pods.
* Incorrect port number in the connection string.

**Resolution:**

1. Verify Cloud Native Gateway is running:  
```console  
$ kubectl get pods -l app=couchbase -o wide  
$ kubectl logs pod/<pod-name> -c cloud-native-gateway | tail -20  
```
2. Check that the Cloud Native Gateway port is accessible:  
```console  
$ kubectl port-forward pod/<pod-name> 18098:18098  
$ grpcurl --insecure localhost:18098 grpc.health.v1.Health/Check  
```
3. Verify the Kubernetes Service endpoints:  
```console  
$ kubectl get endpoints <service-name>  
```
4. Check NetworkPolicies that might block ingress to Cloud Native Gateway.

### [](#connection-timeout)Connection Timeout

**Symptoms:**

* SDK connection attempt times out without receiving a response.
* Slow initial connection but subsequent requests may work.

**Causes:**

* Network routing issue between client and Cloud Native Gateway.
* Load balancer health checks fail, removing Cloud Native Gateway from rotation.
* Cloud Native Gateway has not yet connected to the Couchbase cluster during startup.
* DNS resolution issues.

**Resolution:**

1. Check Cloud Native Gateway startup logs for cluster connection status:  
```console  
$ kubectl logs pod/<pod-name> -c cloud-native-gateway | grep -i "ping\|connect\|waiting"  
```  
If you see `waiting for couchbase server to become available`, Cloud Native Gateway has not yet connected to the cluster.
2. Verify DNS resolution:  
```console  
$ kubectl run -it --rm debug --image=busybox -- nslookup <service-name>  
```
3. Check load balancer health status in your cloud provider's console.

### [](#authentication-failed-unauthenticated)Authentication Failed (UNAUTHENTICATED)

**Symptoms:**

* gRPC status code `UNAUTHENTICATED`.
* Data API returns HTTP 401.
* Cloud Native Gateway logs show `invalid credentials` or `failed to check credentials with cbauth`.

**Causes:**

* Incorrect username or password.
* User does not exist in the Couchbase cluster.
* Cloud Native Gateway cannot reach the Couchbase management service.
* Client certificate authentication failure (invalid certificate, CA not configured).

**Resolution:**

1. Verify credentials are correct by testing against the Couchbase management UI or REST API directly.
2. Check cbauth status in Cloud Native Gateway logs:  
```console  
$ kubectl logs pod/<pod-name> -c cloud-native-gateway | grep -i "cbauth"  
```
3. For client certificate issues, verify the client CA is configured and the certificate is signed by it:  
```console  
$ openssl verify -CAfile client-ca.crt client.crt  
```

## [](#diagnostic-tools)Diagnostic Tools

Use these tools to isolate connection issues and verify where the problem occurs. Check whether the issue is in the client, network path, load balancer, or Cloud Native Gateway itself.

### [](#grpcurl)grpcurl

[grpcurl](https://github.com/fullstorydev/grpcurl) is invaluable for diagnosing Cloud Native Gateway connectivity:

```console
# Check health
$ grpcurl --insecure -proto health.proto \
    -d '{"service": ""}' \
    localhost:18098 grpc.health.v1.Health/Check

# List available services
$ grpcurl --insecure localhost:18098 list

# Test with authentication
$ grpcurl --insecure \
    -H "Authorization: Basic $(echo -n 'user:pass' | base64)" \
    localhost:18098 list
```

### [](#curl-data-api)curl (Data API)

Test the Data API endpoint:

```console
# Check caller identity
$ curl -k -u user:pass https://localhost:18099/v1/callerIdentity

# Test document access
$ curl -k -u user:pass \
    https://localhost:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/airline_10
```

### [](#kubectl-port-forward)kubectl Port-Forward

Bypass the load balancer to test a specific Cloud Native Gateway instance directly:

```console
$ kubectl port-forward pod/<pod-name> 18098:18098 18099:18099
```

This is useful for isolating whether an issue is at the load balancer or the Cloud Native Gateway instance level.