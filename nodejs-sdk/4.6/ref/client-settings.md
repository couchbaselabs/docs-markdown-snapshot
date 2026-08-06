---
title: Client Settings
description: Client settings
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/ref/pages/client-settings.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.6@nodejs-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.6/ref/client-settings.html)

# Client Settings

> Client settings 

> [!TIP]
> The backend implementation of client settings changed substantially in 4.0\. Full details can be found in [the API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/ConnectOptions.html).

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

## [](#configuration-profiles)Configuration Profiles

Configuration Profiles provide predefined client settings that allow you to quickly configure an environment for common use-cases. When using a configuration profile, the current client settings are overridden with the values provided in the profile. Any property that is not specified in the profile is left unchanged.

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#wan-development)WAN Development

**Cluster Method:** `applyProfile("wanDevelopment")`

A `wanDevelopment` configuration profile can be used to modify client settings for development or high-latency environments. This profile changes the default timeouts.

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