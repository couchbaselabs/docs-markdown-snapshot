---
title: Connecting to Tableau Cloud using the Tableau Bridge
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.1/modules/ROOT/pages/connecting-to-tableau-cloud-using-tableau-bridge.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tableau-connector::connecting-to-tableau-cloud-using-tableau-bridge.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/connecting-to-tableau-cloud-using-tableau-bridge.html)

# Connecting to Tableau Cloud using the Tableau Bridge

> This guide will walk you through the steps for connecting to Tableau Cloud via the Tableau Bridge. The Tableau Bridge is currently available for Windows and Linux, so the following guide will show you how to run the Linux version in a Docker instance.
> 
> (Instructions for running the bridge under Windows are available [here](https://help.tableau.com/current/online/en-us/to%5Fbridge%5Fwindow%5Finstall.htm)).

## [](#prerequisites)Prerequisites

Before you run through this guide, make sure that you have [installed Tableau Desktop](setup-tableau-desktop.md)and have [set up a Couchbase Analytics datasource](setup-tableau-desktop.md).

## [](#download-the-tableau-bridge)Download the Tableau Bridge package

1. Download the latest Bridge `.rpm` package from the [Tableau download page](https://www.tableau.com/support/releases/bridge).
2. Create a working directory and copy the `.rpm` package to the new directory.  
```shell  
cd ~  
mkdir Docker  
cd Docker  
cp <download location>/TableauBridge-20243.24.1211.0901.x86_64.rpm .  
```

## [](#download-the-couchbase-analytics-tableau-connector)Download the Couchbase Analytics Tableau Connector

1. Download the latest version of the Couchbase Analytics Tableau Connector from [here](release-notes.md).
2. Unzip the downloaded zip archive and copy the `.taco` and `.jar` files to the working directory you created in the [Download the Tableau Bridge package](#download-the-tableau-bridge) section.  
```shell  
cp <download location>/couchbase-tableau-connector-1/couchbase-analytics-1.1.3.taco .  
cp <download location>/couchbase-tableau-connector-1/couchbase-jdbc-driver-1.0.5.jar .  
```

## [](#create-the-docker-file)Create the Docker file

1. Create a new Docker file in the working directory.  
```shell  
touch Dockerfile  
```
2. Now edit `Dockerfile`, adding the following contents.  
```shell  
FROM registry.access.redhat.com/ubi8/ubi:latest  
RUN yum -y update  
COPY TableauBridge-20243.24.1211.0901.x86_64.rpm /opt  
RUN ACCEPT_EULA=y yum install -y /opt/TableauBridge-20243.24.1211.0901.x86_64.rpm  
COPY couchbase-jdbc-driver-1.0.5.jar /opt/tableau/tableau_driver/jdbc/  
COPY couchbase-analytics-1.1.3.taco /root/Documents/My_Tableau_Bridge_Repository/Connectors/  
```  
> [!NOTE]  
> Make sure the name of the `.rpm` file matches the file downloaded in the [Download the Tableau Bridge package](#download-the-tableau-bridge) section.

## [](#build-the-docker-image)Build the Docker image

1. Use the following command to build a new container image.  
```shell  
docker buildx build --platform=linux/amd64 -t bridge_base .  
```
2. When the `docker` command completes, use the following command to ensure that the images have been installed properly.  
```shell  
docker images | grep bridge  
```

## [](#start-an-instance-of-the-bridge-container)Start an instance of the Bridge Container

1. Start a second instance of the shell.
2. Use the following command to start the container with the `bride_base` image in the new shell.  
```shell  
docker run -it bridge_base /bin/bash  
```  
This will create and run the container and open a command shell in the new container instance. In the following section, you will create an access token and add it to the new container.

## [](#create-a-personal-access-token)Create a Personal Access Token

> [!NOTE]
> Creating personal access tokens on Tableau Cloud
> 
> Before you can create a Personal Access Token, your Tableau Cloud service must be set up to allow you to do so.
> 
> If you cannot create a PAT, ask your Tableau Cloud administrator to grant PAT permissions on your service instance

1. Log in to your Tableau Cloud instance and select **My Account Settings** from the drop-down menu on the top-right.
2. Scroll down to the section named **Personal Access Tokens** and enter a **Token Name** in the field.
3. Click the **Create Token** button.  
![create PAT](_images/create_PAT.png)
4. Press **Copy Secret** to copy the PAT to the clipboard.  
> [!WARNING]  
> You should copy the PAT to a file immediately (as shown below).  
>  
> Tableau Cloud will not allow you to view or copy the token again after you have pressed **Done**.
5. Create a new directory called `Documents` in your `bridge_base` container.
6. Create a new `.txt` file in your `Documents` directory. You can call it `MyTokenFile.txt`, for example. The file should be in JSON format and take the form:  
```json  
{  
  "MyToken":  
  "<PAT_Token/>"  
}  
```  
Where `PAT_token` is the token you have copied [here](#create%5Fcopy%5Ftoken).

## [](#run-the-bridge)Run the Bridge

1. Execute the bridge by running the following command inside the container.  
```shell  
/opt/tableau/tableau_bridge/bin/run-bridge.sh -e --patTokenId="MyToken" \
 --userEmail="admin@tableau.com" --client="myBridgeAgent" --site="couchbasetableaupartnerprogram" \
 --patTokenFile="/Documents/MyTokenFile.txt"  
```  
`--patTokenId`  
The name of the personal access token given in the [JSON file](#create-pat-file).  
`--userEmail`  
Your email address.  
`--client`  
An arbitrary name that the bridge will assign to the agent.  
`--site`  
The name of the Tableau Cloud site that the bridge will attach to. The name of the site can be found in the URL site string of your Tableau cloud instance.  
![url example](_images/url-example.png)  
`--patTokenFile`  
The location of the file where the PAT is stored.

## [](#publish-a-datasource-to-tableau-cloud)Publish a DataSource to Tableau Cloud

1. Start the Tableau Desktop application and sign in to Tableau Cloud  
![Sign into Tableau Cloud](_images/sign-in-tableau-cloud.png)
2. After providing your sign-in credentials, check the status on the menu bar to ensure you’re signed in correctly.  
![Signed in](_images/signed-in-menu.png)
3. From the Tableau Desktop menu, click **Server** **Publish Data Source**and select the pre-existing datasource you wish to publish to Tableau Cloud.  
![Publish datasource](_images/publish-data-source-dialog.png)
4. Change the `location`, if required.
5. Click the **Publish** button.

Tableau Cloud should now load in your web browser, showing the newly published datasource.

![extracted to tableau cloud](_images/extracted-to-tableau-cloud.png) 

For more information …

For more information on installation and troubleshooting, see [Install Bridge for Linux for Containers](https://help.tableau.com/current/online/en-us/to%5Fbridge%5Flinux%5Finstall.htm)