---
title: Security Considerations
description: Ensure that you follow security best practices throughout the
  deployment lifecycle.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/security-considerations.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:enterprise-analytics:install:security-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/install/security-considerations.html)

# Security Considerations

> Ensure that you follow security best practices throughout the deployment lifecycle. 

Security is important for every line of business. This topic summarizes some security best practices that you should consider both before and after you install Enterprise Analytics.

While you're setting up your environment, be sure to do the following:

Use a firewall

Firewalls offer a layer of defense against external threats and you should use them to safeguard the perimeters of your deployment. It's a security best practice not to expose your Enterprise Analytics nodes to the Internet; instead, place your entire cluster behind a firewall.

Below are some guidelines for using firewall rules with Enterprise Analytics:

* Enable a firewall rule between the Internet and your Enterprise Analytics cluster.
* Use the least privilege access method when designing web applications with multi-tier architecture. Segment the cluster into defined network layers appropriately with firewall rules in front of the application layer and between the application and data layers. Block all traffic through the firewall, and selectively permit traffic on only the required ports between the required hosts.

Operating system updates

Make sure that you apply the latest patches to secure your operating system; a configuration management solution is good for helping with this.

Securing in-transit data to and from the cluster

Make sure that you use SSL for client-Enterprise Analytics communications and to access the Enterprise Analytics Web Console.

Securing the filesystem

You might also consider encrypting your filesystem so that only authorized processes and users can access it. Third-party libraries are available for transparently encrypting Enterprise Analytics data without any application changes.

Practice secure authentication procedures

* Audit who has access to the system
* Change passwords regularly and do not reuse them
* Use strong and unique passwords

Enhance physical security

To enhance physical security of your Enterprise Analytics clusters, consider the following points:

* Make sure that only authorized personnel have physical access to the Enterprise Analytics cluster environment.
* Regularly backup all data and secure backups in an off-site location.