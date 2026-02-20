---
title: Authentication
description: To access Couchbase Server, users must be authenticated.
  <em>Authentication</em> is a process for identifying who is attempting to
  access a system.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/security/authentication.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:learn:security/authentication.adoc[]
---

[View original HTML](/server/7.2/learn/security/authentication.html)

# Authentication

To access Couchbase Server, users must be authenticated. _Authentication_ is a process for identifying who is attempting to access a system. Subsequent to successful authentication, _authorization_ can be performed, whereby the user’s appropriate access-level is determined.

Authentication can be performed by means of a _username_ and _password_, assigned to each administrator or application. Authentication can also be performed by means of _X.509 Certificates_: these support _Transport Layer Security_, by establishing the identity of a client or server through _digital signatures_. They also provide keys to support _on-the-wire_ encryption, according to the conventions of _Public Key Infrastructure_ (PKI).

Couchbase Server assigns each user to one of two _authentication domains_: the _local_ domain consisting of users whose credentials are maintained by Couchbase Server itself; the _external_ domain consisting of users whose credentials are maintained remotely — for example, on an _LDAP_ server.

For detailed information on these topics, see:

* [Understanding Authentication](authentication-overview.md), which provides an overview of all the key aspects of Couchbase authentication.
* [Usernames and Passwords](usernames-and-passwords.md), which lists the conventions whereby usernames and passwords can be designed and passed by administrators and applications.
* [Authentication Domains](authentication-domains.md), which contains full explanations of the _local_ and _external_ authentication domains supported by Couchbase Server.
* [Certificates](certificates.md), which provides a detailed overview of how certificates are supported by Couchbase Server, for the authentication of clusters, nodes, and client applications.