[View original HTML](/server/current/rest-api/rest-ddocs-delete.html)

> To delete a design document, use the `DELETE /buckets/_design/[ddocs-name]` HTTP request and URI on the `8092` port. 

## [](#description)Description

Deleting a design document immediately invalidates the design document and all views and indexes associated with it. The indexes and stored data on disk are removed in the background.

## [](#http-method-and-uri)HTTP method and URI

The design document name follows the `/bucket/_design` URI.

DELETE /bucket/_design/[ddoc-name]

| **Request Data**            | Design document definition (JSON)        |
| --------------------------- | ---------------------------------------- |
| **Response Data**           | Success and confirmed design document ID |
| **Authentication Required** | Optional                                 |

## [](#syntax)Syntax

Curl request syntax:

curl -v -X DELETE
  -H "Content-Type: application/json"
  -u [admin]:[password]
  http://[localhost]:8092/default/_design/[ddoc-name]

|  | The request is issued on the 8092 port. |
|  | --------------------------------------- |

## [](#example)Example

Curl request example:

curl -v -X DELETE \
  http://Administrator:Password@192.168.0.77:8092/default/_design/dev_byfield

## [](#response)Response

When the design document has been successfully removed, the JSON returned indicates successful completion and confirmation of the removal.

{
   "ok":true,
   "id":"_design/dev_byfield"
}

Error conditions are returned if the authorization is incorrect or the specified design document cannot be found.

## [](#response-codes)Response codes

| Response codes | Description                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 200            | Request completed successfully.                                                                                              |
| 401            | The item requested was not available using the supplied authorization, or authorization was not supplied.                    |
| 404            | The requested content could not be found. The returned content includes further information, as a JSON object, if available. |