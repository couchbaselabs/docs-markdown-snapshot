---
title: Client Settings
description: Client settings using <code>ConnectOptions</code> for
  bootstrapping, timeouts, reliability, and performance.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/ref/pages/client-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:go-sdk:ref:client-settings.adoc[]
---

[View original HTML](/go-sdk/current/ref/client-settings.html)

# Client Settings

> Client settings using `ConnectOptions` for bootstrapping, timeouts, reliability, and performance. 

Almost all configuration for the SDK can be specified through the ConnectOptions which are passed to the `gocb.Connect` call in the SDK. In addition to this, as with SDK 2.0, the majority of these options can also be specified through the connection string.

## [](#general-options)General Options

These options specify the general configuration options for the client.

Name: **Authenticator**

Default: `nil`

Set this to the authenticator you wish to use to authenticate with the server. Possible options which are included in the SDK include the PasswordAuthenticator and CertificateAuthenticator.

Name: **Username / Password**

Default: `nil` / `nil`

Username and Password provide a shortcut to creating a PasswordAuthenticator which is then used as an Authenticator for connecting to the Cluster.

Name: **Transcoder**

Default: `JSONTranscoder{}`

Transcoder specifies the transcoding behaviour that is required of the application. By default this is configured as a JSONTranscoder, which will encode all values through the standard Go JSON marshalling facilities.

Name: **RetryStrategy**

Default: `BestEffortRetryStrategy{}`

The retry strategy decides if an operation should be retried or canceled. While implementing a custom strategy is fairly advanced, the SDK ships with a best effort retry strategy out of the box (BestEffortRetryStrategy). This default will retry the operation until it either succeeds or the maximum request lifetime is reached.

Name: **unordered\_execution\_enabled**

Default: `true`

From Couchbase 7.0, Out-of-Order execution allows the server to concurrently handle multiple requests on the same connection, potentially improving performance for durable writes and multi-document ACID transactions. This means that tuning the number of connections (KV endpoints) is no longer necessary as a workaround where data not available in the cache is causing timeouts.

Note, this can only be specified through the query string.

This is set to `true` by default. Note, changing the setting will only affect Server versions 7.0 onwards.

## [](#security-options)Security Options

By default the client will connect to Couchbase Server using an unencrypted connection. If you are using the Enterprise Edition, it’s possible to secure the connection using TLS by specifying these options in conjunction with a `couchbase://` connecting string scheme.

Name: **TLSRootCAs**

Default: `nil`

TLSRootCAs enables the specification of the Root Certificate’s to use when validating a server certificate on the client-side.

Name: **TLSSkipVerify**

Default: `false`

This is an advanced option which can be used to disable TLS certificate validation. This will disable any form of server validation, but will still encrypt the data being settings between the SDK and the server. This option is intended strictly for use on older versions of Couchbase Server where strict validation was not possible.

## [](#orphan-reporting-options)Orphan Reporting Options

The Go SDK implements the ability to report when unexpected operation responses are received from the server. This primarily occurs when an operation is timed out and later received.

Name: **Disabled**

Default: `false`

Specifies whether orphan reporting should be disabled.

Name: **ReportInterval**

Default: `10s`

Specifies the duration between reporting of orphaned responses.

Name: **SampleSize**

Default: `10`

Specifies the number of samples of orphan responses that should be stored between reports.

## [](#circuit-breaker-options)Circuit Breaker Options

The Go SDK provides a built in circuit breaker system to enable the SDK to more quickly reject requests which are unlikely to succeed.

Name: **Disabled**

Default: `false`

…​

Name: **VolumeThreshold**

Default: `20`

The volume threshold defines how many operations must be in the window before the threshold percentage can be meaningfully calculated.

Name: **ErrorThresholdPercentage**

Default: `50`

The percentage of operations in a window that may fail before the circuit is opened. The value is an integer in the range \[0,100\].

Name: **SleepWindow**

Default: `5s`

The delay between when the circuit opens and when the canary is tried.

Name: **RollingWindow**

Default: `1m`

How long the window is in which the number of failed ops are tracked in a rolling fashion.

Name: **CanaryTimeout**

Default: `5s`

The period of time which canary operations are permitted to take before they are marked as a failure.

> [!TIP]
> Cloud Native Gateway
> 
> If using the `couchbase2://` connection protocol with [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway), note that circuit breaker options are not available when using this protocol. The connection protocol uses a separate queue per node, and thus avoids the main cause of possible cascading failure.

## [](#timeout-options)Timeout Options

Name: **ConnectTimeout**

Default: `10s`

The connect timeout is used when a Bucket is opened and if not overridden by a custom timeout. If you feel the urge to change this value to something higher, there is a good chance that your network is not properly set up. Connecting to the server should in practice not take longer than a second on a reasonably fast network.

Name: **KVTimeout**

Default: `2.5s`

The Key/Value default timeout is used on operations which are performed on a specific key if not overridden by a custom timeout. This includes all commands like get(), getFromReplica() and all mutation commands, but does not include operations that are performed with enhanced durability requirements.

> [!TIP]
> [Durable Write operations](../concept-docs/durability-replication-failure-considerations.md#synchronous-writes) have their own timeout setting, `KVDurableTimeout`, see below.

Name: **KVDurableTimeout**

Default: `10s`

Key/Value operations with enhanced durability requirements may take longer to complete, so they have a separate default timeout.

**Do not** set this above 65s, which is the maximum possible `SyncWrite` timeout on the Server side.

> [!WARNING]
> The `KVDurableTimeout` property is not part of the stable API and may change or be removed at any time.

Name: **ViewTimeout**

Default: `75s`

The View timeout is used on view operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows. Also, if there is a node failure during the request the internal cluster timeout is set to 60 seconds.

Name: **QueryTimeout**

Default: `75s`

The Query timeout is used on all [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **AnalyticsTimeout**

Default: `75s`

The Analytics timeout is used on all Analytics query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **SearchTimeout**

Default: `75s`

The Search timeout is used on all FTS operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **ManagementTimeout**

Default: `75s`

The management timeout is used on all cluster management APIs (BucketManager, UserManager, CollectionManager, QueryIndexManager, etc.) if not overridden by a custom timeout. The default is quite high because some operations (such as flushing a bucket, for example) might take a long time.

Name: **server\_wait\_backoff**

Default: `5s`

The `server_wait_backoff` is used across a cluster as the period of time waited between key/value reconnect attempts to a node after a connection failure occurs.

Note, this can only be specified through the connection string.

## [](#io-options)IO Options

Name: **DisableMutationTokens**

Default: `false`

This is an advanced option which will disable the inclusion of mutation tokens in operation responses from the server. This should generally not be set.

Name: **DisableServerDurations**

Default: `false`

This is an advanced option which will disable the inclusion of server processing times in operation responses from the server. This should generally not be set.

Name: **max\_perhost\_http\_connections**

Default: `0` (unlimited)

This setting sets a maximum on the number of HTTP connections per-host. There is no limit by default.

Note, this can only be specified through the connection string (and only from Go SDK 2.9.3 onwards).

## [](#commonly-used-options)Commonly Used Options

The defaults above have been carefully considered and in general it is not recommended to make changes without expert guidance or careful testing of the change. Some options may be commonly used together in certain envionments or to achieve certain effects.

### [](#constrained-network-environments)Constrained Network Environments

Though [wide area network](../project-docs/compatibility.md#network-requirements) (WAN) connections are not directly supported, some development and non-critical operations activities across a WAN are convenient. Most likely for connecting to Couchbase Capella, or Server running in your own cloud account, whilst developing from a laptop or other machine not located in the same data center. These settings are some you may want to consider adjusting:

* Connect Timeout to 30s
* Key-Value Timeout to 5s
* Config Poll Interval to 10s
* Circuit Breaker ErrorThresholdPercentage to 75

> [!NOTE]
> As of SDK API 3.4 you can also use a **Configuration Profile**, which allows you to quickly configure your environment for common use-cases. See the [Configuration Profiles](#configuration-profiles) section for more details.

A program using the SDK can also use the `waitUntilReady()` API call to handle all connection negotiations and related errors at one place. It may be useful to block in, for example, a basic console testing application for up to 30 seconds before proceeding in the program to perform data operations. See the API reference for further details.

## [](#configuration-profiles)Configuration Profiles

Configuration Profiles provide predefined client settings that allow you to quickly configure an environment for common use-cases. When using a configuration profile, the current client settings are overridden with the values provided in the profile. Any property that is not specified in the profile is left unchanged.

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#wan-development)WAN Development

**Setting:** `ClusterOptions`

**Method:** `ApplyProfile(gocb.ClusterConfigProfileWanDevelopment)`

A `ClusterConfigProfileWanDevelopment` configuration profile can be used to modify client settings for development or high-latency environments. This profile changes the default timeouts.

__Table 1\. Profile Settings__
| Setting             | Default Value | WAN Profile Value |
| ------------------- | ------------- | ----------------- |
| KvConnectTimeout    | 10s           | 20s               |
| kvTimeout           | 2.5s          | 20s               |
| kvDurabilityTimeout | 10s           | 20s               |
| ViewTimeout         | 75s           | 120s              |
| QueryTimeout        | 75s           | 120s              |
| AnalyticsTimeout    | 75s           | 120s              |
| SearchTimeout       | 75s           | 120s              |
| ManagementTimeout   | 75s           | 120s              |

**Do not** set `kvDurabilityTimeout` above 65s, which is the maximum possible `SyncWrite` timeout on the Server side.

## [](#cloud-native-gateway)Cloud Native Gateway

Using the [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway) protocol (to connect to Couchbase Server running on [Couchbase Autonomous Operator](../../../operator/current/concept-cloud-native-gateway.md) 2.6.1 or newer) should not need any changes to config.

Cloud Native Gateway should not need any changes to config. Some settings will be ignored — currently, these include:

* Compression
* `numKvConnections`