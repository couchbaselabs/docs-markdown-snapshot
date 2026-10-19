---
title: Deploy Managed Agent Memory
description: Deploy a Managed Agent Memory server in Capella, connected to an
  operational cluster, and prepare it to accept requests from your agent.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/managed/pages/deploy-agent-mem-managed.adoc
  xref: xref:agent-mem:managed:deploy-agent-mem-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/managed/deploy-agent-mem-managed.html)

# Deploy Managed Agent Memory

> Deploy a Managed Agent Memory server in Capella, connected to an operational cluster, and prepare it to accept requests from your agent. 

Managed Agent Memory is the quickest way to get started with Agent Memory. With this deployment option, Capella deploys and runs your Agent Memory server. You choose the operational cluster and bucket where Agent Memory stores its data, and the embedding model and LLM it uses. You also set your server's name, number of nodes, and advanced settings. Capella provisions your server's compute in the same region as your chosen Couchbase cluster. To get working with Agent Memory, your agent connects to the server with the Python SDK and REST API.

If you have already completed the [quickstart](../get-started/get-started-agent-mem-managed.md), see [Manage Your Deployment](#manage).

> [!IMPORTANT]
> Managed Agent Memory is available on AWS only. You cannot scale a server after you deploy it, or connect to a server through a private endpoint.

## [](#prerequisites)Prerequisites

* A Capella account with 1 of the following roles:

  * [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../../../cloud/projects/project-roles.md#project-owner-role) in the project where you want to deploy your server  
  For the permissions of each role, see [Control Access to Managed Agent Memory](access-agent-mem-managed.md).
* A Couchbase Capella operational cluster with the following configuration:

  * A `Healthy` status.
  * Couchbase Server 8.0 or later.
  * The following services enabled:

    * [Data Service](../../../server/current/learn/services-and-indexes/services/data-service.md)
    * [Index Service](../../../server/current/learn/services-and-indexes/services/index-service.md)
    * [Query Service](../../../server/current/learn/services-and-indexes/services/query-service.md)
    * [Search Service](../../../server/current/learn/services-and-indexes/services/search-service.md)
  * Deployed on AWS in 1 of the following regions:

    * US East (N. Virginia), `us-east-1`
    * Europe (London), `eu-west-2`
  * No existing Agent Memory server. Each cluster can have 1 Agent Memory server.  
For more information about deploying an operational cluster to AWS, see [Create A Paid Cluster](../../../cloud/clusters/create-database.md).
* An OpenAI API key, added to the AI Data Plane as an integration. Agent Memory uses this key for its embedding model and large language model (LLM). You can use 1 integration for both models, or a separate integration for each. To create an AI integration, see [Manage AI Integration Settings](../../../ai/admin/manage-ai-integrations.md).

## [](#step-1-prepare-your-couchbase-cluster)Step 1: Prepare Your Couchbase Cluster

Before you deploy Managed Agent Memory, you need a dedicated bucket for Agent Memory in your operational cluster.

Your Agent Memory server connects to 1 bucket. Agent Memory creates the following scope and collections to store its data:

* Scope:

  * `<bucket>.agentmemory`
* Collections:

  * `<bucket>.agentmemory.users`
  * `<bucket>.agentmemory.sessions`
  * `<bucket>.agentmemory.memory`
  * `<bucket>.agentmemory.prompts`
  * `<bucket>.agentmemory.nodes`

To create a bucket in your operational cluster, see [Create a Bucket](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket).

## [](#deploy)Step 2: Deploy a Managed Agent Memory Server

To deploy a new Managed Agent Memory server:

1. Go to **AI Data Plane** **Services** **Agent Memory**.
2. Click **Deploy Agent Memory**.
3. In the **Cluster** list, choose the operational cluster you want to connect to your Agent Memory server, and click **Continue**.  
The list shows only clusters that meet the [prerequisites](#prerequisites). Your Agent Memory server uses the same Capella project, cloud provider region, and availability zones as your chosen cluster.
4. In the **Bucket** list, choose the bucket you created for Agent Memory to store its users, sessions, and memory blocks.
5. In the **Agent Memory Name** field, enter a name for your server, or accept the generated name.  
The name must be 2 to 64 characters, and cannot contain `<`, `>`, or quote characters (`"`, `'`, `` ` ``).
6. Under **Compute tier**, **Small** is the only option.  
Each node has 2 vCPUs and 4 GB of memory.
7. In the **Nodes** list, choose the number of nodes: 1, 3, 5, 7, or 9.  
The default is 1 node for a cluster in a single Availability Zone, and 3 nodes for a cluster in multiple Availability Zones.
8. Click **Next**.
9. On the **Models** step, choose your embedding model and LLM. For each model:

  1. In the **Model Source** list, choose **OpenAI**.
  2. In the **Choose OpenAI Model** list, choose a model.
  3. In the **OpenAI Integration Name** list, choose the OpenAI integration that provides the API key for the model.  
  To add a new OpenAI API key, click **\+ Add New OpenAI API key**. For more information about AI integrations, see [Manage AI Integration Settings](../../../ai/admin/manage-ai-integrations.md).
10. Click **Next**.
11. On the **Advanced** step, review the [server settings](#server-settings) and change any values you need.
12. Click **Next**.
13. On the **Review** step, review your configuration and click **Deploy Agent Memory**.

> [!IMPORTANT]
> You cannot change a server's cluster, bucket, models, compute tier, node count, or settings after you deploy it. To use a different configuration, see [Changing Your Configuration](#change-config).

### [](#server-settings)Advanced Settings

The **Advanced** step prefills each setting with its default. These settings correspond to the self-managed environment variables in [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md).

| Setting                 | Default | Range               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | ------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Requests per minute     | 1500    | 1 to 10,000         | Maximum model API requests per minute, across all nodes in the server. Set this to the limit for your OpenAI account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Tokens per minute       | 125000  | 8,192 to 10,000,000 | Maximum tokens per minute that Agent Memory sends to your models, across all nodes in the server. Set this to the limit for your OpenAI account. Set this to at least the **Per-request token limit** multiplied by the number of nodes. Otherwise, memory blocks larger than each node's share of the token budget stay in the extraction queue and are never extracted.                                                                                                                                                                                                                                                                                                                 |
| Queue max size          | 10000   | 10 to 50,000        | Maximum number of blocks queued for async extraction. When the queue is full, Agent Memory returns HTTP 429 with a Retry-After header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Max concurrent tasks    | 100     | 1 to 512            | Maximum number of concurrent async extraction tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Task timeout (s)        | 90      | 10 to 600           | Maximum time, in seconds, that a single async extraction task can run before Agent Memory cancels it. Increase if number of timeout errors from OpenAI increase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Idle sleep (s)          | 0.5     | 0.1 to 5            | Time, in seconds, between async extraction dispatch cycles. Lower to reduce extraction latency under sustained load; raise to reduce CPU usage when the queue is mostly idle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Per-request token limit | 4096    | 256 to 32,768       | Maximum token count for a single memory block. Agent Memory rejects larger blocks when your agent adds them. If a request contains blocks that fit, the response lists the rejected blocks in its rejected\_details field. If every block in the request is too large, the request fails with HTTP 400 and the error code MEMORY\_BLOCK\_TOO\_LARGE, and the error's details field lists the rejected blocks. If your agent updates a block with content that is too large, the request fails with the same error, and Agent Memory keeps the original block. Agent Memory also returns this error when a block is within this limit but exceeds the input limit of your embedding model. |
| Max fail count          | 3       | 1 to 10             | Number of extraction failures after which Agent Memory marks a block as permanently failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Summary token limit     | 700     | 256 to 4,096        | Maximum number of tokens in a generated summary. If your LLM is a reasoning model, such as GPT-5 or an o-series model, set a higher value. Reasoning tokens count towards this limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Processing batch size   | 5       | 1 to 20             | Number of memory blocks processed per batch when your agent adds memory with async\_processing=False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

> [!TIP]
> By default, memory blocks do not expire. To set a server-wide default TTL, use the `config.memoryBlockTTL` field in the [Management API](../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-Servers/operation/createAgentMemoryServer). You can also set a TTL for each session or memory block, as described in [Manage TTL](../develop/develop-agent-mem.md#manage-ttl).

## [](#check-status)Step 3: Verify the Deployment

To verify the deployment, go to **AI Data Plane** **Services** **Agent Memory** and see if your server has the `Healthy` status. The list shows the status of each server.

## [](#connect)Step 4: Allow Access and Connect

A new Agent Memory server blocks all requests until you add an allowed IP address. You can add allowed IP addresses only while the server is `Healthy`, and create API keys only after the server has finished deploying.

To allow your agent to connect to your Managed Agent Memory server:

1. [Add an allowed IP address](../api-guide/managed/api-start.md#add-agent-memory-ips) for the machine where your agent runs.
2. [Generate an Agent Memory API key](../api-guide/managed/api-start.md#generate-agent-memory-keys).  
Choose the Write access level for an agent that stores and searches memory.
3. [Copy your Agent Memory server endpoint](../api-guide/managed/api-start.md#copy-agent-memory-endpoint).

### [](#test-connection)Test the Connection

Run the following command from a machine on your server's allowed IP address list:

```console
curl <your-agent-memory-endpoint>/health
```

If the `status` field in the response is `healthy`, your server is reachable from that machine. This check confirms that the server is running and that your IP address is allowed.

> [!TIP]
> The interactive API documentation is available at:
> 
> * Swagger: `<your-agent-memory-endpoint>/docs`
> * Redocly: `<your-agent-memory-endpoint>/redoc`
> 
> You can also browse the same endpoints without a deployment, in the [Agent Memory API Reference](../agent-memory-api-reference/rest-api.md).

## [](#manage)Manage Your Deployment

After your deployment is running, you can monitor it, change its configuration, copy its settings to a new server on another cluster, or delete it.

### [](#monitoring-your-server)Monitoring Your Server

Capella collects metrics from every node in your server and sends alerts through your existing Capella alert integrations. For more information, see [Monitor Managed Agent Memory](monitor-agent-mem-managed.md).

### [](#change-config)Changing Your Configuration

> [!WARNING]
> Replacing a server interrupts your agents' access to Agent Memory. Your agents lose access as soon as you delete the server. They cannot reach Agent Memory again until the new server is healthy, you add its allowed IP addresses, and you update your agents with its endpoint and a new API key.

You cannot change a server's cluster, bucket, models, compute tier, node count, or other settings after you deploy it. To change any of these settings, you must [delete the server](#delete), wait for the deletion to complete, and then [deploy a new server](#deploy).

To keep access to your stored memory, the new server must use:

* The same cluster and bucket as the previous server.
* An embedding model that produces the same number of dimensions as the previous server's model.

To use an embedding model that produces a different number of dimensions, deploy the new server with a different bucket. The new server starts without your stored memory.

### [](#clone)Cloning Your Server

Cloning deploys a new Agent Memory server on another cluster, with the compute tier, node count, and settings of an existing server. You choose the cluster, bucket, and models again. The original server is unaffected and keeps running.

To clone an Agent Memory server:

1. Go to **AI Data Plane** **Services** **Agent Memory**.
2. Next to the server you want to clone, click the **More Options** (⋮) menu.
3. Click **Clone**.
4. In the **New deployment name** field, enter a name for the new server, and click **Continue to review**.
5. In the **Cluster** list, choose the cluster for the new server, and click **Continue**.  
The list shows only clusters that meet the [prerequisites](#prerequisites), and does not include the original server's cluster.
6. Complete the deployment steps in [Step 2: Deploy a Managed Agent Memory Server](#deploy), starting from the bucket.

### [](#delete)Deleting Your Server

When you delete an Agent Memory server, Capella removes its nodes, endpoint, and API keys. Agents that use the server lose access immediately.

Your stored memory stays in the associated operational cluster. If you deploy a new Agent Memory server using the same cluster and bucket, the new server can read the memories the deleted server stored.

To delete a Managed Agent Memory server:

1. Go to **AI Data Plane** **Services** **Agent Memory**.
2. Next to the server you want to delete, click the **More Options** (⋮) menu.
3. Click **Delete**.
4. Enter the name of the server, and click **Delete agent memory**.

## [](#troubleshooting)Troubleshooting

If requests return HTTP `503` with the error code `EMBEDDING_SERVICE_UNAVAILABLE` or `LLM_SERVICE_UNAVAILABLE`

Your Agent Memory server cannot reach 1 of its models. The error code tells you which model:

* `EMBEDDING_SERVICE_UNAVAILABLE`: the embedding model is unreachable. Requests to add, update, or search memory fail.
* `LLM_SERVICE_UNAVAILABLE`: the LLM is unreachable. Requests to add or update memory fail, and search still works.  
In both cases, listing and retrieving existing users, sessions, and memory blocks still works. Check that your OpenAI integrations still exist and that their API keys are valid. If you deleted an integration, [deploy a new server](#change-config) that uses a valid integration.

If your agent receives HTTP `401` with the error code `INVALID_TOKEN`

Your API key is invalid, expired, deleted, or belongs to a different Agent Memory server. Agent Memory returns the same error for every problem with an API key. [Generate a new API key](../api-guide/managed/api-start.md#generate-agent-memory-keys) for this server.

If your agent receives HTTP `503` with the error code `AUTH_UNAVAILABLE`

Agent Memory cannot confirm your API key because of a temporary problem with its authentication service. Retry the request with backoff.

## [](#next-steps)Next Steps

* [Develop with the Agent Memory SDK](../develop/develop-agent-mem.md)
* [Monitor Managed Agent Memory](monitor-agent-mem-managed.md)
* [Control Access to Managed Agent Memory](access-agent-mem-managed.md)
* [Agent Memory APIs for Managed Deployments](../api-guide/managed/api-intro.md)