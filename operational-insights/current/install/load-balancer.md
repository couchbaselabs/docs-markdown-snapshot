---
title: Configure a Load Balancer
description: This topic describes how to place a load balancer or reverse proxy
  in front of an Operational Insights cluster, using NGINX as an example.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/load-balancer.adoc
  xref: xref:enterprise-analytics:install:load-balancer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/load-balancer.html)

# Configure a Load Balancer

> This topic describes how to place a load balancer or reverse proxy in front of an Operational Insights cluster, using NGINX as an example. For a conceptual overview of load-balancing topologies, see [Connectivity & Topology Management](../manage/manage-nodes/cluster-connectivity-topology-management.md#active-load-balancer). 

## [](#why-use-a-reverse-proxy)Why Use a Reverse Proxy

* A reverse proxy can hide the existence of individual Operational Insights nodes. This helps secure your cluster when it's exposed to the internet.
* A reverse proxy can provide application firewall features that protect against common web-based attacks.
* A reverse proxy can offload TLS termination from the Operational Insights nodes, which can be significant overhead when supporting large numbers of clients.
* A reverse proxy can distribute incoming requests across several Operational Insights nodes.
* A reverse proxy may rewrite the URL of each incoming request to match the relevant internal location of the requested resource. For Operational Insights, the reverse proxy typically maps an internet-facing port, such as 443, to the Analytics Service REST API port (8095, or 18095 for TLS). See [Operational Insights Ports](cb-operational-insights-ports.md).

## [](#connection-timeouts)Connection Timeouts

Operational Insights queries can run for an extended period, and the [Request REST API](../analytics-rest-service/index.md) supports asynchronous execution of long-running requests. Any intervening load balancer or proxy must be configured with keep-alive and read timeouts long enough to accommodate these connections, rather than the short defaults many load balancers use for typical web traffic.

## [](#nginx-configuration)NGINX Configuration

This section demonstrates how to configure NGINX as a reverse proxy in front of Operational Insights.

1. Connect to a server that can reach your Operational Insights cluster and install NGINX:  
```bash  
sudo apt-get install nginx  
```
2. Once the installation completes, confirm you can access the NGINX welcome page from your browser:  
```bash  
http://127.0.0.1/ (1)  
```

| **1** | Replace 127.0.0.1 with the IP address of your server. |
| ----- | ----------------------------------------------------- |

### [](#basic-nginx-configuration)Basic NGINX Configuration

If you installed NGINX using the instructions above, create your Operational Insights configuration file in **/etc/nginx/sites-available**.

1. Create a file in that directory called `operational-insights` with the content shown in [Example 1](#ex-nginx-cfg):  
Example 1\. NGINX configuration sample  
```text  
upstream operational_insights { (1)  
    server 127.0.0.1:8095;  
}  
# HTTP server  
#  
server {  
    listen 80; (2)  
    server_name  oi-cluster.example.com; (3)  
    location / { (4)  
        proxy_pass              http://operational_insights; (5)  
        proxy_http_version      1.1; (6)  
        keepalive_requests      1000; (7)  
        keepalive_timeout       360s;  
        proxy_read_timeout      360s; (8)  
    }  
}  
```

| **1** | The upstream block specifies the server and port NGINX forwards traffic to. In this example, it's an Operational Insights node running on the same server as NGINX and listening on the default Analytics Service REST API port, 8095\. Change these values to match your cluster's nodes. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The listen directive instructs NGINX to listen on port 80 for incoming traffic.                                                                                                                                                                                                            |
| **3** | The server\_name directive instructs NGINX to check that the HTTP Host: header value matches oi-cluster.example.com (change this value to your domain).                                                                                                                                    |
| **4** | The location block specifies directives for all URL paths below the root path /.                                                                                                                                                                                                           |
| **5** | The proxy\_pass directive instructs NGINX to forward all incoming traffic to the servers defined in the operational\_insights upstream block.                                                                                                                                              |
| **6** | The proxy\_http\_version directive enables keep-alive connections to the upstream servers.                                                                                                                                                                                                 |
| **7** | The keepalive\_requests directive instructs NGINX to allow up to a thousand requests on the same connection.                                                                                                                                                                               |
| **8** | The keepalive\_timeout and proxy\_read\_timeout directives instruct NGINX to keep connections open long enough to accommodate long-running Operational Insights queries. See [Connection Timeouts](#connection-timeouts).                                                                  |
2. Enable the `operational-insights` site. In the `sites-enabled` directory, make a symbolic link to the file you just created:  
```bash  
ln -s /etc/nginx/sites-available/operational-insights /etc/nginx/sites-enabled/operational-insights  
```
3. Restart NGINX:  
```bash  
sudo service nginx restart  
```
4. Verify that requests are proxied through to Operational Insights. Use your browser, or a command-line tool such as `curl`, specifying the virtual host name you configured above:  
```bash  
curl http://oi-cluster.example.com/  
```  
You should receive a response from the Analytics Service REST API, confirming traffic is reaching your cluster over port 80.

### [](#load-balancing-multiple-operational-insights-nodes)Load Balancing Multiple Operational Insights Nodes

Add the IP address of each additional node to the `upstream` block, as shown in [Example 2](#ex-multiple-nodes). NGINX distributes incoming traffic across all listed nodes.

Example 2\. Configuring for multiple Operational Insights nodes

```bash
upstream operational_insights {
    server 192.168.1.10:8095;
    server 192.168.1.11:8095;
    server 192.168.1.12:8095;
}
```

## [](#transport-layer-security-https-ssl)Transport Layer Security (HTTPS, SSL)

To secure the connection between clients and Operational Insights in production, use Transport Layer Security (TLS, also known as HTTPS or SSL). This encrypts data in transit, including credentials, and protects against Man-in-the-Middle attacks by verifying to the client that it's connecting to the real cluster, not an impostor.

### [](#certificates)Certificates

To enable TLS, you need an X.509 certificate.

For production, get a certificate from a reputable Certificate Authority (CA), so clients can verify your certificate is trustworthy. You'll end up with two files, both of which must be stored on a filesystem accessible to the NGINX process:

* A private key. Treat this file as highly confidential, since anyone with the key can impersonate your site in a Man-in-the-Middle attack. Limit read access to the NGINX process and no others.
* A public certificate.

For testing, you can create a self-signed certificate using the `openssl` command-line tool, as shown in [Example 3](#ex-crt-selfsigned).

Example 3\. Creating a self-signed certificate with OpenSSL

```bash
sudo mkdir -p /etc/nginx/ssl
sudo openssl req -x509 -nodes -days 1095 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
```

### [](#using-the-certificate-and-key)Using the Certificate and Key

Whichever way you generated the certificate, you should now have two files: a certificate and a private key. The following steps assume they're at **/etc/nginx/ssl/nginx.crt** and **/etc/nginx/ssl/nginx.key**.

1. Add a new server section to the NGINX configuration file to support TLS termination, as shown in [Example 4](#ex-cfg-ssl-term):  
Example 4\. Configure for TLS termination  
```text  
server {  
    listen 443 ssl;  
    server_name  oi-cluster.example.com;  
    ssl_certificate /etc/nginx/ssl/nginx.crt;  
    ssl_certificate_key /etc/nginx/ssl/nginx.key;  
    ssl_session_cache   shared:SSL:10m;  
    ssl_session_timeout 10m;  
    location / {  
        proxy_pass              http://operational_insights;  
        proxy_http_version      1.1;  
        keepalive_requests      1000;  
        keepalive_timeout       360s;  
        proxy_read_timeout      360s;  
    }  
}  
```
2. Restart NGINX to enable the new server:  
```bash  
sudo service nginx restart  
```
3. Test using `curl`:  
```bash  
curl -k https://oi-cluster.example.com/  
```  
> [!NOTE]  
> If you're using a self-signed certificate, add the `-k` flag to accept an untrusted certificate. Without this flag, the command fails because your certificate isn't signed by a trusted CA.

## [](#aws-elastic-load-balancer-elb)AWS Elastic Load Balancer (ELB)

Operational Insights queries and streaming ingestion can involve long-running connections. Set the **Idle Timeout** setting of the ELB to the maximum value of 3600 seconds (1 hour) to avoid the load balancer closing connections prematurely.

See the [ELB documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html) for more information on how to change this setting.

## [](#see-also)See Also

* [Connectivity & Topology Management](../manage/manage-nodes/cluster-connectivity-topology-management.md)
* [Operational Insights Ports](cb-operational-insights-ports.md)