---
title: Request Error
description: A request error happens when there is a problem with the REST
  request itself, e.g. missing a required parameter.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/n1ql/pages/n1ql-rest-api/exrequesterror.adoc
  xref: xref:7.6@server:n1ql:n1ql-rest-api/exrequesterror.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-rest-api/exrequesterror.html)

# Request Error

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