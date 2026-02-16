[View original HTML](/cmos/current/cluster-monitor.html)

Couchbase cluster monitor is a core component of CMOS that provides cluster-level information via a Prometheus endpoint. If Couchbase cluster monitor is enabled, it will output the status of its checkers to Prometheus like the following:

# HELP multimanager_cluster_checker_status Checker results for cluster level checkers
# TYPE multimanager_cluster_checker_status gauge
multimanager_cluster_checker_status{cluster_name="CMOS 7 Test",cluster_uuid="7ce7c09b3514e83792724b8a530b66e0",id="CB90002",name="singleOrTwoNodeCluster"} 0
# HELP multimanager_node_checker_status Checker results for node level checkers
# TYPE multimanager_node_checker_status gauge
multimanager_node_checker_status{cluster_name="CMOS 7 Test",cluster_uuid="7ce7c09b3514e83792724b8a530b66e0",id="CB90001",name="oneServicePerNode",node_name="10.145.212.101:18091",node_uuid="730c37dace488f37f47c397f376c1c05"} 1
# HELP multimanager_bucket_checker_status Checker results for bucket level checkers
# TYPE multimanager_bucket_checker_status gauge
multimanager_bucket_checker_status{bucket="pillowfight",cluster_name="CMOS 7 Test",cluster_uuid="7ce7c09b3514e83792724b8a530b66e0",id="CB90009",name="missingActiveVBuckets"} 2

The values of each metric represents the current status of the checker. The integer values have the following meanings:

* 0: Good (everything is fine, no action required)
* 1: Warn (potential issue, worth investigating)
* 2: Alert (serious issue, action required)
* 3: Info (informational only, no action required)
* 4: Missing (checker failed to run or information was not available)

## [](#next-steps)Next steps

* [Architecture overview](architecture.md)
* [Microlith container deployment](deployment-microlith.md)
* [On-premise deployment](deployment-onpremise.md)
* [On-premise example](tutorial-onpremise.md)