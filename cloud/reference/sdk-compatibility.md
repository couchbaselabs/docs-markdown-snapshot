[View original HTML](/cloud/reference/sdk-compatibility.html)

|  | If you are connecting from _IPv6-only_ environment, you cannot connect to Couchbase Capella as you are unable to use the IPv4 records published for Capella clusters. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Couchbase Capella works with the latest versions of _all_ supported [Couchbase SDKs](#home:ROOT:sdk.adoc).

The following minimum versions of Couchbase SDKs are supported by Capella (everything released later than these is also supported).

| SDK                    | Minimum Version                                                     | **Recommended** Version                                              |
| ---------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| C SDK (_libcouchbase_) | [3.3.0](../../c-sdk/current/hello-world/start-using-sdk.md) and up. | [3.3.14](../../c-sdk/current/hello-world/start-using-sdk.md) and up. |
| C++ SDK                | [1.0.0](../../cxx-sdk/1.0/hello-world/overview.md) and up.          | [1.0.4](../../cxx-sdk/1.0/hello-world/overview.md) and up.           |
| .NET                   | [3.5.3](#3.5@dotnet-sdk:hello-world:start-using-sdk.adoc) and up.   | [3.6.3](../../dotnet-sdk/3.6/hello-world/start-using-sdk.md) and up. |
| Go                     | [2.6.0](#2.6@go-sdk:hello-world:start-using-sdk.adoc) and up.       | [2.9.3](../../go-sdk/2.9/hello-world/start-using-sdk.md) and up.     |
| Java                   | [3.4.0](#3.4@java-sdk:hello-world:start-using-sdk.adoc) and up.     | [3.7.4](#3.7@java-sdk:hello-world:start-using-sdk.adoc) and up.      |
| Kotlin                 | [1.1.0](#1.1@java-sdk:hello-world:start-using-sdk.adoc) and up.     | [1.3.0](#1.3@java-sdk:hello-world:start-using-sdk.adoc) and up.      |
| Node.js                | [4.2.0](#4.2@nodejs-sdk:hello-world:start-using-sdk.adoc) and up.   | [4.4.4](../../nodejs-sdk/4.4/hello-world/start-using-sdk.md) and up. |
| PHP                    | [4.1.0](#4.1@php-sdk:hello-world:start-using-sdk.adoc) and up.      | [4.2.2](../../php-sdk/4.2/hello-world/start-using-sdk.md) and up.    |
| Python                 | [4.1.0](#4.1@python-sdk:hello-world:start-using-sdk.adoc) and up.   | [4.3.4](../../python-sdk/4.3/hello-world/start-using-sdk.md) and up. |
| Ruby                   | [3.4.0](#3.4@ruby-sdk:hello-world:start-using-sdk.adoc) and up.     | [3.5.2](../../ruby-sdk/3.5/hello-world/start-using-sdk.md) and up.   |
| Scala                  | [1.4.0](#1.4@scala-sdk:hello-world:overview.adoc) and up.           | [1.6.0](#1.6@scala-sdk:hello-world:overview.adoc) and up.            |

We _strongly advise_ using the latest version of your preferred SDK. The recommended versions (other than the C SDK) carry the client certificate for Capella, simplifying connection during free tier. Recent versions carry updates specifically for working with Capella — see the [SDK Release Notes](../../nodejs-sdk/current/project-docs/sdk-release-notes.md) for details.

Ideally, the client code should be running in the same LAN-like network (e.g. AWS Availability Zone) as the Couchbase Server nodes, although for development this is often not practical. See more on this in each SDK’s pages on [compatibility](../../java-sdk/current/project-docs/compatibility.md#network-requirements), settings for [Constrained Network Environments](../../java-sdk/current/ref/client-settings.md#commonly-used-options), and details of [Managing Connections](../../java-sdk/current/howtos/managing-connections.md#working-in-the-cloud).