---
title: Connect To Your Cluster
description: Use the Connect page to choose how you want to connect to your cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/connect.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/get-started/connect.html)

# Connect To Your Cluster

> Use the Connect page to choose how you want to connect to your cluster. 

This page covers connecting to your cluster from:

* [SDKs](#home::sdk.adoc)
* [Couchbase Shell (cbsh)](../reference/command-line-tools.md#couchbase-shell-cbsh)
* [Command line tools](../reference/command-line-tools.md)
* [IDE Plugins and Extensions](../third-party/integrations.md#ide-integrations)

To enable access to your cluster via the Data API, see [Get Started with the Data API](../data-api-guide/data-api-start.md).

## [](#prerequisites)Prerequisites

The procedures on this page assume the following:

* You have [configured cluster access](../clusters/manage-database-users.md#create-database-credentials) by creating a cluster access credential. You’ll need the username and password for the cluster credential to connect to the cluster.
* You have [added your IP address](../clusters/allow-ip-address.md#accessing-allowed-ips-in-the-capella-ui) to the cluster’s list of allowed IPs.
* You have [downloaded the security certificate](create-account.md#next-steps) for your cluster. The certificate is bundled with all of the Couchbase SDKs, except the C SDK (libcouchbase).
* You’re not connecting from an IPv6-only environment — you need to be able to use the IPv4 records published for Capella clusters.

You can do all of this from a single location using the Connect page in the Capella UI.

## [](#connect-from-sdk-cbsh-cli-or-ide)Connect from SDK, cbsh, CLI, or IDE

Follow these steps to connect from an SDK, Couchbase Shell, the command line tools, or an IDE plugin or extension:

* SDK
* cbsh
* CLI Tools
* IDE

The Connect page in the Capella UI provides the details to connect to your cluster with an application using an [SDK](../reference/sdk-compatibility.md).

From the Capella UI:

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **SDK**.
3. Note the **public connection string** — you’ll need this to connect to the cluster.
4. If you have not already done so, follow the instructions on screen to enter an allowed IP address.
5. Choose an existing cluster user from the drop-down, or create a new cluster access user.
6. Select the preferred SDK language.
7. Now install the SDK for the language that you have chosen, following the instructions in the linked SDK docs.
8. To get started with your chosen SDK, choose a snippet or the full code sample.

  * Select **Snippet** to generate the connection code snippet for the chosen language, pre-populated with the connection string and user name. Replace `<<password>>` with the password you specified when you created the cluster access user.
  * Select **Full Code Sample** to display a full code sample for your chosen language. You can customize the code sample by choosing the bucket, scope, and collection the cluster user has access to — although some fields will be pre-populated already, such as the connection string and username.

You can find documentation and troubleshooting reference materials within the **Connect** **SDK** screen.

The [SDK Compatibility page](../reference/sdk-compatibility.md) lists the minimum supported SDK versions. Couchbase recommends using the latest version of your chosen SDK, as it contains bug fixes and feature enhancements.

The Connect page in the Capella UI provides the details to connect your cluster with [cbsh](https://couchbase.sh/) — the Couchbase Shell.

From the Capella UI:

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **Couchbase Shell**.
3. Note the **public connection string** — you’ll need this to connect to the cluster.
4. If you have not already done so, follow the instructions on screen to enter an allowed IP address.
5. Choose an existing cluster user from the drop-down, or create a new cluster access user.
6. Download and unzip the latest version of [Couchbase Shell](https://couchbase.sh) for your operating system.
7. Create a hidden folder `.cbsh` in the folder where you unzipped the binaries.
8. Copy the generated config file, including the generated connection string and username, into the hidden `.cbsh folder`, replacing `<<password>>` with the password for the specified cluster user.

Sample cbsh config file

```toml
version = 1
[[cluster]]
identifier = "capella"
connstr = "<<connection string>>"
user-display-name = ""
username = "<<username>>"
password = "<<password>>" # Replace this with password from cluster access credentials
```

You can find examples, documentation, and reference materials within the **Connect** **Couchbase Shell** page.

The Connect page in the Capella UI provides the details to connect to your cluster with the [backup](../clusters/cli-backup-restore.md#backup-and-restore-examples), [import and export](../connect/cli-import-export.md#import-and-export-with-command-line-tools-examples), and [cbq](../n1ql/n1ql-intro/cbq.md) tools.

From the Capella UI:

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **Import & Export Tools**.
3. Note the **public connection string** — you’ll need this to connect to the cluster.
4. If you have not already done so, follow the instructions on screen to enter an allowed IP address.
5. If you have not already done so, follow the instructions on screen to create a cluster access user.
6. Download the security certificate, following the instructions on screen.
7. Download and install the command line tools, following the instructions on the [command line tools reference page](../reference/command-line-tools.md#download-and-install-the-couchbase-command-line-tools).

Basic examples for the tools are given on the **Connect** **Import & Export Tools** page, along with links to their full reference pages.

The Connect page in the Capella UI provides the details to connect to your cluster with an [IDE plugin or extension](../third-party/integrations.md#ide-integrations).

From the Capella UI:

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **IDE Plugins and Extensions**.
3. Note the **public connection string** — you’ll need this to connect to the cluster.
4. If you have not already done so, follow the instructions on screen to enter an allowed IP address.
5. If you have not already done so, follow the instructions on screen to create a cluster access user.
6. Download the security certificate, following the instructions on screen.
7. Select an IDE plugin or extension:

  * [Couchbase Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-couchbase)
  * [Couchbase VS Code extension on Open VSX](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-cblite)
  * [Couchbase Plugin for JetBrains](https://plugins.jetbrains.com/plugin/22131-couchbase)
8. Follow the specific installation instructions to get started and add a cluster connection.

## [](#troubleshooting)Troubleshooting

Working across networks adds an extra layer of complexity. See the [troubleshooting documentation](../clouds/connection-troubleshooting.md) if you have problems making a connection.

## [](#next-steps)Next Steps

* [Set up a VPC peering connection](../clouds/private-network.md) to interact with Couchbase Capella over a private connection.
* [Work with your data](../guides/kv-operations.md) using an SDK or the Couchbase Shell.
* [Import and export data](../guides/load.md) using an SDK or a command line tool.
* [Backup and restore](../clusters/backup-restore.md) data using the Capella UI or a command line tool.
* Query data using the [cbq shell](../n1ql/n1ql-intro/cbq.md).