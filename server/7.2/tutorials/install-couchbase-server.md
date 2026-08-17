---
title: Install or provision the Couchbase server
description: A short tutorial that will guide the developer in downloading and
  installing Couchbase, then creating a database to store our student records.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/tutorials/pages/install-couchbase-server.adoc
  xref: xref:7.2@server:tutorials:install-couchbase-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/tutorials/install-couchbase-server.html)

# Install or provision the Couchbase server

> A short tutorial that will guide the developer in downloading and installing Couchbase, then creating a database to store our student records. 

## [](#installation)Installation

The easiest way to get started with Couchbase is to use [Capella](https://www.couchbase.com/products/capella), which allows you to set up, administer and run Couchbase clusters as a cloud service.

This tutorial is designed for use with standalone or Docker installations of the Couchbase Server. If you wish to use [the Couchbase Capella cloud service](https://www.couchbase.com/products/capella) then you can run through the tutorials for [Getting Started with Couchbase Capella](https://docs.couchbase.com/cloud/get-started/get-started.html).

This tutorial focuses on running Couchbase as a standalone application, or a `Docker` instance.

* Standalone install
* Docker install
* Capella Installation

Using any browser, navigate to <https://www.couchbase.com/downloads> to download the server installation pack.

Pick the **Couchbase server** option for your free trial.

![Couchbase download page](_images/couchbase-capella-download-page.png) 

> [!NOTE]
> You may need to fill out a brief web form before you can download the installation package.

Select **Couchbase Server**, and from there, download the community edition of the server.

![Download Couchbase community edition dialog](_images/download-couchbase-community-edition.png) 

> [!NOTE]
> Make sure you download the latest version of the server software.

Once you've downloaded the software, install it on your machine. (The method for installation will depend on your operating system).

The method for running the application will, again, depend on your host operating system. In our example, we're using a Mac, so the installation will place then executable app in the standard `Applications` folder.

First, make sure that you have Docker installed and running on your system. (You can download it from [here](https://www.docker.com/get-started)).

Open a terminal window and run the following command:

```sh
docker run -t --name db -p 8091-8096:8091-8096 -p 11210-11211:11210-11211 \
couchbase/server:enterprise-7.2
```

This will provision the server image, set up the storage location and run the server.

This tutorial is designed for use with standalone or Docker installations of the Couchbase Server. If you wish to use [the Couchbase Capella cloud service](https://www.couchbase.com/products/capella) then you can run through the tutorials for [Getting Started with Couchbase Capella](https://docs.couchbase.com/cloud/get-started/get-started.html).

## [](#set-up-a-new-cluster)Set up a new cluster

Each Couchbase server can run as its own cluster, or join another cluster to form a multi-node system. For the purposes of this basic tutorial, we're only going to concern ourselves with running as a single node.

> [!TIP]
> You can always find the server's configuration page by pointing your browser at `http://127.0.0.1:8091`.

![Click button to set up new cluster](_images/launch-couchbase-server-page.png) 

Press **Setup New Cluster** to create your new cluster. The next page will allow you to fill in details for the cluster:

![Enter the cluster details](_images/enter-cluster-details.png) 

Since we're going to be housing student records, let's call the cluster `student-cluster`. You'll also need an admin username and a strong yet memorable password. Since this is just a demonstration, leave the administrator username as `Administrator`. After you've filled in the details, press **Next: Accept Terms**.

> [!TIP]
> Since this is a tutorial, then feel free to use something like `password` for your password. In a real system, of course, you'll use something much stronger.

On the next page, you'll find the terms and conditions for using Couchbase. If you're happy with them, then check the box and press **Finish with Defaults**.

You're now on the main dashboard page.

## [](#next-steps)Next steps

Now you have installed the server and created a cluster, the next thing to do is create the database where you're going to store your documents. In [Buckets, Scopes and Collections](buckets-scopes-and-collections.md) you will also learn other ways in which Couchbase allows you to logically partition your data.