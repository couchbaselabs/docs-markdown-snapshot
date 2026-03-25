---
title: Health Check
description: In today's distributed and virtual environments, users will often
  not have full administrative control over their whole network.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/howtos/pages/health-check.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:go-sdk:howtos:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/howtos/health-check.html)

# Health Check

> In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Health Check introduces _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information. 

Diagnosing problems in distributed environments is far from easy, so Couchbase provides a _Health Check API_ with `Ping()` for active monitoring and `Diagnostics()` for a look at what the client believes is the current state of the cluster. More extensive discussion of the uses of Health Check can be found in the [Health Check Concept Guide](../concept-docs/health-check.md).

## [](#ping)Ping

At its simplest, `ping` provides information about the current state of the connections in the Couchbase Cluster, by actively polling: `Ping` is available at the `Cluster` and `Bucket` object levels. Below we use it at the `Bucket` level:

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

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#Ping).

As the Go SDK does not hold long lived HTTP connections the `Diagnostics` operation will only return information about connections to the KeyValue service.

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