[View original HTML](/rust-sdk/current/concept-docs/management-api.html)

> Cluster management from the SDK. 

The Couchbase Rust SDK has a management API to provision clusters. This is not the only programmatic way to deploy Couchbase, and you may wish to look at [Terraform](../../../cloud/terraform/index.md) for Capella, or some of our command line tools.

## [](#user-management)User Management

The SDK lets you programmatically create _users_, assign them _roles_ and associated _privileges_, and remove them from the system.

This is an overview of the user management API’s capabilities.

### [](#creating-a-user)Creating a User

The syntax required for creating a user varies according to language, and is covered for each SDK in the management documentation. The basic form is as follows:

async fn upsert_user(
        &self,
        settings: User,
        opts: impl Into<Option<UpsertUserOptions>>,
    ) -> error::Result<()>

The method **upsert\_user** creates a user and adds the user to the Couchbase Cluster. The user will subsequently be visible in the **Security** panel of the Couchbase Web Console. Note that successful user-addition results in a user _locally_ defined, with _username_ and _password_ stored on Couchbase Server: _external_ users (whose credentials reside on a network-available server, possibly accessed by means of LDAP) should not be created by this SDK method. If the local user created by **upsert\_user** already exists, the previous definition is overwritten.

```rust
pub struct User {
    pub username: String,
    pub display_name: String,
    pub groups: Vec<String>,
    pub roles: Vec<Role>,

    pub(crate) password: Option<String>,
}
```

Creation of a _User_ is typically performer using a builder:

```rust
pub fn new(
        username: impl Into<String>,
        display_name: impl Into<String>,
        roles: Vec<Role>,
    ) -> Self
```

Role must be non-empty and each _Role_ takes the following form:

```rust
pub struct Role {
    pub name: String,
    pub bucket: Option<String>,
    pub scope: Option<String>,
    pub collection: Option<String>,
}
```

Again, creation of a _Role_ is typically performer using a builder:

```rust
pub fn new(name: impl Into<String>) -> Self
```

The name specified as the role must correspond to a role supported by Couchbase Server. When specified the bucket, scope, and collection fields must either correspond to a resource currently defined on Couchbase Server; or be the asterisk character (_\*_), meaning _all_.

### [](#listing%5Fusers)Listing Users

The basic form of the method used to return currently defined users is as follows:

```rust
async fn get_all_users(
        &self,
        opts: impl Into<Option<GetAllUsersOptions>>,
    ) -> error::Result<Vec<UserAndMetadata>>
```

### [](#getting-a-user)Getting a User

The basic form of the method used to return an already defined user is as follows:

```rust
pub async fn get_user(
    &self,
    username: impl Into<String>,
    opts: impl Into<Option<GetUserOptions>>,
) -> error::Result<UserAndMetadata>
```

### [](#removing-a-user)Removing a User

The basic form of the method used to remove users is as follows:

pub async fn drop_user(
        &self,
        username: impl Into<String>,
        opts: impl Into<Option<DropUserOptions>>,
    ) -> error::Result<()>