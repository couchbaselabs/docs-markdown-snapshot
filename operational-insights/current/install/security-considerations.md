---
title: Security Considerations
description: Ensure that you follow security best practices throughout the
  deployment lifecycle.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/security-considerations.adoc
  xref: xref:enterprise-analytics:install:security-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/security-considerations.html)

# Security Considerations

> Ensure that you follow security best practices throughout the deployment lifecycle. 

Security is important for every line of business. This topic summarizes some security best practices that you should consider both before and after you install Operational Insights.

While you're setting up your environment, be sure to do the following:

Use a firewall

Firewalls offer a layer of defense against external threats and you should use them to safeguard the perimeters of your deployment. It's a security best practice not to expose your Operational Insights nodes to the Internet; instead, place your entire cluster behind a firewall.

Below are some guidelines for using firewall rules with Operational Insights:

* Enable a firewall rule between the Internet and your Operational Insights cluster.
* Use the least privilege access method when designing web applications with multi-tier architecture. Segment the cluster into defined network layers appropriately with firewall rules in front of the application layer and between the application and data layers. Block all traffic through the firewall, and selectively permit traffic on only the required ports between the required hosts.

Operating system updates

Make sure that you apply the latest patches to secure your operating system; a configuration management solution is good for helping with this.

Securing in-transit data to and from the cluster

Make sure that you use SSL for client-Operational Insights communications and to access the Operational Insights Web Console.

Securing the filesystem

You might also consider encrypting your filesystem so that only authorized processes and users can access it. Third-party libraries are available for transparently encrypting Operational Insights data without any application changes.

Sandboxing Python UDFs

Operational Insights runs Python user-defined functions (UDFs) inside an isolated sandbox, but this is not a security boundary. Vet any code that you deploy as a UDF library carefully, and assume that anyone who can create a function can run arbitrary code in the sandbox as part of a query. For more information, see [Python User-Defined Functions](../sqlpp/9b%5Fpython%5Fudf.md).

Inside the sandbox:

* A single gVisor (`runsc`) container runs per node, shared by every library on that node, with no network access.
* Operational Insights does not validate, when you run `CREATE FUNCTION`, that the bound method exists in the uploaded library. The sandbox checks this the first time you call the function instead, and refuses to run an entry module whose file is not inside the library directory.

Practice secure authentication procedures

* Audit who has access to the system
* Change passwords regularly and do not reuse them
* Use strong and unique passwords

Enhance physical security

To enhance physical security of your Operational Insights clusters, consider the following points:

* Make sure that only authorized personnel have physical access to the Operational Insights cluster environment.
* Regularly backup all data and secure backups in an off-site location.