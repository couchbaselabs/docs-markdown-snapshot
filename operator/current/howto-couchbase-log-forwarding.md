[View original HTML](/operator/current/howto-couchbase-log-forwarding.html)

> Configure Couchbase Server logs to be forwarded to standard console output. 

## [](#overview)Overview

Couchbase Server produces a [variety](../../server/current/manage/manage-logging/manage-logging.md#log-file-listing) of log files. By default, these logs cannot be collected from the Couchbase Server container’s standard console output. This limits the ability to integrate Couchbase logging with 3rd-party monitoring or collection technologies deployed within a Kubernetes cluster.

However, the Kubernetes Operator can optionally enable [_log forwarding_](concept-couchbase-logging.md#log-forwarding) by deploying a third party log processor in a sidecar container on each Couchbase pod, which then reads the log files and forwards them to standard console output. For this purpose, Couchbase supplies a default [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) based on [Fluent Bit](https://fluentbit.io/).

The sections on this page describe how to enable and configure log forwarding using the Couchbase-supplied log processor image.

|  | The Couchbase-supplied log processor container image is only supported on Kubernetes platforms in conjunction with the Couchbase Kubernetes Operator. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Log forwarding requires that logs be written to a persistent volume (i.e. the Couchbase deployment’s default or logs volumes are backed by [persistent storage](best-practices.md#storage)). Fully-ephemeral clusters are not supported by this feature. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Log forwarding requires that [couchbaseclusters.spec.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-securitycontext) is set as appropriate for your Kubernetes distribution, as the sidecar requires read access to the shared volume. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#enabling-log-forwarding)Enabling Log Forwarding

Log forwarding is fundamentally provided by two components:

1. the _log processor image_ that is used by the Kubernetes Operator to deploy the `logging` sidecar container onto each Couchbase Server pod, and
2. the _log forwarding configuration_, stored in a Kubernetes Secret, that gets consumed by the `logging` sidecar container and which controls its behavior.

Enabling log forwarding for a particular Couchbase cluster involves enabling these two components in the [CouchbaseCluster](resource/couchbasecluster.md) resource specification.

The required configuration parameters for enabling log forwarding are described in the example below. Specified values represent the defaults for their respective fields unless otherwise noted in a callout. (The Kubernetes Operator will set the default values for any fields that are not specified by the user.)

Basic [CouchbaseCluster](resource/couchbasecluster.md) Parameters That Enable Log Forwarding

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  servers:
  - size: 3
    name: all_services
    volumeMounts:
      default: couchbase
  volumeClaimTemplates:
      - metadata:
          name: couchbase
        spec:
          storageClassName: "standard"
          resources:
            requests:
              storage: 1Gi
  logging:
    server:
      enabled: true (1)
      sidecar:
        image: "couchbase/fluent-bit:1.2.3" (2)
    audit:
      enabled: false (3)
```

| **1** | [couchbaseclusters.spec.logging.server.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-enabled): This is technically the only field that must be changed in order to enable log forwarding. Setting this field to true (defaults to false) instructs the Kubernetes Operator to deploy the logging sidecar container on each pod.                                                                                                                                                                           |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.logging.server.sidecar.image](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-image): This field specifies the container image that the Kubernetes Operator will use for deploying the logging sidecar container. This field defaults to couchbase/fluent-bit:1.2.3, which pulls the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit). You may need to modify this field if your Kubernetes nodes can’t pull from the Docker public registry. |
| **3** | (Optional) [couchbaseclusters.spec.logging.audit.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-logging-audit-enabled): This field is used to enable Couchbase audit logging, and defaults to false. Unlike other Couchbase logs, audit logging is not turned on by default. If you intend to forward audit logs, you must [configure audit logging](howto-manage-couchbase-logging.md#configuring-audit-logging) first.                                                                                                  |

After deploying the [CouchbaseCluster](resource/couchbasecluster.md) resource specification, the logs will be available on the standard output of the `logging` container on each pod:

```console
$ kubectl logs cb-example-0000 logging
```

## [](#configuring-log-forwarding)Configuring Log Forwarding

As described in [Enabling Log Forwarding](#enabling-log-forwarding), there are two primary components that provide log forwarding: the _log processor image_ and the _log forwarding configuration_. The Kubernetes Operator uses Couchbase-provided defaults for both of these components, which can be used _as-is_ (refer to [Using Default Log Forwarding](#using-default-log-forwarding)). However, these components can be further customized to better meet the needs of your environment (refer to [Using Custom Log Forwarding](#using-custom-log-forwarding)).

### [](#enable-memory-buffer-limits)Enable memory buffer limits

The Fluent Bit input plugins have memory buffer limits that can be used to help prevent the container from being terminated for exceeding memory limits. Once an input plugin reaches its memory buffer limit, all new incoming data is instead buffered to file system.

Memory buffer limits are disabled by default and can be enabled by adding the annotation `fluentbit.couchbase.com/mem.buf.limits.enabled` to a pod.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  servers:
  - name: default
    pod:
      metadata:
        annotations:
          fluentbit.couchbase.com/mem.buf.limits.enabled: "true"
```

See [Fluent Bit Memory Buffer Limits](https://docs.fluentbit.io/manual/administration/backpressure#mem%5Fbuf%5Flimit) and [Fluent Bit Buffering and Storage](https://docs.fluentbit.io/manual/administration/buffering-and-storage) from more information.

### [](#using-default-log-forwarding)Using Default Log Forwarding

A Couchbase deployment is considered to be using _default log forwarding_ when the Couchbase-supplied defaults for both the _log processor image_ and the _log forwarding configuration_ are being used.

[CouchbaseCluster](resource/couchbasecluster.md) Parameters Involved with Default Log Forwarding

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  logging:
    server:
      enabled: true
      manageConfiguration: true (1)
      configurationName: “fluent-bit-config” (2)
      sidecar:
        image: couchbase/fluent-bit:1.2.3” (3)
        configurationMountPath: “/fluent-bit/config/”
        resources:
          requests:
            cpu: 100m
            memory: 500Mi
```

| **1** | [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration): When this field is set to true (the default), the Kubernetes Operator ensures that the logging sidecar container always uses the default log forwarding configuration. The Kubernetes Operator accomplishes this by creating a Secret that contains the default log forwarding configuration, which is then consumed by the logging sidecar container. The name of the Secret will be whatever name is specified in [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname). If a Secret already exists with the same name, the Kubernetes Operator overwrites it, ensuring that the default log forwarding configuration is maintained.                                                                                |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname): This field defines the name of the Secret that contains the log forwarding configuration that will be consumed by the logging sidecar container. This field defaults to fluent-bit-config and will be the name of the Secret that gets automatically created by the Kubernetes Operator when [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) is set to true. If running multiple clusters in the same Kubernetes namespace, make sure to use a different name for the Secret of each cluster rather than attempting to share the same Kubernetes Secret.                                                                                                                                                        |
| **3** | [couchbaseclusters.spec.logging.server.sidecar.image](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-image): This field specifies the container image that the Kubernetes Operator will use for deploying the logging sidecar container. This field defaults to couchbase/fluent-bit:1.2.3, which pulls the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit). You may need to modify this field if your Kubernetes nodes can’t pull from the Docker public registry. When [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) is set to true, then the default log processor image supplied by Couchbase (or an image that is effectively equivalent) must also be used. This is because the default log forwarding configuration requires certain features that are a part of the default image. |

By default, this configuration will only output to the standard console output, however, there are other output plugins included that do not match any existing streams. It is possible to enable matching of streams to output plugins by setting the `fluentbit.couchbase.com/<PLUGIN>_MATCH` annotation. The following is an example for Loki usage.

      pod:
        metadata:
          annotations:
            fluentbit.couchbase.com/loki.match: "*"
            fluentbit.couchbase.com/loki.host: loki.monitoring

Other supported output plugins include Elasticsearch and Splunk. See [Configuring Couchbase Fluent Bit](https://github.com/couchbase/couchbase-fluent-bit#configuration) for more detailed output configuration options.

### [](#using-custom-log-forwarding)Using Custom Log Forwarding

A Couchbase deployment is considered to be using _custom log forwarding_ when either a custom _log processor image_ and/or a custom _log forwarding configuration_ is being used for log forwarding.

[CouchbaseCluster](resource/couchbasecluster.md) Parameters Involved with Custom Log Forwarding

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  logging:
    server:
      enabled: true
      manageConfiguration: false (1)
      configurationName: fluent-bit-config” (2)
      sidecar:
        image: couchbase/fluent-bit:1.2.3” (3)
        configurationMountPath: “/fluent-bit/config/” (4)
        resources:
          requests:
            cpu: 100m
            memory: 500Mi
```

| **1** | [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration): When this field is set to false (defaults to true), the Kubernetes Operator allows the Secret specified in [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname) to contain a non-default log forwarding configuration. This field _must_ be set to false in order to use a custom log forwarding configuration, otherwise the Kubernetes Operator will always reconcile and update the Secret with the _default_ log forwarding configuration. If [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) was ever set to true when you enabled log forwarding, then the Kubernetes Operator will have already created the default Secret. In this situation, if you were to then set this field to false, the logging sidecar container would continue to consume the default Secret. You could then choose to add your custom log forwarding configuration to this same Secret. However, if you were to change [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname) to point to a different Secret, it won’t get picked up until the next time a pod starts. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname): This field defines the name of the Secret that contains the _custom_ log forwarding configuration that will be consumed by the logging sidecar container. When [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) is set to false, then [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname) _must_ specify the name of a Secret that currently exists in the same namespace. Otherwise, _new Couchbase pods will not start_, since they will be waiting on a non-existent Secret. Since the log forwarding configuration is stored in a Secret, it can be shared by two or more Couchbase clusters in the same namespace. This has the benefit of allowing you to manage a single log forwarding configuration for multiple clusters. However, when sharing a _custom_ log forwarding configuration between clusters, it’s important to remember that setting [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) to true on any of the clusters will overwrite the shared Secret with the _default_ log forwarding configuration.                      |
| **3** | [couchbaseclusters.spec.logging.server.sidecar.image](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-image): If desired, you can use this field to specify a custom log processing image. A few reasons for specifying a custom image include adding certificates for self-signed endpoints internally, or using another implementation of either the Fluent Bit image or any other log forwarder/processor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **4** | [couchbaseclusters.spec.logging.server.sidecar.configurationMountPath](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-configurationmountpath): This field defines the location to mount the Secret into the logging sidecar container. This field currently defaults to the usual Fluent Bit mount path (/fluent-bit/config/). This field only needs to be modified if a custom image is specified in [couchbaseclusters.spec.logging.server.sidecar.image](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-image), and only if that image requires a non-default mount path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## [](#creating-a-custom-log-forwarding-configuration)Creating a Custom Log Forwarding Configuration

Since a log forwarding configuration can contain sensitive information, it is stored in a Kubernetes Secret. The Secret is used to [populate the volume mounted into the sidecar](https://kubernetes.io/docs/concepts/configuration/secret/#restrictions) so that the actual _configuration files_ get picked up by the log processor.

When [using default log forwarding](#using-default-log-forwarding), the Kubernetes Operator automatically creates a Secret named `fluent-bit-config` that contains the default log forwarding configuration. This configuration, which can be viewed on [GitHub](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/fluent-bit.conf), is used by the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) in order to provide features like automatic _parsing_ of a number of supported logs, automatic _filtering_ for adding useful information to the logs (e.g. pod host names), as well as optional log _redaction_ (another type of filtering).

When [using _custom_ log forwarding](#using-custom-log-forwarding), the Kubernetes Operator does _not_ automatically create a log forwarding configuration Secret. Instead, the administrator is expected to create a custom Secret themselves, and specify that Secret in [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname).

The rest of this section covers some relatively simple ways in which you can customize the default log forwarding configuration, such as limiting the number of forwarded logs, and enabling log redaction. However, since the Couchbase-supplied log processor image is based on Fluent Bit, you can technically customize the log forwarding configuration with any kind of configuration that is [supported by Fluent Bit](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit). Some examples of these types of customizations are covered in the tutorial [Configure Log Forwarding](howto-couchbase-log-forwarding.md).

|  | Only custom configurations that leverage the built-in parsing, redaction, and other standard features of the Couchbase-supplied log processor image are supported. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#create-custom-log-forwarding-config-secret)Creating a Secret That Contains a Custom Log Forwarding Configuration

The following is an example of a custom log forwarding configuration Secret that is based on the [default configuration](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/fluent-bit.conf), but which limits the number of Couchbase logs that are processed and forwarded to just the Couchbase [audit log](howto-manage-couchbase-logging.md#configuring-audit-logging):

Example: Custom Log Forwarding Configuration Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config (1)
stringData:
  fluent-bit.conf: | (2)
    [SERVICE]
        flush        1
        daemon       Off
        log_level    Warning
        parsers_file /fluent-bit/etc/parsers-couchbase.conf (3)

    # @include /fluent-bit/etc/couchbase/in-*.conf (4)
    @include /fluent-bit/etc/couchbase/in-audit-log.conf (5)

    [FILTER]
        Name modify
        Match couchbase.log.*
        Add pod ${HOSTNAME}
        Add logshipper couchbase.sidecar.fluentbit

    [OUTPUT] (6)
        name  stdout
        match couchbase.log.audit (7)
```

| **1** | metadata.name: The Kubernetes Operator expects the default name fluent-bit-config. If you use a different name, then you will need to specify that name in [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | stringData.fluent-bit.conf: Log forwarding configuration files are defined here in the stringData field of the Secret (the data field is also [potentially an option](https://kubernetes.io/docs/concepts/configuration/secret/)). The fluent-bit.conf file is specified with a field that starts with a space and a vertical bar (\|), followed by the contents of the [_main configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file). Note that Fluent Bit is very particular about its [format and schema](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/format-schema) — files must all follow the same indentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **3** | /fluent-bit/etc/parsers-couchbase.conf: This is the path to the built-in file that contains all of the default [_parser configurations_](https://docs.fluentbit.io/manual/pipeline/filters/parser) in the Couchbase-supplied log processor image (you can view this file on [GitHub](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/parsers-couchbase.conf)). You should only have to modify this if you’re using a custom log processor image that invokes a parser file from a different location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **4** | @include /fluent-bit/etc/couchbase/in-\*.conf: This is the default [_input configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Finput) that processes most Couchbase logs. Since the example is meant to only process the Couchbase audit log, this line is commented out. Couchbase logs are supported by individual _input configurations_, with those that are [_included_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Finclude%5Ffile-1) in the default configuration being prefixed with in-. Therefore by including a wildcard in-\*.conf, all default input configurations are invoked. Some logs are not included by default. The individual input configurations for non-default logs are ones that are _not_ prefixed with in-. The reason that a particular log is left out of the default input configuration is often because the log has negligible value compared to the load that it puts on the log processor. About Input Configurations Input configurations determine _which_ Couchbase logs are processed, as well as some details about _how_ they are processed. A typical input configuration for a Couchbase log will specify (among other things): the input plugin (usually [tail](https://docs.fluentbit.io/manual/pipeline/inputs/tail)), the logs that the input configuration applies to, the parsers to use on those logs, and the [tags](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) to apply to those logs. Each Couchbase log is supported by an input configuration, with many input configurations supporting more than one log. The reason input configurations usually support more than one log is because certain logs are similar enough that they can share the same input plugin, parser(s), etc. Across all available input configurations, each Couchbase logging event can be captured. |
| **5** | @include /fluent-bit/etc/couchbase/in-audit-log.conf: This is the path to the built-in file that contains the input configuration that processes just the Couchbase audit log (you can view this file on [GitHub](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-audit-log.conf)). Since this line is [_included_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Finclude%5Ffile-1), and @include /fluent-bit/etc/couchbase/in-\\\*.conf is commented out, only the Couchbase audit log will be processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **6** | A log forwarding configuration includes one or more [_output configurations_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file#config%5Foutput). The default output configuration forwards the processed logs to the [standard output](https://docs.fluentbit.io/manual/pipeline/outputs/standard-output) of the logging container. A log forwarding configuration can include more than one output configuration. This allows for specific logs to be [_routed_](https://docs.fluentbit.io/manual/concepts/data-pipeline/router) to different, or multiple, destinations. For example, all Couchbase logs could be sent to standard output, with the Couchbase audit log also being sent to AWS S3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **7** | couchbase.log.audit: By default, all parsed Couchbase log events are [_tagged_](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) with couchbase.log._<name-of-log_\>. Therefore, specifying the [_match_](https://docs.fluentbit.io/manual/concepts/key-concepts#match) couchbase.log.audit ensures that only Couchbase audit log events are sent to the specified output destination. (The default output configuration normally uses the wildcard match couchbase.log.\* to forward all tagged Couchbase logs to the output.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

You can copy the [example](#custom-log-forwarding-config-secret) Secret above and create it in your Kubernetes cluster for use with existing and future Couchbase cluster deployments. However, please review [Using Custom Log Forwarding](#using-custom-log-forwarding), as there are a few things that you need to be aware of when creating a custom log forwarding configuration Secret. In particular, you should make sure that any Couchbase cluster deployment that references the Secret in [couchbaseclusters.spec.logging.server.configurationName](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-configurationname) _also_ has [couchbaseclusters.spec.logging.server.manageConfiguration](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-manageconfiguration) set to `false`, otherwise the Kubernetes Operator will overwrite the custom Secret with the _default_ log forwarding configuration.

### [](#updating-existing-custom-log-forwarding-configuration)Updating an Existing Custom Log Forwarding Configuration

Further updates can be made to a custom log forwarding configuration Secret, even after it has been [created](#create-custom-log-forwarding-config-secret) in Kubernetes and consumed by the `logging` sidecar containers in Couchbase deployments. Changing the Secret will update the volume in the sidecar, and when the configuration change is detected in the [couchbaseclusters.spec.logging.server.sidecar.configurationMountPath](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-configurationmountpath) directory, the watcher process restarts Fluent Bit internally to pick it up without having to restart the entire Couchbase Server pod.

The ability to restart Fluent Bit internally is a special characteristic of the Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit). If you’re using a custom sidecar container image, be aware that Fluent Bit, on its own, does not currently support [dynamic reload](https://github.com/fluent/fluent-bit/issues/365) of its configuration.

|  | The Couchbase-supplied log forwarding implementation does not currently support log buffering during restart. Therefore, log events that occur while Fluent Bit is restarting may be lost. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#configuring-log-redaction)Configuring Log Redaction

The Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) provides optional support for [_log redaction_](concept-couchbase-logging.md#log-redaction), whereby sensitive data from Couchbase log events are redacted before the events are forwarded to standard console output or other locations. Log redaction isn’t enabled by default, and therefore must be enabled via the [log forwarding configuration Secret](#create-custom-log-forwarding-config-secret).

|  | This section describes how to configure the built-in LUA-based log redaction facility. However, there are simpler, more rudimentary methods of performing log redaction that may be more desirable depending on the use-case. Refer to log forwarding [tutorial](#) for examples. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The following example is the same custom log forwarding configuration Secret from the section [Creating a Secret That Contains a Custom Log Forwarding Configuration](#create-custom-log-forwarding-config-secret), except that it is configured to additionally perform redaction of the audit log:

Example: Custom Log Forwarding Configuration That Redacts the Couchbase Audit Log

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |
    [SERVICE]
        flush        1
        daemon       Off
        log_level    Warning
        parsers_file /fluent-bit/etc/parsers-couchbase.conf

    @include /fluent-bit/etc/couchbase/in-audit-log.conf

    [FILTER]
        Name    lua
        Match   couchbase.log.audit (1)
        script  /fluent-bit/etc/redaction/redaction.lua (2)
        call    cb_sub_message (3)

    [FILTER]
        Name modify
        Match couchbase.log.*
        Add pod ${HOSTNAME}
        Add logshipper couchbase.sidecar.fluentbit

    [OUTPUT]
        name  stdout
        match couchbase.log.audit (4)

  redaction.salt: salty (5)
```

| **1** | couchbase.log.audit: Log events that match this tag will be processed for redaction. In this example, only events from the audit log will be processed. To have all logs processed for redaction, you can specify the wildcard couchbase.log.\*.                                                                                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | redaction.lua: This is the path to the Couchbase-supplied [LUA script file](https://github.com/couchbase/couchbase-fluent-bit/blob/main/redaction/redaction.lua) in the default Couchbase-supplied log processor image. You should only have to modify this if you’re using a custom log processor image that invokes a LUA script from a different location.                                                                        |
| **3** | cb\_sub\_message: This is the function that is called within the Couchbase-supplied LUA script file. You should only have to modify this if you’re using a custom log processor image and a custom LUA script.                                                                                                                                                                                                                       |
| **4** | couchbase.log.audit: Specifying couchbase.log.audit as the match ensures that only Couchbase audit log events are forwarded to standard console output. As a means of reducing load on the logging container, it is recommended to only match the tags of the specific logs that you want to redact. LUA scripting has an overhead and it is recommended to use at least one extra Fluent Bit worker thread if you enable redaction. |
| **5** | redaction.salt: You can optionally define a custom salt for the hashing of tagged data. The salt is specified in the configuration Secret as a separate file/value (in the example, the salt value is salty). If a salt is not specified, the Kubernetes Operator will default to using the cluster name as the salt.                                                                                                                |

After [updating](#updating-existing-custom-log-forwarding-configuration) the log forwarding configuration with the [example](#custom-log-forwarding-config-secret-with-redaction) above, you’ll notice output similar to the following, showing the redacted strings as hashes:

[0] couchbase.log.audit: [1615320737.445039000, {"filename":"/fluent-bit/test/logs/audit.log","bucket":"default","description":"Cats are <ud>00b335216f27c1e7d35149b5bbfe19d4eb2d6af1</ud> than dogs, and <ud>888f807d45ff6ce47240c7ed4e884a6f9dc7b4fb</ud>","id":20492,"name":"select bucket","peername":"127.0.0.1:56021","real_userid":{"domain":"local","user":"@ns_server"},"sockname":"127.0.0.1:11209","timestamp":"2021-03-09T20:12:17.445039Z"}]

One thing to note about the above configuration is that the log processor is _only_ outputting a redacted version of the audit log. There may be situations where it is desired to have the log processor output both a redacted _and_ an unredacted version of a particular log.

The following is an example of a custom log forwarding configuration Secret that creates an additional stream of the Couchbase audit log that is then redacted and forwarded to a separate output:

Example: Custom Log Forwarding Configuration _with Separate Redaction Stream_

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: fluent-bit-config
stringData:
  fluent-bit.conf: |
    [SERVICE]
        flush        1
        daemon       Off
        log_level    Warning
        parsers_file /fluent-bit/etc/parsers-couchbase.conf

    @include /fluent-bit/etc/couchbase/in-*.conf (1)

    [FILTER]
        Name modify
        Match couchbase.log.*
        Add pod ${HOSTNAME}
        Add logshipper couchbase.sidecar.fluentbit

    [FILTER] (2)
        Name rewrite_tag
        Match couchbase.log.audit
        Rule message .* couchbase.log.audit.redact true

    [FILTER] (3)
        Name    lua
        Match   couchbase.log.*.redact
        script  /fluent-bit/etc/redaction/redaction.lua
        call    cb_sub_message

    [OUTPUT] (4)
        name  stdout
        match couchbase.log.*

    [OUTPUT] (5)
        Name                         s3
        Match                        couchbase.log.audit.redact
        bucket                       my-bucket
        region                       us-west-2
        total_file_size              250M
        s3_key_format                /$TAG[2]/$TAG[0]/%Y/%m/%d/%H/%M/%S
        s3_key_format_tag_delimiters .-

  redaction.salt: salty
```

| **1** | @include /fluent-bit/etc/couchbase/in-\*.conf: specifies the default input configuration that processes most Couchbase logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | A [rewrite\_tag](https://docs.fluentbit.io/manual/pipeline/filters/rewrite-tag) filter is defined in order to duplicate the Couchbase audit log events. Match couchbase.log.audit: specifies that only the events with the tag couchbase.log.audit are to be selected. Rule message .\* couchbase.log.audit.redact true: specifies that a duplicate of each selected Couchbase audit log event is to be emitted with the new tag couchbase.log.audit.redact. The final value in the rule — true — specifies that the events with the old tag (couchbase.log.audit) are to be preserved. The final result is two streams of the same audit log events: one stream with the tag couchbase.log.audit, and another with the tag couchbase.log.audit.redact. |
| **3** | A [LUA filter](https://docs.fluentbit.io/manual/pipeline/filters/lua) is defined in order to perform redaction on one of the streams of audit log events. Match couchbase.log.\*.redact: specifies that events with the tag suffix .redact are to be selected and subject to redaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **4** | An output configuration is defined that forwards all _unredacted_ Couchbase log events to the [standard output](https://docs.fluentbit.io/manual/pipeline/outputs/standard-output) of the logging container. match couchbase.log.\*: specifies that the log events with the wildcard tag couchbase.log.\* are to be selected and forwarded. Note that this includes the unredacted audit log events tagged couchbase.log.audit.                                                                                                                                                                                                                                                                                                                         |
| **5** | A second output configuration is defined that forwards _redacted_ Couchbase audit log events to the [Amazon S3](https://docs.fluentbit.io/manual/pipeline/outputs/s3). Match couchbase.log.audit.redact: specifies that only the audit log events with the tag couchbase.log.audit.redact (the ones that have been redacted) are to be selected and forwarded.                                                                                                                                                                                                                                                                                                                                                                                          |

## [](#about-custom-log-processor-images)About Custom Log Processor Images

A different container image may be used in order to implement your own log processor and forwarding configuration. [couchbaseclusters.spec.logging.server.sidecar.image](resource/couchbasecluster.md#couchbaseclusters-spec-logging-server-sidecar-image) supports specifying a different image and/or version for log forwarding support. For example, this field can be used to specify a custom image with self-signed certificates. It can also be used to specify an image made available by a public cloud provider, such a [AWS for Fluent Bit](https://github.com/aws/aws-for-fluent-bit).

It’s important to note that the built-in parsing, redaction, and other configurations provided by the Couchbase-supplied log processor image are lost if a stock log processor image is used.