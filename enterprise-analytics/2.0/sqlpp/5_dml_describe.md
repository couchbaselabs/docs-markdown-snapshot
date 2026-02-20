---
title: DESCRIBE LINK Statements
description: This topic describes how you can get information about a link with
  a <code>DESCRIBE LINK</code> statement.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_dml_describe.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:sqlpp:5_dml_describe.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/sqlpp/5_dml_describe.html)

# DESCRIBE LINK Statements

> This topic describes how you can get information about a link with a `DESCRIBE LINK` statement. 

You can use a `DESCRIBE LINK` statement to get information about either a remote or an external link.

> [!NOTE]
> To create a remote or external link, or to associate an Enterprise Analytics collection with a link, you must use the Enterprise Analytics UI. See [Stream Data from Remote Sources](../sources/manage-remote.md) or [Set Up an External Data Source](../sources/manage-external.md).

## [](#syntax)Syntax

**DescribeLinkStmt EBNF** 

```EBNF
DescribeLink ::= "DESCRIBE" "LINK" LinkName
```

**DescribeLinkStmt Diagram** 

!["DESCRIBE" "LINK" LinkName](_images/DescribeLink.png) 

## [](#examples)Examples

This example requests information about the remote `capellaLink` link that you set up between your Enterprise Analytics cluster and a Capella operational database. As a prerequisite for running this example yourself, follow the [Connecting to Data Sources](../intro/connecting-to-data-sources.md) procedures to add remote collections to Enterprise Analytics.

```SQL++
  DESCRIBE LINK capellaLink;
```

Results in:

```SQL++
  {
    "bootstrapHostname": "cb.<HOST_NAME>.com",
    "username": "alison",
    "password": "<redacted sensitive entry>",
    "encryption": "full",
    "certificates": [
      "-----BEGIN CERTIFICATE-----\nMIIDFT<CERTIFICATE_DETAILS>ivA==\n-----END CERTIFICATE-----\n"
    ],
    "uuid": "5ddea2d48e57a32b09a48c61ea1b32e4",
    "activeHostname": "svc-<HOST_NAME>.com:18091",
    "nodes": [
      {
        "hostname": "svc-<HOST_NAME>.com",
        "services": {
          "kv": 11210,
          "kvSSL": 11207,
          "mgmt": 8091,
          "mgmtSSL": 18091
        }
      },
      {
        "hostname": "svc-<HOST_NAME>.com",
        "services": {
          "kv": 11210,
          "kvSSL": 11207,
          "mgmt": 8091,
          "mgmtSSL": 18091
        }
      },
      {
        "hostname": "svc-<HOST_NAME>.com",
        "services": {
          "kv": 11210,
          "kvSSL": 11207,
          "mgmt": 8091,
          "mgmtSSL": 18091
        }
      }
    ],
    "bootstrapAlternateAddress": false,
    "clusterCompatibility": 458758,
    "httpsOpts": {
      "verifyPeer": true,
      "verifyHostname": true
    },
    "trustedCAsURIVersion": 22329081,
    "preventRedirects": true,
    "certificate": "-----BEGIN CERTIFICATE-----\nMIIDFT<CERTIFICATE_DETAILS>ivA==\n-----END CERTIFICATE-----\n",
    "name": "capellaLink",
    "database": null,
    "type": "couchbase"
  }
```

**Show an additional example** 

This example requests information about an external `musicLink` link set up between an Enterprise Analytics cluster and Amazon S3.

```SQL++
  DESCRIBE LINK musicLink;
```

Results in:

```SQL++
  {
    "instanceProfile": null,
    "accessKeyId": null,
    "secretAccessKey": null,
    "sessionToken": null,
    "region": "us-east-1",
    "serviceEndpoint": null,
    "name": "musicLink",
    "database": null,
    "type": "s3"
  }
```

## [](#see-also)See Also

* [Stream Data from Remote Sources](../sources/manage-remote.md)
* [Set Up an External Data Source](../sources/manage-external.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)