---
title: What&#8217;s New?
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/whats-new.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/whats-new.html)

# What&#8217;s New?

Autonomous Operator 2.6 release is primarily focused on platform updates, feature parity with Couchbase Server, improvements to Pod Management and Security, as well as a number of minor fixes.

## [](#immediate-backups)Immediate Backups

It is now possible to run a CouchbaseBackup resource immediately via the new immediate\_full and immediate\_incremental backup strategies.

See [Configure Backups](howto-backup.md#configure-backups) for futher details.

## [](#improved-pod-management)Improved Pod Management

Couchbase Operator now takes into consideration data topography and Couchbase Server version when determining which pods to scale down.

## [](#log-uploads)Log Uploads

There are new parameters that can be passed to the `cao collect-logs` command that will automatically upload the logs to Couchbase Support.

See [Cao Collect Logs](tools/cao.md#cao-collect-logs) for further details.

## [](#delta-recovery-upgrades)Delta Recovery Upgrades

Couchbase Clusters can now be configured to perform a Delta-Recovery upgrades. This upgrade is considerably faster than the current SwapRebalance method.

See [Upgrade Process](#resources/couchbasecluster.adoc#couchbaseclusters-spec-upgradeProcess) for further details

## [](#quality-of-life-improvements)Quality of Life Improvements

Added an onlineExpansionTimeout to Couchbase Cluster to specify the number of minutes operator should wait before falling back to a rolling upgrade when volume expansion fails. Added annotations to better help integrations with Prometheus. Added platform specific zone labels to persistent volume claims for EKS, GKE and AKS.

## [](#pod-readiness-delay-and-pod-readiness-period)Pod Readiness Delay and Pod Readiness Period

Added pod readiness delay and pod readiness period parameters to the `cao create operator` command. These will be applied to all Couchbase Server pods created by the operator.

See [Cao Create Operator](tools/cao.md#cao-create-operator) for further details.

## [](#cloud-native-gateway-from-couchbase-autonomous-operator-2-6-1)Cloud Native Gateway (from Couchbase Autonomous Operator 2.6.1)

The Couchbase _Cloud Native Gateway_ (CNG) is a new component that allows applications to access Couchbase through a set of RPC network endpoints based on [gRPC](https://grpc.io/), a [Cloud Native Computing Foundation](https://cncf.io/) project.

See [Cloud Native Gateway](concept-cloud-native-gateway.md) for details.