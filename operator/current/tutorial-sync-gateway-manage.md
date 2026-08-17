---
title: Managing a Sync Gateway Cluster
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/tutorial-sync-gateway-manage.adoc
  xref: xref:operator::tutorial-sync-gateway-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/tutorial-sync-gateway-manage.html)

# Managing a Sync Gateway Cluster

> Collecting logs from your Sync Gateway cluster 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#troubleshooting-and-log-collection)Troubleshooting and Log Collection

This tutorial provides guidance on how to diagnose and troubleshoot problems with the Sync Gateway deployment on Kubernetes.

When troubleshooting, it is important to rule out Kubernetes itself as the root cause of the problem you are experiencing. See the [Kubernetes Troubleshooting guide](https://kubernetes.io/docs/tasks/debug-application-cluster/troubleshooting/) for information about debugging applications within a Kubernetes cluster. For troubleshooting a Couchbase Server deployment using the Couchbase operator, please refer to our [guide](howto-manage-operator-logging.md).

### [](#prerequisites)Prerequisites

* The location of the Sync Gateway logs within a pod is specified with the "logging" key in the Sync Gateway configuration file (see [logging guide](../../sync-gateway/current/manage/logging.md#log-rotation-configuration))
* To view or fetch the logs from a Sync Gateway pod, you must first identify the Sync Gateway pods in your deployment using the following command.  
```console  
$ kubectl get pods  
```  
Your response will include a list of sync gateway pods in your deployment

### [](#viewing-logs-in-console)Viewing Logs in Console

You can use `kubectl` to view logs for a specific pod using following command. This command will output logs to the console.

```console
$ kubectl logs -f <pod_id>
```

## [](#using-sgcollect%5Finfo)Using `sgcollect_info`

[sgcollect\_info](#sync-gateway::sgcollect%5Finfo.adoc) is a command line utility with detailed statistics for a specific Sync Gateway node. This tool must be run on each node individually. The `sgcollect_info` tool is bundled as part of the Sync Gateway container image. You have two options on how to retrieve the logs from the Sync Gateway pods.

### [](#option-1)Option 1

You can trigger the execution of the `sgcollect_info` tool on each individual pod using the [\_sgcollect\_info](#sync-gateway::admin-rest-api.adoc) REST endpoint.

In order to do this, you would need access to the admin port. As recommended, the admin port is expected to only be accessible from within the Sync Gateway pod.

#### [](#identify-list-of-sync-gateway-pods)Identify list of Sync Gateway Pods

Run the following command to get list of sync gateway pods. Repeat the steps in the [\[Triggering sgcollect\_info\]](#Triggering sgcollect%5Finfo) section for every pod listed in the output.

```console
$ kubectl get pods -o=name | grep sync-gateway
```

#### [](#set-up-port-forwarding)Set up Port Forwarding

Run following command to set up port forwarding from your local machine to admin port on the Sync Gateway pod. This command assumes the default admin port of 4985\. If you have configured your sync gateway to use an alternative admin port, replace that in the command below

```console
$ kubectl port-forward <pod_id> 4985:4985
```

#### [](#triggering-sgcollect%5Finfo)Triggering `sgcollect_info`

Trigger the execution of the `sgcollect_info` tool on the Sync Gateway pod using the [POST \_sgcollect\_info](#sync-gateway::admin-rest-api.adoc) REST endpoint. This is an example of the command.

> [!NOTE]
> The example below outputs the logs to local directory. Instead, Enterprise customers can use this endpoint to automatically upload it to Couchbase support servers.

```console
$ curl -X POST \
  http://localhost:4985/_sgcollect_info \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "output_dir": "/home/sync_gateway/logs",
  "upload": false
}’
```

#### [](#monitor-the-status-of-the-log-collection)Monitor the status of the log collection

Use the [GET \_sgcollect\_info](#sync-gateway::admin-rest-api.adoc) REST endpoint to monitor the status of the log collection. This is an example of the command. Wait until the status reported back is not `running`

```console
$ curl -X GET \
  http://localhost:4985/_sgcollect_info \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
```

#### [](#copy-log-files)Copy Log Files

This is an optional step and is only required if you had opted to not directly upload documents to the Couchbase support servers. This would be the case if you are intending to troubleshoot yourself. Once `sgcollect_info` has completed, you can copy the output .zip file from each of the pods to your local machine for further analysis.

```console
$ kubectl cp <pod-id>:/home/sync_gateway/logs/* .
```

### [](#option-2)Option 2

This option is less secure than the option discussed in the previous section as it uses `kubectl exec` to trigger the execution of [sgcollect\_info](#sync-gateway::sgcollect%5Finfo.adoc) for a specific Sync Gateway node. This tool must be run on each Sync Gateway node individually. The `sgcollect_info` tool is bundled as part of the Sync Gateway container image.

#### [](#collecting-logs-on-a-pod)Collecting logs on a pod

To collect logs on a specific pod, run `sgcollect_info` using the `kubectl` [exec command](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec). The following command runs `sgcollect_info` on the specified pod and outputs the results to an **out.zip** file.

```console
$ kubectl exec <pod_id> -- /opt/couchbase-sync-gateway/tools/sgcollect_info /tmp/out.zip
```

#### [](#coping-log-output-from-pod)Coping log output from pod

To copy the `sgcollect_info` generated output from the pod, use the `kubectl` [cp command](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#cp).

```console
$ kubectl cp <pod_id>:/tmp/out.zip .
```

#### [](#convenience-scripts)Convenience Scripts

##### [](#collecting-sgcollect%5Finfo-logs-from-all-pods)Collecting `sgcollect_info` logs from all pods

The following script runs `sgcollect_info` on all the pods and to copy the zipped files over to the current folder.

```sh
#! /bin/sh
OUTFOLDER=${1:-/tmp}
for pod in `kubectl get pods -o=name | grep sync-gateway | sed "s/^.\{4\}//"`
do
    LOGFILE=$OUTFOLDER/$pod'_sgcollect_info_out.zip'
    echo "Running sgcollect_info to generate $LOGFILE"
    kubectl exec $pod -- /opt/couchbase-sync-gateway/tools/sgcollect_info $LOGFILE
    echo "copying $pod:$LOGFILE to current folder"
    kubectl cp $pod:$LOGFILE .
done
```

## [](#rolling-upgrades-of-sync-gateway-nodes)Rolling Upgrades of Sync Gateway Nodes

A deployment controller facilitates a rolling upgrade of the Sync Gateway nodes in the cluster and the load balancer will automatically take care of redirecting the traffic to the remaining nodes.

A deployment that is configured to have a single Sync Gateway import node will experience some latency in processing write requests until the import node comes back up again.

* For example, to upgrade the version of the Sync Gateway, update the corresponding deployment configuration file and re-apply that to the cluster:  
```console  
$ kubectl apply -f sgw-deployment-upgrade.yaml  
```
* Verify the status of the rollout as follows:  
```console  
$ kubectl rollout status deployment sync-gateway  
```  
The deployment controller will ensure that at least one replica is available to serve the incoming requests while the other replicas are being upgraded. The load balancer will automatically redirect all requests to the remaining nodes.
* If the upgrade fails for any reason, rollback or undo the rollout with the following command:  
```console  
$ kubectl rollout undo  deployment sync-gateway  
```

## [](#upgrading-the-kubernetes-cluster)Upgrading the Kubernetes Cluster

Refer to the following [Couchbase Operator guide](concept-kubernetes-upgrade.md) for a discussion about upgrading the Kubernetes cluster for the Couchbase deployment.

## [](#further-reading)Further Reading

* [Sync-Gateway Documentation](../../sync-gateway/current/introduction.md)
* [Connecting Sync-Gateway to Couchbase Server](tutorial-sync-gateway.md)
* [Connecting Couchbase Lite Clients](tutorial-sync-gateway-clients.md)