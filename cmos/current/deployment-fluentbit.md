---
title: Fluent Bit deployment
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/deployment-fluentbit.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cmos/current/deployment-fluentbit.html)

# Fluent Bit deployment

> [Fluent Bit](https://fluentbit.io/) is the recommended way to forward logs to CMOS from Couchbase Server instances. 

## [](#kubernetes-usage)Kubernetes usage

Couchbase Autonomous Operator (CAO) versions 2.2 and greater already support Fluent Bit log forwarding. Refer to the [CAO documentation](https://docs.couchbase.com/operator/current/concept-couchbase-logging.html#log-forwarding) for the full details.

The main configuration required is providing the CMOS Loki endpoint as part of the [Couchbase cluster configuration](https://docs.couchbase.com/operator/current/resource/couchbasecluster.html#couchbaseclusters-spec-servers-pod). To do this, use Couchbase Fluent Bit [versions 1.1.2 or greater](https://github.com/couchbase/couchbase-fluent-bit#releases) and supply the following annotations with appropriate values.

```yaml
            pod:
                metadata:
                    annotations:
                        # Match all logs
                        fluentbit.couchbase.com/loki_match: "*"
                        # Send to this SVC
                        fluentbit.couchbase.com/loki_host: loki.default
```

A full example of integrating is available as part of the [Kubernetes example](tutorial-kubernetes.md).

## [](#on-premise-usage)On-premise usage

Fluent Bit [already provides various supported targets](https://docs.fluentbit.io/manual/installation/supported-platforms) so on-premise installation is straight forward. For full details, please refer to the [official documentation](https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit).

For CMOS needs we must do the following:

1. Install Fluent Bit.
2. Configure Fluent Bit.

Step one is deploying the Fluent Bit binary with Couchbase Server and providing a startup script to launch it. Refer to the installation instructions above from Fluent Bit for this.

Step two is configuring fluent bit with the [configuration](https://github.com/couchbase/couchbase-fluent-bit/tree/main/conf) provided by the official Couchbase Fluent Bit image. You can either clone the repository or just copy over the configuration file. The key is to get all the configuration into the expected location for the local Fluent Bit to use, refer to the deployment guide from Fluent Bit for full details for the specific targets. Whilst this is intended primarily for CAO deployments and not officially supported on-premise, it will function there as well.

```console
$ git clone --depth 1 https://github.com/couchbase/couchbase-fluent-bit.git
$ cp -R conf/* <config directory for Fluent Bit on this OS>
```

### [](#container-deployment)Container deployment

A simplified solution would be to deploy the container solution explicitly with local volume mounts for the Couchbase Server logs. An [existing example](https://github.com/couchbase/couchbase-fluent-bit/tree/main/tools/loki-stack) and [blog post](https://blog.couchbase.com/using-fluent-bit-for-log-forwarding-processing-with-couchbase-server/) is available in the Couchbase Fluent Bit repository to show a complete stack.

```console
$ docker run --rm -d --name logger -v /opt/couchbase/var/lib/couchbase/logs/:/opt/couchbase/var/lib/couchbase/logs/:ro -e COUCHBASE_LOGS=/opt/couchbase/var/lib/couchbase/logs/ -e LOKI_MATCH="*" -e LOKI_HOST="127.0.0.1" couchbase/fluent-bit:1.1.3
```

Replace `LOKI_HOST` here with your actual DNS name or IP address for CMOS.

### [](#loki-configuration-for-fluent-bit)Loki configuration for Fluent Bit

Similar to the Kubernetes set up, make sure to set the environment variables to the appropriate values when Fluent Bit is launched.

__Table 1\. Loki configuration for Fluent Bit__
| Variable name | Description                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| LOKI\_HOST    | The (resolvable) hostname to send the logs to, i.e. where CMOS is running or another Loki stack if you want to integrate with that. |
| LOKI\_PORT    | The port open on LOKI\_HOST for Loki to receive logs, defaults to 3100 if not provided.                                             |
| LOKI\_MATCH   | The set of logs to match to send to Loki, this can be a wildcard or specific logs in the format couchbase.log.<file>.               |

> [!IMPORTANT]
> In addition to the above Loki specific configuration make sure to set the [environment variables Fluent Bit requires](https://github.com/couchbase/couchbase-fluent-bit#configuration).
> 
> The [example](https://github.com/couchbase/couchbase-fluent-bit/tree/main/tools/loki-stack) and [blog post](https://blog.couchbase.com/using-fluent-bit-for-log-forwarding-processing-with-couchbase-server/) cover this as well in more detail.