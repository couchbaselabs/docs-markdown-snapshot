---
title: Migrate Existing Self-Managed Couchbase Mobile Clusters to App Services
description: Migrate your data, users, and roles from a self-managed Couchbase
  Server and Sync Gateway deployment to Capella App Services.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Capella App Services
    version: ""
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/migrating/on-prem-to-capella.adoc
  xref: xref:app-services::migrating/on-prem-to-capella.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/migrating/on-prem-to-capella.html)

# Migrate Existing Self-Managed Couchbase Mobile Clusters to App Services

If you're an existing Couchbase Mobile user, you may already have a Couchbase Server cluster with an attached Sync Gateway. You can migrate your data and users from your self-managed servers to Couchbase Capella. Once you migrate the data and users, configure the App Services for remote sync.

## [](#requirements)Requirements

* You're running a self-hosted Couchbase Server with a Sync Gateway 2.0 or higher with [shared bucket access](../../sync-gateway/current/sync/sync-with-couchbase-server.md#sba-feature) enabled.
* You have registered for access to [Capella Cloud](https://cloud.couchbase.com/sign-up).
* You migrate your data with XDCR, the only supported migration method. App Services does not support backup and restore with `cbbackupmgr` for this migration. The `--filter-keys` option accepts only an include regular expression and does not support excluding patterns, so a restore cannot exclude the `_sync` configuration and registry documents.

## [](#before-you-migrate)Before You Migrate

Give your App Endpoint the same name as your on-prem Sync Gateway database. Sync Gateway calculates a metadata ID for each database, and a different name can produce a different metadata ID. If that happens, App Services cannot find the existing metadata documents in the bucket, including the user and role documents that XDCR copies. This requirement still applies in App Services 4.1.

XDCR copies your Sync Gateway users and roles to Capella along with your data. The following table shows when a matching name is strictly required:

| Configuration type                              | App Endpoint name requirement                                                                                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default collection only                         | Use a matching name. Users and roles also carry over with a different name because this configuration sets no metadata ID, but a matching name avoids the risk. |
| Persistent configuration with named collections | Required. The App Endpoint must use the same name as the on-prem database, and the same scopes and collections.                                                 |

Compare every setting in your on-prem database configuration with the App Endpoint configuration, for example delta sync. Some on-prem settings have no Capella equivalent and no exact migration path. Examples include Inter-Sync Gateway Replication, `revs_limit`, and `import_partitions`, but this is not a complete list.

If your on-prem configuration sets `enable_star_channel` to `false`, remove that setting. App Services always enables the star channel to support reliable replication of the `*` channel.

Before you start Step 1, record the following from your on-prem configuration:

* Database name
* Scopes
* Collections
* Configuration settings

Later steps depend on them.

## [](#process)Process

Complete the following steps to migrate from your self-managed cluster to App Services.

### [](#step-1-set-up-capella-server-for-replication)Step 1\. Set up Capella server for replication

* First [deploy a Couchbase cluster on Capella](../../cloud/clusters/create-database.md).
* Now [create an appropriately named bucket](../../cloud/clusters/data-service/manage-buckets.md#add-bucket). Give the bucket the same name as the source bucket on your self-managed cluster.

### [](#step-2-set-up-xdcr-replication)Step 2\. Set up XDCR replication

[Set up an XDCR one way data replication](#server:manage:manage-xdcr:create-xdcr-replication.adoc) from the self-managed cluster bucket to the Capella bucket. For the Capella side of the setup, see [Replicate from a self-managed cluster to Capella](../../cloud/clusters/xdcr/manage-xdcr-replications.md#from-on-prem-to-capella).

> [!IMPORTANT]
> Use a one-way replication that copies the whole bucket. Do not use the Active-Active XDCR with Sync Gateway setup for this migration.

> [!WARNING]
> If your Sync Gateway deployment uses persistent configuration mode, you must configure the following XDCR filter:
> 
> ```sqlpp
> NOT REGEXP_CONTAINS(META().id, "^_sync:(dbconfig|registry|dcp_ck|cfg|.*:cfg)")
> ```

#### [](#xdcr-private-link)Replicate Over a Private Endpoint

XDCR over a private endpoint is available only on request from Capella Support, and only when your self-managed cluster and your Capella cluster use the same cloud service provider and region. For the full requirements, see [Replicate Data Over a Private Endpoint Connection](../../cloud/clusters/xdcr/manage-xdcr-security.md#private-endpoints).

Once Capella Support has made the feature available, [enable XDCR over the private endpoint](../../cloud/clusters/xdcr/manage-xdcr-security.md#enable-pe-xdcr) for your Capella cluster with the Management API. Then create the XDCR remote reference on your self-managed cluster, using the cluster's [Private Endpoint DNS](../../cloud/clusters/xdcr/manage-xdcr-replications.md#get-hostname) as the hostname:

* Couchbase Server 8.x: in the Web Console, set the network type to **Force using alternate address**.
* Couchbase Server 7.x: create the remote reference with the [REST API](../../server/current/rest-api/rest-xdcr-create-ref.md) and set `network_type=external`.

### [](#step-3-wait-for-replication-to-complete)Step 3\. Wait for replication to complete

The following figure shows the setup of the components at this point. XDCR is copying the data from the on-prem bucket into Capella.

During this period, clients stay connected to the original Sync Gateway, and XDCR replication captures their updates.

![Diagram](../_images/diag-f6485af74e66ecec4fed596e8f353fb228537a58.svg) 

### [](#step-4-detach-replication)Step 4\. Detach replication

Once the XDCR replication is complete:

* Stop Sync Gateway cluster on source self-managed cluster.
* Stop XDCR replication from source self-managed cluster.

This ensures that Couchbase Mobile clients cannot write new data that never migrates to the Capella cluster.

### [](#step-5-set-up-capella-app-services)Step 5\. Set up Capella App Services

Now [launch App Services](../app-services/creating-an-app-service.md) on the target Capella Cluster.

Then [create an App Endpoint](../app-endpoints/creating-an-app-endpoint.md) and configure it via Capella UI. Give your App Endpoint the same name as your on-prem Sync Gateway database, so App Services finds your migrated users and roles. For more information, see [Before You Migrate](#before-you-migrate).

Here are key aspects of the App Endpoint creation that you'll have to handle:

* [Import Filter](../app-endpoints/import-filters.md): If your existing setup uses a custom Import Filter function, you can write the filter function using the inline editor on Capella or import an existing Import Filter function file.
* [Access Control](../app-endpoints/access-control-data-validation.md): You can write the sync function using the inline editor on Capella or import existing sync filter function file.
* [Authentication Provider](../security/set-up-authentication-provider.md): If your existing application uses basic authentication, then there are no changes required. If your existing setup uses OpenID Connect (OIDC), reconfigure the OIDC provider on Capella.
* Users and roles: Your Sync Gateway users and roles carry over through XDCR when your configuration meets the conditions in [Before You Migrate](#before-you-migrate). If they do not carry over, recreate them with the [App Services Admin API](../references/rest%5Fapi%5Fadmin.md).
* Configuration settings: Apply the on-prem database settings that have an App Endpoint equivalent, such as delta sync. For settings with no Capella equivalent, see [Before You Migrate](#before-you-migrate).

[Bring the App Endpoint online](../app-endpoints/configuring-app-endpoints.md#resume-endpoint).

### [](#step-6-direct-couchbase-mobile-clients-to-the-new-capella-app-services)Step 6\. Direct Couchbase Mobile clients to the new Capella App Services

Direct Couchbase Lite clients to App Endpoint URL. Choose one of the following options:

* You can roll out a new application version that points to the App Services URL endpoint. Rolling out the new version this way causes downtime.
* You can configure the [load balancer](../../sync-gateway/current/deploy/load-balancer.md) available in the source cluster to redirect existing clients to new App Services target.

The following figure shows the setup of the components now that the migration is complete.

![Diagram](../_images/diag-037b226a920ec99afc1a90883752c93279074737.svg)