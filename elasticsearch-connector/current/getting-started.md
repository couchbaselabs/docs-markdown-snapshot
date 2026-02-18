---
title: Getting Started
description: Learn how to install the Elasticsearch Connector.
editUrl: https://github.com/couchbase/docs-elastic-search/edit/main/modules/ROOT/pages/getting-started.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/elasticsearch-connector/current/getting-started.html)

# Getting Started

> A brief overview of the various ways to run the Couchbase Elasticsearch Connector, followed by step-by-step instructions for installing the connector in solo/distributed mode. 

## [](#operational-modes)Operational Modes

The connector can be deployed in different modes depending on the requirements of your project.

### [](#solo)Solo

In the simplest mode, the connector runs as a single standalone Java process. This is referred to as "solo" mode. Solo mode is appropriate for experimentation and low-traffic environments.

If this is your first time working with the connector, we recommend starting with solo mode.

### [](#distributed)Distributed

If a single connector process cannot handle all of your traffic, multiple connector processes can be deployed in "distributed" mode.

![Distributed data flow with ElasticSearch](_images/diag-c94b8ced3fc2374e5b94104554a7a498574356e7.svg) 

Figure 1\. Distributed data flow with ElasticSearch

In this mode each process is manually configured to handle only a subset of the replication workload. Distributed mode can scale to handle high volumes of traffic, but is inflexible; adding an additional process to a distributed connector group requires stopping and reconfiguring _all_ of the processes in the group.

> [!NOTE]
> Solo mode is effectively the same as distributed mode with a group size of 1\.

### [](#autonomous-operations)Autonomous Operations

For scalable environments that require high availability and centralized management, you can run the connector in "autonomous operations" (AO) mode. This mode is similar to distributed mode in that each process handles a subset of the replication workload, but improves upon it by using a [HashiCorp Consul](https://www.consul.io) cluster to coordinate the activities of the connector processes. This enables connector processes to dynamically join or leave the group, and allows an administrator to reconfigure the group on-the-fly without needing to shut down all of the processes.

AO mode is discussed in more detail in the [Autonomous Operations](autonomous-operations.md) guide. The page you’re reading now is focused on solo and distributed mode; we recommend becoming familiar with these modes before progressing to AO mode.

## [](#pre-requisites)Pre-requisites

Linux is required for production deployments. macOS is fine for experimentation and development, but is not officially supported.

To deploy the connector in solo or distributed mode, you will need:

* The [latest release](release-notes.md) of Couchbase Elasticsearch Connector.
* [Compatible versions](compatibility.md) of Java, Elasticsearch, and Couchbase Server.

> [!NOTE]
> Couchbase Enterprise Edition is required if you wish to enable secure connections to Couchbase. Likewise, versions of Elasticsearch prior to 6.8 and 7.1 require an additional license in order to support secure connections. Trial versions of both are available.

## [](#pre-flight-check)Pre-flight Check

Verify the Elasticsearch cluster is up and running (the default port is `9200`).

```console
$ curl localhost:9200
```

Expected result is something like:

```json
{
  "name" : "K3RqW4F",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "Bw-Ta0wDTcekzQIhXZHGkg",
  "version" : {
    "number" : "5.6.5",
    "build_hash" : "6a37571",
    "build_date" : "2017-12-04T07:50:10.466Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.1"
  },
  "tagline" : "You Know, for Search"
}
```

Verify that Couchbase Server is running.

```console
$ curl localhost:8092
```

Expected result is something like:

```json
{"couchdb":"Welcome","version":"v4.5.1-60-g3cf258d","couchbase":"5.0.2-5506-community"}
```

## [](#installation)Installation

Extract the connector distribution archive. This should give you a directory called `couchbase-elasticsearch-connector-<version>`. This directory will be referred to as `$CBES_HOME`.

Add `$CBES_HOME/bin` to your `PATH`.

## [](#configuration)Configuration

Copy `$CBES_HOME/config/example-connector.toml` to `$CBES_HOME/config/default-connector.toml`.

> [!TIP]
> The connector commands get their configuration from `$CBES_HOME/config/default-connector.toml` by default. You can tell them to use a different config file with the `--config <file>` command line option.

Take a moment to browse the settings available in `default-connector.toml`. Make sure the Couchbase and Elasticsearch credentials and hostnames match your environment. Note that the passwords are stored separately in the `$CBES_HOME/secrets` directory.

The sample config will replicate documents from the Couchbase `travel-sample` bucket. Go ahead and [install sample buckets](../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui) now if you haven’t already.

## [](#controlling-the-connector)Controlling the Connector

The command-line tools in `$CBES_HOME/bin` are used to start the connector and manage replication checkpoints.

### [](#starting-the-connector)Starting the connector

Run this command:

cbes

The connector should start copying documents from the `travel-sample` bucket into Elasticsearch.

### [](#stopping-the-connector)Stopping the connector

A connector process will shut down gracefully in response to an interrupt signal (ctrl-c, or `kill -s INT <pid>`).

## [](#distributed-mode)Distributed Mode

The throughput of the connector is limited by the time it takes for Elasticsearch to index documents. If you determine a single instance of the connector is unable to saturate your Elasticsearch indexing capacity, you can run multiple instances of the connector in distributed mode for horizontal scalability.

A Couchbase bucket consists of many separate partitions (also known as virtual buckets, abbreviated as "vbuckets"). When the connector runs in distributed mode, each instance of the connector is responsible for replicating a different subset of the partitions.

To run the connector in distributed mode, install the connector on multiple machines. Make sure the connector configuration is identical on each machine, except for the `memberNumber` config key, which must be unique within the group. Set the `totalMembers` config key to the total number of connector processes in the group.

> [!WARNING]
> Make sure to stop all of the connector instances in a group before changing the number of instances in the group.

When a connector instance runs in distributed mode, it replicates from only the partitions that correspond to its group membership configuration.

## [](#managing-checkpoints)Managing Checkpoints

The connector periodically saves its replication state by writing metadata documents to the Couchbase bucket. These documents have IDs starting with `_connector:cbes:`

Command line tools are provided to manage the replication checkpoint.

> [!CAUTION]
> You must stop all connector instances in a group before modifying the replication checkpoint, otherwise the changes will not take effect. (This restriction does not apply when running in [Autonomous Operations mode](autonomous-operations.md).)

The following commands are specific to the solo and distributed modes. [Autonomous Operations mode](autonomous-operations.md) has its own separate commands for managing checkpoints.

### [](#checkpoint-command-config)Configuring the checkpoint management commands

The checkpoint management commands use the same config file as the connector. The `--config` argument tells the checkpoint management command the filesystem path of the config file to use. For example:

cbes-<command> --config <path/to/connector/config.toml>

If the `--config` argument is not specified, the path defaults to `config/default-connector.toml`.

When running a checkpoint management command from an environment where the connector is already installed and configured, use the same config file as the connector.

If you want to run a checkpoint management command in a different environment, you’ll need to:

1. Get the connector distribution archive and unzip it.
2. Edit the `config/example-connector.toml` and `config/secrets/couchbase-password.toml` files to match the settings of the connector whose checkpoints you want to manage.

The checkpoint management commands use only the following parts of the config file:

* The `name` field from the `[group]` section.
* The `[couchbase]` section.
* The `[couchbase.clientCertificate]` section, if applicable.
* The `[couchbase.env]` section, if applicable.

See [connector configuration](configuration.md) for details about these settings.

> [!WARNING]
> Although the other config sections are unused by the checkpoint management commands, they must still be present in the config file, otherwise the commands fail and complain of an invalid config file. Any files referenced by the config must also be present (for example, the contents of the `secrets` directory).

> [!TIP]
> Instead of hardcoding values in the connector config file, you can pass in values via environment variables. This requires editing the config file to use environment variable placeholders.
> 
> For example, you could edit your config file to say:
> 
> ```toml
> [group]
> name = '${GROUP_NAME}'
> ```
> 
> Then specify the group name by setting an environment variable when running the checkpoint management command:
> 
> env GROUP_NAME=example-group \
>     cbes-<command> --config <path/to/connector/config.toml>
> 
> For more details, see [using environment variable placeholders in config files](configuration.md#environment-variables).

### [](#save-checkpoint)Saving the current replication state

To create a backup of the current state:

cbes-checkpoint-backup --output <checkpoint.json>

This will create a checkpoint document on the local filesystem. On Linux, to include a timestamp in the filename:

cbes-checkpoint-backup \
    --output checkpoint-$(date -u +%Y-%m-%dT%H:%M:%SZ).json

This command is safe to use while the connector is running, and can be triggered from a cron job to create periodic backups.

### [](#restore-checkpoint)Reverting to a saved checkpoint

If you want to rewind the event stream and re-index documents starting from a saved checkpoint, first stop all running connector processes in the connector group. Then run:

cbes-checkpoint-restore --input <checkpoint.json>

The next time you run the connector, it will resume from the checkpoint you just restored.

### [](#reset-checkpoint)Resetting the connector

If you want to discard all replication state and start streaming from the beginning, first stop all of the connector processes, then run:

cbes-checkpoint-clear

### [](#catch-up-checkpoint)Setting the checkpoint to "now"

If you want to reset the connector so it starts from the current state of the bucket, first stop all connector processes in the group, then run:

cbes-checkpoint-clear --catch-up

## [](#whats-next)What’s Next?

After successfully deploying the connector in solo or distributed mode, you’re ready to dive into the [Autonomous Operations](autonomous-operations.md) guide.