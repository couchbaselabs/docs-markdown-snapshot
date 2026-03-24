---
title: Manage AWS Private Endpoints Using the Management API
description: Configure and manage AWS private endpoints for App Services using
  the Capella Operational Management API.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/private-endpoints/app-services-private-endpoints-aws-api.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:app-services::private-endpoints/app-services-private-endpoints-aws-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/private-endpoints/app-services-private-endpoints-aws-api.html)

# Manage AWS Private Endpoints Using the Management API

> Configure and manage AWS private endpoints for App Services using the Capella Operational Management API. 

This guide walks you through setting up AWS private endpoints for App Services using the Capella Operational Management API for programmatic control and automation.

* For an overview of the Management API, see [Manage Deployments with the Capella Operational Management API](../../cloud/management-api-guide/management-api-intro.md).
* To get started with the Management API, see [Get Started with the Capella Operational Management API](../../cloud/management-api-guide/management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Operational Management API](../../cloud/management-api-guide/management-api-use.md).
* For a full reference guide, see [Management API Reference](../../cloud/management-api-reference/index.md).

## [](#prerequisites)Prerequisites

Before you set up and connect an AWS private endpoint for an App Service, you need:

* A successfully deployed Couchbase Capella cluster and App Service.
* Information about your AWS network, including:

  * The AWS VPC ID.
  * The AWS Subnet ID of each of the subnets.
* The [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured.
* Access to the [AWS VPC console](https://console.aws.amazon.com/vpc/).

## [](#examples-on-this-page)Examples on this Page

In the examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$appServiceId` is the App Service ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it is included in the examples.

## [](#configuration-procedure)Configuration Procedure

To configure private endpoints using the Management API:

1. [Enable private endpoints](#enable-private-endpoints)
2. [Monitor private endpoints](#monitor-private-endpoints)
3. [Obtain a connection command](#obtain-connection-command)
4. [Run the connection command](#run-connection-command)
5. [List connections](#list-connections) (Optional)
6. [Accept the connection](#accept-connection)
7. [Enable private DNS and security group access](#private-dns-sec-grp-access)
8. [Validate the connection](#validate-connection) (Optional)

## [](#enable-private-endpoints)Enable Private Endpoints

Enabling private endpoints for an App Service deploys all of the infrastructure which you need to initiate a connection. This runs as a job in the background, and deploys components such as the network load balancer and DNS configuration.

To enable private endpoints for a specified App Service:

1. Use [POST /appservices/{appServiceId}/privateEndpointService](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/postAppServicePrivateEndpoints).
2. Pass the App Service ID as a path parameter.

It can take several minutes for Capella to enable private endpoints.

Example 1\. Enable private endpoints for an App Service

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService" \
  -H "Authorization: Bearer $apiKeySecret"
```

## [](#monitor-private-endpoints)Monitor Private Endpoints

To view the current status of private endpoints for a specified App Service:

1. Use [GET /appservices/{appServiceId}/privateEndpointService](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/getAppServicePrivateEndpoints).
2. Pass the App Service ID as a path parameter.

The operation returns an object containing the following properties.

| state       | The current state of private endpoints for the specified App Service. Possible values are: enabling, disabling, enabled, disabled, and failed. |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| targetState | The intended state of private endpoints for the specified App Service. Possible states are: enabled and disabled.                              |

Example 2\. Get the status of private endpoints for an App Service

Request

```sh
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
    "state": "disabled",
    "targetState": "disabled"
}
```

## [](#obtain-connection-command)Obtain a Connection Command

Before you can initiate the private endpoint connection for an App Service, you must obtain the AWS connection command. For this procedure, you need the VPC ID and subnet IDs.

To obtain the connection command for a specified App Service:

1. Use [POST /appservices/{appServiceId}/privateEndpointService/privateEndpointCommand](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/getAppServicePrivateEndpointsCommand).
2. Pass the App Service ID as a path parameter.
3. Pass the VPC ID as a string in the request body.
4. Pass the subnet IDs as an array of strings in the request body.

The return value includes the connection command.

Example 3\. Get the connection command for an App Service

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService/privateEndpointCommand" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "vpcId": "vpc-0e4c66e70f63b51e0",
  "subnetIds": ["subnet-01423b12bd81bb116"]
}'
```

Output

```json
{
    "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-0e4c66e70f63b51e0 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-0823b61a6d8cee231 --vpc-endpoint-type Interface --subnet-ids subnet-01423b12bd81bb116"
}
```

## [](#run-connection-command)Run the Connection Command

To initiate the private endpoint connection for an App Service, run the connection command within the AWS CLI.

The connection command returns a JSON object, giving information about the private endpoint. The most useful information to note is the value of `VpcEndpointId`.

> [!NOTE]
> The private endpoint connection must be accepted by the App Service before you can use it.

Example 4\. Run the connection command for an App Service

This example uses the connection command obtained in [Example 3](#ex-obtain-connection-command).

Request

```sh
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-0e4c66e70f63b51e0 \
  --region us-east-1 \
  --service-name com.amazonaws.vpce.us-east-1.vpce-svc-0823b61a6d8cee231 \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-01423b12bd81bb116
```

Output

```json
{
    "VpcEndpoint": {
        "VpcEndpointId": "vpce-067bd56a2df9a130e",
        "VpcEndpointType": "Interface",
        "VpcId": "vpc-0e4c66e70f63b51e0",
        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03cf83ff522bf54aa",
        "State": "pendingAcceptance",
        "RouteTableIds": [],
        "SubnetIds": [
            "subnet-01423b12bd81bb116"
        ],
       // ...
    }
}
```

## [](#list-connections)List Connections

To list connection requests for a specified App Service:

1. Use [GET /appservices/{appServiceId}/privateEndpointService/endpoints](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/listAppServicePrivateEndpoints).
2. Pass the App Service ID as a path parameter.

Example 5\. List connection requests for an App Service

Request

```sh
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService/endpoints" \
  -H "Authorization: Bearer $apiKeySecret"
```

Output

```json
{
    "endpoints": [
        {
            "id": "vpce-067bd56a2df9a130e",
            "status": "pending"
        }
    ]
}
```

In this case, there is a private endpoint connection request in a pending state.

## [](#accept-connection)Accept and Complete Connection

When you run the connection command, the connection is pending, and not complete. To complete the connection, the App Services network must accept it.

To accept a connection for a specified private endpoint:

1. Use [POST /appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/acceptPrivateEndpointRequest).
2. Pass the App Service ID and private endpoint ID as path parameters.

The connection is initiated. It may take a short time to transition to the connected state.

Example 6\. Accept a connection for a private endpoint

In this example:

* `$endpointId` is the private endpoint ID.

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService/endpoints/$endpointId" \
  -H "Authorization: Bearer $apiKeySecret"
```

To verify the status of the connection, see [List Connections](#list-connections).

## [](#private-dns-sec-grp-access)Enable Private DNS and Security Group Access

> [!IMPORTANT]
> These steps are required to complete the private endpoint configuration. Complete these steps in the AWS VPC Console.

Follow these steps to ensure the connection is working correctly.

### [](#private-dns)Private DNS

You must enable private DNS in the cloud service provider’s endpoint to successfully connect to App Services.

To enable private DNS in AWS:

1. In the AWS console, go to **Endpoints** using the ID obtained earlier.
2. Choose **Actions** **Modify private DNS name**.
3. Under **Enable private DNS names**, select **Enable for this endpoint**.

### [](#security-groups)Security Groups

If your Couchbase Capella security groups do not properly allow through a connection, any attempt to communicate over the connection will hang. If this occurs, modify the security groups to allow the connection through.

To modify the security groups:

1. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), add an inbound rule for the private endpoint:

  1. With the **Your VPCs** page open, find and record the **IPv4 CIDR** value for your VPC, for example `10.0.0.0/16`. You need this for later steps.
  2. In the navigation pane, click **Endpoints**.
  3. Select your endpoint.
  4. In the **Security groups** panel, click the **Group ID** link. This link is to your default VPC security group.
  5. With the security group open to the **Inbound rules** panel, click **Edit inbound rules**.
  6. In the **Edit inbound rules** dialog, add the VPC IPv4 CIDR you recorded earlier and use the following port ranges:

    * `4984-4985`
    * `4988`
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
  > For any further questions or concerns, contact [Couchbase Support](#support:manage-support.adoc).
  5. Click **Save changes**.
3. In the [AWS VPC console](https://console.aws.amazon.com/vpc/), configure your network ACL with an outbound rule:

  1. In the navigation pane, click **Network ACLs**.
  2. Select the Network ACL associated with your VPC.
  3. Click **Actions** **Edit outbound rules**.
  4. On the **Edit outbound rules** page, specify the following for the new outbound rule:

| Field       | Value                                       |
| ----------- | ------------------------------------------- |
| Type        | Custom TCP                                  |
| Port ranges | 4984-4985; 4988                             |
| Destination | Your VPC IPv4 CIDR.For example: 10.0.0.0/16 |
  5. Click **Save Changes**.

## [](#validate-connection)Validate the Connection

Connect to an instance within the connected VPC and validate your connection.

Example 7\. Look up the App Services node

Request

```sh
nslookup a24yjkpxarl3drdb.apps.cloud.couchbase.com
```

Output

```console
Server: 10.0.1.2
Address: 10.0.1.2#53
Non-authoritative answer:
Name: a24yjkpxarl3drdb.apps.cloud.couchbase.com
Address: 10.0.1.89
```

Example 8\. Test the App Services node

Request

```sh
curl https://a24yjkpxarl3drdb.apps.cloud.couchbase.com:4984
```

Output

```json
{
  "couchdb": "Welcome",
  "vendor": {
    "name": "Couchbase Sync Gateway",
    "version":"3.2"
  },
  "version": "Couchbase Sync Gateway/3.2.2(21;3c0abf2) EE",
  "persistent_config": true
}
```

## [](#additional-operations)Additional Operations

### [](#reject-connection)Reject Connection

To reject a connection for a specified private endpoint:

1. Use [DELETE /appservices/{appServiceId}/privateEndpointService/endpoints/{endpointId}](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/deletePrivateEndpointRequest).
2. Pass the App Service ID and private endpoint ID as path parameters.

If the connection is already made, the connection is severed. If the connection is not yet established, the connection is just listed as rejected. It may take a short period of time to transition to the rejected state.

Example 9\. Reject a connection for a private endpoint

In this example:

* `$endpointId` is the private endpoint ID.

Request

```sh
curl -X DELETE "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService/endpoints/$endpointId" \
  -H "Authorization: Bearer $apiKeySecret"
```

To verify the status of the connection, see [List Connections](#list-connections).

### [](#remove-connections)Remove Connections

Removing connections isn’t usually necessary for most operations using App Services. If you want to remove a connection, there are two options:

* Delete the endpoint via the AWS CLI or the AWS console.
* [Reject the connection](#ex-reject-connection). The connection is severed, but remains in the [connection list](#list-connections) as rejected.

### [](#turn-app-services-on-and-off)Turn App Services On and Off

The [App Services On/Off](../app-services/turn-on-off.md) feature is fully compatible with private endpoints. When an App Service is turned off, any private endpoints will remain in place, although not usable. When the App Service is turned back on, any private endpoints will begin working again. You do not need to re-create any private endpoints.

> [!NOTE]
> When an App Service is turned off, a network load balancer remains active in the infrastructure to maintain the private endpoint state. There is some cost associated with this, even though the App Service is turned off. To avoid this cost, you must fully tear down the private endpoint and disable it, before turning off the App Service.

### [](#disable-private-endpoints)Disable Private Endpoints

You can disable private endpoints for an App Service without needing to remove or reject any connections first.

To disable private endpoints for a specified App Service:

1. Use [DELETE /appservices/{appServiceId}/privateEndpointService](../../cloud/management-api-reference/index.md#tag/App-Services-Private-Endpoints/operation/deleteAppServicePrivateEndpoints).
2. Pass the App Service ID as a path parameter.

All existing connections are rejected and the private endpoints service is torn down.

Example 10\. Disable private endpoints for an App Service

Request

```sh
curl -X DELETE "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/appservices/$appServiceId/privateEndpointService" \
  -H "Authorization: Bearer $apiKeySecret"
```

To monitor the status of private endpoints for an App Service, see [Monitor Private Endpoints](#monitor-private-endpoints).

## [](#see-also)See Also

* [Private Endpoints for App Services](app-services-private-endpoints.md)
* [Manage AWS Private Endpoints Using the UI](app-services-private-endpoints-aws-ui.md)
* [Add Private Endpoints](../../cloud/security/private-endpoints.md)
* [Configure a VPC Peering Connection](../../cloud/clouds/private-network.md)
* [Add an AWS PrivateLink Connection](../../cloud/security/add-aws-private-link.md)