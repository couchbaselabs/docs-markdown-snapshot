---
title: Install Couchbase Server
description: Install and set up Couchbase Server to continue following the
  Student Record System tutorial.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/tutorials/pages/install-couchbase-server.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:tutorials:install-couchbase-server.adoc[]
---

[View original HTML](/server/7.6/tutorials/install-couchbase-server.html)

# Install Couchbase Server

> Install and set up Couchbase Server to continue following the Student Record System tutorial. 

## [](#installation)Installation

You can install and run Couchbase Server as a standalone application or as a Docker instance.

### [](#standalone)Standalone

To download Couchbase Server as a standalone application:

1. Go to the [Couchbase download page](https://www.couchbase.com/downloads/).
2. Go to **Server** **Couchbase Server Community**.
3. Select a **Version** and an **OS** and click **Download**.

After Couchbase Server is finished downloading, follow the instructions to install it on your machine.

### [](#docker)Docker

To download Couchbase Server as a Docker instance:

1. Download [Docker](https://docs.docker.com/get-docker/).
2. Open a terminal window and run this command to provision the server image, set up the storage location, and run the server:  
```sh  
docker run -t --name db -p 8091-8096:8091-8096 -p 11210-11211:11210-11211 \  
couchbase/server:community-7.6.1  
```

## [](#set-up-a-cluster)Set Up a Cluster

Couchbase Server can run as its own cluster or join another cluster to form a multi-node system. For this tutorial, your server runs as a single node.

To set up a cluster:

1. Make sure your Couchbase Server is running.
2. In your browser, go to `http://127.0.0.1:8091` to access your server’s configuration page.
3. Click **Setup New Cluster**.
4. For your cluster name, enter **student-cluster**.
5. For your username, enter **username**.
6. For your password, enter **password**.
7. Click **Next: Accept Terms**.
8. Accept the terms and conditions and click **Finish With Defaults** to access the **Dashboard** page.

## [](#next-steps)Next Steps

After installing Couchbase Server and setting up a cluster, you can [implement a data model](buckets-scopes-and-collections.md).