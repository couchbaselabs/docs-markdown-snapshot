---
title: Index Service Cross Reference
description: A cross-referenced table of the metrics provided by the Index
  Service as named by various generations of reporting tools.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/index-service-metrics-cross-reference.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:metrics-reference:index-service-metrics-cross-reference.adoc[]
---

[View original HTML](/server/7.6/metrics-reference/index-service-metrics-cross-reference.html)

# Index Service Cross Reference

> A cross-referenced table of the metrics provided by the Index Service as named by various generations of reporting tools. 

See [Index Service Metrics](index-service-metrics.md) for full description of all the Index Service metrics.

The following table lets you lookup a metric name you may know from an alternative supported or legacy reporting tool.

__Table 1\. Index Service Metrics Cross Reference__
| Couchbase Server pre-7.0  | Couchbase Exporter                  | Couchbase Server 7.0+                                                     |
| ------------------------- | ----------------------------------- | ------------------------------------------------------------------------- |
| index\_memory\_quota      | cbindex\_memory\_quota              | index\_memory\_quota                                                      |
| index\_memory\_used       | cbindex\_memory\_used               | index\_memory\_used\_total                                                |
| index\_ram\_percent       | cbindex\_ram\_percent               | (index\_memory\_used\_total / ignoring(name) index\_memory\_quota) \* 100 |
| index\_remaining\_ram     | cbindex\_remaining\_ram             | index\_memory\_quota - ignoring(name) index\_memory\_used\_total          |
| avg\_scan\_latency        | cbindex\_avg\_scan\_latency         | index\_avg\_scan\_latency                                                 |
| cache\_hit\_percent       | cbindex\_cache\_hit\_percent        | (index\_cache\_hits \* 100) / (index\_cache\_hits + index\_cache\_misses) |
| cache\_hits               | cbindex\_cache\_hits                | index\_cache\_hits                                                        |
| cache\_misses             | cbindex\_cache\_misses              | index\_cache\_misses                                                      |
| data\_size                | cbindex\_data\_size                 | index\_data\_size                                                         |
| data\_size\_on\_disk      | N/A                                 | index\_data\_size\_on\_disk                                               |
| disk\_size                | cbindex\_disk\_size                 | index\_disk\_size                                                         |
| frag\_percent             | cbindex\_frag\_percent              | index\_frag\_percent                                                      |
| items\_count              | cbindex\_items\_count               | index\_items\_count                                                       |
| log\_space\_on\_disk      | N/A                                 | index\_log\_space\_on\_disk                                               |
| memory\_used              | N/A                                 | index\_memory\_used                                                       |
| num\_docs\_indexed        | cbindex\_num\_docs\_indexed         | index\_num\_docs\_indexed                                                 |
| num\_docs\_pending        | N/A                                 | index\_num\_docs\_pending                                                 |
| num\_docs\_queued         | N/A                                 | index\_num\_docs\_queued                                                  |
| num\_docs\_pending+queued | cbindex\_num\_docs\_pending\_queued | (index\_num\_docs\_pending + index\_num\_docs\_queued)                    |
| num\_requests             | cbindex\_num\_requests              | index\_num\_requests                                                      |
| num\_rows\_returned       | cbindex\_num\_rows\_returned        | index\_num\_rows\_returned                                                |
| raw\_data\_size           | N/A                                 | index\_raw\_data\_size                                                    |
| recs\_in\_mem             | N/A                                 | index\_recs\_in\_mem                                                      |
| recs\_on\_disk            | N/A                                 | index\_recs\_on\_disk                                                     |
| index\_resident\_percent  | cbindex\_resident\_percent          | index\_resident\_percent                                                  |
| scan\_bytes\_read         | N/A                                 | index\_scan\_bytes\_read                                                  |
| total\_scan\_duration     | N/A                                 | index\_total\_scan\_duration                                              |