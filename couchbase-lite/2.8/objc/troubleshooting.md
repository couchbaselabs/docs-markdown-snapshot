---
title: Troubleshooting
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/troubleshooting.adoc
  xref: xref:2.8@couchbase-lite:objc:troubleshooting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/troubleshooting.html)

# Troubleshooting

## [](#replication-issues)Replication Issues

As always, when there is a problem with replication, logging is your friend. The following example increases the log output for activity related to replication with Sync Gateway.

```objc
// Replicator
[CBLDatabase setLogLevel:kCBLLogLevelVerbose domain:kCBLLogDomainReplicator];
// Network
[CBLDatabase setLogLevel:kCBLLogLevelVerbose domain:kCBLLogDomainNetwork];
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/objc/gs-prereqs.md)
* [Install](../../current/objc/gs-install.md)
* [Build and Run](../../current/objc/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/objc/database.md)
* [Documents](../../current/objc/document.md)
* [Blobs](../../current/objc/blob.md)
* [Remote Sync using Sync Gateway](../../current/objc/replication.md)
* [Handling Data Conflicts](../../current/objc/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)