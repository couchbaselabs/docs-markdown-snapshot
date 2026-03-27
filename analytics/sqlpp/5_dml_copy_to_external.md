---
title: COPY TO External Data Store Statements
description: This topic describes how you use <code>COPY TO</code> statements to
  structure and write the results of a query--or a copy of an entire
  collection--out to an external data store such as Amazon S3 and GCS.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5_dml_copy_to_external.adoc
pubDate: 2026-03-27T05:16:21.194Z
link: xref:analytics:sqlpp:5_dml_copy_to_external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/5_dml_copy_to_external.html)

# COPY TO External Data Store Statements

> This topic describes how you use `COPY TO` statements to structure and write the results of a query—​or a copy of an entire collection—​out to an external data store such as Amazon S3 and GCS. 

Structuring the data in the external store is useful when you plan to query it later using [dynamic prefixes](../sources/dynamic-prefixes.md) for better performance.

> [!NOTE]
> To be able to read or write data to or from external cloud storage, you need to configure your connection and permissions. For more information, see [AWS](../sources/required-permissions-aws.md) and [GCS](../sources/required-permissions-gcs.md).

Following are the supported output formats:

* [JSON](5%5Fdml%5Fcopy%5Fto%5Fjson.md)
* [CSV/TSV](5%5Fdml%5Fcopy%5Fto%5Fcsv.md)
* [Parquet](5%5Fdml%5Fcopy%5Fto%5Fparquet.md)