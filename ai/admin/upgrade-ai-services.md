---
title: Upgrades for AI Services
description: Your AI Services components run regular maintenance jobs to
  maintain health and reliability.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/admin/pages/upgrade-ai-services.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:admin:upgrade-ai-services.adoc[]
---

[View original HTML](/ai/admin/upgrade-ai-services.html)

# Upgrades for AI Services

> Your AI Services components run regular maintenance jobs to maintain health and reliability. 

Maintenance jobs are scheduled by support. You cannot change or reschedule a maintenance job on your AI Services.

The following AI Services can receive regular maintenance jobs:

* [Workflows](../build/vectorization-service/data-processing.md)
* [Model Service](../build/model-service/model-service.md)

## [](#what-happens-during-a-maintenance-job)What Happens During a Maintenance Job

When a new maintenance job is available, a banner displays in the Capella UI, giving you information about the specific affected service.

Depending on the specific maintenance job, your service or its workflows might become temporarily unavailable until the maintenance job completes.

If you deploy a new service at the same time as a scheduled upgrade, Capella queues the deployment and upgrade operations, based on whatever operation was requested first.

The Capella Model Service must be healthy to complete an upgrade. A specific model in an unhealthy state does not stop the Model Service from upgrading. Models do not have to finish deploying through the Model Service for the Model Service to upgrade.

## [](#new-model-version-upgrades)New Model Version Upgrades

When a new version of a model becomes available on the Model Service, Capella does not automatically upgrade your existing model deployment.

If you want to use the newest version of a model on the Model Service, you must deploy that model as a separate deployment.

## [](#see-also)See Also

* [Process Your Data For Capella AI Services](../build/vectorization-service/data-processing.md)
* [Deploy Models with the Capella Model Service](../build/model-service/model-service.md)