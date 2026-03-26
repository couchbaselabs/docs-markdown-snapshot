---
title: Security Best Practices
description: Security is a process and Couchbase Capella strives to achieve the
  best ways to protect your data, from Zero Trust, through adaptive access, to
  centralized management and proactive monitoring.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/security.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:security:security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/security/security.html)

# Security Best Practices

> Security is a process and Couchbase Capella strives to achieve the best ways to protect your data, from Zero Trust, through adaptive access, to centralized management and proactive monitoring. Best practices in the way you work with Capella further protect you from malicious attacks. 

This page groups together listings of some of the many features of Capella security architecture with links to places in the docs where you have a chance to apply good practice to your Couchbase instance.

## [](#security-highlights)Security Highlights

All communication is encrypted using TLS 1.2 or higher. This can't be turned off.

### [](#auditing)Auditing

Capella provides event auditing, whereby events are logged. Log files can be downloaded for inspection.

Event auditing occurs on a _per node_ basis: each node captures only its own events, and saves the records in its own log file. When a cluster's log files are to be inspected, the user can perform a _download_: all log files are duly downloaded, as a single, compressed file, to the user's current system.

For a full overview, providing access to step-by-step instructions and reference information, see [Auditing](auditing.md).

### [](#encryption-at-rest)Encryption at Rest

By default, Couchbase Capella clusters use the underlying cloud provider's key management service to create a new key for each cluster. These key management services include AWS Key Management Service, Google Cloud Key Management Service, and Azure Key Vault.

Capella uses customer master keys that are 256-bit Advanced Encryption Standard (AES) symmetric keys and are not exportable. AES-256, which has a key length of 256 bits, supports the largest bit size and is practically unbreakable by brute force based on current computing power, making it the strongest encryption standard. Customer master keys use hardware security modules (HSMs) validated under FIPS 140-2.

#### [](#customer-managed-encryption-keys)Customer Managed Encryption Keys

Capella also supports [customer-managed encryption keys](cmek.md). Customer-managed encryption allows you to move control of the keys from Couchbase to your own key management system. By managing your encryption keys, you control their configuration, rotation cycles, geographic storage location, and can directly revoke them.

### [](#access-management)Access Management

Capella is built upon Couchbase's sophisticated Role-Based Access Control.

[Organization and Project Overview](../organizations/organization-projects-overview.md): Couchbase Capella is organized into organizations and projects, each of which has its own user roles.

[Allowed IPs](../clusters/allow-ip-address.md): Limit both the IP addresses that can access your data, and the period for which they have access.

[Cluster Credentials](../clusters/manage-database-users.md): Provide programmatic and application-level access to data on a cluster.

### [](#authentication)Authentication

[Federated & SSO Authentication](../organizations/ui-auth/capella-ui-auth.md): Couchbase Capella allows users to sign in to the Capella UI using federated and SSO authentication after configuring Capella to authenticate using data passed from your identity provider (IdP). Okta, Azure AD, Ping Identity, and CyberArk are supported IdPs.

[Multi-Factor Authentication (MFA)](../organizations/ui-auth/mfa.md): Any non-SSO user within your organization can use Capella's MFA. MFA improves your Capella account security by requiring two credentials to sign in: your password and a time-based one-time password (TOTP).

Five failed attempts at logging in a user results in that account being locked for five minutes.

### [](#secrets-management)Secrets Management

Application passwords management can be simplified with our [Hashicorp Vault plug-in](https://github.com/couchbasecloud/vault-plugin-database-couchbasecapella). Vault's Cluster Secrets Engine generates dynamic, short-lived cluster credentials, which streamlines the management of cluster connections and roles. You can also customize permissions and TTL settings.

## [](#applying-best-practice)Applying Best Practice

Make sure to familiarize yourself with [our Access Management](../clusters/manage-database-users.md) (RBAC), to ensure your applications take advantage of the Least Privileges and Separation of Duties that we offer.

We strongly recommend enabling [Multi-Factor Authentication](../organizations/ui-auth/mfa.md) (MFA) to authenticate against Capella—​adding a strong layer of protection against many common attacks.

### [](#lifecycle)Lifecycle

Couchbase Capella manages the infrastructure lifecycle for you, upgrading the Couchbase Cluster with a new version of Couchbase Server, and communicating the release cycle and policy with you. Customers should update the Couchbase SDK that they use in their applications to the latest patched version, and validate after upgrading.

### [](#monitoring-alerts)Monitoring & Alerts

Couchbase Capella provides a performance metrics dashboard. The customer reviews the metrics and is responsible for scaling the cluster to accommodate changes in workload or dataset size Capella provides an Alerts dashboard — informing you of any problems, such as a failed backup. Reviewing these [alerts](../clusters/monitoring/monitoring.md) and taking appropriate actions is a shared responsibility between the Couchbase Support team and the customer.

### [](#multi-factor-authentication)Multi-Factor Authentication

Multi-Factor Authentication (MFA) is available for non-SSO Capella users. Users can choose to add another layer of security by requiring a one-time passcode to be used in conjunction with the password to log in to the Couchbase Capella Control Plane.

See [Manage Multi-Factor Authentication (MFA)](../organizations/ui-auth/mfa.md) for more information.

### [](#networking)Networking

[Set up a VPC peering connection](../clouds/private-network.md) with AWS, Azure, or GCP.

[Add a private endpoint](private-endpoints.md) with AWS PrivateLink, Azure Private Link, or GCP Private Service Connect.

#### [](#public-access)Restrict Public Access

> [!IMPORTANT]
> Limited availability
> 
> The option to create a cluster with restricted public access is available only on request. For more information, contact Couchbase Support.

If Couchbase grants your organization access to this feature, you can restrict public access for a [new cluster](../clusters/create-database.md).

With restrict public access turned on for your cluster, you can only connect to your cluster through Capella's private networking options, including [VPC peering](../clouds/private-network.md) and [private endpoints](private-endpoints.md).

For example, with restrict public access enabled, only your cloud service provider (CSP) network that's peered with Capella can access your cluster. This configuration allows direct traffic routing from your on-premises network to Capella through your CSP's network that's peered with Capella.

When you restrict public access for a cluster, the cluster is accessible only through private IP addresses that Capella assigns. In your applications, you can use the [DNS hostname](../clusters/modify-database.md#view-config) provided by Capella to resolve your cluster's private IP addresses. You can also still use the connection string for your cluster on the **Settings** **Connect** page.

### [](#shared-responsibilities)Shared Responsibilities

Good security is a partnership of application and cluster. With Capella, most operations are automated, but some areas need active input from the customer to get the best possible results.

With a fully-hosted solution, Couchbase takes care of all of the infrastructure, as well as managing the cluster deployment. However, customers should take care to follow best practices for authentication, as well as least privilege in RBAC. This page highlights some of those best practices.

Key areas of customer responsibility are _Defining Roles_ and _Customer Access Control policy_.

### [](#common-next-steps)Common Next Steps

Now that you have seen an overview of Capella's security features, any one of the above links will take you deeper. You may also want to continue with one of the following next steps:

* Authenticating your client by X.509 certificate — [Java](../../java-sdk/current/howtos/sdk-authentication.md#authenticating-the-java-client-by-certificate); [Node.js](../../nodejs-sdk/current/howtos/sdk-authentication.md#authenticating-a-node-js-client-by-certificate).