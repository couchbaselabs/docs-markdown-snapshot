---
title: Logging
description: Logging with the Operational Insights Python SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Python Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-python/edit/release/1.0/modules/howtos/pages/logging.adoc
  xref: xref:python-operational-insights-sdk:howtos:logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-operational-insights-sdk/current/howtos/logging.html)

# Logging

> Logging with the Operational Insights Python SDK. 

The Operational Insights Python SDK allows logging via the standard `logging` module, or directly to the console.

## [](#enabling-logging)Enabling Logging

Python Logging Module

```python
import logging

from couchbase_operational_insights import LOG_DATE_FORMAT, LOG_FORMAT
from couchbase_operational_insights.cluster import Cluster
from couchbase_operational_insights.credential import Credential


# output log messages to example.log
logging.basicConfig(filename='example.log',
                    filemode='w', 
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=LOG_DATE_FORMAT)

logger = logging.getLogger(__name__)
# Good to set the logger's level because if the root level is not set, only WARNING level and above logs are output.
logger.setLevel(logging.DEBUG)


def main() -> None:
    # Update this to your cluster
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)

    # Execute a query and buffer all result rows in client memory.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    res = cluster.execute_query(statement)
    all_rows = res.get_all_rows()
    for row in all_rows:
        logger.info(f'Found row: {row}')
    logger.info(f'metadata={res.metadata()}')

if __name__ == '__main__':
    main()
```

## [](#logging-via-environmental-settings)Logging via Environmental Settings

> [!IMPORTANT]
> Only one logger can be created. Either use `PYCBAC_LOG_LEVEL` to create a console logger or python `logging`, as mentioned above.

In the command line environment, the PYCBAC\_LOG\_LEVEL variable is set as follows:

GNU/Linux and Mac

```console
export PYCBAC_LOG_LEVEL=<log-level>
```

Windows

```console
set PYCBAC_LOG_LEVEL=<log-level>
```

Where `<log-level>` is either `error`, `warn`, `info`, or `debug`.

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* critical — important functionality not working.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information (level required to investigate problems).