---
title: Performing Searches
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-perform-searches.adoc
  xref: xref:7.2@server:fts:fts-perform-searches.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-perform-searches.html)

# Performing Searches

Full text searches can be performed with:

* The Couchbase Web Console. This UI can also be used to create indexes and analyzers. Refer to [Searching from the UI](fts-searching-from-the-UI.md) for information.
* The Couchbase REST API. Refer to [Searching with the REST API](fts-searching-with-curl-http-requests.md) for information. Refer also to [Full Text Search API](../rest-api/rest-fts.md) for REST reference details.
* The Couchbase SDK. This supports several languages, and allows full text searches to be performed with each. Refer to the SDK's [Full Text Search](../../../java-sdk/current/concept-docs/full-text-search-overview.md) page for information.

> [!NOTE]
> The [Searching from the SDK](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md) page for the _Java_ SDK provides an extensive code-example that demonstrates multiple options for performing full text searches.

* The SQL++ Search functions. These enable you to perform a full text search as part of a SQL++ query. Refer to [Search Functions](../n1ql/n1ql-language-reference/searchfun.md) for information.