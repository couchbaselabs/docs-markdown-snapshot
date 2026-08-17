---
title: Upgrade a Couchbase Deployment
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-couchbase-upgrade.adoc
  xref: xref:2.5@operator::howto-couchbase-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-couchbase-upgrade.html)

# Upgrade a Couchbase Deployment

> How-to upgrade Couchbase Server to a newer version. 

Given the existing configuration:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:6.6.4 (1)
```

| **1** | [couchbaseclusters.spec.image](resource/couchbasecluster.md#couchbaseclusters-spec-image) can be modified to any valid Couchbase Server image, in this example we want to upgrade the version only. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  image: couchbase/server:7.2.0 (1)
```

| **1** | The modification will trigger the Operator to detect that existing pod specifications do not match the new pod specifications. This will perform a [rolling upgrade](concept-upgrade.md#upgrading-couchbase-server) of Couchbase Server. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |