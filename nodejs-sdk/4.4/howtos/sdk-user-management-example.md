---
title: User Management
description: The Node.js SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/howtos/pages/sdk-user-management-example.adoc
  xref: xref:4.4@nodejs-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.4/howtos/sdk-user-management-example.html)

# User Management

> The Node.js SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Node.js SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```javascript
const userMgr = clusterAdm.users();

await userMgr.upsertUser({
    username: testUsername,
    password: testPassword,
    displayName: "Constance Lambert",
    roles: [
        // Roles required for the reading of data from the bucket
        { name: "data_reader", bucket: "*" },
        { name: "query_select", bucket: "*" },
        
        // Roles required for the writing of data into the bucket. 
        { name: "data_writer", bucket: bucketName },
        { name: "query_insert", bucket: bucketName },
        { name: "query_delete", bucket: bucketName },
        
        // Role required for the creation of indexes on the bucket.
        { name: "query_manage_index", bucket: bucketName }
    ]
})
```

Listing Users

```javascript
const listOfUsers = await clusterAdm.users().getAllUsers();

for (const currentUser of listOfUsers) {
    console.log(`User's display name is: ${ currentUser.displayName }`);
    const currentRoles = currentUser.effectiveRoles;
    for (const role of currentRoles) {
        console.log(`   User has the role: ${ role.name }, applicable to bucket ${ role.bucket }`);
    }
}
```

Using a user created in the SDK to access data:

```javascript
const userCluster = await couchbase.connect(
    "couchbase://localhost", {
    username: testUsername,
    password: testPassword,
})
const bucket = userCluster.bucket(bucketName)
const scope = bucket.scope("inventory")
const collection = scope.collection("airline")

await collection.upsert(
    "airline_11", {
        callsign: "MILE-AIR",
        iata: "Q5",
        icao: "MLA",
        id: 11,
        name: "40-Mile Air",
        type: "airline"
    }
)
userCluster.close()
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).