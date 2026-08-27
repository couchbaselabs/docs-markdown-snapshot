---
title: Zero Downtime Index Upgrades
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-high-availability-for-search-zero-downtime-index-upgrades.adoc
  xref: xref:7.6@server:fts:fts-high-availability-for-search-zero-downtime-index-upgrades.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-high-availability-for-search-zero-downtime-index-upgrades.html)

# Zero Downtime Index Upgrades

Users can update/recreate/rebuild the indexes without interfering with the live systems by leveraging the index-alias feature. The index aliases permit indirection in the index naming, whereby applications refer to an alias-name that never changes, leaving administrators free to change the identity of the real index pointed to by the alias. This may be particularly useful when an index needs to be updated: to avoid downtime, while the current index remains in service, a clone of the current index can be created, modified, and tested. Then, when the clone is ready, the existing alias can be retargeted so that the clone becomes the current index; and the (now) previous index can be removed.