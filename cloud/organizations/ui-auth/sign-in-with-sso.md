---
title: Sign in to Capella with SSO
description: Once federated authentication with single sign-on (SSO) is
  configured for your organization, you can sign in to Couchbase Capella with
  SSO.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sign-in-with-sso.adoc
  xref: xref:cloud:organizations:ui-auth/sign-in-with-sso.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/sign-in-with-sso.html)

# Sign in to Capella with SSO

> Once federated authentication with single sign-on (SSO) is configured for your organization, you can sign in to Couchbase Capella with SSO. 

> [!NOTE]
> Couchbase Capella does not support identity provider-initiated (IdP-initiated) sign-in, where the user initiates a sign-in request through the IdP's SSO page.

This page walks you through signing up and signing in to a Couchbase Capella organization that uses SSO.

1. On the [Capella Sign In page](https://cloud.couchbase.com/login), click **Sign in with SSO**.
2. In the **SSO Realm Name** field, enter the _realm name_ for the Capella organization you're signing in to. If you do not know the realm name, contact your Capella administrator.  
> [!TIP]  
> If you're an [Organization Owner](../organization-user-roles.md#organization-role-organization-owner), you can view the realm name and copy a link for the sign in page with the realm name already filled out. See [Manage Identity Providers](manage-identity-providers.md#access-realms) for more information.
3. Click **Submit**.  
Your browser redirects to your organization's configured identity provider (IdP).
4. If not already, sign in to your IdP account.  
Your browser redirects you back to Capella.
5. (_First-Time Sign Up_) If you're signing in to your Capella organization for the first time, you're prompted with a welcome message and to review the terms of service. Click **Sign Up** to accept the terms and create your account.  
You're now signed in to your account. Your permissions depend on the team you belong to.