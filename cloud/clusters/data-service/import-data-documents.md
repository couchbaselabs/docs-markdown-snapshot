[View original HTML](/cloud/clusters/data-service/import-data-documents.html)

> Use the Capella Import page to import data from your local drive into your cluster. The Capella Import page guides you through each step of the process, prompting you to select source files and identify target locations. Capella prepares a preview of your import, displaying real-time updates as you explore options for refining your import. Using preview, you can ensure you’re satisfied with the import before importing data into your cluster. 

## [](#about-importing-data)About Importing Data

Choose one of these options when importing data using the Capella UI:

* Import data sets smaller than 40 MB from your browser.
* Generate a command to import larger datasets using `cbimport`.
* Explore Capella using sample data.

### [](#required-permissions)Required Permissions

You must have the Data Writer role to be able to import data.

### [](#source-files)Source Files

The Capella UI lets you import source files that reside on your local machine. Capella supports importing these file formats:

* CSV — Comma-separated values file.
* TSV — Tab-separated values file.
* JSON — JavaScript Object Notation file.
* JSONL — JSON Lines file, a structured data storage format where each line is treated as an independent, valid JSON object.

### [](#cluster-target-locations)Cluster Target Locations

You can specify existing Scopes and Collections for your data import target. You can also create new ones as you set up the import.

## [](#reviewing-and-refining-your-import)Reviewing and Refining Your Import

Once you’ve specified your source file and target location, you can explore options for creating document keys and specify what parts of the data should be imported using Import Rules.

### [](#options-for-creating-document-keys)Options for Creating Document Keys

Each document extracted from your imported files needs a document key. You can choose to let Capella generate keys randomly for each document or specify a field value from your dataset for the document key. You can also choose to add a custom expression to generate document keys.

Use any of the following components to create custom document keys.

| Document Key Component | Description                                      | Delimiter   |
| ---------------------- | ------------------------------------------------ | ----------- |
| UUID                   | Universally Unique Identifier generator          | # (hash)    |
| MONO\_INCR             | Monotonically increasing number generator        | # (hash)    |
| Field values           | The value of a field selected from your data set | % (percent) |

For example, the expression `#UUID#_%City%_#MONO_INCR#` generates the following document key:

"docId": "6e41a1b1-c876-481a-afa0-aab395cadce2_Leominster_1",

### [](#import-rules)Import Rules

Using import rules, you can control which portions of your source file are included in the import.

* JSON/JSONL
* CSV/TSV

* **Skip the first n documents**: by default, all documents are loaded. Setting this option skips a specified number of documents before importing. When enabled, enter the number of documents to skip before the import starts.
* **Import a maximum of n documents**: stop loading after a specified number of documents. Use this to partially load large datasets. When enabled, enter the maximum number of documents to import.
* **Exclude field names**: Omit named fields from the uploaded documents. Use this to remove a field from documents, for example, a document key from a field in a document. When enabled, specify a comma-separated list of field names to exclude from the import.

* **Skip the first n documents**: by default, Capella loads all documents. Setting this option skips a specified number of documents before importing. When enabled, enter the number of documents to skip before the import starts.
* **Import a maximum of n documents**: stops loading after a specified number of documents. Use this to partially load large datasets. When enabled, enter the maximum number of documents to import.
* **Exclude field names**: Omit named fields from the uploaded documents. Use this to remove a field from documents, for example, a document key from a field in a document. When enabled, specify a comma-separated list of field names to exclude from the import.
* **Omit Empty Types**: rows in the CSV file which don’t contain data are stored as empty strings in the JSON doc. Setting this option removes these fields from the uploaded document.
* **Infer Field Types**: all values in a CSV are interpreted as strings by default. Setting this option causes the Import tool to look at each value and decide if it’s a string, integer, or Boolean value and put the inferred field type into the document.

## [](#how-to-import-data)How to Import Data

Follow the steps in the Capella UI to populate your cluster.

To access the **Import** tool, go to **Data Tools** **Import**.

|  | In free tier accounts, the **Home** tab also has a link to the Import tool. |
|  | --------------------------------------------------------------------------- |

### [](#import-data-from-your-browser)Import Data from Your Browser

Import a single file smaller than 40MB.

1. Go to **Data Tools** **Import**.
2. Choose **Load from your browser**.
3. Choose a file to upload or drag-and-drop it into the UI.
4. Specify the target for your import. You can choose existing Scopes and Collections or create new ones.
5. Preview and refine your import by:

  1. Choosing how to create document keys.
  2. Configuring Import rules.
6. Click **Import**.  
When the import is complete, a banner appears at the top of the page to tell you it was successful.  
To view your documents, click the **Documents** tab.

### [](#generate-a-command-to-import-data)Generate a Command to Import Data

Import a data set that is larger than 40MB. Generate a custom `cbimport` command that you can run from the command line. See [Command Line Tools](../../reference/command-line-tools.md) to download and install Couchbase Command Line Tools.

1. Go to **Data Tools** **Import**.
2. Choose a file to upload or drag-and-drop it into the UI.
3. Specify the target for your import. You can choose existing Scopes and Collections or create new ones.
4. Preview and refine your import by:

  1. Choosing how to create document keys
  2. Configuring Import rules
5. Copy the generated command and replace all values surrounded by brackets. Run the `cbimport` command from the command line to import your file.  
For more examples of how to use `cbimport`, see [Import and Export Data with Command Line Tools](../../connect/cli-import-export.md).

### [](#import-sample-data)Import Sample Data

Load sample data to try out Capella’s Data Tools.

1. Go to **Data Tools** **Import**.
2. Choose **Load sample data**.
3. Choose a sample.
4. Click **Import**.

## [](#related-links)Related Links

The Import tool loads data into your cluster. To restore a bucket of data, see [Restore a Bucket](../manage-restore.md#restore-bucket).