---
title: Get Started with Agent Memory
description: Deploy the Couchbase Agent Memory server and store and retrieve
  memory using its Python SDK.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-memory/get-started-agent-mem.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:ai:build:agent-memory/get-started-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-memory/get-started-agent-mem.html)

# Get Started with Agent Memory

> Deploy the Couchbase Agent Memory server and store and retrieve memory using its Python SDK. 

Use this quickstart to get Agent Memory running, and to write a simple Python script that demonstrates how to store and retrieve memories.

> [!NOTE]
> This quickstart is for development and testing purposes only. For production deployment instructions, see [Deploy Agent Memory for Production](deploy-agent-mem-prod.md).

## [](#prerequisites)Prerequisites

* A Couchbase Server Enterprise or Couchbase Capella cluster with the following configuration:

  * Couchbase Server 8.0.2 or later.
  * The following services enabled:

    * [Data Service](../../../server/current/learn/services-and-indexes/services/data-service.md)
    * [Index Service](../../../server/current/learn/services-and-indexes/services/index-service.md)
    * [Query Service](../../../server/current/learn/services-and-indexes/services/query-service.md)
    * [Search Service](../../../server/current/learn/services-and-indexes/services/search-service.md)
  * A bucket created for Agent Memory.
  * Cluster access credentials with read and write permissions on that bucket. For more information, see [Create Cluster Access Credentials](../../../cloud/clusters/manage-database-users.md#create-database-credentials) or [Manage Users and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).
  * Your cluster's connection string. For more information, see [Connect To Your Cluster](../../../cloud/get-started/connect.md).
* You have an API key for an OpenAI-compatible embedding model and large language model (LLM). These can be external or from the [Capella Model Service](../model-service/model-service.md).
* You have [Docker](https://docs.docker.com/engine/install/) installed.
* You have [Python 3.12](https://www.python.org/downloads/) or later installed.

## [](#step-1-deploy-the-agent-memory-server)Step 1: Deploy the Agent Memory Server

To deploy the Agent Memory server on Linux, Intel/AMD, Apple Silicon, or AWS Graviton:

1. Download the artifacts using the time-limited download link provided to you.  
> [!NOTE]  
> The download link expires in 24 hours.
2. Load the Docker image:

  * Intel/AMD (amd64)
  * ARM (arm64)  
Use these commands for most Linux servers and Intel/AMD machines:  
```console  
docker load -i agentmemory-server-amd64-v1.0.0.tar  
```  
Use these commands for Apple Silicon and AWS Graviton instances:  
```console  
docker load -i agentmemory-server-arm64-v1.0.0.tar  
```
3. Create a `.env` file with the following configuration:  
Replace each placeholder with your actual values.  
```bash  
AGENTMEMORY_CONN_STRING=couchbases://your_cluster_host (1)  
AGENTMEMORY_USERNAME=your_username  
AGENTMEMORY_PASSWORD=your_password  
AGENTMEMORY_BUCKET=your_bucket_name  
# AGENTMEMORY_CONN_ROOT_CERTIFICATE=/app/certs/ca.pem (2)  
OPENAI_API_KEY=your_api_key  
AGENTMEMORY_EMBEDDING_MODEL=text-embedding-3-small  
AGENTMEMORY_LLM_MODEL=gpt-4o-mini  
AGENTMEMORY_SERVER_HOST=0.0.0.0  
AGENTMEMORY_SERVER_PORT=8080  
OIDC_AUTH_ENABLED=false  
LOG_LEVEL=INFO  
```

| **1** | Use couchbase:// for clusters without TLS, or couchbases:// for clusters with TLS.                                                                                                                                                                                                                                                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | When connecting to a Capella cluster, you need to use the cluster's root certificate. To use your Capella cluster's certificate, first uncomment this line. Next, [Download the root certificate from the Capella UI](../../../cloud/security/security-certificates.md), rename it to ca.pem, and place it in the same directory as your .env file. The path /app/certs/ca.pem is the location inside the container. |  
> [!TIP]  
> This `.env` file shows only the variables you need for a minimal deployment. For the full list of available variables, see [Agent Memory Environment Variable Reference](config-agent-mem-env.md).
4. Start the server:  
> [!NOTE]  
> If Couchbase Server and Agent Memory are running on the same host, see [connecting to Couchbase Server on the same host](#same-host-conn).

  * Intel/AMD (amd64)
  * ARM (arm64)  
Use these commands for most Linux servers and Intel/AMD machines:  
```console  
docker run -d \
  --name agentmemory-server \
  --platform linux/amd64 \
  --env-file .env \
  -p 8080:8080 \
  -p 9090:9090 \
  -v agentmemory-logs:/app/logs \
  --restart unless-stopped \  
  agentmemory-server:amd64  
```

  * If connecting to a Capella cluster, add `-v $(pwd)/ca.pem:/app/certs/ca.pem:ro` before the image name in the `docker run` command.
  * Port `8080` is the Agent Memory API. For more information, see [API Endpoints](#api-endpoints).
  * Port `9090` is the embedded Prometheus metrics endpoint. If you do not need to scrape Prometheus from outside the host, omit the `-p 9090:9090` flag.  
Use these commands for Apple Silicon and AWS Graviton instances:  
```console  
docker run -d \
  --name agentmemory-server \
  --env-file .env \
  -p 8080:8080 \
  -p 9090:9090 \
  -v agentmemory-logs:/app/logs \
  --restart unless-stopped \  
  agentmemory-server:arm64  
```

  * If connecting to a Capella cluster, add `-v $(pwd)/ca.pem:/app/certs/ca.pem:ro` before the image name in the `docker run` command.
  * Port `8080` is the Agent Memory API. For more information, see [API Endpoints](#api-endpoints).
  * Port `9090` is the embedded Prometheus metrics endpoint. If you do not need to scrape Prometheus from outside the host, omit the `-p 9090:9090` flag.
5. Verify the server is healthy:  
```console  
curl http://localhost:8080/health  
```  
The server is ready when the response includes `"status": "healthy"`.  
If the status is unhealthy, check the logs for more information:  
```console  
docker logs agentmemory-server  
```  
If you encounter issues, see [Troubleshooting](#troubleshooting).

## [](#step-2-install-the-python-sdk)Step 2: Install the Python SDK

To install the Python SDK on the machine where you want to develop with Agent Memory:

1. Create and activate a virtual environment in your project directory:  
```console  
python -m venv .venv  
source .venv/bin/activate  
```  
> [!TIP]  
> You can also use [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or another virtual environment manager.
2. Install the [Agent Memory Python SDK](https://pypi.org/project/couchbase-agent-memory/):  
```console  
python -m pip install --upgrade pip  
python -m pip install couchbase-agent-memory  
```

## [](#step-3-store-and-retrieve-memory)Step 3: Store and Retrieve Memory

You can use the following quickstart example to learn how to store and retrieve memories from Agent Memory:

1. Create a file called `quickstart.py` and add the following code. This code demonstrates creating a user and session, storing memory blocks, and retrieving them by semantic search:  
```python  
from agentmemory import AgentMemoryClient, ChatMessage  
with AgentMemoryClient(base_url="http://localhost:8080") as client:  
    # Create a persistent user identity  
    user = client.create_user(user_id="support-agent-1", name="Support Bot")  
    print(f"Created user: {user.user_id}")  
    # Open a session — the container for this conversation's memory blocks  
    session = user.create_session(session_id="ticket-4821")  
    print(f"Created session: {session.session_id}")  
    # Store a conversation exchange.  
    # async_processing=False blocks until the embedding is generated;  
    # all returned blocks are in ready status on return.  
    r1 = session.add_memory(  
        messages=[  
            ChatMessage(  
                user_content="My payments keep failing at checkout.",  
                assistant_content="I can help with that. Are you seeing a specific error code?",  
            )  
        ],  
        async_processing=False,  
    )  
    print(f"Stored message block(s): {r1.block_ids}")  
    # Store a discrete fact extracted from the conversation  
    r2 = session.add_memory(  
        facts=["Customer is on the free tier and has not added a payment method."],  
        async_processing=False,  
    )  
    print(f"Stored fact block(s):    {r2.block_ids}")  
    # Retrieve memory blocks relevant to a query via semantic search  
    print("\nRetrieving memories relevant to 'billing issues'...")  
    results = session.search_memory(query="billing issues")  
    for block in results.memory_blocks:  
        if block.message:  
            print(f"  User:      {block.message.user_content}")  
            print(f"  Assistant: {block.message.assistant_content}")  
        if block.fact:  
            print(f"  Fact: {block.fact}")  
    session.end()  
    print("Session ended.")  
```  
> [!NOTE]  
> `async_processing=False` makes `add_memory()` wait for embedding generation to complete before returning. This is appropriate for a quickstart, but it adds latency per call. In production, use the default `async_processing=True`, which returns immediately and generates embeddings in the background. Blocks remain searchable only after their status reaches `ready`, which happens within seconds under normal load.  
> [!NOTE]  
> If your server has OIDC authentication enabled, pass your JWT bearer token to the client constructor: `AgentMemoryClient(base_url="http://localhost:8080", token="your-jwt-token")`
2. Run the file:  
```console  
python quickstart.py  
```
3. Review your expected output:  
```none  
Created user: support-agent-1  
Created session: ticket-4821  
Stored message block(s): ['<block-id-1>']  
Stored fact block(s):    ['<block-id-2>']  
Retrieving memories relevant to 'billing issues'...  
  User:      My payments keep failing at checkout.  
  Assistant: I can help with that. Are you seeing a specific error code?  
  Fact: Customer is on the free tier and has not added a payment method.  
Session ended.  
```  
Agent Memory stored both blocks, generated a vector embedding for each, and returned them based on semantic similarity to the search query.

## [](#api-endpoints)Step 4: Explore the API Interactively

Agent Memory serves 2 API explorers at the following URLs with no setup required beyond running the server. If you're running the server on a different host or port, replace `localhost:8080` with your host and port in the URLs below:

`http://localhost:8080/docs`

Swagger UI. Try any endpoint directly in the browser, with request and response schemas auto-populated from the OpenAPI spec.

`http://localhost:8080/redoc`

ReDoc. A read-only reference view of the full API spec.

## [](#troubleshooting)Troubleshooting

If `/health` returns an error

Check `docker logs agentmemory-server` for startup errors. Both the Agent Memory server and Prometheus log to the same stream; lines are prefixed by the process name.

If the Couchbase connection fails

Verify `AGENTMEMORY_CONN_STRING`, `AGENTMEMORY_USERNAME`, `AGENTMEMORY_PASSWORD`, and `AGENTMEMORY_BUCKET`. Check that the Search Service is enabled on the cluster and that the network allows the connection. If using TLS, verify `AGENTMEMORY_CONN_ROOT_CERTIFICATE` is correct.

If model calls fail

Verify `OPENAI_API_KEY`, `AGENTMEMORY_EMBEDDING_MODEL`, and `AGENTMEMORY_LLM_MODEL`.

If port `9090` returns nothing

Confirm you published the port with `-p 9090:9090` and that no other process on the host is already bound to port `9090`.

If Docker reports a platform incompatibility error

Use `agentmemory-server-amd64.tar` for Intel/AMD Linux servers and `agentmemory-server-arm64.tar` for ARM machines.

If Agent Memory cannot connect to Couchbase Server when both are running on the same host

When running Couchbase Server and Agent Memory containers on the same host, such as an EC2 instance, the Agent Memory container cannot reach the Couchbase Server using `couchbase://localhost`. To share the host's network namespace, run Agent Memory with `--network host` and keep the connection string as `couchbase://localhost`.

**Example**: `docker run` with `--network host` (Intel/AMD) 

```console
docker run -d \
  --name agentmemory-server --network host \
  --platform linux/amd64 \
  --env-file .env \
  -v agentmemory-logs:/app/logs \
  -v agentmemory-prometheus:/prometheus-data \
  --restart unless-stopped \
  agentmemory-server:amd64
```

If you're using Docker Desktop on Mac/Windows, you can instead leave the Agent Memory container on its default bridge network and set the connection string to `couchbase://host.docker.internal`. That name is not defined by default on Linux servers, so do not rely on it when using EC2.

## [](#next-steps)Next Steps

* [Develop with the Agent Memory SDK](develop-agent-mem.md)
* [Deploy Agent Memory for Production](deploy-agent-mem-prod.md)