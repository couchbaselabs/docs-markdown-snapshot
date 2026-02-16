[View original HTML](/rust-sdk/current/howtos/sdk-user-management-example.html)

> The Rust SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The SDK lets you programmatically create _users_, assign them _roles_ and associated _privileges_, and remove them from the system.

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are administering users:

Upserting Users

```rust
let mgr = cluster.users();
mgr.upsert_user(
    User::new("example-user", "display-name", vec![Role::new("admin")]).password("password"),
    None,
)
.await?;
```

Listing Users

```rust
let mgr = cluster.users();
let users = mgr.get_all_users(None).await?;
```

Removing Users

```rust
let mgr = cluster.users();
mgr.drop_user("example-user", None).await?;
```

Changing a password

```rust
let mgr = cluster.users();
mgr.change_password("new-password", None).await?;
```

|  | change\_password applies to the user currently authenticated in the Cluster instance. |
|  | ------------------------------------------------------------------------------------- |

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).