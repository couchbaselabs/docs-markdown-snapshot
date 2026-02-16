[View original HTML](/server/current/rest-api/rest-rotate-internal-credentials.html)

> Credentials used for Couchbase-Server internal users can be rotated at any time, on a specified node, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /node/controller/rotateInternalCredentials

## [](#description)Description

Rotates, on the specified node. all credentials used for Couchbase-Server internal users. Internal users include `@eventing`, `@cbq-engine`, `@ns_server`, `@index`, `@projector`, `@goxdcr`, `@fts`, and `@cbas`.

Note that these internal credentials are already rotated _automatically_, by default, in accordance with the interval specified by the `intCredsRotationInterval` parameter of `POST /settings/security/` (described in [Configure On-the-Wire Security](rest-setting-security.md)). However, the `POST /node/controller/rotateInternalCredentials` method and URI additionally permit the credentials to be rotated immediately, in the event of a security breach.

## [](#curl-syntax)Curl Syntax

curl -X POST -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/node/controller/rotateInternalCredentials

## [](#responses)Responses

If successful, the method gives `200 OK`, and returns an empty array.

An incorrect URI gives `404 Object Not Found`. Failure to authenticate gives `401 Unauthorized`. An improper port number returns an error message such as `Failed to connect`, or `Port number out of range`.

## [](#example)Example

The following immediately rotates credentials for all Couchbase-Server internal users on `localhost`:

curl -X POST http://localhost:8091/node/controller/rotateInternalCredentials \
-u Administrator:password

If successful, the call returns an empty array. Note that completing rotation of the credentials may take some time.

## [](#see-also)See Also

Information on establishing and retrieving cluster-wide settings for the use of encryption and cipher-suites is provided in [Configure On-the-Wire Security](rest-setting-security.md).