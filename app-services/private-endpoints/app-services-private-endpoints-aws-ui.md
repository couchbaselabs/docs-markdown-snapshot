---
title: Manage AWS Private Endpoints Using the Capella UI
description: Configure and manage AWS private endpoints for App Services using
  the Capella UI.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/private-endpoints/app-services-private-endpoints-aws-ui.adoc
  xref: xref:app-services::private-endpoints/app-services-private-endpoints-aws-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/private-endpoints/app-services-private-endpoints-aws-ui.html)

# Manage AWS Private Endpoints Using the Capella UI

> Configure and manage AWS private endpoints for App Services using the Capella UI. 

This guide walks you through setting up AWS private endpoints for App Services using the Capella UI for a streamlined, guided experience.

## [](#prerequisites)Prerequisites

Before you set up and connect an AWS private endpoint for an App Service, you need:

* A successfully deployed Couchbase Capella cluster and App Service.
* Information about your AWS network, including:

  * The AWS VPC ID.
  * The AWS Subnet ID of each of the subnets.
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.
* Access to the [AWS VPC console](https://console.aws.amazon.com/vpc/).

## [](#configuration-procedure)Configuration Procedure

To configure private endpoints using the UI:

1. [Enable private endpoints](#enable-pe)
2. [Add a private endpoint](#add-pe)
3. [Configure AWS VPC console settings](#config-aws-vpc):

  1. [Enable private DNS names](#enable-private-dns)
  2. [Edit VPC settings](#edit-vpc-settings)
  3. [Add an inbound rule](#add-inbound-rule)
  4. [Configure inbound and outbound network ACL rules](#config-acl-rules)
4. [Verify the connection](#verify-connection)

To get started, open the Capella UI, the AWS command line interface, and the AWS VPC console.

## [](#enable-pe)Enable Private Endpoints

In Capella, enable Private Endpoints:

> [!NOTE]
> Enabling Private Endpoints bills your account hourly for AWS PrivateLink until you turn off this option.

1. Go to **Operational** and click the name of your cluster.
2. Click the name of the App Service where you want to add an AWS PrivateLink connection.
3. Go to **Settings** **Private Endpoints**.
4. Click **Enable Private Endpoint Service**.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints in Capella. You can leave and return to the **Private Endpoints** page at any time.

## [](#add-pe)Add a Private Endpoint

To add a private endpoint:

1. Click **Add Private Endpoint**.
2. In the **Provide Private Endpoint Details** section, add the following information:

| Field      | Value                                                |
| ---------- | ---------------------------------------------------- |
| VPC ID     | Enter your AWS VPC ID.                               |
| Subnet IDs | Enter each Subnet ID and separate them with a comma. |
3. Click **Next**.
4. Copy and run the shell script provided by Capella:

  1. In the **Run the following script** area, click **Copy Script**.
  2. With AWS CLI installed and signed in, run the copied shell script in your terminal.  
  This script contains the command to create the private endpoint in your chosen AWS VPC. When successful, the provisioning details output appears as follows:  
  ```json  
  {  
    "VpcEndpoint": {  
      "VpcEndpointId": "vpce-06da68c605432752f",  
      "VpcEndpointType": "Interface",  
      "VpcId": "vpc-08bf9fdbf7174a563",  
      "ServiceName": "com.amazonaws.vpce.us-west-2.vpce-svc-015986e75057cc4e6",  
      "State": "pendingAcceptance",  
      "RouteTableIds": [],  
      "SubnetIds": [  
        "subnet-05f92391c3bb6b0fd",  
        "subnet-0b70e5c9e897f7ef0"  
      ],  
      "Groups": [  
        {  
          "GroupId": "sg-01505951c7752141d",  
          "GroupName": "default"  
        }  
      ],  
      "PrivateDnsEnabled": false,  
      "RequesterManaged": false,  
      "NetworkInterfaceIds": [  
        "eni-08cb66b65644ac32e",  
        "eni-0c824869e81a21fac"  
      ],  
      "DnsEntries": [  
        {  
          "DnsName": "vpce-06da68c605432752f-1zrggw92.vpce-svc-015986e75057cc4e6.us-west-2.vpce.amazonaws.com",  
          "HostedZoneId": "Z1YSA3EXCYUU9Z"  
        },  
        {  
          "DnsName": "vpce-06da68c605432752f-1zrggw92-us-west-2b.vpce-svc-015986e75057cc4e6.us-west-2.vpce.amazonaws.com",  
          "HostedZoneId": "Z1YSA3EXCYUU9Z"  
        },  
        {  
          "DnsName": "vpce-06da68c605432752f-1zrggw92-us-west-2a.vpce-svc-015986e75057cc4e6.us-west-2.vpce.amazonaws.com",  
          "HostedZoneId": "Z1YSA3EXCYUU9Z"  
        }  
      ],  
      "CreationTimestamp": "2022-11-15T18:50:45.062000+00:00",  
      "OwnerId": "429712224361"  
    }  
  }  
  ```
5. In Capella, the new interface endpoint is now shown and has a **Pending Acceptance** status. Click **Accept**.
6. After you accept the connection, [validate the connection](app-services-private-endpoints-aws-api.md#validate-connection).

## [](#config-aws-vpc)Configure Your AWS VPC Console Settings

> [!IMPORTANT]
> These steps are required to complete the private endpoint configuration. Complete these steps in the AWS VPC Console.

In the [AWS VPC console](https://console.aws.amazon.com/vpc/), you need to:

1. [Enable private DNS names](#enable-private-dns).
2. [Edit VPC settings](#edit-vpc-settings).
3. [Add an inbound rule](#add-inbound-rule).
4. [Configure inbound and outbound network ACL rules](#config-acl-rules).

### [](#enable-private-dns)Enable Private DNS Names

To enable private DNS names for the new endpoint:

1. In the navigation pane, click **Endpoints**.
2. With your endpoint selected, click **Actions** **Modify private DNS name**.
3. On the **Modify private DNS name** screen, select **Enable for this endpoint**.
4. Click **Save changes**.

### [](#edit-vpc-settings)Edit VPC Settings

To edit your VPC settings:

1. In the navigation pane, click **Your VPCs**.
2. With your VPC selected, click **Actions** **Edit VPC settings**.
3. In the **Edit VPC settings** dialog, select **Enable DNS resolution** and **Enable DNS hostnames**.
4. Click **Save**.
5. With the **Your VPCs** page open, find and record the **IPv4 CIDR** value for your VPC. You need this for later steps.

### [](#add-inbound-rule)Add an Inbound Rule

To add an inbound rule for the private endpoint:

1. In the navigation pane, click **Endpoints**.
2. Select your endpoint.
3. In the **Security groups** panel, click the **Group ID** link. This link is to your default VPC security group.
4. With the security group open to the **Inbound rules** panel, click **Edit inbound rules**.
5. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port ranges:

  * `4984-4985`
  * `4988`
6. Click **Save rules**.

### [](#config-acl-rules)Configure Inbound and Outbound Network ACL Rules

To configure your network access control list (ACL) with an **Inbound** and **Outbound** rule:

1. In the navigation pane, click **Network ACLs**.
2. On the **Network ACLs** page, select the Network ACL associated with your VPC.
3. Configure your inbound rule:

  1. Click **Actions** **Edit inbound rules**.
  2. On the **Edit inbound rules** page, specify the following for a new inbound rule:

| Field      | Value                                       |
| ---------- | ------------------------------------------- |
| Source     | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
| Type       | All traffic                                 |
| Port range | All                                         |  
  > [!CAUTION]  
  > Before selecting `All traffic` as an inbound rule, consult with your security team and confirm that your private link meets security standards. For any further questions or concerns, contact [Couchbase Support](#support:manage-support.adoc).
  3. Click **Save changes**.
4. Configure your outbound rule:

  1. Click **Actions** **Edit outbound rules**.
  2. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value                                       |
| ----------- | ------------------------------------------- |
| Type        | Custom TCP                                  |
| Port ranges | 4984-4985; 4988                             |
| Destination | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  3. Click **Save Changes**.

## [](#additional-operations)Additional Operations

### [](#turn-app-services-on-and-off)Turn App Services On and Off

The [App Services On/Off](../app-services/turn-on-off.md) feature is fully compatible with private endpoints. When an App Service is turned off, any private endpoints remain in place, although not usable. When the App Service is turned back on, any private endpoints begin working again. You do not need to re-create any private endpoints.

> [!NOTE]
> When an App Service is turned off, a network load balancer remains active in the infrastructure to maintain the private endpoint state. There is some cost associated with this, even though the App Service is turned off. To avoid this cost, you must fully tear down the private endpoint and disable it, before turning off the App Service.

### [](#disable-private-endpoints)Disable Private Endpoints

To disable private endpoints in the Capella UI:

1. Go to **Operational** and click the name of your cluster.
2. Click the name of the App Service.
3. Go to **Settings** **Private Endpoints**.
4. Click **Disable Private Endpoint Service**.

All existing connections are rejected and the private endpoints service is torn down.

## [](#see-also)See Also

* [Private Endpoints for App Services](app-services-private-endpoints.md)
* [Manage AWS Private Endpoints Using the Management API](app-services-private-endpoints-aws-api.md)
* [Add Private Endpoints](../../cloud/security/private-endpoints.md)
* [Configure a VPC Peering Connection](../../cloud/clouds/private-network.md)
* [Add an AWS PrivateLink Connection](../../cloud/security/add-aws-private-link.md)