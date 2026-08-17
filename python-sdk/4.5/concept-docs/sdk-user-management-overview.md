---
title: User Management
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/concept-docs/pages/sdk-user-management-overview.adoc
  xref: xref:4.5@python-sdk:concept-docs:sdk-user-management-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.5/concept-docs/sdk-user-management-overview.html)

# User Management

> The SDK lets you programmatically create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

This is an overview of the user management API's capabilities.

## [](#creating-a-user)Creating a User

The syntax required for creating a user varies according to language, and is covered for each SDK in the management documentation. The basic form is as follows:

boolean upsertUser (String userid, UserSettings settings)

The method **upsertUser** creates a user and adds the user to the Couchbase Cluster. The user will subsequently be visible in the **Security** panel of the Couchbase Web Console. Note that successful user-addition results in a user _locally_ defined, with _username_ and _password_ stored on Couchbase Server: _external_ users (whose credentials reside on a network-available server, possibly accessed by means of LDAP) should not be created by this SDK method. If the local user created by **upsertUser** already exists, the previous definition is overwritten.

The method takes two arguments. The first, a _String_ is the user ID of the user to be created: for example, `johnsmith0325`, or `user734`. This must be specified.

The second is a _UserSettings_ object. This takes the following form:

UserSettings {
    String password;
    String name;
    Role[] roles;
}

The object contains three data-members. The first is a _String_ that specifies the user's password: this must be provided. The second is a _String_ that specifies the user's name (for example, `John Smith`): this is optional, and so may be omitted. The third is an array of _Role_ objects: this must be specified. Each _Role_ object takes the following form:

Role {
    String role;
    String bucket_name;
}

The object's two data-members are both _Strings_, and must both be specified. The _String_ specified as the role must correspond to a role supported by Couchbase Server. The _String_ specified as the bucket\_name must either correspond to a bucket currently defined on Couchbase Server; or be the asterisk character (_\*_), meaning _all buckets_.

The method returns a _boolean_, which is `true` if the operation is successful, otherwise `false`.

## [](#listing%5Fusers)Listing Users

The basic form of the method used to return currently defined users is as follows:

List<User> getUsers()

The method returns a list of _User_ objects, each of which takes the following form:

User {
    String name;
    String id;
    String domain;
    Role[] roles;
}

The name is the full name of the user. The id is the user's ID. The domain is either `local` or `external`. Each Role object in the Role-array has the form already described above, in _Creating a User_.

## [](#getting-a-user)Getting a User

The basic form of the method used to return an already defined user is as follows:

User getUser (String userid)

The method returns a _User_ object, which takes the following form:

User {
    String name;
    String id;
    String domain;
    Role[] roles;
}

The name is the full name of the user. The id is the user's ID. The domain is either `local` or `external`. Each Role object in the Role-array has the form described above, in _Creating a User_.

## [](#removing-a-user)Removing a User

The basic form of the method used to remove users is as follows:

boolean removeUser (String userid)

The method's sole argument is the id of the user to be removed from the system, specified as a _String_. The method returns a _boolean_, whose value is `true` if the operation is successful, otherwise `false`.