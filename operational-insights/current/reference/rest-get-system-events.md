---
title: Getting System Events
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-get-system-events.adoc
  xref: xref:enterprise-analytics:reference:rest-get-system-events.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-get-system-events.html)

# Getting System Events

> System events that occur on the cluster can be retrieved. 

## [](#http-method-and-uris)HTTP method and URIs

GET /events

GET /eventsStreaming

## [](#rest-getting-system-events-description)Description

The `events` URI returns previously logged system events. The `eventsStreaming` URI returns previously logged system events as an array; and then streams all further system events as they occur.

Either the Full or the Cluster Admin role is required.

## [](#curl-syntax)Curl Syntax

curl -v -X GET -u [username]:[password]
  http://<ip-address-or-domain-name>:8091/events?sinceTime=<time-value>&limit=<limit-value>

curl -v -X GET -u [username]:[password]
  http://<ip-address-or-domain-name>:8091/eventsStreaming

The `sinceTime` path-parameter specifies the time (inclusive) from which previously logged events are to be returned. The associated `time-value` must be specified in _ISO 8601 UTC_ format — which is `YYYY-MM-DDThh:mm:ssZ`. If this path-parameter is not used, events starting from the oldest are returned. Note that events are stored in a log file by the Cluster Manager, and are replicated to each individual node. Delays in replication may result in some events being omitted from the results returned from the node specified in the call. Note also that the maximum size of each event log is 10K: logs are rotated (in memory and on disk) when this limit is reached: events not in the current log cannot be returned.

The `limit` path-parameter specifies the maximum number of events to be returned. The default `limit-value` is `250`. If a `sinceTime` is specified, the events returned are, starting from the `sinceTime`, the earliest events that have been logged. If no `sinceTime` is specified, the events returned are the most recent events to have been logged. If `limit-value` is specified as `-1`, no limit is imposed; and all events logged since the specified `sinceTime` — or, if no `sinceTime` has been specified, from and including the oldest logged event — are therefore returned.

## [](#responses)Responses

Success gives the response code `200 OK`. A malformed URI returns `404 Object Not Found`. Failure to authenticate gives `401 Unauthorized`.

## [](#examples)Examples

The following examples show how to use the calls.

### [](#return-previously-logged-events)Return Previously Logged Events

The following call returns events logged since 10:36 am on January 4th, 2022 — specifying a maximum of two. The events returned are the first two events to have occurred since the specified `sinceTime`. The output is piped to the [jq](https://jqlang.org/) program, to facilitate readability.

curl -X GET 'http://localhost:8091/events?sinceTime=2022-01-04T10:36:00Z&limit=2' -u Administrator:password | jq

If successful, the call returns output such as the following:

{
  "events": [
    {
      "timestamp": "2022-01-05T11:30:48.265Z",
      "uuid": "11a03d9d-cc1c-c402-37ec-4e48abdd69b9",
      "event_id": 1,
      "component": "ns_server",
      "description": "Service started",
      "severity": "info",
      "extra_attributes": {
        "name": "ns_server"
      },
      "node": "cb.local",
      "otp_node": "ns_1@cb.local"
    },
    {
      "timestamp": "2022-01-05T11:30:48.279Z",
      "uuid": "a24057ac-b4a8-8b82-d1b0-0a380be41344",
      "event_id": 18,
      "component": "ns_server",
      "description": "Master selected",
      "severity": "info",
      "extra_attributes": {
        "new_master": "ns_1@cb.local"
      },
      "node": "cb.local",
      "otp_node": "ns_1@cb.local"
    }
  ]
}

Note that if no `sinceTime` is specified, but a `limit` _is_ specified, the number of events returned is that specified by the `limit-value`; these being the most recent events to have occurred. For example, the following call returns the most recent two events:

curl -X GET 'http://localhost:8091/events?limit=2' -u Administrator:password | jq

If the call is successful, the output resembles the following:

{
  "events": [
    {
      "timestamp": "2022-01-10T11:59:22.837Z",
      "event_id": 2,
      "component": "ns_server",
      "description": "Rebalance initiated",
      "severity": "info",
      "node": "10.144.220.101",
      "otp_node": "ns_1@10.144.220.101",
      "uuid": "83bd3f33-be2c-4dd9-9ba0-845dcb01f92c",
      "extra_attributes": {
        "operation_id": "87ded2912711c9452db360197c15bc80",
        "nodes_info": {
          "active_nodes": ["ns_1@10.144.220.101", "ns_1@10.144.220.102"],
          "keep_nodes": ["ns_1@10.144.220.101", "ns_1@10.144.220.102"],
          "eject_nodes": [],
          "delta_nodes": [],
          "failed_nodes": []
        }
      }
    },
    {
      "timestamp": "2022-01-10T11:59:24.277Z",
      "event_id": 3,
      "component": "ns_server",
      "description": "Rebalance completed",
      "severity": "info",
      "node": "10.144.220.101",
      "otp_node": "ns_1@10.144.220.101",
      "uuid": "a4cdb37e-036b-402a-84a5-4228f8b0df61",
      "extra_attributes": {
        "operation_id": "87ded2912711c9452db360197c15bc80",
        "nodes_info": {
          "active_nodes": ["ns_1@10.144.220.101", "ns_1@10.144.220.102"],
          "keep_nodes": ["ns_1@10.144.220.101", "ns_1@10.144.220.102"],
          "eject_nodes": [],
          "delta_nodes": [],
          "failed_nodes": []
        },
        "time_taken": 1440,
        "completion_message": "Rebalance completed successfully."
      }
    }
  ]
}

### [](#event-filtering)Event Filtering

You can filter events by specifying any of the following parameters:

| component | Filter events by component name. The component name can be one of the following values: ns\_server, analytics, or security          |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| event\_id | An integer value representing the ID of the event.                                                                                  |
| severity  | Filter events by severity level. The filter accepts one of the following for the severity parameter: info, warning, error, or fatal |

### [](#filtering-examples)Filtering Examples

The following call filters events by the `ns_server` component.

curl -v -X GET  'http://localhost:8091/events?component=ns_server' -u Administrator:password | jq

If the call is successful, it returns a result similar to this:

{
  "events": [
    {
      "timestamp": "2026-01-14T11:05:27.558Z",
      "event_id": 1,
      "component": "ns_server",
      "description": "Service started",
      "severity": "info",
      "node": "cb.local",
      "otp_node": "ns_1@cb.local",
      "uuid": "00adda40-bbdc-4c0a-ae78-ae682c4ce085",
      "extra_attributes": {
        "name": "ns_server"
      }
    },
    {
      "timestamp": "2026-01-14T11:05:28.121Z",
      "event_id": 1,
      "component": "ns_server",
      "description": "Service started",
      "severity": "info",
      "node": "cb.local",
      "otp_node": "ns_1@cb.local",
      "uuid": "e2ba670b-2023-4d3f-8cc1-60e59d68365d",
      "extra_attributes": {
        "name": "saslauthd_port"
      }
    }
   ]
}

You can also filter events using a combination of parameters. This example filters for a specific event ID with a severity level of `info`.

curl -v -X GET  'http://localhost:8091/events?event_id=18&severity=info' -u Administrator:password | jq

If successful, then a result similar to the following is returned:

{
  "events": [
    {
      "timestamp": "2026-01-14T11:05:28.548Z",
      "event_id": 18,
      "component": "ns_server",
      "description": "Master selected",
      "severity": "info",
      "node": "cb.local",
      "otp_node": "ns_1@cb.local",
      "uuid": "b6a4b1d1-7ce7-4e45-ab71-0c8365de1984",
      "extra_attributes": {
        "new_master": "ns_1@cb.local"
      }
    },
    {
      "timestamp": "2026-01-14T11:06:44.709Z",
      "event_id": 18,
      "component": "ns_server",
      "description": "Master selected",
      "severity": "info",
      "node": "127.0.0.1",
      "otp_node": "ns_1@127.0.0.1",
      "uuid": "6e213fae-136a-4bcc-8339-56abd9e6a749",
      "extra_attributes": {
        "new_master": "ns_1@127.0.0.1"
      }
    }
  ]
}

### [](#return-a-stream-of-ongoing-events)Return a Stream of Ongoing Events

The following call returns all previously logged system events that are held in the event log; then, it starts a stream of system events, which are displayed on the console as they occur on the cluster:

curl -v -X GET localhost:8091/eventsStreaming -u Administrator:password

If successful, the call initially returns an array of previously logged system events:

[{"timestamp":"2021-11-30T09:35:58.536Z","uuid":"0cc06643-4aa9-c8e1-7488-9cee65eadcbd","event_id":1,"component":"ns_server","description":"Service started","severity":"info","extra_attributes":{"name":"ns_server"}, . . .

                                                      . . . "node":"10.144.220.101"}]

Subsequently, events are displayed on the console as they occur. For example, triggering a rebalance results in the following information displayed to the console:

[{"timestamp":"2022-01-04T12:54:47.072Z","event_id":2,"component":"ns_server","description":"Rebalance initiated","severity":"info","node":"10.144.220.101","uuid":"828b9993-ed40-4196-b779-3f2aa4440b7e","extra_attributes":{"operation_id":"87ded2912711c9452db360197c15bc80","nodes_info":{"active_nodes":["ns_1@10.144.220.101","ns_1@10.144.220.102"],"keep_nodes":["ns_1@10.144.220.101","ns_1@10.144.220.102"],"eject_nodes":[],"delta_nodes":[],"failed_nodes":[]}}},{"timestamp":"2022-01-04T12:54:48.521Z","event_id":3,"component":"ns_server","description":"Rebalance completed","severity":"info","node":"10.144.220.101","uuid":"7b3d6236-71b8-431b-8ac6-39c443e9a628","extra_attributes":{"operation_id":"87ded2912711c9452db360197c15bc80","nodes_info":{"active_nodes":["ns_1@10.144.220.101","ns_1@10.144.220.102"],"keep_nodes":["ns_1@10.144.220.101","ns_1@10.144.220.102"],"eject_nodes":[],"delta_nodes":[],"failed_nodes":[]},"time_taken":1440,"completion_message":"Rebalance completed successfully."}}]

## [](#see-also)See Also

For a complete list of system events, see the [System Event Reference](system-event-reference.md).