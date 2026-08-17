---
title: Forwarding Couchbase Logs with Fluent Bit
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/tutorial-couchbase-log-forwarding.adoc
  xref: xref:2.6@operator::tutorial-couchbase-log-forwarding.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/tutorial-couchbase-log-forwarding.html)

# Forwarding Couchbase Logs with Fluent Bit

> Learn how to configure the Autonomous Operator to forward Couchbase logs using Fluent Bit. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#introduction)Introduction

Having a containerized application's logs available on standard console output is desirable in Kubernetes environments, since it allows for [simple debugging](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-running-pod/#examine-pod-logs), as well as standards-based integration with centralized log management systems running in a Kubernetes cluster. Unfortunately, the Couchbase Server container doesn't natively write its logs to standard console output. Instead, the [default behavior](concept-couchbase-logging.md#default-logging) of the Couchbase Server container (in deployments managed by the Autonomous Operator) is to write its [various log files](../../server/current/manage/manage-logging/manage-logging.md#log-file-listing) to the `default` or `logs` persistent volumes.

However, as of version 2.2, the Autonomous Operator can optionally deploy and manage a third party log processor on each Couchbase pod which enables Couchbase Server logs to be [forwarded](concept-couchbase-logging.md#log-forwarding) to the log processor's standard console output as well as other destinations. This guide will walk you through an example of how to configure log forwarding for a Couchbase deployment using the Couchbase-supplied log processor image based on [Fluent Bit](https://fluentbit.io/).

Examples are provided for forwarding logs to Loki and Elasticsearch, as well as how to target Azure blob storage and Amazon S3 storage for Couchbase Server [audit logs](howto-manage-couchbase-logging.md#configuring-audit-logging). An example for configuring log redaction is also shown to demonstrate how the log forwarding solution can redact logs in-flight.

## [](#before-you-begin)Before You Begin

This tutorial assumes that you have already [installed](install-kubernetes.md) the Autonomous Operator. The Autonomous Operator needs to be running in the same namespace where you deploy the Couchbase cluster in the [Configure the Couchbase Cluster](#configure-the-couchbase-cluster) section below.

## [](#configure-the-couchbase-cluster)Configure the Couchbase Cluster

Log forwarding is enabled via the [CouchbaseCluster](resource/couchbasecluster.md) resource specification. The following example contains a basic Couchbase cluster deployment configuration that already has log forwarding configured. Important non-default settings are called out and described.

> [!NOTE]
> It is not a requirement that log forwarding be configured when the cluster is first deployed. You can always [enable and configure](howto-couchbase-log-forwarding.md) log forwarding post-deployment.

Example: Couchbase Cluster Deployment Configuration with Log Forwarding Enabled

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cb-example-auth
type: Opaque
data:
  username: QWRtaW5pc3RyYXRvcg== # Administrator
  password: cGFzc3dvcmQ=         # password
---
apiVersion: couchbase.com/v2
kind: CouchbaseBucket
metadata:
  name: default
---
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  logging:
    server:
      enabled: true (1)
      manageConfiguration: true
      configurationName: "fluent-bit-config"
      sidecar:
        image: "couchbase/fluent-bit:1.2.3"
    audit:
      enabled: true (2)
      garbageCollection:
        sidecar:
          enabled: true (3)
  image: couchbase/server:7.1.3
  security:
    podSecurityContext:
      fsGroup: 1000
    adminSecret: cb-example-auth
  buckets:
    managed: true
  servers:
  - size: 3
    name: all_services
    services:
    - data
    - index
    - query
    - search
    - eventing
    - analytics
    volumeMounts:
      default: couchbase
  volumeClaimTemplates: (4)
  - metadata:
      name: couchbase
    spec:
      resources:
        requests:
          storage: 1Gi
```

| **1** | [couchbaseclusters.spec.logging.server.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-enabled): Setting this field to true enables the logging sidecar container. This field normally defaults to false. This is technically the only field that needs to be modified in order to enable log forwarding. The Autonomous Operator will default to pulling the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) from the Docker public registry.                                                                                                                                                                                 |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.logging.audit.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-logging-audit-enabled): Setting this field to true enables [audit logging](howto-manage-couchbase-logging.md#configuring-audit-logging) on the Couchbase cluster. This field normally defaults to false. Unlike other Couchbase logging, audit logging is not turned on by default. Since some of the examples in this tutorial utilize audit logs, we want to make sure it is turned on.                                                                                                                                                                                                       |
| **3** | [couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-enabled): Setting this field to true enables garbage collection of rotated audit logs, and instructs the Autonomous Operator to deploy a sidecar helper container in each Couchbase pod for cleaning up rotated logs. This field normally defaults to false. Couchbase Server rotates audit logs, but cannot, itself, expire or delete them. Therefore, for the purposes of this tutorial, we want to enable garbage collection to clean up rotated audit logs so that they don't accidentally consume all available storage. |
| **4** | [couchbaseclusters.spec.volumeClaimTemplates](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates): This setting is not specifically for log forwarding, it is purely that log forwarding requires a persistent volume to access the logs so this shows an example of how to set one up. Refer to the storage documentation for your platform as well as the [Couchbase documentation](concept-persistent-volumes.md) for full details. You may want to tweak the resources allocated for example or the storage class.                                                                                                                                                       |

Copy the example cluster deployment configuration from above and save it to a file. (In this case we've named the file `couchbase-cluster-log-forwarding.yaml`.) Run the following command to deploy it into Kubernetes:

```console
$ kubectl apply -f couchbase-cluster-log-forwarding.yaml
```

Note that the Autonomous Operator must already be deployed and running in the current namespace in order for the above command to succeed (refer to the [prerequisites](#before-you-begin)).

Next, verify that the cluster has been deployed successfully.

```console
$ kubectl get pods
```

NAME                                  READY     STATUS    RESTARTS   AGE
cb-example-0000                       1/1       Running   0          1m
cb-example-0001                       1/1       Running   0          1m
cb-example-0002                       1/1       Running   0          1m
couchbase-operator-1917615544-pd4q6   1/1       Running   0          8m

You should observe the three Couchbase pods that were created according to the cluster configuration, and they should each have a status of `RUNNING`.

With the Couchbase cluster successfully deployed, you should now be able to observe Couchbase log events on the standard output of the `logging` container of each pod.

```console
$ kubectl logs cb-example-0000 logging
```

Example log event on standard console output:

[1615311121.859344000, {"filename":"/fluent-bit/test/logs/memcached.log.000000.txt","timestamp":"2021-03-09T17:32:01.859344+00:00","level":"INFO","message":"Couchbase version 7.2.3-7909 starting."}]

You'll notice that processed log events are structured messages with keys and values:

* `"timestamp":"2021-03-09T17:32:01.859344+00:00"`
* `"level":"INFO"`
* `"message":"Couchbase version 7.2.3-7909 starting."`

The default configuration used has support for Elasticsearch, Loki, Splunk and standard console output as destinations for logs. However, everything aside from standard console output will not match any streams by default. See [Configure Log Forwarding](howto-couchbase-log-forwarding.md) for how to enable them.

Now that we've successfully implemented the default configuration for processing and forwarding Couchbase logs to standard console output, we can move on to the [next section](#customize-the-log-forwarding-configuration) where we'll explore how to customize the configuration to do things like apply different types of parsing and redaction to specific logs, as well as forward those logs to multiple different locations.

## [](#customize-the-log-forwarding-configuration)Customize the Log Forwarding Configuration

The _log forwarding configuration_ determines how the `logging` sidecar container processes and forwards Couchbase logs. Since this configuration can contain sensitive information, it is stored in a Kubernetes Secret.

When we created the Couchbase cluster in the [previous section](#configure-the-couchbase-cluster), the Autonomous Operator automatically created a _default_ log forwarding configuration Secret with the name `fluent-bit-config`. We'll be modifying this Secret in order to implement our own custom configuration.

### [](#allow-custom-configurations)Allow Custom Configurations

Before we can modify the `fluent-bit-config` secret, we'll first need to modify the [CouchbaseCluster](resource/couchbasecluster.md) resource to allow custom log forwarding configurations.

```console
$ kubectl patch cbc cb-example -p '{"spec":{"logging": {"server": {"manageConfiguration": false}}}}'
```

Patching your [CouchbaseCluster](resource/couchbasecluster.md) resource so that [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) is set to `false`.

Now that we've successfully allowed our Couchbase cluster to use custom log forwarding configurations, let's get to customizing!

### [](#create-a-custom-configuration)Create a Custom Configuration

Since the Couchbase-supplied default [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) is based on Fluent Bit, you can technically customize the log forwarding configuration with any kind of configuration that is [supported by Fluent Bit](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit). In addition, the default image also contains built-in parsers, redaction scripts, and other configuration files — all of which can be selectively utilized in your custom configuration.

The following is an example of a custom log forwarding configuration Secret that limits the number of Couchbase logs that are processed and forwarded to just the Couchbase [audit log](howto-manage-couchbase-logging.md#configuring-audit-logging):

Example: Custom Log Forwarding Configuration Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |(1)
    [SERVICE]
        flush        1
        daemon       Off
        log_level    Warning
        parsers_file /fluent-bit/etc/parsers-couchbase.conf(2)
    # Include audit log only
    @include /fluent-bit/etc/couchbase/in-audit-log.conf(3)
    # Send to the standard output
    [OUTPUT]
        name  stdout
        match couchbase.log.*(4)
```

| **1** | stringData.fluent-bit.conf: Log forwarding configuration files are defined in the stringData field of the Secret. The fluent-bit.conf file is specified with a field that starts with a space and a vertical bar (\|), followed by the contents of the [_main configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file). Note that Fluent Bit is very particular about its [format and schema](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/format-schema) — files must all follow the same indentation.                                                                                                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | /fluent-bit/etc/parsers-couchbase.conf: This is the path to the built-in file that contains all of the default [_parser configurations_](https://docs.fluentbit.io/manual/pipeline/filters/parser) in the Couchbase-supplied log processor image (you can view this file on [GitHub](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/parsers-couchbase.conf)).                                                                                                                                                                                                                                                                                                                                                                        |
| **3** | @include /fluent-bit/etc/couchbase/in-audit-log.conf: This is the path to the built-in file that contains the [_input configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Finput) that processes just the Couchbase audit log (you can view this file on [GitHub](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-audit-log.conf)). Since we want to limit the Couchbase logs being processed to just the audit log, we want to make sure that we only [_include_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Finclude%5Ffile-1) the input configuration file for the audit log.                    |
| **4** | couchbase.log.\*: By default, all parsed Couchbase log events are [_tagged_](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) with couchbase.log._<name-of-log_\>. The default [_output configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Foutput) then uses the wildcard [_match_](https://docs.fluentbit.io/manual/concepts/key-concepts#match) couchbase.log.\* to forward all tagged Couchbase logs to the output. However, because we defined a single input configuration that only processes the audit log, we are free to leave the default wildcard match. This is because the only log events that will be available for output will be those from the audit log. |

> [!NOTE]
> This log forwarding configuration assumes that you've already enabled Couchbase audit logging in the [CouchbaseCluster](resource/couchbasecluster.md) resource. If you deployed the [example cluster configuration](#cluster-config-log-forwarding) from earlier in this tutorial, then audit logging is already enabled and no action is necessary.

Copy the above secret configuration and save it to a file. Make sure to check for any formatting issues when copying from HTML to text format for YAML. (In this case we've named the file `fluent-bit-config.yaml`.) Run the following command to deploy it into Kubernetes:

```console
$ kubectl apply -f fluent-bit-config.yaml
```

Once the Secret is updated in Kubernetes, the configuration changes will be populated into the volume that is mounted in the `logging` sidecar container on each Couchbase pod. The `logging` container's watcher process will detect the new configuration, and restart Fluent internally to consume the new configuration. Once Fluent Bit restarts, only audit log events will be processed and forwarded to standard console output.

> [!IMPORTANT]
> The ability to restart Fluent Bit internally is a special characteristic of the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit). If you're using a custom sidecar container image, be aware that Fluent Bit, on its own, does not currently support [dynamic reload](https://github.com/fluent/fluent-bit/issues/365) of its configuration.
> 
> Also note that the Couchbase-supplied log forwarding implementation does not currently support log buffering during restart. Therefore, log events that occur while Fluent Bit is restarting may be lost.

If you want to check the configuration then a simple base64 decode command can be run using the Kubernetes `Secret` name:

```console
$ kubectl get secret "fluent-bit-config" -o go-template='{{range $k,$v := .data}}{{printf "%s: " $k}}{{if not $v}}{{$v}}{{else}}{{$v | base64decode}}{{end}}{{"\n"}}{{end}}'
```

### [](#next-steps)Next Steps

Now that you've successfully implemented some basic log forwarding customizations, we recommend that you try out some of the other examples in this tutorial. These examples should help you get an even better idea of the capabilities of both Fluent Bit and the Autonomous Operator when it comes to processing and forwarding Couchbase logs.

## [](#example-loki-stack)Example: Loki Stack

> [!NOTE]
> This example assumes you've deployed the CouchbaseCluster resource described at the [beginning of the tutorial](#cluster-config-log-forwarding). It also assumes that you are familiar with how to [customize a log forwarding configuration](#customize-the-log-forwarding-configuration).

A simple approach to deploy a full logging and monitoring solution is to use a [Loki Stack](https://grafana.com/docs/loki/latest/overview/). A stack that includes a Fluent Bit `daemonset` (node logs), Loki, Grafana, and Prometheus, provides a nice and simple integrated solution for monitoring and logging. You can deploy this stack using a Helm chart.

Once you have Helm installed, add the chart repository:

```console
helm repo add grafana https://grafana.github.io/helm-charts
```

The following command installs the chart in the default namespace:

```console
helm upgrade --install loki grafana/loki-stack \
--set fluent-bit.enabled=false,grafana.enabled=true,prometheus.enabled=true,prometheus.alertmanager.persistentVolume.enabled=false,prometheus.server.persistentVolume.enabled=false
```

The above command was borrowed and modified from the [official Loki documentation](https://grafana.com/docs/loki/latest/installation/helm/#deploy-loki-stack-loki-promtail-grafana-prometheus-with-persistent-volume-claim), where you can find further details on how to then use Grafana and configure the stack how you might want in your cluster.

Once the chart is deployed, you can update the Couchbase Cluster to forward logs to Loki by adding the correct annotation as per below.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  servers:
  - size: 3
    name: all_services
    pod:
      metadata:
        annotations:
          fluentbit.couchbase.com/loki_match: "*"
```

You can retrieve the Grafana admin secret and do any port forwarding or similar required:

```console
kubectl get secret loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
kubectl port-forward service/loki-grafana 3000:80
```

> [!NOTE]
> In order to have alerting on logs through the UI, you'll need to use Grafana 7.5 or higher.

## [](#example-elasticsearch)Example: Elasticsearch

> [!NOTE]
> This example assumes you've deployed the CouchbaseCluster resource described at the [beginning of the tutorial](#cluster-config-log-forwarding). It also assumes that you are familiar with how to [customize a log forwarding configuration](#customize-the-log-forwarding-configuration).

An Elasticsearch deployment or StatefulSet can provide a good integrated solution for monitoring and logging. A basic deployment configuration with a single replica is shown below.

```yaml
kind: Service
apiVersion: v1
metadata:
  name: elasticsearch
  labels:
    app: elasticsearch
spec:
  selector:
    app: elasticsearch
  clusterIP: None
  ports:
    - port: 9200
      name: rest
    - port: 9300
      name: inter-node
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: es-cluster
spec:
  serviceName: elasticsearch
  replicas: 1
  selector:
    matchLabels:
      app: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      containers:
      - name: elasticsearch
        image: docker.elastic.co/elasticsearch/elasticsearch:7.2.0
        resources:
            limits:
              cpu: 1000m
            requests:
              cpu: 100m
        ports:
        - containerPort: 9200
          name: rest
          protocol: TCP
        - containerPort: 9300
          name: inter-node
          protocol: TCP
        env:
          - name: cluster.name
            value: k8s-logs
          - name: node.name
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
          - name: discovery.seed_hosts
            value: "es-cluster-0.elasticsearch"
          - name: cluster.initial_master_nodes
            value: "es-cluster-0"
          - name: ES_JAVA_OPTS
            value: "-Xms512m -Xmx512m"
---
apiVersion: v1
kind: Service
metadata:
  name: kibana
  labels:
    app: kibana
spec:
  ports:
  - port: 5601
  selector:
    app: kibana
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kibana
  labels:
    app: kibana
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kibana
  template:
    metadata:
      labels:
        app: kibana
    spec:
      containers:
      - name: kibana
        image: docker.elastic.co/kibana/kibana:7.2.0
        resources:
          limits:
            cpu: 1000m
          requests:
            cpu: 100m
        env:
          - name: ELASTICSEARCH_URL
            value: http://elasticsearch:9200
        ports:
        - containerPort: 5601
```

This needs to be deployed in the same namespace as the Couchbase cluster, otherwise the service URL will need to be explicit (include the namespace) in the log configuration.

Once the Elasticsearch deployment is in place, we can update the stream match for the Elasticsearch output.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
...
  servers:
  - size: 3
    name: all_services
...
    pod:
      metadata:
        annotations:
          fluentbit.couchbase.com/es_match: "*"
```

## [](#example-azure-blob-storage)Example: Azure Blob Storage

> [!NOTE]
> This example assumes you've deployed the CouchbaseCluster resource described at the [beginning of the tutorial](#cluster-config-log-forwarding). It also assumes that you are familiar with how to [customize a log forwarding configuration](#customize-the-log-forwarding-configuration).

This example shows you how to forward audit logs to an Azure endpoint. The main area to manage is the output configuration, so in the following example we've simply included the default configuration file and then appended an output to Azure Blob Storage:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |
    # Just include the normal file and append to it the Azure Blob output
    @include /fluent-bit/etc/fluent-bit.conf

    # Output only audit log by default
    [OUTPUT](1)
        name                  azure_blob
        match                 couchbase.log.audit
        account_name          YOUR_ACCOUNT_NAME
        shared_key            YOUR_SHARED_KEY
        path                  kubernetes
        container_name        logs
        auto_create_container on
        tls                   on
```

| **1** | Make sure to specify your details for account\_name and shared\_key, along with things like the container\_name and path. All the various options are described in the official Fluent Bit documentation for the [Azure Blob output plugin](https://docs.fluentbit.io/manual/pipeline/outputs/azure%5Fblob). |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

To simplify testing, the [Azurite](https://github.com/Azure/Azurite) emulator can be used.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: azurite
  labels:
    app: azurite
spec:
  ports:
  - port: 10000
  selector:
    app: azurite
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: azurite-deployment
  labels:
    app: azurite
spec:
  replicas: 1
  selector:
    matchLabels:
      app: azurite
  template:
    metadata:
      labels:
        app: azurite
    spec:
      containers:
      - name: azurite
        image: mcr.microsoft.com/azure-storage/azurite
        ports:
        - containerPort: 10000
```

The log forwarding configuration then becomes:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |
    # Just include the normal file and append to it the Azure Blob output
    @include /fluent-bit/etc/fluent-bit.conf
    # Output only audit log by default
    [OUTPUT]
        name                  azure_blob
        match                 couchbase.log.audit
        account_name          devstoreaccount1
        shared_key            Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==
        path                  kubernetes
        container_name        logs
        auto_create_container on
        tls                   off
        emulator_mode         on
        endpoint              azurite:10000
```

## [](#example-amazon-s3)Example: Amazon S3

> [!NOTE]
> This example assumes you've deployed the CouchbaseCluster resource described at the [beginning of the tutorial](#cluster-config-log-forwarding). It also assumes that you are familiar with how to [customize a log forwarding configuration](#customize-the-log-forwarding-configuration).

This example shows you how to forward audit logs to an Amazon S3 endpoint. The main area to manage is the output configuration, so in the following example we've simply included the default configuration file and then appended an output to the S3 cloud object store:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |
    # Just include the normal file and append to it the S3 output
    @include /fluent-bit/etc/fluent-bit.conf
    # Output only audit log by default
    [OUTPUT] (1)
        Name                         s3
        Match                        couchbase.log.audit
        bucket                       my-bucket
        region                       us-west-2
        total_file_size              250M
        s3_key_format                /$TAG[2]/$TAG[0]/%Y/%m/%d/%H/%M/%S/$UUID.gz
        s3_key_format_tag_delimiters .-
```

| **1** | Note that the role\_arn key is an important setting to specify if not using something like instance roles. All the various options are described in the official Fluent Bit documentation for the [Amazon S3 output plugin](https://docs.fluentbit.io/manual/pipeline/outputs/s3). |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#log-redaction-in-flight)Log Redaction In-flight

> [!NOTE]
> This example assumes you've deployed the CouchbaseCluster resource described at the [beginning of the tutorial](#cluster-config-log-forwarding). It also assumes that you are familiar with how to [customize a log forwarding configuration](#customize-the-log-forwarding-configuration).

Fluent Bit provides some very powerful facilities to mutate the log lines before they even leave the container. These facilities can be effectively utilized to redact sensitive information from log events.

When Couchbase Server writes an event to a log file, it encases certain [sensitive information](../../server/current/manage/manage-logging/manage-logging.md#understanding%5Fredaction) in special tags. Therefore, the goal of redaction is to remove or replace the contents of the `<ud>…​</ud>` tags in the string.

There are two main approaches we can take:

1. Just remove the entire line
2. Replace or remove redacted content within the line

The _first approach_ can be provided by a simple [grep filter](https://docs.fluentbit.io/manual/pipeline/filters/grep) within Fluent Bit. The following configuration will filter out any entries for the `message` key that match a regex:

```console
[FILTER]
    Name grep
    Match *
    Exclude message \<ud\>
```

However, the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) provides optional support for the _second approach,_ whereby the contents of the `<ud>…​</ud>` tags are hashed before the log events are forwarded to standard console output or other locations. This selective log redaction is currently facilitated by a [LUA filter](https://docs.fluentbit.io/manual/pipeline/filters/lua) that leverages a Couchbase-supplied [LUA script](https://github.com/couchbase/couchbase-fluent-bit/blob/main/redaction/redaction.lua) and a third-party [SHA-1 hashing library](https://github.com/mpeterv/sha1), both of which are included in the default log processor image.

Log redaction isn't enabled by default, so we'll need to enable it by customizing the log forwarding configuration. The following example generates a sample message to redact using the Fluent Bit dummy plugin:

```none
# Simple test generator for redaction
[INPUT]
    Name dummy
    Tag couchbase.redact.test
    Dummy {"message": "Cats are <ud>sma#@&*+-.!!!!!rter</ud> than dogs, and <ud>sheeps</ud>"}

# Redaction of fields
[FILTER]
    Name    lua
    # Typically this would be a couchbase.log.X tag instead you match on, this is just for the test here
    Match   couchbase.redact.*
    script  redaction.lua
    call    cb_sub_message

# Now rewrite the tags for redacted information - not required if redacting normal logs
[FILTER]
    Name rewrite_tag
    Match couchbase.redact.*
    Rule message .* couchbase.log.$TAG[2] false

[OUTPUT]
    name  stdout
    match couchbase.log.*
```

When run, this will output something like the following showing the redacted strings as hashes:

[0] couchbase.logs.test: [1616146713.035099437, {"message"=>"Cats are <ud>00b335216f27c1e7d35149b5bbfe19d4eb2d6af1</ud> than dogs, and <ud>888f807d45ff6ce47240c7ed4e884a6f9dc7b4fb</ud>"}]
[0] couchbase.logs.test: [1616146714.035226932, {"message"=>"Cats are <ud>00b335216f27c1e7d35149b5bbfe19d4eb2d6af1</ud> than dogs, and <ud>888f807d45ff6ce47240c7ed4e884a6f9dc7b4fb</ud>"}]
[0] couchbase.logs.test: [1616146715.035028818, {"message"=>"Cats are <ud>00b335216f27c1e7d35149b5bbfe19d4eb2d6af1</ud> than dogs, and <ud>888f807d45ff6ce47240c7ed4e884a6f9dc7b4fb</ud>"}]

> [!NOTE]
> For redaction we recommend only matching those streams you want to redact to reduce the load. LUA scripting has an overhead and it is recommended to use an extra Fluent Bit worker thread at least if you enable it.
> 
> A salt for redaction can be provided in the logging configuration secret by specifying it in the `redaction.salt` file/key. The salt is defaulted to the cluster name by the operator and is provided in the default configuration even though it is not used by default.