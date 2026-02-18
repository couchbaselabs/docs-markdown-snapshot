---
title: Install Couchbase Server Using Docker
description: Couchbase Server can be installed using official Couchbase images
  from Docker Hub.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/getting-started-docker.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/install/getting-started-docker.html)

# Install Couchbase Server Using Docker

> Couchbase Server can be installed using official Couchbase images from Docker Hub. 

If you’re trying Couchbase Server for the first time and just want to explore a Couchbase configuration, the quickest way to install a pre-configured single-node deployment using Docker is to follow the [Get Started](../getting-started/start-here.md) tutorial.

For more traditional Docker deployments, use the following sections below:

* [Deploy a Single-Node Cluster with Containers](#section%5Fjvt%5Fzvj%5F42b)
* [Deploy a Multi-Node Cluster with Containers](#section%5Fmsh%5Ffbl%5F42b)
* [Deploy Multiple Clusters with Containers](#section%5Fdeploy%5Fmultiple%5Fclusters)

If you’re simply looking for the official Couchbase Server Docker image, you can find it on [Docker Hub](https://hub.docker.com/%5F/couchbase/).

## [](#section%5Fjvt%5Fzvj%5F42b)Deploy a Single-Node Cluster with Containers

To run a single-node cluster, you will need to deploy a single container representing the single Couchbase Server node.

> [!NOTE]
> For detailed information about deploying Couchbase Server, make sure to review the Couchbase Server [system requirements](plan-for-production.md) and [deployment guidelines](install-production-deployment.md), paying particular attention to the following pages:
> 
> * [Deployment Considerations for Virtual Machines and Containers](best-practices-vm.md)
> * [Two-Node and Single-Node Clusters](deployment-considerations-lt-3nodes.md).

1. Download and install Docker on the host computer.  
To set up Docker on the host computer, refer to Docker’s [installation instructions](https://www.docker.com/get-started).
2. Install the official Couchbase Server container image.  
```console  
$ docker run -d --name db -p 8091-8097:8091-8097 -p 11210-11211:11210-11211 couchbase/server  
```  
Multiple instances with Docker  
When running multiple instances on the same machine, make use of Docker’s `-p` option to map `external:internal` ports used by the container.  
For example:  
`-p 9091:8091` instructs the container to map the external machine port `9091` to the container application’s port `8091`.  
After running the above command, a single instance (`db`) of the latest [official Couchbase Server container image](https://hub.docker.com/%5F/couchbase/) is downloaded and run on the host computer. If a traditional installation of Couchbase Server is running locally on the host computer, the port mappings specified using the `-p` option may fail. Ensure that you stop any local instance of Couchbase Server before running this command.  
(For instructions on starting up or shutting down a standalone instance of Couchbase server, see [Starting and stopping the Couchbase Server](startup-shutdown.md)).  
You can check the Docker logs to verify that the container has started.  
```console  
$ docker logs db  
```  
If the container has started, the output should start with the following:  
```console  
Starting Couchbase Server -- Web UI available at http://<ip>:8091  
...  
```
3. From a web browser, go to `http://localhost:8091` to access the Couchbase Web Console.  
If the container is up and running, you should see the Couchbase Server setup screen:  
![The Couchbase Server setup screen.](_images/welcome.png)
4. Click **Setup New Cluster** and proceed through the setup wizard to create a cluster of one node.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md) for instructions on using the setup wizard. You may need to lower the RAM allocation for various services to fit within the bounds of the container’s resources.

Now that you have a single-node Couchbase cluster running in containers, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

## [](#section%5Fmsh%5Ffbl%5F42b)Deploy a Multi-Node Cluster with Containers

There are two popular topologies for multi-node container deployments of Couchbase Server:

[All Containers on One Host](#multi-node-cluster-one-host)

This model is commonly used for scale-minimized deployments that simulate production deployments for development and testing purposes.

[Each Container on Its Own Host](#multi-node-cluster-many-hosts)

This model is commonly used for production deployments.

> [!NOTE]
> For detailed information about deploying Couchbase Server, make sure to review the Couchbase Server [system requirements](plan-for-production.md) and [deployment guidelines](install-production-deployment.md), paying particular attention to [Deployment Considerations for Virtual Machines and Containers](best-practices-vm.md).

### [](#multi-node-cluster-one-host)All Containers on One Host

In this cluster deployment model, all node containers are placed on the same physical host computer. When all containers run on a single physical host, it’s important to remember that all containers will compete for the same resources. For this reason, it’s not recommended to use this deployment model for use with applications that are sensitive to performance.

The following procedure explains how to set up a three-node Couchbase cluster with all the containers running on one physical host.

1. Download and install Docker on the host computer.  
To set up Docker on the host computer, refer to Docker’s [installation instructions](https://www.docker.com/get-started).
2. Install three instances of the official Couchbase Server container image.  
Make sure to run each of the following commands:  
```console  
$ docker run -d --name db1 couchbase  
```  
```console  
$ docker run -d --name db2 couchbase  
```  
```console  
$ docker run -d --name db3 -p 8091-8097:8091-8097 -p 11210-11211:11210-11211 couchbase/server  
```  
After running the above commands, three instances (`db1`, `db2`, `db3`) of the latest [official Couchbase Server container image](https://hub.docker.com/%5F/couchbase/) are downloaded and run on the host computer. If a traditional installation of Couchbase Server is running locally on the host computer, the port mappings specified using the `-p` option may fail. Ensure that you stop any local instance of Couchbase Server before running these commands.  
(For instructions on starting up or shutting down a standalone instance of Couchbase server, see [Starting and stopping the Couchbase Server](startup-shutdown.md)).  
> [!NOTE]  
> If you’re using encrypted communication for the Couchbase Web Console, client, and server, and using XDCR, you need to open up additional ports. For details, refer to [Couchbase Server Ports](install-ports.md).  
You can check the Docker logs to verify that each container has started:  
```console  
$ docker logs db1  
```  
If the container has started, the output should start with the following:  
```console  
Starting Couchbase Server -- Web UI available at http://<ip>:8091  
...  
```
3. Discover the local IP addresses of `db1` and `db2`.  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' db1  
```  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' db2  
```  
If the above commands return an empty result, then run the following commands to discover the local IP addresses:  
```console  
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db1  
```  
```console  
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db2  
```  
You’ll need these IP addresses later to add `db1` and `db2` into the cluster. (The initial cluster setup will be run from `db3`, so there is no need for its IP address.)
4. From a web browser, go to `http://localhost:8091` to access the Couchbase Web Console.  
If `db3` is up and running, you should see the Couchbase Server setup screen:  
![The Couchbase Server setup screen.](_images/welcome.png)
5. Click **Setup New Cluster** and proceed through the setup wizard as normal.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md) for instructions on using the setup wizard. You may need to lower the RAM allocation for various services to fit within the bounds of the container’s resources.
6. After the cluster is initialized on the first Couchbase Server node (`db3`), the next step is to add the Couchbase Server nodes from `db1` and `db2` to the cluster.

  1. In the Couchbase Web Console, go to the **Servers** tab and click **ADD SERVER**. This opens the **Add Server Node** dialog.  
  In the **Hostname/IP Address** field, enter the IP address that you previously captured for `db1`. Click **Add Server** to add the node to the cluster configuration.  
  ![The 'Add Server Node' dialog showing an IP address having been entered.](_images/cluster-setup-add-server-db1.png)
  2. After `db1` is successfully added to the cluster configuration, repeat the previous step using the IP address that you captured for `db2`.
  3. Once `db1` and `db2` have successfully been added to the cluster configuration, click **Rebalance** to make the new nodes active in the cluster.  
  ![The 'Servers' tab showing three nodes in the process of rebalancing.](_images/docker-single-machine-db123.png)

Now that you have a multi-node Couchbase cluster running in containers on a single host, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

### [](#multi-node-cluster-many-hosts)Each Container on Its Own Host

In this cluster deployment model, each node container is placed on its own physical host computer. This is the supported model for Couchbase Server container deployments in production.

The following procedure explains how to set up a three-node Couchbase cluster with each container running on its own physical host. Note that all physical hosts must be able to discover one another on the same network and be able to communicate over the [required ports](install-ports.md).

1. Download and install Docker on each host computer.  
To set up Docker on each host computer, refer to Docker’s [installation instructions](https://www.docker.com/get-started).
2. On each of the three physical hosts, install the official Couchbase Server container image.  
```console  
$ docker run -d --name db -v ~/couchbase:/opt/couchbase/var --net=host couchbase  
```  
After running the above command, a single instance (`db`) of the latest [official Couchbase Server container image](https://hub.docker.com/%5F/couchbase/) is downloaded and run on the host computer. The `-v` option is recommended for better I/O performance and persists the data stored by Couchbase on the local host. The `--net=host` option provides better network performance and maps the host network stack to the container.  
You can check the Docker logs to verify that the container has started.  
```console  
$ docker logs db  
```  
If the container has started, the output should start with the following:  
```console  
Starting Couchbase Server -- Web UI available at http://<ip>:8091  
...  
```
3. On each physical host, discover the local IP address for the Couchbase Server container.  
```console  
docker inspect --format '{{ .NetworkSettings.IPAddress }}' db  
```  
You’ll need these IP addresses later to add each node into the cluster.
4. On one of the physical hosts, open a web browser and go to `http://localhost:8091` or `http://<node-ip>:8091` to access the Couchbase Web Console.  
If the Couchbase Server container is up and running, you should see the Couchbase Server setup screen:  
![The Couchbase Server setup screen.](_images/welcome.png)
5. Click **Setup New Cluster** and proceed through the setup wizard as normal.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md) for instructions on using the setup wizard.
6. After the cluster is initialized on the first host, the next step is to incorporate the other Couchbase Server nodes running on the other hosts.

  1. In the Couchbase Web Console on the host you just initialized, go to the **Servers** tab and click **ADD SERVER**. This opens the **Add Server Node** dialog.  
  In the **Hostname/IP Address** field, enter the IP address of one of the other nodes that you captured previously. Click **Add Server** to add the node to the cluster configuration.  
  ![The 'Add Server Node' dialog showing an IP address having been entered.](_images/cluster-setup-add-server-db1.png)
  2. Once the second node has been successfully added to the cluster configuration, repeat the previous step using the IP address of the third and final node.
  3. Once all three nodes have been successfully added to the cluster configuration, click **Rebalance** to make the new nodes active in the cluster.  
  ![The 'Servers' tab showing three nodes in the process of rebalancing.](_images/docker-single-machine-db123.png)

Now that you have a multi-node Couchbase cluster running in containers across multiple physical hosts, you can move on to [Next Steps](#section%5Fpfz%5Fp1r%5F42b).

## [](#section%5Fdeploy%5Fmultiple%5Fclusters)Deploy Multiple Clusters with Containers

In this cluster deployment model, each cluster, running one or more nodes, is run in a separate container. All the containers run on a single physical host. When all containers run on a single physical host, it’s important to remember that all containers will compete for the same resources. For this reason, it’s not recommended to use this deployment model for use with applications that are sensitive to performance.

The following procedure explains how to set up two clusters, each in a separate container, all running on one physical host.

1. Download and install Docker on the host computer.  
To set up Docker on the host computer, refer to Docker’s [installation instructions](https://www.docker.com/get-started).
2. Install two instances of the official Couchbase Server container image.  
Make sure to run each of the following commands:  
```console  
$ docker run -d --name db1 -p 8091-8097:8091-8097 -p 11210-11211:11210-11211 couchbase/server  
```  
```console  
$ docker run -d --name db2 -p 9091-9097:8091-8097 -p 21210-21211:11210-11211 couchbase/server  
```  
After running the above commands, two instances (`db1` and `db2`) of the latest [official Couchbase Server container image](https://hub.docker.com/%5F/couchbase/) are downloaded and run on the host computer. If a traditional installation of Couchbase Server is running locally on the host computer, the port mappings specified using the `-p` option may fail. Ensure that you stop any local instance of Couchbase Server before running these commands.  
(For instructions on starting up or shutting down a standalone instance of Couchbase server, see [Starting and stopping the Couchbase Server](startup-shutdown.md)).  
> [!NOTE]  
> If you’re using encrypted communication for the Couchbase Web Console, client, and server, and using XDCR, you need to open up additional ports. For details, refer to [Couchbase Server Ports](install-ports.md).
3. You can check the Docker logs to verify that each container has started:  
```console  
$ docker logs db1  
```  
```console  
$ docker logs db2  
```  
If the containers have started successfully, then each one will return the following output:  
```console  
Starting Couchbase Server -- Web UI available at http://<ip>:8091  
...  
```
4. Discover the local IP addresses of `db1` and `db2`.  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' db1  
```  
```console  
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' db2  
```  
Note down the IP addresses as these will be needed for configuring the server nodes.  
Each instance is a Couchbase cluster, so you will need to access the UI for each cluster to add a server node.  
__Table 1\. Accessing the server UI__
| Instance | Address                 |
| -------- | ----------------------- |
| db1      | <http://localhost:8091> |
| db2      | <http://localhost:9091> |  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md) for instructions on using the setup wizard. You may need to lower the RAM allocation for various services to fit within the bounds of the container’s resources.

## [](#section%5Fpfz%5Fp1r%5F42b)Next Steps

Once you’ve successfully initialized a Couchbase cluster running in containers, you can start installing and querying [sample buckets](../manage/manage-settings/install-sample-buckets.md), as well as begin connecting clients.

* [Run Your First SQL++ Query](../getting-started/try-a-query.md)  
If you would like to practice querying on a new Couchbase cluster, log into the Couchbase Web Console at `http://localhost:8091` and go to the **Query** tab. If you don’t have any buckets set up yet, you can go to the **Buckets** tab and click **sample bucket** to load some sample data.
* Connect via SDK  
The SDKs communicate with Couchbase Server services over various ports using the name that is used to register each node in the **Servers** tab. Given that each node is registered using the IP address of the hosts, applications using the SDK can be run from any host that can reach the nodes of the cluster.  
For single-node clusters, simply run your application through the Couchbase Server SDK on the host and point it to `http://localhost:8091/pools` to connect to the container.  
For more information about deploying a sample application, refer to the [SDK documentation](../../../java-sdk/current/hello-world/sample-application.md).