---
title: Couchbase Monitoring and Observability Stack
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cmos/current/index.html)

# Couchbase Monitoring and Observability Stack

> [!CAUTION]
> CMOS is provided as a Developer Preview. Developer Preview features and their use are subject to Couchbase’s “Non-GA Offering Supplemental Terms” set forth in the [License Agreement](https://www.couchbase.com/LA03012021). Developer Preview features may not be functionally complete and are not intended for production use. They are intended for development and testing purposes only.

The intention of this repository is to provide a simple, out-of-the-box solution based on industry standard tooling to observe the state of your Couchbase cluster.

* An additional requirement is to ensure we can integrate into existing observability pipelines people may already have as easily as possible.
* This must all support being deployed on-premise and on cloud platforms with minimal change.
* Any bespoke software must be minimal and ideally just restricted to configuration of generic tools.
* We should provide default configurations based on the best practices guidelines and support customers to customize what is "important" to monitor in their clusters.
* A simple and often upgrade pipeline to support frequent changes and updates to the solution which are then easy to roll out for users.

We essentially need to support two fairly distinct types of user:

1. Those who have nothing and just want a simple working solution to monitor their cluster.
2. Those who have an existing monitoring pipeline and want to integrate Couchbase monitoring into it, likely with a set of custom rules and configuration.

## [](#caveats-and-restrictions)Caveats and restrictions

* CMOS is built for Couchbase Server 7.0 and above. Lower versions are supported but some features might be missing. We intend to improve support for lower versions in future releases, however Couchbase Server 7.0 and above will remain the primary target of development.
* Limited cross-version compatibility by supporting migrating from previous version to latest version. Best efforts will be made but the intention is this iterates often and no backwards compatibility is provided. We will show how to migrate from X-1 to X but no more than that, users should be following an agile lifecycle of constant upgrade.
* CMOS is open source; however, the Couchbase Cluster Monitor is a closed source (private repository) component. If you are building from source, this component will require access to the repository to be included in the container. The container can be built without it by removing it and there is a [helper script](https://github.com/couchbaselabs/observability/tree/main/tools/build-oss-container.sh) that does this, however certain features (in particular Grafana dashboards) may not be fully functional without it. We plan to address this in a future release.

## [](#known-issues)Known Issues

CMOS is provided as a Developer Preview and may have bugs, missing features, or other issues. Below is an incomplete list of issues that we plan to address in a future release. To see the full list or report any issues you encounter, please check the JIRA board and Forums linked below.

* The landing page may not be fully functional on Mozilla Firefox ([CMOS-363](https://issues.couchbase.com/browse/CMOS-363))
* Grafana dashboards may show incorrect information if two clusters with the same name are added ([CMOS-203](https://issues.couchbase.com/browse/CMOS-203))
* Buckets may persist in dashboards after they are dropped ([CMOS-231](https://issues.couchbase.com/browse/CMOS-231))
* Prometheus scrape targets are not updated if nodes are added or removed from the cluster ([CMOS-106](https://issues.couchbase.com/browse/CMOS-106))
* When Couchbase Server is running in containers or on Kubernetes, CPU and memory statistics may display data from the host node rather than the container ([CMOS-233](https://issues.couchbase.com/browse/CMOS-233))

## [](#feedback-and-support)Feedback and support

Please use our official [JIRA board](https://issues.couchbase.com/projects/CMOS/issues) to report any bugs and issues with the appropriate components. We also encourage you to use the [Couchbase Forums](https://forums.couchbase.com) for posting any questions or feedback that you might have.

No official support is currently provided but best efforts will be made and we are keen to hear of any issues.

## [](#next-steps)Next steps

* [Architecture](architecture.md)
* [Microlith container deployment](deployment-microlith.md)
* [On-premise deployment](deployment-onpremise.md)