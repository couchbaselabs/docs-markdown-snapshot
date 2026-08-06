---
title: Deploy Sync Gateway with Docker
description: Deploy <em>Sync Gateway</em> using Docker; securely sync enterprise
  data from cloud to edge.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/start-here/pages/get-started-install-docker.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:start-here:get-started-install-docker.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/start-here/get-started-install-docker.html)

# Deploy Sync Gateway with Docker

> Deploy _Sync Gateway_ using Docker; securely sync enterprise data from cloud to edge.  
> This is an alternative to the **Install** and **Configure** steps in the _Start Here!_ topic group. It deploys _{sgw}_ and _{cbs}_ using Docker containers.

> [!NOTE]
> Preparatory Steps
> 
> Make sure you have read and acted-upon the information in [Prepare](get-started-prepare.md) before proceeding.

Steps in Getting Started

[Introduction](../introduction.md)| [Prepare](get-started-prepare.md)| [Install](get-started-install.md)| [Configure](get-started-configure.md)

## [](#before-you-begin)Before You Begin

Make sure you have:

* Docker installed on your machine. See the [Docker installation guide](https://docs.docker.com/get-docker/) for instructions.
* The bucket name and RBAC credentials from [Prepare](get-started-prepare.md).

## [](#deploy-couchbase-server)Deploy Couchbase Server

### [](#create-a-docker-network)Create a Docker Network

Create a Docker bridge network so that _Couchbase Server_ and _Sync Gateway_ containers can communicate.

```bash
docker network create --driver bridge couchbase
```

### [](#run-couchbase-server)Run Couchbase Server

Run Couchbase Server in a Docker container on the `couchbase` network.

```bash
docker run -d --name cb-server \
  --network couchbase \
  -p 8091-8097:8091-8097 \
  -p 11210-11211:11210-11211 \
  couchbase/server
```

### [](#configure-couchbase-server)Configure Couchbase Server

Once Couchbase Server is running, open the Admin UI at `http://localhost:8091` and complete the setup described in [Prepare](get-started-prepare.md), including:

* Creating a cluster
* Creating a bucket
* Creating an RBAC user for Sync Gateway

> [!NOTE]
> Note the bucket name and RBAC credentials. You will need them in the next step.

## [](#deploy-sync-gateway)Deploy Sync Gateway

### [](#create-a-configuration-file)Create a Configuration File

Create a configuration file named `sync-gateway-config.json` on your local machine.

Replace `<rbac-username>` and `<rbac-password>` with the credentials you set up in Couchbase Server.

Example 1\. Sync Gateway Bootstrap Config for Docker

```json
{
  "bootstrap": {
    "server": "couchbase://cb-server", (1)
    "username": "<rbac-username>", (2)
    "password": "<rbac-password>",
    "use_tls_server": false (3)
  },
  "logging": {
    "console": {
      "enabled": true,
      "log_level": "info",
      "log_keys": ["*"]
    }
  }
}
```

| **1** | Use the Couchbase Server container name cb-server as the hostname. Docker resolves this name within the couchbase network. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | Use the RBAC credentials you created when you configured Couchbase Server.                                                 |
| **3** | TLS is disabled for local development. For production deployments, enable TLS and use couchbases://cb-server instead.      |

### [](#run-sync-gateway)Run Sync Gateway

Run Sync Gateway in a Docker container, mounting the configuration file you created.

Replace `/path/to/sync-gateway-config.json` with the absolute path to the file on your local machine.

```bash
docker run -d --name sync-gateway \
  --network couchbase \
  -p 4984-4985:4984-4985 \
  -v /path/to/sync-gateway-config.json:/etc/sync_gateway/config.json \
  couchbase/sync-gateway \
  /etc/sync_gateway/config.json
```

> [!NOTE]
> Port 4985 is the Sync Gateway Admin port. By default it is only accessible from within the container. Do not expose port 4985 to external traffic in production environments.

## [](#verify-the-connection)Verify the Connection

1. Point your browser to the Sync Gateway public port:  
```bash  
http://localhost:4984  
```
2. Confirm that you receive a response similar to this:  
```bash  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"4.1"},"version":"Couchbase Sync Gateway/4.1.0 EE"}  
```  
If there are issues, select the [Console Logs](../manage/logging.md#lbl-console-logs) for more information.

## [](#manage-your-containers)Manage Your Containers

### [](#stop-containers)Stop Containers

```bash
docker stop sync-gateway
docker stop cb-server
```

### [](#start-containers)Start Containers

Start Couchbase Server before Sync Gateway.

```bash
docker start cb-server
docker start sync-gateway
```

> [!NOTE]
> If Couchbase Server is stopped for an extended period, Sync Gateway loses the connection. Restart Sync Gateway after restarting Couchbase Server.

### [](#update-the-sync-gateway-configuration)Update the Sync Gateway Configuration

To update the Sync Gateway configuration, stop and remove the container, then re-run it with the updated configuration file.

```bash
docker stop sync-gateway
docker rm sync-gateway
```

Then repeat [Run Sync Gateway](#run-sync-gateway).

## [](#next-steps)Next Steps

Now that you have Sync Gateway running in Docker, continue to [Explore](get-started-explore.md) to add a database configuration, create users, and run a CRUD cycle to confirm sync is working end-to-end.

From there, you can explore more complex scenarios:

* Learn more about Sync Gateway's [Bootstrap Configuration](../configuration/configuration-schema-bootstrap.md)
* Learn how to [Sync with Couchbase Server](../sync/sync-with-couchbase-server.md)
* Implement access controls — see: [Users](../access-control/users.md), [Roles](../access-control/roles.md), and the [Sync Function](../access-control/sync-function/sync-function.md)

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