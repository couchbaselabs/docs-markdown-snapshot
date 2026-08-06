---
title: Install Enterprise Analytics Using Docker
description: Enterprise Analytics can be installed using Couchbase-provided
  images from Docker Hub.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/install/pages/getting-started-docker.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:install:getting-started-docker.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/install/getting-started-docker.html)

# Install Enterprise Analytics Using Docker

> Enterprise Analytics can be installed using Couchbase-provided images from Docker Hub. 

If you're trying Enterprise Analytics for the first time and want to explore a Couchbase configuration, follow the [Get Started](../intro/do-a-quick-install.md#install-enterprise-analytics-using-docker) tutorial.

You can install a pre-configured single-node deployment using Docker.

For more traditional Docker deployments:

* [Deploy a Single-Node Cluster with Containers](#section%5Fjvt%5Fzvj%5F42b)
* [Deploy a Multi-Node Cluster with Containers](#section%5Fmsh%5Ffbl%5F42b)
* [Deploy Multiple Clusters with Containers](#section%5Fdeploy%5Fmultiple%5Fclusters)

If you're looking for the Enterprise Analytics Docker image, you can find it on [Docker Hub](https://hub.docker.com/r/couchbase/enterprise-analytics).

## [](#section%5Fjvt%5Fzvj%5F42b)Deploy a Single-Node Cluster with Containers

To run a single-node cluster, deploy a single container for a single Enterprise Analytics node.

> [!NOTE]
> For detailed information about deploying Enterprise Analytics, make sure to review the Enterprise Analytics [system requirements](system-requirements.md) and [deployment guidelines](deploy-guidelines.md), paying particular attention to the following pages:
> 
> * [Deployment Considerations for Virtual Machines and Containers](vm-container-guidelines.md)
> * [Two-Node and Single-Node Clusters](single-two-node-clusters.md).

1. Download and install Docker on the host computer.  
To set up Docker on the host computer, see Docker's [installation instructions](https://www.docker.com/get-started).
2. Install the official Enterprise Analytics container image.  
```console  
$ docker run -d --name ea -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 -p 11207:11207 -p 11210:11210 couchbase/enterprise-analytics  
```  
Multiple instances with Docker  
When running multiple instances on the same machine, make use of Docker's `-p` option to map `external:internal` ports used by the container.  
For example:  
`-p 9091:8091` instructs the container to map the external machine port `9091` to the container application's port `8091`.  
After you run the above command, Docker downloads and runs a single instance (`ea`) of the latest [official Enterprise Analytics container image](https://hub.docker.com/r/couchbase/enterprise-analytics) on your host computer. If a traditional installation of Enterprise Analytics is running locally on the host computer, the port mappings specified using the `-p` option might fail. Make sure that you stop any local instance of Enterprise Analytics before running this command.  
For instructions on starting or stopping Enterprise Analytics, see [Start and Stop Enterprise Analytics](start-stop-cb-enterprise-analytics.md).  
You can check the Docker logs to verify that the container has started.  
```console  
$ docker logs ea  
```  
If the container has started, the output should start with the following:  
```console  
Starting Enterprise Analytics -- Web UI available at http://<ip>:8091  
...  
```
3. From a web browser, go to `http://localhost:8091`.
4. Click **Setup New Cluster** and proceed through the setup wizard to create a cluster of 1 node.  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).

Now that you have a single-node Couchbase cluster running in containers, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

## [](#section%5Fmsh%5Ffbl%5F42b)Deploy a Multi-Node Cluster with Containers

You can use the following models for multi-node container deployments of Enterprise Analytics:

[All Containers on One Host](#multi-node-cluster-one-host)

This model is commonly used for scale-minimized deployments that simulate production deployments for development and testing purposes.

[Each Container on Its Own Host](#multi-node-cluster-many-hosts)

This model is commonly used for production deployments.

> [!NOTE]
> For detailed information about deploying Enterprise Analytics, make sure to review the Enterprise Analytics [system requirements](system-requirements.md) and [deployment guidelines](deploy-guidelines.md).

### [](#multi-node-cluster-one-host)All Containers on One Host

In this cluster deployment model, all node containers are placed on the same physical host computer. Running multiple containers on a single physical host causes your containers to compete for the same resources. Couchbase does not recommended using this deployment model for applications that are sensitive to performance.

To set up a 3-node Couchbase cluster with all the containers running on 1 physical host:

1. Download and install Docker on the host computer.  
To set up Docker on the host computer, see Docker's [installation instructions](https://www.docker.com/get-started).
2. Install 3 instances of the official Enterprise Analytics container image.  
Make sure to run each of the following commands:  
```console  
$ docker run -d --name ea1 couchbase/enterprise-analytics  
```  
```console  
$ docker run -d --name ea2 couchbase/enterprise-analytics  
```  
```console  
$ docker run -d --name ea3 -p 8091-8096:8091-8096 -p 11210-11211:11210-11211 couchbase/enterprise-analytics  
```  
After you run the above commands, Docker downloads and runs 3 instances (`ea1`, `ea2`, `ea3`) of the latest [official Enterprise Analytics container image](https://hub.docker.com/%5F/couchbase/) on your host computer. If a traditional installation of Enterprise Analytics is running locally on the host computer, the port mappings specified using the `-p` option might fail. Make sure that you stop any local instance of Enterprise Analytics before running these commands.  
\+ For instructions on starting or stopping Enterprise Analytics, see [Start and Stop Enterprise Analytics](start-stop-cb-enterprise-analytics.md).  
You can check the Docker logs to verify that each container has started:  
```console  
$ docker logs ea1  
```  
If the container has started, the output should start with the following:  
```console  
Starting Enterprise Analytics -- Web UI available at http://<ip>:8091  
...  
```
3. Discover the local IP addresses of `ea1` and `ea2`.  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' ea1  
```  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' ea2  
```  
If the earlier commands return an empty result, then run the following commands to discover the local IP addresses:  
```console  
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ea1  
```  
```console  
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ea2  
```  
You'll need these IP addresses later to add `ea1` and `ea2` into the cluster and since you'll run the initial cluster setup from `ea3`, there is no need for its IP address.
4. From a web browser, go to `http://localhost:8091`.
5. Click **Setup New Cluster** and set up a new cluster.  
For more information about creating a new cluster, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
6. After the cluster is initialized on the first Enterprise Analytics node (`ea3`), the next step is to add the Enterprise Analytics nodes from `ea1` and `ea2` to the cluster.

  1. In the Web Console, go to the **Enterprise Analytics** tab and click **Add Node**.  
  In the **Hostname/IP Address** field, enter the IP address for `ea1`. Click **Add Node** to add the node to the cluster configuration.
  2. After you have added `ea1` to the cluster configuration, repeat the previous step using the IP address for `ea2`.
  3. After you have added `ea1` and `ea2` to the cluster configuration, click **Rebalance** to make the new nodes active in the cluster.

Now that you have a multi-node Couchbase cluster running in containers on a single host, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

### [](#multi-node-cluster-many-hosts)Each Container on Its Own Host

In this cluster deployment model, each node container is placed on its own physical host computer. This is the supported model for Enterprise Analytics container deployments in production.

The following procedure explains how to set up a 3-node Couchbase cluster with each container running on its own physical host. All physical hosts must be able to discover each another on the same network and be able to communicate via the [required ports](cb-enterprise-analytics-ports.md).

1. Download and install Docker on each host computer.  
To set up Docker on each host computer, see Docker's [installation instructions](https://www.docker.com/get-started).
2. On each of the 3 physical hosts, install the official Enterprise Analytics container image.  
```console  
$ docker run -d --name ea -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 -p 11207:11207 -p 11210:11210 couchbase/enterprise-analytics  
```  
After you run the above command, Docker downloads and runs a single instance (`ea`) of the latest [official Enterprise Analytics container image](https://hub.docker.com/r/couchbase/enterprise-analytics) on your host computer. Couchbase recommends the `-v` option for better I/O performance and persists the data stored by Couchbase on the local host. The `--net=host` option provides better network performance and maps the host network stack to the container.  
You can check the Docker logs to verify that the container has started.  
```console  
$ docker logs ea  
```  
If the container has started, the output should start with the following:  
```console  
Starting Enterprise Analytics -- Web UI available at http://<ip>:8091  
...  
```
3. On each physical host, discover the local IP address for the Enterprise Analytics container.  
```console  
docker inspect --format '{{ .NetworkSettings.IPAddress }}' ea  
```  
You'll need these IP addresses later to add each node into the cluster.
4. On 1 of the physical hosts, open a web browser and go to `http://localhost:8091` or `http://<node-ip>:8091` to access the Enterprise Analytics Web Console.
5. Click **Setup New Cluster** and proceed through the setup wizard as normal.  
For more information about how to create a new cluster, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
6. After the cluster is initialized on the first host, the next step is to incorporate the other Enterprise Analytics nodes running on the other hosts.

  1. In the Web Console on the host you just initialized, go to the **Enterprise Analytics** tab and click **Add Node**.  
  In the **Hostname/IP Address** field, enter the IP address of one of the other nodes. Click **Save** to add the node to the cluster configuration.
  2. Once you have added the second node to the cluster configuration, repeat the previous step using the IP address of the third and final node.
  3. Once all 3 nodes have been added to the cluster configuration, click **Rebalance** to make the new nodes active in the cluster.

Now that you have a multi-node Couchbase cluster running in containers across multiple physical hosts, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

## [](#section%5Fdeploy%5Fmultiple%5Fclusters)Deploy Multiple Clusters with Containers

In this cluster deployment model, each cluster, running 1 or more nodes, is run in a separate container. All the containers run on a single physical host. Running multiple containers on a single physical host causes your containers to compete for the same resources. Couchbase does not recommended using this deployment model for applications that are sensitive to performance.

The following procedure explains how to set up 2 clusters, each in a separate container, all running on 1 physical host.

1. Download and install Docker on the host computer.  
To set up Docker on the host computer,see Docker's [installation instructions](https://www.docker.com/get-started).
2. Install 2 instances of the official Enterprise Analytics container image.  
Make sure to run each of the following commands:  
```console  
$ docker run -d --name ea -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 -p 11207:11207 -p 11210:11210 couchbase/enterprise-analytics  
```  
```console  
$ docker run -d --name ea -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 -p 11207:11207 -p 11210:11210 couchbase/enterprise-analytics  
```  
After you run the above command, Docker downloads and runs a 2 instances (`ea1` and `ea2`) of the latest [official Enterprise Analytics container image](https://hub.docker.com/r/couchbase/enterprise-analytics) on your host computer. If a traditional installation of Enterprise Analytics is running locally on the host computer, the port mappings specified using the `-p` option may fail. Make sure that you stop any local instance of Enterprise Analytics before running these commands.  
For instructions on starting or stopping Enterprise Analytics, see [Start and Stop Enterprise Analytics](start-stop-cb-enterprise-analytics.md).
3. You can check the Docker logs to verify that each container has started:  
```console  
$ docker logs ea1  
```  
```console  
$ docker logs ea2  
```  
If the containers have started, then each of them returns the following output:  
```console  
Starting Enterprise Analytics -- Web UI available at http://<ip>:8091  
...  
```
4. Discover the local IP addresses of `ea1` and `ea2`.  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' ea1  
```  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' ea2  
```  
Note the IP addresses as you need them for configuring the server nodes.  
Each instance is a Couchbase cluster, so you need to access the UI for each cluster to add a server node.  
__Table 1\. Accessing the server UI__
| Instance | Address                 |
| -------- | ----------------------- |
| ea1      | <http://localhost:8091> |
| ea2      | <http://localhost:9091> |  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).

## [](#configuring-cloud-credentials-in-the-docker-container)Configuring Cloud Credentials in the Docker Container

Enterprise Analytics may require access to AWS resources. Since the container runs as the Couchbase user, credentials should be accessible under `/home/couchbase`.

The standard container run command is

```console
$ docker run -d --name ea \
    -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 \
    -p 11207:11207 -p 11210:11210 \
    couchbase/enterprise-analytics
```

You can supply AWS credentials securely and effectively, using 1 of the following runtime options:

* Mount Local AWS Credentials

Bind-mount your local AWS credentials directory:

```console
$ docker run -d --name ea \
    -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 \
    -p 11207:11207 -p 11210:11210 \
    -v ~/.aws:/home/couchbase/.aws \
    couchbase/enterprise-analytics
```

This allows the AWS SDK to read from:

/home/couchbase/.aws/credentials
/home/couchbase/.aws/config

> [!NOTE]
> Couchbase recommends this option for local development.\\ Do not use for production unless credentials are isolated and access-controlled.

* Copy Credentials File into a Running Container

If the container is already running:

```console
$ docker cp ~/.aws ea:/home/couchbase/.aws
$ docker exec ea chown -R couchbase:couchbase /home/couchbase/.aws
```

Caution:You'll lose the credentials if you remove or restart the container.

* Pass Credentials via Environment Variables

Pass AWS credentials directly:

```console
$ docker run -d --name ea \
    -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 \
    -p 11207:11207 -p 11210:11210 \
    -e AWS_ACCESS_KEY_ID=your-access-key \
    -e AWS_SECRET_ACCESS_KEY=your-secret-key \
    -e AWS_SESSION_TOKEN=your-session-token \
    couchbase/enterprise-analytics
```

> [!NOTE]
> Couchbase recommends this option for local development.\\ Do not use for production unless credentials are isolated and access-controlled.

Caution:The values may be visible via Docker inspect or logs.

## [](#section%5Fpfz%5Fp1r%5F42b)Next Steps

* Connect via SDK  
The SDKs communicate with Enterprise Analytics over various ports using the name you used to register each node in the **Servers** tab. Given that you register each node using the IP address of the hosts, you can run the applications using the SDK from any host that can reach the nodes of the cluster.  
For single-node clusters, run your application through the Enterprise Analytics SDK on the host and point it to `http://localhost:8091/pools` to connect to the container.