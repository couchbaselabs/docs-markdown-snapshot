---
title: Configure a Sync Gateway Install
description: Configure your <em>Sync Gateway</em> installation; securely sync
  enterprise data from cloud to edge!
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/start-here/pages/get-started-configure.adoc
pubDate: 2026-04-09T05:16:09.658Z
link: xref:sync-gateway:start-here:get-started-configure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/start-here/get-started-configure.html)

# Configure a Sync Gateway Install

> Configure your _Sync Gateway_ installation; securely sync enterprise data from cloud to edge!  
> This is **Step 3** in the _Start Here!_ topic group. Here you'll configure _sync gateway_ to connect to a _Couchbase Server_ instance and verify that the connection is working.

> [!NOTE]
> Preparatory Steps
> 
> Make sure you have read and acted-upon the information and steps in [Prepare](get-started-prepare.md) and [Install](get-started-install.md) before proceeding.

These instructions are for local or server based deployments. If you're using a container such as Docker, see this [blog post on using Docker with Couchbase Mobile](https://blog.couchbase.com/using-docker-with-couchbase-mobile/) for additional details.

Steps in Getting Started

[Introduction](../introduction.md)| [Prepare](get-started-prepare.md)| [Install](get-started-install.md)| [Configure](get-started-configure.md)

## [](#introduction)Introduction

In this step of the Getting Started topic we will configure your _Sync Gateway_ to connect to a _Couchbase Server_ instance and verify that the connection is working.

You'll need to edit the configuration file used in the [Install](get-started-install.md) step to point to a bucket on your Couchbase Server — see [Bootstrap Sync Gateway](#lbl-config).

On completion of this topic you'll have a working sync gateway instance connected to Couchbase Server. You can then continue to [Explore](get-started-explore.md) to add a database, create users, and run a CRUD cycle.

## [](#lbl-config)Bootstrap Sync Gateway

To configure sync gateway to connect to a Couchbase Server:

1. Make sure your sync gateway service stops/unloads
2. Edit the configuration file you used in [Install](get-started-install.md) and replace the contents with those shown in [Example 1](#sample-cfg).  
The configuration points to your Couchbase Server cluster, which you'll use to verify that you can connect to Couchbase Server through sync gateway.
3. Make sure you start Couchbase Server
4. Restart/Load your sync gateway to pick-up the changed configuration

Example 1\. Simple Sync Gateway Bootstrap Config

```json
{
  "bootstrap": {
    "server": "couchbases://localhost", (1)
    "username": "sync_gateway", (2)
    "password": "password",
    "server_tls_skip_verify": true, (3)
    "use_tls_server": true (4)
  },
  "logging": { (5)
    "console": {
      "enabled": true,
      "log_level": "info",
      "log_keys": ["*"]
    }
  }
}
```

About the Configuration Properties:

| **1** | Here you'll point to the Couchbase Server cluster using secure connection. Server ships with self-signed certs that work out of the box, as long as server\_tls\_skip\_verify is set, as it's below.                                            |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here you'll provide the credentials for the RBAC user that you created on the Couchbase Server Admin Console — see [Configure Server for Sync Gateway](get-started-prepare.md#configure-server)                                                 |
| **3** | Here you'll opt to ignore CA Cert verification of the certificate presented by the server; allowing for example use of self-signed certificate. The connection is unverified but encrypted.                                                     |
| **4** | Optionally, you can choose to run without TLS by setting this value to false. In that case you should also use the plaintext URI couchbase://localhost to connect.                                                                              |
| **5** | Define your logging requirements.Here you'll set general diagnostic console logs on. If you're having issues, for more information, see [Logging](../manage/logging.md) for how to tune diagnostics to provide additional troubleshooting help. |

Start Sync Gateway

Run the following in a terminal:

```bash
bin/sync_gateway -<options> sgwconfig.json (1)
```

| **1** | Optionally provide any CLI flags you require to use. |
| ----- | ---------------------------------------------------- |

## [](#connect-to-sync-gateway)Connect to Sync Gateway

> [!TIP]
> You can use [Console Logs](../manage/logging.md#lbl-console-logs) to aid diagnosis of connection issues.

1. With sync gateway and Couchbase Server started, point your browser to the sync gateway url, typically on port 4984, but this can be changed — see: [REST API Access](../rest-api/rest-api-access.md).  
So, for example:  
```bash  
http://localhost:4984  
```
2. Check that you receive a response similar to this:  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"4.0"},"version":"Couchbase sync gateway/{version-full}(376;e2e7d42) EE"}  
```  
If there are issues, check the [Console Logs](../manage/logging.md#lbl-console-logs) for more information. Where necessary you can redirect console output to a file — see: [Redirect Console Logs](../manage/logging.md#lbl-log-redirect).

> [!TIP]
> If sync gateway is behind a load balancer, check the websockets configuration — see [Load Balancer](../deploy/load-balancer.md).

## [](#next-steps)Next Steps

Now that you have a configured sync gateway installation connected to Couchbase Server, continue to [Explore](get-started-explore.md) page, where you'll add a database configuration, create users, and run a CRUD cycle to confirm sync is working end-to-end.

From there, you can explore more complex scenarios with confidence:

* Learn more about sync gateway's [Bootstrap Configuration](../configuration/configuration-schema-bootstrap.md)
* Learn how to [Sync with Couchbase Server](../sync/sync-with-couchbase-server.md)
* Implement access controls — see: [Users](../access-control/users.md), [Roles](../access-control/roles.md), and the [Sync Function](../access-control/sync-function/sync-function.md)
* Implement secure connectivity — see: [User Authentication](../security/authentication-users.md) and [TLS Certificate Authentication](../security/authentication-certs.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](get-started-prepare.md)
* [Install](get-started-install.md)
* [Configure](get-started-configure.md)

###### [](#-3)

Product Information

* [Release Notes](../product-notes/release-notes.md)
* [Compatibility Matrix](../product-notes/compatibility.md)
* [Supported OS](../product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)