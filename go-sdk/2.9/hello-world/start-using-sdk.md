[View original HTML](/go-sdk/2.9/hello-world/start-using-sdk.html)

> A quick start guide to get you up and running with Couchbase and the Go SDK. 

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

To connect to [Couchbase Capella](#cloud::index.adoc), be sure to get the correct endpoint as well as user, password and bucket name.

```go
package main

import (
	"fmt"
	"log"
	"time"

	"github.com/couchbase/gocb/v2"
)


func main() {
	// Uncomment following line to enable logging
	// gocb.SetLogger(gocb.VerboseStdioLogger())

	// Update this to your cluster details
	connectionString := "cb.<your-endpoint>.cloud.couchbase.com"
	bucketName := "travel-sample"
	username := "username"
	password := "Password!123"

	options := gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: username,
			Password: password,
		},
	}

	// Sets a pre-configured profile called "wan-development" to help avoid latency issues
	// when accessing Capella from a different Wide Area Network
	// or Availability Zone (e.g. your laptop).
	if err := options.ApplyProfile(gocb.ClusterConfigProfileWanDevelopment); err != nil {
		log.Fatal(err)
	}

	// Initialize the Connection
	cluster, err := gocb.Connect("couchbases://"+connectionString, options)
	if err != nil {
		log.Fatal(err)
	}

	bucket := cluster.Bucket(bucketName)

	err = bucket.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Get a reference to the default collection, required for older Couchbase server versions
	// col := bucket.DefaultCollection()

	col := bucket.Scope("tenant_agent_00").Collection("users")

	// Create and store a Document
	type User struct {
		Name      string   `json:"name"`
		Email     string   `json:"email"`
		Interests []string `json:"interests"`
	}

	_, err = col.Upsert("u:jade",
		User{
			Name:      "Jade",
			Email:     "jade@test-email.com",
			Interests: []string{"Swimming", "Rowing"},
		}, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Get the document back
	getResult, err := col.Get("u:jade", nil)
	if err != nil {
		log.Fatal(err)
	}

	var inUser User
	err = getResult.Content(&inUser)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("User: %v\n", inUser)

	// Perform a N1QL Query
	inventoryScope := bucket.Scope("inventory")
	queryResult, err := inventoryScope.Query(
		fmt.Sprintf("SELECT * FROM airline WHERE id=10"),
		&gocb.QueryOptions{},
	)
	if err != nil {
		log.Fatal(err)
	}

	// Print each found Row
	for queryResult.Next() {
		var result interface{}
		err := queryResult.Row(&result)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(result)
	}

	if err := queryResult.Err(); err != nil {
		log.Fatal(err)
	}
}
```

```go
package main

import (
	"fmt"
	"log"
	"time"

	"github.com/couchbase/gocb/v2"
)

func main() {
	// Uncomment following line to enable logging
	// gocb.SetLogger(gocb.VerboseStdioLogger())

	// Update this to your cluster details
	connectionString := "localhost"
	bucketName := "travel-sample"
	username := "Administrator"
	password := "password"

	// For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
	cluster, err := gocb.Connect("couchbase://"+connectionString, gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: username,
			Password: password,
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	bucket := cluster.Bucket(bucketName)

	err = bucket.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Get a reference to the default collection, required for older Couchbase server versions
	// col := bucket.DefaultCollection()

	col := bucket.Scope("tenant_agent_00").Collection("users")

	type User struct {
		Name      string   `json:"name"`
		Email     string   `json:"email"`
		Interests []string `json:"interests"`
	}

	// Create and store a Document
	_, err = col.Upsert("u:jade",
		User{
			Name:      "Jade",
			Email:     "jade@test-email.com",
			Interests: []string{"Swimming", "Rowing"},
		}, nil)
	if err != nil {
		log.Fatal(err)
	}

	// Get the document back
	getResult, err := col.Get("u:jade", nil)
	if err != nil {
		log.Fatal(err)
	}

	var inUser User
	err = getResult.Content(&inUser)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("User: %v\n", inUser)

	// Perform a N1QL Query
	inventoryScope := bucket.Scope("inventory")
	queryResult, err := inventoryScope.Query(
		fmt.Sprintf("SELECT * FROM airline WHERE id=10"),
		&gocb.QueryOptions{Adhoc: true},
	)
	if err != nil {
		log.Fatal(err)
	}

	// Print each found Row
	for queryResult.Next() {
		var result interface{}
		err := queryResult.Row(&result)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(result)
	}

	if err := queryResult.Err(); err != nil {
		log.Fatal(err)
	}
}
```

As well as the Go SDK (see below), and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-ui)or the [command line](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-cli).

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Couchbase Server

* You have initalised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.
* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

|  | Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* You have initalised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.
* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

|  | Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#quick-installation)Quick Installation

Version 2 of the Go SDK has added support for [Go Modules](https://github.com/golang/go/wiki/Modules). You can use `go get` to download the SDK:

```console
$ go get github.com/couchbase/gocb/v2
```

More details on installation can be found [here](../project-docs/sdk-full-installation.md).

|  | In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), we support both the current, and the previous, versions of Go. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#step-by-step)Step by Step

Create an empty file named `main.go` and walk through adding code step-by-step.

Here are all the imports needed to run the sample code:

```golang
package main

import (
	"fmt"
	"log"
	"time"

	"github.com/couchbase/gocb/v2"
)
```

Now, create an empty `main()` function.

```golang
func main() {
	// add code here...
}
```

In your `main()` function, add the following variables and update them accordingly:

* Couchbase Capella
* Local Couchbase Server

```golang
// Update this to your cluster details
connectionString := "cb.<your-endpoint>.cloud.couchbase.com"
bucketName := "travel-sample"
username := "username"
password := "Password!123"
```

```golang
// Update this to your cluster details
connectionString := "localhost"
bucketName := "travel-sample"
username := "Administrator"
password := "password"
```

### [](#connect)Connect

Connect to your cluster by calling the `Cluster.Connect()` function and pass it your connection details. The basic connection details that you’ll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Couchbase Capella
* Local Couchbase Server

Couchbase Capella requires mandatory use of TLS (Transport Layer Security). As of Go SDK version 2.5.0, the standard certificate required to connect to a Capella cluster is automatically included with no additional configuration.

```golang
options := gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: username,
		Password: password,
	},
}

// Sets a pre-configured profile called "wan-development" to help avoid latency issues
// when accessing Capella from a different Wide Area Network
// or Availability Zone (e.g. your laptop).
if err := options.ApplyProfile(gocb.ClusterConfigProfileWanDevelopment); err != nil {
	log.Fatal(err)
}

// Initialize the Connection
cluster, err := gocb.Connect("couchbases://"+connectionString, options)
if err != nil {
	log.Fatal(err)
}
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 2.6 introduces a `wan-development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

|  | The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```golang
// For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
cluster, err := gocb.Connect("couchbase://"+connectionString, gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: username,
		Password: password,
	},
})
if err != nil {
	log.Fatal(err)
}
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

```golang
bucket := cluster.Bucket(bucketName)

err = bucket.WaitUntilReady(5*time.Second, nil)
if err != nil {
	log.Fatal(err)
}
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

The Go SDK supports full integration with the [Collections](../concept-docs/collections.md) feature introduced in Couchbase Server 7.0\. _Collections_ allow documents to be grouped by purpose or theme, according to a specified _Scope_.

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```golang
// Get a reference to the default collection, required for older Couchbase server versions
// col := bucket.DefaultCollection()

col := bucket.Scope("tenant_agent_00").Collection("users")
```

|  | For Local Couchbase Server only The DefaultCollection must be used when connecting to a 6.6 cluster or earlier — see comment in the code snippet above. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------- |

The code shows how you would use a named collection and scope. A named or default collection will provide the same functionality as bucket-level operations did in previous versions of Couchbase Server.

[Data operations](../howtos/kv-operations.md), such as storing and retrieving documents, can be done using `Collection.Upsert()` and `Collection.Get()`.

Add the following code to create a new document:

```golang
// Create and store a Document
type User struct {
	Name      string   `json:"name"`
	Email     string   `json:"email"`
	Interests []string `json:"interests"`
}

_, err = col.Upsert("u:jade",
	User{
		Name:      "Jade",
		Email:     "jade@test-email.com",
		Interests: []string{"Swimming", "Rowing"},
	}, nil)
if err != nil {
	log.Fatal(err)
}
```

Now, let’s retrieve it using a key-value (data) operation.

```golang
// Get the document back
getResult, err := col.Get("u:jade", nil)
if err != nil {
	log.Fatal(err)
}

var inUser User
err = getResult.Content(&inUser)
if err != nil {
	log.Fatal(err)
}
fmt.Printf("User: %v\n", inUser)
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries are performed by invoking `Cluster.Query()` or `Scope.Query`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```golang
// Perform a N1QL Query
inventoryScope := bucket.Scope("inventory")
queryResult, err := inventoryScope.Query(
	fmt.Sprintf("SELECT * FROM airline WHERE id=10"),
	&gocb.QueryOptions{},
)
if err != nil {
	log.Fatal(err)
}

// Print each found Row
for queryResult.Next() {
	var result interface{}
	err := queryResult.Row(&result)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}

if err := queryResult.Err(); err != nil {
	log.Fatal(err)
}
```

You can learn more about SQL++ queries on the [Query](../howtos/n1ql-queries-with-sdk.md) page.

### [](#execute)Execute!

Now we can run our code using the following command:

```console
$ go run main.go
```

The results you should expect are as follows:

```console
User: {Jade jade@test-email.com [Swimming Rowing]}
map[airline:map[callsign:MILE-AIR country:United States iata:Q5 icao:MLA id:10 name:40-Mile Air type:airline]]
```

## [](#next-steps)Next Steps

Now you’re up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) (CRUD) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL-based SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and can be found [here](https://pkg.go.dev/github.com/couchbase/gocb/v2). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

[The Migrating from SDK2 API (Go 1.x) to API 3 page (Go 2.x SDK)](../project-docs/migrating-sdk-code-to-3.n.md) highlights the main differences to be aware of when migrating your code.

Couchbase welcomes community contributions to the Go SDK. The Go SDK source code is available on [GitHub](https://github.com/couchbase/gocb).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you’re running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/go-sdk/23) is a great source of help.