[View original HTML](/nodejs-sdk/4.4/howtos/concurrent-async-apis.html)

> The Couchbase Node.js SDK allows the use, and mixing, of two distinct forms of result handling. 

The Node.js SDK provides two APIs, which can be freely mixed:

* A simple promises approach, available in the newest editions of Javascript.
* A standard callback based approach, typical of Node.js.

## [](#using-the-promises-api)Using the Promises API

This is the simplest API, in which all operations can be directly waited upon. A simple upsert example looks like this:

```javascript
const result = await collection.get(key);
document = result.value;
```

Methods will return a Javascript 'Promise' object, which can be chained, joined or handled.

An example of performing a couple of operations simultanously with the Promises API looks like this:

```javascript
var results = await Promise.all([
    collection.get(key),
    collection.get('airport_1254')
]);
```

## [](#using-the-callback-api)Using the Callback API

In addition to the Promises approach, we also simultaneously support the standard callback approach which is well known. A simple get example looks like this:

```javascript
collection.get(key,
    (err, res) => {
        if (err) console.log(err);
        if (res) {
            console.log(res);
            resolve(res);
        };
    }
);
```

## [](#batching)Batching

As Node.js inherently performs all operations in an asynchronous manner, no special implementation is required in order to enable batching. Simply perform a number of operations simultaenously and they will be batched on the network. This happens internally and is highly efficient.

Note that this behaviour extends to the world of async/await, such that following would be automatically batched across the network:

```javascript
[res0, res1] = await Promise.all([
    collection.get(key),
    collection.get('airport_1254')
]);
```

## [](#choosing-an-api)Choosing an API

So which API should you choose?

It’s really down to you and the needs of your application. If you’re already writing code using promises, then it makes sense to continue that way. If you working with a legacy application which is still using the standard callback approach, it may make sense to continue using callbacks.