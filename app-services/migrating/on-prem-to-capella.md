---
title: Migrate Existing Self-Managed Couchbase Mobile Clusters to App Services
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/migrating/on-prem-to-capella.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:app-services::migrating/on-prem-to-capella.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/migrating/on-prem-to-capella.html)

# Migrate Existing Self-Managed Couchbase Mobile Clusters to App Services

If you are an existing user of Couchbase Mobile, have set up a Couchbase Server cluster, and have attached Sync Gateway, then you may wish to migrate your data and users from your existing self-managed servers to Couchbase Capella. Once the data and users are migrated, you will have to configure the App Services and set it up for remote sync.

## [](#requirements)Requirements

* You are running a self-hosted Couchbase Server with a Sync Gateway 2.0 or higher with [shared bucket access](../../sync-gateway/current/upgrading.md#upgrade-to-shared-bucket) enabled.
* You have signed up for access to [Capella Cloud](https://cloud.couchbase.com/sign-up).

## [](#process)Process

### [](#step-1-set-up-capella-server-for-replication)Step 1\. Set up Capella server for replication

* First [deploy a Couchbase cluster on Capella](../../cloud/clusters/create-database.md).
* Now [create an appropriately named bucket](../../cloud/clusters/data-service/manage-buckets.md#add-bucket).

### [](#step-2-set-up-xdcr-replication)Step 2\. Set up XDCR replication.

[Set up an XDCR one way data replication](#server:manage:manage-xdcr:create-xdcr-replication.adoc) from the self-managed cluster bucket to the Capella bucket.

> [!WARNING]
> If you are replicating from a 3.x version of Sync Gateway deployment using persistent configuration mode then you MUST SETUP the following XDCR filter
> 
> ```sqlpp
> NOT REGEXP_CONTAINS("^_sync:(dbconfig|registry|dcp_ck|cfg|.*:cfg).*")
> ```

### [](#step-3-wait-for-replication-to-complete)Step 3\. Wait for replication to complete

The following figure shows the setup of the components at this point. XDCR is copying the data from the on-prem bucket into Capella.

During this period, clients are still connected to the original Sync Gateway, and their updates will be captured by the XDCR replication.

![Diagram](../_images/diag-dad0e08a9e6b840fc5cf1d47695799fd20496b32.svg) 

### [](#step-4-detach-replication)Step 4\. Detach replication

Once the XDCR replication is complete:

* Stop Sync Gateway cluster on source self-managed cluster.
* Stop XDCR replication from source self-managed cluster.

This ensures that no new data is written from Couchbase Mobile clients without being migrated to the Capella cluster.

### [](#step-5-set-up-capella-app-services)Step 5\. Set up Capella App Services

Now [launch App Services](../app-services/creating-an-app-service.md) on the target Capella Cluster.

Then [create an App Endpoint](../app-endpoints/creating-an-app-endpoint.md) and configure it via Capella UI. Here are key aspects of the App Endpoint creation that you will have to handle:

* [Import Filter](../app-endpoints/creating-an-app-endpoint.md#app-endpoint-import-filter): If your existing setup uses a custom Import Filter function, you can write the filter function using the inline editor on Capella or import an existing Import Filter function file.
* [Access Control](../app-endpoints/access-control-data-validation.md): You can write the sync function using the inline editor on Capella or import existing sync filter function file.
* [Authentication Provider](../security/set-up-authentication-provider.md): If your existing app uses basic authentication, then there are no changes required. Otherwise, if your existing setup was using OIDC then you will need to reconfigure the OIDC provider on Capella.

Finally, [bring the App Endpoint online](../app-endpoints/configuring-app-endpoints.md#stopping-and-starting).

### [](#step-6-direct-couchbase-mobile-clients-to-the-new-capella-app-services)Step 6\. Direct Couchbase Mobile clients to the new Capella App Services.

Direct Couchbase Lite clients to App Endpoint URL. There are couple of options here:

* You can roll out a new version of the app to point to App Services URL endpoint. There will be downtime as the new app is rolled out.
* You can configure the [load balancer](../../sync-gateway/current/deploy/load-balancer.md) available in the source cluster to redirect existing clients to new App Services target.

The following figure shows the setup of the components now that the migration is complete.

![Diagram](../_images/diag-febfa4b968948cca704b1fe43fe4018f7a1b9e78.svg)