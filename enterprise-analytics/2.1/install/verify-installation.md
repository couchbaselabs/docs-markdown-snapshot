---
title: Verify the Enterprise Analytics Installation
description: You can test your connection to Enterprise Analytics in multiple ways.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/verify-installation.adoc
  xref: xref:2.1@enterprise-analytics:install:verify-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/install/verify-installation.html)

# Verify the Enterprise Analytics Installation

> You can test your connection to Enterprise Analytics in multiple ways. 

## [](#basic-verification)Basic Verification

For a basic confirmation that a node is available, connect to the Enterprise Analytics Web Console with a web browser.

If you set up Enterprise Analytics on a port other than `8091`, go to that specified port. You should clear your browser's cache before opening the Web Console. For example, if your server is identified on your network as `serverA`, you can access the Web Console by going to `http://serverA:8091/` or `http://<serverA's-IP-address>:8091/`. (If you set up Enterprise Analytics on a port other than `8091`, go to that specified port.) You should clear your browser's cache before attempting to access to the Web Console.

If you're logged into the node itself, you can go to `http://localhost:8091`. You can also use the `couchbase-cli` command to query node to confirm that it's available.

> [!NOTE]
> The Web Console uses the same port as smart clients when communicating with Enterprise Analytics. If you can connect to the Web Console from a particular machine, then administration and database clients on the same machine can also connect to the core cluster port and perform operations. The Web Console provides a warning if the Web browser loses connectivity to the node.

## [](#detailed-verification)Detailed Verification

To verify that clients can connect to the node, you can use [cbworkloadgen](#testing-with-cbworkloadgen).

The `cbworkloadgen` command is a python program that performs basic operations (reads and writes) against the Enterprise Analytics cluster.

Testing With cbworkloadgen

The command `cbworkloadgen` generates random data, then performs reads and writes of this data in Enterprise Analytics. It's not intended to be a performance benchmarking tool.

To test an Enterprise Analytics installation using `cbworkloadgen`, execute the following command, supplying the IP address of the running node:

> cbworkloadgen -n [host]:8091
        Thread 0 - average set time : 0.0257480939229 seconds , min : 0.00325512886047 seconds , max : 0.0705931186676 seconds , operation timeouts 0