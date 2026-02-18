---
title: Assigning Services
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-set-up-services.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/rest-api/rest-set-up-services.html)

# Assigning Services

> By means of the REST API, services can be assigned to a new, single-node cluster. 

## [](#http-method-and-uri)HTTP Method and URI

POST /node/controller/setupServices

## [](#description)Description

Sets up the services for a one-node cluster, as part of its initial provisioning.

## [](#curl-syntax)Curl Syntax

curl  -X POST http://<ip-address-or-domain-name>:8091/node/controller/setupServices \
  -d services=<list-of-service-names>
  -u <username>:password

The `list-of-service-names` must consist of either:

* One or more of the following: `kv` (Data Service), `n1ql` (Query Service), `index` (Index Service), `fts` (Search Service), `eventing` (Eventing Service), `cbas` (Analytics Service), `backup` (Backup Service). Each name must be separated from the following name with a comma.
* Nothing. For 7.6 and later, this indicates that no service will be set up on the node.

Each assigned service is allocated a default amount of memory, unless custom allocations have been made. See [Configuring Memory](rest-configure-memory.md) for information on allocating memory per service, and on the default minimum values per service.

Note that during the process of provisioning a single-node cluster, `username` and `password` are required after the administrator has established credentials, as described in [Establishing Credentials](rest-establish-credentials.md).

## [](#responses)Responses

Success returns `200 OK`. If a username and password have already been assigned, failure to authenticate returns `401 Unauthorized`. An incorrectly expressed URI returns `404 Object Not Found`. An incorrect expression of the flag returns `400 Bad Request`, and an error message such as the following: `{"errors":{"services":"The value must be supplied"}}`. An incorrectly expressed service-name returns `400 Bad Request`, and an error message such as the following: `{"errors":{"services":"Unknown services: [\"eve3nting\"]"}}`.

## [](#examples)Examples

The following example establishes data paths for the Data, Index, and Eventing Services. Commas in the list of service-names have been encoded.

curl -X POST http://10.144.220.101:8091/node/controller/setupServices \
-d 'services=kv%2Cn1ql%2Cindex%2Ceventing' \
-u Administrator:password

The following example establishes that no service should run on the specified node.

curl -X POST http://10.144.220.101:8091/node/controller/setupServices \
-d 'services=' \
-u Administrator:password

## [](#see-also)See Also

The sequence of tasks divided into _initialization_ and _provisioning_ is explained in [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

For each of the other specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), and [Establishing Credentials](rest-establish-credentials.md). Specifically, see [Configuring Memory](rest-configure-memory.md) for information on allocating memory per service, and on the default minimum values per service.

For further information on initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).