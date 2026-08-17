---
title: Logging
description: Logging with the Python SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/collecting-information-and-logging.adoc
  xref: xref:4.5@python-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.5/howtos/collecting-information-and-logging.html)

# Logging

> Logging with the Python SDK. 

The Python SDK allows logging via the standard `logging` module.

## [](#enabling-logging)Enabling Logging

Python Logging Module

```python
import logging
import traceback
from datetime import timedelta

import couchbase
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.diagnostics import ServiceType
from couchbase.exceptions import CouchbaseException
from couchbase.options import ClusterOptions, WaitUntilReadyOptions

# output log messages to example.log
logging.basicConfig(filename='example.log',
                    filemode='w', 
                    level=logging.DEBUG,
                    format='%(levelname)s::%(asctime)s::%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()
couchbase.configure_logging(logger.name, level=logger.level)

cluster = Cluster('couchbase://your-ip',
                  ClusterOptions(PasswordAuthenticator("Administrator", "password")))

cluster.wait_until_ready(timedelta(seconds=3),
                         WaitUntilReadyOptions(service_types=[ServiceType.KeyValue, ServiceType.Query]))

logger.info('Cluster ready.')

bucket = cluster.bucket("travel-sample")
coll = bucket.scope('inventory').collection('airline')
try:
    coll.get('not-a-key')
except CouchbaseException:
    logger.error(traceback.format_exc())
```

### [](#environmental-settings)Environmental Settings

> [!IMPORTANT]
> Only one logger can be created. Either use `PYCBC_LOG_LEVEL` to create a console logger or `configure_logging` as mentioned above.

In the command line environment, the `PYCBC_LOG_LEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export PYCBC_LOG_LEVEL=<log-level>
```

Windows

```console
set PYCBC_LOG_LEVEL=<log-level>
```

Version 4.3.3 of the SDK introduces the `PYCBC_LOG_FILE` variable that can be used in conjunction with `PYCBC_LOG_LEVEL`. Set `PYCBC_LOG_FILE` to a filename in order to have the log output to a file (instead of stdout).

In the command line environment, the `PYCBC_LOG_FILE` variable is set as follows:

GNU/Linux and Mac

```console
export PYCBC_LOG_FILE=<filename>
```

Windows

```console
set PYCBC_LOG_FILE=<filename>
```

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* critical — important functionality not working.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.

## [](#log-redaction)Log Redaction

Redacting logs is a two-stage process. If you want to redact client logs (for example before handing them off to the Couchbase Support team) you first need to enable log redaction in your application. This is done through the [ClusterOptions](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#clusteroptions), setting `log_redaction` to `True`.

Once the SDK writes the logs with the tags to a file, you can then use the [cblogredaction tool](../../../server/current/cli/cbcli/cblogredaction.md) to obfuscate the log.

* You may wish to read more on Log Redaction [in the Server docs](../../../server/current/manage/manage-logging/manage-logging.md#understanding%5Fredaction).

## [](#sdk-telemetry-from-the-server)SDK Telemetry from the Server

In addition to Tracing and other metrics, and client logging, SDK telemetry is also sent to the Server — available from 8.0, and in new Capella Operational clusters — for ingestion with other Prometheus metrics. Capella Operational exposes these metrics through the UI.

For self-managed Server, collection can be disabled and enabled through the REST API:

```console
curl --user Administrator:password http://172.17.0.2:8091/settings/appTelemetry -d enabled=true
```

And the Prometheus-format metrics fetched with:

```console
curl --user Administrator:password http://172.17.0.2:8091/metrics
```

There may be advantages to collecting information this way, but note that metrics are collected per node, and a central Prometheus instance should be set to collect all metrics so that information is not lost in case of a sudden failover.

Also note that if the cluster is behind a load balancer, the collected metrics may not accurately record the actual correct node with which the SDK interacts.