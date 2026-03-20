---
title: Client Settings
description: Client settings
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/ref/pages/client-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.2@php-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/ref/client-settings.html)

# Client Settings

> Client settings 

> [!TIP]
> The backend implementation of client settings changed substantially in 4.0\. Full details can be found in [the API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.0.0/classes/Couchbase-ClusterOptions.html).

Unresolved include directive in modules/ref/pages/client-settings.adoc - include::7.5@sdk:shared:partial$client-settings-nowait.adoc\[\]

## [](#configuration-profiles)Configuration Profiles

Configuration Profiles provide predefined client settings that allow you to quickly configure an environment for common use-cases. When using a configuration profile, the current client settings are overridden with the values provided in the profile. Any property that is not specified in the profile is left unchanged.

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#wan-development)WAN Development

**Cluster Option:** `applyProfile("wan_development")`

A `wan_development` configuration profile can be used to modify client settings for development or high-latency environments. This profile changes the default timeouts.

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