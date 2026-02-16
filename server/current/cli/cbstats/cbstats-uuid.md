[View original HTML](/server/current/cli/cbstats/cbstats-uuid.html)

> Provides the UUID for a bucket. 

## [](#syntax)Syntax

Request syntax:

cbstats [host]:11210 uuid [options]

## [](#description)Description

Provides the UUID for a bucket.

## [](#options)Options

| Option            | Description                                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-b <bucket-name> | This flag and value are required: if they are omitted, an error is returned. The bucket-name must be the name of a bucket currently defined on the cluster of which the specified host is a member. |

## [](#example)Example

**Request**

/opt/couchbase/bin/cbstats localhost:11210 uuid -b travel-sample

**Response**

 uuid: 027ea0ff4684d631c491ecfbb812ac6a