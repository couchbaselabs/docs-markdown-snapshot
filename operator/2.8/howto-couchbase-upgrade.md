---
title: Upgrade a Couchbase Deployment
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/howto-couchbase-upgrade.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.8@operator::howto-couchbase-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/howto-couchbase-upgrade.html)

# Upgrade a Couchbase Deployment

> How-to upgrade Couchbase Server to a newer version. 

Given the existing configuration:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:7.0.0 (1)
```

| **1** | [couchbaseclusters.spec.image](resource/couchbasecluster.md#couchbaseclusters-spec-image) can be modified to any valid Couchbase Server image, in this example we want to upgrade the version only. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:7.6.6 (1)
```

| **1** | The modification will trigger the Operator to detect that existing pod specifications do not match the new pod specifications. This will perform a [rolling upgrade](concept-upgrade.md#upgrading-couchbase-server) of Couchbase Server. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#in-place-upgrade)In Place Upgrade

Given the existing configuration:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:7.0.0
  upgradeProcess: InPlaceUpgrade (1)
```

| **1** | This field will inform the operator that we want to perform an in-place upgrade of the existing pods. |
| ----- | ----------------------------------------------------------------------------------------------------- |

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:7.6.6 (1)
  upgradeProcess: InPlaceUpgrade
```

| **1** | The Operator will detect that existing pod specifications do not match the new pod specifications and trigger an in-place upgrade. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------- |