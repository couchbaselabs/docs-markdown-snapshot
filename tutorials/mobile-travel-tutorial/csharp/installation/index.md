---
title: Backend Installation
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/csharp/installation/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:csharp/installation/index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/csharp/installation/index.html)

# Backend Installation

First, we will install the "backend components" required for the tutorial. This includes Couchbase Server, Sync Gateway and Python web app - essentially all components with the exception of the Couchbase Lite app.

If you already have a running instance of the Python Travel Sample Web App, Sync Gateway and Couchbase Server you can skip this section of the tutorial and proceed to the installation of the Couchbase Lite client app.

There are three options available to install those components.

| [Manual](manual.md)                                                        | [Docker (Local)](docker.md)                                                                                     |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Here, you would download and install the components on your local machine. | In this case, you would install all the backend components in separate docker containers on your local machine. |

> [!NOTE]
> Make sure to use the same installation option for _all_ backend components, so if you select Docker (Local), then you must use docker for Python Travel Sample Web App, Sync Gateway and Couchbase Server.