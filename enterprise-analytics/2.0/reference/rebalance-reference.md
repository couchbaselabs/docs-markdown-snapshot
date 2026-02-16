[View original HTML](/enterprise-analytics/2.0/reference/rebalance-reference.html)

> Enterprise Analytics creates a _report_ for every rebalance that is performed. This section explains how to obtain the report, and how to read it. 

## [](#Obtaining-a-rebalance-report)Obtaining a Rebalance Report

Enterprise Analytics automatically creates a _rebalance report_ for every rebalance that occurs on the cluster. The report’s content consists of a JSON document, which provides statistics for every service that has been involved in the rebalance. On conclusion of the rebalance, the report can be accessed in any of the following ways:

* By means of Couchbase Web Console, as described in [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).
* By means of the REST API, as described in [Getting Cluster Tasks](rest-get-cluster-tasks.md).
* By accessing the directory `/opt/enterprise-analytics/var/lib/couchbase/logs/rebalance` on _any_ of the cluster nodes. A rebalance report is maintained here for (up to) the last _five_ rebalances performed. Each report is provided as a `*.json` file, whose name indicates the time at which the report was run — for example, `rebalance_report_2020-03-17T11:10:17Z.json`.  
For more information about logging, see [Manage Logging](../manage/manage-logging/manage-logging.md).

## [](#reading-a-rebalance-report)Reading a Rebalance Report

Each rebalance report consists of a JSON document whose principal object is `stage_info`. This itself contains an object corresponding to each rebalance _stage_: one stage has occurred for each of the services deployed on the cluster. Therefore, if all six services have been deployed, six stages occur in a successful rebalance; and objects for `analytics`, `eventing`, `search`, `index` `query`, and `data` are provided.

Among the details provided for each service are the times at which rebalance-processes started and ended, the durations of rebalance-processes, and the numbers of documents already handled and still to be handled. When rebalance concludes successfully, a report is duly generated, with all fields corresponding to the successful completion of the rebalance-processes they represent. In cases where rebalance is interrupted (for example, by the user’s left-clicking the **Stop Rebalance** button, in Couchbase Web Console, or due to auto-failover), a generated report will describe a partially unsuccessful rebalance; indicating, in certain fields, an incomplete or unstarted rebalance-process, by means of the value `false`.

## [](#standard-fields)Standard Fields

Standard fields are provided for each stage. These are as follows:

* `startTime`. The point in time at which the stage was started (or possibly, has been determined _not_ to have started). Specified as a UTC date/time string.
* `completedTime`. The point in time at which the stage was completed (or possibly, has been determined _not_ to have completed). Specified as a UTC date/time string.
* `timeTaken`. The amount of elapsed time since `startTime`. Specified as an integer, in milliseconds. The value is `undefined`, if the stage has been determined _not_ to have started.
* `totalProgress`. The current, total progress that has been achieved for the stage. Specified as a percentage. In a completed report, the value is expected to be `100`. This is an _optional_ field, which may not appear if not implemented for the stage.
* `perNodeProgress`. The current progress that has been achieved for the stage for each node. The value is an object, which itself provides a progress figure for each node. Each progress figure is specified as a floating-point number between `0.0` and `1.0`. In a completed report, the value is expected to be `1`. This is an _optional_ field, which may not appear if not implemented for the stage.
* `subStage`. Details on any _substages_ that the stage may contain. For each _substage_, the standard fields are identical to those for each _stage_. This is an _optional_ field, which does not appear, if the stage contains no substages. (An example is _delta\_recovery_, which is a substage reflected in the `data` output, when _Delta Recovery Warmup_ has been performed on one or more nodes running the Data Service, during rebalance of that service.)
* `events`. An array of strings, each of which provides information about a significant event. The information may be a warning, an error message, or otherwise informational. This is an _optional_ field, which does not appear if not implemented for the stage, or if no significant events have occurred.
* `details`. Further details of the stage. This is an _optional_ field, which is currently implemented for the `data` stage only (information provided below).
* `rebalanceID`. A 32-bit string that is the identifier for the rebalance: for example, `"4f64c7dd5a1a452d3bcc3668307d64a6"`.
* `nodesInfo`. information about the nodes of the cluster, in relation to the rebalance. The following objects are provided — each consists of an array of strings, each of which represents a node. Where the category has no nodes, the array is empty.

  * `active_nodes`. The nodes included in the rebalance.
  * `keep_nodes`. The nodes that were intended to be part of the cluster, following rebalance.
  * `eject_nodes`. The nodes that were to be ejected by rebalance.
  * `delta_nodes`. The nodes on which Delta Recovery was to be performed.
  * `failed_nodes`. The nodes that were failed over prior to rebalance, and will be ejected from the cluster on successful rebalance.
* `master_node`. The master node for the cluster, on which the _Master Services_ run — these are sometimes referred to as the _Orchestrator_. If this node is rebalanced out of the cluster, a new Orchestrator is elected by the Cluster Manager, on a surviving node. For further information, see [ns-server](#learn:clusters-and-availability/cluster-manager.adoc#ns-server).
* `completionMessage`. A message that signifies the way in which rebalance ended. For example, `"Rebalance completed successfully"`, or `"Rebalance stopped by user"`.

If the report is downloaded by means of Couchbase Web Console, additional information in provided, concerning the download.

### [](#standard-fields-example)Standard Fields Example

The following example displays the initial section of a rebalance report, following a rebalance performed on a cluster consisting of the following nodes:

* `10.143.194.101`, running the Data, Query, and Index Services.
* `10.143.194.102`, running the Data and Search Services.
* `10.143.194.103`, running the Analytics and Eventing Services.
* `10.143.194.104`, running the Data Service.

The rebalance follows an edit made to both buckets resident on the cluster, `beer-sample` and `travel-sample`, changing the number of replicas from 1 to 2, for each. This excerpt starts at the top of the structure, and stops at the point at which the Data Service `details` begin (these are described further below).

{
  "stageInfo": {
    "analytics": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.103": 1
      },
      "startTime": "2020-03-18T00:34:13.415-07:00",
      "completedTime": "2020-03-18T00:34:14.724-07:00",
      "timeTaken": 1310
    },
    "eventing": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.103": 1
      },
      "startTime": "2020-03-18T00:34:14.724-07:00",
      "completedTime": "2020-03-18T00:34:14.939-07:00",
      "timeTaken": 214
    },
    "search": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.102": 1,
        "ns_1@10.143.194.104": 1
      },
      "startTime": "2020-03-18T00:34:12.453-07:00",
      "completedTime": "2020-03-18T00:34:12.758-07:00",
      "timeTaken": 306
    },
    "index": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.101": 1
      },
      "startTime": "2020-03-18T00:34:12.758-07:00",
      "completedTime": "2020-03-18T00:34:13.415-07:00",
      "timeTaken": 656
    },
    "data": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.101": 1,
        "ns_1@10.143.194.102": 1,
        "ns_1@10.143.194.104": 1
      },
      "startTime": "2020-03-18T00:33:36.969-07:00",
      "completedTime": "2020-03-18T00:34:12.452-07:00",
      "timeTaken": 35483,
      "details": {
        .
        .
        .

Each service thus has its stage-information provided in an object named after the service. Progress is provided for the whole cluster, and per node. Start times and completion times are provided, as are elapsed times. The Data Service contains the additional object, `details`, which is described immediately below.

## [](#see-also)See Also

General information about rebalance and Data-Service phases is provided in [Rebalance](../../../server/current/learn/clusters-and-availability/rebalance.md). information about performing a rebalance and downloading a report by means of Couchbase Web Console is provided in [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). Details on obtaining rebalance status and accessing the latest rebalance report by means of the REST API are provided in [Getting Cluster Tasks](rest-get-cluster-tasks.md).