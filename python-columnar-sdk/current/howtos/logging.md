[View original HTML](/python-columnar-sdk/current/howtos/logging.html)

> Logging with the Columnar Python SDK. 

The Columnar Python SDK allows logging via the standard `logging` module, or directly to the console.

## [](#enabling-logging)Enabling Logging

Python Logging Module

```python
import logging

import couchbase_columnar
from couchbase_columnar.cluster import Cluster
from couchbase_columnar.credential import Credential

# output log messages to example.log
logging.basicConfig(filename='example.log',
                    filemode='w', 
                    level=logging.DEBUG,
                    format='%(levelname)s::%(asctime)s::%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
# Good to set the logger's level because if the root level is not set, only WARNING level and above logs are output.
logger.setLevel(logging.DEBUG)
couchbase_columnar.configure_logging(logger.name, level=logger.level) 


def main() -> None:
    # Update this to your cluster
    connstr = 'couchbases://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(connstr, cred)

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

|  | Only one logger can be created. Either use PYCBCC\_LOG\_LEVEL to create a console logger or python logging, as mentioned above. |
|  | ------------------------------------------------------------------------------------------------------------------------------- |

In the command line environment, the PYCBCC\_LOG\_LEVEL variable is set as follows:

GNU/Linux and Mac

```console
export PYCBCC_LOG_LEVEL=<log-level>
```

Windows

```console
set PYCBCC_LOG_LEVEL=<log-level>
```

Where `<log-level>` is either `error`, `warn`, `info`, `debug` or `trace`.

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* critical — important functionality not working.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.