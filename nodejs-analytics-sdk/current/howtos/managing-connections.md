[View original HTML](/nodejs-analytics-sdk/current/howtos/managing-connections.html)

> This section describes how to connect the Node.js Analytics SDK to an Enterprise Analytics cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Enterprise Analytics cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to an Analytics cluster is represented by an `analytics` object. Connect to Enterprise Analytics by calling `analytics.createInstance` with the connection string, credentials, and any required optional parameters.

```javascript
const analytics = require('couchbase-analytics')

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'https://<your_hostname>:<PORT>'
    const username = 'username'
    const password = 'Password123!'
    // User Input ends here.

    const credential = new analytics.Credential(username, password)
    const cluster = analytics.createInstance(clusterConnStr, credential)
```

## [](#connection-strings)Connection Strings

Typically, an Enterprise Analytics cluster will be behind a load balancer, and you will be making a connection over TLS — so the port used will be `443`. This is the defaut for the SDK, so port `443` does not need to be specified: `<https://analytics.example.com>`.

You must specify the schema — either `https://` (for TLS) or `http://` (for insecure connections — perhaps on a development machine) in the connection string. The default port for insecure connections is port `80`.

If you’re connecting to a cluster directly, without a load balancer, you can specify the port in the connection string: `<https://analytics.example.com:18095>`. For a standalone Analytics cluster, the port is usually `18095` (or `8095` for an insecure connection). Make sure to check with your administrator.

### [](#client-settings-parameters)Client Settings Parameters

Connection strings can also include client settings, which will override any that are also set in the code.

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options).