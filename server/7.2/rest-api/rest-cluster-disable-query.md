[View original HTML](/server/7.2/rest-api/rest-cluster-disable-query.html)

> Ensuring view query results consistency is performed with the `POST /internalSettings -d indexAwareRebalanceDisabled` HTTP method, URI, and parameter. 

## [](#description)Description

If view queries are performed during rebalance, this setting ensures that query results are consistent with the original bucket and data organization prior to rebalancing. In other words, the query results reflect the data on an original node prior to rebalance rather than data on a node after rebalance started. By default, this functionality is enabled.

|  | Be aware that rebalance may take significantly more time if you implemented views for indexing and querying. If rebalance time becomes a critical factor for your application, this feature can be disabled, however, it is not recommend. Do not disable this functionality for production applications without thorough testing. To do so may lead to unpredictable query results during rebalance. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#http-method-and-uri)HTTP method and URI

POST /internalSettings -d indexAwareRebalanceDisabled

## [](#syntax)Syntax

Curl request syntax:

curl -v -u [admin]:[password] -X POST
  http://[localhost]:8091/internalSettings
  -d indexAwareRebalanceDisabled=[true | false]

## [](#example)Example

Curl request example to disable this feature:

curl -v -u Administrator:password -X POST \
http://10.5.2.54:8091/internalSettings \
-d 'indexAwareRebalanceDisabled=true'

## [](#response)Response

HTTP/1.1 200 OK
Content-Type: application/json