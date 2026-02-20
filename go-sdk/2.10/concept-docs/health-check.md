---
title: Health Check
description: Health Check provides ping() and diagnostics() tests for the health
  of the network and the cluster.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.10/modules/concept-docs/pages/health-check.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.10@go-sdk:concept-docs:health-check.adoc[]
---

[View original HTML](/go-sdk/2.10/concept-docs/health-check.html)

# Health Check

> Health Check provides ping() and diagnostics() tests for the health of the network and the cluster. 

`Ping` and `diagnostics` methods, on the bucket and cluster objects respectively, can give us information about the current state of nodes, and their connections.

## [](#uses)Uses

'Ping\` provides a raw JSON payload suitable for feeding into reactive log and aggregation components, including monitoring systems like _Splunk_, _ElasticSearch_, and _Nagios_. It can also help keep connections alive if you are operating across an environment which aggressively closes down unused connections.

`Diagnostics` provides a strongly typed API for proactive, pull-based monitoring systems, such as:

* [Kubernetes Liveness and Readiness Probes via HTTP or CLI commands](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/).
* [Docker Health Check with CLI commands](https://docs.docker.com/engine/reference/builder/#healthcheck).
* [AWS ELB through HTTP](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html).

This API does not provide binary yes/no answers about the health of the cluster; rather it summarizes as much information as possible, for the application developer to assemble a complete, contextual view and come to a conclusion.

Note: `Ping` may reopen a connection, so is not without side-effects. `Diagnostics` shows what the SDK _perceives_ as the current state of the network and services — it is without side-effects, but may not be up to date.

## [](#ping)Ping

`Ping` _actively_ queries the status of the specified services,giving status and latency information for every node reachable. In addition to its use as a monitoring tool, a regular `Ping` can be used in an environment which does not respect keep alive values for a connection.

The return value is a `PingResult` containing detail about the report including a `services` field. The `services` field is a map of service type (e.g. `ServiceTypeKeyValue` or `ServiceTypeQuery`) to the value containing latency and status information. The report also supports being exported to JSON for purposes such as logging.

```golang
	// We'll ping the KV nodes in our cluster.
	pings, err := bucket.Ping(&gocb.PingOptions{
		ReportID:     "my-report",                                  (1)
		ServiceTypes: []gocb.ServiceType{gocb.ServiceTypeKeyValue}, (2)
	})
	if err != nil {
		panic(err)
	}

	for service, pingReports := range pings.Services {
		if service != gocb.ServiceTypeKeyValue {
			panic("we got a service type that we didn't ask for!")
		}

		for _, pingReport := range pingReports {
			if pingReport.State != gocb.PingStateOk {
				fmt.Printf(
					"Node %s at remote %s is not OK, error: %s, latency: %s\n",
					pingReport.ID, pingReport.Remote, pingReport.Error, pingReport.Latency.String(),
				)
			} else {
				fmt.Printf(
					"Node %s at remote %s is OK, latency: %s\n",
					pingReport.ID, pingReport.Remote, pingReport.Latency.String(),
				)
			}
		}
	}

	b, err := json.Marshal(pings) (3)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Ping report JSON: %s", string(b))
```

| **1** | ReportID is optional and assigns a name to this report, if empty then a uuid will be assigned. |
| ----- | ---------------------------------------------------------------------------------------------- |
| **2** | ServiceTypes are which services to ping against.                                               |
| **3** | The report can be marshalled down into JSON in a human friendly format.                        |

The output from exporting to JSON could look like:

```json
{
  "version":2,
  "sdk":"gocb/v2.1.5 gocbcore/v9.0.3",
  "id":"my-report",
  "services":{
    "kv":[
      {
        "id":"0xc000192280",
        "remote":"172.23.111.129:11210",
        "state":"ok",
        "namespace":"<md>travel-sample</md>",
        "latency_us":162551275
      },
      {
        "id":"0xc000192230",
        "remote":"172.23.111.128:11210",
        "state":"ok",
        "namespace":"<md>travel-sample</md>",
        "latency_us":162543150
      }
    ]
  }
}
```

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#ping).

```golang
	diagnostics, err := cluster.Diagnostics(&gocb.DiagnosticsOptions{
		ReportID: "my-report", (1)
	})
	if err != nil {
		panic(err)
	}

	if diagnostics.State != gocb.ClusterStateOnline {
		log.Printf("Overall cluster state is not online\n")
	} else {
		log.Printf("Overall cluster state is online\n")
	}

	for serviceType, diagReports := range diagnostics.Services {
		for _, diagReport := range diagReports {
			if diagReport.State != gocb.EndpointStateConnected {
				fmt.Printf(
					"Node %s at remote %s is not connected on service %s, activity last seen at: %s\n",
					diagReport.ID, diagReport.Remote, serviceType, diagReport.LastActivity.String(),
				)
			} else {
				fmt.Printf(
					"Node %s at remote %s is connected on service %s, activity last seen at: %s\n",
					diagReport.ID, diagReport.Remote, serviceType, diagReport.LastActivity.String(),
				)
			}
		}
	}

	db, err := json.Marshal(diagnostics) (2)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Diagnostics report JSON: %s", string(db))
```

| **1** | ReportID is optional and assigns a name to this report, if empty then a uuid will be assigned. |
| ----- | ---------------------------------------------------------------------------------------------- |
| **2** | The report can be marshalled down into JSON in a human friendly format.                        |

The output from exporting to JSON could look like:

```json
{
  "version":2,
  "sdk":"gocb/v2.1.5",
  "id":"my-report",
  "services":{
    "kv":[
      {
        "id":"0xc0000beb90",
        "last_activity_us":1639000,
        "remote":"172.23.111.129:11210",
        "local":"192.168.75.17:65310",
        "state":"connected",
        "namespace":"<md>travel-sample</md>"
      },
      {
        "id":"0xc000192320",
        "last_activity_us":1481000,
        "remote":"172.23.111.128:11210",
        "local":"192.168.75.17:65311",
        "state":"connected",
        "namespace":"<md>travel-sample</md>"
      }
    ]
  },
  "state":"online"
}
```