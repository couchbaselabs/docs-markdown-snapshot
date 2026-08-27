---
title: Verifying the Couchbase Server Installation
description: Testing the connection to Couchbase Server can be performed in a
  number of different ways.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/testing.adoc
  xref: xref:7.2@server:install:testing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/testing.html)

# Verifying the Couchbase Server Installation

> Testing the connection to Couchbase Server can be performed in a number of different ways. 

## [](#basic-verification)Basic Verification

Connecting to the Couchbase Server Web Console with a Web browser provides basic confirmation that a node is available.

On all platforms, you can access the Web Console by connecting to the embedded Web server on port 8091\. For example, if your server can be identified on your network as `serverA`, you can access the Web Console by going to `http://serverA:8091/` or `http://<serverA's-IP-address>:8091/`. (If you set up Couchbase Server on a port other than `8091`, go to that specified port.) You should clear your browser's cache before attempting to access to the Web Console.

If you are logged into the node itself, you can go to `http://localhost:8091`. You can also use the `couchbase-cli` command to query node to confirm that it is available.

> [!NOTE]
> The Web Console uses the same port as smart clients when communicating with Couchbase Server. If you can connect to the Web Console from a particular machine, then administration and database clients on the same machine can also connect to the core cluster port and perform operations. The Web Console will provide a warning if the Web browser loses connectivity to the node.

## [](#detailed-verification)Detailed Verification

To verify that clients can connect to the node, you can use [cbworkloadgen](#testing-with-cbworkloadgen).

The `cbworkloadgen` command is a python program that performs basic operations (reads and writes) against the Couchbase Server cluster.

Testing With cbworkloadgen

The command `cbworkloadgen` generates random data, then performs reads and writes of this data in Couchbase Server. It is not intended to be a performance benchmarking tool.

To test a Couchbase Server installation using `cbworkloadgen`, execute the following command, supplying the IP address of the running node:

> cbworkloadgen -n [host]:8091
        Thread 0 - average set time : 0.0257480939229 seconds , min : 0.00325512886047 seconds , max : 0.0705931186676 seconds , operation timeouts 0

The progress and activity of the tool can also be monitored within the Web Console.

Further details about `cbworkloadgen` can be found on [its CLI reference page](../cli/cbtools/cbworkloadgen.md).