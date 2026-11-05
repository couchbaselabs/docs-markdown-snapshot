---
title: Service Error
description: "A service error means there is a problem that prevents the request
  being fulfilled:"
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/n1ql/pages/n1ql-rest-api/exserviceerror.adoc
  xref: xref:7.6@server:n1ql:n1ql-rest-api/exserviceerror.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-rest-api/exserviceerror.html)

# Service Error

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

A service error means there is a problem that prevents the request being fulfilled:

Request

```sh
curl -v http://localhost:8093/query/service \
     -d "statement=SELECT text FROM tweets LIMIT 1"
```

Response

```console
     $lt; HTTP/1.1 503 Service Unavailable
     {
     "requestID": "5c0a6a81-2fc8-4a33-a035-ed7fb1512710",
     "errors": [
     {
     "code": <int>,
     "msg": "Request queue full"
     }],
     "status": "errors",
     "metrics": {
     "elapsedTime": "134.7944us",
     "executionTime": "130.5518us",
     "resultCount": 0,
     "resultSize": 0,
     "mutationCount": 0,
     "errorCount": 1,
     "warningCount": 0
     }
     }
     $
```