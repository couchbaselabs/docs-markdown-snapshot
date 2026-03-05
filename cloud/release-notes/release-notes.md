---
title: Couchbase Capella Release Notes
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/release-notes/pages/release-notes.adoc
pubDate: 2026-03-05T03:41:02.175Z
link: xref:cloud:release-notes:release-notes.adoc[]
---

[View original HTML](/cloud/release-notes/release-notes.html)

# Couchbase Capella Release Notes

## [](#march-2026-changelog)March 2026 Changelog

* Default Billing Alerts and Low Credit Warnings for Prepaid Accounts  
If you use pre-paid credits to pay for your usage in Capella, Capella now creates default billing alerts automatically when new pre-paid credits are applied to your account.  
When you [create a new cluster](../clusters/create-database.md) or [change a cluster’s Support Plan](#billing:change-support-plan) and your pre-paid credit balance is depleted or running low, Capella also shows warnings to help you avoid unexpected [pay-as-you-go charges](../billing/billing.md#pay-as-you-go-credits) and choose the right Support Plan with confidence.  
For more information, see [Default Billing Alerts](../billing/about-billing-alerts.md#default-billing-alerts) and [Low Credit Warning Calculations](../billing/billing.md#low-credits).

## [](#february-2026-changelog)February 2026 Changelog

* Couchbase Server 7.6.10  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.10 maintenance release. This version includes bug fixes.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.10](../../server/7.6/release-notes/relnotes.md#release-7610).
* Custom Subdomains in Capella Endpoints  
You can now customize endpoints for Capella resources, such as URLs for clusters, private links, and nodes, with unique identifiers. This option is now also available for GCP and Azure clusters through the [Capella Management API](../management-api-reference/index.md#tag/Organizations/operation/putOrganizationConfiguration).  
This feature is currently only available upon request from [Couchbase Capella Support](../support/manage-support.md#create-support-ticket).
* Couchbase Capella Customer-Managed Encryption Keys (CMEK) for Azure now supports unique Entra ID applications per Capella project and is now generally available.  
You can now configure specific Azure Key Vault connections for each project individually, rather than relying on a single Entra ID application across your entire organization.  
For more information, see [Use Customer-Managed Encryption Keys (CMEK)](../security/cmek.md).
* Capella operational clusters now support fine-grained RBAC for cluster access credentials  
You can now define fine-grained Role-Based Access Control (RBAC) for cluster access using advanced access credentials. Advanced access credentials allow you to assign combinations of fine-grained privileges and roles to cluster access credentials at the bucket, scope, and collection levels.  
Basic access credentials that assign read, write, or read/write access at the bucket, scope, and collection level are still available.  
For more information about advanced access credentials, see [Cluster Access](../clusters/cluster-rbac.md).
* XDCR for Multi-Node Clusters Over Private Link  
Couchbase Capella has enhanced the security of your multi-cluster topology. Capella can now support XDCR through private endpoint connectivity, allowing you to replicate data between clusters entirely over a private network connection.  
This feature is currently only available upon request from [Couchbase Capella Support](../support/manage-support.md#create-support-ticket).  
For more information, see [Replicate Data Across a Private Endpoint Connection](../clusters/xdcr/manage-xdcr-security.md#private-endpoints).
* Prometheus for Multi-Node Cluster Over Private Link  
Couchbase Capella is announcing native support for scraping Prometheus metrics endpoints through private endpoint connectivity. This capability allows you to collect observability data from your internal resources without exposing endpoints to the public Internet.  
This feature is currently only available upon request from [Couchbase Capella Support](../support/manage-support.md#create-support-ticket).  
For more information, see [Add a Capella Cluster to a Prometheus Server](../clusters/monitoring/prometheus.md).

## [](#january-2026-changelog)January 2026 Changelog

* Couchbase Server 7.6.9  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.9 maintenance release. This version includes bug fixes.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.9](../../server/7.6/release-notes/relnotes.md#release-769).

## [](#december-2025-changelog)December 2025 Changelog

* Couchbase Capella now supports Customer-Managed Encryption Keys (CMEK) for clusters running in Microsoft Azure. With CMEK, you can use your own keys stored in Azure Key Vault to protect data-at-rest, giving you tighter control over your encryption lifecycle and compliance.  
This feature is currently only available upon request. For more information, see [Use Customer-Managed Encryption Keys (CMEK)](../security/cmek.md).

## [](#november-2025-changelog)November 2025 Changelog

* Couchbase Server 7.6.8  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.8 maintenance release. This version includes bug fixes.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.8](../../server/7.6/release-notes/relnotes.md#release-768).

## [](#october-2025-changelog)October 2025 Changelog

* New Workload Monitoring Dashboards  
Introducing a new workload monitoring experience in Capella, designed to make performance investigations easier and more actionable for real-world operational workloads. It includes a new Cluster Overview dashboard, Service-specific Workload Monitoring dashboards, and tools to investigate slow queries. The goal is to reduce complexity, accelerate root cause analysis, and help optimize performance and resource usage more effectively.  
For more information, see [View Monitoring Dashboards](../clusters/monitoring/metrics-dashboard.md).
* Ask AI is now available in the Couchbase Capella UI as a public preview.  
This new feature harnesses AI to answer your Couchbase questions right within Capella based on our documentation. Use it to learn about Capella features, get configuration recommendations, and discover next steps quickly and easily.  
See [Ask AI](../get-started/ask-ai.md) for more information.
* Capella now supports Couchbase Server 8.0.  
You can choose Couchbase Server 8.0 when creating a new paid operational cluster. All new Capella free tier operational clusters will be deployed using Couchbase Server 8.0\. To upgrade an existing cluster to Couchbase Server 8.0, contact Couchbase Support.  
Couchbase Server 8.0 on Capella includes the following features:

  * Magma with 128 vBuckets is the new default storage engine  
  Operational clusters created with Couchbase Server 8.0 use Magma with 128 vBuckets as the default storage engine. This new storage engine option has a minimum memory quota requirement of 100 MiB compared to the original 1024 vBucket Magma bucket’s requirement of 1 GiB.  
  For more information about Magma, see [Storage Engines](../clusters/data-service/storage-engines.md).  
  > [!IMPORTANT]  
  > The new default storage backend for buckets may cause issues if you rely on the previous defaults. Update any deployment scripts to accommodate this change before upgrading. For more information about potential compatibility concerns, see [Before You Upgrade](../../server/current/install/upgrade.md#before-you-upgrade).
  * GSI Vector Indexes  
  Couchbase Server 8.0 introduces support for Hyperscale Vector indexes and Composite Vector indexes, along with a new, simplified UI in Capella for creating vector indexes.  
  Use Hyperscale Vector indexes and Composite Vector indexes to perform vector searches in support of AI applications and other uses.

    * Hyperscale Vector indexes contain a single vector column. Hyperscale Vector indexes excel at indexing huge datasets that can scale to billions of documents. Use this type of index when you want to perform queries on vector values while maintaining a low memory footprint.
    * Composite Vector indexes contain a single vector column and 1 or more scalar columns. Composite Vector indexes apply scalar filters before performing a vector similarity search. This is ideal for workflows where you want to exclude large portions of the dataset to reduce the number of vectors that the vector search has to compare.
    * Use Search Vector indexes when you need to perform hybrid searches that combine vector searches with other Search Service features, such as text or geospatial search.  
  For more information, see [Filtered Search Using Composite Vector Indexes](../vector-index/composite-vector-index.md) and [Vector Search Using Hyperscale Vector Indexes](../vector-index/hyperscale-vector-index.md).
  * Query Service updates  
  Couchbase Server 8.0 introduces the following enhancements and features to the Query Service, including:

    * New SQL++ statements for Vector Indexes  
      SQL++ has new statements and keywords to create, alter, and drop Hyperscale Vector indexes and Composite Vector indexes. You can also specify the number of dimensions in the vector, the distance metric for comparing vectors, and the settings for quantization and index algorithms.  
      To review these new statements, see [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md) and [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).
    * New data definition language statements  
      SQL++ now supports the following new statements to improve user, group, and bucket management:

      * [CREATE USER](../n1ql/n1ql-language-reference/createuser.md)
      * [ALTER USER](../n1ql/n1ql-language-reference/alteruser.md)
      * [DROP USER](../n1ql/n1ql-language-reference/dropuser.md)
      * [CREATE GROUP](../n1ql/n1ql-language-reference/creategroup.md)
      * [ALTER GROUP](../n1ql/n1ql-language-reference/altergroup.md)
      * [DROP GROUP](../n1ql/n1ql-language-reference/dropgroup.md)
      * [CREATE BUCKET](../n1ql/n1ql-language-reference/createbucket.md)
      * [ALTER BUCKET](../n1ql/n1ql-language-reference/alterbucket.md)
      * [DROP BUCKET](../n1ql/n1ql-language-reference/dropbucket.md)
    * New SQL++ functions for vector comparisons  
      SQL++ has new functions to work with vector values, including:

      * APPROX\_VECTOR\_DISTANCE and VECTOR\_DISTANCE to find the distance between 2 vectors. The APPROX\_VECTOR\_DISTANCE function selects a suitable Hyperscale Vector index or Composite Vector index to use with the query, if 1 is available.
      * ISVECTOR, which checks for a vector value.
      * DECODE\_VECTOR, ENCODE\_VECTOR, and NORMALIZE\_VECTOR, which modify vector values.  
      For more information, see [Vector Functions](../n1ql/n1ql-language-reference/vectorfun.md).
    * Other New SQL++ Functions  
      The following SQL++ functions are also new in Couchbase Server 8.0.

      * [EVALUATE](../n1ql/n1ql-language-reference/metafun.md#evaluate)
      * [COMPRESS](../n1ql/n1ql-language-reference/stringfun.md#fn-str-compress)
      * [UNCOMPRESS](../n1ql/n1ql-language-reference/stringfun.md#fn-str-uncompress)
    * The USING AI Statement  
      The USING AI statement leverages AI capabilities to generate SQL++ queries from natural language prompts. For example, you can input prompts such as "How many airlines are based in Europe?" or "List the names of all hotels in the same city as an airport," and generate the corresponding SQL++ query.  
      For more information, see [USING AI](../n1ql/n1ql-language-reference/using-ai.md).
    * Optimizer hints for DML statements and negative optimizer hints  
      Couchbase Server 8.0 supports optimizer hints with the DELETE, UPDATE, and MERGE statements.  
      In addition, you can now use negative keyspace hints, allowing you to instruct the optimizer not to use certain indexes or join methods. The supported hints are NO\_INDEX, NO\_INDEX\_FTS, NO\_USE\_NL, and NO\_USE\_HASH.  
      For more information, see [Optimizer Hints](../n1ql/n1ql-language-reference/optimizer-hints.md) and [Negative Keyspace Hints](../n1ql/n1ql-language-reference/negative-keyspace-hints.md).
    * Extended attributes (XATTR) support in SQL++  
      You can now modify extended attributes (XATTRs) of documents directly through SQL++ statements such as INSERT, UPSERT, and UPDATE. You can include up to 15 XATTRs per query.  
      For more information, see [INSERT](../n1ql/n1ql-language-reference/insert.md), [UPSERT](../n1ql/n1ql-language-reference/upsert.md), and [UPDATE](../n1ql/n1ql-language-reference/update.md).
    * Auto-reprepare feature for prepared statements  
      Couchbase Server 8.0 includes an auto-reprepare feature for PREPARE statements. When enabled, a prepared statement automatically updates its query plan whenever GSI metadata version changes, ensuring it always uses newer, more efficient indexes as they become available.  
      For more information, see [PREPARE](../n1ql/n1ql-language-reference/prepare.md).
    * Enhanced logging for completed requests  
      You can now log query requests using 2 new qualifiers: statement and plan. This allows for logging based on the query text or specific values within the query plan.  
      For more information, see [Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-completed-req).
    * Additional options for the INFER statement  
      The INFER statement now supports the following options: `array_sample_size`, `max_nesting_depth`, and `flags`. Additionally, this statement now automatically returns the `meta.id()` attribute, which provides the document keys in the output.  
      For more information, see [INFER](../n1ql/n1ql-language-reference/infer.md).
  * New Search Service features  
  Couchbase Server 8.0 introduces several new features for the Search Service, including:

    * Partition selection for queries Use the `partition_selection` property in a search request to choose how the Search Service chooses the specific partitions to search for a query.  
      For more information, see [partition\_selection](../search/search-request-params.md#partition%5Fselection).
    * Synonym searches Add a synonym collection and synonym documents to add synonym search support to a Search index. Use synonyms to return matches for words that share the same meaning as the term in your Search query, instead of exact matches.  
      For more information, see [Add Synonyms to a Search Index](../search/synonyms/synonyms-search.md).
    * Custom document filters Instead of the [default type identifiers](../search/customize-index.md#type-identifiers), you can now create [custom document filters](../search/set-type-identifier.md#custom) to control the documents added to your Search index from a type mapping.  
      For more information, see [Set a Document Filter](../search/set-type-identifier.md).
    * New Search Index algorithm Couchbase Server 8.0 supports the `bm25` algorithm for scoring search results. The `bm25` algorithm supports better hybrid searches and richer result rankings, as well as more stable result ordering across Search index partitions.  
      You can now choose to use `tf-idf` or `bm25` from your [Search index settings](../search/set-advanced-settings.md#scoring%5Fmodel).  
      For more information about how `bm25` scoring works, see [Scoring for Search Queries](../search/run-searches.md#scoring).  
  > [!NOTE]  
  > For more information about this version of Couchbase Server, see [Couchbase Server 8.0](../../server/current/release-notes/relnotes.md#release-80).
* Expanded AWS region availability  
Couchbase Capella supports 2 new AWS regions, including:

  * Mexico (Mexico City)
  * Asia Pacific (Thailand)
* Data API Support for Capella Operational Clusters  
The Couchbase Capella Data API is now available. The Data API is a fully managed service that provides programmatic access to data in Capella clusters over HTTPS-based REST APIs, without the need for SDKs or drivers. Users must explicitly enable Data API access for clusters deployed in free or paid tenants.  
For more information about the Data API and how to get started, see [Manage Data with the Data API](../data-api-guide/data-api-intro.md).
* Enhancements to Capella Cluster Backups  
Capella cluster backups now support cross-region backup replicas and restores, adding better reliability for restoring your cluster. Replicate your cluster backups on-demand or on a schedule to additional regions, for better data resilience when you have strict requirements for business continuity or compliance.  
Cross-region backup replication and restores are only available on clusters hosted through AWS or Azure.  
For more information, see [Back Up and Restore An Entire Cluster](../clusters/cloud-snapshots.md).
* Create SQL++ and JavaScript User-Defined Functions (UDFs) from Data Tools  
You can now create and manage UDFs directly from your cluster’s Data Tools > Query Tab, using either SQL++ inline expressions or JavaScript functions.  
Use UDFs to write, edit, and manage reusable logic for your cluster. You can define UDFs using the [CREATE FUNCTION statement](#n1ql:n1ql-language-reference/create-function.adoc) or the [Query Tab UI](../guides/create-user-defined-function.md).  
For more information, see [User-Defined Functions with JavaScript](../guides/javascript-udfs.md) or [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md).

## [](#september-2025-changelog)September 2025 Changelog

## [](#august-2025-changelog)August 2025 Changelog

* Couchbase Server 7.6.7  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.7 maintenance release.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.7](../../server/7.6/release-notes/relnotes.md#release-767).
* Fine-grained access for cluster access credentials, and other enhancements  
Capella’s Role-Based Access Control (RBAC) now reaches the collection level, so you can assign cluster access credentials privileges at the bucket, scope, or collection level. This finer level of control simplifies least-privilege design and leaves all existing bucket and scope-level roles fully intact.  
You can also now generate a password for your cluster access credentials with a single click.  
For more information, see [Manage Cluster Access Credentials](../clusters/manage-database-users.md).

## [](#july-2025-changelog)July 2025 Changelog

* Announcing Customer Self-Service Upgrades  
You can now schedule and manage operational cluster upgrades on your own timeline without the need to open a support ticket. This new feature offers a simplified upgrade experience. By giving you more control, you can speed up the adoption of fixes and improvements that keep your cluster up to date and performing at their best.  
For more information, see [Upgrading a Cluster](../clusters/upgrade-database.md).
* GCP Private Service Connect is now available as a network access management option  
With private endpoints, you can use GCP Private Service Connect to connect a GCP VPC to Couchbase Capella. The benefits of this include:

  * Private endpoint traffic does not travel through the Internet, allowing services to function as if you host them within your GCP VPC.
  * Private endpoints only provide access to a specific service or application, whereas VPC peering gives access to all resources in your VPC.
  * Private endpoints support CIDR overlap.
  * Only private endpoints can initiate a connection, providing uni-directional access.  
For more information about how to start using GCP Private Service Connect with Capella, see [Add a GCP Private Service Connection](../security/add-gcp-private-link.md).

## [](#june-2025-changelog)June 2025 Changelog

* Enhancements to Capella Cluster Backups  
Capella Cluster Backups have been updated to ensure better reliability and flexibility during restoration:

  * You can now retain cluster backups, even after deleting a cluster, through a new project-level **Backups** tab.
  * You can now restore an existing cluster backup to another compatible cluster in the same project, or use a backup to create an entirely new cluster with the same storage and configuration.  
For more information, see [Back Up and Restore An Entire Cluster](../clusters/cloud-snapshots.md).
* Added support for OpenID Connect (OIDC) single sign-on (SSO)  
You can now configure an OIDC identity provider as an alternative to SAML for streamlined authentication and improved compatibility.  
For more information, see [Capella UI Authentication](../organizations/ui-auth/capella-ui-auth.md).
* Set up single sign-on (SSO) for your organization using Capella UI without a support ticket  
Organization owners using a paid plan can now configure and manage SSO without needing to create a support ticket.  
For more information, see [Add SSO Authentication](../organizations/ui-auth/add-sso-auth.md).
* Expanded Azure region availability  
Couchbase Capella supports 2 new Azure regions, including:

  * South Central US (Texas)
  * North Europe (Ireland)  
These Azure regions are available only on request. For more information, [contact Couchbase Support](../support/manage-support.md#create-support-ticket).  
For a list of all Azure regions that Capella now supports, see [Azure Supported Regions](../reference/azure.md#supported-regions).

## [](#may-2025-changelog)May 2025 Changelog

* Couchbase Server 7.6.6  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.6 maintenance release. This version includes bug fixes.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.6](../../server/7.6/release-notes/relnotes.md#release-7-6-6-may-2025).
* Credit Card Billing Support  
Capella now supports credit card billing as a payment method for paid cluster and service usage. You can add a credit card directly through the Capella UI to upgrade from free tier to a paid environment, with no sales interaction.  
Credit card billing supports the Basic and Developer Pro Support Plans. All charges are billed automatically in USD on the seventh day of each month.  
For more information about credit card billing, see [Manage Your Billing](../billing/billing.md).

## [](#april-2025-changelog)April 2025 Changelog

* Replication now available on single node clusters  
For ease of development and testing, you can now create Cross Data Center Replications (XDCR) on single node clusters.  
For more information about XDCR, see [Cross Data Center Replication (XDCR)](../clusters/xdcr/xdcr.md).
* Expanded Azure region availability  
Couchbase Capella now supports the Central US (Iowa) region.  
For a list of all Azure regions that Capella now supports, see [Azure Supported Regions](../reference/azure.md#supported-regions).

## [](#march-2025-changelog)March 2025 Changelog

* Adjustable IOPS for 100-199 GB Disks in AWS  
You can now lower IOPS for 100-199 GB AWS storage disks from a default of 4370 to a minimum of 3000 IOPS.  
This minimum IOPS setting helps you reduce costs for workloads with consistently lower IOPS needs while maintaining 20-30% extra IOPS for cluster management tasks, like scaling and upgrades.  
For more information, see [AWS IOPS Defaults](../clusters/scale-database.md#aws-iops).

## [](#february-2025-changelog)February 2025 Changelog

* Expanded Azure region availability  
Couchbase Capella supports 3 new Azure regions, including:

  * France Central (Paris) \[[1](#footnote-2)\]
  * Spain Central (Madrid) \[[1](#footnote-2)\]
  * Southeast Asia (Singapore)  
For a list of all Azure regions that Capella now supports, see [Azure Supported Regions](../reference/azure.md#supported-regions).  
\[1\] This Azure region is available only on request. For more information, [contact Couchbase Support](../support/manage-support.md#create-support-ticket).
* Couchbase Server 7.6.5  
Creating a new operational cluster with Couchbase Server 7.6 now deploys the Couchbase Server 7.6.5 maintenance release. This version includes bug fixes and changes found in Couchbase Server 7.6.4.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.5](../../server/7.6/release-notes/relnotes.md#release-7-6-5-january-2025) and [Couchbase Server 7.6.4](../../server/7.6/release-notes/relnotes.md#release-7-6-4-december-2024).

## [](#january-2025-changelog)January 2025 Changelog

* Ability to Pause Your On/Off Schedule  
You can now pause the on/off schedule for your operational cluster. This eliminates the need to delete the schedule when you do not want the cluster to turn on or off at the scheduled time. When you’re ready, you can reactivate the schedule without needing to recreate it, saving time and memory.  
For more information, see [Pause Cluster Schedule](../clusters/off-on-schedule.md#pause-cluster-schedule).
* Capella Search Service UI Redesign  
The process for creating a Search index in the Datatools - Search tab has been redesigned. Building simple Search indexes is more straightforward. Turn on **Advanced Mode** to add more customization and advanced features to a Search index.  
For more information, see [Create a Search Index](../search/create-search-indexes.md).
* Legacy Management API v3.0  
The legacy Management API v3.0, formerly known as the Public API, has been removed from Couchbase Capella.

## [](#december-2024-changelog)December 2024 Changelog

* Announcing Capella Health Advisor  
Use Capella Health Advisor to get proactive, actionable recommendations to optimize your operational clusters. Stay informed about your cluster’s health, configuration, performance, and usage trends with insights that help you maximize uptime and efficiency.  
Take control and use Health Advisor’s ready-to-use suggestions to simplify and improve your cluster’s health management.

To get started and learn more about Health Advisor, see [View Health Advisor](../clusters/monitoring/health-advisor.md).

## [](#november-2024-changelog)November 2024 Changelog

* Visualize Query Results with iQ Insights  
After running a query, you can use iQ Insights to generate a variety of relevant graphs and charts with the help of AI. Use iQ insights to better understand your data and gain more insights from your query results.  
iQ Insights is available to use with both Capella Operational and Capella Analytics clusters.  
For more information, see [Explore iQ Insights](../get-started/capella-iq/explore-iq-insights.md).
* Single Node Scaling  
You can now modify your Single Node operational cluster by scaling out to a Multi-Node cluster, switch to a larger VM, and change services as needed. Certain limitations apply to the available configuration options.  
For more information about these limitations, see [Modify a Paid Cluster](../clusters/modify-database.md#modify-existing-service).

## [](#october-2024-changelog)October 2024 Changelog

* Improvements to Single Sign-On (SSO)  
Capella now includes several new features designed to enhance your experience with realm management, SSO processes, and user management:

  * [Customize realm names](../organizations/ui-auth/manage-identity-providers.md#change-realm-name) to make them more memorable and identifiable.
  * Simplify the sign-in process for your SSO users by [providing a link to the sign-in screen that prepopulates the realm name](../organizations/ui-auth/manage-identity-providers.md#access-realms).
  * [Update the signing certificates](../organizations/ui-auth/manage-identity-providers.md#change-cert) without recreating the realm, reducing downtime and simplifying SAML certificate rotation.
  * [Individually or batch remove SSO users using the Capella UI](../organizations/manage-organization-users.md#remove-user-sso), improving compliance and user management efficiency.

## [](#september-2024-changelog)September 2024 Changelog

* Capella iQ User Feedback  
Users can now provide feedback on the accuracy of iQ results in the Capella UI by clicking the thumbs-up or thumbs-down button. Your feedback directly enhances the quality of SQL++ query generation, making iQ more intuitive and effective for your needs.  
If you’re new to Capella iQ, see [Get Started with Capella iQ](../get-started/capella-iq/get-started-with-iq.md).
* Cluster Deletion Protection  
For additional protection for your sensitive clusters, you can block any attempt to delete a cluster by enabling deletion protection in your cluster settings. Deletion protection will also block attempts to delete a cluster’s buckets and any linked App Services. For more information about deletion protection, see [Change Your Deletion Protection](../clusters/modify-database.md#deletion-protection).
* Couchbase Server 7.6.3  
When you create a new cluster with Couchbase Server Version 7.6 selected, it uses Couchbase Server 7.6.3\. This version includes bug fixes.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.3](../../server/7.6/release-notes/relnotes.md#release-7-6-3-september-2024).
* Private-only access to clusters  
> [!IMPORTANT]  
> The option to create a cluster with restricted public access is available only on request. For more information, [contact Couchbase Support](../support/manage-support.md#create-support-ticket).  
The restrict public access option is available when creating a [new cluster](../clusters/create-database.md). When your cluster has restrict public access turned on, you can only connect to it through Capella’s private networking options, including [VPC peering](../clouds/private-network.md) and private endpoints.  
For example, with this option enabled, only your cloud service provider (CSP) network that’s peered with Capella can access your cluster. This configuration allows direct traffic routing from your on-premises network to Capella through your CSP’s network that’s peered with Capella.  
For more information, see [Restrict Public Access](../security/security.md#public-access).
* GCP Private Service Connections  
> [!IMPORTANT]  
> Adding a GCP Private Service Connection is available only on request. For more information, [contact Couchbase Support](../support/manage-support.md#create-support-ticket).  
Use [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) to peer your GCP network with Capella when your cluster uses GCP as its cloud provider. The benefits of this include:

  * Private endpoint traffic does not traverse the Internet, allowing services to function as if you hosted them within your GCP network.
  * Private endpoints provide access to only a specific service or application, unlike VPC peering, which allows access to all resources.
  * Private endpoints support CIDR overlap.
  * Only private endpoints can initiate a connection.  
To learn more about using GCP Private Service Connections with Capella, see [Add a GCP Private Service Connection](../security/add-gcp-private-link.md).
* Announcing Capella Free Tier  
Couchbase Capella now supports a forever free tier offering to replace the 30-day Capella free trials.  
The free tier allows developers to get started with Capella without any financial commitment, making it ideal for learning, development, and small projects.  
The free tier is available in perpetuity without being encumbered by time limits so long as the cluster is actively used, making it suitable for exploration and evaluation of new features when they’re available.  
For first time users, [create an account](../get-started/create-account.md) to get started with your free tier operational cluster.

## [](#august-2024-changelog)August 2024 Changelog

* Terminology changes in Capella  
With the introduction of a new Capella service, Capella Analytics, Couchbase has introduced the following terminology changes to improve clarity:

  * Capella service names  
  The Capella documentation introduces these terms to distinguish between the two available services:

    * _Capella operational_ refers to the original Database-as-a-Service (DBaaS), introduced in 2021.
    * _Capella Analytics_ refers to a new column-oriented DBaaS designed to handle large-scale analytical workloads.  
      Together, these offerings provide both translational (OLTP) and analytical (OLAP) capabilities in the same platform.
  * Operational terminology update  
  In Capella operational, the top level entity within Capella operational has been changed from database to cluster. Couchbase made this change to better align with terminology used in traditional RDMS and with our new Analytics offering. With this change, Capella operational entities are now:

    * Cluster
    * Bucket
    * Scope
    * Collection
    * Document
* Backup Checksum Support  
You can now retrieve a SHA-256 checksum to verify your downloaded backup files.  
For more information about the new checksum feature, see [Using A Downloadable Backup Checksum](../clusters/backup-restore.md#checksum).
* Redesigned Cluster Deployment Experience  
Capella’s cluster deployment experience has been redesigned to provide more flexibility and better guidance to get you started. Take advantage of new cluster options to make it easier to deploy exactly what you need:

  * Use the Single Node cluster option for prototyping and experimentation at a low cost.
  * Use a Multi-Node cluster template and quickly get the ideal configuration for the Services you need.
  * Take full control with the Custom cluster option and choose exactly what you need for an enterprise workload.  
See your available pre-paid credits at a glance and get a breakdown of estimated costs that updates as you configure your cluster. Choose a specific Availability Zone (AZ) when deploying to a single AZ on AWS. Use Private Links with a single AZ on AWS or Azure. For more information about the new cluster deployment experience, see [Create A Paid Cluster](../clusters/create-database.md).
* Full Cluster Backups with Cloud Snapshots  
Easily backup your entire cluster using cloud native snapshot backups. A cluster backup, or cloud snapshot backup, uses your cloud service provider’s storage snapshot service to backup your entire cluster, including all of its buckets, in a single backup. Benefits over individual bucket backups include:

  * Back up all your data, and indexes — everything in your cluster storage at once, with one backup schedule.
  * Restore all your data, indexes, and other cluster artifacts at the same time, with no need to build indexes.
  * Backups do not affect cluster performance and resources.
  * Get consistent, short backup and restore times, regardless of dataset size.
  * Improved RPO and RTO — especially for clusters with large datasets.
  * Supports cluster storage encryption at rest using the Customer Managed Encryption Keys (CMEK) feature.  
For more information, see [Back Up and Restore An Entire Cluster](../clusters/cloud-snapshots.md).
* The billing reporting experience has been updated to provide more detailed information about your credit usage among Couchbase Capella’s services, including App Services and clusters. These updates include:

  * An [overview of your organization’s credit usage](../billing/manage-billing.md#access-billing).
  * [Granular filtering and reporting](../billing/manage-billing.md#filter-usage) of all credit usage.
  * [Alerting](../billing/manage-billing-alerts.md) for credit balances and pay-as-you-go usage.

## [](#july-2024-changelog)July 2024 Changelog

* Couchbase Server 7.6.2  
When you create a new cluster with Couchbase Server Version 7.6 selected, it uses Couchbase Server 7.6.2\. If you want to upgrade an existing cluster to Couchbase Server 7.6.2, contact Couchbase Support.  
This version includes the following features:

  * The ability to store vector embeddings in efficiently compressed base64 encoded strings.
  * Create Search Indexes that use XATTRS in Advanced Mode, and run search queries or use SQL++ search functions to return document metadata with the Search Service.  
For more information about this version of Couchbase Server, see [Couchbase Server 7.6.2](../../server/7.6/release-notes/relnotes.md#release-7-6-2-july-2024)
* Expanded GCP region availability  
Couchbase Capella supports 2 new Google Cloud regions, including:

  * Middle East Central (Dammam)
  * Africa South (Johannesburg)\[[1](#footnote-1)\]  
\[1\] App Services are not supported in this region.  
For a list of all 37 GCP regions that Capella now supports, see [GCP Supported Regions](../reference/gcp.md#supported-regions).

## [](#june-2024-changelog)June 2024 Changelog

* A new connection method is now available on the Connect page in the Capella UI: IDE Plugins and Extensions  
You can now [connect to your cluster](../get-started/connect.md) using a Couchbase IDE plugin or extension:

  * [Couchbase Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-couchbase)
  * [Couchbase VS Code extension on Open VSX](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-cblite)
  * [Couchbase Plugin for JetBrains](https://plugins.jetbrains.com/plugin/22131-couchbase)  
For more details, see [IDE Integrations](../third-party/integrations.md#ide-integrations).

## [](#may-2024-changelog)May 2024 Changelog

* Migrate from a Couchstore bucket to Magma using the Capella Management API v4.  
For clusters using Couchbase Server 7.6 or later, Capella now supports online migration from Couchstore to Magma storage engines using the [Capella Management API](../management-api-reference/index.md#tag/Clusters/operation/putBucketStorageBackend).
* Custom subdomains in Capella endpoints  
You can now customize the Capella endpoints — such as URLs for clusters, private links, and nodes — with unique identifiers. This option is currently only available for AWS clusters through the [Capella Management API](../management-api-reference/index.md).  
You must reach out to Couchbase support to enable this feature.

## [](#april-2024-changelog)April 2024 Changelog

* Introducing social sign-in: seamlessly access Capella with Google and GitHub  
You can now sign in to Capella using your existing Google or GitHub accounts. Social sign-in includes:

  * Simplified Access: Skip the hassle of creating and remembering another set of credentials. Use your existing Google or GitHub account for a quick and easy sign-in process.
  * Enhanced Security: Take advantage of the security protocols of Google and GitHub. Your sign-in process is as secure as your social accounts, ensuring peace of mind.
  * Streamlined User Experience: Enjoy a more fluid and integrated experience. Access Capella with just a few clicks, making the transition smooth and efficient.  
For more information, see [Link Your Capella Account to a Google or GitHub Account](../organizations/manage-account.md#link-social-account).
* Couchbase Server 7.6.1  
When you create a new cluster with Couchbase Server Version 7.6 selected, it uses [Couchbase Server 7.6.1](../../server/7.6/release-notes/relnotes.md#release-7-6-1-april-2024).

## [](#march-2024-changelog)March 2024 Changelog

* Replication (XDCR) now supports the Filter Binary option  
For additional flexibility, Set Up Replication filtering options now include an option to disable the replication of binary documents.
* Alert Notification Integrations using Webhook  
Get notified in the toolset of your choice by integrating Capella alert notifications with third-party tools like ServiceNow and more, using an incoming Webhook.  
Customers can now configure alert integrations in Capella at the project level using UI or public management APIs. On the receiving side, you can leverage the payload sent with cluster alert notifications to automate workflows and further meet your organizational observability needs.  
For more information, see [Alert Integrations](../clusters/monitoring/alert-integration.md).
* Couchbase Server 7.6 on Capella with Vector Search  
Capella now supports Couchbase Server 7.6 and you can choose this version when creating a new cluster. If you want to upgrade an existing cluster to Couchbase Server 7.6, contact Couchbase Support.  
This version includes the following features:

  * Vector Search to enable AI integration, semantic search, and the Retrieval-Augmented Generation (RAG).  
  Get a developer-friendly vector indexing engine to use a vector cluster and search functionality. With Couchbase Capella Vector Search, you can enable fast and highly accurate semantic search, ground LLM responses in relevant data to reduce hallucinations, and enhance or enable use cases like personalized searches in e-commerce and media & entertainment, product recommendations, fraud detection, and reverse image search. You can also enable full access to an AI ecosystem with a LangChain integration, the most popular open-source framework for LLM driven applications.  
  A Vector Search vector cluster includes:

    * Standard Couchbase vertical/horizontal scaling
    * Indexing capable of efficient Insert/Update/Removal of Items (or documents)
    * Storage of raw Embedding Vectors in the Data Service in the documents themselves
    * Querying Vector Indexes (REST and UI via a JSON object/fragment, Couchbase SDKs, and SQL++)
    * SQL++/N1QL integration
    * Third-party framework integrations: LangChain and LlamaIndex (with future integrations planned)
    * Full support for Replicas Partitions and file-based Rebalance  
  To start using Vector Search in the Capella UI, go to **Data Tools** **Search** from a 7.6 cluster. For more information about Vector Search in Capella, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md).
  * \_system scope  
  In Couchbase Server Version 7.6 and later, all sample buckets and buckets that you create include a `_system` scope. When upgrading to a cluster to Couchbase Server 7.6, Capella adds the `_system` scope to your existing buckets.  
  The `_system` scope contains the `_mobile` and `_query` collections that store system documents for related Couchbases services. The `_system` scope and its collections are read-only, and their structure is subject to change without notice. Do not use these collections for other purposes. You cannot drop the `_system` scope or its collections.
  * Changes to the maxTTL setting for collections  
  In earlier versions, you could only set a collection’s TTL setting when creating the collection. You can now change the TTL setting on a collection after creation.  
  You can now set a collection’s TTL to `-1` to prevent a bucket’s non-zero TTL setting from causing documents in the collection to expire automatically. This new setting is useful if you want most of the documents in a bucket to automatically expire, but want to prevent the documents in one or more collections from expiring by default.  
  For more information, see [Expiration](../../server/current/learn/data/expiration.md).
  * Bucket priority  
  An option is now available to specify relative bucket priority when creating a bucket or updating bucket properties using the Capella Management API. When set, buckets recover in the order specified during failover to improve application availability. This option is only available through the [Capella Management API](../management-api-reference/index.md).
  * Updates to the Eventing Service:

    * The new optional parameter `{ "self_recursion": true }` can be used with the INSERT, UPSERT, and REPLACE advanced operations to prevent the suppression of recursive source bucket mutations.
    * The new built-in `ANALYTICS()` function allows the Eventing Service to integrate directly with SQL++ Analytics. This integration simplifies Eventing code logic and lets Eventing benefit from the high availability and load balancing of SQL++ Analytics.
    * The new advanced TOUCH operation allows you to modify the expiration time of a document without having to access that document first.
    * The Sub-Document MUTATEIN operation allows you to modify only parts of a document instead of the entire document. This Sub-Document operation is faster and more efficient than a full-document operation like REPLACE or UPSERT.  
  For more information about Eventing updates, see [Language Constructs](../../server/current/eventing/eventing-language-constructs.md) and [Advanced Keyspace Accessors](../../server/current/eventing/eventing-advanced-keyspace-accessors.md).
* Support for Customer Managed Encryption Keys (CMEK) is now available for clusters deploying with AWS and GCP  
Use Customer-Managed Encryption Keys (CMEK) to control the encryption keys you use to secure your data. In Capella clusters using CMEK, data is encrypted using encryption keys that you generate and manage in your own Key Management System (KMS) instead of the Capella-managed KMS. CMEK gives you greater control over data security, enabling you to manage key creation, key rotation, access control, and allow for independent auditing. For organizations with strict compliance and regulatory requirements, CMEK can help meet data protection standards.  
For more information, see [Use Customer-Managed Encryption Keys (CMEK)](../security/cmek.md).

## [](#february-2024-changelog)February 2024 Changelog

* Enhancements to the Eventing Service in Capella  
The user interface of the Eventing Service in Capella has been redesigned. You can now add Constant bindings to define fixed values for your Eventing functions. You can now also view your logs after deploying an Eventing function.  
For more information, see [Add Eventing to Your Application](../eventing/eventing-overview.md).
* Expanded Azure region availability  
Couchbase Capella supports 2 new Azure regions, including:

  * Germany West Central (Frankfurt)
  * UAE North (Dubai)  
For a list of all Azure regions that Capella now supports, see [Azure Supported Regions](../reference/azure.md#supported-regions).

## [](#january-2024-changelog)January 2024 Changelog

* Capella iQ is now available  
Capella iQ is your partner in Capella, allowing you to work faster and assist you directly in the Capella UI. Using natural language prompts, you can complete common cluster application development tasks. Use Capella iQ to create and optimize SQL++ queries, sample data, starter SDK code, and more.  
To start using Capella iQ in the Capella UI, click **Data Tools** **Query**.  
For more information, see [Work Faster with Capella iQ](../get-started/capella-iq/work-with-capellaiq.md).

## [](#december-2023-changelog)December 2023 Changelog

* Storage Auto-Expansion is now available on Azure  
Capella now provides the storage auto-expansion feature for Azure. Storage auto-expansion automatically scales your storage capacity as your data grows over time. You can enable storage auto-expansion on any existing or new clusters. You will incur charges for the extra storage only when the system triggers a capacity increase.  
For more information, see [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion).
* Hashicorp Terraform Provider 1.0.0 is now available  
Version 1.0.0 of [Terraform Provider for Capella](https://registry.terraform.io/providers/couchbasecloud/couchbase-capella/latest) is now available. The first version of the Provider can be used for programmatically managing Capella resources including API keys, users, projects, cluster buckets, App Services, and bucket backups. The provider will be continually enhanced to include support for further resources.

## [](#november-2023-changelog)November 2023 Changelog

* Expanded AWS region availability  
Couchbase Capella now supports the Israel (Tel Aviv) region.  
For a list of all 25 AWS regions that Capella now supports, see [AWS Supported Regions](../reference/aws.md#supported-regions).
* Expanded GCP region availability  
Couchbase Capella supports 5 new Google Cloud regions, including:

  * US East (Columbus)
  * US West (Los Angeles)
  * US South (Dallas)
  * Europe West (Paris)
  * Europe Southwest (Madrid)  
For a list of all 35 GCP regions that Capella now supports, see [GCP Supported Regions](../reference/gcp.md#supported-regions).
* Pre-authorize support to take action on failing clusters  
Use **Request prompt action for cluster recovery** to pre-authorize Capella Support to quickly take remediation actions on clusters that are in a critical health state. Keep this feature enabled at all times to minimize service disruptions.  
For more information, see [Request Prompt Action for Cluster Recovery](../billing/support-pre-auth.md).

## [](#october-2023-changelog)October 2023 Changelog

* Hashicorp Vault Plug-in  
The initial release of [Couchbase Capella Vault plug-in](https://www.hashicorp.com/partners/tech/couchbase#vault) is now available. This plugin is a powerful and secure solution for cluster integration with Hashicorp Vault. It enables seamless and secure access to clusters while leveraging Hashicorp Vault’s robust secret management capabilities.
* Expanded Microsoft Azure region availability  
Couchbase Capella now supports the Switzerland North (Zürich) region.
* Expanded AWS region availability  
Couchbase Capella supports 9 new AWS regions, including:

  * Africa (Cape Town)
  * Asia Pacific (Hong Kong)
  * Asia Pacific (Hyderabad)
  * Asia Pacific (Jakarta)
  * Asia Pacific (Melbourne)
  * Europe (Milan)
  * Europe (Zurich)
  * Middle East (Bahrain)
  * Middle East (UAE)  
For a list of all 24 AWS regions that Capella now supports, see [AWS Supported Regions](../reference/aws.md#supported-regions).

## [](#september-2023-changelog)September 2023 Changelog

* SDK Playground Enhancements  
We have added Go SDK tutorial support to the [SDK Playground](../get-started/sdk-playground.md).  
In addition, users can the edit SDK code samples available in the Playground SDK tutorials in a controlled manner, trying out the code snippets with different SDK options or outputs. Users cannot make changes that access networks outside the Capella environment, nor can they access the underlying infrastructure.
* Couchbase Server 7.2 is now available in Capella for new clusters.  
Couchbase Server 7.2 in Capella includes the following features:

  * Cost Based Optimizer for Analytics (CBO). The cost-based optimizer for Analytics chooses the optimal plan to execute an Analytics query. The cost-based optimizer gathers and utilizes samples from Analytics collections, and then queries the samples at query planning time to estimate the cost of each operation. The Analytics Service introduces new syntax for managing samples, and provides parameters and hints to help specify the behavior of the cost-based optimizer. See [Cost-Based Optimizer for Analytics](../guides/cbo.md).
  * Time Series Queries. Time series data is any data that changes over time. It’s usually collected frequently, in regular or irregular intervals, from a device or a process. The Query Service provides a standard format for time series data, which promotes compact storage and quick processing, and introduces a \_TIMESERIES function to query time series data. See [Time Series Data](../n1ql/n1ql-language-reference/time-series.md) and the [\_TIMESERIES Function](../n1ql/n1ql-language-reference/timeseries.md).
  * Remote analytics links to Azure Blob Storage and GCP Cloud Storage. See [Analytics Links](../clusters/analytics-service/analytics-links.md).  
To upgrade an existing cluster to Couchbase Server 7.2, please contact Couchbase Support.
* Management API v4.0  
The Couchbase Capella Management API v4.0 is now available. The Management API v4.0 is a secure REST API that enables you to provision, deploy, and configure Capella deployments programmatically across all supported cloud service providers. You can use the API within any off-the-shelf HTTP clients, or within your Infrastructure-as-Code (IaC) tools and scripts.  
The legacy Management API v3.0, formerly known as the Public API, has been deprecated and will be removed in future. Users of the Management API v3.0 must plan to migrate to the Management API v4.0.  
For more information, see [Manage Deployments with the Management API](../management-api-guide/management-api-intro.md).

## [](#august-2023-changelog)August 2023 Changelog

* Payment Card Industry Data Security Standard (PCI DSS) attestation of compliance (AoC)  
Capella’s PCI DSS version 4.0 compliant controls, which have been verified by an independent third-party auditor, help organizations manage and store credit card financial data on the platform.
* CSA STAR  
Couchbase has received a CSA STAR Level 2 certification for attestation of compliance, following an external security audit of Capella.  
See the [Cloud Trust Center](https://www.couchbase.com/products/capella/trust/) for additional information on the security controls and compliance of the platform.
* Filtering enhancements to Capella Replications  
Capella has already provided support for the creation of _filter expressions_. These allow you to _filter_ items (so that the items are selectively included in or excluded from the replication) by referencing _document IDs_, _X-attributes_, and _values_. Now, to support the creation of complex expressions, a _syntax-checker_ and an _expression-tester_ are added.  
Additionally, to support archival use-cases, Capella provides filters that remove _delete operations_, _document expirations_, and _Time To Live (TTL) configurations_ from replicated items.  
See [Create a Replication Between Capella Clusters](../clusters/xdcr/manage-xdcr-replications.md#between-capella-dbs).
* On-demand and Scheduled Hibernation of Provisioned Clusters (On/Off)  
You can now turn off your non-production provisioned clusters when you are not using them, allowing you to save on costs. Turning off your cluster turns off the compute for your cluster but the storage remains — this means that all of your data, schema (buckets, scopes, collections), and indexes remain, as well as your cluster configuration, including users and allow lists. You can turn on and off your cluster [on-demand](../clusters/off-on-database.md) or using a [schedule](../clusters/off-on-schedule.md). For example, you can set a schedule for your development cluster to be on from 9 am to 5 pm on week days and off at all other times. Any linked App Service will also be turned off when the linked cluster is turned off.
* Capella integration on Vercel marketplace  
Couchbase Capella is now available on [Vercel’s Integration Marketplace](https://vercel.com/integrations). This seamless integration will allow developers to fully leverage the strengths of both technologies, enabling them to create web applications that are scalable, resilient, and performant.

## [](#july-2023-changelog)July 2023 Changelog

* Expanded Google Cloud region availability  
Couchbase Capella now supports the GCP Tel Aviv (`me-west1`) region.
* Couchbase Capella has a refreshed Data Tools tab. Highlights include:

  * [Simplified Data Import](../clusters/data-service/import-data-documents.md)
  * [Streamlined Document Management](../clusters/data-service/manage-documents.md)
  * [Integrated visual interface for query development and testing](../clusters/query-service/query-workbench.md#query-editor)
  * [Schema browser](../clusters/query-service/query-workbench.md#insights-sidebar)
  * [Performance Optimization](../clusters/query-service/query-workbench.md#index-advice)
  * [Index Advisor window](../clusters/query-service/query-workbench.md#index-advice)
  * [View Charts](../clusters/query-service/query-workbench.md#query-chart)
  * Improved creation of Search Index
* Changes to IOPS and Storage Auto-Expansion  
To further enhance cluster performance, reliability, and availability, IOPS and Storage Auto-Expansion have the following changes:

  * [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion) is now mandatory for new clusters in Capella. With Storage Auto-Expansion turned on, Couchbase bills you only for the additional storage capacity when the limit increase triggers.
  * Capella now automatically adjusts the IOPS to match the [recommended settings](../clusters/scale-database.md#IOPS-Defaults) for the storage capacity of your cluster. You can replace the default IOPS value in the UI with a value that’s higher than the default but not lower.
* Expanded Microsoft Azure region availability  
Couchbase Capella supports three new Azure regions, including:

  * East US 2 (Virginia)
  * West US 2 (Washington)
  * East Asia (Hong Kong)  
For a list of all 14 Azure regions that Capella now supports, see [Microsoft Azure Supported Regions](../reference/azure.md#supported-regions).
* Single Sign-On (SSO) enhancements

  * Support for Google Workspaces and OneLogin.  
  The list of supported identity providers is now:

    * Microsoft Azure AD
    * Okta
    * Ping
    * CyberArk
    * Google Workspaces
    * OneLogin  
  To configure Capella with any of these supported identity providers, see [Add SSO Authentication](../organizations/ui-auth/add-sso-auth.md).
  * A generic SAML integration feature that allows integration with your SAML 2.0 provider, even if it’s not in the supported identity provider list.  
  > [!NOTE]  
  > While you can configure Capella with other SAML identity providers, Couchbase provides instructions and support for only those identity providers on the supported identity provider list.
* Backups can now be downloaded from Capella  
You can now [download backups](../clusters/backup-restore.md#downloading-backups) and store or use them outside Capella. Downloads are zip archive files of on-demand bucket backups or completed backup cycles of scheduled bucket backups. When downloaded onto your machine, you can store backups for retention or availability requirements. Use [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) to restore data to another Couchbase cluster.

## [](#june-2023-changelog)June 2023 Changelog

* Cluster audit logging is now available for Azure-hosted clusters  
Capella provides auditing, where you can download cluster audit logs for inspection or archiving. This feature helps with investigations and meeting organizational security or compliance requirements. Cluster auditing is now available on Capella Azure-hosted clusters with the Enterprise plan.

> [!NOTE]
> This feature is available on new clusters. Couchbase is upgrading existing clusters so all Azure enterprise customers can use this feature. If auditing isn’t yet available for your cluster, open a support ticket so we can prioritize your cluster upgrade to get you using audit logging with your existing Azure clusters as soon as possible.

* Connect tab in the Capella UI  
To simplify the developer journey of connecting to Capella, a new Connect tab is now available on Capella UI. The Connect tab has information about the necessary connection parameters, prerequisites, installation instructions, code snippets, full code samples, and examples for different connection methods—​including SDK samples and snippets for three languages, Couchbase Shell, and Couchbase CLI tools for managing the cluster.  
See [Generate Your Connection Code](../get-started/connect.md) and [Import and Export Data with Command Line Tools](../connect/cli-import-export.md) for more information.

## [](#may-2023-changelog)May 2023 Changelog

* XDCR replications can now be created from Capella to self-managed clusters.  
In addition to being able to create an XDCR replication from your self-managed cluster to Capella, you can now create an XDCR replication _from Capella to your self-managed cluster_, using the Capella console. Add your self-managed cluster target reference information, and select the self-managed cluster as a target. For more information, see [Create a Replication from Capella to a Self-Managed Cluster](../clusters/xdcr/manage-xdcr-replications.md#from-capella-to-self-managed).

## [](#april-2023-changelog)April 2023 Changelog

* Azure Private Link is now available as a network access management option.  
With private endpoints, you can use [Azure Private Link](https://azure.microsoft.com/en-us/services/private-link/) to connect an Azure VNET to Couchbase Capella. The benefits of this include:

  * Private endpoint traffic doesn’t traverse the Internet, allowing services to function as if you host them within your Azure VNET.
  * Private endpoints provide access to only a specific service or application, unlike [VNET peering](../clouds/private-network.md), which allows access to all resources.
  * Private endpoints support CIDR overlap.
  * Only private endpoints can initiate a connection.  
To start using Azure Private Link with Capella, see [Add an Azure Private Link Connection](../security/add-azure-private-link.md).
* Larger instance types are available.  
These additional compute and memory configurations are now available when deploying a cluster using AWS or GCP as your cloud provider:

| AWS                                                             | GCP                                                               |
| --------------------------------------------------------------- | ----------------------------------------------------------------- |
| 64 vCPUs 512 GB 96 vCPUs 192 GB 96 vCPUs 384 GB 96 vCPUs 768 GB | 96 vCPUs 384 GB (select regions) 96 vCPUs 768 GB (select regions) |  
To see a full list of the available instance types for AWS and GCP, see [Amazon Web Services (AWS) ](../reference/aws.md#compute-and-memory) and [Google Cloud Platform (GCP)](../reference/gcp.md#compute-and-memory).
* Storage Auto-Expansion is now available.  
Capella now provides a [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion) feature that automatically scales your storage capacity as your data grows over time. This scaling occurs seamlessly, without adding new nodes or rebalancing data, ensuring uninterrupted and smooth cluster operations.  
The system enables Storage Auto-Expansion by default when you create a new Service Group, provided you are an AWS or GCP user. Remember, you will only incur charges for the extra storage when the system triggers a capacity increase.
* Memory Only buckets are now available  
Use Memory Only buckets in Capella for use cases such as caching where you need low latencies. Please use caution with memory only buckets as the data resides in-memory only and data can be lost on cluster restart. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* Server audit logging is now available for GCP-hosted clusters  
Capella provides [event auditing](../security/auditing.md), where you can download server-logged events for inspection or archiving. This feature helps with investigations and meeting organizational security or compliance requirements. Server auditing is now available on Capella GCP-hosted clusters with the [Enterprise plan](../support/support.md#support-levels).  
> [!NOTE]  
> This feature is available on new clusters. Couchbase is upgrading existing clusters so all GCP enterprise customers can use this feature. If GCP auditing isn’t yet available for your cluster, open a support ticket so we can prioritize your cluster upgrade to get you using audit logging with your existing GCP clusters as soon as possible.

## [](#march-2023-changelog)March 2023 Changelog

## [](#february-2023-changelog)February 2023 Changelog

* Capella is now available on [Microsoft Azure Cloud in 11 regions worldwide](../reference/azure.md).  
Capella can now securely deploy Couchbase Server using a Couchbase-managed cloud powered by Azure. If you are using or plan to use our [self-service trial with Azure](https://cloud.couchbase.com/sign-up), you can upgrade to a sales-assisted or paying account at any time.

## [](#january-2023-changelog)January 2023 Changelog

* Capella is available on Azure for self-service trials in select regions.  
Couchbase Capella can now securely deploy clusters using a Couchbase-managed cloud powered by Microsoft Azure. Paid subscriptions and additional regions will be available in the near future.  
To try Capella with Azure today, see the [self-service trial](https://cloud.couchbase.com/sign-up).
* Bucket Backup Schedules  
We have included 4, 6, 8, 12, and 24 hour incremental options to the Set Weekly Schedule bucket backup setting. Any previous Set Weekly Schedule options have now been removed.  
The Set Daily Schedule bucket backup setting has been deprecated for new Capella users and clusters. However, Set Daily Schedule is still available if you are already using this setting on existing clusters.  
For more information, see [Configure Scheduled Backups](../clusters/manage-backup.md#configure-automatic-backups).
* Cost Optimized Retention Policy  
When you set a Weekly schedule, you can now choose a cost-optimized retention policy for bucket backups. You can do this by selecting a new Cost Optimized Retention checkbox option. When selected, the cost optimized retention policy applies to your bucket backups.  
For more information, see [Cost Optimized Retention Policy](../clusters/backup-restore.md#cost-optimized-retention-policy).

## [](#december-2022-changelog)December 2022 Changelog

* Single Sign-On (SSO) enhancements

  * Support for Ping and CyberArk.  
  The full list of supported identity providers is now:

    * Microsoft Azure AD
    * Okta
    * Ping
    * CyberArk  
  To configure Capella with any of these supported identity providers, see [Add SSO Authentication](../organizations/ui-auth/add-sso-auth.md).
  * Turn off SSO group mapping.  
  [Turning off SSO group mapping](../organizations/ui-auth/manage-identity-providers.md#group-mapping) lets you manage your SSO users like other Capella users through the People tab and each project’s Collaborators tab. You can change the group mapping setting during or after realm creation.

## [](#november-2022-changelog)November 2022 Changelog

* A new developer experience UI:  
Couchbase Capella has an updated UI. Highlights include:

  * Each page has a dynamic contextually relevant menu to reduce distraction.
  * The main page directly relates to your projects.
  * You can more easily navigate using the top navigation bar.
  * The popular Couchbase Playground is now integrated into Capella, enhancing the developer experience. The Playground includes:

    * SQL++ Playground.
    * SQL++ Tutorial.
    * SDK Tutorial for Node.js, Python, and Java.
* Couchbase Server 7.1.3  
Capella now supports Couchbase Server 7.1.3 — the most recent version of Couchbase Server. This version includes the following features:

  * Magma storage engine:  
  Magma is a High Data Density storage option for your buckets. This storage engine enables you to go down to as low as a 1% Resident Ratio. For more information about the Magma storage engine, see [Storage Engines](../clusters/data-service/storage-engines.md).
  * Improved auto-failover:

    * Support for automatic failover of index services.
    * High availability for the Analytics Service:  
      This service is now replicated by default with two replicas.
  * Unequal server groups:  
  Data nodes no longer require multiples of three.
  * Parquet Support:  
  Read Parquet files from AWS S3\. Apache Parquet is an open source data file format designed for efficient data storage and retrieval.
  * Couchbase Tableau Connector:  
  Native connectivity to Tableau using a native Couchbase-built and supported driver.
* Single Sign-On (SSO)  
Secure and convenient Single Sign-On authentication for users is now available.

  * Delegate authentication to your identity provider.
  * Supported identity providers include:

    * Microsoft Azure AD
    * Okta
  * Users can use existing corporate credentials.
  * Easy provisioning of new users, which removes the overhead of sending invitations.
  * Support for SSO Groups:  
  You can map SSO groups to Capella Teams—​a new way to organize users with SSO.  
For more information about SSO for Capella, see [Capella UI Authentication | Federated & SSO Authentication](../organizations/ui-auth/capella-ui-auth.md#federated-sso-authentication). To configure your identity provider with Capella, see [Add SSO Authentication](../organizations/ui-auth/add-sso-auth.md).
* AWS Private Endpoints  
AWS Private Endpoints allow a Capella cluster to be offered as a Private Endpoint. Private Endpoints have many benefits:

  * Private Endpoint traffic doesn’t traverse the Internet, allowing services to function as if they’re hosted directly within your Amazon VPC.
  * While VPC peering allows access to all resources, Private Endpoints only allow access to a specific service or application.
  * Private Endpoints support CIDR overlap.
  * Only Private Endpoints can initiate a connection.
  * Private Endpoints give on-premises networks private access to Capella Clusters through AWS Direct Connect, a safe and secure migration from on-prem.  
For more information about AWS Private Endpoints, see [Add an AWS PrivateLink Connection](../security/add-aws-private-link.md).

## [](#october-2022-changelog)October 2022 Changelog

* Cluster Level Audit Logging  
Audit logging at the cluster level is now possible within Couchbase Capella. Users can configure granular Couchbase Server audit logging down to the access of individual documents, then export these audit logs into their own systems on-demand. This complements the existing Capella-level audit logging that has always been in place, which can now also be exported via API.  
This functionality is available only to clusters with an Enterprise Support Plan.
* HIPAA  
Capella HIPAA-compliant controls, which have been audited by an independent third-party auditor, help organizations manage and store protected health information (PHI).  
See the [Cloud Trust Center](https://www.couchbase.com/products/capella/trust) for additional information on the security controls and compliance of the platform.

## [](#july-2022-changelog)July 2022 Changelog

## [](#june-2022-changelog)June 2022 Changelog

* Capella now available on Google Cloud Platform (GCP) in 31 regions worldwide.  
Capella can now securely deploy Couchbase Server using a Couchbase-managed cloud powered by GCP. If you are using or plan to use our [self-service trial](https://cloud.couchbase.com/sign-up) with GCP, you can upgrade to a sales-assisted or paying account at any time. For more information on the configuration and region options available to GCP clusters, see the [Google Cloud Platform (GCP)](../reference/gcp.md) reference page.
* Capella is now available in 15 AWS regions  
Couchbase Capella is now available in Sydney and Stockholm bringing Capella to a total of [15 AWS regions](../reference/aws.md#supported-regions). You can select these new options as your region when creating a new cluster.
* Maintenance notifications and scheduling  
Capella now automatically notifies you about upcoming upgrades and maintenance jobs on clusters you manage. For each cluster, a new Maintenance tab enables you to reschedule upcoming maintenance jobs, set your preferred maintenance times, and learn about what is new in Capella. For more information, see [Clusters Overview](../clusters/databases.md) and [Upgrading a Cluster](../clusters/upgrade-database.md).
* Cluster Cost Estimation Feature  
The "Create Cluster" screen now makes pricing more clear visually, allowing customers to see the dollar equivalent for on-demand — so making it easy for users to know how much their desired cluster will cost them.
* New Connection Code Examples  
Head to the Connect section of the Clusters screen to see SDK connection code for Kotlin, Ruby, and Scala. We have updated all of the other code samples to the latest SDK releases — which are now shipped with the Capella client certificate included, for fuss-free connection.
* SOC II Type 2  
We have completed a Service Organization Controls (SOC) 2 Type II compliance audit for Capella. This audit validates that we have been working according to our security and governance controls to effectively maintain the security, confidentiality, and availability of Capella .  
As a industry standard in data security, SOC 2 evaluates a technology service provider’s ability to securely manage customer data. To achieve a SOC 2 Type II designation, organizations undergo a rigorous audit by an independent third party that analyzes the following trust services criteria: security, availability, and confidentiality.

## [](#march-2022-changelog)March 2022 Changelog

* Capella AWS region expansion  
Couchbase Capella is now available in Singapore, bringing Capella to a total of [11 regions](../reference/aws.md#supported-regions). You can select "Singapore" as your region when creating a new cluster.
* Node-level cluster visibility  
The [**Nodes** tab](../get-started/run-first-queries.md#nodes) is now available on Capella clusters providing visibility into the state of each node in the cluster. This new tab allows you to easily obtain hostnames of specific nodes and to see the overall health of each node at a glance.
* Cluster data tools available during scaling and upgrades  
The Cluster screen is now accessible while a cluster is scaling after being reconfigured or upgraded. Cluster data tools such as the [Documents Editor](../clusters/data-service/manage-documents.md) and [Query Workbench](../clusters/query-service/query-workbench.md) can be used throughout, and other screens are available in a read-only mode.
* Expanded activity log  
Backup, restore, and flush events are now tracked within the [activity log](../clusters/monitoring/activity-log.md), providing increased visibility into key events that affect your clusters.
* Cluster credentials now provide access to metrics endpoint  
Cluster credentials that are generated with read access to _all_ buckets now allow users to access the metrics endpoint within their Couchbase Server cluster. For details on how you can use this to integrate your Capella clusters with Prometheus, see [Set up Prometheus to Consume Couchbase Metrics](../../server/current/manage/monitor/set-up-prometheus-for-monitoring.md).  
> [!NOTE]  
> This change only affects newly created or updated cluster credentials. You may need to recreate any existing credentials to provide them access to this functionality.
* Purchase information is now shown in Billing  
Capella customers can see information for each of their credit plan purchases providing awareness of consumption. This enables customers to take action before credit plan credits expire or are consumed and manage their spending more effectively.
* Projects can be renamed  
It is now possible to [change the name of a project](../projects/manage-projects.md#rename-a-project) after it has been created.
* Bucket flush requires confirmation  
Bucket flushes now require a confirmation step in the UI.
* Check for CIDR overlap  
Classless Inter-Domain Routing (CIDR) is specified during the creation of a cluster in Capella and cannot be changed afterward. To ensure that CIDR are unique and avoid overlaps, Capella now checks that CIDR is not already in use within a customer’s tenant.  
To use the [Private Networking feature](../clouds/private-network.md), where the virtual private cloud (VPC) of a cluster is joined with that of a customer’s application, or when clusters have [XDCR](../clusters/xdcr/xdcr.md) between each other, the CIDR of each VPC cannot overlap with each other. This requirement for CIDR originates from the cloud provider.

## [](#30-november-2021-release)30 November 2021 Release

* Couchbase Capella hosted DBaaS now available with extended configuration and options  
Capella now offers fully-featured configuration and options. This enables you to securely deploy Couchbase Server using an entirely Couchbase-managed cloud powered by AWS. If you are using or plan to use our [self-service trial](https://cloud.couchbase.com/sign-up), you can now upgrade to a sales-assisted or paying account at any time. Three plans are available providing different levels of features and support services to match your needs. For more information, see [Support Plans](../billing/billing.md#support-plans).
* More Couchbase Server 7.0 enhancements  
More Couchbase 7.0+ features have been added to Capella. The Analytics Workbench and Eventing Service now support scopes and collections. The Analytics Workbench can now create links to S3\. These features are only available if you are using the Developer Pro or Enterprise plans, and are using Couchbase 7.0+ clusters hosted by Couchbase.
* Couchbase Capella hosted clusters now support XDCR  
XDCR (Cross Data Center Replication) is now available for Couchbase hosted clusters. This update includes support for scopes and collections with collection mapping, quality of service (QoS) options, and a more streamlined setup process.  
XDCR for Couchbase hosted clusters supports the following:

| Source                              | Direction          | Target                 |
| ----------------------------------- | ------------------ | ---------------------- |
| Couchbase Hosted in Own Cloud (AWS) | Unidirectional (→) | Couchbase Hosted (AWS) |
| Couchbase Hosted (AWS)              | Bidirectional (←→) | Couchbase Hosted (AWS) |
| Self-managed Cluster                | Unidirectional (→) | Couchbase Hosted (AWS) |
* Improved backup and restore  
Capella’s Backup and Restore feature now provides more granular capabilities and a better user experience. Using an improved user interface, you can now trigger on-demand backups and restores by the bucket. Weekly and daily backup schedules can also be set by the bucket. Previous backups are now more easily accessible, show more detail, and are better manageable with manual deletion. Only users with the Project Owner role can access backups.
* Email alert notifications  
Email alerts can now be sent to you ensuring you don’t miss important events in your deployment. Emails include descriptions and visualizations of the event, and a link navigating you directly to the alert in the Capella Control Plane. Alerts are controlled at user account level.

## [](#25-november-2021-release)25 November 2021 Release

* Private networking support for clusters hosted with Capella  
Private networking is now supported for clusters hosted by Couchbase Capella. Private networks provide an added layer of security and better network performance for organizations by avoiding communication over the Internet. By setting up a private network, your application can interact with Capella over a private connection, resulting in a reduction in latency and data egress costs. For more information about private networking support in Capella, see [Configure a Private Network](../clouds/private-network.md) and try it using our free [self-service trial](https://cloud.couchbase.com/sign-up).
* Custom Dataset Import  
All managed clusters can now import your data in JSON and CSV file formats, from a local machine or URL, for files under 5 GB. When importing, you can easily specify a collection mapping for the import with previews. This feature is available to try in our free [self-service trial](https://cloud.couchbase.com/sign-up). If you already have a trial cluster deployed, you need to launch a new trial cluster to see this new functionality. For more information about importing your data, see [Import Data](../clusters/data-service/import-data-documents.md).
* Couchbase Server 7.0.2  
All new clusters hosted by Couchbase now use [Couchbase Server 7.0.2](#7.0@server:release-notes:relnotes.adoc#release-702).

## [](#19-october-2021-release)19 October 2021 Release

* Couchbase Cloud is now Couchbase Capella  
Going forward, Couchbase’s database-as-a-service (DBaaS) will be known as Couchbase Capella, previously Couchbase Cloud. Capella adds the ability to deploy our DBaaS in Couchbase’s Cloud Account, making it easier and faster to get started.
* Free self-service trial  
Capella now offers the ability to securely deploy Couchbase Server using an entirely Couchbase-managed cloud powered by AWS. This free self-service trial lets you sign up in seconds and deploy a cluster in under three minutes. The trial also includes 50GB of storage. [Sign up](https://cloud.couchbase.com/sign-up) and learn how to [get started](../get-started/create-account.md).
* Couchbase 7.0 enhancements  
This release brings many Couchbase 7.0+ features to Capella. With the introduction of [scopes and collections](../clusters/data-service/scopes-collections.md), Capella clusters using Couchbase Server 7.0+ store documents in a collection, which are contained in a scope, which is in a bucket. This provides multiple tiers of data hierarchy to make it easier to map a relational data model to Couchbase 7.0+. A default scope and default collection are used when a named scope and collection are not available or has not yet been created. In addition to scopes and collections, other updates include the ability to run queries as distributed multi-document ACID [transactions](../clusters/query-service/query-workbench.md#run-a-transaction), use the [ADVISE statement](../clusters/query-service/query-workbench.md#index-advisor), build indexes concurrently, and more. Note that these features are only available to clusters using Couchbase Server 7.0+, which only includes clusters created through our Couchbase-managed cloud offering.
* Improved monitoring and alerts  
The [Activity Log](../clusters/monitoring/activity-log.md) provides an audit trail of events that bring transparency to user activity and cluster performance. This has been enhanced to include a more complete timeline of activity that includes a summary of the activity, the resource affected, the actor, date and time, and actionable recommendations. Additionally, smart filtering has been added that allows you to narrow down activity events based on cloud, cluster, severity, and tag (activity event type).  
Alerts have also been enhanced. Active alerts are now shown as an alert banner at the top of all cluster screens for the affected cluster. These banner alerts include severity, count, and time information about the event. Alerts also include a detailed description of why the alert was triggered, recommended remediation guidance, and in some cases direct actions to resolve the issue.  
The new metrics dashboard is a customizable area that makes it easy to discover and trend cluster performance and identify outliers quickly using charts. It also provides zoom-in-on-runtime behavior through a full suite of time controls and drag-to-select thresholds.
* Faster and more improved user experience  
There have been many improvements to the overall experience of using Couchbase Capella. You will see changes to the user management experience to facilitate improved user management, UX improvements to various tools such as the documents editor, additions to monitoring and alerting capabilities, as well as many improvements to quickly and easily launch and manage deployments that use your own cloud and those that use the Couchbase-managed cloud.
* User management improvements  
The roles-based user management system in Capella has been updated to make it more intuitive and enable easy management of user permissions at the project level. Organizations and projects still exist, but their user roles have been made more granular and easy to understand. See [Organization Roles](../organizations/organization-user-roles.md) and [Project Roles](../projects/project-roles.md) for more information about the new user roles.  
Cluster users are now [_cluster credentials_](../clusters/manage-database-users.md). Cluster credentials are independent of users and allow access to cluster data. They can only be viewed, created, and managed by members of a project with the appropriate project role.  
To see information about how this change affects existing users, see the [Migration to New User Management](#reference:user-management-migration.adoc) reference page.

## [](#15-june-2021-release)15 June 2021 Release

* Couchbase Cloud API is now GA  
The Couchbase Cloud APIs enable you to automate many of the administrative operations using secure RESTful APIs. Couchbase Cloud APIs contain functionality to create and delete clusters, buckets, and cluster users, as well as list clouds, manage projects, and more. For more information on the Couchbase Cloud Public API, see [Overview of the Public API](../management-api-guide/management-api-intro.md).
* Migration and Import enhancements  
Enhanced import functionality enables you to migrate data to Couchbase Cloud more easily and in new ways. Using the new Import Tools interface, you can now import JSON (lines, list, and archive) and CSV files into Couchbase Cloud from a local machine using your browser or manually using a cURL command provided by the API. Keys for each document extracted from a CSV row or JSON list flat file can be auto-generated (UUID) or specified using a Generated Key Name Expression that follows the same syntax used by the cbimport utility.  
When creating an import, you also have the option to select from additional configuration options. These options include Skip Documents, Limit Documents, Ignore Fields, Infer Field Types (CSV only), and Omit Empty Fields (CSV only).  
For more information and how to use the enhanced import functionality, visit [Import Data](../clusters/data-service/import-data-documents.md).
* Streamlined sign-up experience  
Improvements made to the sign-up flow for Couchbase Cloud better guide you through the process and allow you to get signed up as quickly and easily as possible. To sign up for Couchbase Cloud, visit [Sign Up for Couchbase Cloud](https://cloud.couchbase.com/sign-up).
* Geo-expansion (AWS)  
Couchbase Cloud is now available in the AWS Middle East (Bahrain) Region. For a complete list of supported AWS regions, see [Amazon Web Services (AWS)](../reference/aws.md).

## [](#31-march-2021-release)31 March 2021 Release

* Support for public and private endpoints in AWS and Azure is now GA  
Private networks provide an added layer of security for organizations by avoiding communication over the Internet. By setting up a private network, your application can interact with Couchbase Cloud over a private connection, resulting in significant reduction in latency and egress cost. Refer to the documentation for more information on configuring a private network.
* Couchbase Cloud now available on Microsoft Azure Marketplace  
Couchbase Cloud can now be discovered, transacted, and deployed directly via the Azure Marketplace.
* Couchbase Cloud REST API in BETA  
The Couchbase Cloud REST APIs, currently in restricted BETA, enable you to automate many of the administrative operations using secure REST APIs. Specifically, this release of the Cloud APIs contains functionality that enables you to deploy and destroy clusters, buckets, and cluster users, and to list clouds and to manage projects.  
> [!NOTE]  
> The use of these APIs in production applications is not supported. Refer to the documentation for more information.
* Improved in-product Support UX  
We’ve integrated the support workflow with the core application so you can perform actions such as the following from the Couchbase Cloud Control Plane:

  * Close opened tickets
  * Filter tickets using filters like ‘all, open, or closed’
  * View assigned priority for tickets
  * Perform free-text searching across tickets
  * Upload multiple files for a ticket
  * Add a comment on ticket closure
* Performance and reliability enhancements for Full-text Search  
Full-text Search (FTS) indexes are now highly available with the ability to configure replicas via the Control Plane. And you can now configure partitions for better performance.
* IaaS-expansion (Storage capacity on Microsoft Azure)  
Expansion of disk storage on Azure to a maximum size of 16TB, increases aggregate max IOPs for higher performance and capacity.
* Geo-expansion (Microsoft Azure)  
Couchbase Cloud on Azure is now available in the West Central Region of Germany (Frankfurt).

## [](#07-january-2021-release)07 January 2021 Release

* Support for Microsoft Azure Cloud Provider  
This release expands the choice for Cloud providers by adding support for Microsoft Azure and will be available globally across North America, Europe, and Asia. For a complete list of supported regions, see [Microsoft Azure](../reference/azure.md).
* Introduces Multi-factor Authentication (MFA) for Couchbase Cloud  
With the introduction of Multi-factor Authentication (MFA) for Couchbase Cloud, users can choose to add another layer of security by requiring a one-time passcode to be used in conjunction with the password to log in to the Couchbase Cloud Control Plane.
* Improved Monitoring  
The Cluster **Overview** screen has been improved to provide more visibility into node and cluster health.
* Standardized AWS Instance Sizes  
This releases standardizes the list of available AWS compute instances to be consistent across instance families. The expanded instance selection now includes: m5.xlarge, m5.8xlarge, m5.16xlarge, r5.8xlarge, and c5.12xlarge.

## [](#30-november-2020-release)30 November 2020 Release

* Introduces the Couchbase [Analytics Service](../clusters/analytics-service/analytics-service.md)  
The _Analytics Service_ provides a parallel data-management capability that enables you to run complex analytical queries. It supports large _join_, _set_, _aggregation_, and _grouping_ operations, any of which may result in long running queries, high CPU usage, high memory consumption, and/or excessive network latency due to data fetching and cross node coordination.

  * The Analytics service can be added to new and existing clusters.

    * Like the other Couchbase services, the Analytics Service can be deployed during [cluster creation](../clusters/create-database.md), or by [adding it to an existing cluster](../clusters/scale-database.md). Note that the Analytics Service depends on the [_Data Service_](../clusters/data-service/data-service.md). This service must also be deployed on the cluster in order to use the Analytics Service.
  * For a cluster with Analytics Service deployed, SQL++ for Analytics queries can be issued using the Couchbase SDK and the interactive [Analytics Workbench](../clusters/analytics-service/analytics-workbench.md) Analytics.
* Introduces the Couchbase Eventing Service  
The _Eventing Service_ provides a framework to operate on changes to data in real time and streamline your business workflows.  
Events are changes to data in the Couchbase cluster. Couchbase Eventing Functions, also referred to as Functions or Handlers, offer a computing paradigm that developers can use to handle data changes. In the Couchbase cluster, you can use the Functions to process and respond to data-changes according to an Event-Condition-Action model.
* Introduces a 30-day free trial of Couchbase Cloud  
By signing up for a 30-day free trial of Couchbase Cloud, you can deploy the _Quick Start 30-day Trial_ template that is ideal to evaluate all Couchbase services.
* Adds support for AWS [Asia Pacific](../reference/aws.md) regions.

## [](#30-september-2020-release)30 September 2020 Release

The September release of Couchbase Cloud adds more features to the Search Service, and brings improvements to user management, charting, and metrics.

* Updates the Search Service

  * The following Full Text Index settings can now be configured via the Couchbase Cloud UI:

    * [Type Identifiers](../search/create-search-indexes.md#specifying-type-identifiers)
    * [Analyzer Defaults](../search/create-search-indexes.md#specifying-analyzer-defaults)
    * [Analyzers](../search/create-search-indexes.md#creating-analyzers)
    * [Custom Filters](../search/create-search-indexes.md#adding-custom-filters)
    * [Date/Time Parsers](../search/create-search-indexes.md#date-time-parsers)
  * When making configuration changes to a Full Text Index, the changes are now stored in browser memory until definitively submitted using the new **Save Index** button on the index’s [configuration page](../search/create-search-indexes.md#modify-full-text-index). This ensures that the index is only rebuilt once all desired configuration changes have been made.
  * When [searching](../search/create-search-indexes.md#query-full-text-index) a Full Text Index via the Couchbase Cloud UI, search results are now enhanced with highlighting, scoring, pagination, timeouts, consistency levels, consistency vectors, viewing docs from the result set, and time taken for execution.
  * The cluster’s **Tools > Full Text Search** tab in the Couchbase Cloud UI [now displays](../search/create-search-indexes.md#index-summary) document counts and indexing progress for Full Text Indexes.
  * Statistics can be [viewed](../search/create-search-indexes.md#view-full-text-index-statistics) for individual Full Text Indexes via the Couchbase Cloud UI.
  * Relevant documentation links have been added to various areas of the cluster’s **Tools > Full Text Search** tab in the Couchbase Cloud UI.
* Introduces proactive alerts within the Couchbase Cloud UI  
When an issue is automatically detected within a Couchbase Cloud-managed cluster, the Couchbase Cloud UI displays the details of the issue and enables you to be better informed about the overall health of the cluster and provides an option to contact Support with the details of the issue.
* User management

  * Improvements to user management to resolve bugs and improve the user experience when adding one or more users to Couchbase Cloud or your clusters and buckets.
  * Improved permission workflow in Couchbase Cloud, which enables users to directly edit their accounts to take corrective action.
  * Support to include NIST Guidelines for user session timeouts.
* Monitoring and Metrics Charts

  * Syncing the mouse-over behavior across charts.
  * Performance improvements for charts.
* Other improvements

  * When configuring allowed IP addresses for a cluster, you can now specify IP address ranges.
  * Improved error message to guide user action when attempting to delete a cloud that contains one or more clusters.
  * UI performance has been improved by reducing network activity to backend APIs through the implementation of improved polling techniques.

## [](#31-august-2020-release)31 August 2020 Release

* Introduces the Couchbase [Search Service](../search/search.md).  
The _Search Service_ — also referred to as _Full Text Search_ (or FTS) — provides extensive capabilities for natural-language querying. Deploying the Search Service on a cluster allows you to create, manage, and query specially purposed indexes that enable Google-like search capabilities on JSON documents within a bucket.

  * The Search Service can be added to new and existing clusters.

    * For _new clusters_, the Search Service can be deployed using the Quick Start and Full Text Search templates, or via custom sizing. Refer to [Create A Paid Cluster](../clusters/create-database.md).
    * For _existing clusters_, refer to [Add a New Service to a Cluster](../clusters/modify-database.md#add-service).
  * Full Text Indexes can be created, managed, and queried from the [Couchbase Cloud UI](../search/create-search-indexes.md).  
  The following Search Service features are available in the UI:

    * Create and manage Full Text Indexes
    * Configure advanced index options
    * Add and manage type mappings
    * Import/export Full Text Index definitions
    * Query Full Text Indexes and view returned documents  
  The following advanced Search Service features are _not_ currently available in the UI:

    * Adding analyzers, custom filters, and data/time parsers; rearranging type mapping configurations; editing advanced index options; viewing service-specific FTS metrics

* Introduces billing integration with AWS Marketplace.

  * Couchbase Cloud can now optionally be purchased through [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B08DRXPXWT).
  * When purchasing through AWS Marketplace, invoices and payments for the Couchbase Cloud service are handled directly by AWS, allowing for consolidated billing alongside your infrastructure.  
For more information about purchasing Couchbase Cloud through the AWS Marketplace, please contact Couchbase Sales. You can also refer to the [Couchbase Cloud Credits](../billing/billing.md#couchbase-cloud-credits) documentation for additional information regarding supported payment methods.