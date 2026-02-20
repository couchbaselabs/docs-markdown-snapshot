---
title: Scale a Deployed App Service
description: Having deployed an App Service, you may wish to scale it up or down
  by adjusting its configuration.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-services/scaling-a-deployed-app-service.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:app-services::app-services/scaling-a-deployed-app-service.adoc[]
---

[View original HTML](/app-services/app-services/scaling-a-deployed-app-service.html)

# Scale a Deployed App Service

> Having deployed an App Service, you may wish to scale it up or down by adjusting its configuration. 

By increasing the number and/or the specifications of the nodes, you can adjust the cost and performance of the App Service.

1. Select the App Service you want to configure from the list of App Services attached to your project.
2. Select the **Settings** tab.
3. Select **Configuration** from the menu list on the left of the screen.

![App Service configuration screen](../_images/deployment/configuration-screen.png) 

From here you can adjust the number of nodes and the number of CPUs/amount of memory for each of those nodes.

> [!NOTE]
> There is no downtime associated with changing the configuration. The App Services will continue to run while the system is reconfigured.
> 
> If you deployed a Single Node App Service to use with a [Single Node cluster](../../cloud/clusters/databases.md#option), you cannot add additional nodes. You can choose to switch between the 2 available Compute configuration options for Single Node App Services.

For more details on deployment configurations, see [./configuring-app-endpoints.adoc](#./configuring-app-endpoints.adoc)