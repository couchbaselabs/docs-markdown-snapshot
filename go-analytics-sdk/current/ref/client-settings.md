---
title: Client Settings
description: Change the SDK's behavior by configuring client settings.
editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:go-analytics-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-analytics-sdk/current/ref/client-settings.html)

# Client Settings

> Change the SDK’s behavior by configuring client settings. 

Almost all configuration for the SDK can be specified through the `ClusterOptions` which are passed to the `cbanalytics.Connect` call in the SDK.

## [](#configure-with-code)Configure with Code

To configure SDK client settings by writing code, provide an options block when creating the `Cluster` instance. Here’s an example that configures several settings by passing the optional third argument to `cbanalytics.NewCluster()`:

```go
	cluster, err := cbanalytics.NewCluster(
		connStr,
		cbanalytics.NewBasicAuthCredential(username, password),
		cbanalytics.NewClusterOptions().
			SetTimeoutOptions(
				cbanalytics.NewTimeoutOptions().
					SetConnectTimeout(30*time.Second).
					SetQueryTimeout(2*time.Minute),
			),
	)
	handleErr(err)
```

Note: Options blocks can created using builder-style functions, like above, or by assigning to the struct fields directly.

> [!TIP]
> You don’t need to call every method in the above example; call only the methods where you want to override the client setting’s default value.

## [](#configure-with-connection-string)Configure with Connection String Parameters

Another way to configure client settings is to include parameters in the connection string. Here is an example connection string with two parameters:

```none
https://example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m
```

If the same parameter name appears in the connection string more than once, the SDK uses the rightmost value.

If the same client setting is specified both in code and in the connection string, the SDK uses the value in the connection string.

> [!TIP]
> If your application reads the connection string from a config file (or other external source), you can change the connection string to override client settings without having to recompile your code.

### [](#durations)Durations

For client settings that represent durations, the connection string parameter’s value is specified using the format accepted by [Golang’s time.ParseDuration](https://pkg.go.dev/time#ParseDuration) method.

> A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", and "h".

Note that although the Golang syntax allows negative durations, the SDK rejects non-positive timeout durations.

### [](#booleans)Booleans

For boolean client settings, the SDK expects the connection string parameter value to be `true` or `false` (case-sensitive).

## [](#client-settings-reference)Client Settings Reference

This section describes all client settings supported by the SDK.

### [](#timeout-options)Timeout Options

Configuring timeouts gives you control over how long the SDK waits for operations to succeed or fail.

| Connection string parameter | Default value    | Description                                                                                                                    |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| timeout.connect\_timeout    | 10s (10 seconds) | Time limit for establishing a network connection. Indirectly controls SDK bootstrap timeout, which is 1.5 times this duration. |
| timeout.query\_timeout      | 10m (10 minutes) | Default query execution time limit for executing the query when no deadline is applied by context.Context at the query level.  |

### [](#security-options)Security Options

The SDK is secure by default. You probably won’t need to configure the SDK’s security options unless:

* You have special security compliance requirements that restrict the set of allowed TLS cipher suites.
* You are a Couchbase employee working with an internal non-production hosted service, or a local server installation.

| Connection string parameter     | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| security.trust\_only\_pem\_file | N/A           | Filesystem path of the PEM-encoded root certificate(s) to trust instead of the Couchbase Capella certificate authority (CA) root certificate bundled with the SDK. In the unlikely event the Couchbase Capella CA is compromised, you can use this to point the SDK at an updated CA certificate without having to immediately upgrade to a new version of the SDK (which will include the updated CA certificate and trust it by default). |

#### [](#danger-zone)Danger Zone

Finally, there is one security option whose use is strongly discouraged in nearly all circumstances. Setting `security.disable_server_certificate_verification` to `true` allows the SDK to connect to any server, regardless of whether the server presents a certificate trusted by the SDK.

> [!CAUTION]
> Disabling server certificate verification is roughly equivalent to sending your credentials and all data over an insecure connection. Don’t do this unless connecting to a server running locally on your development machine.

### [](#unmarshaler)Unmarshaler

The SDK uses a component called an `Unmarshaler` to convert query result rows into Go typed. The default implementation is `JSONUnmarshaler`, a thin wrapper around `json.Unmarshal` from `"encoding/json"`.

This cluster option specifies the _default_ unmarshaler. You can override the unmarshaler for a specific query by setting the `Unmarshaler` query option when executing the query.

#### [](#custom-unmarshalers)Custom unmarshalers

Implement the `Unmarshaler` interface to add support for other JSON processing libraries.