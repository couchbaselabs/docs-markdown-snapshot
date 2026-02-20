---
title: DocID with regexp in Type Mappings
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-Docid-with-regexp.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-type-mappings-Docid-with-regexp.adoc[]
---

[View original HTML](/server/7.2/fts/fts-type-mappings-Docid-with-regexp.html)

# DocID with regexp in Type Mappings

“Doc ID with regexp” is another way the search service allows the user to extract “type identifiers” for indexing.

* Set up a valid regular expression within docid\_regexp. Remember this will be applied on the document IDs.
* Choose a type mapping name that is considered a match for the regexp.
* The type mapping name CANNOT be a regexp.

For example, while working with the `travel-sample` bucket, set up docid\_regexp to `air[a-z]{4}` and use the following type mappings. \* airline \* airport

Below is a full index definition using it. { "name": "airline-airport-index", "type": "fulltext-index", "params": { "doc\_config": { "docid\_prefix\_delim": "", "docid\_regexp": "air\[a-z\]{4}", "mode": "docid\_regexp", "type\_field": "type" }, "mapping": { "default\_analyzer": "standard", "default\_datetime\_parser": "dateTimeOptional", "default\_field": "\_all", "default\_mapping": { "dynamic": true, "enabled": false }, "default\_type": "\_default", "docvalues\_dynamic": false, "index\_dynamic": true, "store\_dynamic": false, "type\_field": "\_type", "types": { "airline": { "dynamic": true, "enabled": true }, "airport": { "dynamic": true, "enabled": true } } }, "store": { "indexType": "scorch", "segmentVersion": 15 } }, "sourceType": "gocbcore", "sourceName": "travel-sample", "sourceParams": {}, "planParams": { "indexPartitions": 1 } }

So setting this as the index definition would index all attributes of documents with “airline” or "airport" in its document IDs.

![fts type mapping regexp with docid](_images/fts-type-mapping-regexp-with-docid.png) 

Note: The golang regexp support is based on [Access the github link](#https://github.com/google/re2/wiki/Syntax)