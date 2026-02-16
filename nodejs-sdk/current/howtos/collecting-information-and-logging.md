[View original HTML](/nodejs-sdk/current/howtos/collecting-information-and-logging.html)

> Node.js SDK logging. 

|  | the Logging implementation has changed substantially in 4.x. Customized logging is not yet implemented, this will be resolved in a future 4.x release. Use of the console logger (detailed below) is currently recommended. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#library-logging)Library logging

The Node.js SDK allows logging via the `CBPPLOGLEVEL` environment variable.

Note that these logs will go to `stderr` — on most developers' laptops, `stderr` will be redirected to `stdout` (standard output), and displayed in the terminal running the app. Redirection to a log file may depend upon which shell you use. For the `BASH` shell, for example, see the [Bash Scripting Guide](https://tldp.org/LDP/abs/html/io-redirection.html).

### [](#environmental-settings)Environmental Settings

In the command line environment, the `CBPPLOGLEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGLEVEL=<log-level>
```

Windows

```console
set CBPPLOGLEVEL=<log-level>
```

Version 4.4.3 of the SDK introduces the `CBPPLOGFILE` variable that can be used in conjunction with `CBPPLOGLEVEL`. Set `CBPPLOGFILE` to a filename in order to have the log output to a file (instead of `stderr`).

In the command line environment, the `CBPPLOGFILE` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGFILE=<filename>
```

Windows

```console
set CBPPLOGFILE=<filename>
```

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.

When logging is turned on, the SDK will output messages similar to this:

```console
[2022-05-17 15:23:46.221] [85833,13741777] [debug] 1ms, [2aed64fd-5d38-416a-cc09-e67c371b8444]: use default CA for TLS verify
```

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