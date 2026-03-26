---
title: Compatibility
editUrl: https://github.com/couchbase/docs-elastic-search/edit/main/modules/ROOT/pages/compatibility.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:elasticsearch-connector::compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/elasticsearch-connector/current/compatibility.html)

# Compatibility

Legend

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade to a supported version.
* ✔ **Supported**: This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

## [](#operating-system)Operating System

Linux is required for production deployments.

macOS is fine for experimentation and development, but is not officially supported.

Windows is completely untested and unsupported.

## [](#elasticsearch)Elasticsearch

Elasticsearch version support is informed by [Elastic product end of life dates](https://www.elastic.co/support/eol).

|                | Connector |
| -------------- | --------- |
| Elasticsearch↓ | 4.4       |
| 8.0 - 9.0      | ✔         |
| 7.17           | ✔         |

## [](#opensearch)OpenSearch

> [!CAUTION]
> This is an experimental feature. If you'd like to share feedback, please post in the [Elasticsearch category](https://forums.couchbase.com/c/elasticsearch-connector/36) on the Couchbase Forum.

OpenSearch version support is informed by the [OpenSearch Maintenance Policy](https://opensearch.org/releases.html#maintenance-policy).

|                | Connector       |
| -------------- | --------------- |
| OpenSearch↓    | 4.4.5 and later |
| 2.0.0 - 2.18.0 | ✔               |
| 1.3.14         | ✔               |
| 1.3.3 - 1.3.13 | ◎               |
| 1.0.0 - 1.3.2  | ✖               |

## [](#elastic-cloud)Elastic Cloud

> [!CAUTION]
> This is an experimental feature. If you'd like to share feedback, please post in the [Elasticsearch category](https://forums.couchbase.com/c/elasticsearch-connector/36) on the Couchbase Forum.

Connector versions 4.4.5 and later are compatible with Elastic Cloud.

See [how to configure the connector for Elastic Cloud](configuration.md#elastic-cloud).

## [](#amazon-opensearch-service)Amazon OpenSearch Service

> [!CAUTION]
> This is an experimental feature. If you'd like to share feedback, please post in the [Elasticsearch category](https://forums.couchbase.com/c/elasticsearch-connector/36) on the Couchbase Forum.

Connector versions 4.4.5 and later are compatible with Amazon OpenSearch Service.

See [how to configure the connector for Amazon OpenSearch Service](configuration.md#amazon-opensearch-service).

## [](#couchbase-capella)Couchbase Capella

Connector versions 4.2.4 and later are compatible with Couchbase Capella.

See [how to configure the connector for Couchbase Capella](configuration.md#couchbase-capella).

## [](#couchbase-server)Couchbase Server

The connector is compatible with Couchbase Server Enterprise Edition and Couchbase Server Community Edition.

|               | Connector |
| ------------- | --------- |
| Couchbase↓    | 4.4       |
| 7.0 and later | ✔         |
| 5.0 - 6.6     | ◎         |
| < 5.0         | ✖         |

\* If you've been using an earlier version of Couchbase, you can upgrade to Couchbase 7 and everything will continue working as before. To take advantage of the Scopes and Collections introduced in Couchbase 7, please upgrade the connector to version 4.3 or later.

## [](#java)Java

Java 11 or later is required.

|                              | Connector |
| ---------------------------- | --------- |
| Java↓                        | 4.4       |
| OpenJDK 17 (Eclipse Temurin) | ✔         |
| OpenJDK 11 (Eclipse Temurin) | ✔         |

## [](#consul)Consul

Only required for Autonomous Operations mode.

|         | Connector |                 |
| ------- | --------- | --------------- |
| Consul↓ | 4.4.0     | 4.4.1 and later |
| 1.19.1  | ✖         | ✔               |
| 1.17.1  | ✖         | ✔               |
| 1.15.1  | ✖         | ✔               |
| 1.14.3  | ✖         | ✔               |
| 1.13.1  | ✖         | ✔               |
| 1.12.4  | ✖         | ✔               |
| 1.11.8  | ✖         | ✔               |
| 1.10.12 | ✖         | ◎               |
| 1.9.1   | ✔         | ◎               |
| 1.5.3   | ✔         | ◎               |