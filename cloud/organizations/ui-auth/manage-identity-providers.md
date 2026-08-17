---
title: Manage Identity Providers
description: After creating a realm, you can change its realm name, rotate its
  certificates, change the default team, turn group mapping on or off, or delete
  it.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/manage-identity-providers.adoc
  xref: xref:cloud:organizations:ui-auth/manage-identity-providers.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/manage-identity-providers.html)

# Manage Identity Providers

> After creating a realm, you can change its realm name, rotate its certificates, change the default team, turn group mapping on or off, or delete it. 

Realms manage the link with your identity provider (IdP). Each organization supports one realm. If you need to create a realm, see [Add SSO Authentication](add-sso-auth.md).

## [](#prerequisites)Prerequisites

* You must have the [Organization Owner](../organization-user-roles.md#organization-role-organization-owner) role to manage realms.

## [](#access-realms)Edit Realms in the Capella UI

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **SSO**.  
When you first open it, the **Organization Realms** page shows basic information about your configured realm.  
> [!TIP]  
> On the Organization Realms page, there is a copy button that provides a link pointing to the SSO login page for Capella and has your realm name prepopulated. You can send this to your users so they can more easily sign in with SSO.
3. Click **⌄** to show more detailed information about the realm. This information includes its Callback URL, Entity ID, Signature Certificate, Signature Algorithm, and Digest Algorithm.
4. Click **Edit Realm**.

### [](#change-realm-name)Change the Realm Name

> [!CAUTION]
> It may be possible for another party to guess your custom realm name. Keep this in mind when you're choosing one. Automatically generated realm names can help prevent this.

When you create a realm, the realm is automatically assigned a unique auto-generated realm name. To change your realm name:

1. Enter your new realm name into the **Realm Name** field.  
When you change the text in the **Realm Name** field, **Notify SSO users of your organizations when the realm name changes** checks automatically. When you save your changes, this notification option sends an email to all SSO users in your organization with the new realm name and a sign-in link that prepopulates the sign-in form with the new realm name.
2. Click **Save**.  
SSO users must provide the realm name when they sign in to Capella to connect to the SSO provider.

### [](#change-cert)Change Signing Endpoint URL and Certificate (SAML)

You can change the signing endpoint URL and signing certificate for an existing realm. Editing these fields allows you to rotate the SAML certificate without having to recreate a realm or cause an outage.

1. In the **Signing Endpoints URL & Certificate** section, enter the new signing endpoint URL and certificate you would like the realm to use.  
You must provide both the URL and certificate to save your changes.
2. Click **Save**.

### [](#change-oidc)Change Identity Provider Configuration (OIDC)

You can change the OpenID Connect Discovery URL, Client ID, Client Secret, and Scopes for an existing realm. When making any change, you must supply a new Client Secret.

1. In the **Identity Provider Configuration** section, enter the new configuration information that you want the realm to use.  
Provide a new Client Secret to save your changes.
2. Click **Save**.

### [](#default-teams)Change the Default Team

> [!CAUTION]
> Capella assigns SSO users to the default team if they're not mapped to another team. Typically, a default team should have the fewest permissions.

Every SSO user is a member of a realm's default team unless otherwise specified through [role mapping](manage-role-mapping.md). When you create a realm, the default team is "My First Team," but you can designate any team in your organization as the default. You cannot delete any team set as the default team.

1. In the **Default Team** section use the **Capella Team** list to choose a new default team.  
This list includes any existing teams within your organization.
2. Click **Save**.  
Any permission changes apply to affected users when they next sign in to Capella.

### [](#group-mapping)Turn Group Mapping On or Off

If group mapping is on, Capella assigns roles to SSO users based on which teams map to which SSO groups. If group mapping is off, you can manage SSO users like any other Capella user.

When you turn off group mapping for a realm, Capella still uses the [default team](#default-teams) to assign roles when SSO users first sign in. After SSO users sign in, you manage them like other Capella users through the **People** tab and each project's **Collaborators** tab.

> [!CAUTION]
> When SSO users sign in for the first time after you turn off group mapping, they keep their current roles. If they sign in after you turn on group mapping, their roles sync based on any mapped SSO groups, and Capella deletes the old permissions.

1. In the **Default Team** section, turn group mapping on or off by selecting or deselecting **Group Mapping**.
2. Click **Save**.  
Any permission changes apply to affected users when they next sign in to Capella.

For more information about managing SSO users with group mapping turned off, see [Manage Organization Users](../manage-organization-users.md) and [Manage Project Users](../../projects/manage-project-users.md).

### [](#delete-a-realm)Delete a Realm

> [!IMPORTANT]
> You cannot delete a realm that you're signed into.

> [!WARNING]
> When you delete a realm, Capella deletes the permissions of all SSO users connected to your organization through that realm.

1. In the **Delete Realm** section, click **Delete Realm**.
2. Type `delete` to confirm the action.
3. Click **Delete Realm**.