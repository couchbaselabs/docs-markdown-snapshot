[View original HTML](/java-columnar-sdk/current/howtos/managing-connections.html)

> This section describes how to connect the Java Columnar SDK to a Couchbase cluster. It contains best practices as well as advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to a Capella Columnar cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```java
import com.couchbase.columnar.client.java.Cluster;
import com.couchbase.columnar.client.java.Credential;
import com.couchbase.columnar.client.java.QueryResult;
```

A connection to a Capella Columnar cluster is represented by a `Cluster` object. A `Cluster` provides access to databases, scopes, and collections, as well as various Columnar services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.newInstance()` with a [connection string](#connection-strings), username, and password:

```java
public class Example {
  public static void main(String[] args) {
    var connectionString = "couchbases://cb.<your-endpoint>.cloud.couchbase.com";
    var username = "...";
    var password = "...";

    try (Cluster cluster = Cluster.newInstance(
      connectionString,
      Credential.of(username, password)
    )) {
        // Interact with the cluster here
    }
  }
}
```

|  | The above example uses a try-with-resources block to ensure the Cluster instance gets closed at the end. It’s important to either use a try-with-resources block, or make sure to call cluster.close() when you’re done with the cluster. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Capella’s root certificate is **not** signed by a well known Certificate Authority. However, the certificate is bundled with the SDK, and is automatically trusted unless you specify a different certificate to trust. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

For Columnar, as for all Capella products, connection must be made with Transport Layer Security (TLS) — for full encryption of client-side traffic — for which the `couchbases://` schema is used as the root of the connection string (note the trailing **s**).

Simple connection string

couchbases://cb.<your-endpoint>.cloud.couchbase.com

Connection string with two parameters

couchbases://cb.<your-endpoint>.cloud.couchbase.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Capella Operational docs](../../../cloud/get-started/connect.md#connecting-your-sdk-to-capella).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can’t handle an SRV record that’s large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\].