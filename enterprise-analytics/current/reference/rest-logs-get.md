[View original HTML](/enterprise-analytics/current/reference/rest-logs-get.html)

> Diagnostic information can be retrieved by using the `GET` method with the `/diag` URI. The current content of a log file can be returned by using `GET` with the `/sasl_logs` URI. 

## [](#http-method-and-uris)HTTP method and URIs

GET /diag

GET /sasl_logs/<log-name>

## [](#description)Description

The `GET /diag` method and URI return general Couchbase-Server diagnostic information. This requires the **Full Admin**, the **Cluster Admin**, or the **Local User Security Admin** role.

The `GET /sasl_logs` method and URI return the contents of a Couchbase-Server _log_ file. This requires the **Full Admin** or the **Cluster Admin** role.

For general information about logging and log files, including the location of log files and descriptions of their content, see [Manage Logging](../manage/manage-logging/manage-logging.md).

## [](#curl-syntax)Curl Syntax

curl -X GET -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/diag

curl -X GET -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/sasl_logs/<log-name>

The `log-name` argument should be the name of a Couchbase-Server log file that is present in the directory used for saving log files on the specified node. For the per-platform default locations for saving log files, see the page [Manage Logging](../manage/manage-logging/manage-logging.md#logging%5Foverview). For a complete list of log files, see [Log File Listing](../manage/manage-logging/manage-logging.md#log-file-listing).

If no `log-name` argument is specified, the default value is `debug`; whereby the contents of the `debug.log` file are displayed.

## [](#responses)Responses

For both URIs, success gives `200 OK`, and displays the returned content. Failure to authenticate gives `401 Unauthorized`. When `GET /sasl_logs` is used, a `log-name` that is incorrectly specified, or corresponds to a log file that does not currently exist, gives `404 Object Not Found`.

## [](#examples)Examples

The following examples show how to return diagnostic information and log-file content.

### [](#returning-diagnostic-information)Returning Diagnostic Information

The following example uses `GET /diag` to return Couchbase-Server diagnostic information:

curl -v -X GET -u Administrator:password http://10.143.194.101:8091/diag

If successful, this returns (extensive) output whose initial section resembles the following:

logs:
-------------------------------
2020-02-07T04:30:30.429-08:00, ns_cookie_manager:3:info:cookie update(ns_1@cb.local) - Initial otp cookie generated: {sanitized,
                                  <<"ioEsqBp4LGNDxWCwMhypDPgfIrcseb1GCgSBno+G7d8=">>}
2020-02-07T04:30:30.580-08:00, menelaus_sup:1:info:web start ok(ns_1@cb.local) - Couchbase Server has started on web port 8091 on node 'ns_1@cb.local'. Version:
 "6.5.0-4960-enterprise".
2020-02-07T04:30:30.816-08:00, mb_master:0:info:message(ns_1@cb.local) - I'm the only node, so I'm the master.
2020-02-07T04:30:30.880-08:00, compat_mode_manager:0:warning:message(ns_1@cb.local) - Changed cluster compat mode from undefined to [6,5]
2020-02-07T04:30:30.937-08:00, memcached_config_mgr:0:info:message(ns_1@cb.local) - Hot-reloaded memcached.json for config change of the following keys: [<<"cli
ent_cert_auth">>,
      .
      .
      .

### [](#returning-log-file-content)Returning Log-File Content

The following example uses `GET /sasl_logs` with the `stats` endpoint, to return the contents of the `stats.log` log file:

curl -v -X GET -u Administrator:password http://10.143.194.101:8091/sasl_logs/stats

If successful, this returns (extensive) output, whose initial section resembles the following:

logs_node (stats.log):
-------------------------------
[ns_doctor:debug,2020-02-07T04:30:30.602-08:00,ns_1@cb.local:ns_doctor<0.354.0>:ns_doctor:handle_info:182]Got initial status:
[{'ns_1@cb.local',
     [{last_heard,-576460749154163105},
      {now,-576460749183621671},
      {active_buckets,[]},
      {ready_buckets,[]},
      {status_latency,29351},
      {outgoing_replications_safeness_level,[]},
      {incoming_replications_conf_hashes,[]},
      {meminfo,
          <<"MemTotal:        1016332 kB\nMemFree:
          .
          .
          .

## [](#see-also)See Also

General information about logging and log files, including locations and descriptions of all log files, is provided in [Manage Logging](../manage/manage-logging/manage-logging.md).