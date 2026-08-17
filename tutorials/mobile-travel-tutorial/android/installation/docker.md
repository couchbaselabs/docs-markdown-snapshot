---
title: Docker (Local)
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/installation/docker.adoc
  xref: xref:tutorials:mobile-travel-tutorial:android/installation/docker.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/android/installation/docker.html)

# Docker (Local)

## [](#prerequisites)Prerequisites

> [!TIP]
> Windows Users
> 
> If you are developing on Windows, we recommend that you use a Windows 10 machine.  
> Also, note that if you choose the Manual or Docker installation mode, you should also have **administrative privileges on the Windows box** so you can authorize the installation and running of the required executables.

* Docker: downloadable from [docker.com](https://www.docker.com/get-docker). Community edition would suffice.

**Windows Users** : If you are developing on Windows, you will likely need to install Docker as Admin user.
* Microsoft Visual Studio 2019 (**only Windows Users**)
* Git: Downloadable from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Try it out

1. Verify the docker installation (applicable only if you decided to use the Docker install option).

  * Run the following command from your terminal.  
  ```bash  
  bash docker -v  
  ```  
  You should see the version of docker displayed.
2. Verify git installation

  * Run the following command from your terminal.  
  ```bash  
  bash git --version  
  ```  
  You should see the version of git installed.

## [](#repository)Workshop Repo

* Clone the "master" branch of the workshop source from GitHub. We are doing a shallow pull with `depth` as 1 to speed the cloning process.  
```bash  
git clone -b master --depth 1 https://github.com/couchbaselabs/mobile-travel-sample.git  
```

## [](#svr-local-dock)Couchbase Server

* Create a local docker network named "workshop" if one does not exist already. Open a terminal window and run the following command.  
```bash  
docker network ls  
docker network create -d bridge workshop  
```
* To run the application in a container, you will first get the docker image from Docker Hub. Open a new terminal window and run the following.  
```bash  
docker pull couchbase/server-sandbox:7.1.1  
```
* Once the command has completed you can start the application with the following.  
```bash  
docker run -d --name cb-server --network workshop -p 8091-8094:8091-8094 -p 11210:11210 couchbase/server-sandbox:7.1.1  
```
* You can view the logs at any time by running the following command.  
```bash  
docker logs cb-server  
```
* It may take a few seconds for the server to startup. Verify that the docker image is running with following command.  
```bash  
docker ps  
```

Try it out

1. Open the Couchbase Server "Admin Console" by opening <http://localhost:8091>(or <http://127.0.0.1:8091>)
2. Log into the console with username as "Administrator" and password as "password"
3. Select the "Buckets" option from the menu on the left
4. Verify that you have around 63,000 documents in your travel-sample bucket.  
Note that it can take a few minutes for the travel\_sample data set to load.

## [](#sgw-local-dock)Sync Gateway

> [!NOTE]
> If you are running the Sync Gateway in a docker container, please make sure that you have the Couchbase Server running in a container as well. If not, please follow the instructions in [Couchbase Server (above)](#svr-local-dock) to install the server container.

* Create a local docker network named "workshop" if one does not exist already. This should not be the case if you had followed the instructions to deploy Couchbase server using docker Open a terminal window and run the following command.  
```bash  
docker network ls  
docker network create -d bridge workshop  
```
* To run the application in a container, you will first get the docker image from Docker Cloud.  
```bash  
docker pull couchbase/sync-gateway:3.0.4-enterprise  
```
* The Sync Gateway will have to be launched with the config file named `sync-gateway-config-travelsample-docker.json`that you should have downloaded as part of the [Workshop Repo](#repository) step. The config file is located in the root folder of `/path/to/mobile-travel-sample`.
* Open the `sync-gateway-config-travelsample-docker.json` file using any text editor of choice
* For the app to connect to the Couchbase Server, the address of the the server needs to be specified. Note that when you launched the Couchbase Server docker container, you gave it the `name` of "cb-server".  
```json  
"server": "couchbase://cb-server"  
```
* Launch the Sync Gateway with the `sync-gateway-config-travelsample-docker.json` file. You must run the command below from the folder that contains the `sync-gateway-config-travelsample-docker.json` file.

* Windows
* Non-Windows platform

```bash
cd /path/to/mobile-travel-sample/
docker run -p 4984-4986:4984-4986 --network workshop --name sync-gateway -d -v %cd%/sync-gateway-config-travelsample-docker.json:/etc/sync_gateway/config.json couchbase/sync-gateway:3.0.4-enterprise -adminInterface :4985 /etc/sync_gateway/config.json
```

```bash
cd c:\path\to\mobile-travel-sample\
docker run -p 4984-4986:4984-4986 --network workshop --name sync-gateway -d -v `pwd`/sync-gateway-config-travelsample-docker.json:/etc/sync_gateway/config.json couchbase/sync-gateway:3.0.4-enterprise -adminInterface :4985 /etc/sync_gateway/config.json
```

* You can view the logs at any time by running the following command.  
```bash  
docker logs sync-gateway  
```
* Verify that the docker container named "sync-gateway" is running with the following command in the terminal window.  
```bash  
docker ps  
```

Try it out

1. Access this URL `<http://127.0.0.1:4984>` in your browser
2. Verify that you get back a JSON response similar to one below  
```json  
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"3.0"},"version":"Couchbase Sync Gateway/3.0.4(13;godeps/) EE"}  
```

## [](#python-travel-sample-web-backend)Python Travel Sample Web Backend

> [!NOTE]
> If you are running the Web App in a docker container, please make sure that you have the Couchbase Server and Sync Gateway running in the same docker network as well. If not, please follow instructions in the [Couchbase Server](#svr-local-dock) section to install the server container using docker and instructions in the [Sync Gateway](#sgw-local-dock) section to install sync gateway container.

* Create a local docker network named "workshop" if one does not exist already. Open a terminal window and run the following command.  
```bash  
docker network ls  
docker network create -d bridge workshop  
```
* To run the application in a container, you will first get the docker image from Docker Cloud. Open a terminal window and run the following.  
```bash  
docker pull connectsv/try-cb-python:7.1.1-server  
```
* Once the command has completed you can start the application with the following.  
```bash  
docker run -dip 8080:8080 --network workshop --name cb-backend-py connectsv/try-cb-python:7.1.1-server  
```
* You can view the logs at any time by running the following command.  
```bash  
docker logs cb-backend-py  
```  
You should then see the following in the console output.  
```bash  
Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)  
```
* Verify that the docker container named "cb-backend-py" is running with the following command in the terminal window.  
```bash  
docker ps  
```

1. Open <http://127.0.0.1:8080/>in your web browser.
2. Verify that you see the login screen of the Travel Sample Web App as shown in [Figure 1](#fig-travsample)

![try cb login 2](../../_images/try-cb-login-2.png) 

Figure 1\. Travel Sample Login Screen