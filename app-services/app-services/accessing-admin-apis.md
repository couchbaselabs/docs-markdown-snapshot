---
title: Grant Admin Access to REST APIs
description: In order to maintain a high level of security, the REST APIs used
  to administer App Services can only be accessed from a set of defined IP
  addresses.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-services/accessing-admin-apis.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:app-services::app-services/accessing-admin-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-services/accessing-admin-apis.html)

# Grant Admin Access to REST APIs

> In order to maintain a high level of security, the REST APIs used to administer App Services can only be accessed from a set of defined IP addresses. 

Any external application or service that needs to make use of the admin or metrics REST APIs (see [Manage App Services with the App Services API](../references/rest-api-introduction.md) for reference information on the REST APIs), needs to be defined in the App Service administration screen. Each App Service has a configurable Allowed IP list that can include up to 26 entries. Each entry can be a single IP address or an IP address space in CIDR\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] format.

![Selecting the Allowed IP page](../_images/deployment/selecting-allowed-ips-ui.png) 

Figure 1\. The `Allowed IP` page.

The App Service **Settings** **Allowed IP** page lists the IP addresses which we have allowed access. Click on the **Create Allowed IP** button.

![Add allowed IP](../_images/deployment/add-allowed-ip.png) 

Figure 2\. Add Allowed IP

You can permit IP addresses temporarily for testing purposes or set them up permanently.

You can click the **Add Current IP Address** button to fill in the IP address of the machine you're currently working on.

Press the **Add IP** button to save the entry.

![Allowed IP list with single entry](../_images/deployment/allowed-ip-list-with-entry.png) 

Figure 3\. Allowed IP list with single entry

---

[1](#%5Ffootnoteref%5F1). CIDR notation is a compact representation of an IP address and its associated network mask. For more information, see <https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation>