---
title: Logging
description: Logging with the Python SDK.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.3@python-sdk:howtos:collecting-information-and-logging.adoc[]
---

[View original HTML](/python-sdk/4.3/howtos/collecting-information-and-logging.html)

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
couchbase.configure_logging(logger.name, level=logger.level) (1)

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

Once the SDK writes the logs with the tags to a file, you can then use the [cblogredaction tool](../../../server/7.6/cli/cbcli/cblogredaction.md) to obfuscate the log.

* You may wish to read more on Log Redaction [in the Server docs](../../../server/7.6/manage/manage-logging/manage-logging.md#understanding%5Fredaction).