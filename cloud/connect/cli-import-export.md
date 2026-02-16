[View original HTML](/cloud/connect/cli-import-export.html)

> Use Couchbase command line tools to import and export large amounts of data. 

You can use the `cbimport` and `cbexport` command line tools included with Couchbase Server with a Couchbase Capella cluster. The command line tools are available as a separate package.

Couchbase command line tools for Capella include [cbimport](../../server/current/tools/cbimport.md) and [cbexport](../../server/current/tools/cbexport.md).

* Use `cbimport` to import large datasets and multiple files at once, up to the maximum size of your Capella cluster.
* Use `cbexport` to export data from your Capella cluster.

## [](#prerequisites)Prerequisites

The procedures on this page assume the following:

* You have [configured cluster access](../clusters/manage-database-users.md) by creating cluster access credentials. You’ll need the username and password for the cluster credentials to connect to the cluster.
* You have [added your IP address](../clusters/allow-ip-address.md) to the cluster’s list of allowed IPs.
* You have [downloaded your security certificate](../get-started/create-account.md#next-steps) for your cluster.
* You have [downloaded and installed](../reference/command-line-tools.md) the command line tools package.

## [](#import-data)Import Data

1. Go to **Connect** **Import & Export Tools**.
2. Copy the command under **cbimport**.
3. Replace `username` and `password` with the username and password of your cluster access credentials respectively.
4. Update `bucketname` with the name of your bucket.
5. Update dataset with the `path to the dataset file`.
6. Set the `cacert` to point to the downloaded CA cert.

|  | You can also import from JSON. See the [examples](#import-json) for more details. |
|  | --------------------------------------------------------------------------------- |

## [](#export-data)Export Data

1. Copy the command under **cbexport**.
2. Replace `username` and `password` with the username and password of your cluster access credentials respectively.
3. Update the path to the location where you want to create your JSON file export.
4. Update `bucketname`, `scope`, `collection`, and the `collection_field` with the name of your bucket, scope, and collection.
5. Set the `cacert` to point to the downloaded CA cert.

## [](#import-and-export-with-command-line-tools-examples)Import and Export with Command Line Tools Examples

For production environments, use the secure `--cacert <cert_file>` option shown in the examples. For development environments, replace `--cacert <cert_file>` with `--no-ssl-verify`.

For more information, see the Couchbase Server documentation for [cbimport](../../server/current/tools/cbimport.md) and [cbexport](../../server/current/tools/cbexport.md).

### [](#cbimport)cbimport

#### [](#import-from-csv)Import from CSV

Use the `cbimport csv` command to import data into your Capella cluster from a CSV file:

```console
$ cbimport csv --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --bucket mybucket1 --dataset file:///home/someuser/test_records.csv --generate-key '#UUID#' --infer-types --cacert /root/capella.pem --threads 4
```

#### [](#import-json)Import from JSON

Use the `cbimport json` command to import data into your Capella cluster from a JSON file:

```console
$ cbimport json --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --bucket mybucket1 --dataset file://./profile_docs.json --format lines --generate-key %profile_id% --cacert /root/capella.pem --threads 4
```

In this example, the `travel-sample-export.json` was created with the [cbexport](#cbexport) example.

```console
$ cbimport json --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --bucket mytravelsample --dataset file://./travel-sample-export.json --scope-collection-exp %myscopefield%.%mycollectionfield% --format lines --generate-key %doc_key% --ignore-fields doc_key,myscopefield,mycollectionfield --cacert /root/capella.pem
```

### [](#cbexport)cbexport

Use the `cbexport json` command to export JSON documents from your Capella cluster.

```console
$ cbexport json --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --bucket travel-sample --format lines --output  /home/someuser/travel-sample-export.json --scope-field myscopefield --collection-field mycollectionfield --include-key doc_key --cacert /root/capella.pem
```