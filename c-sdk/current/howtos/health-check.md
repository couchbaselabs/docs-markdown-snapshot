[View original HTML](/c-sdk/current/howtos/health-check.html)

> In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Health Check introduces _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information. 

Diagnosing problems in distributed environments is far from easy, so Couchbase provides a _Health Check API_ with `Ping()` for active monitoring. ans `Diagnostics()` for a look at what the client believes is the current state of the cluster. More extensive discussion of the uses of Health Check can be found in the [Health Check Concept Guide](../concept-docs/health-check.md).

## [](#ping)Ping

At the simplest `lcb_PING_SERVICE` is an enumeration used to indicate the type of service in PING responses. You can customize the type of services to ping through this service. Service types include:

* `LCB_PING_SERVICE_KV`
* `LCB_PING_SERVICE_VIEWS`
* `LCB_PING_SERVICE_QUERY`
* `LCB_PING_SERVICE_SEARCH`
* `LCB_PING_SERVICE_ANALYTICS`

`lcb_PING_STATUS` returns the current status of the service.

```c
void ping_callback(lcb_INSTANCE *, int, const lcb_RESPPING *resp)
{
    lcb_STATUS rc = lcb_respping_status(resp);
    if (rc != LCB_SUCCESS) {
        fprintf(stderr, "failed: %s\n", lcb_strerror_short(rc));
    } else {
        const char *json;
        size_t njson;
        lcb_respping_value(resp, &json, &njson);
        while (njson > 1 && json[njson - 1] == '\n') {
            njson--;
        }
        if (njson) {
            printf("%.*s", int(njson), json);
        }
    }
}
```

## [](#diagnostics)Diagnostics

Diagnostics work in a similar fashion to `lcb_PING_SERVICE` in the sense that it returns a report of how all the sockets/end-points are doing, but the main difference is that it is passive. While `lcb_PING_SERVICE` proactively sends an operation across the network, a diagnostics report just returns whatever current state the client is in. This makes it much cheaper to call on a regular basis, but does not provide any live insight into network slowness, _et al._.

```c
lcb_install_callback(instance, LCB_CALLBACK_DIAG, diag_callback);
void diag_callback(lcb_INSTANCE, int, const lcb_RESPBASE *rb)
{
    const lcb_RESPDIAG *resp = (const lcb_RESPDIAG *)rb;
    char* json;
    size_t json_len;
    lcb_STATUS rc = lcb_respdiag_status(resp);
    if (rc != LCB_SUCCESS) {
        fprintf(stderr, "failed: %s\n", lcb_strerror_short(rc));
    } else {
        lcb_respdiag_value(resp, &json, &json_len);
        if (json) {
            fprintf(stderr, "\n%.*s", json_len, json);
        }
    }
}
```

For more information on `lcb_diag()`, refer to [API Documentation](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-ping.html#ga5229063d7be73f0231233a3c0dd1e3c4).