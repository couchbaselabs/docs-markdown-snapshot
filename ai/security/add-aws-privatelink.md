[View original HTML](/ai/security/add-aws-privatelink.html)

> Add an AWS PrivateLink connection that peers your Amazon Web Service (AWS) network with AI Services using AWS as its cloud provider. 

|  | To link a Capella operational cluster with a model on the [Model Service](../get-started/intro.md#model), you only need to enable private networking. You do not have to perform any other configuration, Capella handles the connection automatically. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Private endpoints for AI Services are region-based. You’re linking the AWS region for your AI Services to your AWS VPC.

A single private endpoint can be shared by all your AI Services, as long as the models they access are deployed in the same region. For example, you can deploy multiple models within the same AWS region and use 1 private endpoint to link them all. You do not need to create a separate private endpoint for each model.

You can create another private endpoint when:

* You need to connect your AI Services AWS region to an application in a different AWS VPC.
* You deploy a model with a new AWS region. AI Services using models deployed in different regions need to add their own private endpoints.

## [](#prerequisites)Prerequisites

To use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) with Capella AI Services, you need:

* A deployed Capella model with:

  * The same AWS region as your AWS VPC.  
  For more information about Capella models, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md) or [Deploy a Large Language Model (LLM)](../build/model-service/deploy-llm-model.md).
* The [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role assigned to your user account.
* Information about your AWS network, including:

  * The [AWS VPC ID](https://docs.aws.amazon.com/quicksuite/latest/userguide/vpc-finding-setup-information.html#vpc-id).
  * The [AWS Subnet ID](https://docs.aws.amazon.com/quicksuite/latest/userguide/vpc-finding-setup-information.html#vpc-subnet-id) of each of the subnets.
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.
* You have logged in to and have access to the AWS VPC console.

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

In Capella AI Services, enable Private Endpoints:

|  | Enabling Private Endpoints bills your account hourly for AWS PrivateLink until you turn off this option. |
|  | -------------------------------------------------------------------------------------------------------- |

1. Go to **AI Services** **Private Endpoints**.
2. Find the region you want and click **Enable Private Endpoint**.

It can take several minutes for Capella to enable private endpoints.

### [](#add-pe)Add a Private Endpoint

To add a private endpoint:

1. Click the AWS region with the enabled private endpoint.
2. Click **Add Private Endpoint**.
3. In the **Provide Private Endpoint Details** section, add the following information:

| Field      | Value                                                |
| ---------- | ---------------------------------------------------- |
| VPC ID     | Enter your AWS VPC ID.                               |
| Subnet IDs | Enter each Subnet ID and separate them with a comma. |

|  | Before you complete your AWS PrivateLink connection, confirm that the port 8081 is open on your AWS VPC. |
|  | -------------------------------------------------------------------------------------------------------- |
4. Click **Get Script**.
5. Download and run the shell script provided by Capella:

  1. In the **Run the following script** area, click the download icon to download the shell script.
  2. Using the AWS CLI, run the downloaded shell script.  
  This script contains the command to create the private endpoint in your chosen AWS VPC. When successful, the provisioning details output appears as follows:  
  {  
      "VpcEndpoint": {  
          "VpcEndpointId": "vpce-1234567890abcdef0",  
          "VpcEndpointType": "Interface",  
          "VpcId": "vpc-1234567890abcdef0",  
          "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-abcdef1234567890",  
          "State": "pendingAcceptance",  
          "RouteTableIds": [],  
          "SubnetIds": [  
              "subnet-abcdef1234567890"  
          ],  
          "Groups": [  
              {  
                  "GroupId": "sg-abcdef1234567890",  
                  "GroupName": "default"  
              }  
          ],  
          "IpAddressType": "ipv4",  
          "DnsOptions": {  
              "DnsRecordIpType": "ipv4"  
          },  
          "PrivateDnsEnabled": false,  
          "RequesterManaged": false,  
          "NetworkInterfaceIds": [  
              "eni-abcdef1234567890"  
          ],  
          "DnsEntries": [  
              {  
                  "DnsName": "vpce-1234567890abcdef0-xyzabcde.vpce-svc-abcdef1234567890.us-east-1.vpce.amazonaws.com",  
                  "HostedZoneId": "ZABCDEFG123456"  
              },  
              {  
                  "DnsName": "vpce-1234567890abcdef0-xyzabcde-us-east-1a.vpce-svc-abcdef1234567890.us-east-1.vpce.amazonaws.com",  
                  "HostedZoneId": "ZABCDEFG123456"  
              }  
          ],  
          "CreationTimestamp": "2025-09-25T21:47:35.463000+00:00",  
          "OwnerId": "123456789012"  
      }  
  }
6. In Capella, the new interface endpoint is now shown and has a **Pending Acceptance** status. Click the **Accept** button.

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
3. In the **Security groups** panel, click the **Group ID** link. This link is to your default VPC security group.
4. With the security group open to the **Inbound rules** panel, click **Edit inbound rules**.
5. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port:

  * 8081
6. Click **Save rules**.

#### [](#config-in-out-rules)Configure Inbound and Outbound Network ACL Rules

To configure your network access control list (ACL) with an **Inbound** and **Outbound** rule:

1. In the navigation pane, click **Network ACLs**.
2. On the **Network ACLs** page, select the Network ACL associated with your VPC.
3. Configure your inbound rule:

  1. Click **Actions** **Edit inbound rules**.
  2. On the **Edit inbound rules** page, specify the following for a new inbound rule:

| Field      | Value               |
| ---------- | ------------------- |
| Source     | Your VPC IPv4 CIDR. |
| Type       | All traffic         |
| Port range | All                 |

|  | Before selecting All traffic as an inbound rule, consult with your security team and confirm that your private link meets security standards. For any further questions or concerns, contact [Couchbase Support](../../cloud/support/manage-support.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  3. Click **Save changes**.
4. Configure your outbound rule:

  1. Click **Actions** **Edit outbound rules**.
  2. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value               |
| ----------- | ------------------- |
| Type        | Custom TCP          |
| Port range  | 1024-65535          |
| Destination | Your VPC IPv4 CIDR. |
  3. Click **Save Changes**.

### [](#verify-connection)Verify the Connection

Verify the connection in Capella AI Services by opening the **Private Endpoints** page. The new private endpoint shows a **Linked** status when the connection is complete. This status change can take several minutes after completing the configuration procedure.