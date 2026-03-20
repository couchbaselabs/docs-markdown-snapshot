---
title: Handling Errors
description: Practical steps to handle errors and exceptions.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:php-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/howtos/error-handling.html)

# Handling Errors

> Practical steps to handle errors and exceptions. 

Errors are inevitable. The developer’s job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#how-the-sdk-handles-errors)How the SDK Handles Errors

Couchbase-specific exceptions are all derived from `\Couchbase\BaseException`. Errors that cannot be recovered by the SDK will be returned to the application. These unrecoverable errors are left to the application developer to handle — this section covers handling many of the common error scenarios.

The approach will depend upon the type of error thrown. Is it transient? Is it even recoverable? Below we examine error handling strategies in relation to the Couchbase SDKs, then take a practical walk through some common error scenarios you are likely to have to handle when working with a Couchbase cluster.

### [](#logging)Logging

It is always important to log errors, but even more so with highly concurrent asynchronous applications.

See the logging page for more details: [Logging](collecting-information-and-logging.md)

### [](#retry)Retry

Transient errors — such as those caused by resource starvation — are best tackled with one of the following retry strategies:

* Retry immediately.
* Retry with a fixed delay.
* Retry with a linearly increasing delay.
* Retry with an exponentially increasing delay.
* Retry with a random delay.

```php
$max_attempts = 5;
for ($attempt = 1; $attempt <= $max_attempts; $attempt++) {
    printf("Attempt $attempt. \n");
    try {
        $result = $collection->get("expected-document");
        break;
    }
    catch (\Couchbase\Exception\DocumentNotFoundException $ex) {
        printf("Document still not created. \n");
        usleep(100);
        continue;
    }
    catch (\Couchbase\NetworkException $ex) {
      printf("An unrecoverable network exception happened! \n");
      break;
    }
}
```

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common errors that can be encountered — both during development, and to be handled by the production app. Here we will cover some of the most common errors.

### [](#key-does-not-exist)Key does not exist

If a particular key cannot be found it is raised as a `DocumentNotFoundException`:

```php
try {
    $collection->get("foo");
} catch (\Couchbase\Exception\DocumentNotFoundException $ex) {
    printf("Document does not exist, creating. \n");
    $collection->upsert("foo", ["bar" => 42]);
}
```

### [](#key-already-exists)Key already exists

On the other hand if the key already exists and should not (e.g. on an insert) then it is raised as a `KeyExistsException`:

```php
try {
    $collection->insert("foo", ["bar" => 43]);
} catch (\Couchbase\KeyExistsException $ex) {
    printf("Document already exists. \n");
}
```

### [](#document-body-too-large)Document body too large

```php
try {
    $collection->insert("big", $big_object);
} catch (\Couchbase\ValueTooBigException $ex) {
    printf("Document is bigger than maximum size (20MB). \n");
}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using CAS. Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value, and when replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns `CasMismatchException`, and the most appropriate response is to simply retry:

```php
$result1 = $collection->get("foo");
$original_cas = $result1->cas();

$opts = new \Couchbase\ReplaceOptions();

$result2 = $collection->replace("foo",
                                ["bar" => 44],
                                $opts->cas($original_cas));
$updated_cas = $result2->cas();

try {
    $collection->replace("foo",
                         ["bar" => 45],
                         $opts->cas($original_cas));
                         # oops, we should have used $updated_cas!
} catch (\Couchbase\Exception\CasMismatchException $ex) {
    printf("CAS mismatch error. \n");
}
```