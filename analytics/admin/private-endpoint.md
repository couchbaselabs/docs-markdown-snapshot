---
title: AWS PrivateLink Connection
description: Add an AWS PrivateLink connection that connects your Amazon Web
  Service (AWS) network with a Capella Analytics cluster.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/private-endpoint.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:admin:private-endpoint.adoc[]
---

[View original HTML](/analytics/admin/private-endpoint.html)

# AWS PrivateLink Connection

> Add an AWS PrivateLink connection that connects your Amazon Web Service (AWS) network with a Capella Analytics cluster. 

This connection can reduce latency and egress costs for applications hosted in the same region.

## [](#prerequisites)Prerequisites

To use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) with Capella Analytics, you need:

* One of the following Capella roles:

  * Organization Owner
  * Project Owner
* A Capella Analytics cluster in your project with multiple availability zones.
* Access to the [Amazon VPC console](https://console.aws.amazon.com/vpc/) and information about your AWS network, including:

  * AWS VPC ID
  * AWS Subnet ID of each subnet
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.

## [](#set-up-the-private-endpoint)Set Up the Private Endpoint

> [!NOTE]
> Enabling private endpoints bills your account hourly for AWS PrivateLink until you disable this option.

To add a connection using AWS PrivateLink, you use both the Capella UI and the AWS command line interface. Use an authorized account to access each one.

1. In the Capella UI, select the **Capella Analytics** tab and then select a cluster.
2. Select **Settings** **Private Endpoints**.
3. Click **Enable Private Endpoints**.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints in Capella.
4. Click **Add Private Endpoint**.
5. Complete the **Private Endpoint Details** fields.  
> [!TIP]  
> You can use the [Amazon VPC console](https://console.aws.amazon.com/vpc/) to locate most of this information.  
VPC ID  
The AWS VPC ID.  
Subnet IDs  
Enter every Subnet ID in a comma-separated list.
6. Click **Next**.
7. Download the connection shell script provided by Capella.
8. In the AWS CLI, run the downloaded shell script.  
This script contains the command to create the private endpoint in your AWS VPC. When successful, the provisioning details output appears as follows:  
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
9. In the Capella UI, the new endpoint appears with a **Pending Acceptance** status. Click **Accept**.
10. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), enable private DNS names for the new endpoint:

  1. In the navigation pane, click **Endpoints**.
  2. With your endpoint selected, click **Actions** **Modify private DNS name**.
  3. On the **Modify private DNS name** screen, select **Enable for this endpoint**:  
  ![AWS VPC Modify private DNS name screen](../../cloud/security/_images/aws-modify-private-dns-name-screen.png)
  4. Click **Save changes**.
11. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), edit your VPC settings:

  1. In the navigation pane, click **Your VPCs**.
  2. With your VPC selected, click **Actions** **Edit VPC settings**.
  3. In the **Edit VPC settings** dialog, select **Enable DNS resolution** and **Enable DNS hostnames**:  
  ![AWS VPC Enable VPC Settings](../../cloud/security/_images/aws-enable-vpc-settings.png)
  4. Click **Save**.
12. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), add an inbound rule for the private endpoint:

  1. With the **Your VPCs** page open, find and record the **IPv4 CIDR** value for your VPC. You need this for later steps. In this example, it’s `10.0.0.0/16`:  
  ![AWS VPC Dashboard](../../cloud/security/_images/aws-vpc-dashboard-for-ingress-rule.png)
  2. In the navigation pane, click **Endpoints**.
  3. Select your endpoint.
  4. In the **Security groups** pane, click the **Group ID** link. This link is to your default VPC security group.  
  ![AWS VPC Endpoints Display](../../cloud/security/_images/aws-endpoints-display.png)
  5. With the security group open to the **Inbound rules** pane, click **Edit inbound rules**.  
  ![AWS Security Groups display](../../cloud/security/_images/aws-security-groups.png)
  6. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port ranges:

    * 18091-18203
    * 11207-11308
  7. Click **Save rules**.
13. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), configure your network access control list (ACL) with an inbound rule:

  1. In the navigation pane, click **Network ACLs**.
  2. On the **Network ACLs** page, select the Network ACL associated with your VPC.
  3. Click **Actions** **Edit inbound rules**.
  4. On the **Edit inbound rules** page, specify the following for a new inbound rule:

| Field  | Value                                       |
| ------ | ------------------------------------------- |
| Source | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  5. Click **Save changes**.
14. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), configure your network ACL with an outbound rule:

  1. In the navigation pane, click **Network ACLs**.
  2. Select the Network ACL associated with your VPC.
  3. Click **Actions** **Edit outbound rules**.
  4. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value                                       |
| ----------- | ------------------------------------------- |
| Type        | Custom TCP                                  |
| Port range  | 1024-65535                                  |
| Destination | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  5. Click **Save Changes**.

## [](#next-steps)Next Steps

Verify the connection in Capella Analytics by reopening the cluster’s **Settings** **Private Endpoints** page. The new private endpoint shows a **Linked** status when the connection is complete. This status change can take several minutes after completing the configuration procedure.