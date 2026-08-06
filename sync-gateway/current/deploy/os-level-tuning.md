---
title: OS Level Tuning
description: OS level parameters you can use to tune _Couchbase Sync&nbspGateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/deploy/pages/os-level-tuning.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:deploy:os-level-tuning.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/deploy/os-level-tuning.html)

# OS Level Tuning

> OS level parameters you can use to tune \_Couchbase Sync Gateway  

## [](#introduction)Introduction

To get the most out of Sync Gateway, you may need to tune OS-level parameters that control the maximum number of open file descriptors. This directly affects the maximum number of **sockets** Sync Gateway can have open, and therefore the maximum number of endpoints it can support.

> [!NOTE]
> The host-level instructions on this page apply to Sync Gateway installed directly on a host OS (for example, a bare-metal server or virtual machine). For container environments (Docker, Kubernetes, or similar), see [Container Environments](#container-environments).

The host-level instructions below are geared towards CentOS deployments but are broadly applicable to other Linux distributions.

## [](#container-environments)Container Environments

In a container environment, the host OS controls the upper bound on file descriptors, but each container gets its own `ulimit` set by the container runtime at startup — not by the host-level `/etc/security/limits.conf` or `sysctl` configuration. This means your Infra or Platform team, rather than the application team, typically owns this configuration.

File descriptor limits for Sync Gateway scale with the number of connected clients. There is no single fixed minimum, but the default OS limit of `1024` is insufficient for any production deployment. The recommended starting value for `nofile` (maximum open files) is `250000`, which provides headroom for high client concurrency.

> [!NOTE]
> The exact value your deployment needs depends on your expected peak concurrent client connections and the resources available on the host. Start with `250000` and adjust based on observed behavior. If you continue to see `too many open files` errors after raising the limit, see [TCP Keepalive Parameters](#tcp-keepalive-params) for additional tuning options.

### [](#docker)Docker

Pass the `--ulimit` flag when starting the Sync Gateway container to set the `nofile` limit for that container:

```bash
docker run -d \
  --ulimit nofile=250000:250000 \ (1)
  --name sync-gateway \
  -p 4984:4984 -p 4985:4985 \
  couchbase/sync-gateway
```

| **1** | Sets both the soft and hard nofile limit to 250,000 for this container. The \--ulimit flag requires Docker 1.6 or later. |
| ----- | ------------------------------------------------------------------------------------------------------------------------ |

Verify the effective limit inside the running container:

```bash
docker exec sync-gateway sh -c "ulimit -n"
```

The output should be `250000`.

### [](#kubernetes)Kubernetes

Kubernetes does not expose a direct `ulimit` field in the Pod spec. The `nofile` limit for containers is inherited from the node's container runtime configuration (containerd or CRI-O). To raise the limit, you have two options:

1. **Configure the container runtime on each node** — edit the runtime configuration (for example, containerd's `config.toml`) to raise `DefaultRlimits` for `NOFILE`.
2. **Use a privileged init container via a DaemonSet** — set the limit at the node level before the Sync Gateway pod starts.

Work with your Infra or Platform team to determine which approach fits your cluster policy. The required changes depend on your runtime, distribution, and cluster security policy, and are therefore outside the scope of Couchbase documentation.

> [!TIP]
> After applying changes, verify the effective limit from inside the running pod:
> 
> ```bash
> kubectl exec <sync-gateway-pod> -- sh -c "ulimit -n"
> ```

## [](#operating-system-file-descriptor-limits)Operating System File Descriptor Limits

Increase the max number of file descriptors available to **all processes**.

Set the number of system wide file descriptors

1. Edit the `/etc/sysctl.conf` file
2. Add the following line.  
```bash  
fs.file-max = 500000  
```
3. Apply the changes by running the following command.  
```bash  
$ sysctl -p (1)  
```

| **1** | The \-p will persist the change across reboots |
| ----- | ---------------------------------------------- |

## [](#sync-gateway-file-descriptor-limits)Sync Gateway File Descriptor Limits

Configure the maximum number of open file descriptors in Sync Gateway in line with the above changes.

See the [max\_file\_descriptors](../configuration/configuration-schema-bootstrap.md#max%5Ffile%5Fdescriptors) and [Example 1](#ex-max-file-desc).

Example 1\. Set the Maximum File Descriptors

```json
{
  "max_file_descriptors": 250000 (1)
}
```

| **1** | Default = 5000\. Setting max\_file\_descriptors higher than the OS or container nofile limit has no effect — Sync Gateway cannot exceed the limit imposed by the runtime. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#service-fd-limits)Service File Descriptor Limits

For systemd config

The `/usr/lib/systemd/system/sync_gateway.service` has a hardcoded limit specified by `LimitNOFILE=65535`.

To increase that, edit the `/sync_gateway.service` file to your desired value and restart the service.

## [](#process-fd-limits)Process File Descriptor Limits

> [!NOTE]
> This section applies only to **host-based** Sync Gateway deployments running outside of systemd. For container environments, see [Container Environments](#container-environments). For systemd deployments, see [Service File Descriptor Limits](#service-fd-limits).

> [!TIP]
> If you're using systemd, you can skip this section.

1. Increase the **ulimit** setting for max number of file descriptors available to a single process. For example, setting it to 250K will allow Sync Gateway to have 250K connections open at any given time, and leave 250K remaining file descriptors available for the rest of the processes on the machine. These settings are an example — tune them for your own use case.  
```bash  
$ ulimit -n 250000  
```
2. To persist the ulimit change across reboots, add the following lines to `/etc/security/limits.conf`:  
```bash
* soft nofile 250000
* hard nofile 250000  
```
3. Verify your changes by running the following commands:  
```bash  
$ cat /proc/sys/fs/file-max  
$ ulimit -n  
```  
The output value of both commands above should be `250000`.

See also: [Increasing ulimit and file descriptors limit on Linux](https://glassonionblog.wordpress.com/2013/01/27/increase-ulimit-and-file-descriptors-limit/)

## [](#tcp-keepalive-params)TCP Keepalive Parameters

If you have already raised the maximum number of file descriptors available to Sync Gateway, but you are still seeing "too many open files" errors, you may need to tune the TCP Keepalive parameters.

### [](#understanding-the-problem)Understanding the Problem

Mobile endpoints tend to abruptly disconnect from the network without closing their side of the connection, as described in [Section 2.3\. (Checking for dead peers)](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html) of the TCP-Keepalive-HOWTO.

By default, these connections will hang around for approximately 7200 seconds (2 hours) before they are detected to be dead and cleaned up by the tcp/ip stack of the Sync Gateway process. If enough of these connections accumulate, you can end up seeing "too many open files" errors on Sync Gateway.

If you are seeing "too many open files" errors, you can count the number of established connections coming into your sync gateway with the following command:

```bash
$ lsof -p <sync_gw_pid> | grep -i established | wc -l
```

If the value returned is near your max file descriptor limit, you can either try increasing the max file descriptor limit even further, or tune the TCP Keepalive parameters to reduce the amount of time that dead peers hold a socket open on their behalf.

### [](#%5Flinux%5Finstructions%5Fcentos%5F1)Linux Instructions (CentOS)

Tuning the TCP Keepalive settings is not without its downsides — it will increase the amount of overall network traffic on your system, because the tcp/ip stack will be sending more frequent keepalive packets in order to detect dead peers faster.

The following settings will reduce the amount of time that dead peer connections hang around from approximately 2 hours down to approximately 30 minutes. Add the following lines to your `/etc/sysctl.conf` file:

```bash
net.ipv4.tcp_keepalive_time = 600
net.ipv4.tcp_keepalive_intvl = 60
net.ipv4.tcp_keepalive_probes = 20
```

This translates to:

1. The keepalive routines wait initially for 10 minutes (600 secs) before sending the first keepalive probe.
2. Resend the probe every minute (60 seconds).
3. If no ACK response is received for 20 consecutive times, the connection is marked as broken.

To reduce the amount of time even further, you can reduce the `tcp_retries2` value. Add the following line to your `/etc/sysctl.conf` file:

```bash
net.ipv4.tcp_retries2 = 8
```

To activate the changes and persist them across reboots, run:

```bash
$ sysctl -p
```

See [Using TCP keepalive under Linux](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/usingkeepalive.html) for more details on setting these parameters.

Further Reading

* [TCP Keepalive HOWTO](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html)
* [Application control of TCP retransmission on Linux](https://stackoverflow.com/questions/5907527/application-control-of-tcp-retransmission-on-linux)
* [Proactively closing longpoll connections for endpoints that disappear from the network](https://groups.google.com/forum/#!msg/golang-nuts/rRu6ibLNdeI/0bjSmO5fN%5F8J)
* [TCP man page](https://linux.die.net/man/7/tcp)
* [Sync Gateway Issue 742](https://github.com/couchbase/sync%5Fgateway/issues/742)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)