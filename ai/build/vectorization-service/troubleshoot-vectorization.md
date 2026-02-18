---
title: Troubleshoot a Workflow
description: If your Capella AI Services Workflows complete with errors or have
  documents that cannot be processed, you can query a document's extended
  attributes (XATTRs) data for more information.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/vectorization-service/troubleshoot-vectorization.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ai/build/vectorization-service/troubleshoot-vectorization.html)

# Troubleshoot a Workflow

> If your Capella AI Services Workflows complete with errors or have documents that cannot be processed, you can query a document’s extended attributes (XATTRs) data for more information. 

Workflows create a `META().xattrs.vectorization.status` field on a document when that document is skipped during vectorization. You can use a SQL++ query to get information from this field and troubleshoot your Workflow.

If your Workflow returns a `LCB_ERR_DURABILITY_AMBIGUOUS` error, see [Resolve a LCB\_ERR\_DURABILITY\_AMBIGUOUS Error](#resolve).

For more information about Workflows, see [Process Your Data For Capella AI Services](data-processing.md).

> [!NOTE]
> If you deleted or modified your Workflow’s metadata scope, collections, or Eventing functions, your Workflow might fail to run correctly. You must delete the Workflow and create a new one.

## [](#prerequisites)Prerequisites

* You created and ran a Workflow on Capella AI Services. For more information, see:

  * [Vectorize Structured Data from Capella](vectorize-structured-data-capella.md)
  * [Vectorize Structured Data from Amazon S3](vectorize-structured-data-s3.md)
  * [Process and Vectorize Unstructured Data](vectorize-unstructured-data.md)

## [](#run-a-troubleshooting-query)Run a Troubleshooting Query

To troubleshoot and query the XATTRs for a skipped document:

1. On the **Operational** page, click the name of the cluster you used in your Workflow.
2. Go to **Data Tools** **Query**.
3. In the query editor, paste the following query, replacing the following values:

  * `<$WORKFLOW_ID>` with the ID value of your Workflow. You can view and copy your Workflow ID by expanding the entry for your Workflow on the **Workflows** page.
  * `<$BUCKET>` with the name of the bucket you selected as the destination for your Workflow.
  * `<$SCOPE>` with the name of the scope you selected as the destination for your Workflow.
  * `<$COLLECTION>` with the name of the collection you selected as the destination for your Workflow.  
  ```sqlpp  
  WITH idx AS (  
      SELECT COUNT(1) AS idx_count  
      FROM system:indexes  
      WHERE name = "<$WORKFLOW_ID>_progress"  
        AND state = "online"  
  )  
  SELECT VALUE result  
  FROM (  
      SELECT CASE WHEN (SELECT RAW idx_count FROM idx)[0] > 0  
          THEN (SELECT META().id AS doc_id,  
          {  
              "num_malformed_payload_to_model": META().xattrs.vectorization.status.bad_request,  
              "num_non_json_objects": META().xattrs.vectorization.status.non_json,  
              "num_payload_size_exceeds_model_context_window": META().xattrs.vectorization.status.too_big,  
              "num_non_existent_fields": META().xattrs.vectorization.status.no_fields,  
              "num_successful_embeddings": META().xattrs.vectorization.status.success  
          } AS details  
              FROM `<$BUCKET>`.`<$SCOPE>`.`<$COLLECTION>`  
              WHERE META().xattrs.vectorization.status IS NOT MISSING  
                AND (  
                      META().xattrs.vectorization.status.bad_request > 0  
                   OR META().xattrs.vectorization.status.non_json   > 0  
                   OR META().xattrs.vectorization.status.too_big    > 0  
                )  
                AND META().xattrs.vectorization.model    IS NOT MISSING  
                AND META().xattrs.vectorization.encoding IS NOT MISSING  
                AND META().xattrs.vectorization.version  IS NOT MISSING)  
          ELSE [{"message": "There looks to be an issue with this workflow’s index status. Contact Couchbase support for further help."}]  
      END AS arr  
  ) AS subq UNNEST subq.arr AS result;  
  ```
4. Press Enter or click **Run**.  
The query should return results similar to the following:  
```json  
[  
  {  
    "details": {  
      "num_malformed_payload_to_model": 0,  
      "num_non_existent_fields": 0,  
      "num_non_json_objects": 2,  
      "num_payload_size_exceeds_model_context_window": 0,  
      "num_successful_embeddings": 0  
    },  
    "doc_id": "mydoc123"  
  }  
]  
```

## [](#understand-query-results)Understand Query Results

The troubleshooting SQL++ query, in the `details` object for each `doc_id`, provides the following information:

| Error                                               | Description                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| num\_malformed\_payload\_to\_model                  | The number of processing requests to the embedding model that were rejected as malformed or bad requests.                                                                                                                                                                                                                                         |
| num\_non\_existent\_fields                          | The number of processing requests that referenced non-existent fields in the document. Check the configuration of your Workflow to make sure your selected source fields exist in the document you’re trying to process.                                                                                                                          |
| num\_non\_json\_objects                             | The number of processing requests that were rejected for JSON serialization issues. Check the content of your document and its fields to make sure the JSON is properly formed, if you’re using a [Data from Capella](vectorize-structured-data-capella.md) or [Structured Data from External sources](vectorize-structured-data-s3.md) Workflow. |
| num\_payload\_size\_exceeds\_model\_context\_window | The number of processing requests that exceeded the embedding model’s context size limit. Check the configuration of the embedding model you chose for your Workflow.                                                                                                                                                                             |
| num\_successful\_embeddings                         | The number of processing requests that created an embedding.                                                                                                                                                                                                                                                                                      |

## [](#resolve)Resolve a LCB\_ERR\_DURABILITY\_AMBIGUOUS Error

A Workflow can return a `LCB_ERR_DURABILITY_AMBIGUOUS` error when:

* The destination cluster is rebalancing.
* The destination bucket has a [Minimum Durability Level](../../../cloud/clusters/data-service/manage-buckets.md#durability) set to **Replicate to Majority**.

If your Workflow fails to run and returns this error, rerun your Workflow after your destination cluster has finished rebalancing:

1. Go to **AI Services** **Workflows**.
2. Go to **More Options (⋮)** **Rerun Workflow**.

## [](#next-steps)Next Steps

After you check your Workflow configurations and documents, you can rerun a Workflow by going to **More Options (⋮)** **Rerun Workflow** on the Workflows page.

If you cannot resolve the errors with a Workflow, [contact Couchbase Capella Support](../../../cloud/support/manage-support.md).