---
title: User Management
description: The Java SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.6/modules/howtos/pages/sdk-user-management-example.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.6@java-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.6/howtos/sdk-user-management-example.html)

# User Management

> The Java SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Java SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/user/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```java
User user = new User(testUsername).password(testPassword).displayName("Constance Lambert");
user.roles(
    // Roles required for the reading of data from the bucket
    new Role("data_reader", "*"),
    new Role("query_select", "*"),
    // Roles required for the writing of data into the bucket.
    new Role("data_writer", bucketName),
    new Role("query_insert", bucketName),
    new Role("query_delete", bucketName),
    // Role required for the creation of indexes on the bucket.
    new Role("query_manage_index", bucketName));

cluster.users().upsertUser(user);
```

Listing Users

```java
List<UserAndMetadata> listOfUsers = cluster.users().getAllUsers();
for (int j = 0; j < listOfUsers.size(); j++) {
  UserAndMetadata currentUser = listOfUsers.get(j);
  System.out.println("User's display name is: " + currentUser.user().displayName() );
  Set<Role> currentRoles = currentUser.user().roles();
  for (Role role : currentRoles) {
    System.out.println("   User has the role: " + role.name() + ", applicable to bucket " + role.bucket() );
  }
}
```

Using a user created in the SDK to access data:

```java
ClusterEnvironment environment = ClusterEnvironment.builder().build();
Cluster userCluster = Cluster.connect(connectionString,
    ClusterOptions.clusterOptions(testUsername, testPassword).environment(environment));
Bucket userBucket = userCluster.bucket(bucketName);
Scope scope = userBucket.scope("inventory");
Collection collection = scope.collection("airline");

cluster.queryIndexes().createPrimaryIndex(bucketName, // create index if needed
    CreatePrimaryQueryIndexOptions.createPrimaryQueryIndexOptions().ignoreIfExists(true));

JsonObject returnedAirline10doc = collection.get("airline_10").contentAsObject();

JsonObject airline11Object = JsonObject.create().put("callsign", "MILE-AIR").put("iata", "Q5").put("icao", "MLA")
    .put("id", 11).put("name", "40-Mile Air").put("type", "airline");

collection.upsert("airline_11", airline11Object);

JsonObject returnedAirline11Doc = collection.get("airline_11").contentAsObject();

QueryResult result = userCluster.query("SELECT * FROM `travel-sample`.inventory.airline LIMIT 5");

userCluster.disconnect();
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).