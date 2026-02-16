[View original HTML](/ruby-sdk/3.6/howtos/sdk-user-management-example.html)

> The Ruby SDK lets you create _users_, assign them _roles_ and associated _privileges_, and remove them from the system. 

## [](#user-management-apis)User-Management APIs

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The Ruby SDK provides APIs to support these activities. A high-level summary of the APIs can be found in [User-Management](../concept-docs/sdk-user-management-overview.md), and details of all options in the [UserManager API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/UserManager.html).

## [](#using-the-usermanager-api)Using the UserManager API

The most common uses of the `UserManager` API are creating and listing users:

Creating Users

```ruby
user = Management::User.new
user.username = "testUsername"
user.password = "testPassword"
user.display_name = "Constance Lambert"
user.roles = [
  # Roles required for the reading of data from the bucket
  Management::Role.new do |r|
    r.name = "data_reader"
    r.bucket = "*"
  end,
  Management::Role.new do |r|
    r.name = "query_select"
    r.bucket = "*"
  end,

  # Roles required for the writing of data into the bucket
  Management::Role.new do |r|
    r.name = "data_writer"
    r.bucket = "*"
  end,
  Management::Role.new do |r|
    r.name = "query_insert"
    r.bucket = "*"
  end,
  Management::Role.new do |r|
    r.name = "query_delete"
    r.bucket = "*"
  end,

  # Role required for the creation of indexes on the bucket
  Management::Role.new do |r|
    r.name = "query_manage_index"
    r.bucket = "*"
  end,
]
cluster.users.upsert_user(user)
```

Listing Users

```ruby
list_of_users = cluster.users.get_all_users
list_of_users.each do |current_user|
  puts "User's display name is: #{current_user.display_name}"
  current_roles = current_user.roles
  current_roles.each do |role|
    puts "    User has the role: #{role.name}, applicable to bucket #{role.bucket}"
  end
end
```

Using a user created in the SDK to access data:

```ruby
bucket_name = "travel-sample"
options = Cluster::ClusterOptions.new
options.authenticate("testUsername", "testPassword")
user_cluster = Cluster.connect("couchbase://localhost", options)
user_bucket = user_cluster.bucket(bucket_name)
user_collection = user_bucket.default_collection

options = Management::QueryIndexManager::CreatePrimaryIndexOptions.new
options.ignore_if_exists = true
cluster.query_indexes.create_primary_index(bucket_name, options)

p returned_airline10_doc: user_collection.get("airline_10").content

airline11_object = {
  "callsign" => "MILE-AIR",
  "iata" => "Q5",
  "icao" => "MLA",
  "id" => 11,
  "name" => "40-Mile Air",
  "type" => "airline",
}
user_collection.upsert("airline_11", airline11_object)

p returned_airline11_doc: user_collection.get("airline_11").content

result = user_cluster.query("SELECT * from `#{bucket_name}` LIMIT 5")
result.rows.each_with_index do |row, idx|
  puts "#{idx}: #{row}"
end

user_cluster.disconnect
```

## [](#further-reading)Further Reading

The SDK also contains management APIs for dealing with [Cluster resources](provisioning-cluster-resources.md).