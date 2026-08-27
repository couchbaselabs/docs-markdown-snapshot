---
title: Troubleshooting
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.3/modules/ROOT/pages/troubleshooting.adoc
  xref: xref:kafka-connector::troubleshooting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kafka-connector/current/troubleshooting.html)

# Troubleshooting

## [](#address-already-in-use)Address already in use

If you try to run multiple connect workers on the same machine, you may see this error message: `java.net.BindException: Address already in use`. This happens because every worker has an embedded REST server that listens on port 8083 by default.

### [](#how-to-run-multiple-workers)How to run multiple workers on the same machine?

You'll need to assign a different REST port to each worker.

One solution is to use a different config file for each worker, with each config file specifying a different port. By default this file is called `connect-standalone.properties` or `connect-distributed.properties`. Create a copy of this file for each worker. In each file, set the `rest.port` property to a unique port.

### [](#not-running-multiple-workers)But I'm not running multiple workers!

Maybe the Confluent `connect` service is running? The `connect` service is essentially a connector worker running in distributed mode. Unless you're experimenting with running the connector in distributed mode, you can probably just stop this service:

```bash
confluent local services connect stop
```

If you're sure it's not the Confluent `connect` service that's causing the port conflict, it's possible that some other software is using port 8083\. In that case, you can [tell the worker to use a different port](#how-to-run-multiple-workers).