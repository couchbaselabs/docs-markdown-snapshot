---
title: Deploy Agent Memory for Production
description: Deploy the Agent Memory server to a Linux server with HTTPS, Docker
  Compose, and persistent storage.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-memory/deploy-agent-mem-prod.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:ai:build:agent-memory/deploy-agent-mem-prod.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-memory/deploy-agent-mem-prod.html)

# Deploy Agent Memory for Production

> Deploy the Agent Memory server to a Linux server with HTTPS, Docker Compose, and persistent storage. 

This guide deploys Agent Memory using Docker Compose with 1 of 4 HTTPS methods to a Linux server. For local development and testing, see [Get Started with Agent Memory](get-started-agent-mem.md). If you have already completed the quickstart, you can proceed from [Step 2](#step-2).

Agent Memory is a stateless server and holds no durable data of its own. Instead, all memory data lives in a Couchbase cluster. You can stop, restart, or replace the Agent Memory container without losing data. Because of this, your cluster's availability is a key factor in the service's availability.

## [](#prerequisites)Prerequisites

* A Linux server instance, for example an EC2, GCP, DigitalOcean, or Azure VM instance.
* [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on the server.
* A Couchbase Capella or Couchbase Server Enterprise cluster with the following configuration:

  * Couchbase Server 8.0.2 or later.
  * The following services enabled:

    * [Data Service](../../../server/current/learn/services-and-indexes/services/data-service.md)
    * [Index Service](../../../server/current/learn/services-and-indexes/services/index-service.md)
    * [Query Service](../../../server/current/learn/services-and-indexes/services/query-service.md)
    * [Search Service](../../../server/current/learn/services-and-indexes/services/search-service.md)
  * Cluster access credentials with read and write permissions on that bucket. For more information, see [Create Cluster Access Credentials](../../../cloud/clusters/manage-database-users.md#create-database-credentials) or [Manage Users and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).
  * Your cluster's connection string. For more information, see [Connect To Your Cluster](../../../cloud/get-started/connect.md).
* An API key for an OpenAI-compatible embedding model and large language model (LLM). These can be external or from the [Capella Model Service](../model-service/model-service.md).
* The unique download URL from your Agent Memory access approval email.
* For [Traefik](https://traefik.io/traefik/) deployments: a domain name pointing to your server's public IP, ports `80` and `443` open in your firewall or security group, and a valid email address for Let's Encrypt registration.
* For Cloudflare Tunnel deployments: a [Cloudflare](https://www.cloudflare.com/) account.

## [](#step-1-prepare-your-couchbase-cluster)Step 1: Prepare Your Couchbase Cluster

Before starting the server, create a dedicated bucket in your Couchbase cluster for Agent Memory. For production, pre-create a vector index with settings matched to your workload.

### [](#bucket)Bucket

A single Agent Memory server connects to 1 bucket. Multiple deployments of Agent Memory can connect to the same cluster, but each deployment must have its own bucket to avoid data collisions.

Create a dedicated bucket for each deployment of Agent Memory. Agent Memory stores all data for users, sessions, and memories in that bucket, in the `agentmemory` scope and its `users`, `sessions`, and `memory` collections.

For details on creating a bucket, see:

* [Create a Bucket](../../../server/current/manage/manage-buckets/create-bucket.md) for Couchbase Server.
* [Create a Bucket](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket) for Couchbase Capella.

### [](#vector-index)Vector Index

While Agent Memory creates a Search Vector Index automatically on startup if it does not already exist, you should pre-create the index in production to optimize it for your workload.

The index's vector dimension must match the output dimension of your embedding model. For example, `text-embedding-3-small` produces 1536 dimensional vectors by default, so you must configure the index for 1536 dimensions. A mismatch causes semantic search to fail or return no results.

When pre-creating the index, target the `agentmemory` scope and the `memory` collection inside your bucket: `<bucket>.agentmemory.memory`.

For details on creating a Search Vector Index, see:

* [Vector Search Using Search Vector Indexes](../../../server/current/vector-search/vector-search.md) for Couchbase Server
* [Vector Search Using Search Vector Indexes](../../../cloud/vector-search/vector-search.md) for Couchbase Capella.

## [](#step-2)Step 2: Download and Load the Agent Memory Image

1. In your Agent Memory access approval email, locate your unique download URL.
2. Use curl to download the file to your server.  
> [!NOTE]  
> The download includes the Agent Memory server image only. Install the Python SDK separately with `pip install couchbase-agent-memory`. For more information, see [Get Started with Agent Memory](get-started-agent-mem.md).
3. Load the Docker image:  
```console  
docker load -i agentmemory-server-<arch>-<version>.tar  
```
4. Tag the image as `latest` so it matches the image name used in the Docker Compose files:  
```console  
docker tag agentmemory-server:<arch>-<version> agentmemory-server:latest  
```

## [](#step-3-create-a-project-directory)Step 3: Create a Project Directory

On your server, create a project directory for your deployment and navigate into it:

```console
mkdir ~/agentmemory-deploy && cd ~/agentmemory-deploy
```

## [](#step-4-configure-and-deploy)Step 4: Configure and Deploy

Choose the HTTPS method that best fits your infrastructure, then follow the tab for that method.

> [!TIP]
> Not sure which method to choose?
> 
> Use the following table to compare some common HTTPS methods:
> 
> Show table 
> 
> | Method                  | Best for                                                       | Complexity | Auto SSL Renewal |
> | ----------------------- | -------------------------------------------------------------- | ---------- | ---------------- |
> | Traefik + Let's Encrypt | Production with a domain name                                  | Low        | Yes              |
> | Cloudflare Tunnel       | Quick setup, or servers behind firewalls with no inbound ports | Very low   | Yes              |
> | Uvicorn SSL             | Internal deployments or custom certificate authorities         | Low        | Manual           |
> | Nginx Reverse Proxy     | Environments with existing nginx infrastructure                | Medium     | Manual           |

> [!TIP]
> Each `.env` file shown below includes only the variables you need for that deployment method. For the full list of available variables, see [Agent Memory Environment Variable Reference](config-agent-mem-env.md).

* Traefik + Let's Encrypt
* Cloudflare Tunnel
* Uvicorn SSL
* Nginx Reverse Proxy

Traefik acts as a reverse proxy that terminates TLS and automatically obtains and renews SSL certificates from Let's Encrypt. Agent Memory runs on the internal Docker network with no direct Internet exposure. The configuration below uses the HTTP challenge. For DNS challenge or wildcard certificates, see the [Traefik ACME documentation](https://doc.traefik.io/traefik/https/acme/).

1. Create a `docker-compose.yml` file:  
```yaml  
name: agentmemory  
services:  
  traefik:  
    image: traefik:v3.2  
    container_name: traefik  
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--providers.docker.network=agentmemory-network"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.web.http.redirections.entrypoint.to=websecure"
      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web"
      - "--certificatesresolvers.letsencrypt.acme.email=${ACME_EMAIL}"
      - "--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json"
      - "--log.level=INFO"  
    ports:
      - "80:80"
      - "443:443"  
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - letsencrypt:/letsencrypt  
    restart: unless-stopped  
    networks:
      - agentmemory-network  
  agentmemory-server:  
    image: agentmemory-server:latest  
    container_name: agentmemory-server  
    env_file:
      - .env  
    environment:
      - AGENTMEMORY_SERVER_HOST=0.0.0.0
      - AGENTMEMORY_SERVER_PORT=8080  
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.agentmemory.rule=Host(`${DOMAIN}`)"
      - "traefik.http.routers.agentmemory.entrypoints=websecure"
      - "traefik.http.routers.agentmemory.tls.certresolver=letsencrypt"
      - "traefik.http.routers.agentmemory.service=agentmemory"
      - "traefik.http.services.agentmemory.loadbalancer.server.port=8080"
      - "traefik.http.services.agentmemory.loadbalancer.healthcheck.path=/health"
      - "traefik.http.services.agentmemory.loadbalancer.healthcheck.interval=30s"  
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
    networks:
      - agentmemory-network  
networks:  
  agentmemory-network:  
    driver: bridge  
volumes:  
  agentmemory-logs:  
  agentmemory-prometheus:  
  letsencrypt:  
```
2. Create a `.env` file in the project directory. Replace each placeholder with your actual values:  
```bash  
# HTTPS configuration  
DOMAIN=api.example.com (1)  
ACME_EMAIL=admin@example.com (2)  
# Couchbase configuration  
AGENTMEMORY_CONN_STRING=couchbases://your_cluster_host (3)  
AGENTMEMORY_USERNAME=your_username  
AGENTMEMORY_PASSWORD=your_password  
AGENTMEMORY_BUCKET=your_bucket_name  
# AGENTMEMORY_CONN_ROOT_CERTIFICATE=/app/certs/ca.pem (4)  
# Model configuration  
OPENAI_API_KEY=your_api_key  
AGENTMEMORY_EMBEDDING_MODEL=text-embedding-3-small  
AGENTMEMORY_LLM_MODEL=gpt-4o-mini  
# AGENTMEMORY_EMBEDDING_URL=your_embedding_endpoint (5)  
# AGENTMEMORY_LLM_URL=your_llm_endpoint (5)  
# Server configuration  
LOG_LEVEL=INFO  
OIDC_AUTH_ENABLED=false (6)  
```

| **1** | Your domain name, for example api.example.com.                                                                                                                                                                                                                                                        |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | A valid email address for Let's Encrypt certificate registration.                                                                                                                                                                                                                                     |
| **3** | Use couchbase:// for clusters without TLS, or couchbases:// for clusters with TLS.                                                                                                                                                                                                                    |
| **4** | Required for Capella clusters. [Download the root certificate from the Capella UI](../../../cloud/security/security-certificates.md), rename it to ca.pem, place it in your project directory, and add \- $(pwd)/ca.pem:/app/certs/ca.pem:ro to the agentmemory-server volumes in docker-compose.yml. |
| **5** | Required when using a non-OpenAI-compatible endpoint, such as the [Capella Model Service](../model-service/model-service.md). Set both variables to the base URL of your inference provider.                                                                                                          |
| **6** | Set to true and complete [Configure Agent Memory Authentication](config-agent-mem-auth.md) to secure your deployment with OIDC authentication.                                                                                                                                                        |
3. Deploy the containers:  
```console  
docker compose up -d  
```

Cloudflare Tunnel provides HTTPS without opening inbound ports or managing certificates. A named tunnel with your own domain requires a Cloudflare account.

1. Install `cloudflared` on your server following the [official installation instructions](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) for your OS and architecture.
2. Create a `docker-compose.yml` file:  
```yaml  
name: agentmemory  
services:  
  agentmemory-server:  
    image: agentmemory-server:latest  
    container_name: agentmemory-server  
    ports:
      - "127.0.0.1:8080:8080"  
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
3. Create a `.env` file in the project directory. Replace each placeholder with your actual values:  
```bash  
# Couchbase configuration  
AGENTMEMORY_CONN_STRING=couchbases://your_cluster_host (1)  
AGENTMEMORY_USERNAME=your_username  
AGENTMEMORY_PASSWORD=your_password  
AGENTMEMORY_BUCKET=your_bucket_name  
# AGENTMEMORY_CONN_ROOT_CERTIFICATE=/app/certs/ca.pem (2)  
# Model configuration  
OPENAI_API_KEY=your_api_key  
AGENTMEMORY_EMBEDDING_MODEL=text-embedding-3-small  
AGENTMEMORY_LLM_MODEL=gpt-4o-mini  
# AGENTMEMORY_EMBEDDING_URL=your_embedding_endpoint (3)  
# AGENTMEMORY_LLM_URL=your_llm_endpoint (3)  
# Server configuration  
LOG_LEVEL=INFO  
OIDC_AUTH_ENABLED=false (4)  
```

| **1** | Use couchbase:// for clusters without TLS, or couchbases:// for clusters with TLS.                                                                                                                                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Required for Capella clusters. [Download the root certificate from the Capella UI](../../../cloud/security/security-certificates.md), rename it to ca.pem, place it in your project directory, and add \- $(pwd)/ca.pem:/app/certs/ca.pem:ro to the agentmemory-server volumes in docker-compose.yml. |
| **3** | Required when using a non-OpenAI-compatible endpoint, such as the [Capella Model Service](../model-service/model-service.md). Set both variables to the base URL of your inference provider.                                                                                                          |
| **4** | Set to true and complete [Configure Agent Memory Authentication](config-agent-mem-auth.md) to secure your deployment with OIDC authentication.                                                                                                                                                        |
4. Deploy the container:  
```console  
docker compose up -d  
```
5. Create a named tunnel, route your domain to it, and start the tunnel. For full instructions, see [Create a remotely-managed tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/) in the Cloudflare documentation.  
```console  
cloudflared tunnel login  
cloudflared tunnel create agentmemory  
cloudflared tunnel route dns agentmemory api.yourdomain.com  
cloudflared tunnel run --url http://localhost:8080 agentmemory  
```
6. Install `cloudflared` as a system service so the tunnel starts on boot:  
```console  
sudo cloudflared service install  
sudo systemctl enable --now cloudflared  
```

Use this option for internal deployments or environments with a custom certificate authority. Agent Memory handles TLS termination directly.

> [!IMPORTANT]
> Certificates and private keys mounted into the container must be readable by UID `65532`, the non-root user the hardened runtime runs as. Run `ls -ln certs/key.pem` to verify ownership before deploying.

1. Place your SSL certificate and private key in a `certs/` subdirectory and set ownership:  
```console  
mkdir -p certs  
sudo chown -R 65532:65532 certs/  
```
2. Create a `docker-compose.yml` file:  
```yaml  
name: agentmemory  
services:  
  agentmemory-server:  
    image: agentmemory-server:latest  
    container_name: agentmemory-server  
    ports:
      - "443:8080"  
    env_file:
      - .env  
    environment:
      - AGENTMEMORY_SERVER_HOST=0.0.0.0
      - AGENTMEMORY_SERVER_PORT=8080
      - AGENTMEMORY_SSL_CERTFILE=/app/certs/cert.pem
      - AGENTMEMORY_SSL_KEYFILE=/app/certs/key.pem  
    volumes:
      - agentmemory-logs:/app/logs
      - agentmemory-prometheus:/prometheus-data
      - ./certs:/app/certs:ro  
    healthcheck:  
      test: ["CMD", "python", "-c", "import ssl, urllib.request; urllib.request.urlopen('https://localhost:8080/health', context=ssl._create_unverified_context()).read()"]  
      interval: 30s  
      timeout: 10s  
      retries: 3  
      start_period: 40s  
    restart: unless-stopped  
volumes:  
  agentmemory-logs:  
  agentmemory-prometheus:  
```
3. Create a `.env` file in the project directory. Replace each placeholder with your actual values:  
```bash  
# Couchbase configuration  
AGENTMEMORY_CONN_STRING=couchbases://your_cluster_host (1)  
AGENTMEMORY_USERNAME=your_username  
AGENTMEMORY_PASSWORD=your_password  
AGENTMEMORY_BUCKET=your_bucket_name  
# AGENTMEMORY_CONN_ROOT_CERTIFICATE=/app/certs/ca.pem (2)  
# Model configuration  
OPENAI_API_KEY=your_api_key  
AGENTMEMORY_EMBEDDING_MODEL=text-embedding-3-small  
AGENTMEMORY_LLM_MODEL=gpt-4o-mini  
# AGENTMEMORY_EMBEDDING_URL=your_embedding_endpoint (3)  
# AGENTMEMORY_LLM_URL=your_llm_endpoint (3)  
# Server configuration  
LOG_LEVEL=INFO  
OIDC_AUTH_ENABLED=false (4)  
```

| **1** | Use couchbase:// for clusters without TLS, or couchbases:// for clusters with TLS.                                                                                                                                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Required for Capella clusters. [Download the root certificate from the Capella UI](../../../cloud/security/security-certificates.md), rename it to ca.pem, place it in your project directory, and add \- $(pwd)/ca.pem:/app/certs/ca.pem:ro to the agentmemory-server volumes in docker-compose.yml. |
| **3** | Required when using a non-OpenAI-compatible endpoint, such as the [Capella Model Service](../model-service/model-service.md). Set both variables to the base URL of your inference provider.                                                                                                          |
| **4** | Set to true and complete [Configure Agent Memory Authentication](config-agent-mem-auth.md) to secure your deployment with OIDC authentication.                                                                                                                                                        |
4. Deploy the container:  
```console  
docker compose up -d  
```

Use this option if you have existing nginx infrastructure.

1. Place your SSL certificate and private key in a `certs/` subdirectory.
2. Create an `nginx.conf` file:  
```nginx  
events {  
    worker_connections 1024;  
}  
http {  
    server {  
        listen 80;  
        server_name api.example.com;  
        return 301 https://$server_name$request_uri;  
    }  
    server {  
        listen 443 ssl http2;  
        server_name api.example.com;  
        ssl_certificate /etc/nginx/certs/cert.pem;  
        ssl_certificate_key /etc/nginx/certs/key.pem;  
        ssl_protocols TLSv1.2 TLSv1.3;  
        ssl_prefer_server_ciphers off;  
        ssl_session_cache shared:SSL:10m;  
        # For a hardened cipher list, see https://ssl-config.mozilla.org/  
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;  
        add_header X-Frame-Options DENY;  
        add_header X-Content-Type-Options nosniff;  
        location / {  
            proxy_pass http://agentmemory-server:8080;  
            proxy_http_version 1.1;  
            proxy_set_header Host $host;  
            proxy_set_header X-Real-IP $remote_addr;  
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
            proxy_set_header X-Forwarded-Proto $scheme;  
        }  
    }  
}  
```
3. Create a `docker-compose.yml` file:  
```yaml  
name: agentmemory  
services:  
  nginx:  
    image: nginx:alpine  
    container_name: nginx-proxy  
    ports:
      - "80:80"
      - "443:443"  
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro  
    depends_on:
      - agentmemory-server  
    restart: unless-stopped  
    networks:
      - agentmemory-network  
  agentmemory-server:  
    image: agentmemory-server:latest  
    container_name: agentmemory-server  
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
    networks:
      - agentmemory-network  
networks:  
  agentmemory-network:  
    driver: bridge  
volumes:  
  agentmemory-logs:  
  agentmemory-prometheus:  
```
4. Create a `.env` file in the project directory. Replace each placeholder with your actual values:  
```bash  
# Couchbase configuration  
AGENTMEMORY_CONN_STRING=couchbases://your_cluster_host (1)  
AGENTMEMORY_USERNAME=your_username  
AGENTMEMORY_PASSWORD=your_password  
AGENTMEMORY_BUCKET=your_bucket_name  
# AGENTMEMORY_CONN_ROOT_CERTIFICATE=/app/certs/ca.pem (2)  
# Model configuration  
OPENAI_API_KEY=your_api_key  
AGENTMEMORY_EMBEDDING_MODEL=text-embedding-3-small  
AGENTMEMORY_LLM_MODEL=gpt-4o-mini  
# AGENTMEMORY_EMBEDDING_URL=your_embedding_endpoint (3)  
# AGENTMEMORY_LLM_URL=your_llm_endpoint (3)  
# Server configuration  
LOG_LEVEL=INFO  
OIDC_AUTH_ENABLED=false (4)  
```

| **1** | Use couchbase:// for clusters without TLS, or couchbases:// for clusters with TLS.                                                                                                                                                                                                                    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Required for Capella clusters. [Download the root certificate from the Capella UI](../../../cloud/security/security-certificates.md), rename it to ca.pem, place it in your project directory, and add \- $(pwd)/ca.pem:/app/certs/ca.pem:ro to the agentmemory-server volumes in docker-compose.yml. |
| **3** | Required when using a non-OpenAI-compatible endpoint, such as the [Capella Model Service](../model-service/model-service.md). Set both variables to the base URL of your inference provider.                                                                                                          |
| **4** | Set to true and complete [Configure Agent Memory Authentication](config-agent-mem-auth.md) to secure your deployment with OIDC authentication.                                                                                                                                                        |
5. Deploy the containers:  
```console  
docker compose up -d  
```

## [](#step-5-verify-the-deployment)Step 5: Verify the Deployment

Run the following commands to verify that the containers are running and the server is healthy:

```console
docker compose ps
curl https://<YOUR_DOMAIN>/health
```

The server is ready when the response includes `"status": "healthy"`. If you're using a self-signed or internal CA certificate (Uvicorn SSL), add `-k` to skip certificate verification. If you're using Traefik, wait 30—​60 seconds for the SSL certificate to be issued before verifying. If the certificate is not issued, see [Troubleshooting](#troubleshooting).

> [!TIP]
> The interactive API documentation is available at:
> 
> * Swagger: `https://<YOUR_DOMAIN>/docs`
> * Redocly: `https://<YOUR_DOMAIN>/redoc`

## [](#manage-your-deployment)Manage Your Deployment

After your deployment is running, you can view logs, monitor Prometheus metrics, apply configuration changes, and collect diagnostics for Couchbase Support.

### [](#viewing-logs)Viewing Logs

Agent Memory and its embedded Prometheus instance log to the same output stream, with each line prefixed by the process name.

To stream live logs:

```console
docker compose logs -f agentmemory-server
```

To export the full log tree to the host:

```console
docker cp agentmemory-server:/app/logs ./logs
```

To write logs directly to the host filesystem for an external log shipper, replace `agentmemory-logs:/app/logs` with `./logs:/app/logs` in `docker-compose.yml`, and prepare the host directory first:

```console
mkdir -p logs
sudo chown -R 65532:65532 logs
```

### [](#prometheus-metrics)Prometheus Metrics

Agent Memory includes an embedded Prometheus instance that scrapes its own `/metrics` endpoint on loopback. The `agentmemory-prometheus` volume persists the Prometheus time-series database across container restarts. Without this, you would lose metrics history when you recreate or update the container.

> [!CAUTION]
> Do not expose port `9090` to the public Internet without an authentication layer. To [federate](https://prometheus.io/docs/prometheus/latest/federation/) metrics from an external Prometheus, reach the endpoint over a private network.

### [](#applying-configuration-changes)Applying Configuration Changes

To apply changes to your `.env` file, restart the containers:

```console
docker compose down && docker compose up -d
```

On restart, Agent Memory automatically re-queues any memory blocks that were mid-extraction when you stopped the previous instance. This crash recovery consumes queue capacity and can trigger HTTP `429` responses if the backlog is large.

### [](#collecting-support-diagnostics)Collecting Support Diagnostics

The `agentmemory-collect` tool collects Agent Memory logs, system diagnostics, and Prometheus metrics from inside the container and uploads them to Couchbase Support:

```console
docker exec agentmemory-server agentmemory-collect --customer your-company --ticket-id 12345
```

To restrict the collection to a specific time range:

```console
docker exec agentmemory-server agentmemory-collect \
  --customer your-company \
  --ticket-id 12345 \
  --start-time 2026-05-14T10:00:00 \
  --end-time 2026-05-14T12:00:00
```

Add `--no-upload` to write the archive locally without uploading it.

## [](#troubleshooting)Troubleshooting

If the Traefik certificate is not issued

Check Traefik logs for ACME (Automatic Certificate Management Environment) errors:

```console
docker compose logs traefik | grep -i "certificate\|acme\|error"
```

Common causes: DNS has not yet propagated (verify with `nslookup api.example.com`), port 80 is blocked by your firewall or security group, or the Let's Encrypt rate limit was reached (wait 1 hour and retry).

If the Couchbase connection fails

Verify `AGENTMEMORY_CONN_STRING`, `AGENTMEMORY_USERNAME`, `AGENTMEMORY_PASSWORD`, and `AGENTMEMORY_BUCKET`. Check that the Search Service is enabled on the cluster and that your server's network allows the connection. If you're using TLS, verify that `AGENTMEMORY_CONN_ROOT_CERTIFICATE` is mounted and points to the correct path inside the container.

If the container starts but `/health` returns an error

Check startup logs with `docker compose logs agentmemory-server`.

If the container exits immediately on startup

The model provider must be reachable when the container starts. If the embedding or LLM endpoint returns an authentication or connectivity error, the server exits. Verify your `OPENAI_API_KEY` or `AGENTMEMORY_EMBEDDING_API_KEY`/`AGENTMEMORY_LLM_API_KEY` and that the model endpoint is reachable from the server.

If the container appears to hang for \~25 seconds before exiting

Agent Memory retries the Couchbase connection 5 times at 5-second intervals before exiting. If using Docker Compose, the `start_period: 40s` healthcheck setting covers this window. For manual `docker run` deployments, allow up to 25 seconds for the container to report healthy or fail.

If a volume causes a permission error on startup

The Prometheus TSDB or log volume may have been initialized by an older image. Recreate the affected volume:

```console
docker compose down
docker volume rm agentmemory_agentmemory-prometheus
docker compose up -d
```

## [](#next-steps)Next Steps

* [Agent Memory Environment Variable Reference](config-agent-mem-env.md)
* [Configure Agent Memory Authentication](config-agent-mem-auth.md)
* [Develop with the Agent Memory SDK](develop-agent-mem.md)