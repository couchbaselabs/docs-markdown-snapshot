---
title: Sync Metadata Isolation
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/migrating/migrate-sync-metadata.adoc
  xref: xref:app-services::migrating/migrate-sync-metadata.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/migrating/migrate-sync-metadata.html)

# Sync Metadata Isolation

In App Services 4.1 and later, sync metadata moves from the `_default` collection to a dedicated mobile system collection. This improves security and operational consistency by separating system metadata from your application data.

For new App Services deployments on 4.1 and later, this change is automatic. For existing deployments upgrading to 4.1, the migration runs as a background process during the upgrade and does not cause downtime.

## [](#compatibility-considerations)Compatibility Considerations

> [!WARNING]
> The mobile system collection is managed exclusively by App Services. Do not access, modify, or delete its contents directly from your applications, queries, or tooling. For more information, see [the system scope](../../server/current/learn/data/scopes-and-collections.md#the-%5Fsystem-scope-and-its-collections).

If you have custom integrations, [Eventing functions](../../cloud/eventing/eventing-overview.md#eventing-functions), or queries that reference sync metadata in the `_default` collection, you must update them to reference the new system collection location.

Contact [Couchbase Support](#support.adoc) if you're unsure whether this change affects your applications, or to opt-out of the migration during the upgrade. If you opt-out, you can trigger the migration at any time after upgrade.

> [!IMPORTANT]
> Before you upgrade, verify your App Services deployment is running version 4.1 or later.

## [](#upgrade-behavior)Upgrade Behavior

When you upgrade an existing App Services deployment to 4.1, the following applies:

* The migration runs automatically as a background process.
* Your App Services operations continue without interruption.
* If your applications are not ready for the metadata location change, contact [Couchbase Support](#support.adoc) before upgrading to defer the migration.

## [](#trigger-migration-after-upgrade)Trigger Migration After Upgrade

If your App Services opted out of the migration during the 4.1 upgrade, you can trigger it from App Services settings at any time.

The migration applies to all App Endpoints within the App Services. You cannot trigger it for individual App Endpoints.

> [!IMPORTANT]
> Migrating sync metadata to the mobile system collection is irreversible.

### [](#steps)Steps

1. In the Capella UI, navigate to your App Services.
2. Click the **Settings** tab.
3. Under **Sync Metadata Isolation**, select **Migrate sync metadata to mobile system collection**.
4. Click **Save**.

The migration runs as a background process and does not affect your App Services operations or cause downtime. You can also trigger the migration using the [Management API](../references/rest%5Fapi%5Fadmin.md).