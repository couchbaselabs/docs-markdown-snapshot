[View original HTML](/analytics/sources/import-data-standalone.html)

> You can use the Capella Analytics workbench to upload a data file into a standalone collection. 

The web interface guides you through each step of the import process, prompting you to select a local source file in a supported format and then to select or create a standalone collection.

Capella Analytics offers filtering options that you can apply to the selected file before importing, and prepares a set of previews of the results. You can review the raw data, see it in tabular format, and preview the JSON documents before you import.

## [](#source-files)Source Files

You use the workbench to import local source files. Capella Analytics supports importing data in these formats:

* CSV: Comma-separated values file.
* TSV: Tab-separated values file.
* JSON: JavaScript Object Notation file, which contains an array of JSON objects.
* JSONL: JSON Lines file, in which new lines delimit JSON objects.

You can import data sets that are 40 MB or less in size. If you attempt to import a file that is larger:

* For files in CSV, TSV, or JSONL format, Capella Analytics provides a warning message and automatically truncates the file.
* For files in JSON format, Capella Analytics provides an error message. After you edit the source file to reduce its size you can try the import again.

|  | You can use a SQL++ for Capella Analytics COPY INTO statement to import data from an Amazon S3 bucket to a standalone collection. The 40 MB size limitation does not apply. See [COPY INTO Statements](../sqlpp/5%5Fdml%5Fcopy%5Fin.md). |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#reviewing-and-refining-your-import)Reviewing and Refining Your Import

After you specify a file, you can preview the import. You can also explore options for filtering the data. Then, you select a target collection.

### [](#previewing-data-to-import)Previewing Data to Import

After you select a file to import, Capella Analytics prepares a set of different previews. You can use the previews to review the raw data and compare it to a tabular view and to the JSON documents that result from any conversions Capella Analytics applies.

While Capella Analytics detects the format of the selected file automatically, you can select a different **Parsed As** method to view differences in the previews.

If you set any import filters, the tabular and JSON document previews update to show their effects. By using the previews, you can be sure you’re satisfied with the options you select and how Capella Analytics parses the data before you populate the standalone collection.

### [](#filters)Import Filters

Using import filters, you can control which portions of your source file Capella Analytics includes in the import.

|  | Capella Analytics applies the maximum file size limitation of 40 MB before applying any filtering options. |
|  | ---------------------------------------------------------------------------------------------------------- |

* CSV/TSV
* JSON/JSONL

* **Skip the first n documents**: Specifies an offset to apply before beginning to import rows from the selected file. Check this option to enter a number of rows to skip before the import starts.
* **Import a maximum of n documents**: Places a limit on the number of rows to import from the selected file. Check this option to enter a maximum number of rows to import.
* **Exclude field names**: Omits specified columns from the imported rows. Use this option to prevent a column from being imported, for example, a set of columns that are not relevant to your needs. Check this option to specify a comma-separated list of column names to exclude from the import.
* **Omit Empty Types**: By default, Capella Analytics converts a cell that does not contain data to a key with an empty string value ("") in the JSON document. Check this option to prevent Capella Analytics from including empty key::value pairs in the JSON documents
* **Infer Field Types**: By default, Capella Analytics applies a data type of string, integer, or Boolean to each value imported into a JSON document. Clear this option to import all values as strings.

* **Skip the first n documents**: Specifies an offset to apply before beginning to import documents from the selected file. Check this option to enter a number of documents to skip before the import starts.
* **Import a maximum of n documents**: Places a limit on the number of documents to import from the selected file. Check this option to enter a maximum number of documents to import.
* **Exclude field names**: Omits specified keys (fields) from the imported documents. Use this option to prevent a field from being imported, for example, a field that’s not relevant to your needs. Check this option to specify a comma-separated list of field names to exclude from the import.

### [](#target-collection)Target Collection

You can specify an existing standalone collection as your target for the data import. If you select a target collection that already contains data, Capella Analytics performs an UPSERT operation to insert and update the documents in the collection. The primary key and data type of the data you’re importing must match the values defined for the collection.

You can also create a new standalone collection as the target. See [Create a Standalone Collection](manage-columnar.md#create-standalone) for information about requirements.

## [](#importing-a-data-file)Importing a Data File

To import a data file:

1. In the web interface, select the **Capella Analytics** tab.
2. Click the name of the cluster you want to work with. The workbench opens.
3. Click **Import**. Alternatively, you can move your cursor over the name of a standalone collection and then choose **⋮ (More)** **Import Data to Collection**.  
The Import Data dialog opens.
4. Choose a file to upload.
5. Preview your import and optionally refine it by setting [import filters](#filters).
6. Specify the target database, scope, and standalone collection for your import. You can choose an existing collection or click **Create Collection** to create a new one.  
The primary key and data type of the data you’re importing must match the values defined for the collection. See [Create a Standalone Collection](manage-columnar.md#create-standalone).
7. Click **Import Data**. Your browser begins a batch process to upsert documents into the collection.

|  | Navigating away from the Import Data dialog can interrupt this process. |
|  | ----------------------------------------------------------------------- |  
When the import is complete, a banner appears at the top of the page to tell you that it was successful.

After you import data, you can run `ANALYZE COLLECTION` to sample data in the collection so that cost-based optimization (CBO) can be applied instead of rule-based optimization. See [Cost-Based Optimizer for Capella Analytics Services](../sqlpp/5b%5Fcbo.md)

## [](#see-also)See Also

* [Set Up a Standalone Collection](manage-columnar.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [UPSERT INTO Statements](../sqlpp/5%5Fdml%5Fupsert.md)