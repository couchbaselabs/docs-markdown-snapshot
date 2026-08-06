---
title: CREATE CATALOG
description: The <code>CREATE CATALOG</code> statement registers an external
  Apache Iceberg catalog with Enterprise Analytics, enabling Iceberg tables to
  be created on it as external collections.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_iceberg_catalog.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_ddl_iceberg_catalog.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_iceberg_catalog.html)

# CREATE CATALOG

> The `CREATE CATALOG` statement registers an external Apache Iceberg catalog with Enterprise Analytics, enabling Iceberg tables to be created on it as external collections. 

Once a catalog is registered, create individual Iceberg tables on it using [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md). Catalogs are globally unique and do not belong to an Analytics database.

For an overview of supported catalog types and authentication, see [Iceberg Support](5%5Fddl%5Ficeberg.md).

Enterprise Analytics supports the following catalog types:

* [AWS Glue](#aws-glue)
* [AWS Glue REST](#aws-glue-rest)
* [S3 Tables](#s3-tables)
* [Google BigLake Metastore](#google-biglake-metastore)
* [Nessie](#nessie)
* [Nessie REST](#nessie-rest)
* [REST](#rest)

## [](#syntax)Syntax

```SQL++
CREATE CATALOG <catalog-name>
TYPE Iceberg
SOURCE <source-type>
AT <link-name>
[ WITH <object> ];
```

## [](#arguments)Arguments

catalog-name

The name of the catalog entity in Enterprise Analytics. catalog-name must be globally unique.

TYPE Iceberg

Specifies that this is an Apache Iceberg catalog.

SOURCE

The catalog implementation to connect to. Accepted values: `AWS_GLUE`, `AWS_GLUE_REST`, `S3_TABLES`, `BIGLAKE_METASTORE`, `NESSIE`, `NESSIE_REST`, `REST`.

AT link-name

The [link](../sources/manage-links.md) used to authenticate connections to the catalog service. The required link type differs by `SOURCE`. See each catalog section on this page for details.

WITH

A JSON object containing catalog-specific configuration properties. Required properties differ by `SOURCE` type, as described in each catalog section on this page.

Enterprise Analytics supports the following catalog types:

* [AWS Glue](#aws-glue)
* [AWS Glue REST](#aws-glue-rest)
* [S3 Tables](#s3-tables)
* [Google BigLake Metastore](#google-biglake-metastore)
* [Nessie](#nessie)
* [Nessie REST](#nessie-rest)
* [REST](#rest)

## [](#aws-glue)AWS Glue

AWS Glue does not require any `WITH` properties. Authentication uses the AWS credentials in the specified AWS link, which authenticate any AWS service including AWS Glue. To target an AWS Glue catalog in a different AWS account, provide the optional `"glue.id"` property in the `WITH` clause.

```SQL++
CREATE CATALOG myGlueCatalog
TYPE Iceberg
SOURCE AWS_GLUE
AT myAwsLink
WITH {};
```

## [](#aws-glue-rest)AWS Glue REST

AWS Glue REST connects to the AWS Glue Iceberg REST endpoint using Sigv4-signed credentials from the specified AWS link.

```SQL++
CREATE CATALOG myGlueRestCatalog
TYPE Iceberg
SOURCE AWS_GLUE_REST
AT myAwsLink
WITH {
    "uri": "https://glue.<aws-region>.amazonaws.com/iceberg",
    "sigv4SigningRegion": "<aws-region>"
};
```

| Property           | Description                                    | Required |
| ------------------ | ---------------------------------------------- | -------- |
| uri                | URI of the AWS Glue Iceberg REST endpoint.     | Yes      |
| sigv4SigningRegion | AWS region used to sign the Sigv4 credentials. | Yes      |

## [](#s3-tables)S3 Tables

S3 Tables connects to an Amazon S3 Tables bucket via the Iceberg REST endpoint using Sigv4-signed credentials. Two signing configurations are supported — `s3tables` and `glue` — each using different values for `uri` and `warehouse`.

### [](#using-s3tables-signing)Using `s3tables` Signing

```SQL++
CREATE CATALOG myS3TablesCatalog
TYPE Iceberg
SOURCE S3_TABLES
AT myAwsLink
WITH {
    "uri": "https://s3tables.<aws-region>.amazonaws.com/iceberg",
    "warehouse": "<s3-tables-bucket-arn>",
    "sigv4SigningName": "s3tables",
    "sigv4SigningRegion": "<aws-region>"
};
```

### [](#using-glue-signing)Using `glue` Signing

```SQL++
CREATE CATALOG myS3TablesCatalog
TYPE Iceberg
SOURCE S3_TABLES
AT myAwsLink
WITH {
    "uri": "https://glue.<aws-region>.amazonaws.com/iceberg",
    "warehouse": "<account-id>:s3tablescatalog/<table-bucket-name>",
    "sigv4SigningName": "glue",
    "sigv4SigningRegion": "<aws-region>"
};
```

| Property           | Description                                                                                                               | Required |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------- | -------- |
| uri                | REST endpoint URI — use the S3 Tables endpoint with s3tables signing, or the AWS Glue endpoint with glue signing.         | Yes      |
| warehouse          | S3 Tables bucket ARN when signing with s3tables; <account-id>:s3tablescatalog/<table-bucket-name> when signing with glue. | Yes      |
| sigv4SigningName   | Signing service name: s3tables or glue.                                                                                   | Yes      |
| sigv4SigningRegion | AWS region used to sign the Sigv4 credentials.                                                                            | Yes      |

## [](#google-biglake-metastore)Google BigLake Metastore

Google BigLake Metastore is a REST-compatible Iceberg catalog backed by GCP. Authentication uses the Google credentials in the specified GCS link.

```SQL++
CREATE CATALOG myBiglakeCatalog
TYPE Iceberg
SOURCE BIGLAKE_METASTORE
AT myGcsLink
WITH {
    "warehouse": "gs://my-iceberg-bucket/",
    "uri": "https://biglake.googleapis.com/iceberg/v1/restcatalog",
    "quotaProjectId": "my-gcp-project-id"
};
```

| Property       | Description                                                         | Required |
| -------------- | ------------------------------------------------------------------- | -------- |
| warehouse      | GCS bucket used as the base path for table metadata and data files. | Yes      |
| uri            | URI of the Google BigLake Metastore Iceberg REST endpoint.          | Yes      |
| quotaProjectId | GCP project ID for billing.                                         | Yes      |

## [](#nessie)Nessie

Nessie provides its own catalog implementation with Git-like branching semantics. Authentication uses an HTTP link and supports basic auth, Bearer token, or OAuth 2.0.

```SQL++
CREATE CATALOG myNessieCatalog
TYPE Iceberg
SOURCE NESSIE
AT myHttpLink
WITH {
    "uri": "http://<address:port>/api/v2",
    "warehouse": "s3://my-iceberg-bucket/nessie/warehouse"
};
```

| Property  | Description                                  | Required |
| --------- | -------------------------------------------- | -------- |
| uri       | URI of the Nessie server Iceberg endpoint.   | Yes      |
| warehouse | Base path for table metadata and data files. | Yes      |

## [](#nessie-rest)Nessie REST

Nessie REST uses the Nessie REST catalog implementation. The `uri` encodes both the branch name and the warehouse name in its path. Authentication uses an HTTP link and supports basic auth, Bearer token, or OAuth 2.0.

```SQL++
CREATE CATALOG myNessieRestCatalog
TYPE Iceberg
SOURCE NESSIE_REST
AT myHttpLink
WITH {
    "uri": "http://<address:port>/iceberg/main%7Cwarehouse"
};
```

| Property | Description                                                                                                                                                                                | Required |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| uri      | URI of the Nessie REST catalog endpoint. The path must include the branch and warehouse name in the form /branchName\|warehouseName. The pipe character may need to be URL-encoded as %7C. | Yes      |

## [](#rest)REST

The `REST` source type connects Enterprise Analytics to any REST-compatible Iceberg catalog. Authentication uses an HTTP link and supports basic auth, Bearer token, or OAuth 2.0.

```SQL++
CREATE CATALOG myRestCatalog
TYPE Iceberg
SOURCE REST
AT myHttpLink
WITH {
    "uri": "<catalog-service-uri>"
};
```

| Property | Description                       | Required |
| -------- | --------------------------------- | -------- |
| uri      | URI of the REST catalog endpoint. | Yes      |

## [](#see-also)See Also

* [Iceberg Tables](5%5Fddl%5Ficeberg.md)
* [Create an Iceberg Table](5%5Fddl%5Ficeberg%5Ftable.md)
* [Manage Links](../sources/manage-links.md)
* [Set Up an External Data Source](../sources/manage-external.md)