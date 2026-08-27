---
title: SDK Compatibility Issues
description: Troubleshooting compatibility issues between Couchbase SDKs and
  Cloud Native Gateway, including connection scheme errors, unsupported
  operations, and version requirements.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/troubleshooting/pages/SDK-compatibility-issues.adoc
  xref: xref:cloud-native-gateway:troubleshooting:SDK-compatibility-issues.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/troubleshooting/SDK-compatibility-issues.html)

# SDK Compatibility Issues

> Troubleshooting compatibility issues between Couchbase SDKs and Cloud Native Gateway, including connection scheme errors, unsupported operations, and version requirements. 

## [](#connection-scheme)Connection Scheme

When connecting through Cloud Native Gateway, you must use the correct connection scheme. This section covers common connection scheme issues and how to resolve them.

### [](#using-the-wrong-connection-scheme)Using the Wrong Connection Scheme

**symptom:**SDK connects but operations fail with unexpected errors, or the SDK connects directly to Couchbase Server instead of Cloud Native Gateway.

**cause:**The connection string uses `couchbase://` or `couchbases://` instead of `couchbase2://`.

**resolution:**When connecting through Cloud Native Gateway, the SDK must use the `couchbase2://` connection scheme:

```none
// Correct - connects via Cloud Native Gateway using Couchbase2
couchbase2://cng.example.com

// Incorrect - connects directly to Couchbase Server using classic protocol
couchbase://cng.example.com
couchbases://cng.example.com
```

The `couchbase2://` scheme tells the SDK to use the Couchbase2 gRPC protocol instead of the traditional memcached binary protocol.

### [](#sdk-does-not-recognize-couchbase2)SDK Does Not Recognize couchbase2://

**symptom:**SDK throws a `scheme not recognized` or `invalid connection string` error.

**cause:**The SDK version does not support the Couchbase2 protocol.

**resolution:**Upgrade to a Couchbase SDK version that supports `couchbase2://`:

| SDK    | Minimum Version |
| ------ | --------------- |
| .NET   | 3.9.0 ①         |
| Go     | 2.7.0           |
| Java   | 3.5.0           |
| Kotlin | 1.2.0           |
| PHP    | 4.2.0 ②         |
| Ruby   | 3.5.0 ②         |
| Scala  | 1.5.0           |

| **1** | 3.9.0 introduced full support for Cloud Native Gateway. Versions from 3.5.1 provide some compatibility.                                                                                                                                                                     |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | PHP and Ruby currently continue to mark this feature's [stability level](../../../php-sdk/current/project-docs/compatibility.md#sdk-api-stability) as uncomitted. Nevertheless, feature implementation is reasonaby complete, and the API unlikely to change significantly. |

If your SDK version is older, you must upgrade before using Cloud Native Gateway. Direct SDK connections to the Couchbase cluster (using the classic `couchbase://` or `couchbases://` scheme) remain fully supported in parallel with Cloud Native Gateway.

## [](#unsupported-operations)Unsupported Operations

Cloud Native Gateway supports a large subset of SDK operations, but does not expose every feature through the Couchbase2 interface. Use the following guidance to determine whether Cloud Native Gateway supports the operation and identify practical alternatives.

### [](#operation-returns-unimplemented)Operation Returns UNIMPLEMENTED

**symptom:**SDK operation fails with gRPC status code `UNIMPLEMENTED`.

**cause:**The requested operation is not yet implemented in the Cloud Native Gateway Couchbase2 interface.

**resolution:**Check the [Supported and Unsupported Capabilities](../intro/supported-unsupported-capabilities.md) page for the current list of supported operations. Operations that are not yet available through Cloud Native Gateway include:

* Views
* Eventing
* Some advanced administrative operations

If the operation is critical to your application, use a direct SDK connection (`couchbase://`) for that specific operation while using Cloud Native Gateway for other operations. Both connection types can coexist in the same application.

### [](#legacy-durability-not-available)Legacy Durability Not Available

**symptom:**SDK reports that legacy (observe-based) durability is not supported.

**cause:**Cloud Native Gateway does not support the legacy durability mechanism. Only synchronous durability (introduced in Couchbase Server 6.5) is available through Couchbase2.

**resolution:**Use synchronous durability levels instead of legacy durability:

```java
// Instead of legacy durability:
// collection.upsert(id, doc, UpsertOptions.upsertOptions().durability(PersistTo.ONE, ReplicateTo.ONE));

// Use synchronous durability:
collection.upsert(id, doc, UpsertOptions.upsertOptions().durability(DurabilityLevel.MAJORITY));
```

Available durability levels through Cloud Native Gateway:

* `NONE` — No durability requirement (default).
* `MAJORITY` — Mutation must be replicated to a majority of replicas.
* `MAJORITY_AND_PERSIST_TO_ACTIVE` — Majority replication plus persistence to active node's disk.
* `PERSIST_TO_MAJORITY` — Mutation must be persisted to disk on a majority of replicas.

## [](#error-mapping-differences)Error Mapping Differences

When requests pass through Cloud Native Gateway, it translates errors between Couchbase Server responses, gRPC status codes, and SDK-specific exceptions. Use the following section to map these differences to their semantic meaning.

### [](#different-error-types-from-expected)Different Error Types From Expected

**symptom:**The SDK returns different error types or error codes from expected based on experience with direct connections.

**cause:**Cloud Native Gateway maps native Couchbase errors to gRPC status codes, which the SDK then maps back to SDK error types. The mapping is semantically equivalent but the specific error chain may differ.

**resolution:**Handle errors by their semantic meaning rather than specific error types:

* `NOT_FOUND` → Document does not exist.
* `ALREADY_EXISTS` → Document already exists (on insert).
* `FAILED_PRECONDITION` → CAS mismatch, document locked, or similar state conflict.
* `PERMISSION_DENIED` → Insufficient RBAC permissions.
* `INVALID_ARGUMENT` → Malformed request parameters.
* `DEADLINE_EXCEEDED` → Operation timed out.
* `UNAVAILABLE` → Transient service unavailability (may include redirect information).

### [](#missing-retry-context)Missing Retry Context

**symptom:**SDK retry strategies behave differently from those with direct connections.

**cause:**With Cloud Native Gateway, some retries happen server-side (inside Cloud Native Gateway or the Couchbase cluster) rather than client-side. The SDK may see fewer retryable errors because Cloud Native Gateway has already handled them.

**resolution:**This is expected behavior. Cloud Native Gateway handles transient errors such as `NOT_MY_VBUCKET` internally and only surfaces errors to the client when Cloud Native Gateway itself cannot resolve them. The SDK's retry strategy still applies to errors that reach the client.

## [](#server-version-compatibility)Server Version Compatibility

Cloud Native Gateway validates the connected Couchbase Server version at startup. Use the following section to interpret the warning and determine the required upgrade path.

### [](#cloud-native-gateway-warns-about-unsupported-server-version)Cloud Native Gateway Warns About Unsupported Server Version

**symptom:**Cloud Native Gateway logs a warning: `stellar-gateway does not support cluster server version`.

**cause:**The Couchbase Server version is older than 7.2.2.

**resolution:**Upgrade Couchbase Server to version 7.2.2 or later. While Cloud Native Gateway may partially function with earlier versions, it's not tested or supported.

## [](#debugging-sdk-cloud-native-gateway-communication)Debugging SDK-Cloud Native Gateway Communication

To diagnose issues at the SDK level:

### [](#enable-sdk-verbose-logging)Enable SDK Verbose Logging

Most Couchbase SDKs support verbose/debug logging that shows the individual Couchbase2 RPC calls:

```java
// Java
System.setProperty("com.couchbase.client.core.logging.level", "DEBUG");
```

```go
// Go
cluster, err := gocb.Connect("couchbase2://cng.example.com",
    gocb.ClusterOptions{
        Username: "user",
        Password: "pass",
    },
)
```

### [](#capture-grpc-traffic)Capture gRPC Traffic

For detailed protocol-level debugging, use gRPC reflection or a gRPC-aware proxy to inspect Couchbase2 messages between the SDK and Cloud Native Gateway.