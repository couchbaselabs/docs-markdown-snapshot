---
title: Quickstart in Couchbase with C&#43;&#43;
description: Quickstart app to build a REST API using Couchbase Capella in C&#43;&#43;.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/hello-world/pages/sample-application.adoc
  xref: xref:1.3@cxx-sdk:hello-world:sample-application.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.3/hello-world/sample-application.html)

# Quickstart in Couchbase with C&#43;&#43;

> Quickstart app to build a REST API using Couchbase Capella in C++. Discover how to program interactions with Couchbase via the Data, Query, and Search services. 

After you have navigated through [signing up to Capella](https://cloud.couchbase.com/sign-up), if C++ is entered as your chosen language, you will be pointed to a clonable quickstart app on GitHub. If you were not, you can still find it [here](https://github.com/couchbase-examples/cxx-quickstart).

Often, the first step developers take after creating their database is to create a REST API that can perform Create, Read, Update, and Delete (CRUD) operations for that database. The [quickstart project](https://github.com/couchbase-examples/cxx-quickstart) is designed to teach you and give you a starter project (in C++) to generate such a REST API. After you have loaded the travel-sample bucket in your database, you can run this application which is a REST API with Swagger documentation so that you can learn:

1. How to create, read, update, and delete documents using [Key-Value operations](#howto:kv-operations). KV operations are unique to Couchbase and provide super fast (under millisecond) operations.
2. How to write simple parametrized [SQL++ queries](#howtos:n1ql-queries-with-sdk.html) using the built-in travel-sample bucket.

This documentation — and a number of other useful developer tutorials — can be found on the [Couchbase Developer Portal](https://github.com/couchbase-examples/cxx-quickstart).

## [](#prerequisites)Prerequisites

To run this prebuilt project, you will need:

* A [Couchbase Capella](https://www.couchbase.com/products/capella/) cluster with the [travel-sample](../ref/travel-app-data-model.md) bucket loaded.  
To run this tutorial using a self-managed Couchbase cluster, refer to the [Running Self-Managed Couchbase Cluster](#running-self-managed-couchbase-cluster) section.
* The Travel Sample Bucket is pre-loaded in Capella Free Tier. If you need to load it manually, see the [sample data impost page](../../../cloud/clusters/data-service/import-data-documents.md#import-sample-data).
* [CMake](https://cmake.org/) 3.9 or higher installed
* [C++17](https://en.cppreference.com/w/cpp/17) and a compatible compiler, such as [clang++](https://clang.llvm.org/) or [g++](https://gcc.gnu.org/).

## [](#app-setup)App Setup

We will walk through the different steps required to get the application running:

1. Cloning the Repo  
```console  
$ git clone https://github.com/couchbase-examples/cxx-quickstart.git  
```
2. Navigate to the Project Directory  
```console  
$ cd cxx-quickstart  
```

### [](#setup-database-configuration)Setup Database Configuration

To learn more about connecting to your Capella cluster, follow the [instructions](https://docs.couchbase.com/cloud/get-started/connect.html). Specifically, you need to do the following:

1. Create the [database credentials](../../../cloud/clusters/manage-database-users.md) to access the travel-sample bucket (Read and Write) used in the application.
2. [Allow access](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) to the Cluster from the IP on which the application is running.

All configuration for communication with the database is read from the environment variables. We have provided a convenience feature in this quickstart to set the required environment variables using the shell script `set_env_vars.sh`. Change the values of the following lines:

```sh
export DB_CONN_STR=<connection_string>
export DB_USERNAME=<username>
export DB_PASSWORD=<password>
export BUCKET_NAME=<bucket_name>
export SCOPE_NAME=<inventory>
export COL_NAME=<collection_name>
Note: The connection string expects the couchbases:// or couchbase:// part.
```

Run the command:

```console
source set_env_vars.sh
```

This will set the environment variables for that session.

### [](#install-dependencies-and-build)Install Dependencies and Build

This project makes use of CMake and CPM to install dependencies.

```console
$ mkdir build
```

```console
$ cd build
```

```console
$ cmake ..
```

```console
$ cmake --build .
```

This will download and install all of the dependencies required for the project to be built, and it will build the executable required to run the application.

## [](#running-the-application)Running The Application

> [!TIP]
> Running from a Development Machine
> 
> Couchbase — including Capella — is designed to run in a LAN-like environment. For development, connecting to a remote cloud instance from a local laptop instead of an application server in the same region, may require you to adjust some timeouts. For more information, see the [constrained network environments](../ref/client-settings.md#constrained-network-environments) section of the docs.

### [](#directly-on-your-local-machine)Directly on Your Local Machine

At this point, we have installed the dependencies, loaded the travel-sample data, and configured the application with the credentials. The application is now ready and you can run it by executing the following command from the `build` directory:

```console
$ cmake --build .
$ ./cxx_quickstart
```

### [](#verifying-the-application)Verifying the Application

Once you run the executable, your terminal should fill up with the results of the executed statements written in the main function of the `main.cpp` and should look something like this:

image::cli\_output.png

### [](#running-tests)Running Tests

For running tests, a self-managed cluster is required with travel-sample bucket loaded or you need to update the connection details in the `tests/test.cpp` file.

To run the tests, use the following command from the `build` directory:

```console
$ ./tests/u_tests
```

### [](#schema-and-usage-overview)Schema and Usage Overview

This quickstart utilizes two collections: airline and hotel. The airline collection is used for CRUD operations, while the hotel collection is leveraged for Search indexes and Query execution. The schemas for both collections can be found in the model folder.

## [](#code-review)Code Review

To begin this tutorial, clone the repo and open it up in the IDE of your choice. Now you can explore how to interact with Couchbase Server using the C++ SDK.

We have separated out the SDK code and the main function. The `db.h` and `db.cpp` contain the declaration and the implementation of utility functions we will use to parse environment variables and create a connection to the cluster. `operations.h` and `operations.cpp` contain all the functions that perform operations on the database. Both `db.cpp` and `operations.cpp` are combined to make a static library. The tests are similarly separated out in the tests folder which utilize the library created earlier. The `main.cpp` is the executable which is also built by linking the library and contains code that demonstrates the usage of the functions we defined earlier to interact with the database.

### [](#connecting-to-the-cluster)Connecting to the Cluster

In `db.h`, we include the required header files to work with C++ SDK in order to implement the functions required to initialize the database. In the `db.cpp` we implement the functions that help us connect to the database. We begin by implementing a few utility functions that will help us later. The `parseEnvironmentVariables` serves as a utility to get the values set for a list of environment variables. This enables us to get the connection parameters and credentials set by running source `set_env_vars.sh`. Following this, `checkScopeAndColExists` and `checkSearchEnabled` are implemented to check for the existence of a scope and collection of a given name and to verify if the Search Service is enabled respectively. Finally we have the `InitCluster` function which returns the connection objects as a tuple.

db.h

```c++
...
std::vector<std::string> parseEnvironmentVariables(const std::vector<std::string>& keys);
bool checkScopeAndColExists(couchbase::bucket& bucket, const std::string& scope_name, const std::string& col_name);
bool checkSearchEnabled(couchbase::cluster& cluster, int min_nodes);
...
std::tuple<couchbase::cluster, couchbase::bucket, couchbase::scope, couchbase::collection> InitCluster();
```

We recommend creating a single Couchbase connection when your application starts up, and sharing this instance throughout your application. You should always set the default `BUCKET_NAME`, `SCOPE_NAME`, `COL_NAME` environment variables, and use the `InitCluster` function to get the instances. You should share and use these instances throughout your application.

The Couchbase connection is established in the `connectCluster` method defined in `db.h` and implemented in `db.cpp`. There, we call the `connect` method defined in the SDK to create the Database connection. If the connection is already established, we do not do anything. Following connection to the cluster, get the reference to the bucket, scope and collection and return all the objects as a tuple.

db.h

```c++
...
auto [connect_err, cluster] = couchbase::cluster::connect(DB_CONN_STRING, options).get();
...
auto bucket = cluster.bucket(BUCKET_NAME);
...
auto scope = bucket.scope(SCOPE_NAME);
auto col = scope.collection(COL_NAME);
return {cluster, bucket, scope, col};
```

## [](#operations)Operations

Operations for interacting with the database are defined and implemented in `operations.h` and `operations.cpp`.

### [](#insert-document)Insert Document

Insert function is the equivalent of the `POST` request and can be used to insert new documents to the collection. We can pass the document to be inserted as a JSON string or as a JSON file path, the function takes in `file_flag` which is used to differentiate between the two.

* The value gets converted to the type `tao::json::value` and inserts it to the collection if `file_flag=false`.
* If `file_flag=true`, it reads the content from the provided file and then converts it to `tao::json::value`.
* Performs an upsert operation on the collection using the `doc_id` and the converted document content.
* If successful, `return 1`. If an error occurs, prints an error message and `return 0`.

operations.cpp

```c++
auto [in_error, in_res] = col.insert(doc_id, v).get();
```

main.cpp

```c++
auto insert_res = Insert(col, "quickstart_test", "{ \"test\": \"hello\"}", false);
auto insert_res2 = Insert(col, "quickstart_test2", "doc.json", true);
```

### [](#upsert-document)Upsert Document

The `Upsert` function is the equivalent of the `PUT` request. It can be used to update any existing document or to insert a new document to the collection if the `doc_id` does not already exist. Similar to Insert — we can pass the document to be inserted as a JSON string or as a JSON file path, the function takes in `file_flag` which is used to differentiate between the two.

* The value gets converted to the type `tao::json::value` and inserts it to the collection if `file_flag=false`.
* If `file_flag=true`, it reads the content from the provided file and then converts it to `tao::json::value`.
* Performs an insert operation on the collection using the `doc_id` and the converted document content.
* If successful, `return 1`. If an error occurs, prints an error message and `return 0`.

operations.cpp

```c++
auto [up_error, up_res] = col.upsert(doc_id, v).get();
```

main.cpp

```c++
auto upsert_res = Upsert(col, "quickstart_test", "{ \"test\": \"hello\"}", false);
auto upsert_res2 = Upsert(col, "quickstart_test2", "doc.json", true);
```

### [](#read)Read

The `Read` function is equivalent to `GET` requests and can be used to fetch documents using the `doc_id`.

* First checks if the document exists using `col.exists(doc_id)`.
* If the document exists, it retrieves the document's content using `col.get(doc_id)` and returns it after converting it to `tao::json::value` for easier usage on return.
* If an error occurs (such as "document not found"), it prints an error message and returns an empty `tao::json::value` object.

operations.cpp

```c++
auto [ex_err, ex_res] = col.exists(doc_id).get();
...
auto [get_err, get_res] = col.get(doc_id).get();
...
auto doc = get_res.content_as<tao::json::value>();
return doc;
```

main.cpp

```c++
 v = Read(col, "airline_10123");
std::cout << tao::json::to_string(v) << std::endl;
```

### [](#delete)Delete

The `Delete` function attempts to remove a document with the given `doc_id`.

* Attempts to remove the document with a given `doc_id` from the collection.
* If the deletion is successful, `return 1` and if an error occurs, it prints an error message and `return 0`.

operations.cpp

```c++
auto [delete_err, delete_res] = col.remove(doc_id).get();
```

main.cpp

```c++
auto res = Delete(col, doc_id);
```

### [](#query)Query

We can use the `Query` function to execute any SQL++ query on a scope.

* Executes the SQL++ query using the provided `scope.query(query, opts)`.
* Returns the result of the query if successful. The result is added to a `std::vector<std::string>` object that contains the `id`, `country`, `avg_rating`, `title`.
* We can pass `opts` parameter, which can be used to insert positional parameters in the query.
* If there is an error, it prints an error message and returns an empty result object.

operations.cpp

```c++
std::string query{ R"(
    SELECT META(h).id, h AS doc,
            AVG(r.ratings.Overall) AS avg_rating
    FROM hotel h
    UNNEST h.reviews r
    WHERE h.country IN $1 AND h.description LIKE "%cheap%"
    GROUP BY META(h).id, h
    ORDER BY avg_rating DESC
    LIMIT 5;
)" };
auto [q_err, q_res] = scope.query(query, couchbase::query_options{}.positional_parameters(std::vector<std::string>{"United States", "United Kingdom"})).get();
```

main.cpp

```c++
for (auto& row : query_res) {
  std::cout << row << std::endl;
}
```

### [](#create-a-search-index)Create a Search Index

Search indexes in Couchbase are used for full-text search and efficient querying of documents based on specific fields or attributes. The `CreateSearchIndex` function helps in creating a new Search index which can then be used.

* Reads the index configuration from the `index_file`.
* Checks if an index with the same name already exists using the `searchIndexExists` function.
* If the index with same name exists, it returns the index name.
* If the index does not exist, it constructs a new search index object and upserts it into the Couchbase scope.
* Returns the name of the newly created index or an empty string if there was an error.

operations.cpp

```c++
auto err = scope_index_manager.upsert_index(i).get();
```

main.cpp

```c++
std::string index_name = CreateSearchIndex(scope, "hotel_search_index.json");
```

### [](#search-by-name)Search By Name

The `SearchByName` function aims to demonstrate the usage of a Search index to search for documents in a scope. Params:

* `scope`: The Couchbase scope to search in.
* `index`: The Search index name to use for the query.
* `name`: The name to search for in the documents.
* `field`: The field where the name should be searched.
* `limit`: The maximum number of results to return.

operations.cpp

```c++
auto [s_err, s_res] = scope.search(index, searchQ, opts).get();
...
std::vector<std::string> rows_res{};
// Reference is important since the copy constructor is deleted
for(auto &row:s_res.rows()){
    rows_res.push_back(row.id());
}
return rows_res;
```

main.cpp

```c++
auto search_res = SearchByName(scope, index_name, "swanky", "name", 50);
std::cout << "Search result contains:\t" << search_res.size() << std::endl;
```

### [](#filter)Filter

The `Filter` function aims to demo the construction and execution of a `conjunction_query` which can be described as an AND operation on two or more types of filters. This particular implementation performs a conjunction on `couchbase::match_query("United States").field("country")` and `couchbase::term_query("San Diego").field("city")`.

operations.cpp

```c++
auto query = couchbase::conjunction_query{
        couchbase::match_query("United States").field("country"),
        couchbase::term_query("San Diego").field("city")
    };
...
auto [err,res] = scope.search(index_name, couchbase::search_request(query), opts).get();

for(auto &row:res.rows()){
  auto fields = row.fields_as<couchbase::codec::tao_json_serializer>();
  rows_res.push_back(fields["name"].as<std::string>());
}
return rows_res;
```

main.cpp

```c++
auto filter_res = Filter(scope, index_name, 50, 1);
std::cout << "Filter result contains:\t" << filter_res.size() << std::endl;
```

## [](#running-self-managed-couchbase-cluster)Running Self-Managed Couchbase Cluster

If you are running this quickstart with a self-managed Couchbase cluster, you need to [load](../../../server/current/manage/manage-settings/install-sample-buckets.md) the travel-sample data bucket in your cluster and generate the credentials for the bucket.

You need to update the connection string and the credentials in the `application.properties` file in the `src/main/resources` folder.