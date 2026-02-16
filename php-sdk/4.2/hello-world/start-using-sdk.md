[View original HTML](/php-sdk/4.2/hello-world/start-using-sdk.html)

> Installing the Couchbase PHP SDK & a Hello World example program. 

The Couchbase PHP SDK allows you to connect to a Couchbase cluster from PHP. It is a native PHP extension and uses the `Couchbase++` high-performance C++ library to handle communicating to the cluster over Couchbase binary protocols.

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

If you are connecting to [Couchbase Capella](https://docs.couchbase.com/cloud/index.html), be sure to get the correct endpoint as well as the username and password.

```php
<?php

// NOTE: Change the below vendor path to your own.
require_once '../../../vendor/autoload.php';

use Couchbase\ClusterOptions;
use Couchbase\Cluster;

// Update these credentials for your Capella instance!
$connectionString = "couchbases://cb.<your-instance>.cloud.couchbase.com";
$options = new ClusterOptions();

$options->credentials("username", "Password!123");
// Sets a pre-configured profile called "wan_development" to help avoid latency issues
// when accessing Capella from a different Wide Area Network
// or Availability Zone (e.g. your laptop).
$options->applyProfile("wan_development");
$cluster = new Cluster($connectionString, $options);

// get a bucket reference
$bucket = $cluster->bucket("travel-sample");

// get a user-defined collection reference
$scope = $bucket->scope("tenant_agent_00");
$collection = $scope->collection("users");

$upsertResult = $collection->upsert("my-document-key", ["name" => "Ted", "Age" => 31]);

$getResult = $collection->get("my-document-key");

print_r($getResult->content());

$inventoryScope = $bucket->scope("inventory");
$queryResult = $inventoryScope->query("SELECT * FROM airline WHERE id = 10");

// Print result data to the terminal.
foreach ($queryResult->rows() as $row) {
    print_r($row);
}
```

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

```php
<?php

// NOTE: Change the below vendor path to your own.
require_once '../../../vendor/autoload.php';

use Couchbase\ClusterOptions;
use Couchbase\Cluster;

// Update these credentials for your Local instance!
$connectionString = "couchbase://localhost";
$options = new ClusterOptions();

$options->credentials("Administrator", "password");
$cluster = new Cluster($connectionString, $options);

// get a bucket reference
$bucket = $cluster->bucket("travel-sample");

// get a user-defined collection reference
$scope = $bucket->scope("tenant_agent_00");
$collection = $scope->collection("users");

$upsertResult = $collection->upsert("my-document-key", ["name" => "Ted", "Age" => 31]);

$getResult = $collection->get("my-document-key");

print_r($getResult->content());

$inventoryScope = $bucket->scope("inventory");
$queryResult = $inventoryScope->query("SELECT * FROM airline WHERE id = 10");

// Print result data to the terminal.
foreach ($queryResult->rows() as $row) {
    print_r($row);
}
```

As well as the PHP SDK (see below), and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

## [](#quick-installation)Quick Installation

A more detailed guide in our [Installation page](../project-docs/sdk-full-installation.md) covers every supported platform, but this section should be enough to get up and running in most cases.

* Mac and Linux
* Alpine Linux
* Windows

On Mac and most Linux distributions, simply use `pecl` to install the Couchbase PHP SDK.

```console
$ pecl install couchbase
```

**Alpine Linux** is very slim and uses `musl libc` and the `apk` package manager. As a result, the installation is a little different from other Unix-Like systems and `pecl` equivalent packages are used instead.

```console
$ apk add php81-pecl-couchbase
```

Windows downloads and instructions for the PHP SDK are available from [the installation page](../project-docs/sdk-full-installation.md#installing-on-microsoft-windows).

Make sure to add the extension details to your `php.ini`. See [post-installation instructions](../project-docs/sdk-full-installation.md#post-installation) for full details:

```ini
extension=couchbase
```

Additionally, if you are using [Composer](https://getcomposer.org/doc/00-intro.md), simply update your `composer.json` file with the following dependencies:

```json
"require": {
  ...
  "ext-couchbase": "^4.2",
  "couchbase/couchbase": "^4.2"
}
```

And run the `composer update` command. If there are any problems, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

|  | Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to database resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* [Couchbase Server](../../../server/7.6/getting-started/do-a-quick-install.md) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

|  | Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#step-by-step)Step-by-step

Start a new project (in VS Code or PhpStorm, etc.) and create a file `cb-test.php`.

Go to our [Platform Introduction](platform-help.md) if you don’t already have an editor or IDE setup for working with PHP — e.g. you are evaluating the PHP SDK, but it is not your normal platform.

Install the latest 4.x [couchbase](https://pecl.php.net/package/couchbase) SDK package — see [above](#quick-installation).

Firstly, you will need to have a few `import` statements at the top of your PHP program:

```php
// NOTE: Change the below vendor path to your own.
require_once '../../../vendor/autoload.php';

use Couchbase\ClusterOptions;
use Couchbase\Cluster;
```

### [](#connect)Connect

Connect to your cluster by instantiating a new `Cluster` object and pass it your connection details. The basic connection details that you’ll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Couchbase Capella
* Local Couchbase Server

From version 4.0, the PHP SDK includes Capella’s standard certificates by default, so you do not need to additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```php
// Update these credentials for your Capella instance!
$connectionString = "couchbases://cb.<your-instance>.cloud.couchbase.com";
$options = new ClusterOptions();

$options->credentials("username", "Password!123");
// Sets a pre-configured profile called "wan_development" to help avoid latency issues
// when accessing Capella from a different Wide Area Network
// or Availability Zone (e.g. your laptop).
$options->applyProfile("wan_development");
$cluster = new Cluster($connectionString, $options);
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 4.1 introduces a `wan_development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

|  | The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```php
// Update these credentials for your Local instance!
$connectionString = "couchbase://localhost";
$options = new ClusterOptions();

$options->credentials("Administrator", "password");
$cluster = new Cluster($connectionString, $options);
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

```php
// get a bucket reference
$bucket = $cluster->bucket("travel-sample");
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

Collections allow Documents to be grouped by purpose or theme, according to specified _Scope_. Our Travel Sample bucket has separate scopes for inventory (flights, etc.), and for tenants (different travel agents).

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```php
// get a user-defined collection reference
$scope = $bucket->scope("tenant_agent_00");
$collection = $scope->collection("users");
```

[Data operations](../howtos/kv-operations.md), like storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection→get()` and `Collection→upsert()`.

Add the following code to create a new document and retrieve it:

```php
$upsertResult = $collection->upsert("my-document-key", ["name" => "Ted", "Age" => 31]);

$getResult = $collection->get("my-document-key");

print_r($getResult->content());
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster→query()` or `Scope→query()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```php
$inventoryScope = $bucket->scope("inventory");
$queryResult = $inventoryScope->query("SELECT * FROM airline WHERE id = 10");

// Print result data to the terminal.
foreach ($queryResult->rows() as $row) {
    print_r($row);
}
```

You can learn more about SQL++ queries on the [Query](../howtos/n1ql-queries-with-sdk.md) page.

## [](#next-steps)Next Steps

Now you’re up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL-based SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and can be found [here](http://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

[The Migrating to SDK API 3 page](../project-docs/migrating-sdk-code-to-3.n.md) highlights the main differences to be aware of when migrating your code.

Couchbase welcomes community contributions to the PHP SDK. The PHP SDK source code is available on [GitHub](https://github.com/couchbase/php-couchbase).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you’re running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/php-sdk/8) is a great source of help.