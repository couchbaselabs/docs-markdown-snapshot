---
title: SDK Compatibility With Capella
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/reference/pages/sdk-compatibility.adoc
  xref: xref:cloud:reference:sdk-compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/reference/sdk-compatibility.html)

# SDK Compatibility With Capella

> [!IMPORTANT]
> If you are connecting from _IPv6-only_ environment, you cannot connect to Couchbase Capella as you are unable to use the IPv4 records published for Capella clusters.

Couchbase Capella works with the latest versions of _all_ supported [Couchbase SDKs](../../home/sdk.md).

The following minimum versions of Couchbase SDKs are supported by Capella (everything released later than these is also supported).

| SDK                    | Minimum Version                                                        | **Recommended** Version                                                |
| ---------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| C SDK (_libcouchbase_) | [3.3.14](../../c-sdk/current/hello-world/start-using-sdk.md) and up.   | [3.3.18](../../c-sdk/current/hello-world/start-using-sdk.md) and up.   |
| C++ SDK                | [1.0.0](../../cxx-sdk/1.0/hello-world/overview.md) and up.             | [1.2.0](../../cxx-sdk/1.2/hello-world/overview.md) and up.             |
| .NET                   | [3.5.3](../../dotnet-sdk/3.5/hello-world/start-using-sdk.md) and up.   | [3.8.0](../../dotnet-sdk/3.8/hello-world/start-using-sdk.md) and up.   |
| Go                     | [2.8.0](../../go-sdk/2.8/hello-world/start-using-sdk.md) and up.       | [2.11.0](../../go-sdk/2.11/hello-world/start-using-sdk.md) and up.     |
| Java                   | [3.6.0](../../java-sdk/3.6/hello-world/start-using-sdk.md) and up.     | [3.11.0](../../java-sdk/3.10/hello-world/start-using-sdk.md) and up.   |
| Kotlin                 | [1.3.0](#1.3@java-sdk:hello-world:start-using-sdk.adoc) and up.        | [3.10.0](../../java-sdk/3.10/hello-world/start-using-sdk.md) and up.   |
| Node.js                | [4.3.0](../../nodejs-sdk/4.3/hello-world/start-using-sdk.md) and up.   | [4.6.0](../../nodejs-sdk/4.6/hello-world/start-using-sdk.md) and up.   |
| PHP                    | [4.2.0](../../php-sdk/4.2/hello-world/start-using-sdk.md) and up.      | [4.4.0](../../php-sdk/4.4/hello-world/start-using-sdk.md) and up.      |
| Python                 | [4.2.0](../../python-sdk/4.2/hello-world/start-using-sdk.md) and up.   | [4.5.0](../../python-sdk/4.5/hello-world/start-using-sdk.md) and up.   |
| Ruby                   | [3.5.0](../../ruby-sdk/3.5/hello-world/start-using-sdk.md) and up.     | [3.7.0](../../ruby-sdk/3.7/hello-world/start-using-sdk.md) and up.     |
| Rust                   | [1.0.0](../../rust-sdk/current/hello-world/start-using-sdk.md) and up. | [1.0.0](../../rust-sdk/current/hello-world/start-using-sdk.md) and up. |
| Scala                  | [1.6.0](../../scala-sdk/1.6/hello-world/overview.md) and up.           | [3.10.0](../../scala-sdk/3.10/hello-world/overview.md) and up.         |

We _strongly advise_ using the latest version of your preferred SDK. The recommended versions (other than the C SDK) carry the client certificate for Capella, simplifying connection to the Free Tier. Recent versions carry updates specifically for working with Capella, and new features such as Vector GSI — see the [SDK Release Notes](../../java-sdk/current/project-docs/sdk-release-notes.md) for details.

Ideally, the client code should be running in the same LAN-like network (e.g. AWS Availability Zone) as the Couchbase Server nodes, although for development this is often not practical. See more on this in each SDK's pages on [compatibility](../../java-sdk/current/project-docs/compatibility.md#network-requirements), settings for [Constrained Network Environments](../../java-sdk/current/ref/client-settings.md#commonly-used-options), and details of [Managing Connections](../../java-sdk/current/howtos/managing-connections.md#working-in-the-cloud).