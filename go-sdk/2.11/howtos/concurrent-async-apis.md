---
title: Async and Batching APIs
description: The Go SDK offers a synchronous blocking interface but this does
  not stop you from using it asynchronously, or from performing bulk operations
  concurrently.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.11@go-sdk:howtos:concurrent-async-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/howtos/concurrent-async-apis.html)

# Async and Batching APIs

> The Go SDK offers a synchronous blocking interface but this does not stop you from using it asynchronously, or from performing bulk operations concurrently. By using goroutines you can call into the SDK aynchronously and by using the `BulkOp` API you can batch multiple operations into a single SDK call which executes concurrently behind the scenes. 

## [](#goroutines)Goroutines

The Go SDK is designed to be highly performant when used across numerous goroutines, this allows you to start numerous asynchronous goroutines which can all perform operations on the same SDK objects. Using goroutines to perform parallel operations against the SDK means that you can continue to call into the SDK via the standard API and you have all of the operation features available, such as durability.

In the following examples we’ll look at loading the data from one of the Couchbase sample datasets, the beer dataset. This dataset is around 7300 JSON files, each file representing a document. This sample looks for the dataset in the default location for a Linux install, you can find the default locations for other operation systems in our [CLI reference](#https://docs.couchbase.com/server/7.1/cli/cli-intro.html).

First we need to connect to the server and create a cluster object:

```golang
	opts := gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: "Administrator",
			Password: "password",
		},
	}
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}

	bucket := cluster.Bucket("travel-sample")
	collection := bucket.Scope("inventory").Collection("airport")

	// We wait until the bucket is connected and setup.
	err = bucket.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		panic(err)
	}
```

Once we have that in place then we can set up our goroutines. We’re using 24 goroutines so we can do up to 24 concurrent upsert operations. The `workChan` is used by the main goroutine to send documents to the "worker" goroutines which will perform the upserts. When all of the work is done and the `workChan` is exhausted the main goroutine will send on the `shutdownChan` before waiting for the `wg` `sync.WaitGroup` to complete. This allows us to wait for any work being performed in a "worker" to fully complete so we don’t accidentally drop any upserts.

Here we can see setting up the goroutines ready to receive any work:

```golang
	type docType struct {
		Name string
		Data interface{}
	}
	concurrency := 24 // number of goroutines
	workChan := make(chan docType, concurrency)
	shutdownChan := make(chan struct{}, concurrency)
	var wg sync.WaitGroup

	wg.Add(concurrency)
	for i := 0; i < concurrency; i++ {
		go func() {
			for {
				select {
				case doc := <-workChan:
					_, err := collection.Upsert(doc.Name, doc.Data, nil)
					if err != nil {
						// We could use errgroup or something to error out nicely here.
						log.Println(err)
					}
				case <-shutdownChan:
					wg.Done()
					return
				}
			}
		}()
	}
```

Once those are setup we can start loading up our JSON files and sending them to our workers:

```golang
	sampleName := "beer-sample"
	sampleZip := fmt.Sprintf("/opt/couchbase/samples/%s.zip", sampleName)

	r, err := zip.OpenReader(sampleZip)
	if err != nil {
		panic(err)
	}
	defer r.Close()

	for _, f := range r.File {
		// We only want json files from the docs directory.
		if f.FileInfo().IsDir() || !(strings.HasPrefix(f.Name, sampleName+"/docs/") &&
			strings.HasSuffix(f.Name, ".json")) {
			continue
		}

		fileReader, err := f.Open()
		if err != nil {
			panic(err)
		}

		fileContent, err := ioutil.ReadAll(fileReader)
		if err != nil {
			fileReader.Close()
			panic(err)
		}
		fileReader.Close()

		var docContent interface{}
		err = json.Unmarshal(fileContent, &docContent)
		if err != nil {
			panic(err)
		}

		workChan <- docType{
			Name: f.Name,
			Data: docContent,
		}
	}
```

Finally we wait for the `workChan` to empty and then wait for the "workers" to complete:

```golang
	// Wait for all of the docs to be uploaded.
	for len(workChan) > 0 {
		time.Sleep(100 * time.Millisecond)
	}
	// Signal the goroutines to close, this means that we can wait for them to complete any work that they're doing
	// before we actually finish.
	for i := 0; i < concurrency; i++ {
		shutdownChan <- struct{}{}
	}
	wg.Wait()
	cluster.Close(nil)
	log.Println("Completed")
```

## [](#bulk-operations-api)Bulk Operations API

Batching operations allows you to make better utilization of your network and speed up your application by increasing network throughput and reducing latency. Batched operations work by pipelining requests over the network. When requests are pipelined, they are sent in one large group to the cluster. The cluster in turn pipelines responses back to the client. When operations are batched, there are fewer IP packets to be sent over the network (since there are fewer individual TCP segments).

The bulk operations API allows you to send a batch of operations to the server in one SDK call. The SDK sends all of these operations sequentially but does not wait for responses between sending each request; e.g. rather than the typical request-response, request-response pattern that you might be used to, behind the scenes the SDK will do request, request, request — response, response, reponse. From your point of view as the user of the SDK this single SDK call will just be a normal blocking call. As well as the performance benefits of being able to pipeline another main tradeoff between using the bulk operations API and using goroutines is that of complexity (of handling channels and goroutines) against available operation options. The bulk API does not expose options per operation like the standard API, nor does it support features like durability.

Using the same example as before (we’ll skip the connecting code as that’s the same) we’ll see that in the following examples we batch up the documents and then send them sequentially via the bulk API.

Here we can see that we create a map containing 8 batches of documents which we populate instead of sending on a channel:

```golang
	numBatches := 8 // number of batches
	type docType struct {
		Name string
		Data interface{}
	}
	sampleName := "beer-sample"
	sampleZip := fmt.Sprintf("/opt/couchbase/samples/%s.zip", sampleName)
	batches := make(map[int][]gocb.BulkOp)
	var numDocs int

	r, err := zip.OpenReader(sampleZip)
	if err != nil {
		panic(err)
	}
	defer r.Close()

	for i, f := range r.File {
		// We only want json files from the docs directory.
		if f.FileInfo().IsDir() || !(strings.HasPrefix(f.Name, sampleName+"/docs/") &&
			strings.HasSuffix(f.Name, ".json")) {
			continue
		}

		fileReader, err := f.Open()
		if err != nil {
			panic(err)
		}
		defer fileReader.Close()

		fileContent, err := ioutil.ReadAll(fileReader)
		if err != nil {
			panic(err)
		}

		var docContent interface{}
		err = json.Unmarshal(fileContent, &docContent)
		if err != nil {
			panic(err)
		}

		_, ok := batches[i%numBatches]
		if !ok {
			batches[i%numBatches] = []gocb.BulkOp{}
		}
		batches[i%numBatches] = append(batches[i%numBatches], &gocb.UpsertOp{
			ID:    f.Name,
			Value: docContent,
		})
		numDocs++
	}
	log.Printf("Loaded %d docs\n", numDocs)
```

Once we’ve built up our batches we can send them via the `collection.Do` interface. We don’t need to wait for anything to finish in this example because we’ve used the blocking API. Note that we’re checking each individual operation for errors as well as the call to `Do`, this is because individual operations can either succeed or fail.

```golang
	for _, batch := range batches {
		err := collection.Do(batch, nil)
		if err != nil {
			log.Println(err)
		}

		// Be sure to check each individual operation for errors too.
		for _, op := range batch {
			upsertOp := op.(*gocb.UpsertOp)
			if upsertOp.Err != nil {
				log.Println(err)
			}
		}
	}

	cluster.Close(nil)
	log.Println("Completed")
```

### [](#batching-guidelines)Batching guidelines

Batching improves network utilization. However there is a batching threshold at which the maximum network efficiency is gained — and batching beyond this amount will simply increase memory and CPU usage on the client, and in some cases cause operations to prematurely time-out or otherwise fail.

As a guideline, applications should batch no more than 1MB before sending to the server. Calculating the 1 MB value is dependent on the length of the key and value (where applicable) of each operation.

Note that this is just a guideline. The limit may be higher for extremely efficient networks (such as 10-gigabit Ethernet). It is recommended you benchmark your network to get ideal performance numbers. The limit may be lower for congested networks or slow server nodes (for example, a shared development VM with low resources).

The \[cbc-pillowfight\] utility may be used to appropriately determine the correct batch size for a cluster.

When calculating the batch size, also consider that each operation has a 24 byte overhead at the protocol level:

### [](#sizing-batches-examples)Sizing batches: examples

When storing items, with each key being approximately 10 bytes long and each value being approximately 4000 bytes long, estimate the following:

1. Calculate Bytes per operation:

  * 10 (Key)
  * 4000 (Value)
  * 24 (Memcached Packet)
  * Total: 4034.
2. Divide 1 megabyte by the total size of an operation:

  * 1048576 / 4034
  * Batch Size: 259

The 24 byte overhead becomes more evident when dealing with smaller values. Assuming an average key size of 5 and an average value size of 50:

1. Calculate bytes per operation:

  * 5 (Key)
  * 50 (value)
  * 24 (Packet)
  * Total: 74
2. Divide 1 megabyte by the total size of an operation:

  * Batch Size: 14169

## [](#limitations)Limitations

Both of these approaches have the same limitation - the dispatch queue size. This is the limit of the number of operations (the bulk API treats each `BulkOp` as 1 operation, rather than each call to `Do`) that can be queued up waiting to send to Couchbase Server at any time. If your batches are too big or you are concurrently sending too many requests at a time then the queue can overload, which can be checked for using `IsQueueOverloadError(err)`. If this occurs then you could try using more, smaller batches or adding failed ops to a new batch and repeatedly doing that until none have failed.