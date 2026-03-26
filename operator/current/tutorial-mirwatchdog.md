---
title: Monitor for Manual Intervention Scenarios
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/tutorial-mirwatchdog.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:operator::tutorial-mirwatchdog.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/tutorial-mirwatchdog.html)

# Monitor for Manual Intervention Scenarios

> Use the Manual Intervention Required Watchdog to monitor cluster scenarios and alert you when the Operator cannot automatically resolve them. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#overview)Overview

The Operator automatically resolves most cluster issues without user involvement. However, some scenarios fall outside the Operator's control and require manual intervention. The Manual Intervention Required (MIR) Watchdog monitors for these scenarios and places the cluster into a special MIR state when they occur, alerting you to take action.

### [](#enable-the-manual-intervention-required-watchdog)Enable the Manual Intervention Required Watchdog

Enable the Manual Intervention Required Watchdog for each cluster in the `CouchbaseCluster` CRD (Custom Resource Definitions).

```yaml
spec:
  mirWatchdog:
    enabled: true (1)
    interval: 20s (2)
    skipReconciliation: false (3)
```

| **1** | Enable the Manual Intervention Required Watchdog. The default value is false.                                                   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Set the interval at which the Manual Intervention Required Watchdog checks for MIR conditions. The default value is 20 seconds. |
| **3** | Specify whether the Operator skips reconciliation when the cluster is in the MIR state. The default value is false.             |

#### [](#alerting)Alerting

The Manual Intervention Required Watchdog is designed to work with additional alerting based on Kubernetes events, cluster conditions, or metrics.

When a cluster enters the MIR state, the Operator performs the following actions:

* Sets the `cluster_manual_intervention` gauge metric to 1.
* Adds the `ManualInterventionRequired` condition to the cluster, when possible, and includes a message that explains the reason for cluster entering the MIR state.
* Raises a `ManualInterventionRequired` Kubernetes event with a message that describes the reason for manual intervention.
* Optionally skips reconciliation based on the `spec.mirWatchdog.skipReconciliation` setting until you resolve the issue that caused the MIR state.

#### [](#manual-intervention-required-scenarios)Manual Intervention Required Scenarios

For each check that the Manual Intervention Required Watchdog performs, the defined entry and exit conditions determine whether the cluster enters or exits the MIR state.

The supported Manual Intervention Required Watchdog checks are as follows:

* [Consecutive Rebalance Failures](#consecutive-rebalance-failures)
* [Couchbase Cluster Authentication Failure](#couchbase-cluster-authentication-failure)
* [Down Nodes when Quorum is Lost](#down-nodes-when-quorum-is-lost)
* [TLS Certificate Expiration](#tls-certificate-expiration)

##### [](#consecutive-rebalance-failures)Consecutive Rebalance Failures

* Entry: After the Operator exhausts all rebalance retry attempts in 3 consecutive reconciliation loops.
* Exit: After the cluster becomes balanced and the Operator activates all nodes.

##### [](#couchbase-cluster-authentication-failure)Couchbase Cluster Authentication Failure

* Entry: The Operator fails to authenticate with the cluster by using the provided Couchbase cluster credentials.
* Exit: The Operator succeeds to authenticate with the cluster.

##### [](#down-nodes-when-quorum-is-lost)Down Nodes when Quorum is Lost

* Entry: The Operator detects down nodes that it cannot recover.
* Exit: The Operator detects no unrecoverable down nodes.

##### [](#tls-certificate-expiration)TLS Certificate Expiration

* Entry: The Operator detects an expired CA (Certificate Authority), Client or Server Certificate chain, and finds no valid alternative certificates for rotation.
* Exit: The Operator detects no expired TLS certificates or identifies valid alternative certificates available for rotation.