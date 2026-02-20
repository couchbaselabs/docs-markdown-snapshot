---
title: Manage Settings
description: Couchbase-Server <em>settings</em> can be established by the administrator.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-settings/manage-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:manage:manage-settings/manage-settings.adoc[]
---

[View original HTML](/server/7.2/manage/manage-settings/manage-settings.html)

# Manage Settings

> Couchbase-Server _settings_ can be established by the administrator. 

## [](#couchbase-server-settings-overview)Settings Overview

The _settings_ for Couchbase Server can be accessed via Couchbase Web Console. Left-click on the **Settings** tab, in the left-hand navigation menu:

![settingsTab](../_images/manage-settings/settingsTab.png) 

By default, this brings up the **General** settings panel. Along the upper, horizontal control-bar, multiple tabs appear, from which different settings-categories can be selected:

![settingsCategoryTabs](../_images/manage-settings/settingsCategoryTabs.png) 

The tabs are:

* _General_. Allows configuration of _name_, _memory quotas_, _storage modes_, and _node availability_ for the cluster; and of _advanced settings_ for the Index and Query Services These are described in [General](general-settings.md).
* _Auto compaction_, whereby data on the server is automatically compacted if specified thresholds are met. These are described in [Auto-Compaction](configure-compact-settings.md).
* _Alerts_, whereby users can be notified of critical system-events. These are described in [Alerts](configure-alerts.md).
* _Sample buckets_, whereby buckets pre-populated with documents can be installed, for the purpose of experimentation and testing. These are described in [Sample Buckets](install-sample-buckets.md).