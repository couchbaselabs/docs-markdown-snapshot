---
title: Manage AWS Private Endpoints for the Data API
description: How to configure and manage private endpoints for the Data API
  using Amazon Web Services (AWS).
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-guide/pages/data-api-private-aws.adoc
pubDate: 2026-04-01T05:25:30.286Z
link: xref:cloud:data-api-guide:data-api-private-aws.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-guide/data-api-private-aws.html)

# Manage AWS Private Endpoints for the Data API

> How to configure and manage private endpoints for the Data API using Amazon Web Services (AWS). 

To configure and manage AWS private endpoints with the Data API, you can use the Capella UI or the Capella Management API.

* For an overview of the Management API, see [Manage Deployments with the Capella Operational Management API](../management-api-guide/management-api-intro.md).
* To get started with the Management API, see [Get Started with the Capella Operational Management API](../management-api-guide/management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Operational Management API](../management-api-guide/management-api-use.md).
* For a full Management API reference guide, see [Capella Operational Management API Reference](../management-api-reference/index.md).

## [](#prerequisites)Prerequisites

Before you set up and connect an AWS private endpoint for the Data API:

* You must have successfully deployed a Couchbase Capella operational cluster and the Data API.
* You must have installed and configured the [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).
* You must know the VPC ID and Subnet IDs that you want to connect to.

## [](#examples)Examples on this Page

In the Management API examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$apiKeySecret` is the Management API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it's included in the examples.

## [](#setup)Set Up and Connect a Private Endpoint

To set up and connect an AWS private endpoint for the Data API, follow the steps below.

Procedure:

1. [Obtain a Connection Command](#obtain-connection-command)
2. [Run the Connection Command](#run-connection-command)
3. [Accept and Complete Connection](#accept-connection)
4. [Enable Private DNS and Security Group Access](#private-dns-sec-grp-access)
5. [Validate the Connection](#validate-connection) (Optional)

### [](#obtain-connection-command)Obtain a Connection Command

In order to set up the private endpoint connection for the Data API, you must obtain the AWS connection command. For this procedure, you need the VPC ID and subnet IDs.

* Capella UI
* Management API

To obtain the connection command for the Data API:

1. On the **Operational Clusters** page, click on the cluster where you want to add a private endpoint for the Data API.
2. Go to **Settings** **Networking** **Private Endpoints**.
3. Click the **Data API** tab.
4. Click **Add Private Endpoint**.
5. In the **Provide Private Endpoint Details** section, add the following information:

| Field      | Value                                                |
| ---------- | ---------------------------------------------------- |
| VPC ID     | Enter your AWS VPC ID.                               |
| Subnet IDs | Enter each Subnet ID and separate them with a comma. |
6. Click **Next**. The connection command is displayed.
7. Click the connection command to copy it, or click the Download icon  to download a shell script containing the connection command.

To obtain the connection command for the Data API:

1. Use [POST /dataAPI/privateEndpointCommand](../management-api-reference/index.md#tag/Data-API/operation/getDataAPIPrivateEndpointCommand).
2. Pass the VPC ID as a string in the request body.
3. Pass the subnet IDs as an array of strings in the request body.

The return value includes the connection command.

---

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI/privateEndpointCommand" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "vpcID": "vpc-1234",
  "subnetIDs": ["subnet-1234"]
}'
```

Output

```json
{
  "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-1234 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 --vpc-endpoint-type Interface --subnet-ids subnet-1234"
}
```

### [](#run-connection-command)Run the Connection Command

To set up the private endpoint connection for the Data API, run the connection command within the AWS CLI.

The connection command returns a JSON object, giving information about the private endpoint. The most useful information to note is the value of `VpcEndpointId` — this is the private endpoint ID.

> [!NOTE]
> The private endpoint connection must be accepted by the Data API before you can use it.

Run the connection command for the Data API

This example uses the connection command obtained in [Obtain a Connection Command](#obtain-connection-command).

Request

```sh
aws ec2 create-vpc-endpoint \
          --vpc-id vpc-1234 \
          --region us-east-1 \
          --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 \
          --vpc-endpoint-type Interface \
          --subnet-ids subnet-1234
```

Output

```json
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-067bd56a2df9a130e",
        "VpcEndpointType": "Interface",
        "VpcId": "vpc-1234",
        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-1234",
        "State": "pendingAcceptance",
        "RouteTableIds": [],
        "SubnetIds": [
            "subnet-1234"
        ],
       // ...
    }
}
```

### [](#accept-connection)Accept and Complete Connection

When you run the connection command, the connection is pending, and not complete. To complete the connection, the Data API network must accept it.

To reject the connection at this point, see [Remove Private Endpoints](#remove-connections).

* Capella UI
* Management API

To accept a connection for a specified private endpoint:

1. Wait for the new interface endpoint to be shown with a **Pending Acceptance** status.
2. Click the **Accept** button for the pending private endpoint.

The connection is initiated. It may take a short time to transition to the connected state.

To accept a connection for a specified private endpoint:

1. Use [POST /dataAPI/privateEndpoints/{endpointId}/associate](../management-api-reference/index.md#tag/Data-API/operation/associateDataAPIPrivateEndpointRequest).
2. Pass the private endpoint ID as a path parameter.

The connection is initiated. It may take a short time to transition to the connected state.

---

In this example:

* `$endpointId` is the private endpoint ID.

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI/privateEndpoints/$endpointId/associate" \
  -H "Authorization: Bearer $apiKeySecret"
```

To verify the status of the connection, see [View Private Endpoints](#list-connections).

### [](#private-dns-sec-grp-access)Enable Private DNS and Security Group Access

Follow these tips to ensure the connection is working correctly.

#### [](#private-dns)Private DNS

You must enable private DNS in the cloud service provider's endpoint to successfully connect to the Data API.

To enable private DNS in AWS:

1. In the AWS console, go to **Endpoints** using the ID obtained earlier.
2. Choose **Actions** **Modify private DNS name**.
3. Under **Enable private DNS names**, select **Enable for this endpoint**.

#### [](#security-groups)Security Groups

If your Couchbase Capella security groups do not allow a connection, any attempt to communicate over the connection will hang. If this occurs, modify the security groups to allow the connection through.

To modify the security groups:

1. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), add an inbound rule for the private endpoint:

  1. With the **Your VPCs** page open, find and record the **IPv4 CIDR** value for your VPC, for example `10.0.0.0/16`. You need this for later steps.
  2. In the navigation pane, click **Endpoints**.
  3. Select your endpoint.
  4. In the **Security groups** panel, click the **Group ID** link. This link is to your default VPC security group.
  5. With the security group open to the **Inbound rules** panel, click **Edit inbound rules**.
  6. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port ranges:

    * 443
  7. Click **Save rules**.
2. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), configure your network access control list (ACL) with an inbound rule:

  1. In the navigation pane, click **Network ACLs**.
  2. On the **Network ACLs** page, select the Network ACL associated with your VPC.
  3. Click **Actions** **Edit inbound rules**.
  4. On the **Edit inbound rules** page, specify the following for a new inbound rule:

| Field      | Value                                       |
| ---------- | ------------------------------------------- |
| Source     | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
| Type       | All traffic                                 |
| Port range | All                                         |  
  > [!CAUTION]  
  > Before selecting `All traffic` as an inbound rule, consult with your security team and confirm that your private link meets security standards.  
  >  
  > For any further questions or concerns, contact [Couchbase Support](../support/manage-support.md).
  5. Click **Save changes**.
3. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), configure your network ACL with an outbound rule:

  1. In the navigation pane, click **Network ACLs**.
  2. Select the Network ACL associated with your VPC.
  3. Click **Actions** **Edit outbound rules**.
  4. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value                                       |
| ----------- | ------------------------------------------- |
| Type        | Custom TCP                                  |
| Port ranges | 443                                         |
| Destination | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  5. Click **Save Changes**.

For more information, see [Add an AWS PrivateLink Connection](../security/add-aws-private-link.md).

### [](#validate-connection)Validate the Connection

Connect to an instance within the connected VPC and validate your connection.

Look up the Data API node

In this example:

* `$BASEURL` is the base URL for the Data API.

Request

```sh
nslookup $BASEURL
```

Output

```console
Server: 10.0.1.2
Address: 10.0.1.2#53
Non-authoritative answer:
Name: <BASEURL>
Address: 10.0.1.89
```

Test the Data API node

In this example:

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

Request

```sh
curl "$BASEURL/v1/callerIdentity" \
  -u $USER:$PASSWORD
```

Output

```json
{"user": "<USER>"}
```

## [](#list-connections)View Private Endpoints

You can view a list of private endpoints and connection requests using the Capella UI or the Management API.

* Capella UI
* Management API

To view private endpoints and connection requests for the Data API:

1. Go to **Settings** **Networking** **Private Endpoints**.
2. Click the **Data API** tab. Any existing private endpoints or connection requests are shown in the **Data API Private Endpoints** list.

The **Status** column shows the status of each connection. Connection requests are shown with the status **Pending Acceptance**.

To view private endpoints and connection requests for the Data API:

1. Use [GET /dataAPI/privateEndpoints](../management-api-reference/index.md#tag/Data-API/operation/listDataAPIPrivateEndpoints).
2. Check the response to see the status of each connection. Connection requests are shown with the status `"pending"`.

---

Request

```sh
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI/privateEndpoints" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
  "endpoints": [
    {
      "id": "vpce-000000000000aaaaa",
      "status": "pending"
    }
  ]
}
```

In this case, there is a private endpoint connection request in a pending state.

## [](#remove-connections)Remove Private Endpoints

You can remove a private endpoint or reject a connection request using the Capella UI or the Management API.

Alternatively, delete the private endpoint via the AWS CLI or the AWS console.

* Capella UI
* Management API

To delete a specified private endpoint:

1. Display the list of Data API Private Endpoints.
2. Click the trash icon  for the private endpoint.
3. When prompted, type `delete` and click **Delete Private Endpoints**.

The private endpoint is removed from the list. It may take a short period of time to be deleted.

To disassociate a specified private endpoint:

1. Use [POST /dataAPI/privateEndpoints/{endpointId}/unassociate](../management-api-reference/index.md#tag/Data-API/operation/disassociateDataAPIPrivateEndpoint).
2. Pass the private endpoint ID as a path parameter.

If the connection is already made, the connection is severed, but remains in the [connection list](#list-connections) as rejected. If the connection is not yet established, the connection is just listed as rejected. It may take a short period of time to transition to the rejected state.

---

In this example:

* `$endpointId` is the private endpoint ID.

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI/privateEndpoints/$endpointId/unassociate" \
  -H "Authorization: Bearer $apiKeySecret"
```

To verify the status of the connection, see [View Private Endpoints](#list-connections).

## [](#on-off)Turn the Data API On and Off

Turning the Data API on or off is fully compatible with private endpoints. When the Data API is turned off, any private endpoints will remain in place, although not usable. When the Data API is turned back on, any private endpoints will begin working again. You do not need to re-create any private endpoints.

## [](#see-also)See Also

* [Add Private Endpoints](../security/private-endpoints.md)
* [Configure a VPC Peering Connection](../clouds/private-network.md)
* [Private Endpoints for App Services](../../app-services/private-endpoints/app-services-private-endpoints.md)