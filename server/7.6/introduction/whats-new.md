---
title: What&#8217;s New in Version 7.6
description: Couchbase is the modern database for enterprise applications.
  Couchbase Server 7.6 combines the strengths of relational databases with the
  flexibility, performance, and scale of Couchbase.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/introduction/pages/whats-new.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:7.6@server:introduction:whats-new.adoc[]
---

[View original HTML](/server/7.6/introduction/whats-new.html)

# What&#8217;s New in Version 7.6

> Couchbase is the modern database for enterprise applications. Couchbase Server 7.6 combines the strengths of relational databases with the flexibility, performance, and scale of Couchbase. 

For information about platform support changes, deprecation notifications, notable improvements, and fixed and known issues, refer to the [Release Notes](../release-notes/relnotes.md).

> [!IMPORTANT]
> deprecation notice
> 
> Using older x86 processors that do not have the AVX2 instruction set is deprecated in Couchbase Server 7.6.x. Deprecated processors include pre-2013 Intel Core processors, pre-2020 Celeron or Pentium processors, and pre-2015 AMD processors. See [System Resource Requirements](../install/pre-install.md) for details.

> [!IMPORTANT]
> note regarding `cbbackupmgr`
> 
> If you are performing a backup/restore operation on a Couchbase Server 7.6.x cluster, ensure that you use `cbbackupmgr` version 7.6.

## [](#new-features-7610)New Features and Enhancements in 7.6.10

The following new features are provided in this release.

### [](#new-features-7610-query)Query Service

* **[MB-69387](https://jira.issues.couchbase.com/browse/MB-69387):**Couchbase Server 7.6.10 now includes an auto-reprepare feature for PREPARE statements. When enabled, a prepared statement automatically updates its query plan whenever GSI metadata version changes, ensuring it always uses newer, more efficient indexes as they become available. For more information, see [PREPARE](../n1ql/n1ql-language-reference/prepare.md).

## [](#new-features-766)New Features and Enhancements in 7.6.6

The following new features are provided in this release.

* The following new platforms are supported.

  * Windows Server 2025

### [](#new-features-766-xdcr)XDCR

* **[MB-57921](https://jira.issues.couchbase.com/browse/MB-57921):**Created provision to set up XDCR bidirectional replication with Sync Gateway (SGW) 4.0 or a later version. In the versions earlier than Server 7.6.6 and Sync Gateway (SGW) 4.0.0, only an active-passive setup was supported with both XDCR and SGW. XDCR active-active replication with Sync Gateway for XDCR-Mobile interoperability configuration is introduced in the Server 7.6.6 version, where you can configure an active-active XDCR setup with Sync Gateway and mobile applications both on the XDCR source and target clusters. You need to have at least a Server 7.6.6 version and SGW 4.0.0 version to use this setup. For more info, see [XDCR Active-Active with Sync Gateway](../learn/clusters-and-availability/xdcr-active-active-sgw.md).

## [](#new-features-764)New Features and Enhancements in 7.6.4

The following new features are provided in this release.

### [](#new-features-764-cluster-manager)Cluster Manager

* **[MB-63871](https://jira.issues.couchbase.com/browse/MB-63871):**The `/prometheus_sd_config` endpoint provides a new option `clusterLabels`that specifies the cluster will return its name and UUID. Prometheus will use the labels in time series data. This provides a method to guarantee uniqueness for stats with the same name gathered from multiple clusters.  
```console  
curl --get -u <username:password> \  
    http://<ip-address-or-domain-name>:<port-number>/prometheus_sd_config
    -d disposition=[attachment|inline]
    -d network=[default|external]
    -d port=[insecure|secure]
    -d type=[json|yaml]
    -d clusterLabels=none|uuidOnly|uuidAndName  
```

### [](#new-features-764-xdcr)XDCR

* **[MB-62412](https://jira.issues.couchbase.com/browse/MB-62412):**Once faulty remote cluster credentials are fixed, XDCR will now be able to more quickly restart replications that depend on the repaired references.

### [](#new-features-764-search-service)Search Service

* The Search Service now supports pre-filtering on Vector Search queries. Use pre-filtering to execute a vector search over a subset of your Vector Search index, through a defined filter request.  
For more information, see [Pre-filtering Vector Searches](../vector-search/pre-filtering-vector-search.md)
* The Search Service now supports the cosine similarity metric for [Vector Search indexes](../vector-search/vector-search.md). For more information about Vector Search similarity metrics, see [Child Field Options](../search/child-field-options-reference.md).
* The Search Service now supports a new option for optimizing Vector Search indexes: **memory-efficient**. Choose this option to prioritize reduced memory and resource usage for Vector Searches, at the cost of accuracy and latency. For more information, see [Child Field Options](../search/child-field-options-reference.md).
* The Search Service has added a new object to JSON Search queries. Use this new object to view detailed query debugging information and resolve query errors in the Web Console or through the REST API. For more information about how to run a query with this new object, see [the validate property](../search/search-request-params.md#validate), [Run a Simple Search with the REST API and curl/HTTP](../search/simple-search-rest-api.md#example-validate-a-search-query) or [Run A Simple Search with the Web Console](../search/simple-search-ui.md#example-validate-a-search-query).

### [](#new-features-764-eventing-service)Eventing Service

* The Eventing Service now supports Sync Gateway. The Eventing REST API provides settings which enable individual Eventing functions to work with Sync Gateway. For more information, see [Update Function Settings](../eventing-rest-api/index.md#adv%5Fsettings%5Fupdate).

### [](#supported-platforms)Supported Platforms

* Support for Windows 10 is deprecated in Couchbase Server 7.6.4\. A future release of Couchbase Server will remove support for it.

### [](#new-features-764-tools)Tools

* **[MB-63171](https://jira.issues.couchbase.com/browse/MB-63171):**Starting from version 7.6.4, the Couchbase Server tools packages are categorized into the Server developer tools package and the Server admin tools package.  
The Server developer tools package is the same as the previously named Server tools package, which includes `cbimport`, `cbexport`, `cbq`, and `cbbackupmgr`.  
The Server admin tools package is created for the Server admin users who want to download the necessary utilities to remotely administer and monitor multiple Couchbase clusters. The Server admin tools package includes the utilities `cbbackupmgr`, `cbc`, `cbdatarecovery`, `cbexport`, `cbimport`, `cbq`, `cbstats`, `couchbase-cli`, `mcstat`, `mctestauth`, and `mctimings`.  
For details, see [CLI Reference](../cli/cli-intro.md#server-tools-packages).

## [](#new-features-762)New Features and Enhancements in 7.6.2

The following new features are provided in this release.

### [](#platform-support)Platform Support

* Couchbase Server 7.6.2 adds support for the following platforms:

  * Ubuntu 24.04  
See [Supported Platforms](../install/install-platforms.md) for a full list of supported platforms.

### [](#backup%5F762)Backup

* Users with the [Read-Only Admin](../learn/security/roles.md#read-only-admin) role can now read backup information from the following Backup Service REST API endpoints:

  * [/api/v1/cluster/self](../rest-api/backup-get-cluster-info.md)
  * [/api/v1/config](../rest-api/backup-manage-config.md)
  * [/api/v1/cluster/self/repository/{repo-state}](../rest-api/backup-get-repository-info.md)
  * [/api/v1/cluster/self/repository/{repo-state}/{task-name}/taskHistory](../rest-api/backup-get-task-info.md)
  * [/api/v1/plan/](../rest-api/backup-get-plan-info.md)
* You can now set the number of threads each Backup Service node uses when backing up data. For example, if you find backups cause performance issues on your cluster, you can reduce the number of threads the Backup Service uses. Reducing the number of threads also reduces the number of concurrent client connections the Backup Service makes to retrieve data. See [Thread Usage](../learn/services-and-indexes/services/backup-service.md#threads) for more information.

### [](#analytics-service)Analytics Service

* The Analytics Service REST API has two new endpoints that let you get information about active and completed requests. See [Active Requests](../analytics-rest-admin/index.md#return%5Factive%5Frequests) and [Completed Requests](../analytics-rest-admin/index.md#completed%5Frequests) in the [Analytics Administration REST APIs](../analytics-rest-admin/index.md) page.

### [](#cluster-manager)Cluster Manager

* Version 7.6.2 adds Cluster Manager metrics to help you monitor failovers and rebalances:

  * `cm_auto_failover_count`: the number of auto-failovers that occurred.
  * `cm_auto_failover_enabled`: whether auto-failover is enabled.
  * `cm_auto_failover_max_count`: the maximum number of auto-failovers allowed before Cluster Manager disables auto-failover.
  * `cm_failover_total`: The total number of non-graceful failovers that have occurred.
  * `cm_graceful_failover_total`: The total number of graceful failovers that have occurred.
  * `cm_is_balanced`: Whether the Cluster Manager is balanced. Only reported by orchestrator nodes and only reported every 30 seconds.
  * `cm_rebalance_in_progress`: Whether there is a rebalance occurring. Only reported by the orchestrator node.
  * `cm_rebalance_progress`: An estimate of the progress of the current rebalance. Only reported by the orchestrator.
  * `cm_rebalance_total`: The total number of rebalances that have occurred.  
For more information, see [Cluster Manager Metrics](../metrics-reference/ns-server-metrics.md).

### [](#query%5F762)Query Service

* In Couchbase Server version 7.6.2 and later, language constructs that may allow for code injection, speculative execution attacks, or side channel attacks have been removed from JavaScript user-defined functions in the Query service. For details, see [JavaScript Functions for Query](../javascript-udfs/javascript-functions-with-couchbase.md#restricted-features).

### [](#index%5F762)Index Service

* From version 7.6.2, you can specify that index creation operates in deferred build mode by default. In deferred build mode, creating an index does not trigger the index build phase: you must trigger the index build before you can use the index. For details, see [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).
* In Couchbase Server Versions 7.6.0 and 7.6.1, enabling file-based index rebalance prevented you from controlling which Index Service nodes contain an index. Version 7.6.2 removes this restriction. You can now use the `WITH <node>` clause of the `CREATE INDEX` SQL++ statement when your cluster has file-based index rebalancing enabled. See [learn:clusters-and-availability/rebalance-and-index-service.adoc#index-rebalance-methods](../learn/clusters-and-availability/rebalance-and-index-service.md#index-rebalance-methods) for more information.  
> [!NOTE]  
> You still cannot use the `WITH <node>` clause with the `ALTER INDEX` statement when your cluster has file-based index rebalancing enabled.

### [](#search%5F762)Search Service

* Version 7.6.2 adds multiple improvements to the Search Service, including [Vector Search](../vector-search/vector-search.md):

  * [Vector Search](../vector-search/vector-search.md) now automatically adds a [match\_none](../search/search-request-params.md#match%5Fnone) query object to your Vector Search queries. This means you can run a pure Vector Search without adding a `query` object to your JSON Search request.
  * The total dimension support for [Vector Search](../vector-search/vector-search.md) has been increased from 2048 to 4096 array elements.
  * [Vector Search](../vector-search/vector-search.md) now supports vectors encoded as efficiently compressed base64 strings.  
  Add a base64-encoded vector to your Search index with the new `vector_base64` field data type, then use the `vector_base64` object in your Search request.
  * Use the Couchbase Server Web Console to edit and generate a full curl command for a Search request, with a new built-in code editor. Use the curl command to run a Search query with the Search REST API.
  * The Search Service can now index and search for metadata stored in Extended Attributes (XATTRs) fields inside your documents.  
  Use the new [XATTRs mapping type](../search/create-xattrs-mapping.md) in a Search index, then add the prefix `_$xattrs.` to a [field object](../search/search-request-params.md#field) in your Search request. You can also use the [Search Functions](../n1ql/n1ql-language-reference/searchfun.md) from SQL++ to search for XATTRs data.  
  > [!TIP]  
  > You must use the [META function](../n1ql/n1ql-language-reference/metafun.md) to select the XATTRs field you want to search for an uncovered query, or any SQL++ query without a suitable Search index. Use the [SEARCH\_META function](../n1ql/n1ql-language-reference/searchfun.md#search%5Fmeta) to select XATTRs fields when you do have a suitable Search index.
  * [Vector Search](../vector-search/vector-search.md) is now supported on MacOS.
  * [Vector Search](../vector-search/vector-search.md) is up to 7 times more performant, due to improvements in using node resources.

### [](#eventing%5F762)Eventing Service

* Version 7.6.2 adds the following improvements to the Eventing Service:

  * The new [base64 Encode and Decode functions](../eventing/eventing-language-constructs.md#base64%5Fcall) let you pack large arrays of floats as efficiently compressed strings when you use Eventing to generate vector embeddings.
  * The new [Sub-Document LOOKUPIN](../eventing/eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-lookupin) and [Sub-Document MUTATEIN](../eventing/eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-mutatein) operations let you search for or modify a specific field in a document without having to search and retrieve the entire document.
  * You can now fetch and modify a document’s Extended User Attributes (XATTRs) through the [Sub-Document LOOKUPIN](../eventing/eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-lookupin) and [Sub-Document MUTATEIN](../eventing/eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-mutatein) operations.

### [](#sdks%5F762)SDKs

* Alongside Version 7.6.2, Couchbase announces the 1.0.0 GA release of the [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md). This SDK has been long used as the core of our [Node.js](../../../nodejs-sdk/current/hello-world/overview.md), [PHP](../../../php-sdk/current/hello-world/overview.md), [Python](../../../python-sdk/current/hello-world/overview.md), and [Ruby](../../../ruby-sdk/current/hello-world/overview.md) SDKs, to handle communicating with the cluster over Couchbase’s binary protocols. and is now released as a full, standalone SDK for applications needing the speed of C++.
* Version 7.6.2 adds the ability to use multi-document ACID transactions with binary documents, alongside the current handling of JSON documents. This feature is initially implemented in the C++ and Java SDKs.

### [](#tools%5F762)Tools

* From version 7.6.2, the Couchbase Server tools package includes the `cbq` shell, alongside the previously-provided tools such as `cbimport`, `cbexport`, and `cbbackupmgr`. For details, see [CLI Reference](../cli/cli-intro.md#server-tools-packages).

## [](#new-features)New Features and Enhancements in 7.6.0

The following new features are provided in this release.

### [](#platform-support-2)Platform Support

* Couchbase Server 7.6 adds support for the following platforms:

  * Alma Linux 9
  * Debian Linux 12 (Bookworm)
  * Rocky Linux 9
  * macOS 13 "Ventura"
  * macOS 14 "Sonoma"  
See [Supported Platforms](../install/install-platforms.md) for a full list of supported platforms.
* In response to [CVE-2023-5363](https://nvd.nist.gov/vuln/detail/CVE-2023-5363) and [CVE-2023-5678](https://nvd.nist.gov/vuln/detail/CVE-2023-5678), OpenSSL upgraded to version 3.1.4.  
> [!NOTE]  
> This update changes the available ciphers for TLS connections. If you have not updated your client applications to use recent TLS libraries, you may experience an inability to connect and TLS handshake failures. Before upgrading, we recommend testing compatibility in a separate environment – especially if you are unsure that your platform TLS (OpenSSL, Java Secure Socket Extensions, .NET Security Provider, etc.) has compatible ciphers.

### [](#cluster-manager-2)Cluster Manager

* A required minimum can be established for the number of replicas configured for a bucket. See [Setting a Replica-Minimum](../rest-api/setting-minimum-replicas.md).
* In each user-created or sample bucket, a `_system` scope is created and maintained by default. This scope contains collections used by Couchbase services, for service-specific data. See [\_system Scope and its Collections](../learn/data/scopes-and-collections.md#system-scope-and-its-collections).
* A _rank_ can be assigned to each bucket on the cluster, whereby each bucket’s handling by the _rebalance_ process is appropriately prioritized. Assignment can be made by means of either the CLI or the REST API. This feature allows the cluster’s most mission-critical data to be rebalanced most quickly. See [Creating and Editing Buckets](../rest-api/rest-bucket-create.md).
* You can now have Couchbase Server prune rotated audit logs after a period of time. You set how long Couchbase Server should keep audit logs by using the new `pruneAge` parameter for the `/settings/audit` endpoint. The default value of 0 means that Couchbase Server does not prune audit logs. See [Configure Auditing](../rest-api/rest-auditing.md).
* You can add one or more arbiter nodes to a cluster. An arbiter node helps your cluster in two ways:

  * It provides [fast failover](../learn/clusters-and-availability/nodes.md#fast-failover) which helps decrease the cluster’s latency when reacting to a failover.
  * It provides [quorum arbitration](../install/deployment-considerations-lt-3nodes.md#quorum-arbitration) that helps avoid contention issues if the nodes in the cluster become partitioned.
* The `sampleBuckets/install` REST API method now returns a JSON object containing the list of tasks Couchbase Server started to load the buckets. In addition, the `/pools/default/tasks` REST API endpoint now takes an optional `taskId` parameter to view details about a sample bucket loading task. See [Install Sample Buckets with the REST API](../manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-rest-api) for more information.
* The minimum permitted duration for auto-failover on the nodes is reduced from 5 seconds to 1 second when set through the REST API.

### [](#backup-and-restore)Backup and Restore

* The Role-Based Access Control (RBAC) REST API has a new `backup` endpoint that lets you backup and restore user and user groups. See [Backup and Restore Users and Groups](../rest-api/rbac.md#backup-and-restore-users-and-groups).
* The `cbbackupmgr` command has a new `--enable-users` flag that backs up user groups and users including roles and permissions. When you supply the new argument, `cbbackupmgr` saves user passwords in the backup in a hashed format. When restoring a backup, `cbbackupmgr` defaults to not overwriting existing users in the database with identically named users in the backup. You can change this default behavior using the new `--overwrite-users` command-line argument. See [cbbackupmgr config](../backup-restore/cbbackupmgr-config.md) and [cbbackupmgr restore](../backup-restore/cbbackupmgr-restore.md) for more about user backup.
* The `cbbackupmgr` encrypted backups feature is now GA for both cbbackupmgr CLI and the Backup Service. See [Backup Encryption](../backup-restore/cbbackupmgr-encryption.md).

### [](#cross-data-center-replication-xdcr)Cross Data Center Replication (XDCR)

* Node-connectivity can be checked, prior to the creation of an XDCR reference. See [Checking Connections](../rest-api/rest-xdcr-connection-precheck.md).
* Binary documents can optionally be included in, or excluded from XDCR replications. See [Filtering Binary Documents](../learn/clusters-and-availability/xdcr-overview.md#xdcr-filter-binary).

### [](#performance)Performance

* You can now migrate buckets from one storage backend to another. This feature supports migrating buckets from Couchstore to Magma and from Magma to Couchstore. You can migrate buckets while the database continues running. To complete the migration you must trigger a swap rebalance or a graceful failover followed by a full recovery on each node that contains the bucket. See [Migrate a Bucket’s Storage Backend](../manage/manage-buckets/migrate-bucket.md).

### [](#security-and-authentication)Security and Authentication

* Security settings now provide additional parameters, for the configuration of Couchbase-Server user-password hashing. See [Configure On-the-Wire Security](../rest-api/rest-setting-security.md).
* Credentials for Couchbase-Server internal users can now be rotated at any time, by means of the REST API. See [Rotate Internal Credentials](../rest-api/rest-rotate-internal-credentials.md).
* LDAP authentication now supports using regular expressions to map users to LDAP users and groups. You can supply multiple regular expressions that Couchbase attempts to match against the user name supplied during an authentication attempt. This feature gives you greater flexibility when authenticating users. For example, you can use a regular expression to map the domain name in an email address to an LDAP organization. See [Advanced Query](../manage/manage-security/configure-ldap.md#ldap-advanced-mapping) under [User Authentication Enablement](../manage/manage-security/configure-ldap.md#enable-ldap-user-authentication).
* The Couchbase Server Web Console now supports using Structured Authentication Markup Language (SAML) for authentication. When you enable SAML authentication, a **Sign In Using SSO** button appears on the Web Console login screen. This button lets users who have already authenticated with the SAML identity provider (Okta, for example) to skip having to enter credentials. See [SAML Authentication](../learn/security/authentication-domains.md#saml-authentication) for more information.
* Couchbase Server’s LDAP support now has a setting that turns on and off TLS middlebox compatibility. This setting controls low-level network communication options when Couchbase Server securely connects to an LDAP server through intermediate systems such as proxies and firewalls. See [Advanced Settings](../manage/manage-security/configure-ldap.md#advanced-settings) on the [Configure LDAP](../manage/manage-security/configure-ldap.md) page for more information about this setting.
* Couchbase Server now supports using Public-Key Cryptography Standard (PKCS) #12 format certificates for node certificates. This format lets you bundle the node’s private key, public key, and certificate chain into a single file. See [PKCS #12 Certificates for Nodes](../learn/security/certificates.md#pkcs12) for more information.
* Couchbase Server now supports the X.509 Elliptic Curve Key cipher suites. Elliptic Curve Key ciphers are less resource-intensive than other cipher suites. They’re useful when communicating with resource-constrained devices such as IoT hardware. See [Private Keys](../learn/security/certificates.md#private-key-formats) for more information.
* Couchbase Server no longer supports TLS versions 1.0 and 1.1\. When upgrading to version 7.6 or later, the upgrade process automatically sets `minTLSVersion` to `tlsv1.2` if it’s set to `tlsv1` or `tlsv1.1`. Before you upgrade, be sure all the clients you use support TLS 1.2 or greater. See [On-the-Wire Security](../learn/security/on-the-wire-security.md) for more information.
* To prevent [LUCKY13 attacks](https://en.wikipedia.org/wiki/Lucky%5FThirteen%5Fattack), Couchbase Server 7.6 removes the following ciphers from the default cipher list:

  * TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA
  * TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA
  * TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA
  * TLS\_RSA\_WITH\_AES\_128\_CBC\_SHAa
* You can now enable alerts for certificate expiration. When enabled, Couchbase Server alerts you when server, node, or XDCR certificates are within 30 days of expiration. You can change the alert period via the new `certExpirationDays` alert limit setting. Couchbase Server sends a second alert when certificates expire. See [Certificate Expiration](../learn/security/certificates.md#certificate-expiration) for more information.
* Couchbase Server now defaults to using the ([Argon2id](https://en.wikipedia.org/wiki/Argon2%29) algorithm to hash passwords for new users. This hashing algorithm is more secure than the SHA1 algorithm used to hash passwords in earlier server versions.
* If you upgrade a database to Couchbase Server 7.6 or later, it continues to use the older SHA1 hashing algorithm for existing user passwords. You can enable a new setting that has Couchbase Server migrate user passwords from SHA1 to Argon2id when a user authenticates. This setting works only if the entire cluster is running Couchbase Server version 7.6 or later. For more information, see [Automatic Password Hash Migration](../learn/security/authentication-overview.md#password-hash-migration).

### [](#metrics)Metrics

* Couchbase Server has a new service discovery endpoint to help you configure the Prometheus event monitoring system. The old endpoint, named `/prometheus_sd_config.yaml` is now deprecated. The new endpoint is able to produce the same output as the old endpoint and has additional features. See [Configure Prometheus to Collect Couchbase Metrics](../manage/monitor/set-up-prometheus-for-monitoring.md).
* Disk usage statistics now include transient files in progress, state files, and configuration files.

### [](#index-service)Index Service

* You can choose to have the rebalance process move an index’s files between nodes instead of rebuilding them from scratch. This setting improves rebalance performance as moving the files is faster than rebuilding them. See [learn:clusters-and-availability/rebalance-and-index-service.adoc#index-rebalance-methods](../learn/clusters-and-availability/rebalance-and-index-service.md#index-rebalance-methods).

### [](#search-service)Search Service

* Couchbase Server 7.6 introduces Vector Search to enable AI integration, semantic search, and the RAG framework. A developer-friendly vector indexing engine exposes a vector database and search functionality. With Couchbase Vector Search, you can enable fast and highly accurate semantic search, ground LLM responses in relevant data to reduce hallucinations, and enhance or enable use cases like personalized searches in e-commerce and media & entertainment, product recommendations, fraud detection, and reverse image search. You can also enable full access to an AI ecosystem with a LangChain integration, the most popular open-source framework for LLM-driven applications.  
A Vector Search database includes:

  * Standard Couchbase vertical/horizontal scaling
  * Indexing capable of efficient Insert/Update/Removal of Items (or documents)
  * Storage of raw Embedding Vectors in the Data Service in the documents themselves
  * Querying Vector Indexes (REST and UI via a JSON object/fragment, Couchbase SDKs, and SQL++)
  * SQL++/N1QL integration
  * Third-party framework integration: LangChain (later LlamaIndex + others)
  * Full support for Replicas Partitions and file-based Rebalance  
> [!NOTE]  
> Vector Search is currently only supported on Couchbase Server 7.6.0 deployments running on Linux platforms. macOS and Windows platforms are not supported.  
For more information about vector search, see [Use Vector Search for AI Applications](../vector-search/vector-search.md)
* Couchbase Server 7.6 introduces Scoped Index Naming as an optional part of the `WHERE` clause in an SQL++ statement. For more information, see [SEARCH function arguments](../n1ql/n1ql-language-reference/searchfun.md#search-function-arguments-section)

### [](#data-service)Data Service

* Introduces KV Range Scan, used to retrieve all documents in a specified range directly from the Data service. Note that in this initial version, you will achieve better performance using a direct fetch or retrieval from a Query with an Index. See the [SDK docs](../../../java-sdk/current/howtos/kv-operations.md#kv-range-scan) for more information.
* Two changes in Couchbase Server 7.6 affect the `maxTTL` setting for collections:

  * In earlier versions, you could only set a collection’s `maxTTL` setting when creating the collection. You can now change the `maxTTL` setting on a collection after creation.
  * You can now set a collection’s `maxTTL` to -1 to prevent a bucket’s non-zero `maxTTL` setting from causing documents in the collection to expire automatically. This new setting is useful if you want most of the documents in a bucket to automatically expire, but want to prevent the documents in one or more collections from expiring by default.  
See [Expiration](../learn/data/expiration.md) for more information.

### [](#query-service)Query Service

* SQL++ language additions:

  * OFFSET clause added to the DELETE statement. See [DELETE](../n1ql/n1ql-language-reference/delete.md).
  * GROUP AS clause added to the GROUP BY clause. See [GROUP BY Clause](../n1ql/n1ql-language-reference/groupby.md).
  * FORMALIZE() function. See [FORMALIZE()](../n1ql/n1ql-language-reference/metafun.md#formalize).
  * Multi-byte aware string functions. See [String Functions](../n1ql/n1ql-language-reference/stringfun.md).
  * Support for sequences. See [Sequence Operators](../n1ql/n1ql-language-reference/sequenceops.md).
  * EXPLAIN FUNCTION statement. See [EXPLAIN FUNCTION](../n1ql/n1ql-language-reference/explainfunction.md).
* cbq shell additions. See [cbq](../n1ql/n1ql-intro/cbq.md):

  * The `-query_context` command line option.
  * The `-advise` command line option.
* The WITH clause adds support for recursive CTEs. See [WITH RECURSIVE Clause](../n1ql/n1ql-language-reference/with-recursive.md).
* The CREATE COLLECTION statement adds support for maxTTL. See [CREATE COLLECTION](../n1ql/n1ql-language-reference/createcollection.md).
* The `/clusterInit` endpoint in the Nodes and Clusters REST API adds support for Query memory quotas. See [Initializing a Cluster](../rest-api/rest-initialize-cluster.md).
* Named and positional parameters can now be prefixed by `$` or `@` in a query. See [Named Parameters and Positional Parameters](../n1ql/n1ql-manage/query-settings.md#section%5Fsrh%5Ftlm%5Fn1b).
* The `system:indexes` catalog now enables you to find the number of replicas configured for each index. See [Query Indexes](../n1ql/n1ql-intro/sysinfo.md#querying-indexes).
* The Query Service adds cluster-level and node-level parameters to limit the size of explain plans in the cache. See [queryPreparedLimit](../n1ql/n1ql-manage/query-settings.md#queryPreparedLimit) and [prepared-limit](../n1ql/n1ql-manage/query-settings.md#prepared-limit).
* The Query Service adds support for sequential scans, controlled by RBAC, which enables querying without an index. See [Query without Indexes](../learn/services-and-indexes/indexes/query-without-index.md).
* The node-level N1QL Feature Control parameter now accepts hexadecimal strings or decimal integers. See [n1ql-feat-ctrl](../n1ql/n1ql-manage/query-settings.md#n1ql-feat-ctrl).
* Queries can now read from replica vBuckets when active vBuckets are inaccessible. The Query service adds new cluster-level, node-level, and request-level parameters to configure this feature. See [Query Settings](../manage/manage-settings/general-settings.md#query-settings).
* The CREATE FUNCTION statement now enables users to create a SQL++ user-defined function and the corresponding external JavaScript code in a single operation, without having to create an external library. See [SQL++ Managed User-Defined Functions](../n1ql/n1ql-language-reference/createfunction.md#sql-managed-user-defined-functions).
* When a query executes a user-defined function, profiling information is now available for any queries within the UDF. See [Manage and Monitor Queries](../n1ql/n1ql-manage/monitoring-n1ql-query.md).
* The Query service collects statistics for the cost-based optimizer automatically when an index is created or built. See [Understand the Cost-Based Optimizer for Queries](../n1ql/n1ql-language-reference/cost-based-optimizer.md).
* The ORDER BY and GROUP BY operations overspill to disk if they exceed the Query service memory quota.

### [](#eventing-service)Eventing Service

* The optional parameter `{ "self_recursion": true }` can be used with the INSERT, UPSERT, and REPLACE advanced operations to prevent the suppression of recursive source bucket mutations. For more information, see [Optional { "self\_recursion": true } Parameter](../../current/eventing/eventing-advanced-keyspace-accessors.md#optional-params-recursion).
* The built-in `ANALYTICS()` function allows the Eventing Service to integrate directly with SQL++ Analytics. This integration simplifies Eventing code logic and lets Eventing benefit from the high availability and load balancing of SQL++ Analytics. For more information, see [ANALYTICS() Function Call](../../current/eventing/eventing-language-constructs.md#analytics%5Fcall).
* The advanced TOUCH operation allows you to modify the expiration time of a document without having to access that document first. For more information, see [Advanced TOUCH Operation](../../current/eventing/eventing-advanced-keyspace-accessors.md#advanced-touch-op).
* The Sub-Document MUTATEIN operation allows you to modify only parts of a document instead of the entire document. This Sub-Document operation is faster and more efficient than a full-document operation like REPLACE or UPSERT. For more information, see [Sub-Document MUTATEIN Operation](../../current/eventing/eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op).

### [](#analytics)Analytics

* Power BI Connector version 1.0 released. ([Power BI Connector documentation](#power-bi-connector:ROOT:index.adoc))  
You can download the installation package from the following location:  

| Binaries      | [powerbi-connector-1.0.mez](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez)               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Binaries SHAs | [powerbi-connector-1.0.mez.sha256](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez.sha256) |

### [](#install-upgrade)Install & Upgrade

* Due to an Erlang compatibility issue, you cannot directly upgrade to Couchbase Server 7.6 from version 6.5 through 7.0\. To upgrade a database running one of these earlier versions to 7.6, first upgrade it to Couchbase Server 7.1 or 7.2\. See [Upgrade](../install/upgrade.md) for more information.

### [](#couchbase-server-community-edition)Couchbase Server Community Edition

* You can no longer set the `sendStats` to `false` in Couchbase Server Community Edition clusters. You can still set `sendStats` to `false` on Couchbase Server Enterprise Edition clusters.

### [](#net-sdk-compatibility).NET SDK Compatibility

Use version 3.5.1 or later of the .NET SDK with Couchbase Server 7.6\. Earlier versions of this SDK have some compatibility issues.