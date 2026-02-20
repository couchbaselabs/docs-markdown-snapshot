---
title: Zero Downtime Index Upgrades
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-high-availability-for-search-zero-downtime-index-upgrades.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:fts:fts-high-availability-for-search-zero-downtime-index-upgrades.adoc[]
---

[View original HTML](/server/current/fts/fts-high-availability-for-search-zero-downtime-index-upgrades.html)

# Zero Downtime Index Upgrades

Users can update/recreate/rebuild the indexes without interfering with the live systems by leveraging the index-alias feature. The index aliases permit indirection in the index naming, whereby applications refer to an alias-name that never changes, leaving administrators free to change the identity of the real index pointed to by the alias. This may be particularly useful when an index needs to be updated: to avoid downtime, while the current index remains in service, a clone of the current index can be created, modified, and tested. Then, when the clone is ready, the existing alias can be retargeted so that the clone becomes the current index; and the (now) previous index can be removed.