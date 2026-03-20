---
title: Searching Securely Using SSL
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-secure-fts-queries.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-secure-fts-queries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-secure-fts-queries.html)

# Searching Securely Using SSL

To securely query data from the FTS service, the user must follow these steps:

1. Provide the username and password (-u).
2. Use https protocol.
3. Specify the IP address of the server hosting the FTS service - <ip>.
4. Specify the SSL port (18094).

**Example**

```console
curl -u username:password -XPOST -H "Content-Type: application/json" \
https://<ip>:18094/api/index/travel-sample-index/query \
-d '{
        "explain": true,
        "fields": [" * "],
        "highlight": {},
        "query": {
                    "query": "{ \"+nice +view\" }"
                 }
    }'
```

> [!NOTE]
> Ensure that the SSL ports are enabled in the cluster.