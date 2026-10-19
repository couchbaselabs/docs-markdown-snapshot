---
title: Get Started with Managed Agent Memory
description: Deploy a Managed Agent Memory server in Capella and store and
  retrieve memory using its Python SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/get-started/pages/get-started-agent-mem-managed.adoc
  xref: xref:agent-mem:get-started:get-started-agent-mem-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/get-started/get-started-agent-mem-managed.html)

# Get Started with Managed Agent Memory

> Deploy a Managed Agent Memory server in Capella and store and retrieve memory using its Python SDK. 

Use this quickstart to get a Managed Agent Memory server running in Capella. Then, write a Python script that stores and retrieves memories.

To run the Agent Memory server on your own infrastructure instead, see [Get Started with Self-Managed Agent Memory](get-started-agent-mem.md).

## [](#prerequisites)Prerequisites

* You have the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role, or the [Project Owner](../../../cloud/projects/project-roles.md#project-owner-role) role in the project where you want to deploy your server.
* You have a healthy operational cluster in Capella that meets all of the following requirements:

  * Runs Couchbase Server 8.0 or later.
  * Runs the Data, Index, Query, and Search services.
  * Runs on AWS in 1 of the following regions:

    * US East (N. Virginia), `us-east-1`
    * Europe (London), `eu-west-2`
  * Does not already have an Agent Memory server.  
For more information about creating a cluster, see [Create A Paid Cluster](../../../cloud/clusters/create-database.md).
* You have a bucket on that cluster for Agent Memory to store its data in. For more information, see [Create a Bucket](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket).
* You have added an OpenAI API key to the AI Data Plane as an integration. For more information, see [Manage AI Integration Settings](../../../ai/admin/manage-ai-integrations.md).
* You have [Python 3.12](https://www.python.org/downloads/) or later installed.

For the full list of requirements, see [Prerequisites](../managed/deploy-agent-mem-managed.md#prerequisites).

## [](#step-1-deploy-your-agent-memory-server)Step 1: Deploy Your Agent Memory Server

This step uses the default settings for your server. For every setting you can choose, see [Deploy Managed Agent Memory](../managed/deploy-agent-mem-managed.md).

To deploy your server:

1. Go to **AI Data Plane** **Services** **Agent Memory**.
2. Click **Deploy Agent Memory**.
3. In the **Cluster** list, choose your cluster, and click **Continue**.
4. In the **Bucket** list, choose the bucket for Agent Memory.
5. Accept the generated name, the default **Small** compute tier, and the default node count. Click **Next**.
6. On the **Models** step, for both the embedding model and the LLM, choose **OpenAI** as the **Model Source**, choose a model, and choose your OpenAI integration.
7. Click **Next**.
8. On the **Advanced** step, accept the default settings, and click **Next**.
9. On the **Review** step, click **Deploy Agent Memory**.
10. Wait until your server has the `Healthy` status in the **AI Data Plane** **Services** **Agent Memory** list.

## [](#step-2-allow-requests-from-your-machine)Step 2: Allow Requests from Your Machine

Your server blocks all requests until you add an allowed IP address.

To allow requests from your development machine:

1. Next to your Agent Memory server, click the **More Options** (⋮) menu.
2. Click **Add Allowed IP**.
3. In the **Select Allowed IP** list, select **Add Current IP Address**.
4. Click **Add Allowed IP Address**.

## [](#step-3-create-an-api-key-and-copy-your-endpoint)Step 3: Create an API Key and Copy Your Endpoint

To get the API key token and endpoint your script needs:

1. Next to your Agent Memory server, click the **More Options** (⋮) menu.
2. Click **Generate API Key**.
3. In the **API Key Name** field, enter a name for the API key.
4. Under **Access**, select **Write**.
5. Click **Generate API Key**.
6. Save the API key token. Click **Download Key** to save it to a file, or copy the **API Key Token** and paste it somewhere. It's required for Step 5.  
> [!WARNING]  
> You cannot copy or download the API key token again after you leave this page.
7. Click **Close**.
8. Click the name of your Agent Memory server.
9. In the **Connect** section, copy the **Endpoint** and save it with your API key token.

For other access levels and expiry options, see [Generate Agent Memory API Keys](../api-guide/managed/api-start.md#generate-agent-memory-keys).

You now have the endpoint and API key token for the script in [Step 5](#store-and-retrieve-memory).

## [](#install-sdk)Step 4: Install the Python SDK

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

## [](#store-and-retrieve-memory)Step 5: Store and Retrieve Memory

You can use the following quickstart example to learn how to store and retrieve memories from Agent Memory:

1. Create a file called `quickstart.py` and add the following code. This code demonstrates creating a user and session, storing memory blocks, and retrieving them by semantic search:  
```python  
from agentmemory import AgentMemoryClient, ChatMessage  
with AgentMemoryClient(base_url="<your-agent-memory-endpoint>", token="<your-api-key-token>") as client:  
    # Create a persistent user identity  
    user = client.create_user(user_id="customer-42", name="Example Customer")  
    print(f"Created user: {user.user_id}")  
    # Open a session — the container for this conversation's memory blocks  
    session = user.create_session(session_id="ticket-4821")  
    print(f"Created session: {session.session_id}")  
    # Store a conversation exchange.  
    # async_processing=False waits for semantic extraction to finish;  
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
> `add_memory()` always generates embeddings before it returns, so stored blocks are searchable as soon as the call completes. `async_processing=False` also makes `add_memory()` wait for semantic extraction to finish, which adds latency per call. In production, use the default `async_processing=True`, which runs extraction in the background.  
> [!NOTE]  
> Replace `<your-agent-memory-endpoint>` with your Agent Memory server endpoint, and `<your-api-key-token>` with your API key token.
2. Run the file:  
```console  
python quickstart.py  
```
3. Review your expected output:  
```none  
Created user: customer-42  
Created session: ticket-4821  
Stored message block(s): ['<block-id-1>']  
Stored fact block(s):    ['<block-id-2>']  
Retrieving memories relevant to 'billing issues'...  
  User:      My payments keep failing at checkout.  
  Assistant: I can help with that. Are you seeing a specific error code?  
  Fact: Customer is on the free tier and has not added a payment method.  
Session ended.  
```  
Agent Memory stored both blocks, generated a vector embedding for each, and returned them based on semantic similarity to the search query. The order of the results can vary.  
> [!NOTE]  
> If you run the script again, `create_user()` raises `ConflictError` because the user already exists. To run it again, change the `user_id` and `session_id` values.

## [](#api-endpoints)Step 6: Explore the API Interactively

Your Agent Memory server serves 2 API explorers. Replace `<your-agent-memory-endpoint>` with your Agent Memory server endpoint in the following URLs:

`<your-agent-memory-endpoint>/docs`

Swagger UI. Try any endpoint directly in the browser, with request and response schemas auto-populated from the OpenAPI spec.

`<your-agent-memory-endpoint>/redoc`

ReDoc. A read-only reference view of the full API spec.

> [!TIP]
> You can also browse the same endpoints without running a server, in the [Agent Memory API Reference](../agent-memory-api-reference/rest-api.md).

## [](#troubleshooting)Troubleshooting

If requests from your machine are blocked

Check that the IP address you're connecting from is on your server's allowed IP address list. For more information, see [Allowed IP Addresses](../api-guide/managed/api-start.md#agent-memory-allowed-ips).

If you receive `AuthenticationError` with the error code `INVALID_TOKEN`

Check that you passed the API key token, not the API key ID, and that the key belongs to this server and has not expired or been deleted.

If you receive `AuthorizationError`

Your API key's access level is too low for the operation. This quickstart needs the Write access level. For more information, see [API Key Access Levels](../managed/access-agent-mem-managed.md#api-key-access-levels-for-memory-access).

For more troubleshooting, see [Troubleshooting](../managed/deploy-agent-mem-managed.md#troubleshooting).

## [](#next-steps)Next Steps

* [Develop with the Agent Memory SDK](../develop/develop-agent-mem.md)
* [Monitor Managed Agent Memory](../managed/monitor-agent-mem-managed.md)
* [Control Access to Managed Agent Memory](../managed/access-agent-mem-managed.md)