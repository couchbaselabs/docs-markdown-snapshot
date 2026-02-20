---
title: User Management
description: The PHP SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/howtos/pages/sdk-user-management-example.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:php-sdk:howtos:sdk-user-management-example.adoc[]
---

[View original HTML](/php-sdk/current/howtos/sdk-user-management-example.html)

# User Management

> The PHP SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The PHP SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Management-UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```php
$roles = [
    // Roles required for reading data from bucket
    Role::build()->setName("data_reader")->setBucket("*"),
    Role::build()->setName("query_select")->setBucket("*"),
    // Roles required for writing data to bucket
    Role::build()->setName("data_writer")->setBucket("travel-sample"),
    Role::build()->setName("query_insert")->setBucket("travel-sample"),
    Role::build()->setName("query_delete")->setBucket("travel-sample"),
    // Roles required for idx creation on bucket
    Role::build()->setName("query_manage_index")->setBucket("travel-sample"),
];

$user = new User();
$user->setUsername("test-user");
$user->setDisplayName("Test User");
$user->setRoles($roles);
$user->setPassword("test-passw0rd!");

$userMgr->upsertUser($user);
```

Listing Users

```php
$userMetadata = $userMgr->getAllUsers();
foreach ($userMetadata as &$u) {
    printf("User's display name: %s\n", $u->user()->displayName());

    $userRoles = $u->user()->roles();
    foreach ($userRoles as &$role) {
        printf("\tUser has role %s, applicable to bucket %s\n", $role->name(), $role->bucket());
    }
}
```

Using a user created in the SDK to access data:

```php
$options = new ClusterOptions();
$options->credentials("test-user", "test-passw0rd!");
$userCluster = new Cluster("couchbase://localhost", $options);

# For Server versions 6.5 or later you do not need to open a bucket here
$userBucket = $userCluster->bucket("travel-sample");
$collection = $userBucket->defaultCollection();

# create primary idx for testing purposes
$createPrimaryQueryIndexOpts = new CreateQueryPrimaryIndexOptions();
$createPrimaryQueryIndexOpts->ignoreIfExists(true);

$userCluster->queryIndexes()->createPrimaryIndex("travel-sample", $createPrimaryQueryIndexOpts);

# test k/v operations
$airline10 = $collection->get("airline_10");
printf("Airline 10: %s", $airline10->contentAs(RawJsonTranscoder::getInstance()));

$airline11 = [
    "callsign" => "MILE-AIR",
    "iata" => "Q5", "id" => 11,
    "name" => "40-Mile Air",
    "type" => "airline"
];
$collection->upsert("airline11", $airline11);

# test query operations
$queryResult = $userCluster->query("SELECT * FROM `travel-sample` LIMIT 5;");
foreach ($queryResult->rows() as &$row) {
    print("\nQuery Row:\n");
    print_r($row);
}
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).