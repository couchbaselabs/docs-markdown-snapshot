---
title: Handling Errors
description: Errors are inevitable. The developer’s job is to be prepared for
  whatever is likely to come up
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.8/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@go-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.8/howtos/error-handling.html)

# Handling Errors

> Errors are inevitable. The developer's job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. 

Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#handling-errors)Handling Errors

The Go SDK works nicely with the [errors package](https://golang.org/pkg/errors/) to interrogate errors. Of course, you can also just log them and fail the operation.

You can use `errors.Is` as follows:

```golang
	_, err := collection.Get("does-not-exist", nil)
	if err != nil {
		if errors.Is(err, gocb.ErrDocumentNotFound) {
			fmt.Println("Document could not be found")
		} else {
			fmt.Printf("An unknown error occurred: %v", err)
		}
	}
```

You can, of course, just log or print out the error as usual and the SDK will try to include as much information as it can in the error message logged (via the usual `err.Error()`).

The type of operation will influence the type of the underlying error returned. The primary error types are listed below, this is not an exhaustive list of the Go SDK error types.

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common errors that can be encountered - both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found it is return as an `ErrDocumentNotFound`:

```golang
	doc := struct{ Foo string }{Foo: "baz"}
	_, err := collection.Replace("does-not-exist", doc, nil)
	if err != nil {
		if errors.Is(err, gocb.ErrDocumentNotFound) {
			fmt.Println("Key not be found")
		} else {
			fmt.Printf("An unknown error occurred: %v", err)
		}
	}
```

```golang
	_, err := collection.Get("does-not-exist", nil)
	if err != nil {
		if errors.Is(err, gocb.ErrDocumentNotFound) {
			fmt.Println("Document could not be found")
		} else {
			fmt.Printf("An unknown error occurred: %v", err)
		}
	}
```

On the other hand if the key already exists and should not (e.g. on an insert) then it is returned as a `ErrDocumentExists`:

```golang
	doc := struct{ Foo string }{Foo: "baz"}
	_, err := collection.Insert("does-already-exist", doc, nil)
	if err != nil {
		if errors.Is(err, gocb.ErrDocumentExists) {
			fmt.Println("Key already exists")
		} else {
			fmt.Printf("An unknown error occurred: %v", err)
		}
	}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using CAS. Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value, and when replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns `ErrCasMismatch`, and the most appropriate response is to simply retry it:

```golang
	var doOperation func(maxAttempts int) (*gocb.MutationResult, error)
	doOperation = func(maxAttempts int) (*gocb.MutationResult, error) {
		doc, err := collection.Get("doc", nil)
		if err != nil {
			return nil, err
		}

		result, err := collection.Replace("doc", newDoc, &gocb.ReplaceOptions{Cas: doc.Cas()})
		if err != nil {
			if errors.Is(err, gocb.ErrCasMismatch) {
				// Simply recursively retry until maxAttempts is hit
				if maxAttempts == 0 {
					return nil, err
				}
				return doOperation(maxAttempts - 1)
			} else {
				return nil, err
			}
		}

		return result, nil
	}
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. Take this as an example: your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application's connection to the server is lost. The client will timeout waiting for a response and will raise a `TimeoutException`, but it's ambiguous to the app whether the operation succeeded or not.

So `ErrTimeout` is one ambiguous error, another is `ErrDurabilityAmbiguous`, which can returned when performing a durable operation. This similarly indicates that the operation may or may not have succeeded: though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

Given the inevitability of ambiguity, how is the application supposed to handle this?

It really needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, for inserts, they can simply be retried to see if they fail on `ErrDocumentExists`, in which case the operation was successful:

```golang
	var doInsert func(docId string, doc []byte, maxAttempts int) (string, error)
	doInsert = func(docId string, doc []byte, maxAttempts int) (string, error) {
		_, err := collection.Insert(docId, doc, &gocb.InsertOptions{
			DurabilityLevel: gocb.DurabilityLevelMajority,
		})
		if err != nil {
			if errors.Is(err, gocb.ErrDocumentExists) {
				// The logic here is that if we failed to insert on the first attempt then
				// it's a true error, otherwise we retried due to an ambiguous error, and
				// it's ok to continue as the operation was actually successful.
				if maxAttempts == 0 {
					return "", err
				}

				return "ok!", nil
			} else if errors.Is(err, gocb.ErrDurabilityAmbiguous) {
				if maxAttempts == 0 {
					return "", err
				}

				return doInsert(docId, doc, maxAttempts-1)
			} else if errors.Is(err, gocb.ErrTimeout) {
				if maxAttempts == 0 {
					return "", err
				}

				return doInsert(docId, doc, maxAttempts-1)
			}

			return "", err
		}

		return "ok!", nil
	}
```

That example is much closer to what an application will want to be doing. Let's flesh it out further.

### [](#real-world-error-handling)Real-World Error Handling

The application can write wrappers so that it can easily do operations without having to duplicate the error handling each time. Something like this:

```golang
	var doInsertReal func(docId string, doc []byte, maxAttempts int, delay time.Duration) (string, error)
	doInsertReal = func(docId string, doc []byte, maxAttempts int, delay time.Duration) (string, error) {
		_, err := collection.Insert(docId, doc, &gocb.InsertOptions{DurabilityLevel: gocb.DurabilityLevelMajority})
		if err != nil {
			if errors.Is(err, gocb.ErrDocumentExists) {
				// The logic here is that if we failed to insert on the first attempt then
				// it's a true error, otherwise we retried due to an ambiguous error, and
				// it's ok to continue as the operation was actually successful.
				if maxAttempts == 0 {
					return "", err
				}

				return "ok!", nil
				// Ambiguous errors.  The operation may or may not have succeeded.  For inserts,
				// the insert can be retried, and a DocumentExistsException indicates it was
				// successful.
			} else if errors.Is(err, gocb.ErrDurabilityAmbiguous) || errors.Is(err, gocb.ErrTimeout) ||
				// Temporary/transient errors that are likely to be resolved
				// on a retry.
				errors.Is(err, gocb.ErrTemporaryFailure) || errors.Is(err, gocb.ErrDurableWriteInProgress) ||
				errors.Is(err, gocb.ErrDurableWriteReCommitInProgress) ||
				// These transient errors won't be returned on an insert, but can be used
				// when writing similar wrappers for other mutation operations.
				errors.Is(err, gocb.ErrCasMismatch) {
				if maxAttempts == 0 {
					return "", err
				}

				time.Sleep(delay)
				return doInsertReal(docId, doc, maxAttempts-1, delay*2)
			}

			return "", err
		}

		return "ok!", nil
	}
```

This will make a 'best effort' to do the insert (though its retry strategy is rather naive, and applications may want to implement a more sophisticated approach involving exponential backoff and circuit breaking.)

If that best effort fails, and the `doInsertReal` call still returns an error, then it's highly context-dependent how to handle that. Examples would include displaying a "please try again later" error to a user, if there is one, and logging it for manual human review. The application must make a suitable call for each case.

The application can write similar wrappers for the other operations - replace, upsert et al. Note that the logic is a little different in each case: for inserts, we confirm if the operation has already been successful on an ambiguous result by checking for `ErrDocumentExists`. But this wouldn't make sense for an upsert.

### [](#non-idempotent-operations)Non-Idempotent Operations

Idempotent operations are those that can be applied multiple times and only have one effect. Repeatedly setting an email field is idempotent - increasing a counter by one is not.

Some operations we can view as idempotent as they will fail with no effect after the first success - such as inserts.

Idempotent operations are much easier to handle, as on ambiguous error results (`ErrDurabilityAmbiguous` and `ErrTimeout`) the operation can simply be retried.

Most key-value operations are idempotent. For those that aren't, such as a Sub-Document `arrayAppend` call, or a counter increment, the application should, on an ambiguous result, first read the document to see if that change was applied.

## [](#query-and-analytics-errors)Query and Analytics Errors

A [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query either returns results or `QueryError`, like so:

```golang
	_, err := cluster.Query("select * from `someotherbucket`", nil)
	if err != nil {
		var queryErr *gocb.QueryError
		if errors.As(err, &queryErr) {
			fmt.Println(queryErr.ClientContextID) // the identifier for the query
			fmt.Println(queryErr.Endpoint)        // the http endpoint used for the query
			fmt.Println(queryErr.Statement)       // the query statement
			fmt.Println(queryErr.Errors)          // a list of errors codes + messages for why the query failed.
		}
	}
```

Analytics works in an identical fashion, raising an `AnalyticsError`.

## [](#cloud-native-gateway)Cloud Native Gateway

If you connect to the Kubernetes or OpenShift over our [CloudNative Gateway](managing-connections.md#cloud-native-gateway), using the new `couchbase2://` endpoints, there are a few changes in the error messages returned.

Some error codes are more generic — in cases where the client would not be expected to need to take specific action — but should cause no problem, unless you have written code looking at individual strings within the error messages.

## [](#additional-resources)Additional Resources

Errors & Exception handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Diagnostic methods are available to check on the [health of the cluster](health-check.md), and the [health of the network](tracing-from-the-sdk.md).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).

We have a [listing of error messages](../ref/error-codes.md), with some pointers to what to do when you encounter them.