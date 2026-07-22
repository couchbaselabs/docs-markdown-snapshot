---
title: Capella App Services Release Notes
description: Release notes for Capella App Services, including new features,
  enhancements, and updates.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/release-notes/release-notes.adoc
pubDate: 2026-07-22T05:30:13.485Z
link: xref:app-services::release-notes/release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/release-notes/release-notes.html)

# Capella App Services Release Notes

> Release notes for Capella App Services, including new features, enhancements, and updates. 

This page contains release notes specific to Capella App Services. For general Capella release notes, see [Couchbase Capella Release Notes](../../cloud/release-notes/release-notes.md).

## [](#july-2026)July 2026

* Specify a Static CIDR Range for Azure App Services  
When creating an App Service on Azure, you can now optionally specify a static CIDR range for the subnet where the App Service load balancer is deployed. The CIDR value persists when you turn the App Service off and back on, preventing CIDR conflicts when peering with a Capella deployment. If you do not specify a value, Capella assigns a CIDR range automatically.  
For more information, see [Requested CIDR](../app-services/creating-an-app-service.md#requested-cidr).

## [](#june-2026)June 2026

* System Metadata Migration  
App Services 4.1 upgrades initiate an automated, background migration of system metadata from the `_default` collection to a dedicated system collection to improve security and operational consistency. This process is designed to execute without affecting your App Service's operations or incurring any downtime.

**Important Compatibility Note:** If you have implemented custom integrations (including eventing functions) that reference system metadata in the `_default` collection, these will need to be updated to reference the new location.  
[Contact Support](https://support.couchbase.com/hc/en-us) if you require further clarification on whether this impacts your apps or to opt out of the system metadata migration during the upgrade. If you opt out, you can migrate the system metadata any time after upgrade.  
For more information, see [System Metadata Migration](../migrating/migrate-sync-metadata.md).
* Capella now supports native alert integrations for Slack and Microsoft Teams. You can send cluster and App Service [metric-based alerts](../../cloud/reference/alert-reference.md#metric-alerts) directly to your team's preferred Slack or Microsoft Teams channels by using the Capella UI or the Management REST API.  
Customize alert payloads with either standard or advanced templates for Slack and Microsoft Teams integrations. To configure an alert integration, see [Configure a Slack Alert Integration for App Services](../monitoring/configure-slack-integration.md)and [Configure a Microsoft Teams Alert Integration for App Services](../monitoring/configure-microsoft-integration.md).  
For more information about alert integrations, see [Alert Integrations for App Services](../monitoring/alert-integration.md).
* Access to the Metrics and Admin REST APIs over private endpoints no longer requires configuration of IP allow list for the associated Metrics or Admin user.

## [](#may-2026)May 2026

* Test Your Access Control and Data Validation Function  
You can now validate your Access Control and Data Validation function directly in the Capella UI without affecting production data. The new Test Function panel lets you simulate a document write by providing a document, an optional previous document version, an optional user context, and optional XATTRs. The results panel displays channel assignments, role assignments, access grants, and any user-defined console log output from the function execution.  
For more information, see [Test Your Access Control and Data Validation Function](../app-endpoints/access-control-data-validation.md#test-your-access-control-and-data-validation-function).

## [](#april-2026)April 2026

* App Services 4.0.4  
New App Services deployments now deploy Sync Gateway 4.0.4\. This release includes the following fixed issues and enhancements:

  * [CBG-5173](https://issues.couchbase.com/browse/CBG-5173) — Fixed an issue where the `/db/_index_init` endpoint would panic if the database was started in offline mode.
  * [CBG-5202](https://issues.couchbase.com/browse/CBG-5202) — Fixed an issue where remote-wins conflict resolution incorrectly generated a new revision ID.
  * [CBG-5157](https://issues.couchbase.com/browse/CBG-5157) — Added support for EdDSA tokens for OIDC and JWT authentication.
  * [CBG-5214](https://issues.couchbase.com/browse/CBG-5214) — CBL-JS ping BLIP requests are now handled silently to reduce noise in logs.  
For more information about all changes within this maintenance release, see the [Sync Gateway 4.0.4 Release Notes](../../sync-gateway/current/product-notes/release-notes.md#maint-4-0-4).
* New App Services deployments now deploy Sync Gateway 3.3.4  
This release includes the following fixed issues and enhancements:

  * [CBG-5147](https://issues.couchbase.com/browse/CBG-5147) — Fixed an issue where replacement revisions were never utilized for unfiltered replications.
  * [CBG-5174](https://issues.couchbase.com/browse/CBG-5174) — Fixed an issue where the `/db/_index_init` endpoint would panic if the database was started in offline mode.
  * [CBG-5158](https://issues.couchbase.com/browse/CBG-5158) — Added support for EdDSA tokens for OIDC and JWT authentication.
  * [CBG-5215](https://issues.couchbase.com/browse/CBG-5215) — CBL-JS ping BLIP requests are now handled silently to reduce noise in logs.  
For more information about all changes within this maintenance release, see the [Sync Gateway 3.3.4 Release Notes](../../sync-gateway/3.3/product-notes/release-notes.md#maint-3-3-4).

## [](#march-2026)March 2026

* Private Endpoint Support via UI for App Services  
You can now configure Private Endpoints for App Services directly through the Capella UI. This allows you to secure your application traffic by eliminating exposure to the public internet. The UI provides a streamlined, guided experience for setting up private endpoints, making it easier to establish secure connections between your applications and App Services.  
Currently, private endpoints for App Services are only available using Amazon Web Services (AWS).  
For more information, see [Manage AWS Private Endpoints Using the Capella UI](../private-endpoints/app-services-private-endpoints-aws-ui.md).

## [](#december-2025)December 2025

* App Services 4.0.2  
New App Services deployments now deploy Sync Gateway 4.0.2\. This release includes the following fixed issues:

  * [CBG-5007](https://issues.couchbase.com/browse/CBG-5007) — Fixed an issue where the `_ping` endpoint and other endpoints could block when the server context write lock was acquired.
  * [CBG-5026](https://issues.couchbase.com/browse/CBG-5026) — Fixed an issue where resync operations would fail on documents last mutated prior to Sync Gateway 4.0.
  * [CBG-5027](https://issues.couchbase.com/browse/CBG-5027) — Improved revision cache lock handling by using defer for lock and unlock operations where applicable.
  * [CBG-5029](https://issues.couchbase.com/browse/CBG-5029) — Fixed a potential deadlock in the revision cache shard that could occur during memory-based cache eviction.
  * [CBG-5034](https://issues.couchbase.com/browse/CBG-5034) — Fixed delta computation to ensure proper synchronization.  
For more information about all changes within this maintenance release, see the [Sync Gateway 4.0.2 Release Notes](../../sync-gateway/current/product-notes/release-notes.md#maint-4-0-2).
* Dynatrace Support for App Services Log Streaming  
You can now stream App Services operational and audit logs to Dynatrace for proactive troubleshooting and application monitoring.  
Dynatrace joins the existing list of supported third-party observability platforms, including Datadog, Sumo Logic, Elasticsearch, Grafana Loki, Splunk, and custom HTTP collectors.  
For more information, see [Log Streaming](../monitoring/log-streaming.md#supported-providers).

## [](#november-2025)November 2025

* App Services now supports configuring scopes for OIDC providers, enabling apps to request and authorize access to user details during authentication.  
For more information, see [Connect OpenID Connect (OIDC) Providers](../security/set-up-authentication-provider.md#oidc-settings).

## [](#october-2025)October 2025

* App Services 4.0 with Bidirectional XDCR Support  
This App Services release introduces the ability to set up bidirectional XDCR between two active App Services clusters. With this capability, you can set up App Services in active standby mode for failover and disaster recovery use cases. Couchbase Lite clients on v4.0 can seamlessly switch between App Services clusters running this version.  
App Services 4.0 is compatible with Couchbase Server versions 7.6.4 and above. However, the minimum version of Couchbase Server required for the bidirectional XDCR capability is 7.6.6.  
For more information about all changes within this major release, see the [Sync Gateway 4.0 Release Notes](../../sync-gateway/current/product-notes/release-notes.md).

## [](#september-2025)September 2025

* Splunk Support for App Services Log Streaming  
You can now stream App Services operational and audit logs to Splunk for proactive troubleshooting and application monitoring.  
Splunk joins the existing list of supported third-party observability platforms, including Datadog, Sumo Logic, Elasticsearch, Grafana Loki, and custom HTTP collectors.  
For more information, see [Log Streaming](../monitoring/log-streaming.md#supported-providers).
* Capella App Services enhanced UI  
Capella App Services now offers two setup paths to make it easier for developers to get started and connect their applications:

  * **Guided Setup** provides a step-by-step flow with automatic cluster provisioning and app endpoint creation, ideal for new users.
  * **Advanced Setup** requires an existing operational cluster and targets experienced users who need more control for custom configurations.  
For more information about the new setup paths, see [Setup App Services Cluster](../../cloud/get-started/create-account.md#choose-your-setup-method).
* Revamped Connect tab for App Services  
The Connect tab has been redesigned to make it easier for developers to get started, with:

  * Separate sub-tabs for each connection method: Couchbase Lite, Public REST API, and Admin & Metrics API.
  * Guided steps for each method to help you connect your application.
  * The Public REST API page now includes a built-in quick validation tool, allowing you to test your endpoint instantly.  
The Connect tab provides all the necessary connection parameters, prerequisites, installation instructions, code snippets, full code samples, and examples for different connection methods. For more information, see [Connect App Endpoint](../get-started/configuring-app-services.md#access-endpoint).
* Home page for App Service and App Endpoints  
A dedicated Home tab for the App Service cluster and its corresponding App Endpoints allows you to view service health and linked resources in a single place.

## [](#july-2025)July 2025

* Customer Self-Service Upgrades for App Services  
You can now schedule and manage App Service upgrades on your own timeline without the need to open a support ticket. This new feature offers a simplified upgrade experience. By giving you more control, you can speed up the adoption of fixes and improvements that keep your App Service up to date and performing at their best.  
For more information, see [Upgrade App Services](../maintenance/upgrading-app-services.md).
* Private Endpoints for App Services (AWS)  
You can now configure App Services with Private Endpoint support. With this feature, applications can connect to and sync data with App Services over a secure private endpoint. Applications can also continue to sync data over a public network. You can configure this functionality via the Capella Management API. Currently, private endpoints for App Services are only available using Amazon Web Services (AWS).  
For more information, see [Private Endpoints for App Services](../private-endpoints/app-services-private-endpoints.md).
* New App Services deployments now deploy Sync Gateway 3.3.0  
This minor release includes a few internal scalability, indexing, and security-related optimizations. Upgrading to this version does not require any changes to clients to take advantage of the optimizations, which are available automatically on upgrade.  
Starting with Sync Gateway 3.3.0, customers can request Capella support to disable the [GET /{keyspace}/\_all\_docs](../references/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs) operation on their upgraded clusters. Disabling this feature improves performance and prevents potential misuse of this REST API.  
For more information about all changes within this maintenance release, see the [Sync Gateway 3.3.0 Release Notes](../../sync-gateway/3.3/product-notes/release-notes.md#maint-3-3-0).

## [](#june-2025)June 2025

* New App Services deployments now deploy Sync Gateway 3.2.5  
This release includes:

  * Improved attachment handling in replication. It is now correctly verified that `_attachments` is a top-level property before processing attachments. This prevents errors when documents contain the string `_attachments` elsewhere in their content.
  * Fixed `MgmtRequest` function that fetches metadata or settings from Couchbase Server's REST API panic if the HTTP request fails.
  * Updated [go-blip](https://github.com/couchbase/go-blip) to log using the BLIP connection ID instead of the HTTP correlation ID to improve traceability between Sync Gateway changes and BLIP logs.  
For more information about all changes within this maintenance release, see the [Sync Gateway 3.2.5 Release Notes](#3.2@sync-gateway:product-notes:release-notes.adoc#3-2-5june-2025).

## [](#april-2025)April 2025

* App Services OIDC Enhancements — Claims to Access Grants Mapping  
You can now specify a JWT roles claim in the App Services OIDC user interface to assign roles to App Services users.  
For more information, see [OpenID Connect (OIDC)](../security/set-up-authentication-provider.md#oidc-settings).
* New App Services deployments now deploy Sync Gateway 3.2.4  
This release includes:

  * Fixes for goroutine leaks in ISGR and BLIP messaging.
  * Improved import processing efficiency and sequence management.
  * New metrics for assertions and sequence allocation tracking.  
For more information about all changes within this maintenance release, see the [Sync Gateway 3.2.4 Release Notes](#3.2@sync-gateway:product-notes:release-notes.adoc#3-2-4april-2025).

## [](#march-2025)March 2025

* App Services 3.2.2 or later is now fully compatible with Eventing Services on operational clusters that use Couchbase Server 7.6.5 or later.  
The [Eventing Service](../../cloud/eventing/eventing-overview.md) can run one or more Eventing Functions in your cluster to handle data changes according to a real-time Event-Condition-Action model. This update adds the ability to create Eventing Functions that can read and write data from a keyspace (bucket, scope, or collection) that's linked to an App Services App Endpoint. This expands previous capabilities, which only allowed for read-only bindings.  
To [create an Eventing Function](../../cloud/eventing/add-eventing-functions.md) to use with App Services, you must enable the App Services Compatibility setting.

## [](#february-2025)February 2025

* App Services 3.2.2  
New App Services deployments now deploy [Sync Gateway 3.2.2](#3.2@sync-gateway:product-notes:release-notes.adoc#maint-3.2.2). This release includes:

  * Fixes and improvements to revcache on-demand imports.
  * Improving cleanup processes during rollback of the import feed.
  * Additional stats to track background SQL++ queries.

## [](#november-2024)November 2024

* App Services 3.2.1  
New App Services deployments now deploy [Sync Gateway 3.2.1](#3.2@sync-gateway:product-notes:release-notes.adoc#maint-3.2.1). This release includes:

  * Index optimizations that reduce processing time for App Endpoints being linked to tens of collections or more at a given time.
  * CBL powered apps now disconnect automatically when databases are closed, ensuring cleaner resource management and system efficiency.

## [](#september-2024)September 2024

* Cluster Deletion Protection for App Services  
Deletion protection will block attempts to delete a cluster's buckets and any linked App Services. For more information about deletion protection, see [Change Your Deletion Protection](../../cloud/clusters/modify-database.md#deletion-protection).
* App Services 3.2.0  
New App Services deployments now deploy [Sync Gateway 3.2.0](#3.2@sync-gateway:product-notes:release-notes.adoc#maint-3.2.0). This release includes the following:

  * Launch of Audit Logging to track operational irregularities and support auditing and compliance.
* Announcing support for Audit Logging on Capella App Services  
Audit logs capture detailed user, process, or system activities in JSON format, providing a chronological record of actions and events. Users can opt in for audit log generation and configure specific events, users and roles to track for regulatory compliance and observability. Logs can be exported, downloaded, or streamed to third-party services like DataDog, SumoLogic, Grafana Loki, Elastic, or custom HTTP endpoints. Capella App Services is now HIPAA-ready.  
To learn more about Audit Logging on Capella App Services, see [Audit Logging](../monitoring/audit-logging.md).
* Single Node App Services  
Announcing support for Single Node App Services, tailored specifically for development, testing, and prototyping use cases that do not require high availability (HA). Users can choose from two instance types for each cloud provider (AWS, GCP, Azure) and deploy an App Service on them:

  * 2vCPU / 4GB RAM
  * 4vCPU / 8GB RAM  
This new offering provides an efficient and cost-effective way to develop, test, and prototype your Mobile and IoT applications. For more information about Single Node App Services, see [Create an App Service](../app-services/creating-an-app-service.md).

## [](#august-2024)August 2024

* Billing reporting for App Services  
The billing reporting experience has been updated to provide more detailed information about your credit usage among Couchbase Capella's services, including App Services and clusters. These updates include:

  * An [overview of your organization's credit usage](../../cloud/billing/manage-billing.md#access-billing).
  * [Granular filtering and reporting](../../cloud/billing/manage-billing.md#filter-usage) of all credit usage.
  * [Alerting](../../cloud/billing/manage-billing-alerts.md) for credit balances and pay-as-you-go usage.
* Scopes and Collections in App Services  
You can manage your data with a high degree of granularity using Scopes and Collections in App Services. You can link collections to a given App Endpoint to make them mobile aware, allowing synchronization of data from the cloud to your mobile and IoT applications.  
The benefits of scopes and collections include:

  * The logical grouping of similar documents.
  * Secure isolation of different document-types within a bucket, allowing applications to be specifically authorized to use only their appropriate subsets of data.  
For more information about Scopes and Collections in App Services and their use cases, see:

  * [App Services - Linking a Collection](../app-endpoints/creating-an-app-endpoint.md)
  * [Scopes and Collections Blog Post](https://www.couchbase.com/blog/scopes-collections-couchbase-mobile/)

## [](#july-2024)July 2024

* App Services 3.1.8  
New App Services deployments will now deploy [Sync Gateway 3.1.8](#3.1@sync-gateway:product-notes:release-notes.adoc#maint-3.1.8). This release includes general fixes and enhancements - including clarity of messaging for errors, fixes to cluster initialization behavior and improved messaging during the process.
* App Services region availability expansion  
App Services is now available in the Middle East Central (Dammam) Google Cloud region.

## [](#may-2024)May 2024

* App Services: Static App Services URL Endpoints  
URLs associated with App Endpoint APIs now persist in the following scenarios:

  * After restarts and internal redeploys of the App Service.
  * When the App Service is turned off and then turned on again.
  * When a bucket linked to an App Endpoint is backed up and then restored.
  * When an App Service is deleted, then recreated and associated with the same cluster.
  * After App Services scaling and upgrade operations.  
  This enhancement removes the need to update these URLs in your application code or in your firewall configurations.

## [](#march-2024)March 2024

* Alert Notification Integrations for App Services  
Get notified in the toolset of your choice by integrating Capella alert notifications with third-party tools like ServiceNow and more, using an incoming Webhook.  
Customers can now configure alert integrations in Capella at the project level using UI or public management APIs. On the receiving side, you can leverage the payload sent with cluster and App Services alert notifications to automate workflows and further meet your organizational observability needs.  
For more information, see [Alert Integrations](../../cloud/clusters/monitoring/alert-integration.md).
* User-specified CORS Configuration per App Endpoint in Capella App Services  
Cross-Origin Resource Sharing (CORS) is a core web security concept allowing users to specify how resources on App Services should be accessed from a different domain via client-side HTTP requests, such as browser-based or PouchDB applications. Users can now configure CORS in App Services on an App Endpoint basis, providing flexibility in configuring how CORS rules in their applications should interact with App Services.  
For more information, see [CORS Configuration for App Services](../app-endpoints/cors-configuration-for-app-services.md)

## [](#february-2024)February 2024

* Support for Multiple OpenID Connect (OIDC) Providers in Capella App Services  
Open ID Connect (OIDC) authentications allows users' applications to use Couchbase for data synchronization, delegating the authentication to a third-party server known as the Provider, such as Google+ or PayPal. Users can now configure multiple OIDC Providers in App Services per App Endpoint and use them in their client applications. Specify a Default Provider to simplify client flows, as all client requests are handled by the Default Provider unless explicitly defined otherwise.  
For more information, see [Set Up an Authentication Provider](../security/set-up-authentication-provider.md).

## [](#december-2023)December 2023

* Hashicorp Terraform Provider 1.0.0 for App Services  
Version 1.0.0 of [Terraform Provider for Capella](https://registry.terraform.io/providers/couchbasecloud/couchbase-capella/latest) is now available. The first version of the Provider can be used for programmatically managing Capella resources including API keys, users, projects, cluster buckets, app services, and bucket backups. The provider will be continually enhanced to include support for further resources.
* Extended Attributes(XATTRs) for more secure Access Control and Data Validation in Capella App Services  
You can now store channels and roles as User Extended Attributes (XATTRs) on Capella App Services. This is a more flexible alternative that uses metadata to store access grants outside of the document content, which can then be used to make access control and document routing decisions.  
Go to [XATTRs for App Services](../app-endpoints/xattrs-for-app-services.md) to start using XATTRS for your apps.

## [](#november-2023)November 2023

* Real-time Log Streaming now available on Capella App Services  
Log Streaming provides real-time streaming of App Services operational logs to third-party observability platforms such as Datadog or SumoLogic or self-hosted HTTP logs collectors. Gain insights into application behavior, enable rapid issue detection and resolution to enhance application reliability, performance, and security.  
Available at App Services 3.1.2 or higher for Dev Pro and Enterprise customers. Data transfer costs for Log Streaming are billed at the same rate as all other egress costs from App Services
* Pre-authorize support to take action on failing App Services  
Use **Request prompt action for cluster recovery** to pre-authorize Capella Support to quickly take remediation actions on clusters or App Services that are in a critical health state. Keep this feature enabled at all times to minimize service disruptions.  
For more information, see [Request Prompt Action for Cluster Recovery](../../cloud/billing/support-pre-auth.md).

## [](#october-2023)October 2023

* HIPAA compliance for App Services  
HIPAA compliance currently excludes App Services, which will follow-on in a future release.  
See the [Cloud Trust Center](https://www.couchbase.com/products/capella/trust) for additional information on the security controls and compliance of the platform.
* App Services: Persistence of deleted documents & metadata purge interval  
App Services deployments will retain deleted documents in the server cluster for a period of 60 days following deletion.  
This allows disconnected clients to sync down deleted revisions when they come back online, anytime within the 60 day period.  
This only impacts clusters with linked app services deployed after this release.

## [](#august-2023)August 2023

* On/Off Schedule for App Services  
You can now turn off your non-production provisioned clusters when you are not using them, allowing you to save on costs. Turning off your cluster turns off the compute for your cluster but the storage remains — this means that all of your data, schema (buckets, scopes, collections), and indexes remain, as well as your cluster configuration, including users and allow lists. You can turn on and off your cluster [on-demand](../../cloud/clusters/off-on-database.md) or using a [schedule](../../cloud/clusters/off-on-schedule.md). For example, you can set a schedule for your development cluster to be on from 9 am to 5 pm on week days and off at all other times. Any linked App Service will also be turned off when the linked cluster is turned off.

## [](#march-2023)March 2023

* App Services Self-Service Maintenance Schedules  
Capella now automatically notifies you about upcoming upgrades and maintenance jobs on App Services clusters that you manage. A new self-serve maintenance screen enables you to upgrade your App Service, reschedule upcoming maintenance jobs or set your preferred maintenance times. For more information, see [App Services Maintenance](../maintenance/upgrading-app-services.md).

## [](#february-2023)February 2023

* Capella App Services is now generally available on [Microsoft Azure Cloud in 11 regions worldwide](../../cloud/reference/azure.md).  
[Capella App Services](../index.md) is a fully managed application backend that brings the power of [Couchbase Mobile](../../home/mobile.md)'s industry-leading offline-first data sync capability to Capella. [Free self-service trials](https://cloud.couchbase.com/sign-up) are also available. Check out the [App Services Getting Started guide](../get-started/configuring-app-services.md) for more details.

## [](#january-2023)January 2023

* Capella App Services free trials now available on Azure.  
Capella App Services free self-service trial now supports Azure. Developers can try out App Services on Azure for free for a 30-day trial period to build mobile, desktop, and embedded apps with offline-first data sync capabilities. App Services brings the power of Couchbase Mobile as-a-service offering to Azure-hosted clusters.  
App Services will be generally available in Azure in the near future.

## [](#july-2022)July 2022

* Capella App Services now available on GCP, plus several new features across all supported clouds.  
[Capella App Services](../index.md) is now generally available on GCP in [supported regions worldwide](../../cloud/reference/gcp.md). With this release, we bring the power of [Couchbase Mobile](../../home/mobile.md) as-a-service offering to GCP hosted clusters.
* In addition, the release also introduces the following feature enhancements available on AWS and GCP.

  * The Metrics API is directly accessible to client apps. This endpoint will facilitate integration with third party monitoring frameworks like Prometheus.
  * Extensive system level event logging of all activities initiated through Capella that are related to App Services and App Endpoints related are captured in global activity log.
  * Alerting support for key App Services level events, (such as high resource utilization or a large number of sync errors). This allows users to proactively take remedial measures to prevent potential.
  * Guardrails prevent users from deploying eventing functions with read-write bindings to buckets with App Endpoints.
  * Guardrails prevent users from deleting server buckets with App Endpoints.
  * Capella UI allows updates to App Services even when scaling.
  * Lookup added for App Roles.
  * A number of minor bugs have fixed and internal system enhancements made to improve supportability and reliability.

## [](#june-2022)June 2022

* Capella App Services 1.0 on AWS  
Introduces Capella App Services. [Capella App Services](../index.md) is a fully managed application backend that brings the power of [Couchbase Mobile](../../home/mobile.md)'s industry-leading offline-first data sync capability to Capella.

  * With this new service:

    * Couchbase Lite enabled mobile, desktop, and embedded apps can locally store and access data even when there is no Internet and securely sync data with Capella App Services when connectivity is available.
    * Mobile, desktop, and web apps can securely access data over a public REST interface.
    * Couchbase Lite apps can direct sync data with each over a peer-to-peer network in environments disconnected from the Internet and sync data back to Capella App Services backend.
  * Cappella supports the following Couchbase Mobile capabilities:

    * Deploy and bootstrap App Services (Sync Gateway clusters).
    * Create, configure and administer App Endpoints (Sync Gateway clusters).
    * Create and manage App Users.
    * Create and manage App Roles.
    * Define Access Control (Sync Function).
    * Multiple Client Authentication modes - Basic Auth (username/password), OIDC, Anonymous.
    * Metrics dashboard.
    * Connect mobile, web, and embedded apps over a public endpoint.
    * Admin REST access for secure user administration (custom auth).
    * Scaling App Services on demand.
    * Peer-to-Peer Sync.  
Capella App Services is now generally available on AWS. Free 30-day self-service trials are also available with an [App Services Getting Started guide](../get-started/configuring-app-services.md).

## [](#earlier-releases)Earlier Releases

For information about earlier App Services releases, please refer to the [Sync Gateway Release Notes](#sync-gateway::product-notes:release-notes.adoc).