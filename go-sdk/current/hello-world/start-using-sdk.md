---
title: Start Using the Go SDK
description: A quick start guide to get you up and running with Couchbase and the Go SDK.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:go-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/hello-world/start-using-sdk.html)

# Start Using the Go SDK

> A quick start guide to get you up and running with Couchbase and the Go SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let’s look at those data operations, and installing the Go SDK.

```golang
// Upsert with Durability level Majority
durableResult, err := collection.Upsert("document-key", &document, &gocb.UpsertOptions{
	DurabilityLevel: gocb.DurabilityLevelMajority,
})
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We’ll explore creating and retrieving data records in more detail [below](#create-read-update-delete), after walking through a quick installation.

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven’t already got a cluster set up, the easiest route is to [sign up to Couchbase Capella and deploy a free tier cluster](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

Install Couchbase Server locally, or in your private Cloud:

* [Deployment overview](../../../server/current/install/get-started.md)
* [Docker Install](../../../server/current/install/getting-started-docker.md)
* [Couchbase Autonomous Operator](../../../operator/current/overview.md)

  * [Kubernetes](../../../operator/current/install-kubernetes.md)
  * [Openshift](../../../operator/current/install-openshift.md)
* [Cloud Marketplace](#8.0server:cloud:couchbase-cloud-deployment.adoc):

  * [AWS Marketplace](../../../server/current/cloud/couchbase-aws-marketplace.md)
  * [Azure Marketplace](../../../server/current/cloud/couchbase-azure-marketplace.md)
  * [GCP Marketplace](../../../server/current/cloud/couchbase-gcp-cloud-launcher.md)

For the example code below to run, you’ll need the username and password of the Administrator user that you create, and the IP address of at least one of the nodes of the cluster.

### [](#prerequisites)Prerequisites

In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), we support both the current, and the previous, versions of Go. At time of writing (February 2026), this is 1.25 and 1.26.

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

* [Couchbase Server](#8.0@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

## [](#installation)Installation

You can use `go get` to download the SDK:

```console
$ go get github.com/couchbase/gocb/v2
```

More details on installation can be found [here](../project-docs/sdk-full-installation.md).

### [](#ide-plugins)IDE Plugins

To make development easier, Couchbase plugins are available for VSCode and the IntelliJ family of IDEs and editors. For links and more information on these and other integrations across the Go ecosystem, check out the [Integrations & Ecosystem](../project-docs/third-party-integrations.md) page.

### [](#grab-the-code)Grab the Code

If you’re all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

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

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There’s a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)

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

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

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

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a TLS, enabled with `couchbases://`.

Couchbase’s large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — currently only compatible with recent versions of [Couchbase Autonomous Operator](../../../operator/current/concept-cloud-native-gateway.md):

```golang
	cluster, err := gocb.Connect("couchbase2://"+connectionString, gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: username,
			Password: password,
		},
```

Read more on the [Connections](../howtos/managing-connections.md#cloud-native-gateway) page.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app — more on this in [the Security documentation](../concept-docs/best-practices.md#roles-and-rbac).

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. The `wan-development` Configuration Profile, provides pre-configured timeout settings suitable for working in high latency environments. See [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, add this code snippet to access your `Bucket`:

```golang
bucket := cluster.Bucket(bucketName)

err = bucket.WaitUntilReady(5*time.Second, nil)
if err != nil {
	log.Fatal(err)
}
```

`WaitUntilReady` is an optional call, but it is good practice to use it. Opening resources such as buckets is asynchronous — that is, the `cluster.Bucket` call returns immediately and proceeds in the background. `WaitUntilReady` ensures that the bucket resource is fully loaded before proceeding. If not present, then the first key-value (KV) operation on the bucket will wait for it to be ready.

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```golang
col := bucket.Scope("tenant_agent_00").Collection("users")
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, throwing `ErrDocumentExists` — while the `upsert` operation will succeed, replacing the content.

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

### [](#get-read)Get (Read)

The `get` method reads a document from a collection. If the collection does not have a document with this ID, the `get` method also throws `ErrDocumentNotFound`.

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

### [](#replace-update-and-optimistic-locking)Replace (Update) and Optimistic Locking

When you replace a document, it’s usually good practice to use [optimistic locking](../howtos/kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

Setting a Compare and Swap (CAS) value is a form of optimistic locking — dealt with in depth in the [CAS page](#concurrent-document-mutations.adoc). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document’s metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of `0`.

```go
	// Replace Document with Cas
	replaceResultWithCas, err := collection.Replace("document-key", &document, &gocb.ReplaceOptions{
		Cas: 12345,
	})
	if err != nil {
		// We expect this to error
		fmt.Println(err)
	}
```

Typically we would want to use CAS for something more meaningful like performing a `Get`, modifying the result and updating the document. By using the CAS value we know that if anyone else modified this document and updated it before our update then ours will error.

```go
	// Get and Replace Document with Cas
	updateGetResult, err := collection.Get("document-key", nil)
	if err != nil {
		panic(err)
	}

	var doc myDoc
	err = updateGetResult.Content(&doc)
	if err != nil {
		panic(err)
	}

	doc.Bar = "moo"

	updateResult, err := collection.Replace("document-key", doc, &gocb.ReplaceOptions{
		Cas: updateGetResult.Cas(),
	})
```

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

```go
	// Remove with Durability
	removeResult, err := collection.Remove("document-key", &gocb.RemoveOptions{
		Timeout:         100 * time.Millisecond,
		DurabilityLevel: gocb.DurabilityLevelMajority,
	})
	if err != nil {
		panic(err)
	}
```

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document’s ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection’s name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/go-sdk/23).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).

### [](#next-steps)Next Steps

* Take a look at the [Quickstart with Golang and the Gin Web Framework](sample-application.md).
* [Learn more about the Data Service](../concept-docs/data-durability-acid-transactions.md).
* [Discover SQL++](../concept-docs/querying-your-data.md) — our SQL-family querying language.

### [](#additional-resources)Additional Resources

* The API reference is generated for each release and can be found [here](https://pkg.go.dev/github.com/couchbase/gocb/v2). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).
* Couchbase welcomes community contributions to the Go SDK. The Go SDK source code is available on [GitHub](https://github.com/couchbase/gocb).