---
title: Batching
description: The PHP SDK offers only a blocking API -- but this is not
  necessarily a limitation.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.2/howtos/concurrent-async-apis.html)

# Batching

> The PHP SDK offers only a blocking API — but this is not necessarily a limitation. Using process forks we can perform effective bulk operations over data. 

Process forks give an improvement in performance — but at the cost of increased use of CPU and memory. Note, they do not help improve network efficiency, but will be no worse than making individual calls.

## [](#batching-with-process-forks)Batching with process forks

Bulk loading with multiple PHP processes provides a useful way of achieving the effectiveness of parallel operations. In the following example we will look at loading a set of JSON files and uploading them to Couchbase Server in concurrent batches.

To begin with, let’s look at loading the data from one of the Couchbase sample datasets, the beer dataset. This dataset is around 7300 JSON files, each file representing a document. This sample looks for the dataset in the default location for a GNU/Linux install, you can find the default locations for other Operating Systems in our [CLI reference](#https://docs.couchbase.com/server/7.1/cli/cli-intro.html).

```php
$concurrency = 4; // number of processes
$sample_name = "beer-sample";
$sample_zipball = "/opt/couchbase/samples/$sample_name.zip";
printf("Using '%s' as input\n", $sample_zipball);
system("rm -rf /tmp/$sample_name");
system("unzip -q -d /tmp $sample_zipball");
$files = glob("/tmp/$sample_name/docs/*.json");
$batches = [];
for ($i = 0; $i < $concurrency; $i++) {
  $batches[$i] = [];
}
printf("Bundle '%s' contains %d files\n", $sample_name, count($files));
for ($i = 0; $i < count($files); $i++) {
  array_push($batches[$i % $concurrency], $files[$i]);
}
```

Here we’ve unzipped the zip file containing the dataset and then set up the relevant number of batches, where each batch is a set of filenames that we will later read and use the documents from.

In the next snippet we can see that call `pcntl_fork` to fork the process. After forking the process we check if we’re now running as a child or as the parent process. If we’re running as the child then we run the `upload_batch` function. The `upload_batch` function iterates over the filenames, reading the contents of each file and uploading it to Couchbase Server. If we were in the parent process then instead of running the `upload_batch` function we add the PID of the child process to the `$children` array. The parent then uses `pcntl_waitpid` to wait for each child process to complete.

```php
$children = [];
for ($i = 0; $i < $concurrency; $i++) {
  $pid = pcntl_fork();
  if ($pid == -1) {
    die("unable to spawn child process");
  } else if ($pid == 0) {
    printf("Start a process to upload a batch of %d files\n", count($batches[$i]));
    upload_batch($i, $batches[$i]);
    exit(0);
  } else {
    array_push($children, $pid);
  }
}

foreach ($children as $child) {
  pcntl_waitpid($child, $status);
}

use \Couchbase\Cluster;
use \Couchbase\ClusterOptions;
function upload_batch($id, $batch) {
  $options = new ClusterOptions();
  $options->credentials("Administrator", "password");
  $cluster = new Cluster("couchbase://localhost", $options);
  $collection = $cluster->bucket("travel-sample")->scope("inventory")->collection("airport");
  foreach ($batch as $path) {
    $collection->upsert($path, json_decode(file_get_contents($path)));
  }
}
```

In the output we can see something like:

```console
Bundle 'beer-sample' contains 7303 files
Start a process to upload a batch of 1826 files
Start a process to upload a batch of 1826 files
Start a process to upload a batch of 1826 files
Start a process to upload a batch of 1825 files
```

The application has split the files into four batches and then uploaded the batches in parallel.