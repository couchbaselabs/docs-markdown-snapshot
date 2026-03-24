---
title: Manage Azure Private Endpoints for the Data API
description: How to configure and manage private endpoints for the Data API
  using Microsoft Azure.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-guide/pages/data-api-private-azure.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:cloud:data-api-guide:data-api-private-azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-guide/data-api-private-azure.html)

# Manage Azure Private Endpoints for the Data API

> How to configure and manage private endpoints for the Data API using Microsoft Azure. 

To configure and manage AWS private endpoints with the Data API, you can use the Capella UI or the Capella Management API.

* For an overview of the Management API, see [Manage Deployments with the Capella Operational Management API](../management-api-guide/management-api-intro.md).
* To get started with the Management API, see [Get Started with the Capella Operational Management API](../management-api-guide/management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Operational Management API](../management-api-guide/management-api-use.md).
* For a full Management API reference guide, see [Management API Reference](../management-api-reference/index.md).

## [](#prerequisites)Prerequisites

Before you set up and connect an Azure private endpoint for the Data API:

* You must have successfully deployed a Couchbase Capella operational cluster and the Data API.
* You must have installed and configured the [Azure Command Line Interface (CLI)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
* You must know the names of the resource group, virtual network, and subnet that you want to connect to.

## [](#examples)Examples on this Page

In the Management API examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$apiKeySecret` is the Management API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it’s included in the examples.

## [](#setup)Set Up and Connect a Private Endpoint

To set up and connect an Azure private endpoint for the Data API, follow the steps below.

Procedure:

1. [Obtain a Connection Command](#obtain-connection-command)
2. [Run the Connection Command](#run-connection-command)
3. [Accept and Complete Connection](#accept-connection)
4. [Validate the Connection](#validate-connection) (Optional)

### [](#obtain-connection-command)Obtain a Connection Command

In order to set up the private endpoint connection for the Data API, you must obtain the Azure connection command. For this procedure, you need the resource group name and the virtual network and subnet names.

* Capella UI
* Management API

To obtain the connection command for the Data API:

1. On the **Operational Clusters** page, click on the cluster where you want to add a private endpoint for the Data API.
2. Go to **Settings** **Networking** **Private Endpoints**.
3. Click the **Data API** tab.
4. Click **Add Private Endpoint**.
5. In the **Provide Private Endpoint Details** section, add the following information:

| Field                  | Value                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Resource Group Name    | Enter your Azure resource group name.                                                                        |
| Virtual Network/Subnet | Enter your Azure virtual network and subnet in the following format: example-virtual-network/default-subnet. |
6. Click **Next**. The connection command is displayed.
7. Click the connection command to copy it, or click the Download icon  to download a shell script containing the connection command.

To obtain the connection command for the Data API:

1. Use [POST /dataAPI/privateEndpointCommand](../management-api-reference/index.md#tag/Data-API/operation/getDataAPIPrivateEndpointCommand).
2. Pass the resource group name as a string in the request body.
3. Pass the virtual network and subnet names as a string in the request body.

The return value includes the connection command.

---

Request

```sh
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI/privateEndpointCommand" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{
  "resourceGroupName": "test-rg",
  "virtualNetwork": "vnet-1/subnet-1"
}'
```

Output

```json
{
  "command": "az network private-endpoint create --connection-name connection-1 --name private-endpoint --private-connection-resource-id svc-1 --resource-group test-rg --subnet subnet-1 --group-id sites --vnet-name vnet-1"
}
```

### [](#run-connection-command)Run the Connection Command

To set up the private endpoint connection for the Data API, run the connection command within the Azure CLI.

The connection command returns information about the private endpoint, including the private endpoint ID.

> [!NOTE]
> The private endpoint connection must be accepted by the Data API before you can use it.

Run the connection command for the Data API

This example uses the connection command obtained in [Obtain a Connection Command](#obtain-connection-command).

If necessary, log into Azure first.

Request

```sh
az login

az network private-endpoint create \
  --connection-name connection-1 \
  --name private-endpoint \
  --private-connection-resource-id svc-1 \
  --resource-group test-rg \
  --subnet subnet-1 \
  --group-id sites \
  --vnet-name vnet-1
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

Alternatively, delete the private endpoint via the Azure CLI or the Azure portal.

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