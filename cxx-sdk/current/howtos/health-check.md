[View original HTML](/cxx-sdk/current/howtos/health-check.html)

> Health Check provides `ping()` and `diagnostics()` tests for the health of the network and the cluster. 

In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Working in distributed environments is hard. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check features _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information.

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

```c++
        auto options = couchbase::ping_options().service_types({ couchbase::service_type::key_value, couchbase::service_type::query });
        auto [err, res] = cluster.ping(options).get();
        if (err) {
            fmt::println("Got an error doing ping: {}", err);
        } else {
            fmt::println("{}", res.as_json());
        }
        /*
        {
            "id":"0x10290d100","kv":[
                {
                    "id":"0000000072b21d66",
                    "last_activity_us":2363294,
                    "local":"10.112.195.1:51473",
                    "remote":"10.112.195.101:11210",
                    "status":"connected"
                },
                {
                    "id":"000000000ba84e5e",
                    "last_activity_us":7369021,
                    "local":"10.112.195.1:51486",
                    "remote":"10.112.195.102:11210",
                    "status":"connected"
                },
                {
                    "id":"0000000077689398",
                    "last_activity_us":4855640,
                    "local":"10.112.195.1:51409",
                    "remote":"10.112.195.103:11210",
                    "status":"connected"
                }
            ],
            "sdk":"cxx/1.0.0/be41e5e;Darwin/arm64",
            "version":1
        }
        */
```

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#ping).

```c++
auto [err, res] = cluster.diagnostics().get();
if (err) {
    fmt::println("Got an error doing diagnostics: {}", err);
} else {
    fmt::println(res.as_json());
}
/*
{
    "id":"0x10290d100","kv":[
        {
            "id":"0000000072b21d66",
            "last_activity_us":2363294,
            "local":"10.112.195.1:51473",
            "remote":"10.112.195.101:11210",
            "status":"connected"
        },
        {
            "id":"000000000ba84e5e",
            "last_activity_us":7369021,
            "local":"10.112.195.1:51486",
            "remote":"10.112.195.102:11210",
            "status":"connected"
        },
        {
            "id":"0000000077689398",
            "last_activity_us":4855640,
            "local":"10.112.195.1:51409",
            "remote":"10.112.195.103:11210",
            "status":"connected"
        }
    ],
    "sdk":"cxx/1.0.0/be41e5e;Darwin/arm64",
    "version":1
}
*/
```