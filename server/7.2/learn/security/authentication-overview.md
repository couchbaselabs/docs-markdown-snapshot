---
title: Understanding Authentication
description: To access Couchbase Server, users must be authenticated.
  <em>Authentication</em> is a process for identifying who is attempting to
  access a system.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/security/authentication-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/learn/security/authentication-overview.html)

# Understanding Authentication

> To access Couchbase Server, users must be authenticated. _Authentication_ is a process for identifying who is attempting to access a system. Subsequent to successful authentication, _authorization_ can be performed, whereby the user’s appropriate access-level is determined. 

## [](#passing-credentials)Authentication Options

Couchbase-Server authentication typically relies on a _username_ and a _password_, which must be passed into the system by the _user_ (meaning, the administrator or application) that is attempting access. The specified username and password must match ones already defined: these must be accessible either on the Couchbase-Server cluster itself, or _externally_. External accessibility, which is available only with the Enterprise Edition of Couchbase Server, means either:

* On a network-accessible directory-server, by means of the _Lightweight Directory Access Protocol_ (LDAP).
* By means of the _Pluggable Authentication Modules_ (PAM) authentication-framework.

If a match is achieved, the user is thereby recognized, and so _may_ be granted access. If no match is achieved, the user is denied access.

Client applications or systems can also pass credentials to Couchbase Server by means of x.509 _certificates_.

## [](#introduction-to-password-based-authentication)Users, Usernames, and Passwords

To access Couchbase Server, all users and applications must authenticate. This is typically achieved by means of a _username_ and _password_.

The _Full Administrator_ username and password are established during initialization of Couchbase Server: see [Create a Cluster](../../manage/manage-nodes/create-cluster.md) for details.

Subsequently, additional users can be added to the cluster as _local_ users: each is at that time assigned a unique _username_, and a unique _password_. Passwords can be changed by means of the password-reset tool, [reset-admin-password](../../cli/cbcli/couchbase-cli-reset-admin-password.md); or by Couchbase Web Console, as described in [Editing Users and Groups](../../manage/manage-security/manage-users-and-roles.md#editing-users-and-groups). For best practices for password-definition, and restrictions on username-design, see [Usernames and Passwords](usernames-and-passwords.md).

Users can also be added to the cluster as _external_ users, for whom no password need be specified; since the external user is to be authenticated externally.

### [](#console-access)Usernames and Passwords for Administrators

When an administrator logs into Couchbase Web Console, if the console is running on the default port, `http://localhost:8091`, the specified username and password are passed in the clear, from the browser to the console.

Optionally, Couchbase Web Console can be configured for _secure access_, at `https://localhost:18091`; so that the username and password are passed in encrypted form. For information, see [Manage Console Access](../../manage/manage-security/manage-console-access.md).

### [](#authentication-for-applications)Usernames and Passwords for Applications

To pass credentials, applications must use one of four mechanisms provided by the _Simple Authentication and Security Layer_ (SASL) framework. These are PLAIN, and three members of the _Salted Challenge Response Authentication Mechanism_ family of hash functions; which are SCRAM-SHA1, SCRAM-SHA256, and SCRAM-SHA512\. The SCRAM mechanisms allow applications to authenticate securely, by transmitting the password only in _protected form_. Drivers may need to be updated, to support SHA-based hash functions.

In ascending order of strength, the Couchbase password-authentication mechanisms are as follows:

* _PLAIN_: The client sends the password in unencrypted form. All clients support this authentication-method. It is insecure, providing no defence against passwords being stolen in transmission.
* _SCRAM-SHA1_: Uses a 160-bit key.
* _SCRAM-SHA256_: One of a group of hash functions referred to as _SHA2_, SCRAM-SHA256 uses a 256-bit key.
* _SCRAM-SHA512_: Another hash function from the _SHA2_ group, SCRAM-SHA512 uses a 512-bit key; and is the strongest supported authentication protocol.

During initial client-server negotiation, the strongest authentication protocol supported by both Couchbase Server and the application’s client OS is selected for use. For example, if the client supports only the PLAIN protocol, the PLAIN protocol is used; but if the client also supports the SCRAM-SHA1 protocol, then SCRAM-SHA1 is used.

A challenge-response method can be transmitted through both encrypted and unencrypted channels.

Note that the SCRAM challenge-response protocols authenticate only the process of password-validation. To secure the subsequent session, TLS should be used.

## [](#introduction-to-certificate-based-authentication)Certificate-Based Authentication

Couchbase Server supports the use of x.509 certificates, to authenticate clients. This ensures that only approved users, machines, or endpoints are authenticated.

Certificate-based authentication relies on a _Certificate Authority_ (CA) to validate identities and issue certificates. The certificate includes information such as the name of the entity it identifies, an expiration date, the name of the CA that issued the certificate, and the digital signature of the issuing CA.

For a complete overview of Couchbase Server’s certificate-handling mechanisms, see [Certificates](certificates.md). For practical steps required to set up client and server certificates, see [Manage Certificates](../../manage/manage-security/manage-certificates.md)

## [](#authorization)Authorization

Couchbase-Server features — including data, settings, and statistics — can be accessed only by users who have been assigned the appropriate _privileges_. Privileges include _read_, _read-write_, _execute_, and _manage_. Privileges are assigned by _Full_ and _Security_ Administrators, in correspondence with _roles_. When a user successfully authenticates, their assigned roles are examined, and access is granted or denied by Couchbase Server.

Roles can be assigned to a user in either or both of two ways:

* _Directly_. The user is associated directly with one or more Couchbase-Server roles.
* _By Group_. A Couchbase-Server _user-group_ is defined, and roles are assigned to the user-group. The user is made a member of the user-group, and thereby inherits all the roles of the group. A user can be a member of any number of groups.

Note that by means of _LDAP Group Support_, the roles assigned to a Couchbase-Server user-group can be inherited by users not defined on Couchbase Server; as described in [Authentication Domains](authentication-domains.md).

See [Manage Users, Groups, and Roles](../../manage/manage-security/manage-users-and-roles.md), for details on creating users and groups, and assigning roles.

## [](#authentication-domains)Authentication Domains

Couchbase Server assigns each user to one of two _authentication domains_; which are _local_ and _external_. The _local_ domain contains users defined locally, on Couchbase Server. The _external_ domain contains users defined externally, either on an LDAP server, or on Linux systems that are accessed by means of _PAM_. For a complete overview, see [Authentication Domains](authentication-domains.md).