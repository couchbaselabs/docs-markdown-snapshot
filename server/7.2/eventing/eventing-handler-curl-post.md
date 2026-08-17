---
title: "Function: Basic cURL POST"
description: Perform a simple cURL POST using an external REST endpoint.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-handler-curl-post.adoc
  xref: xref:7.2@server:eventing:eventing-handler-curl-post.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/eventing/eventing-handler-curl-post.html)

# Function: Basic cURL POST

**Goal**: Perform a simple cURL POST using an external REST endpoint.

* This function **basicCurlPost** communicates with a public REST echo service.
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Needs a Binding of type URL Alias (as documented in the Scriptlet).
* Will operate on any mutation of the KEY "make\_curl\_request::1".
* The actual cURL request from the Eventing Function will be equivalent to (but test to make sure the service is live):  
```shell  
curl -q 'https://postman-echo.com/post' -d '{ "myboolean": true }'  
```
* Only logs the REST response JSON payload to the Application log file.

* basicCurlPost
* Input Data/Mutation
* Output Data/Logged

```javascript
// To run configure the settings for this Function, basicCurlPost, as follows:
//
// Version 7.1+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
// Version 7.0+
//   "Listen to Location"
//     bulk.data.source
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...",   "URL...",                    "misc.",
//       "URL alias",    "curlEchoApi",     "https://postman-echo.com/", "no auth"
//
// Version 6.X
//   "Source Bucket"
//     source
//   "MetaData Bucket"
//     metadata
//   Binding(s)
//    1. "binding type", "alias name...",   "URL...",                    "misc.",
//       "URL alias",    "curlEchoApi",     "https://postman-echo.com/", "no auth"


function OnUpdate(doc, meta) {
    // You would typically filter to mutations of interest
    if (meta.id !== 'make_curl_request::1') return;
    try {
        // only make a cURL POST request we see a mutation on the above KEY
        var request = {
            path: 'post',   // can also do 'get' in this API
            body: {
                "myboolean": true
            }
        };
        //  perform the cURL request using the URL alias from the settings
        var response = curl('POST', curlEchoApi, request);
        if (response.status != 200 && response.status != 302) {
            log("cURL POST failed response.status:",response.status)
        } else {
            log("cURL POST success, response.body:",response.body)
            // optional write to a bucket - requires a binding alias in settings
            // note the response.body.json is the echo back of request.body
            // dst_col[meta.id] = response.body;
        }
    } catch (e) {
        log("cURL request had an exception:",e)
    }
}
```

```json
INPUT: KEY make_curl_request::1

{
  "anything": 1
}
```

```json
2021-07-18T19:37:35.596-07:00 [INFO] "cURL POST success, response.body:"
{
    "args": {},
    "data": {
        "myboolean": true
    },
    "files": {},
    "form": {},
    "headers": {
        "x-forwarded-proto": "https",
        "x-forwarded-port": "443",
        "host": "postman-echo.com",
        "x-amzn-trace-id": "Root=1-60f4e56f-2cfd45076d474c35198f8278",
        "content-length": "18",
        "user-agent": "libcurl/7.66.0-DEV couchbase/evt-7.0.0-0000-ee (eventing)",
        "accept": "*/*",
        "accept-encoding": "deflate, gzip",
        "content-type": "application/json"
    },
    "json": {
        "myboolean": true
    },
    "url": "https://postman-echo.com/post"
}
```