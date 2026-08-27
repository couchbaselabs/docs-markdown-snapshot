---
title: Configure SAML
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-security/configure-saml.adoc
  xref: xref:enterprise-analytics:manage:manage-security/configure-saml.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/configure-saml.html)

# Configure SAML

You can enable _Structured Authentication Markup Language_ (SAML) authentication that allows users to log into the Enterprise Analytics Web Console. This authentication methods offers features such as single sign on, two-factor authentication, and centralized authentication administration.

To learn more about SAML, see [SAML Authentication](#learn:security/authentication-domains.adoc#saml-authentication).

## [](#prerequisites)Prerequisites

Before configuring SAML authentication consider the following:

### [](#identity-provider)Identity Provider

SAML authentication relies on an _Identity Provider_ (IdP) to authenticate a user with the Enterprise Analytics Web Console. Enterprise Analytics supports the following IdPs:

* Okta
* Microsoft Azure AD

> [!NOTE]
> Other IdPs may work. Enterprise Analytics was tested with the IdPs in the previous list.

Your IdP may have its own requirements for interacting with services like Enterprise Analytics. See your IdP's documentation to understand its requirements.

### [](#idp-metadata)IdP Metadata

Enterprise Analytics needs metadata about the IdP to be able to accept authentication messages from it. Your IdP provides you with a URL to retrieve this metadata. If your Couchbase Cluster can connect to the IdP, you can have it directly retrieve the metadata. You can configure Enterprise Analytics to periodically refresh this metadata to learn of changes to the IdP's configuration.

If Enterprise Analytics cannot connect to the IdP, you can upload a file containing the metadata when initially configuring SAML authentication. In this case, you may need to manually update the configuration periodically.

### [](#certificates)Certificates

You need a key and certificate for your Couchbase cluster to use when signing messages to the IdP. The IdP uses the certificate to verify the signature in SAML messages. This verification lets the IdP know that the message came from Enterprise Analytics. You can use a certificate specifically for SAML authentication or reuse the same certificate you use for client authentication.

You can configure Enterprise Analytics to authenticate SAML message signatures to verify that they came from the IdP. It can authenticate the signature using a full certificate or a trusted fingerprint which is a hash of the certificate. Fingerprints are smaller, so there is a bit less overhead on Enterprise Analytics when using them instead of a full certificate. In either case, you must get the certificate or fingerprint from the IdP so Enterprise Analytics can use it.

To use fingerprints, you just copy them from your IdP and paste them into the Couchbase SAML configuration page.

When using certificates to authenticate messages, Enterprise Analytics gets the certificate from the IdP's metadata. Getting the certificate from the metadata can automate updating new certificates due to key rotation. Enterprise Analytics automatically updates to a new certificate if you configure it to refresh the metadata periodically.

If you choose to use certificates, you must make sure Enterprise Analytics gets the metadata from the IdP securely. You have three options to securely get the metadata:

* Give Enterprise Analytics a secure HTTPS URL to retrieve the metadata from the IdP directly. Then enable **Verify remote peer** on the SAML configuration page and supply the CA certificate that issued the certificate for the IdP's metadata site. This certificate is often different from the certificate it uses to sign its SAML metadata. With this configuration, Enterprise Analytics verifies the identity of the IdP when downloading the metadata.
* If the IdP signs its metadata, enable **Validate metadata using trusted fingerprints** on the SAML configuration page. Then add a trusted fingerprint for the IdP's certificate to the **Trusted Fingerprints** box. Enterprise Analytics verifies the IdP's signature in the metadata using the fingerprint and therefore trusts the certificate in the metadata.
* Directly download the metadata from the IdP and upload it to Enterprise Analytics via the SAML configuration page. In this case, be sure you're using a secure HTTPS connection to the IdP when downloading its metadata.

### [](#network-configuration)Network Configuration

Some IdPs do not require a direct network connection to your Enterprise Analytics. Instead, the user's browser transmits the authentication request and response between Enterprise Analytics and the IdP. As long as the user's browser can reach both Enterprise Analytics and the IdP, they can use SAML to authenticate.

However, some IdPs may want to connect to services such as Enterprise Analytics to verify SAML metadata such as the certificate. This connection enables frequent key rotation, which helps increase security. Verify any inbound network connection requirements with your IdP.

If you restrict your Couchbase cluster's connections to the Internet, consider granting it access to the IdP. Allowing this connection makes SAML configuration easier by letting Enterprise Analytics retrieve most of the configuration information it needs directly from the IdP. This connection also automates updating the IdP's certificates when they change due to key rotation.

### [](#group-and-roles-management)Group and Roles Management

Decide whether you'll manage group and role membership in Enterprise Analytics or in the IdP. If you decide to manage groups and roles in Enterprise Analytics, create Enterprise Analytics users in the external authentication realm. Assign these users the groups and roles they need. If you choose to manage groups and roles in the IdP, create SAML attributes that you'll map to Enterprise Analytics groups and roles. Edit the users in the IdP so their attributes reflect the groups and roles they need.

### [](#nameid)NameID and User Identity

The SAML authentication message sent from the IdP to Enterprise Analytics identifies the user using a format called nameID. The nameID format is a colon-delimited string. It can be one of the following values:

* `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` uses a unique identifier that remains constant across different IdPs and services. This is the default value for Enterprise Analytics.
* `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` does not set a format for the user identity. It can be any text string.
* `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` sets the format to an email address.
* `urn:oasis:names:tc:SAML:2.0:nameid-format:transient` uses a unique but temporary identifier

Instead of relying on the nameID, you can have Enterprise Analytics get the username from an attribute in the SAML message. Use an attribute instead of the nameID if the IdP uses a format that doesn't match Enterprise Analytics usernames. For example, suppose the IdP only supports identifying users using an email address instead of a username. In this case, you can have the IdP send the user's username in an attribute. Then configure Enterprise Analytics to extract the username from the attribute instead of using the nameID.

## [](#configure-saml-with-the-ui)Configure SAML with the UI

To configure SAML authentication using Enterprise Analytics Web Console:

1. In the navigation bar, click **Security**.
2. In the navigation menu, click **SAML**.
3. Turn on the **Enabled** toggle.
4. Complete the following procedures to finish configuring SAML:

  1. [Configure Couchbase Metadata](#configure-couchbase-metadata)
  2. [Configure the IdP](#configure-the-idp)
  3. [Configure Single Sign-On](#configure-single-sign-on)
  4. Optionally, [Configure Advanced Settings](#configure-advanced-settings).
5. Click **Save** to save the SAML settings.
6. Verify that Enterprise Analytics saved the settings by looking for a green popup stating that the settings were saved. If you do not see this popup, look for error messages at the top of the SAML Configuration page.

After you enable SAML authentication, the top of the configuration page lists several URLs you need when you configure your IdP:

* **Current SP metadata URL**: the URL to retrieve your Enterprise Analytics's SAML metadata. A link also appears that you can use to download the metadata. Use this link if your IdP is not able to connect to Enterprise Analytics directly.
* **Current SP consume URL**: the SAML _Assertion Consumer Service_ (ACS) endpoint for your Enterprise Analytics. The IdP sends SAML assertion messages to this endpoint.
* **Current SP logout URL**: the URL to which the IdP sends SAML logout requests and responses.

### [](#configure-couchbase-metadata)Configure Couchbase Metadata

Under **Metadata**, enter information about your Enterprise Analytics and organization. Most of these fields supply contact information to your IdP and do not affect the authentication process. The exceptions are:

SP Entity ID

A URL that identifies your Enterprise Analytics to the IdP. You add this URL to your IdP's configuration so it can identify the service with which the user is authenticating. This field is optional. If you do not enter a value, Enterprise Analytics uses a URL based on the node's fully qualified domain name, port number, and the path to the SAML metadata page (`/saml/metadata`).

SP Base URL Type

This option controls hostname in the URL to which the IdP redirects the user's browser after authentication. Choose this option based on the address users enter to connect to your Enterprise Analytics:

* **Node address** sends the user back to the self-reported address of the node the user is logging into.
* **Alternate node address** sends the user to the node's alternate address. See [Alternate Addresses](#learn:clusters-and-availability/connectivity.adoc#alternate-addresses).
* **Custom URL** sends the user to the URL you enter in **Custom URL** box which appears when you select this option. Select this option when users use some other URL when connecting to nodes in the cluster. For example, if you use a load balancer to redirect users to nodes, enter its URL here.

Key and Certificates

Add the Enterprise Analytics's private key and certificate. Either copy and paste their content or upload them by clicking **Select File**. If the certificate was not directly signed by a CA, added the intermediate certificates in **Certificate chain**.

### [](#configure-the-idp)Configure the IdP

Under **Identity Provider Configuration**, enter the information about your IdP:

Load IDP metadata from

Either enter the IdP's metadata URL or upload a snapshot of its metadata in a file. If you provide a URL, you can have Enterprise Analytics refresh the metadata periodically.

Verify remote peer

Select to enable verification of the IdP's certificate. Only has an effect if you entered a secure URL (`https://`) in **Load IDP metadata from**. If you enable this option, supply a copy of the IdP's certificate in **CA Certificates**.

Validate metadata using trusted fingerprints

Select to enable using fingerprints to validate the signature of the IdP's metadata. Select **Use trusted fingerprints for metadata bootstrap only** to limit using fingerprint verification to just the initial retrieval of the metadata. Select **Always use trusted fingerprints to validate signatures in SAML…​** to use fingerprints to validate all SAML messages instead of just metadata.

Trusted Fingerprints

Add the IdP's trusted fingerprints if you're using them to validate the IdP's messages.

### [](#configure-single-sign-on)Configure Single Sign-On

Under the **Single Sign-On** section, configure how Enterprise Analytics and the IdP communicate about user authentication.

Authentication IDP Binding

Logout IDP Binding

Select **Post** if Enterprise Analytics should use POST messages to send authentication and logout requests to the IdP. Select **Redirect** if Enterprise Analytics should use URL parameters instead.

Validate assertion signature

Validate assertion envelope signature

Select to have Couchbase verify the signature of either the SAML assertions or the entire SAML envelope the IdP sends. You should enable at least one form of signature validation based on how your IdP signs its messages.

NameID format

Enter the format that the IdP uses to identify the user. You must enter a value here, even if you configure Enterprise Analytics to use an attribute for the username.

Username attribute

Select if you want to use a SAML attribute for the username and enter the attribute's name in **Username attribute** box.

Groups attribute

Select if you want Enterprise Analytics to get group membership from the IdP. Enter the name of the SAML attribute containing the groups in the **Groups attribute** box. Enter the separator character in **Groups separator** if your IdP sends lists of groups in a string. If you want Enterprise Analytics to only use a subset of the group names that the IdP sends it, enter a regular expression in **Groups filter**. Enterprise Analytics only applies a group to the user if the group's name matches the regular expression.

Roles attribute

Select if you want the IdP to manage user roles. Works the same way the Groups attribute works.

### [](#configure-advanced-settings)Configure Advanced Settings

In most cases you do not need to change the settings under **Advanced**. If you're having an issue with the SAML integration, these settings may help resolve it. Most of these settings are self-explanatory. The following need some explanation:

Value of SP metadata cacheDuration attribute

Sets how long the IdP caches Enterprise Analytics's metadata. This value is in [ISO8601 duration format](https://en.wikipedia.org/wiki/ISO%5F8601#Durations). The default value `P1M` sets this duration to one month.

SP Assertion Dupe Check

When you select **Enable Dupe Check**, Enterprise Analytics prevents a user from reusing an IdP's SAML assertion to log in a second time. If you enable this option, you can choose whether this restriction applies to all nodes or just a single node. Select the **Global** option to prevent users from reusing a SAML assertion on any node in the cluster. Select **Local** to prevent SAML assertion reuse on the same node. The **Local** option allows a user reuse a SAML assertion to log into a different node.

## [](#configuring-okta-as-a-saml-idp)Configuring Okta as a SAML IdP

Okta is an SSO service that supports SAML and enables 2FA. Follow these steps to configure Okta as a SAML IdP for Enterprise Analytics.

1. Log into your Okta administrator account.
2. Under **Applictions** click **Applications**.
3. Click **Create App Integration**.
4. Select **SAML 2.0** and click **Next**.
5. In **App Name**, enter a name for your Enterprise Analytics and click **Next**.
6. In the **General** section, configure Okta's integration with Enterprise Analytics. The following table lists the Enterprise Analytics fields and their corresponding Okta fields.

| Okta Field             | Couchbase field             | Notes                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single sign-on URL** | **Current SP consume URL**  | **Current SP consume URL** appears in Enterprise Analytics's SAML Configuration page after you enable SAML authentication. The default value is the URL of the Couchbase node plus the path saml/consume. You can add a placeholder value in Okta initially. After enabling SAML in Enterprise Analytics, update the value in Okta. |
| **Audience URI**       | **Current SP metadata URL** | Use the URL shown in **Current SP metadata URL** after enabling SAML in Enterprise Analytics. You can use a placeholder in Okta until after you finish enabling SAML in Enterprise Analytics.                                                                                                                                       |
| **Name ID format**     | **NameID format**           | Okta lists just the description of the format instead of the entire format string. For example, select **Unspecified** in Okta's **Name ID format** list if you entered urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified in Couchbase's **NameID format** field.                                                               |
7. In **Application username** field, choose the Okta attribute that corresponds to the Enterprise Analytics username. For example, choose **Okta username** if the username in Okta is the same as the username in Enterprise Analytics. Choose any value if you're using a SAML attribute instead of the SAML subject to set the username for Enterprise Analytics.
8. Under **Attribute Statements** add entries for any Okta attributes you to want to pass to Enterprise Analytics as SAML attributes. For example, suppose you want to use a SAML attribute to pass the user's roles from Okta to Couchbase. Then choose a name for the SAML attribute and enter it under the **Name** column. Under the **Value** column, select the Okta attribute for the roles. Later, enter the attribute name in the **Roles attribute** field on the Enterprise Analytics's SAML page.
9. Configure the SAML attribute name under **Group Attribute Statements** if you're using the user's Okta's group membership to set the user's Enterprise Analytics groups. In the **Name** column, enter the attribute name you set in **Groups attribute** field of the Enterprise Analytics SAML configuration page.
10. Click **Next** and then **Finish**.
11. The **Sign On** tab contains the information you need to enter into the Enterprise Analytics SAML configuration page. Click **More details** to show all of the information you need.
12. Copy the Okta values in the following table to their corresponding fields on the SAML page.

| Okta Value              | SAML Page Field                        | Notes                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Metadata URL**        | **URL** under **Metadata**             |                                                                                                                                                                                                                    |
| **Signing Certificate** | **CA Certificates** under **Metadata** | **CA Certificates** is hidden until you select **Verify remote peer**. You can download the certificate from Okta by clicking **Download** and then upload it to Enterprise Analytics by clicking **Select File**. |
13. Fill in the rest of the Enterprise Analytics SAML page as explained in [Configure SAML with the UI](#configure-saml-with-the-ui).
14. In Okta, click the **Assignments** tab.
15. Assign users who need to log into the Enterprise Analytics Web Console to the Okta application you just created. See the Okta documentation for the steps you need to take.

## [](#configure-saml-with-the-rest-api)Configure SAML with the REST API

Use the `/settings/saml` endpoint to configure a SAML IdP using the REST API. The following example demonstrates calling this endpoint using curl. In the following example:

Unresolved include directive in modules/manage/pages/manage-security/configure-saml.adoc - include::rest-api:partial$saml-post-example-intro.adoc\[\]

Unresolved include directive in modules/manage/pages/manage-security/configure-saml.adoc - include::rest-api:example$post-saml.sh[]