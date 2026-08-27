---
title: Manage Sessions
description: User-sessions with Couchbase Web Console can be timed out,
  following a specified period of user-inactivity.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-security/manage-sessions.adoc
  xref: xref:7.2@server:manage:manage-security/manage-sessions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-security/manage-sessions.html)

# Manage Sessions

> User-sessions with Couchbase Web Console can be timed out, following a specified period of user-inactivity. 

## [](#examples-on-this-page-manage-sessions)Examples on This Page

The examples on this page indicate how to manage sessions by means of the UI and REST API respectively. Sessions cannot be managed with the CLI.

## [](#access-security-screen)Manage Sessions with the UI

Proceed as follows:

1. Access the **Security** screen of Couchbase Web Console, by left-clicking on the **Security** tab, in the right-hand navigation bar:  
![accessSecurityScreen](../_images/manage-security/accessSecurityScreen.png)  
This brings up the **Security** screen, which appears as follows:  
![securityView](../_images/manage-security/securityView.png)
2. Access the **Other Settings** display, by left-clicking on the **Other Settings** tab, on the upper, horizontal control-bar:  
![sessionsTab](../_images/manage-security/sessionsTab.png)  
The **Other Settings** display contains three panels, which are for **Log Redaction**, **Session Timeout**, and **Cluster Encryption**. The **Session Timeout** panel appears as follows:  
![sessionsPanelInitial](../_images/manage-security/sessionsPanelInitial.png)

The interactive pane accepts integers, representing minutes of user-inactivity that are allowed to elapse before the user-session times out, and the login screen is displayed. Enter the required number of minutes with the keyboard. Then, left-click on **Save**, at the lower right of the display, to save the new setting.

Note that 0 seconds, which is the default, specifies that no timeout is applied.

## [](#manage-sessions-with-rest-api)Manage Sessions with the REST API

Use the `/settings/security` URI, with the `uiSessionTimeout` flag specifying the number of _seconds_ to elapse, as follows:

curl -X POST -u Administrator:password \
http://10.142.181.101:8091/settings/security \
-d "uiSessionTimeout=600"