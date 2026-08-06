---
title: Managing Couchbase Clusters from the SDK
description: Cluster management from the SDK.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/concept-docs/pages/management-api.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.11@java-sdk:concept-docs:management-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.11/concept-docs/management-api.html)

# Managing Couchbase Clusters from the SDK

> Cluster management from the SDK. 

The Couchbase Java SDK has a management API to provision clusters. This is not the only programmatic way to deploy Couchbase, and you may wish to look at [Terraform](../../../cloud/terraform/index.md) for Capella, or some of our command line tools.

## [](#buckets-and-clusters)Buckets and Clusters

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

Management operations in the Java SDK may be performed through several interfaces depending on the object:

### [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `buckets()` call on the cluster:

```java
Cluster cluster = Cluster.connect("127.0.0.1", "user", "123456");
BucketManager manager = cluster.buckets();
manager.createBucket(bucketSettings);
```

This class is also used to expose information about an existing bucket (`manager.getBucket(string)`) or to update an existing bucket (`manager.updateBucket(bucketSettings)`).

The default Collection & Default Scope will be used automatically.

## [](#user-management)User Management

The SDK lets you programmatically create _users_, assign them _roles_ and associated _privileges_, and remove them from the system.

This is an overview of the user management API's capabilities. For a practical look at using it, see [Sample Code](../howtos/sdk-user-management-example.md).

### [](#creating-a-user)Creating a User

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

### [](#listing%5Fusers)Listing Users

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

### [](#getting-a-user)Getting a User

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

### [](#removing-a-user)Removing a User

The basic form of the method used to remove users is as follows:

boolean removeUser (String userid)

The method's sole argument is the id of the user to be removed from the system, specified as a _String_. The method returns a _boolean_, whose value is `true` if the operation is successful, otherwise `false`.