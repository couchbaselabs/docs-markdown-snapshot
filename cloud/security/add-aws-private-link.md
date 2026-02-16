[View original HTML](/cloud/security/add-aws-private-link.html)

> Add an AWS PrivateLink connection that peers your Amazon Web Service (AWS) network with a Capella cluster using AWS as its cloud provider. This connection can reduce latency and egress costs for applications hosted in the same region. 

|  | XDCR and Prometheus Metrics AWS PrivateLink connections can support [cross data center replication (XDCR)](../clusters/xdcr/xdcr.md) and [Prometheus metrics](../clusters/monitoring/prometheus.md). These features are only available upon request and are subject to specific conditions. For more information about the XDCR conditions, see [Replicate Data Across a Private Endpoint Connection](../clusters/xdcr/manage-xdcr-security.md#private-endpoints). For more information about the Prometheus conditions, see [Prometheus metrics](../clusters/monitoring/prometheus.md). |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

To use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) with Capella, you need:

* A project in your organization.  
For more information about projects in Capella, see [Projects Overview](../projects/projects.md).
* The [Project Owner](../projects/project-roles.md#project-owner-role) role assigned to your user account.
* A cluster in your project with:

  * AWS as its cloud provider.
  * The **Developer Pro** or **Enterprise** plan.  
For more information about how to create a cluster, see [Create A Paid Cluster](../clusters/create-database.md).
* Information about your AWS network, including:

  * The **AWS VPC ID**.
  * The **AWS Subnet ID** of each of the subnets.
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.
* Access to the AWS VPC console.

## [](#procedure)Procedure

To add an AWS PrivateLink connection, you need to:

1. [Enable private endpoints](#enable-pe).
2. [Add a private endpoint](#add-pe).
3. [Configure AWS VPC console settings](#config-aws-vpc-settings):

  1. [Enable private DNS names](#enable-private-dns-names).
  2. [Edit VPC settings](#edit-vpc-settings).
  3. [Add an inbound rule](#add-inbound-rule).
  4. [Configure inbound and outbound network ACL rules](#config-in-out-rules).
4. [Verify the connection](#verify-connection).

To get started, open the Capella UI, the AWS command line interface, and the AWS VPC console.

### [](#enable-pe)Enable Private Endpoints

In Capella, enable Private Endpoints:

|  | Enabling Private Endpoints bills your account hourly for AWS PrivateLink until you turn off this option. |
|  | -------------------------------------------------------------------------------------------------------- |

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**. Select the cluster where you want to add an AWS PrivateLink connection.
  2. Click your current project name or search for a project and go to **Operational**. Select the cluster where you want to add an AWS PrivateLink connection.
  3. Expand the cluster breadcrumb and search for or select a cluster where you want to add an AWS PrivateLink connection.
2. Go to **Settings** **Private Endpoints**.
3. Click **Enable Private Endpoint Service**.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints in Capella. You can leave and return to the **Private Endpoints** page at any time.

### [](#add-pe)Add a Private Endpoint

To add a private endpoint:

1. Click **Add Private Endpoint**.
2. In the **Provide Private Endpoint Details** section, add the following information:

| Field      | Value                                                |
| ---------- | ---------------------------------------------------- |
| VPC ID     | Enter your AWS VPC ID.                               |
| Subnet IDs | Enter each Subnet ID and separate them with a comma. |
3. Click **Next**.
4. Download and run the shell script provided by Capella:

  1. In the **Run the following script** area, click **Download Script**.
  2. With AWS CLI installed and signed in, run the downloaded shell script in your terminal.  
  This script contains the command to create the private endpoint in your chosen AWS VPC. When successful, the provisioning details output appears as follows:  
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
5. In Capella, the new interface endpoint is now shown and has a **Pending Acceptance** status. Click **Accept**.

### [](#config-aws-vpc-settings)Configure Your AWS VPC Console Settings

In the [AWS VPC console](https://console.aws.amazon.com/vpc/), you need to:

1. [Enable private DNS names](#enable-private-dns-names).
2. [Edit VPC settings](#edit-vpc-settings).
3. [Add an inbound rule](#add-inbound-rule).
4. [Configure inbound and outbound network ACL rules](#config-in-out-rules).

#### [](#enable-private-dns-names)Enable Private DNS Names

To enable private DNS names for the new endpoint:

1. In the navigation pane, click **Endpoints**.
2. With your endpoint selected, click **Actions** **Modify private DNS name**.
3. On the **Modify private DNS name** screen, select **Enable for this endpoint**.
4. Click **Save changes**.

#### [](#edit-vpc-settings)Edit VPC Settings

To edit your VPC settings:

1. In the navigation pane, click **Your VPCs**.
2. With your VPC selected, click **Actions** **Edit VPC settings**.
3. In the **Edit VPC settings** dialog, select **Enable DNS resolution** and **Enable DNS hostnames**.
4. Click **Save**.
5. With the **Your VPCs** page open, find and record the **IPv4 CIDR** value for your VPC. You need this for later steps.

#### [](#add-inbound-rule)Add an Inbound Rule

To add an inbound rule for the private endpoint:

1. In the navigation pane, click **Endpoints**.
2. Select your endpoint.

  1. In the **Security groups** panel, click the **Group ID** link. This link is to your default VPC security group.
  2. With the security group open to the **Inbound rules** panel, click **Edit inbound rules**.
3. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port ranges:

  * 18091-18203
  * 11207-11308
4. Click **Save rules**.

#### [](#config-in-out-rules)Configure Inbound and Outbound Network ACL Rules

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

|  | Before selecting All traffic as an inbound rule, consult with your security team and confirm that your private link meets security standards. For any further questions or concerns, contact [Couchbase Support](../support/manage-support.md). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  3. Click **Save changes**.
4. Configure your outbound rule:

  1. Click **Actions** **Edit outbound rules**.
  2. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value                                       |
| ----------- | ------------------------------------------- |
| Type        | Custom TCP                                  |
| Port range  | 1024-65535                                  |
| Destination | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  3. Click **Save Changes**.

### [](#verify-connection)Verify the Connection

Verify the connection in Capella by opening the **Private Endpoints** page. The new private endpoint shows a **Linked** status when the connection is complete. This status change can take several minutes after completing the configuration procedure.