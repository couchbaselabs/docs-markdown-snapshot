---
title: Async APIs
description: The Couchbase C&#43;&#43; SDK allows the use, and mixing, of two
  asynchronous APIs.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.0@cxx-sdk:howtos:concurrent-async-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.0/howtos/concurrent-async-apis.html)

# Async APIs

> The Couchbase C++ SDK allows the use, and mixing, of two asynchronous APIs. 

The C++ SDK provides two asynchronous APIs, which can be freely mixed:

* A future-based one, that returns a `std::future`
* A callback-based one, that takes a `std::function`

## [](#using-the-future-based-api)Using the future-based API

The future-based API returns a C++ `std::future<T>`, representing the execution of an asynchronous task and the promise of a future result.

Here’s what a simple upsert looks like, fetching the result with `std::future<T>::get()`:

```c++
auto content = tao::json::value{
        { "foo", "bar" },
        { "baz", "qux" },
};

// The .get() call returns the result from the std::future<std::pair<couchbase::error, couchbase::mutation_result>>
auto [err, res] = collection.upsert("document-key", content).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Success");
}
```

## [](#using-the-callback-based-api)Using the callback-based API

The callback-based API takes a `std::function<T>`, containing the result of the operation once it becomes available.

Here is what a simple upsert looks like, using the callback-based API:

```c++
auto content = tao::json::value{
        { "foo", "bar" },
        { "baz", "qux" },
};
collection.upsert("document-key", content, {}, [](auto err, auto res) {
    if (err) {
        fmt::println("Error: {}", err);
    } else {
        // Can easily 'chain' another operation here. e.g. get the document we just upserted.
        fmt::println("Success");
    }
});
```

## [](#choosing-an-api)Choosing an API

So which API should you choose?

It’s really down to you and the needs of your application. If you’re already writing code using callbacks then it may make sense to continue that way. The callback-based API provides an easy and intuitive way to chain operations together, whereas the future-based API provides a clean and modern way to access results of asynchronous operations. And you can use different APIs at different times.