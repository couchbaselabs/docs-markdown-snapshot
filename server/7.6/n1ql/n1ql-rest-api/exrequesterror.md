---
title: Request Error
description: A request error happens when there is a problem with the REST
  request itself, e.g. missing a required parameter.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/n1ql/pages/n1ql-rest-api/exrequesterror.adoc
  xref: xref:7.6@server:n1ql:n1ql-rest-api/exrequesterror.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-rest-api/exrequesterror.html)

# Request Error

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

A request error happens when there is a problem with the REST request itself, e.g. missing a required parameter.

Request

```sh
curl -v http://localhost:8093/query/service
```

Response

```json
{
  "requestID": "424c0a6d-b851-4feb-892c-0d9a106f2e13",
  "errors": [
    {
      "code": 1050,
      "msg": "No statement or prepared value"
    }
  ],
  "status": "fatal",
  "metrics": {
    "elapsedTime": "1.124637ms",
    "executionTime": "1.094663ms",
    "resultCount": 0,
    "resultSize": 0,
    "serviceLoad": 0,
    "errorCount": 1
  }
}
```