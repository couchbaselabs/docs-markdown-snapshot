---
title: User Management
description: The .NET SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.7/modules/howtos/pages/sdk-user-management-example.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.7@dotnet-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.7/howtos/sdk-user-management-example.html)

# User Management

> The .NET SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The .NET SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-net-client/html/T%5FCouchbase%5FManagement%5FUsers%5FIUserManager.htm).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```csharp
User user = new User(testUsername) {
    Password = testPassword,
    DisplayName = "Constance Lambert",
    Roles = new List<Role>() {
        // Roles required for the reading of data from the bucket
        new Role("data_reader", "*"),
        new Role("query_select", "*"),
        // Roles required for the writing of data into the bucket.
        new Role("data_writer", bucketName),
        new Role("query_insert", bucketName),
        new Role("query_delete", bucketName),
        // Role required for the creation of indexes on the bucket.
        new Role("query_manage_index", bucketName)
    }
};

await cluster.Users.UpsertUserAsync(user);
```

Listing Users

```csharp
IEnumerable<UserAndMetaData> listOfUsers = await cluster.Users.GetAllUsersAsync();

foreach (UserAndMetaData currentUser in listOfUsers) {
    Console.WriteLine($"User's display name is: { currentUser.User().DisplayName }");
    IEnumerable<Role> currentRoles = currentUser.User().Roles;
    foreach (Role role in currentRoles) {
        Console.WriteLine($"   User has the role: { role.Name }, applicable to bucket { role.Bucket }");
    }
}
```

Using a user created in the SDK to access data:

```csharp
var userCluster = await Cluster.ConnectAsync(
    "couchbase://your-ip",
    testUsername, testPassword);

var userBucket = await userCluster.BucketAsync(bucketName);
var scope = await userBucket.ScopeAsync("inventory");
var collection = await scope.CollectionAsync("airline");

try
{
    await userCluster.QueryIndexes.CreatePrimaryIndexAsync(
        $"`{bucketName}`", // NCBC-2955
        new CreatePrimaryQueryIndexOptions().IgnoreIfExists(true));
}
catch (InternalServerFailureException)
{
    Console.WriteLine("Primary index already exists!");
}

using var returnedAirline10doc = await collection.GetAsync("airline_10");

await collection.UpsertAsync(
    "airline_11", new {
        callsign = "MILE-AIR",
        iata = "Q5",
        icao = "MLA",
        id = 11,
        name = "40-Mile Air",
        type = "airline"
    }
);

using var returnedAirline11Doc = await collection.GetAsync("airline_11");
Console.WriteLine($"get -> { returnedAirline11Doc.ContentAs<dynamic>() }");

var result = await userCluster.QueryAsync<dynamic>(
    "SELECT * FROM `travel-sample`.inventory.airline LIMIT 2");

Console.WriteLine("query ->");
await foreach (var airline in result.Rows)
{
    Console.WriteLine(airline);
}

await userCluster.DisposeAsync();
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).