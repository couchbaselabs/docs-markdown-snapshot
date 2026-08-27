---
title: Agent Memory Environment Variable Reference
description: Reference for environment variables that configure the Agent Memory
  server, organized by functional area.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-memory/config-agent-mem-env.adoc
  xref: xref:ai:build:agent-memory/config-agent-mem-env.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-memory/config-agent-mem-env.html)

# Agent Memory Environment Variable Reference

> Reference for environment variables that configure the Agent Memory server, organized by functional area. 

> [!NOTE]
> For authentication variables, see [Configure Agent Memory Authentication](config-agent-mem-auth.md).

You configure Agent Memory through environment variables, either in a `.env` file passed to the container with `--env-file`, or injected directly into the container environment. Variables set directly in the container environment take precedence over values in the `.env` file.

The distribution includes a `.env-sample` file as a starting template. A minimal deployment requires only the database connection variables and a model provider API key, while everything else has a default or is optional. For a minimal deployment configuration, see [Get Started with Agent Memory](get-started-agent-mem.md).

## [](#database-connection)Database Connection

These variables tell Agent Memory which Couchbase cluster and bucket to use.

> [!TIP]
> For help finding the connection string for your Capella operational database, see [Connect To Your Cluster](../../../cloud/get-started/connect.md).

| Variable                  | Required | Default | Description                                                                                                                                      |
| ------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| AGENTMEMORY\_CONN\_STRING | Yes      | —       | Couchbase connection string. Use couchbase:// for a cluster without TLS, or couchbases:// for a cluster with TLS.                                |
| AGENTMEMORY\_USERNAME     | Yes1     | —       | Username of the Couchbase cluster access credentials.                                                                                            |
| AGENTMEMORY\_PASSWORD     | Yes1     | —       | Password of the Couchbase cluster access credentials.                                                                                            |
| AGENTMEMORY\_BUCKET       | Yes      | —       | Name of the bucket Agent Memory reads from and writes to. The bucket holds the users, sessions, and memory collections in the agentmemory scope. |

1 Username and password are ignored when you authenticate with a client certificate. For more information, see [TLS and mTLS](#tls-mtls).

### [](#tls-mtls)TLS and mTLS

These variables secure the connection between Agent Memory and Couchbase.

| Variable                             | Required | Default | Description                                                                                                    |
| ------------------------------------ | -------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_CONN\_ROOT\_CERTIFICATE | No       | —       | Path inside the container to the cluster's root CA certificate. Required when connecting to Couchbase Capella. |
| AGENTMEMORY\_CONN\_CLIENT\_CERT      | No       | —       | Path to the client certificate for mutual TLS (mTLS).                                                          |
| AGENTMEMORY\_CONN\_CLIENT\_KEY       | No       | —       | Path to the client private key for mutual TLS (mTLS).                                                          |

When you provide a client certificate, `AGENTMEMORY_USERNAME` and `AGENTMEMORY_PASSWORD` are ignored.

> [!WARNING]
> Never use plain text `couchbase://` connections in production. Use `couchbases://` instead, with the appropriate TLS settings.

### [](#write-durability)Write Durability

By default, Agent Memory uses standard writes for memory blocks. Enable durable writes to require the cluster to acknowledge persistence to the active node's disk before confirming each write. For more information, see [Durability](../../../server/current/learn/data/durability.md).

| Variable                     | Required | Default | Description                                                                                                                                                                    |
| ---------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AGENTMEMORY\_DURABLE\_WRITES | No       | false   | Set to true to enable durable writes for memory blocks. Requires at least one replica on the bucket. Do not enable this on a single-node cluster or a bucket with no replicas. |

## [](#model-providers)Model Providers

Agent Memory uses an embedding model and an LLM to power semantic extraction.

### [](#api-keys)API Keys

| Variable         | Required | Default | Description                                                                                                                                                                                                                                                 |
| ---------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAI\_API\_KEY | Yes2     | —       | Default API key for both the embedding and LLM providers. When set, it takes precedence over AGENTMEMORY\_EMBEDDING\_API\_KEY and AGENTMEMORY\_LLM\_API\_KEY. Required unless you set both AGENTMEMORY\_EMBEDDING\_API\_KEY and AGENTMEMORY\_LLM\_API\_KEY. |

2 Not required when both `AGENTMEMORY_EMBEDDING_API_KEY` and `AGENTMEMORY_LLM_API_KEY` are set.

### [](#embedding-model)Embedding Model

The embedding model converts each memory block into a vector for semantic search.

| Variable                         | Required | Default | Description                                                                                                          |
| -------------------------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_EMBEDDING\_MODEL    | Yes      | —       | Name of the embedding model, for example text-embedding-3-small.                                                     |
| AGENTMEMORY\_EMBEDDING\_API\_KEY | No3      | —       | API key for the embedding provider. Used only when OPENAI\_API\_KEY is not set.                                      |
| AGENTMEMORY\_EMBEDDING\_URL      | No       | —       | Base URL of an OpenAI-compatible embedding endpoint. Set this to use a self-hosted model or an alternative provider. |

3 If `OPENAI_API_KEY` is set, this variable is ignored.

> [!IMPORTANT]
> Agent Memory creates a [Search Vector Index](../../../server/current/vector-search/vector-search.md) automatically with a dimensionality matching the embedding model you configure. If you change the embedding model to a model that produces vectors of a different dimensionality, you must recreate the index.

### [](#LLM)Large Language Model

Agent Memory uses an LLM to generate a concise, human-readable summary for each memory block. Summaries let agents quickly interpret search results without reading full block content.

| Variable                           | Required | Default | Description                                                                                                                    |
| ---------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| AGENTMEMORY\_LLM\_MODEL            | Yes      | —       | Name of the LLM, for example gpt-4o-mini.                                                                                      |
| AGENTMEMORY\_LLM\_API\_KEY         | No4      | —       | API key for the LLM provider. Used only when OPENAI\_API\_KEY is not set.                                                      |
| AGENTMEMORY\_LLM\_URL              | No       | —       | Base URL of an OpenAI-compatible LLM endpoint. Set this to use a self-hosted model or an alternative provider.                 |
| AGENTMEMORY\_SUMMARY\_TOKEN\_LIMIT | No       | 700     | Maximum number of tokens in a generated summary. Reduce this to keep summaries shorter and decrease LLM token usage per block. |

4 If `OPENAI_API_KEY` is set, this variable is ignored.

### [](#semantic-extraction)Semantic Extraction

Semantic extraction is the process by which Agent Memory generates an embedding and, when using an [LLM](#LLM), a summary for each ingested memory block. Semantic extraction is enabled by default and is what makes blocks searchable. Without embeddings, semantic search has nothing to query against.

If you turn off semantic extraction, Agent Memory skips all model API calls at ingestion time, making ingestion faster and eliminating model provider costs. However, with no semantic extraction, blocks are stored but you cannot search them. In this situation, you can only retrieve blocks using direct lookup with a known block ID.

Only turn off semantic extraction when:

* You're running a test environment and do not need search.
* Your deployment retrieves blocks by ID rather than through semantic search.

| Variable                             | Required | Default | Description                                                                                                                                                                                                                 |
| ------------------------------------ | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_EXTRACT\_SEMANTIC       | No       | true    | Set to false to turn off semantic extraction. When false, Agent Memory stores blocks but does not generate embeddings or summaries, and semantic search returns no results.                                                 |
| AGENTMEMORY\_PROCESSING\_BATCH\_SIZE | No       | 5       | Number of memory blocks processed per batch during synchronous embedding and fact extraction. Only applies when async\_processing=false. Increase this to raise throughput when your model provider's rate limits allow it. |

## [](#server-settings)Server Settings

These variables control the network interface, port, and thread pool the Agent Memory server uses at runtime.

| Variable                                        | Required | Default | Description                                                                                                                                                                                                                                        |
| ----------------------------------------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_SERVER\_HOST                       | No       | 0.0.0.0 | Address the server binds to.                                                                                                                                                                                                                       |
| AGENTMEMORY\_SERVER\_PORT                       | No       | 8080    | Port the API listens on. This must match the port you publish with \-p and any upstream reverse proxy or load balancer.                                                                                                                            |
| AGENTMEMORY\_THREAD\_POOL\_SIZE                 | No       | 40      | Number of worker threads for synchronous route handlers and the Couchbase SDK. Run a single [Uvicorn](https://www.uvicorn.org/) worker and increase this value instead of adding workers — the async extraction processor must remain a singleton. |
| AGENTMEMORY\_HEALTH\_CACHE\_TTL\_SECONDS        | No       | 60      | Cache TTL, in seconds, for health check results. Set to 0 to disable health caching.                                                                                                                                                               |
| AGENTMEMORY\_HEALTH\_REFRESH\_INTERVAL\_SECONDS | No       | 30      | Interval, in seconds, at which the background health cache is refreshed. Must be less than AGENTMEMORY\_HEALTH\_CACHE\_TTL\_SECONDS.                                                                                                               |

### [](#https)HTTPS

These variables configure TLS for the Agent Memory HTTP listener.

> [!NOTE]
> These variables are intended for development and internal use with self-signed certificates. For production deployments, terminate TLS at a reverse proxy or load balancer instead of configuring it directly on the Agent Memory server. For more information, see [Deploy Agent Memory for Production](deploy-agent-mem-prod.md).

| Variable                            | Required | Default | Description                                                                    |
| ----------------------------------- | -------- | ------- | ------------------------------------------------------------------------------ |
| AGENTMEMORY\_SSL\_CERTFILE          | No       | —       | Path to the TLS certificate file for the HTTP listener.                        |
| AGENTMEMORY\_SSL\_KEYFILE           | No       | —       | Path to the TLS private key file for the HTTP listener.                        |
| AGENTMEMORY\_SSL\_KEYFILE\_PASSWORD | No       | —       | Password for an encrypted TLS private key file.                                |
| AGENTMEMORY\_SSL\_CA\_CERTS         | No       | —       | Path to the CA bundle used by Uvicorn for TLS client certificate verification. |

## [](#memory-retention-and-quotas)Memory Retention and Quotas

These variables control automatic expiry and capacity limits.

> [!TIP]
> TTL is the primary mechanism for privacy compliance and data minimization. Any memory block that contains personally identifiable information should carry a TTL. Use a tiered retention approach:
> 
> Hours to days
> 
> Transient conversational details.
> 
> Weeks to months
> 
> Durable user preferences.
> 
> Indefinite (`0`)
> 
> Anonymized or aggregate facts only.
> 
> A block-level TTL overrides the session default, which overrides the global default set by `AGENTMEMORY_MEMORY_BLOCK_TTL`.

| Variable                                | Required | Default | Description                                                                                                                                                   |
| --------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AGENTMEMORY\_MEMORY\_BLOCK\_TTL         | No       | 0       | Global default time to live, in seconds, applied to memory blocks. 0 means no expiry. A session-level or block-level TTL overrides this value.                |
| AGENTMEMORY\_MEMORY\_QUOTA\_MB          | No       | 512     | Estimated memory budget, in megabytes, used by the memory monitor.                                                                                            |
| AGENTMEMORY\_MEMORY\_THRESHOLD\_PERCENT | No       | 70      | Percentage of the quota at which the memory monitor begins rejecting ingestion requests.                                                                      |
| AGENTMEMORY\_MEMORY\_MONITOR            | No       | false   | Enables the memory monitor. When enabled, Agent Memory tracks estimated usage and rejects ingestion once usage exceeds the threshold percentage of the quota. |
| AGENTMEMORY\_MEMORY\_CHECK\_INTERVAL    | No       | 5.0     | Interval, in seconds, at which the memory monitor samples process memory usage. Only applies when AGENTMEMORY\_MEMORY\_MONITOR is true.                       |

## [](#rate-limiting)Rate Limiting and Throughput

The model provider is almost always the throughput ceiling. Agent Memory and Couchbase can ingest far faster than any hosted model provider allows, so the extraction pipeline is almost always the bottleneck. Increasing server or database resources without raising your model provider tier has no effect on extraction throughput.

When setting limits and monitoring throughput, keep the following in mind:

Match the limits to your provider tier

Agent Memory enforces a requests-per-minute limit and a tokens-per-minute limit against the model provider. Set both to the actual limits shown in your provider's account dashboard:

* Set too high, and the provider returns `429` errors. This reduces throughput as Agent Memory handles this by waiting and retrying.
* Set too low, and provider capacity goes unused.

Use extraction queue depth to find the bottleneck

The extraction queue depth reported by the `/health/async-batch-processor-stats` endpoint is the primary signal to identify a bottleneck in your system:

* A steadily growing queue means extraction is not keeping up with ingestion, so the model provider is the constraint. To improve throughput, upgrade the provider tier or throttle ingestion at the application layer.
* A stable queue near zero means the system is not saturated.

| Variable                                | Required | Default | Description                                                                                                                                                                                                                          |
| --------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AGENTMEMORY\_MAX\_REQUESTS\_PER\_MINUTE | No       | 1500    | Maximum model API requests per minute. Set this to the actual limit shown in your provider's account dashboard.                                                                                                                      |
| AGENTMEMORY\_MAX\_TOKENS\_PER\_MINUTE   | No       | 125000  | Maximum model API tokens per minute. Set this to the actual limit shown in your provider's account dashboard.                                                                                                                        |
| AGENTMEMORY\_MAX\_CONCURRENT\_TASKS     | No       | 100     | Maximum number of concurrent async extraction tasks. A useful starting point is (requests\_per\_minute / 60) × average\_LLM\_latency\_seconds.                                                                                       |
| AGENTMEMORY\_PER\_REQUEST\_TOKEN\_LIMIT | No       | 4096    | Maximum token count for a single memory block. Blocks that exceed this limit are rejected from the extraction queue.                                                                                                                 |
| AGENTMEMORY\_QUEUE\_MAX\_SIZE           | No       | 10000   | Maximum number of blocks that can be queued for async extraction. When the queue is full, Agent Memory returns HTTP 429 with a Retry-After header. If this happens frequently, increase this value or explore other scaling options. |
| AGENTMEMORY\_MAX\_FAIL\_COUNT           | No       | 3       | Number of extraction failures after which a block is marked as permanently failed.                                                                                                                                                   |
| AGENTMEMORY\_TASK\_TIMEOUT\_SECONDS     | No       | 300     | Maximum time, in seconds, that a single async extraction task can run before it is cancelled. Increase this for slow or heavily rate-limited model providers.                                                                        |
| AGENTMEMORY\_IDLE\_SLEEP\_SECONDS       | No       | 0.5     | Sleep duration, in seconds, between async extraction dispatch cycles. Decrease to reduce extraction latency at the cost of higher CPU usage when the queue is idle.                                                                  |

## [](#logging)Logging

For information on how to access log files in a running deployment, see [Viewing Logs](deploy-agent-mem-prod.md#viewing-logs).

| Variable           | Required | Default  | Description                                                                  |
| ------------------ | -------- | -------- | ---------------------------------------------------------------------------- |
| LOG\_LEVEL         | No       | INFO     | Log verbosity level. Accepted values: DEBUG, INFO, WARNING, ERROR, CRITICAL. |
| TIMESTAMPED\_LOGS  | No       | true     | Set to false to use fixed log filenames instead of timestamp-based names.    |
| LOG\_MAX\_BYTES    | No       | 10485760 | Maximum log file size in bytes before rotation. The default is 10 MB.        |
| LOG\_BACKUP\_COUNT | No       | 10       | Number of rotated log files to retain.                                       |

## [](#next-steps)Next Steps

* [Deploy Agent Memory for Production](deploy-agent-mem-prod.md)
* [Configure Agent Memory Authentication](config-agent-mem-auth.md)
* [Develop with the Agent Memory SDK](develop-agent-mem.md)