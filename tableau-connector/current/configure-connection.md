---
title: Configure the Connection
description: Set up a connection between Tableau and Enterprise Analytics using
  the Couchbase Tableau Connector.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/configure-connection.adoc
  xref: xref:tableau-connector::configure-connection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/configure-connection.html)

# Configure the Connection

> Set up a connection between Tableau and Enterprise Analytics using the Couchbase Tableau Connector. 

## [](#set-up-the-connection)Set Up the Connection

To set up a connection between Tableau and Enterprise Analytics:

1. Open **Tableau Desktop**.
2. Go to **Connect** **To a Server** **More**.
3. Select a Couchbase Tableau Connector. If there are multiple connectors installed, select the one that is compatible with Enterprise Analytics.
4. In the connection dialog, enter the following details:

| **Server**         | The host and port details. The default HTTP port is 8095, while the default HTTPS/TLS port is 18095.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scope**          | (Optional) The scope to extract data from. You can leave this field blank or use Default if your data is in the default scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Authentication** | The authentication method to use for the connection. Based on the authentication method you select, the required fields differ. Authentication Method Required Fields Description Username and Password Username, Password Enter user credentials. LDAP Username, Password Enter LDAP credentials. Client Certificate Client Certificate Select the client certificate mode. You can select either PEM Files (Certificate + Key) or Keystore (JKS/PKCS12). OAuth 2.0 OAuth Provider Select the OAuth provider from the list. The list contains the default Keycloak configuration and any custom configurations you created. For more information, see [Create a Custom Configuration File](#create-a-custom-configuration-file). To use OAuth 2.0 authentication, you need: Tableau Connector 2.0 or later Enterprise Analytics 2.2 or later An Identity Provider (IdP) A custom XML configuration file For more information, see [OAuth 2.0 Authentication](#oauth-2-0-authentication). |
5. (Optional) Select the **Require SSL** option, if required.  
To set up SSL support, see:

  * [SSL Support for Tableau Desktop](setup-tableau-desktop.md#ssl)
  * [SSL Support for Tableau Server](setup-tableau-server.md#ssl)
6. For advanced settings, click the **Advanced** tab. You can set the connection timeout and scan consistency mode. If you set the scan consistency to `Request plus`, a dropdown appears to select the scan wait time.
7. Click **Sign In**.

## [](#oauth-2-0-authentication)OAuth 2.0 Authentication

The Tableau Connector 2.0 supports OAuth 2.0 authentication for Enterprise Analytics 2.2 and later.

This authentication method uses an external Identity Provider (IdP) to issue an JSON Web Token (JWT). When you initiate a connection, the Tableau Connector opens a browser window for you to log in to the IdP. After you log in, the connector retrieves the access token and passes it to the JDBC driver to authenticate your connection.

Tableau manages token refreshing automatically, so you do not need to manually refresh the token.

To use OAuth 2.0 authentication, you need to:

1. [Get the required IdP details](#get-idp-details)
2. [Create a custom XML configuration file with those IdP details](#create-a-custom-configuration-file)

### [](#get-idp-details)Get IdP Details

The following table lists the IdP details you need to set up OAuth 2.0 authentication.

| Item                    | Description                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Identity Provider (IdP) | An OIDC-compliant IdP must be running and accessible from Tableau. For example: [Keycloak](https://www.keycloak.org/) [Okta](https://www.okta.com/) [Microsoft Azure AD/Entra ID](https://www.microsoft.com/en-in/security/business/identity-access/microsoft-entra-id). |
| Issuer URL              | The base OIDC discovery URL of your IdP realm.For example: <http://192.168.88.4:8080/realms/cb>                                                                                                                                                                          |
| Public Client ID        | A public OIDC client registered on your IdP that: Does not use a client secret. Allows the redirect URIs used by Tableau.                                                                                                                                                |
| Scopes                  | The registered client must have at least the following scopes enabled: openid offline\_access (required for token refresh) You can add additional scopes as well.                                                                                                        |
| User Account            | A valid user account on the IdP and the same user must be registered as an external user on Couchbase.                                                                                                                                                                   |

Once you've established these details, create a custom configuration file.

### [](#create-a-custom-configuration-file)Create a Custom Configuration File

To connect Tableau to your IdP, you must provide your client ID, authentication endpoints, and other IdP settings. You can provide this information in a custom XML configuration file.

Once you add the file to the correct location, Tableau automatically loads it and displays your IdP in the authentication dropdown (see [Set Up the Connection](#set-up-the-connection)).

The Tableau Connector ZIP archive includes pre-filled templates for Keycloak, Okta, Azure AD and AuthO in the `OAuthConfigs-templates/` directory. You can use these templates to create your own custom configuration file.

> [!NOTE]
> The Tableau Connector (.taco) file includes a default Keycloak configuration (displayed as **Keycloak** in the authentication dropdown), but with an empty client ID. To use it, you must provide your own client ID.

#### [](#configure-the-xml-file)Configure the XML File

Open a template file in a text editor and update the attributes using the following rules:

> [!NOTE]
> If you do not follow these exactly, Tableau silently ignores the file and your configuration options do not appear in the connection dialog.

* **Set the plugin class**: Set `dbclass` to `enterprise-analytics`. This links the configuration to the correct connector and must match the exact plugin class of your taco.
* **Prefix the configuration ID**: The `oauthConfigId` attribute must start with `custom_`. For example, `custom_myidp`.
* **Format redirect URIs**: Use a separate `<redirectUrisDesktop>` element for each redirect URI. Do not combine multiple URIs in a single element.
* **Use absolute URLs**: Provide full, absolute URLs for the `authUri` and `tokenUri` elements. Tableau does not support OIDC discovery in override files.  
For information about these endpoints, see your IdP documentation.

The following is an example of a complete XML file for a custom IdP.

```xml
<?xml version="1.0" encoding="utf-8"?>
<pluginOAuthConfig>
    <dbclass>enterprise-analytics</dbclass>
    <oauthConfigId>custom_myidp</oauthConfigId>
    <configLabel>My IdP (my org)</configLabel>
    <clientIdDesktop>YOUR_CLIENT_ID</clientIdDesktop>
    <redirectUrisDesktop>http://localhost:55555/Callback</redirectUrisDesktop>
    <redirectUrisDesktop>http://localhost:55556/Callback</redirectUrisDesktop>
    <redirectUrisDesktop>http://localhost:55557/Callback</redirectUrisDesktop>
    <redirectUrisDesktop>http://localhost:55558/Callback</redirectUrisDesktop>
    <redirectUrisDesktop>http://localhost:55559/Callback</redirectUrisDesktop>
    <authUri>https://YOUR_IDP_HOST/oauth2/authorize</authUri>
    <tokenUri>https://YOUR_IDP_HOST/oauth2/token</tokenUri>
    <scopes>openid</scopes>
    <scopes>offline_access</scopes>
    <capabilities>
        <entry><key>OAUTH_CAP_REQUIRE_PKCE</key><value>true</value></entry>
        <entry><key>OAUTH_CAP_PKCE_REQUIRES_CODE_CHALLENGE_METHOD</key><value>true</value></entry>
        <entry><key>OAUTH_CAP_FIXED_PORT_IN_CALLBACK_URL</key><value>true</value></entry>
        <entry><key>OAUTH_CAP_SUPPORTS_GET_USERINFO_FROM_ID_TOKEN</key><value>true</value></entry>
    </capabilities>
    <accessTokenResponseMaps>
        <entry><key>ACCESSTOKEN</key><value>access_token</value></entry>
        <entry><key>REFRESHTOKEN</key><value>refresh_token</value></entry>
        <entry><key>access-token-expires-in</key><value>expires_in</value></entry>
        <entry><key>id-token</key><value>id_token</value></entry>
    </accessTokenResponseMaps>
    <refreshTokenResponseMaps>
        <entry><key>ACCESSTOKEN</key><value>access_token</value></entry>
        <entry><key>REFRESHTOKEN</key><value>refresh_token</value></entry>
        <entry><key>access-token-expires-in</key><value>expires_in</value></entry>
        <entry><key>id-token</key><value>id_token</value></entry>
    </refreshTokenResponseMaps>
</pluginOAuthConfig>
```

For more information about the XML, see [Tableau OAuth Configuration and Usage](https://tableau.github.io/connector-plugin-sdk/docs/oauth).

#### [](#save-the-xml-file)Save the XML File

Name your XML file (for example, `enterprise-analytics-okta.xml`) and save it in one of the following locations.

* Windows: `%USERPROFILE%\Documents\My Tableau Repository\OAuthConfigs\`
* macOS: `~/Documents/My Tableau Repository/OAuthConfigs/`

After you save the XML file, restart Tableau. Tableau loads all `.xml` files from these directories on startup. When you open the connection dialog, your custom IdP configuration appears in the authentication dropdown.

## [](#connect-tableau-desktop-to-tableau-server)Connect Tableau Desktop to Tableau Server

You can publish reports and dashboards created on Tableau Desktop to Tableau Server.

To configure your Tableau Server connection:

1. In Tableau Desktop, go to **Server** **Tableau Online**.
2. Sign in with your Tableau Server credentials.

After you sign in, the connection appears in the **Server** section.

> [!NOTE]
> If you're using an on-premise instance of Tableau Server, you need to configure SSL. You can do this by logging into the Tableau Services Manager UI and going to **Configuration** **Security** **External SSL**.

For more information about configuring SSL on your Tableau Server, see [Configuring SSL on Tableau Server](https://help.tableau.com/current/server/en-us/ssl%5Fconfig.htm#use-the-tsm-web-interface).