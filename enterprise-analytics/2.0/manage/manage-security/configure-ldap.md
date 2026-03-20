---
title: Configure LDAP
description: Enterprise Analytics can be configured to authenticate users by
  means of LDAP; and to map the LDAP <em>groups</em> of which a user is a member
  to roles defined on Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-security/configure-ldap.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:manage:manage-security/configure-ldap.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-security/configure-ldap.html)

# Configure LDAP

> Enterprise Analytics can be configured to authenticate users by means of LDAP; and to map the LDAP _groups_ of which a user is a member to roles defined on Enterprise Analytics. 

## [](#understanding-ldap-authentication)Understanding LDAP Authentication and Authorization

For authentication purposes, Enterprise Analytics can be configured to use LDAP. This allows users, when they attempt to access Enterprise Analytics by presenting their credentials, to be authenticated by LDAP. Optionally, LDAP _group_ information for the authenticated user can be fetched from the LDAP server. If an LDAP group has been mapped to Couchbase-Server roles, the roles are thereby granted to the user.

> [!NOTE]
> LDAP authentication and authorization may be more appropriate for human users than for applications. For information, see [LDAP: Users and Applications](../../../../server/current/learn/security/authentication-domains.md#ldap-users-and-applications).

Enterprise Analytics provides two different ways of setting up LDAP:

* _Native LDAP Support_. For Enterprise Analytics Enterprise Edition 6.5+, this is the recommended way of setting up LDAP for external authentication. Enterprise Analytics provides support for encrypted communication, and LDAP groups with its Native LDAP Support.

This page provides examples of how to configure _Native LDAP Support_.

The Native LDAP Support require clients to use the PLAIN authentication mechanism, ideally with TLS.

## [](#examples-on-this-page-node-addition)Examples on This Page

The examples in the subsections below show how to configure Native LDAP Support; using the [UI](#configure-ldap-with-the-ui), the [CLI](#configure-ldap-with-the-cli), and the [REST API](#configure-ldap-with-the-rest-api) respectively. The examples assume:

* A one-node cluster already exists; and is named after its IP address: `10.143.192.101`. It is running the Data and Query Services, and has the `travel-sample` bucket installed. (To install this bucket, see [Sample Buckets](#manage:manage-settings/install-sample-buckets.adoc).)
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.
* Two fully configured LDAP servers are available, at `172.23.124.25` and `172.23.124.26`, each using port `389`.
* External authentication for the cluster has been enabled. This can be achieved by means of the Couchbase CLI command, `setting-ldap`, as follows:  
```bash  
/opt/enterprise-analytics/bin/couchbase-cli
-c 10.144.210.101 -u Administrator -p password \
--authentication-enabled 1  
```

Each subsection also shows how to map LDAP groups to Couchbase-Server roles, by means of Couchbase-Server user-groups.

Throughout this page, references are made to LDAP _Distinguished Names_, which must be specified as part of Native-LDAP configuration. For the full definition of Distinguished Names, see [RFC 4514 - Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names](https://tools.ietf.org/html/rfc4514).

## [](#configure-ldap-with-the-ui)Configure LDAP with the UI

To configure LDAP, access the **Security** panel, by means of the entry in the left-hand navigation bar.

This brings up the **Security** screen.

The **LDAP** tab allows an LDAP server to be specified for external authentication. The **ADD GROUP** tab allows definition of _Couchbase-Server user-groups_; which are to be associated with _LDAP groups_, and which can be assigned Couchbase-Server _roles_. The **ADD USER** tab allows individual users to be added, and allows their authentication optionally to be specified as **external**.

To perform LDAP configuration, left-click on the **LDAP** tab, at the upper right of the **Security** screen.

This brings up the **LDAP Configuration** dialog.

The dialog presents two main panels. The vertically scrollable right panel features help text, for **LDAP Host Configuration**, **User Authentication**, and **Group Authorization**. The left panel features options whereby LDAP can be configured.

The fields of the left panel are presented in three principal areas, each corresponding to a key aspect of LDAP configuration:

* _LDAP host configuration_. These fields occupy the upper part of the left panel. They can be used to establish which servers run LDAP, and how they are to be contacted.
* _User authentication enablement_. These fields can be accessed in the lower part of the left panel, by means of the **Enable LDAP user authentication** switch. They can be used to establish that users not recognized as _local_ to Enterprise Analytics will be authenticated by means of the specified _LDAP host configuration_, and to specify the procedures to be used.
* _Group authorization enablement_. These fields can be accessed from near the bottom of the left panel, by means of the **Enable LDAP group authorization & sync** switch. They can be used to establish that the LDAP group-membership of authenticated LDAP users will be checked, to determine whether mappings to Couchbase-Server user-groups exist, and to specify the procedures to be used.

Each of these areas is described below.

### [](#ldap-host-configuration)LDAP Host Configuration

The upper area of the left panel of the **LDAP Configuration** dialog displays the following fields:

* **LDAP Host(s)**. A comma-separated list of host-names, each of which is an LDAP server on which external authentication can occur. The first accessible server in the list is the one that is used. For example, if the list is `server1, server2`, provided that `server1` is accessible, it is used.
* **LDAP Port**. The port used on each of the LDAP servers for authentication.

* **Encryption**. Whether the connection with the LDAP server should be encrypted. Note that use of encryption is _strongly_ recommended.

Left-click on the control at the right-hand side of the **Encryption** field, to display the pull-down menu.

The options are **None** (to connect without encryption — this is insecure, and therefore is _not_ recommended), **TLS** (to connect to a TLS-encrypted port), and **StartTLSExtension** (to upgrade an existing connection).

* **Certificate**. Whether to provide Enterprise Analytics with a copy of the LDAP server’s root certificate, so as to allow Enterprise Analytics to validate the LDAP server when connecting. This set of radio-buttons is enabled only if **TLS** or **StartTLSExtension** has been selected from the [Encryption](#encryption-pulldown-menu) pull-down menu.  
The options are **None**, **Couchbase**, and **Paste Cert**. If **None** is selected, the LDAP server’s root certificate is _not_ provided to Enterprise Analytics: this option is insecure, and therefore _not_ recommended.  
If **Couchbase** is selected, the root certificate for the Couchbase-Server cluster is used to validate the LDAP server: this assumes that the same root certificate is installed for both Enterprise Analytics and the LDAP server.

**Paste Cert** should be selected if the LDAP server root certificate is _not_ the same certificate as has been installed for the Couchbase-Server cluster. When **Paste Cert** is selected, the panel expands vertically, to reveal the **LDAP Server Root Certificate** field.  
The text of the LDAP server root certificate should now be copied and pasted, in PEM format, into the **LDAP Server Root Certificate** field.
* **Contact LDAP host**. The following options are provided, to determine how Enterprise Analytics will contact the LDAP host.

  * **Anonymously**. Checking this checkbox causes Enterprise Analytics to attempt to contact the LDAP host anonymously. However, the attempt succeeds only if supported by the LDAP server.
  * **Credentials**. Checking this checkbox allows credentials to be specified by the user, and submitted to the LDAP host for authentication. The UI expands, to display two additional fields.

**Bind DN** requires the LDAP _Distinguished Name_ of the user who will perform user-search and groups synchronization. This user needs to have _read only_ access to the LDAP server, in order to be able to search for users and groups.

**Password** requires input of the user’s password, as stored on the LDAP server.  
  With data entered into these fields, a dialog might appear.
  * **Client Certificate**. This option, which allows allows Enterprise Analytics to authenticate with LDAP by means of a client certificate, should be used only with an LDAP server that _does not_ expect the `SASL EXTERNAL` bind command to be sent, once a TLS connection has been established. Note, therefore, that this option _can_ be used with the _GSuite_ LDAP server.  
  This option is only enabled if either **TLS** or **StartTLSExtension** has been selected from the [Encryption](#encryption-pulldown-menu) pull-down menu.  
  When the **Client Certificate** option is selected, the UI expands.

The client certificate of Enterprise Analytics should be pasted into the **Client Certificate** panel. The _private key_ corresponding to the client certificate should be pasted into the **Client Key** panel. These files can be selected by means of the **Select File** buttons, which bring up a file-selection interface.

Once all appropriate settings have been made to **LDAP Host(s)**, **Encryption**, **Certificate**, and **Contact LDAP host** fields, optionally, the **Check Network Settings** button can be left-clicked on. This tests whether a specified LDAP host can be accessed by the specified means. If no such access is possible, an error is displayed on the dialog.

### [](#enable-ldap-user-authentication)User Authentication Enablement

When you turn on the **Enable LDAP user authentication** toggle, several fields appear that let you enable LDAP authentication.

When enabled, Enterprise Analytics authenticates users who are not _local_ users with the configured **LDAP Hosts**.

You have three options for how Enterprise Analytics maps the username in an authentication attempt to an LDAP _Distinguished Names_ ([DN](https://ldap.com/ldap-dns-and-rdns/)). These options are explained in the following sections.

#### [](#template)Template

The default option is **Template**. Enter a username-to-DN mapping template string into the **Template** text field. Directly providing the mapping avoids requiring the LDAP server itself provide the mapping itself. The field shows the format for the template string as placeholder text.

The username supplied to Enterprise Analytics by the user who’s attempting to authenticate replaces the `%u` in the template. For example, if the template is `cn=%u,dc=example,dc=com` and the user logs in as `exampleUser`, the template maps the user to the DN `cn=exampleUser,dc=example,dc=com`.

#### [](#ldap-query-user)LDAP Search

Select **LDAP Search**.

You use the three fields to define an LDAP [search operation](https://ldap.com/the-ldap-search-operation/) to get the user’s DN from LDAP server.

* **Base** is the _search base_ DN.
* **Filter** is the [search filter](https://ldap.com/ldap-filters/). For example, if **Base** is specified as `ou=users,dc=example,dc=com`, **Filter** as `(uid=%u)`, and the user has provided `exampleUser` to Enterprise Analytics as their username, Enterprise Analytics performs the following search, in order to obtain the user’s DN: `ou=users,dc=example,dc=com??one?(uid=exampleUser)`.
* **Scope** list sets the scope for the search. See [LDAP Search Scopes](https://ldapwiki.com/wiki/Wiki.jsp?page=LDAP%20Search%20Scopes) for a description of LDAP search scopes.

For further information about **Base**, **Filter**, and **Scope**, see [The LDAP Search Operation](https://ldap.com/the-ldap-search-operation/).

#### [](#ldap-advanced-mapping)Advanced Query

The **Advanced Query** option lets you supply a list of regular expressions that Enterprise Analytics tests against the username. For each regular expression you also supply a replacement string that Enterprise Analytics uses to insert portions of the username into a DN or LDAP query. When you select the **Advanced Query** option, a **Template** text edit box appears for you to enter your list.

You enter your regular expressions and replacement strings as a JSON list. The list contains objects, each of which must have a `match` key containing the regular expression. The object must also contain either a `substitution` key that defines a DN string or a `ldapQuery` key that defines an LDAP query. In either case, these strings should contain back references to capture expressions in the regular expression to extract parts of the username.

For example, the following template has two regular expressions. The first attempts to extract the address and domain name from an email address. If this regular expression matches, Enterprise Analytics uses the address as the user ID and the domain name as the organization unit in a DN. The second regular expression captures the entire username and passes that as an LDAP query in the `people` organizational unit.

```json
[
{
    "match": "([^@]+)@(.+)\\.com",
    "substitution": "cn={0},ou={1},dc=example,dc=com"
},
{
    "match": "(.*)",
    "ldapQuery": "ou=people,dc=example,dc=com??one?(uid={0})"
}
]
```

> [!TIP]
> Always double any backslashes (\\) that you use to escape special characters in your regular expressions because JSON also interprets backslash escapes.

Enterprise Analytics attempts to match the regular expressions against the username supplied by the user who’s attempting to authenticate. If a regular expression matches the username, Enterprise Analytics applies any captured portions of the regular expression to the back references in the replacement string. Then it attempts to authenticate the user with LDAP using the DN or LDAP query.

If the authentication fails, Enterprise Analytics returns an authentication error. It does not attempt match any further regular expressions in the list. This behavior makes the order of the regular expressions in the list important. Always place more specific regular expressions before general ones. In the previous example, the regular expression to matching an email address comes before the general catch all regular expression that matches any username.

The **Save LDAP Configuration** button has no effect if your template contains invalid JSON or an invalid regular expression. Errors in the replacement strings only appear when you try to authenticate a user. Use the **Test User Authentication** section to verify that your regular expressions and replacement strings work the way you intend.

#### [](#testing-user-authentication)Testing User Authentication

**Test User Authentication**, when opened, provides options for testing the authentication of specific users.

Enter the username and password for the user, and left-click **Test User Authentication**. Enterprise Analytics maps the specified username to an LDAP DN, and performs authentication on the LDAP server. Notifications confirming success or failure duly appear on the dialog.

### [](#group-authorization-enablement)Group Authorization Enablement

In the area immediately below that used for _User Authentication Enablement_, fields for enabling _LDAP Group Support_ can be made visible by means of the **Enable LDAP group authorization & sync** switch. Enablement means that when a user has been authenticated by the **LDAP Hosts(s)**, Enterprise Analytics retrieves the _LDAP group membership_ information for that user, in order to authorize them. In each case where an LDAP group has been _mapped_ to a Couchbase-Server user-group, the user is granted the privileges corresponding to the roles assigned that user-group.

Switch on, to enable. This expands the dialog vertically.

The LDAP groups of which a user is a member can be searched for by means of either the **User’s attributes** or an **LDAP Search**, each of which is provided as a radio-button option. Selection of either reveals a corresponding set of fields, in which information can be added. These are as follows.

#### [](#users-attributes)User’s Attributes

The **User’s attributes** radio-button is selected by default. This instructs Enterprise Analytics to assume that each LDAP user-record contains an attribute featuring the list of groups of which the user is a member. Enterprise Analytics therefore performs the following LDAP search: `<userDN>?<attribute>?one`.

The value of the specified `attribute` is treated as a list of groups. For example, if `attribute` is set in the **User Attribute** field to `memberOf`, Enterprise Analytics performs the following search for the specified user’s groups: `uid=exampleUser,dc=example,dc=com?memberOf?one`.

#### [](#traverse-nested-groups-for-user-attributes)Traverse Nested Groups, for User Attribute Search

The **Traverse nested groups** checkbox, when checked, allows nested groups to be traversed by the search. Enterprise Analytics uses the same search to find groups of groups recursively (with each group’s DN being substituted for `%D`). If nested search is selected, `%u` cannot be used.

Note that use of nested groups may significantly increase load on the LDAP server; and should therefore only be used if essential.

#### [](#test-groups-query-for-user-attributes)Test Groups Query, for User Attribute Search

**Test Groups Query** permits a query to be tested for a specific user.

To perform the search, add a username, and left-click on the **Test Groups Query** button. Notifications confirming success or failure appear on the dialog.

#### [](#ldap-query-group)LDAP Search

When the **LDAP Search** radio-button is selected, the **Query for Groups Using** panel appears.

Selection of **LDAP Search** instructs Enterprise Analytics to perform an LDAP [search operation](https://ldap.com/the-ldap-search-operation/), in order to retrieve a list of the user’s groups. **Base** is the _search base_ DN. **Filter** is the [search filter](https://ldap.com/ldap-filters/). **Scope**, accessed from a pulldown menu, can be **base**, **one** (the default), or **sub**.

When the search is conducted, `%u` is replaced with the specified username; and `%D` is replaced with the user’s DN. For example, **Base** might be specified as `ou=groups,dc=example,dc=com`, **Filter** as `(member=%D)`, and **Scope** as `one-level`.

For further information about **Base**, **Filter**, and **Scope**, see [The LDAP Search Operation](https://ldap.com/the-ldap-search-operation/).

#### [](#traverse-nested-groups-for-ldap-query)Traverse Nested Groups, LDAP Search

See the description provided above, in [Traverse Nested Groups, for User Attribute Search](#traverse-nested-groups-for-user-attributes)

#### [](#test-groups-query-for-ldap-query)Test Groups Query, for LDAP Search

See the description provided above, in [Test Groups Query, for User Attribute Search](#test-groups-query-for-user-attributes)

### [](#advanced-settings)Advanced Settings

It is strongly recommended that the **Advanced Settings** _not_ be changed; except in unusual circumstances, and in accordance with expert advice. Inappropriate settings may seriously impair system responsiveness.

The advanced settings are as follows:

* **Request timeout ms**. The number of milliseconds to elapse before a query times out. The default is 5000.
* **Max Parallel Connections**. The maximum number of parallel connections to the LDAP server that can be maintained. The default is 100.
* **Max Cache Records**. The maximum number of requests that can be cached. The default is 10000.
* **Cache Time-to-Live ms**. The lifetime of values in cache, in milliseconds. The default is 300000.
* **Group Max Nesting Depth**. The maximum number of recursive group-queries that the server is allowed to perform. This option is only valid when nested groups are enabled. The value must be an integer between 1 and 100: the default is 10.
* **TLS Middlebox Compatibility**. Controls a low-level network compatibility setting affecting how Enterprise Analytics securely connects to an LDAP server through an intermediate system such as a proxy or firewall. This setting defaults to on. If you have difficulty getting Enterprise Analytics to connect to an LDAP server through an intermediate system, try toggling this setting.

When all required data has been entered, left-click on the **Save LDAP Configuration** button, at the bottom right.

Alternatively, left-click on **Cancel** to abandon the configuration procedure.

### [](#clearing-the-cache)Clearing the Cache

The **Clear Cache** button is located at the lower left of the **LDAP Configuration** dialog.

Enterprise Analytics _caches_ authentication responses and group-search results, thereby minimizing the number of requests to be made on the LDAP server. Each cached value is expired after a configured time-period (controlled by the **Cache Time-to-Live ms** value, provided in the [Advanced Settings](#advanced-settings) panel). Additionally, the **Clear Cache** button is provided, so that all currently cached values can be explicitly removed: each subsequent authentication or group request is, on its first instance following the removal, passed to the LDAP server; and the latest values established on the LDAP server are thereby retrieved.

### [](#map-ldap-groups-to-couchbase-server-roles)Map LDAP Groups to Couchbase-Server Roles

To map an LDAP group to Couchbase-Server roles, create a Couchbase-Server user-group; associate the user-group with the LDAP group; and then assign roles to the user-group.

(Note that each Couchbase-Server user-group can be associated with at most _one_ LDAP group — although if that LDAP group itself incorporates multiple additional LDAP groups by means of _LDAP-group nesting_, an _indirect_ association with those LDAP groups occurs.)

Left-click on the **ADD GROUP** tab, at the upper right of the **Users & Groups** panel, on the **Security** screen.

This brings up the **Add New Group** dialog.

The fields are as follows:

* **Group Name**. The name of the new Couchbase-Server group to be created.
* **Description**. An optional description of the new Couchbase-Server group.
* **Map to LDAP Group**. Optionally, the name of the existing LDAP group to which the new Couchbase-Server group is to be mapped. After a user has authenticated by means of LDAP, provided that LDAP group authorization has been enabled (by means of the **Enable LDAP group authorization & sync** control, described [above](#enable-ldap-group-authorization)), a list of the LDAP groups to which the user is assigned on that server is returned to Enterprise Analytics: if this list contains the LDAP group specified here, the user inherits the roles associated with the Couchbase-Server group here defined.
* **Roles**. The roles to be associated with the new Couchbase-Server group. For information, see [Authorization](../../../../server/current/learn/security/authorization-overview.md).

With appropriate data added, a dialog might appear.

This creates a group named `Admins`, and assigns the `Full Admin` role to it, specifying as its LDAP-group mapping `uid=cbadmins,ou=groups,dc=example,dc=com`.

To save the group, left-click on the **Save** button, at the lower right.

Alternatively, left-click on **Cancel** to abandon group configuration.

### [](#editing-a-group-mapping)Editing a Group Mapping

Once a group-mapping has been defined, it can be edited.

1. Access the **Users & Groups** panel of the **Security** screen. By default, this presents a _users_ view, listing the currently defined users for the cluster. To display the _groups_ view, left-click on the **Groups** tab, towards the upper right.
2. This brings up the _groups_ view, which shows currently defined user-groups for the cluster.
3. This confirms the existence of the user-group `Admins`.
4. Now, left-click on the row displayed for this group.  
The row expands vertically, and exposes additional controls.
5. Left-click on the **Edit** button, at the lower right. This brings up the **Edit Group Admins** dialog.  
Within this dialog, the description, mapping, or roles for the group can be edited. For details of selecting roles within the **Roles** panel, see [Manage Users, Groups, and Roles](manage-users-and-roles.md).

> [!NOTE]
> If the **Delete Group** button is left-clicked on, the group is deleted. This means that all mappings between LDAP groups and the roles that were assigned to this group are also deleted.

### [](#adding-an-externally-authenticated-user)Adding an Externally Authenticated User

Couchbase-Server users can be specified as _externally authenticated_, when they are added to the system. This allows roles to be assigned to them on the cluster; either directly, or by means of group-membership, or both. Additionally, if one or more LDAP group-mappings have been defined for LDAP groups of which the externally authenticated user is a member, the user is recognized as a member of the Couchbase-Server user-groups to which the mappings have been made, and is thereby assigned still more roles.

Step-by-step instructions on adding externally authenticated users are provided in [Adding an Externally Authenticated User](manage-users-and-roles.md#adding-an-externally-authenticated-user).

## [](#configure-ldap-with-the-cli)Configure LDAP with the CLI

To configure an LDAP server to be used as a point of authentication for Enterprise Analytics, use the [setting-ldap](../../cli/couchbase-cli-setting-ldap.md) command.

/opt/enterprise-analytics/bin/couchbase-cli
--cluster http://10.143.192.101 \
--username Administrator \
--password password \
--hosts 172.23.124.25 --port 389 \
--encryption startTLS \
--ldap-cacert '/path/to/cert' \
--bind-dn 'cn=admin,dc=example,dc=com' \
--bind-password 'password' \
--authentication-enabled 1 \
--user-dn-template 'uid=%u,ou=users,dc=example,dc=com' \
--authorization-enabled 1 \
--group-query 'ou=groups,dc=example,dc=com??one?(member=%D)'

This call references the LDAP server at `172.23.125.25`, on port `389`, and specifies `--authorization-enabled` and `--authentication-enabled` for the user-credentials that will be passed from Enterprise Analytics. The argument specified for `--group-query` is the query that retrieves the LDAP groups of which the user is a member. A `--user-dn-template` is specified as a distinguished name template.

If successful, the call produces the following output:

SUCCESS: LDAP settings modified

For more information, see the command reference for [setting-ldap](../../cli/couchbase-cli-setting-ldap.md).

### [](#map-groups-with-the-cli)Map Groups with the CLI

The [user-manage](../../cli/couchbase-cli-user-manage.md) command allows users and groups to be created and deleted, and roles to be assigned.

For example, a Couchbase-Server user-group can be defined as follows:

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password \
--set-group \
--group-name admins \
--roles admin \
--group-description "Enterprise Analytics Administrators" \
--ldap-ref 'uid=cbadmins,ou=groups,dc=example,dc=com'

This establishes a Couchbase-Server group named `admins`, each of whose members is granted the `admin` (the `Full Administrator`) role. It references the LDAP group `uid=cbadmins,ou=groups,dc=example,dc=com`: from this point, LDAP-authenticated users who are in the LDAP group `uid=cbadmins,ou=groups,dc=example,dc=com` are placed in the Couchbase-Server `admins` group, and thereby are granted the `admin` role.

For examples of using the `user-manage` command to create LDAP-authenticated users, and optionally assign them to groups, see [Manage External Users](manage-users-and-roles.md#manage-external-users).

## [](#configure-ldap-with-the-rest-api)Configure LDAP with the REST API

To configure an LDAP server to be used as a source of authentication for Enterprise Analytics, use the `/settings/ldap` endpoint, as follows:

curl -v -X POST -u Administrator:password \
http://10.143.192.101:8091/settings/ldap \
-d hosts=172.23.124.25 \
-d port=389 \
-d encryption=StartTLSExtension \
-d serverCertValidation=true \
--data-urlencode cacert@/path/to/cert \
-d bindDN='cn=admin,dc=example,dc=com' \
-d bindPass=password \
-d authenticationEnabled=true \
--data-urlencode userDNMapping='{"template":"uid=%u,ou=users,dc=example,dc=com"}' \
-d authorizationEnabled=true \
--data-urlencode groupsQuery='ou=groups,dc=example,dc=com??one?(member=%D)'

This call references the LDAP server at `172.23.125.25`, on port `389`, enabling authorization and authentication for user-credentials to be passed from Enterprise Analytics.

For more information, see [Configure LDAP](../../reference/rest-configure-ldap.md).

### [](#map-groups-with-the-rest-api)Map Groups with the REST API

Use the `PUT /settings/rbac/groups/<group-name>` method and URI, as follows:

curl -v -X PUT -u Administrator:password \
http://10.143.192.101:8091/settings/rbac/groups/admins \
-d roles=admin \
-d description=Couchbase+Server+Administrators \
--data-urlencode ldap_group_ref='uid=cbadmins,ou=groups,dc=example,dc=com'

This establishes an Enterprise Analytics group named `admins`, each of whose members is granted the `admin` (the `Full Administrator`) role. It maps the `admins` group to the LDAP group `uid=cbadmins,ou=groups,dc=example,dc=com`: from this point, LDAP-authenticated external users who are in the LDAP `uid=cbadmins,ou=groups,dc=example,dc=com` group are placed in the Enterprise Analytics `admins` group, and thereby are granted the `admin` role.

For more information about using the REST API to manage roles, see [Role Based Admin Control (RBAC)](../../reference/rbac.md).