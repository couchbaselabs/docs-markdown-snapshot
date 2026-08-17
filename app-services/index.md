---
title: Manage App Services for Mobile and Edge
description: App Services synchronizes data between the Couchbase Capella
  cluster and your apps running on mobile applications.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/index.adoc
  xref: xref:app-services::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/index.html)

# Manage App Services for Mobile and Edge

> App Services synchronizes data between the Couchbase Capella cluster and your apps running on mobile applications. 

**App Services** is a fully managed application backend designed to provide data synchronization for mobile/IoT applications and the Capella Cloud Service. The service provides:

* Responsive and reliable data synchronization between devices and the NoSQL Couchbase backend. Synchronization is handled automatically, without the need for developer or user intervention, ensuring low latency, data integrity and high availability for mobile applications.
* A mobile database (Couchbase Lite) that support the creation of off-line apps: users can work within a mobile applications, without the need for an always-available network connection. Changes to data stored with the app are synced with the Capella backend when the internet is available.  
![cb mobile illustrations 2](_images/cb-mobile-illustrations_2.png)
* Automatic conflict resolution: concurrent changes across clients are handled through predefined policies, or custom conflict resolvers.
* Seamless OIDC authentication support.
* Peer-to-peer synchronization between mobile/IoT devices.
* Development frameworks and tooling for:

  * [Swift (iOs, macOS)](../couchbase-lite/current/swift/gs-install.md)
  * [Kotlin (Android)](../couchbase-lite/current/android/kotlin.md)
  * [Java (Android](../couchbase-lite/current/android/gs-install.md))
  * [.Net (Desktop, Xamarin)](../couchbase-lite/current/csharp/gs-install.md)
  * [C (Desktop, Mobile, Embedded)](../couchbase-lite/current/c/gs-install.md)
  * [Java (Desktop)](../couchbase-lite/current/java/gs-install.md)
  * [Obj-C (iOS, macOS)](../couchbase-lite/current/objc/gs-install.md)
  * [Javascript](#couchbase-lite:javascript:quickstart.adoc)
  * [A REST API](references/rest-api-introduction.md) for commuting with the Couchbase engine across a secure web connection.

App Services is the synchronization service for Couchbase Capella, designed to provide data synchronization for large-scale interactive web, mobile, and IoT applications.

App Services maintain secure access using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway.
* **Data Routing**, which ensures that authorized users can only access documents in the channels assigned to them and only in accordance with their assigned privileges.

## [](#see-also)See Also

For more information about the underlying product, see [Couchbase Mobile Sync Gateway](../sync-gateway/current/introduction.md).