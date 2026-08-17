---
title: Request Support
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/support/pages/manage-support.adoc
  xref: xref:cloud:support:manage-support.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/support/manage-support.html)

# Request Support

> You can request support through the Couchbase Capella UI. 

## [](#requesting-support-through-the-couchbase-capella-ui)Requesting Support Through the Couchbase Capella UI

Support tickets are created and managed on the **Support** tab. A summary of the organization's support tickets is displayed here.

Support tickets can be viewed and created by any user with the [Organization Member](../organizations/organization-user-roles.md#organization-role-view) role.

> [!NOTE]
> If you're a free tier plan user, you're unable to create a support ticket. You're community-supported. Use the Couchbase [forums](https://www.couchbase.com/forums/tag/couchbase-capella), [discord channel](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums&utm%5Fmedium=pinnedpost&utm%5Fcampaign=discord) and [documentation](../get-started/intro.md) for community support and feedback.
> 
> For more support options, [upgrade your plan](../billing/upgrade-account.md).

### [](#support-ticket-summary)Support Ticket Summary

The **Support** tab shows a summary of the organization's open and solved support tickets.

The following information is shown for each support ticket:

| Information | Description                                                                                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID          | A unique identification number for the support ticket, which can be used for reference in communications with Couchbase Capella Support staff.                                                                                   |
| Status      | The current status of the support ticket.                                                                                                                                                                                        |
| Subject     | The subject of the issue, specified by the user who created the support ticket.                                                                                                                                                  |
| Priority    | The importance of the issue.                                                                                                                                                                                                     |
| Requester   | The organization user that was specified as the **Requester** when the support ticket was created.                                                                                                                               |
| Created     | The date and time when the issue was created.                                                                                                                                                                                    |
| Updated     | The timestamp of the last activity associated with the ticket. Activity is classified as any updates made to the ticket by users in your organization, Couchbase Capella Support staff, or Couchbase Capella Support automation. |

## [](#create-support-ticket)Create a Support Ticket

You can expect a response from Couchbase Capella Support in accordance with the cluster's [Support Plan](../billing/billing.md#support-plans) and [Support Time Zone](support.md#support-time-zones).

> [!NOTE]
> If you cannot create a support ticket, click **Contact Us** to call Couchbase Support.

To create a support ticket:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Support**.
3. Click **Create Support Ticket**.
4. Configure the **Create Support Ticket** fields to describe your issue.

| Field         | Description                                                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Subject       | Enter a concise subject that summarizes the overall issue and/or the type of support that you're requesting.                                                                                       |
| Description   | Enter a detailed description of your issue.                                                                                                                                                        |
| Topic         | Select an available category that best fits your issue.                                                                                                                                            |
| Impact        | Select the level of impact that the issue is having in your environment.                                                                                                                           |
| Project       | Select either the project that's associated with the issue, or the project that contains a cluster that's experiencing the issue. Only the projects of which you're a member display in this menu. |
| Cluster       | Select the cluster that's associated with the issue. Only clusters from the project that you selected in the **Project** drop-down display in this menu.                                           |
| SDK Type      | If the issue is about interactions between a cluster and your application, select the language and version of the Couchbase SDK that your application is using.                                    |
| Choose a file | Click **Choose a file** and attach it to the issue, or drag and drop to add a file.                                                                                                                |
5. Click **Create**.  
The newly-created ticket displays in the [support ticket summary](#support-ticket-summary).

### [](#escalate-a-support-ticket)Escalate a Support Ticket

If the impact level of your support ticket changes, you have the option to escalate it.

Go to your support ticket, click **Escalate** and provide a brief explanation for the escalation.

> [!NOTE]
> You can escalate support tickets on **Enterprise** and **Developer Pro** clusters only. You cannot escalate tickets marked as **solved** or those related to billing or single node clusters.

If you cannot escalate your support ticket, click **Contact Us** to call Couchbase Support.

### [](#discuss-a-support-ticket)Discuss a Support Ticket

Add a comment on your support ticket to message the Support team directly. Use comments to discuss your ticket, offer more detail, ask questions, or address deadlines and potential impacts.

> [!NOTE]
> You can only view comments on support tickets marked as **solved**. You cannot add comments in this state.

### [](#verify-support-ticket-status)Verify Support Ticket Status

Your support ticket's activity is dependent on its status.

Go to your support ticket and verify its status in your **Support Ticket Summary**.

| Status              | Activity                       |
| ------------------- | ------------------------------ |
| Open                | You can view and add comments. |
| Awaiting your reply | You can view and add comments. |
| Solved              | You can view comments.         |

## [](#see-also)See Also

* [Support Overview](support.md)
* [Provide Feedback](feedback.md)