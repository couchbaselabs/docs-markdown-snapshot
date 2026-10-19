---
title: Rotate Internal Credentials
description: Credentials used for Operational Insights internal users can be
  rotated at any time, on a specified node, by means of the REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-rotate-internal-credentials.adoc
  xref: xref:enterprise-analytics:reference:rest-rotate-internal-credentials.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-rotate-internal-credentials.html)

# Rotate Internal Credentials

> Credentials used for Operational Insights internal users can be rotated at any time, on a specified node, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /node/controller/rotateInternalCredentials

## [](#description)Description

Rotates, on the specified node, all credentials used for Operational Insights internal users. Internal users include `@ns_server` and `@cbas`.

Note that these internal credentials are already rotated _automatically_, by default, in accordance with the interval specified by the `intCredsRotationInterval` parameter of `POST /settings/security` (described in [Configure On-the-Wire Security](rest-setting-security.md)). However, the `POST /node/controller/rotateInternalCredentials` method and URI additionally permit the credentials to be rotated immediately, in the event of a security breach.

The caller must have the Full Admin or Security Admin role.

## [](#curl-syntax)Curl Syntax

curl -X POST -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/node/controller/rotateInternalCredentials

## [](#responses)Responses

If successful, the method gives `200 OK`, and returns an empty array.

If the node is being reconfigured — for example, while nodes are being added or joined — the method gives `503 Service Unavailable`, and returns `["System is being reconfigured. Please try later."]`.

An incorrect URI gives `404 Object Not Found`. Failure to authenticate gives `401 Unauthorized`. An improper port number returns an error message such as `Failed to connect`, or `Port number out of range`.

## [](#example)Example

The following immediately rotates credentials for all Operational Insights internal users on `localhost`:

curl -X POST http://localhost:8091/node/controller/rotateInternalCredentials \
-u Administrator:password

If successful, the call returns an empty array. Note that completing rotation of the credentials may take some time.

## [](#see-also)See Also

Information on establishing and retrieving cluster-wide settings for the use of encryption and cipher-suites, including `intCredsRotationInterval`, is provided in [Configure On-the-Wire Security](rest-setting-security.md).