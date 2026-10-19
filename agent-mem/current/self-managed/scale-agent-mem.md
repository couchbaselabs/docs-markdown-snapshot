---
title: Scale Agent Memory Using Multiple Nodes
description: Run several Agent Memory nodes that share a Couchbase bucket, so
  your deployment handles more client traffic and keeps processing memories when
  nodes fail.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/self-managed/pages/scale-agent-mem.adoc
  xref: xref:agent-mem:self-managed:scale-agent-mem.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/self-managed/scale-agent-mem.html)

# Scale Agent Memory Using Multiple Nodes

> Run several Agent Memory nodes that share a Couchbase bucket, so your deployment handles more client traffic and keeps processing memories when nodes fail. 

By default, Agent Memory runs as a single node. Cluster mode lets you run several Agent Memory nodes that share 1 Couchbase bucket. Each node processes the memory blocks it ingests, and if a node stops, the surviving nodes take over any unfinished work. For more information about how nodes share work, recover from failures, and split rate limits, see [Cluster Mode](../about-agent-mem.md#cluster-mode).

To create an Agent Memory cluster, complete the following steps:

1. [Set up the nodes](#set-up-node).
2. [Configure the load balancer](#configure-load-balancer).
3. [Start the cluster](#start-cluster).
4. [Verify the cluster deployment](#verify-cluster).

> [!NOTE]
> Converting or Expanding a Deployment
> 
> * If you're converting an existing deployment to cluster mode, keep it running while you complete [Step 1](#set-up-node) and [Step 2](#configure-load-balancer). Changes to the `.env` and `docker-compose.yml` files you created when you deployed Agent Memory take effect only when you recreate its container in [Step 3](#start-cluster). Plan a maintenance window for Step 3 because clients must stop writing to Agent Memory until the cluster is running.
> * To add capacity to a running Agent Memory cluster, see [Add Nodes to a Cluster](#add-node).

## [](#prerequisites)Prerequisites

Before you start using Agent Memory's cluster mode, confirm the following:

* You have a server for each node, with [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed. The servers share a private network with the load balancer.
* Every node runs the same version of Agent Memory.
* Your Couchbase cluster and bucket are prepared. For more information, see [Prepare Your Couchbase Cluster](deploy-agent-mem-prod.md#step-1).
* You have a load balancer, such as [nginx](https://nginx.org/), that can terminate HTTPS, and a TLS certificate for your domain.
* You know the requests-per-minute and tokens-per-minute limits of your model provider account.

## [](#set-up-node)Step 1: Set Up Nodes

> [!IMPORTANT]
> Set up each node that you need for your cluster, but do not start them until Step 3\.

To set up your nodes, continue from [Step 2 of Deploy Agent Memory for Production](deploy-agent-mem-prod.md#step-2), but make the following changes to the `docker-compose.yml` and `.env` files.

### [](#update-the-docker-compose-yml-file)Update the docker-compose.yml File

Use the following `docker-compose.yml` file. Its `image` value is the pre-built Agent Memory image that you load and tag in Step 2 of Deploy Agent Memory for Production. It has no HTTPS proxy, and it publishes port `8080` only on the server's private address. Replace `<PRIVATE_IP>` with that address.

```yaml
name: agentmemory

services:
  agentmemory-server:
    image: agentmemory-server:latest
    container_name: agentmemory-server
    ports:
      - "<PRIVATE_IP>:8080:8080"
    env_file:
      - .env
    environment:
      - AGENTMEMORY_SERVER_HOST=0.0.0.0
      - AGENTMEMORY_SERVER_PORT=8080
    volumes:
      - agentmemory-logs:/app/logs
      - agentmemory-prometheus:/prometheus-data
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/health').read()"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped

volumes:
  agentmemory-logs:
  agentmemory-prometheus:
```

### [](#update-the-env-file)Update the .env File

In each node's `.env` file, enable cluster mode and set the rate limits for the whole cluster, not a per-node share:

```bash
AGENTMEMORY_CLUSTER_MODE=true
AGENTMEMORY_MAX_REQUESTS_PER_MINUTE=<REQUESTS_PER_MINUTE>
AGENTMEMORY_MAX_TOKENS_PER_MINUTE=<TOKENS_PER_MINUTE>
```

Set these limits to about 90-95% of your model provider's limits. This leaves headroom for brief over-counting when nodes join or leave, and for other usage on the same provider account. Use the same `.env` values on every node for the Couchbase connection, bucket, model providers, rate limits, and cluster mode settings. For more information, see [cluster mode](../reference/config-agent-mem-env.md#cluster-mode) and [Rate Limiting and Throughput](../reference/config-agent-mem-env.md#rate-limiting).

## [](#configure-load-balancer)Step 2: Configure the Load Balancer

A cluster has a load balancer in front of its nodes, and every node connects to the same Couchbase bucket. Clients connect only to the load balancer, and each node runs on its own server without its own HTTPS proxy.

To use Agent Memory's cluster mode, you must configure your load balancer to:

* Terminate HTTPS for your domain.
* Forward requests to port `8080` on each node's private address.
* Stop routing to a node that fails, and send its requests to the other nodes.

Agent Memory does not distribute ingestion or rebalance work between nodes, so distribute requests evenly, for example with round-robin routing. An uneven load balancer leaves some nodes idle while others build a queue.

The following example configures nginx. Replace `<NODE_1_IP>`, `<NODE_2_IP>`, and `<NODE_3_IP>` with each node's private address, `<YOUR_DOMAIN>` with your domain, and `<CERTIFICATE_PATH>` and `<PRIVATE_KEY_PATH>` with the paths to your TLS certificate and private key.

```nginx
upstream agentmemory {
    server <NODE_1_IP>:8080 max_fails=2 fail_timeout=10s;
    server <NODE_2_IP>:8080 max_fails=2 fail_timeout=10s;
    server <NODE_3_IP>:8080 max_fails=2 fail_timeout=10s;
}

server {
    listen 443 ssl;
    server_name <YOUR_DOMAIN>;

    ssl_certificate     <CERTIFICATE_PATH>;
    ssl_certificate_key <PRIVATE_KEY_PATH>;

    location / {
        proxy_pass http://agentmemory;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_read_timeout 300s;
    }
}
```

With this configuration, nginx stops sending requests to a node after 2 failed attempts within 10 seconds, and tries that node again after 10 seconds.

The `proxy_next_upstream` directive retries a failed request on another node. By default, nginx does not resend a request that creates data, such as a `POST` that adds a memory, after it sends the request to a node.

The `proxy_read_timeout` value allows time for synchronous memory processing, which waits for the model provider.

If your load balancer supports active health checks, point them at each node's `/health` endpoint. `/health` only confirms that the server process responds. It does not check the Couchbase connection or the model providers.

## [](#start-cluster)Step 3: Start the Cluster

* New Deployment
* Convert Existing Deployment

Use these steps if you're creating a new Agent Memory deployment that uses cluster mode:

1. Start each node by running the following command in its project directory.  
```console  
docker compose up -d  
```
2. Point your domain at the load balancer.
3. [Verify the cluster deployment](#verify-cluster).

> [!IMPORTANT]
> Do not start any new nodes until you finish draining the backlog. A node that starts without cluster mode re-queues every unfinished block, including blocks the existing node is processing. A node that starts with cluster mode does not count the existing node, so together they exceed your rate limits.

Use the following steps if you're converting an existing Agent Memory deployment to use cluster mode:

1. Drain the extraction backlog of your existing node.  
Blocks ingested before you enable cluster mode are not owned by any node in the cluster. If they're still waiting for extraction, cluster mode never recovers them.

  1. Stop sending new writes to Agent Memory, for example by pausing your clients.
  2. Keep the existing node running in single-node mode until both `size` and `processing` in the `queue` object are `0`:  
  ```console  
  curl -s https://$YOUR_DOMAIN/health/async-batch-processor-stats | jq '.queue'  
  ```  
  If you have enabled authentication, add `-H "Authorization: Bearer $TOKEN"` with a token that carries the [ams\_ro role](../about-agent-mem.md#authorization) or higher. For more information about getting a token, see [Configure Authentication for Self-Managed Agent Memory](../security/config-agent-mem-auth.md).
  3. Confirm that no unprocessed blocks remain in Couchbase. Run the following SQL++ query in the [Capella Query Workbench](../../../cloud/clusters/query-service/query-workbench.md), the [Couchbase Server Query Workbench](../../../server/current/tools/query-workbench.md), or the [cbq shell](../../../server/current/cli/cbq-tool.md), with credentials that can read the bucket:  
  ```sqlpp  
  SELECT COUNT(*) AS pending  
  FROM `<BUCKET_NAME>`.agentmemory.memory  
  WHERE status != 'ready'  
    AND IFMISSINGORNULL(fail_count, 0) < 3;  
  ```  
  > [!NOTE]  
  > If you changed [AGENTMEMORY\_MAX\_FAIL\_COUNT](../reference/config-agent-mem-env.md#max-fail-count) from its default of `3`, use your value instead.  
  The query returns `0` when the backlog is drained. If the query returns a number greater than `0` while the queue is empty, restart the node with `docker restart agentmemory-server` to re-queue the remaining blocks. Wait until `size` and `processing` in the `queue` object are `0` again, then rerun the query. `docker restart` keeps the node's current configuration, so the node stays reachable at your domain.
2. Point your domain at the load balancer.
3. Restart the existing node and start each new node using the following commands in each node's project directory:  
```console  
docker compose down --remove-orphans && docker compose up -d  
```  
The `--remove-orphans` option removes containers that are no longer in the `docker-compose.yml` file, such as a Traefik or nginx proxy. If you used Cloudflare Tunnel, also stop the `cloudflared` tunnel on the server.
4. [Verify the cluster deployment](#verify-cluster), then resume your clients.

## [](#verify-cluster)Step 4: Verify the Cluster Deployment

To verify that a cluster is operating, wait 30 seconds after the last node starts, then run the following command on each node's host. If your container is not named `agentmemory-server`, replace it with your container name.

```console
docker exec agentmemory-server python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8080/metrics').read().decode())" | grep '^agentmemory_cluster_live_node_count'
```

The output shows the number of nodes you started, for example `agentmemory_cluster_live_node_count 3.0` for a 3-node cluster. If this reports a lower number than you're expecting, see [Troubleshooting](#troubleshooting).

## [](#add-node)Add Nodes to a Cluster

You can add a node to a running cluster without restarting the other nodes.

1. Set up the node, as described in [Step 1: Set Up Nodes](#set-up-node), with the same `.env` values as the other nodes, including `AGENTMEMORY_CLUSTER_MODE=true`.
2. Start the node by running `docker compose up -d` in its project directory.
3. Add the node's private address to your load balancer, and reload the load balancer's configuration.
4. If you scrape metrics with an external Prometheus server, add the node to its [scrape configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape%5Fconfig).
5. Verify the cluster. For more information, see [Step 4: Verify the Cluster Deployment](#verify-cluster).

## [](#monitor-node)Monitor a Cluster

Each node's embedded Prometheus instance collects metrics only from that node. To view the whole cluster in a single place, use an external Prometheus server.

1. Add the `/metrics` endpoint of every node to your Prometheus server's [scrape configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape%5Fconfig). Use each node's private address, and run Prometheus on the same private network.  
```yaml  
scrape_configs:
  - job_name: agentmemory  
    metrics_path: /metrics  
    static_configs:
      - targets:
          - <NODE_1_IP>:8080
          - <NODE_2_IP>:8080
          - <NODE_3_IP>:8080  
```
2. Confirm that Prometheus reaches every node.  
```console  
curl -s "http://$PROMETHEUS_HOST:9090/api/v1/targets?state=active" | jq -r '.data.activeTargets[] | "\(.labels.instance) \(.health)"'  
```  
Each node appears with the health `up`.
3. To tell nodes apart in queries, join a metric to `agentmemory_node_info` on the `instance` label. For example, the following query shows the live node count that each node reports, labeled with its node ID:  
```promql  
agentmemory_cluster_live_node_count * on(instance) group_left(node_id) agentmemory_node_info  
```

Agent Memory exposes metrics for heartbeats, dead-node recovery, and each node's rate limit share. Use them to build dashboards and alerts for the cluster.

For all of the cluster mode metrics that are available, expand the following section:

Show All Cluster Mode Metrics 

| Metric                                                  | Type    | Description                                                                                                                  |
| ------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| agentmemory\_cluster\_live\_node\_count                 | Gauge   | Number of live nodes as seen by this node.                                                                                   |
| agentmemory\_cluster\_per\_node\_rpm                    | Gauge   | This node's share of AGENTMEMORY\_MAX\_REQUESTS\_PER\_MINUTE.                                                                |
| agentmemory\_node\_info                                 | Gauge   | Carries this node's ID in the node\_id label. The value is always 1.                                                         |
| agentmemory\_heartbeat\_total                           | Counter | Heartbeat attempts, labeled by result: success, cas\_mismatch, or error.                                                     |
| agentmemory\_zombie\_detected\_total                    | Counter | Times this node found that a peer had claimed it and shut itself down.                                                       |
| agentmemory\_recovery\_sweep\_total                     | Counter | Dead-node recovery sweeps this node has run.                                                                                 |
| agentmemory\_recovery\_sweep\_dead\_nodes\_found\_total | Counter | Dead nodes found across all sweeps.                                                                                          |
| agentmemory\_recovery\_sweep\_claim\_total              | Counter | Attempts to claim a dead node, labeled by result: success, lost\_race, no\_blocks, enqueue\_failed, or skipped\_full\_queue. |
| agentmemory\_recovery\_sweep\_blocks\_recovered\_total  | Counter | Blocks this node took over from dead nodes.                                                                                  |
| agentmemory\_own\_lineage\_recovery\_total              | Counter | Recovery passes over this node's own unfinished blocks, labeled by result: work\_done, nothing, or skipped\_full\_queue.     |
| agentmemory\_own\_lineage\_blocks\_recovered\_total     | Counter | Blocks re-queued by those recovery passes.                                                                                   |
| agentmemory\_startup\_own\_blocks\_recovered\_total     | Counter | Blocks this node recovered at startup.                                                                                       |

In cluster mode, `agentmemory_health_check_status{component="couchbase"}` reflects heartbeat success. `agentmemory_async_batch_process_outcomes_total` reports `result="lease_expired"` when a node discards an extraction result after it loses contact with Couchbase.

### [](#collect-cluster-diagnostics)Collect Diagnostics from a Cluster

To collect support diagnostics from every node in a single archive, use `agentmemory-collect`:

1. On a chosen node's host, run `agentmemory-collect` and pass the node URLs with `--nodes`.  
```console  
docker exec agentmemory-server agentmemory-collect \
  --customer $CUSTOMER_NAME \
  --ticket-id $TICKET_ID \
  --nodes http://$NODE_1_IP:8080,http://$NODE_2_IP:8080,http://$NODE_3_IP:8080  
```  
The command uploads the archive to Couchbase Support, so you need an open support ticket. Replace the following placeholders.

  * `$CUSTOMER_NAME`: Your company name, using up to 50 letters, numbers, underscores, periods, or hyphens.
  * `$TICKET_ID`: Your Couchbase Support ticket number, up to 7 digits.
  * `$NODE_1_IP`, `$NODE_2_IP`, and `$NODE_3_IP`: Each node's private address.  
  If you have enabled authentication, add `--auth-token` with a token that each node accepts. If you have also enabled authorization, the token must carry the [ams\_admin role](../about-agent-mem.md#authorization).
2. Check the command output for errors.  
The archive leaves out any node that the command cannot reach, and the output shows `Collected <URL>: error` for that node.

For more information, see [Collecting Support Diagnostics](deploy-agent-mem-prod.md#collecting-support-diagnostics).

## [](#troubleshooting)Troubleshooting

If a node reports fewer live nodes than you started

Confirm that every node registered with the cluster by running the following command in each node's project directory.

```console
docker compose logs agentmemory-server | grep "Node document written"
```

This log entry requires `LOG_LEVEL` set to `INFO` or `DEBUG`. `INFO` is the default. A node that does not show this log entry did not register. Check its `AGENTMEMORY_CLUSTER_MODE` value and its Couchbase connection settings.

## [](#next-steps)Next Steps

* [Self-Managed Agent Memory Environment Variable Reference](../reference/config-agent-mem-env.md)
* [Deploy Self-Managed Agent Memory for Production](deploy-agent-mem-prod.md)
* [Develop with the Agent Memory SDK](../develop/develop-agent-mem.md)