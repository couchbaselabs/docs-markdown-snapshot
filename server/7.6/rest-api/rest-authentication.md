[View original HTML](/server/7.6/rest-api/rest-authentication.html)

> Couchbase Server supports authentication via local and external domains. 

## [](#authenticating-externally)Authenticating Locally and Externally

Couchbase users may be given an identity _locally_ on a cluster. This allows their credentials to be maintained and updated on the local cluster. A _password policy_ is enforced for the cluster: the defaults for this policy can be modified. A local user can change their own password.

Enterprises frequently centralize directory services, allowing all user-authentication to be handled by a single server or server-group. LDAP is frequently used in support of such centralization. The authentication handled in this way is therefore _external_ to Couchbase Server.

Couchbase Server supports external authentication. Users are registered as _external_, for authentication purposes. When such users pass their credentials to Couchbase Server, Couchbase Server recognizes the user as external, and duly passes the credentials to the external authentication facility: if the authentication succeeds there, Couchbase Server is informed, and the user is given appropriate access, based on the roles and privileges on Couchbase Server that they have been assigned.

The default password policy is described in [Password Strength](../learn/security/usernames-and-passwords.md#password-strength). For further information on _local_ and _external_ domains, see [Authentication Domains](../learn/security/authentication-domains.md).

### [](#ldap-groups)LDAP Groups

LDAP supports _groups_, of which multiple users can be members. Couchbase Server supports the association of LDAP groups with Couchbase-Server groups: a user successfully authenticated on an LDAP server may have their LDAP group information duly returned to Couchbase Server. If Couchbase Server has configured an association between one or more of the user’s LDAP groups and corresponding groups defined on Couchbase Server, the user is assigned the roles and privileges for the corresponding Couchbase-Server groups.

## [](#external-authentication-configuration-options)Configuration Options

Couchbase provides a recommended REST method for simple and expedited configuration of LDAP-based authentication. This is described in [Configure LDAP](rest-configure-ldap.md).

Alternatively, a [legacy](rest-configure-saslauthd.md) REST API for establishing SASL administrator credentials can be used. Note that this requires prior, manual set-up of saslauthd for the cluster: see [Configure saslauthd](../manage/manage-security/configure-saslauthd.md).

## [](#apis-in-this-section)APIs in this section

A complete list of APIs described in this section is provided in the table below.

### [](#authentication)Authentication

| HTTP Method | URI                                                         | Documented at                                                         |
| ----------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| GET         | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#get-settingsldap)             |
| POST        | /settings/ldap                                              | [Configure LDAP](rest-configure-ldap.md#post-settingsldap)            |
| GET         | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#get-settingssaml)             |
| POST        | /settings/saml                                              | [Configure SAML](rest-configure-saml.md#post-settingssaml)            |
| GET         | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| POST        | /settings/saslauthdAuth                                     | [Configure saslauthd](rest-configure-saslauthd.md)                    |
| GET         | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /settings/passwordPolicy                                    | [Set Password Policy](rest-set-password-policy.md)                    |
| POST        | /controller/changePassword                                  | [Change Password](rest-set-password.md)                               |
| POST        | /node/controller/loadTrustedCAs                             | [Load Root Certificates](load-trusted-cas.md)                         |
| GET         | /node/controller/loadTrustedCAs                             | [Get Root Certificates](get-trusted-cas.md)                           |
| DELETE      | /pools/default/trustedCAs/<id>                              | [Delete Root Certificates](delete-trusted-cas.md)                     |
| GET         | /pools/default/certificates                                 | [Retrieve All Node Certificates](retrieve-all-node-certs.md)          |
| POST        | /node/controller/reloadCertificate                          | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| GET         | /pools/default/certificate/node/<ip-address-or-domain-name> | [Upload and Retrieve Node Certificates](upload-retrieve-node-cert.md) |
| POST        | /controller/regenerateCertificate                           | [Regenerate All Certificates](rest-regenerate-all-certs.md)           |