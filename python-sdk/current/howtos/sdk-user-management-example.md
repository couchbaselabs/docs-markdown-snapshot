---
title: User Management
description: The Python SDK lets you create <em>users</em>, assign them
  <em>roles</em> and associated <em>privileges</em>, and remove them from the
  system.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/howtos/pages/sdk-user-management-example.adoc
  xref: xref:python-sdk:howtos:sdk-user-management-example.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/sdk-user-management-example.html)

# User Management

> The Python SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Python SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/couchbase%5Fmanagement.html#module-couchbase.management.users).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```python
user_manager = adm_cluster.users()
user = User(username=username, display_name="Test User",
            roles=[
                # Roles required for reading data from bucket
                Role(name="data_reader", bucket="*"),
                Role(name="query_select", bucket="*"),
                # Roles require for writing data to bucket
                Role(name="data_writer", bucket=bucket_name),
                Role(name="query_insert", bucket=bucket_name),
                Role(name="query_delete", bucket=bucket_name),
                # Role required for idx creation on bucket
                Role(name="query_manage_index", bucket=bucket_name),
            ], password=pw)

user_manager.upsert_user(user)
```

Listing Users

```python
users_metadata = user_manager.get_all_users()
for u in users_metadata:
    print("User's display name: {}".format(u.user.display_name))
    roles = u.user.roles
    for r in roles:
        print(
            "\tUser has role {}, applicable to bucket {}".format(
                r.name, r.bucket))
```

Using a user created in the SDK to access data:

```python
user_cluster = Cluster.connect(
    "couchbase://your-ip",
    authenticator=PasswordAuthenticator(username, pw))

# For Server versions 6.5 or later you do not need to open a bucket here
user_bucket = user_cluster.bucket(bucket_name)
collection = user_bucket.default_collection()

# create primary idx for testing purposes
user_cluster.query_indexes().create_primary_index(
    bucket_name, CreatePrimaryQueryIndexOptions(
        ignore_if_exists=True))

# test k/v operations
airline_10 = collection.get("airline_10")
print("Airline 10: {}".format(airline_10.content_as[dict]))

airline_11 = {
    "callsign": "MILE-AIR",
                "iata": "Q5",
                "id": 11,
                "name": "40-Mile Air",
                "type": "airline",
}

collection.upsert("airline_11", airline_11)

# test query operations
query_res = user_cluster.query("SELECT * FROM `travel-sample` LIMIT 5;")
for row in query_res.rows():
    print("Query row: {}".format(row))
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).