[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_copy_to_external.html)

> This topic describes how you use `COPY TO` statements to structure and write the results of a query—​or a copy of an entire collection—​out to an external data store such as Amazon S3 or Azure Blob Storage. 

Structuring the data in the external store is useful when you plan to query it later using [dynamic prefixes](../sources/dynamic-prefixes.md) for better performance.

|  | To be able to read or write data to or from external cloud storage exclusive permissions are required. For more information see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Following are the supported output formats:

* [JSON](5%5Fdml%5Fcopy%5Fto%5Fjson.md)
* [CSV/TSV](5%5Fdml%5Fcopy%5Fto%5Fcsv.md)
* [Parquet](5%5Fdml%5Fcopy%5Fto%5Fparquet.md)