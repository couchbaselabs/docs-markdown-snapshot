---
title: Install
editUrl: https://github.com/couchbaselabs/mobile-training-todo/edit/tutorials/content/modules/todo-app/pages/deploy/install.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:tutorials:todo-app:deploy/install.adoc[]
---

[View original HTML](/tutorials/todo-app/deploy/install.html)

# Install

In this lesson you’ll learn how to install Sync Gateway and Couchbase Server, our NoSQL database server.

## [](#requirements)Requirements

Three instances with the following:

* Centos 7
* RAM >= 2GB

## [](#getting-started)Getting Started

This lesson contains some scripts to automatically deploy and configure Sync Gateway with Couchbase Server. Download those scripts on each VM using wget.

```bash
ssh vagrant@192.168.34.11
wget https://cl.ly/1q300A3v3R1D/deploy.zip
sudo yum install -y unzip
unzip deploy.zip
```

Throughout this lesson, you will use different scripts located in the **deploy** folder.

## [](#architecture)Architecture

The server-side architecture will be comprised of 2 nodes of Sync Gateway and 1 node of Couchbase Server. Each node will run on a different VM. The diagram below describes the architecture:

* Couchbase Server is running VM1
* Sync Gateway is running on VM2 and VM3

![image74](img/image74.png) 

## [](#install-couchbase-server)Install Couchbase Server

To deploy Couchbase Mobile to production you must first get familiar with Couchbase Server. It can deployed on a whole host of [operating systems](http://www.couchbase.com/nosql-databases/downloads) and can scale horizontally with multiple nodes or vertically by increasing the VM specs. The following script downloads Couchbase Server and creates a new bucket called todo.

### [](#try-it-out)Try it out

1. Log on VM1 (couchbase-server).
2. `cd deploy`
3. Run the **install\_couchbase\_server.sh** script.  
```bash  
sudo ./install_couchbase_server.sh  
```
4. Log on the Couchbase Server Admin Console on <http://VM1%5FIP:8091> with the user credentials that were created above (**Administrator/password**).

## [](#install-sync-gateway)Install Sync Gateway

Sync Gateway is the middleman server that exposes a database API for Couchbase Lite databases to replicate to and from. It connects internally to a Couchbase Server bucket to persist the documents.

In production, the configuration file should look similar to the one used in development except that instead of using **walrus:** for the bucket it will connect to an instance of Couchbase Server URL as shown below.

```javascript
{
  "interface":":4984",
  "log": ["HTTP", "Auth"],
  "databases": {
    "todo": {
      "server": "http://localhost:8091",
      "bucket": "todo",
      ...
    }
  }
}
```

The `install_sync_gateway.sh` script downloads and installs Sync Gateway 1.3\. Then it restarts the `sync_gateway` service with the configuration file (`deploy/sync-gateway-config.json`) of the todo application.

### [](#%5Ftry%5Fit%5Fout%5F1)Try it out

1. Log on VM2 (sync-gateway).
2. `cd deploy`
3. Run the Sync Gateway install script passing the IP of VM1 where Couchbase Server is running.  
```bash  
sudo ./install_sync_gateway.sh VM1  
```
4. Monitor the log file.  
```bash  
sudo tail -f /home/sync_gateway/logs/sync_gateway_error.log  
```
5. Send an `/{db}/_all_docs` request with a user’s credentials. A user (**user1/pass**) is already defined in the Sync Gateway configuration file.  
```bash  
curl -X GET 'http://user1:pass@localhost:4984/todo/_all_docs'  
```

![image75](https://cl.ly/1j1q3p333D47/image75.gif) 

1. Repeat the same steps on VM3 (sync-gateway).

## [](#using-a-reverse-proxy)Using a reverse proxy

With two Sync Gateway nodes you can now configure the reverse proxy and update the sync endpoint in the mobile app to start replications pointing to the reverse proxy instead of an individual Sync Gateway instance. In this example the NGINX instance will run on VM4.

### [](#%5Ftry%5Fit%5Fout%5F2)Try it out

1. Log on VM4 (nginx).
2. `cd deploy`
3. Run the NGINX install script passing the IP of VM2 and VM3 where the Sync Gateway instances are running.  
```bash  
sudo ./configure_nginx.sh VM2 VM3  
```
4. Send an `/{db}/_all_docs` request with a user’s credentials to the NGINX port. A user (**user1/pass**) is already defined in the Sync Gateway configuration file.  
```bash  
curl -X GET 'http://user1:pass@localhost:8000/todo/_all_docs'  
```

![image76](https://cl.ly/392N2E2K0J0T/image76.gif) 

### [](#docker-cloud)Docker Cloud

In this lesson you’ll learn how to deploy Couchbase Server and Sync Gateway on Docker Cloud behind a load balancer.

#### [](#launch-node-cluster)Launch node cluster

Launch a node cluster with the following settings:

* Provider: AWS
* Region: us-east-1 (or whatever region makes sense for you)
* VPC: Auto (if you don’t choose auto, you will need to customize your security group)
* Type/Size: m3.medium or greater
* IAM Roles: None

![docker cloud launch nodecluster](img/docker_cloud_launch_nodecluster.png) 

#### [](#create-couchbase-server-service)Create Couchbase Server service

Go to **Services** and hit the **Create** button:

![docker cloud service create](img/docker_cloud_service_create.png) 

Click the globe icon and **Search Docker Hub** for `couchbase/server`. You should select the `couchbase/server` image:

![docker cloud create cbs service](img/docker_cloud_create_cbs_service.png) 

Hit the **Select** button and fill out the following values on the Services Wizard:

* Service Name: couchbaseserver
* Containers: 2
* Deployment strategy: High Availability
* Autorestart: On failure
* Network: bridge

![docker cloud create cbs service2](img/docker_cloud_create_cbs_service2.png) 

In the Ports section: Enable **published** on each port and set the Node Port to match the Container Port

![docker cloud create cbs service3](img/docker_cloud_create_cbs_service3.png) 

Hit the **Create and Deploy** button. After a few minutes, you should see the Couchbase Server vervice running:

![docker cloud couchbase server running](img/docker_cloud_couchbase_server_running.png) 

#### [](#configure-couchbase-server-container-1-createbuckets)Configure Couchbase Server Container 1 + CreateBuckets

Go to the **Container** section and choose **couchbaseserver-1**.

![docker cloud couchbase container1](img/docker_cloud_couchbase_container1.png) 

Copy and paste the domain name (`eca0fe88-7fee-446b-b006-99e8cae0dabf.node.dockerapp.io`) into your browser, adding 8091 at the end (`eca0fe88-7fee-446b-b006-99e8cae0dabf.node.dockerapp.io:8091`)

You should now see the Couchbase Server setup screen:

![docker cloud couchbase setup](img/docker_cloud_couchbase_setup.png) 

You will need to find the _container IP_ of Couchbase Server in order to configure it. To do that, go to the **Terminal** section of **Containers/couchbaseserver-1**, and enter `ifconfig`.

![docker cloud couchbase container terminal](img/docker_cloud_couchbase_container_terminal.png) 

Look for the `ethwe1` interface and make a note of the ip: `10.7.0.2` — you will need it in the next step.

Switch back to the browser on the Couchbase Server setup screen. Leave the **Start a new cluster** button checked. Enter the `10.7.0.2` ip address (or whatever was returned for your `ethwe1` interface) under the **Hostname** field.

![docker cloud couchbase server hostname](img/docker_cloud_couchbase_server_hostname.png) 

and hit the **Next** button.

For the rest of the wizard, you can:

* skip adding the samples
* skip adding the default bucket
* uncheck **Update Notifications**
* leave Product Registration fields blank
* check I agree ..
* make sure to write down your password somewhere, otherwise you will be locked out of the web interface

Create a new bucket for your application:

![docker cloud create bucket](img/docker_cloud_create_bucket.png) 

#### [](#configure-couchbase-server-container-2)Configure Couchbase Server Container 2

Go to the **Container** section and choose **couchbaseserver-2**.

As in the previous step, copy and paste the domain name (`4d8c7be0-3f47-471b-85df-d2471336af75.node.dockerapp.io`) into your browser, adding 8091 at the end (`4d8c7be0-3f47-471b-85df-d2471336af75.node.dockerapp.io:8091`)

Hit **Setup** and choose **Join a cluster now** with settings:

* IP Address: 10.7.0.2 (the IP address you setup the first Couchbase Server node with)
* Username: Administrator (unless you used a different username in the previous step)
* Password: enter the password you used in the previous step
* Configure Server Hostname: 10.7.0.3 (you can double check this by going to the **Terminal** for **Containers/couchbaseserver-2** and running `ifconfig` and looking for the ip of the `ethwe1` interface)

![docker cloud join couchbase cluster](img/docker_cloud_join_couchbase_cluster.png) 

Trigger a rebalance by hitting the **Rebalance** button:

![docker cloud trigger rebalance](img/docker_cloud_trigger_rebalance.png) 

#### [](#sync-gateway-service)Sync Gateway Service

Now create a Sync Gateway service.

Before going through the steps in the Docker Cloud web UI, you will need to have a Sync Gateway configuration somewhere on the publicly accessible internet.

_Warning: This is not a secure solution! Do not use any sensitive passwords if you follow these steps_

To make it more secure, you could:

* Use a Volume mount and have Sync Gateway read the configuration from the container filesystem
* Use a HTTPS + Basic Auth for the URL that hosts the Sync Gateway configuration

Create a Sync Gateway configuration on a [github gist](https://gist.github.com/tleyden/f260b2d9b2ef828fadfad462f0014aed) and get the [raw url](https://gist.githubusercontent.com/tleyden/f260b2d9b2ef828fadfad462f0014aed/raw/8f544be6b265c0b57848b2ba36fb3e0f958ddcc9/gistfile1.txt) for the gist.

* Make sure to set the `server` value to `<http://couchbaseserver:8091>` so that it can connect to the Couchbase Service setup in a previous step.
* Use the bucket created in the Couchbase Server setup step above

In the Docker Cloud web UI, go to **Services** and hit the **Create** button again.

Click the globe icon and **Search Docker Hub** for `couchbase/sync-gateway`. You should select the `couchbase/sync-gateway` image.

Hit the **Select** button and fill out the following values on the Services Wizard:

* Service Name: sync-gateway
* Containers: 2
* Deployment strategy: High Availability
* Autorestart: On failure
* Network: bridge

![docker cloud sync gateway service](img/docker_cloud_sync_gateway_service.png) 

In the **Container Configuration** section, customize the **Run Command** to use the raw URL of your gist, eg: `<https://gist.githubusercontent.com/tleyden/f260b2d9b2ef828fadfad462f0014aed/raw/8f544be6b265c0b57848>`

![docker cloud configure sg service](img/docker_cloud_configure_sg_service.png) 

In the **Ports** section, use the following values:

![docker cloud configure sg service ports](img/docker_cloud_configure_sg_service_ports.png) 

In the **Links** section, choose **couchbaseserver** and hit the **Plus** button

![docker cloud sg service links](img/docker_cloud_sg_service_links.png) 

Click the **Create and Deploy** button.

#### [](#verify-sync-gateway)Verify Sync Gateway

Click the **Containers** section and you should have two Couchbase Server and two Sync Gateway containers running.

![docker cloud cbs sg containers](img/docker_cloud_cbs_sg_containers.png) 

Click the **sync-gateway-1** container and get the domain name (`eca0fe88-7fee-446b-b006-99e8cae0dabf.node.dockerapp.io`) and paste it in your browser with a trailing `:4984`, eg `eca0fe88-7fee-446b-b006-99e8cae0dabf.node.dockerapp.io:4984`

You should see the following JSON response:

```none
{
   couchdb:Welcome,
   vendor:{
      name:Couchbase Sync Gateway,
      version:1.3
   },
   version:Couchbase Sync Gateway/1.3.1(16;f18e833)
}
```

#### [](#setup-load-balancer)Setup Load Balancer

Click the **Services** section and hit the **Create** button. In the bottom right hand corner look for **Proxies** and choose **dockercloud/haproxy**

![docker cloud create load balancer service1](img/docker_cloud_create_load_balancer_service1.png) 

General Settings:

* Service Name: sgloadbalancer
* Containers: 1
* Deployment Strategy: High Availability
* Autorestart: Always
* Network: Bridge

Ports:

* Port 80 should be **Published** and the **Node Port** should be set to `80`

Links:

* Choose **sync-gateway** and hit the **Plus** button

![docker cloud haproxy ports links](img/docker_cloud_haproxy_ports_links.png) 

Hit the **Create and Deploy** button

#### [](#verify-load-balancer)Verify Load Balancer

Click the **Containers** section and choose **sgloadbalancer-1**.

![docker cloud sgloadbalancer container](img/docker_cloud_sgloadbalancer_container.png) 

Copy and paste the domain name (eg, `eca0fe88-7fee-446b-b006-99e8cae0dabf.node.dockerapp.io`) into your browser.

You should see the following JSON response:

```none
{
   couchdb:Welcome,
   vendor:{
      name:Couchbase Sync Gateway,
      version:1.3
   },
   version:Couchbase Sync Gateway/1.3.1(16;f18e833)
}
```

Congratulations! You have just setup a Couchbase Server + Sync Gateway cluster on Docker Cloud.

#### [](#conclusion)Conclusion

Well done! You’ve completed this lesson on installing Sync Gateway and Couchbase Server. In the next lesson you’ll learn how to perform an upgrade on Sync Gateway. Feel free to share your feedback, findings or ask any questions on the forums.