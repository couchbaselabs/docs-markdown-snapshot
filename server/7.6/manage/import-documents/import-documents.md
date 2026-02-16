[View original HTML](/server/7.6/manage/import-documents/import-documents.html)

> Couchbase Web Console provides a graphical interface for the importing of data, in both JSON and other formats. 

## [](#importing-data)Options for Importing Data

Data can be imported into Couchbase Server by means of the following:

* The **cbimport json** command-line utility, which imports JSON documents.
* The **cbimport csv** command-line utility, which imports data in CSV, TSV, and other _delimited_ formats.
* The interactive controls provided in the Couchbase Web Console **Import Documents** panel, itself located on the **Documents** screen; allowing import of JSON files, and also of CSV and TSV files.

The **cbimport json** and **cbimport csv** command-line utilities should be used in preference to Couchbase Web Console whenever high-performance importing is required; and especially when the data-set to be imported is greater in size than 100 MB.

For information on the **cbimport** command-line utilities, see [cbimport](../../tools/cbimport.md). The remainder of this page explains how to import data by means of Couchbase Web Console. Note the following prerequisites:

* Data must be imported into a specific bucket. Therefore, before attempting to import, ensure that an appropriate bucket exists. If necessary, create a bucket, following the instructions provided in [Create a Bucket](../manage-buckets/create-bucket.md). The procedures below assume that a bucket named `testBucket` has been created.
* Before attempting to import data with Couchbase Web Console, ensure that the **Query Service** has been deployed on the cluster: data-import with Couchbase Web Console depends on this service.

## [](#access-the-import-documents-panel)Access the Import Documents Panel

Access the **Import Documents** panel of Couchbase Web Console, as follows:

1. Left-click on the **Documents** tab, in the left-hand navigation bar:  
![The Documents tab in the left-hand navigation bar](../_images/import-documents/accessDocumentsTab.png)
2. When the **Documents** screen appears, select the **Import** tab, on the horizontal navigation bar, near the top:  
![The Import tab](../_images/import-documents/accessImportDocumentsTab.png)

The **Import** panel is now displayed:

![The Import panel](../_images/import-documents/importDocumentsPanel.png) 

## [](#understanding-the-import-panel)Understand the Import Panel

The **Import** panel displays the following interactive graphical elements:

* **Select File to Import**. A button that, when left-clicked on, displays a file-selection interface. This allows the user to select a single file that contains the data to be imported. To the right of the button is a link — **file format details** — that, when hovered over with the mouse-cursor, provides a pop-up notification of acceptable file-formats:  
![The file format details popup](../_images/import-documents/fileFormatDetails.png)  
These file-formats are described in the subsections below.
* **Parse File As**. This field displays the _type_ of the imported file: Couchbase Server will parse the data within the file, thereby creating one or more JSON documents; which will be stored in the [Destination Bucket](#destination-bucket). The [File Contents](#file-contents) panel can be reviewed, to verify that Couchbase Server performs the conversion correctly.  
Before any file has been selected, the default value, **CSV**, is displayed in the **Parse File As** field. However, when the user left-clicks on the **Select File to Import** button, Couchbase Server automatically determines the type of the selected file; displays the file-type in this field; and additionally displays, to the right of the field, the number of _records_ that the file contains.  
Should automatic file-type recognition ever result in the display of an incorrect file-type, the control at the right-hand side of the field can be used, to display a pulldown menu; which allows user-selection of the correct file-type. The menu appears as follows:  
![The Parse File As menu](../_images/import-documents/parseFileAsMenu.png)  
The options [CSV](#importing-csv-and-tsv-files), [TSV](#importing-csv-and-tsv-files), [JSON List](#import-a-json-list), and [JSON Lines](#importing-json-lines), are described in the subsections below.

* **Keyspace**. Three pulldown menus, which respectively display all buckets available on the cluster, the scopes in each bucket, and the collections in each scope. The selected bucket, scope, and collection are those into which data will be imported. For example:  
![The Keyspace controls with the bucket menu displayed](../_images/import-documents/destinationBucketSelectTestBucket.png)
* **Import With Document ID**. Two radio-buttons, which allow specification of how the _id_ of the newly imported document is to be determined. Note that each document within a bucket is identified with a unique id.  
The **UUID** option specifies that a _Universal Unique Identifier_ be generated automatically, and used as the document’s id.  
The **Value of Field** option specifies that the _value_ that corresponds to a particular _field_ within each document should be used as the document’s _id_: this option is only activated _after_ a file has been selected for import. Selecting this option displays a pulldown menu, which lists those fields that are common to each document: this is demonstrated below, in [Importing a JSON List](#import-a-json-list). For any document to be imported, when the selected field contains a value that is unique across the selected bucket, the document will be imported into the bucket as a new document, with the unique value as its id. Conversely, when the selected field contains a value that is _not_ unique across the bucket, the document will be imported into the bucket as an _update_ to a document that is already resident within the bucket, and shares the id specified by the value.
* The **cbimport** command-line display. This display changes dynamically, to indicate the **cbimport** command that could be used as an alternative way of performing the current import, based on the user’s ongoing addition of parameter-values into the UI.

* **File Contents**. A read-only field that displays the contents of the imported file. The field provides three display options: these are **Raw File**, which displays the unformatted file-contents; **Parse Table**, which shows the file-contents as a table, with rows and columns; and **Parse JSON**, which shows the file as formatted JSON. Note that this field can be used in conjunction with the **Parse File As** pulldown menu, to verify the correct type and data-format of the file selected for import.
* **Import Data**. This button is to be left-clicked on, when all appropriate details of the file to be imported have been entered: data-import is then commenced. Status on the operation is displayed immediately below the button. Note that if the operation takes a long time, the button’s label is changed to **Cancel**; at which point, by left-clicking, the user can cancel the import operation.

## [](#import-a-json-list)Import a JSON List

To be imported, JSON documents must be specified in a file: the file itself must then specified as the target for import. Within the file, the documents can be specified in either of two ways: as a _list_, or as a series of _lines_.

The procedure for importing a JSON list can be demonstrated as follows.

1. Save the following JSON list, as a file named `list.json`:  
```json  
[  
  {"name": "jane", "age": 22, "height": 5.2, "weight": 97},  
  {"name": "jack", "age": 18, "height": 5.9, "weight": 138},  
  {"name": "henry", "age": 47},  
  {"name": "susan", "age": 35, "height": 5.1, "weight": 110, "birth": {"dayOfBirth": 17, "monthOfBirth": 4}},  
  {"name": "david", "age": 43, "height": 5.11, "weight": 195, "birth": {"dayOfBirth": 3, "monthOfBirth": 12}}  
]  
```  
The file thus contains a JSON array of five elements. Each element is a document, containing multiple key-value pairs.
2. Within the **Import** panel, left-click on the **Select File to Import** button:  
![Select File to Import button](../_images/import-documents/selectFileToImport.png)  
The brings up the file-selection interface specific to the host operating system. Use this to select the file targeted for import. For example:  
![Selecting list.json](../_images/import-documents/fileSelectionInterface.png)  
When the file `list.json` has been selected, the **Import Documents** panel appears as follows:  
![Preview of list.json](../_images/import-documents/importDocumentsWithInitialContent.png)  
The filename `list.json` now appears immediately below the **Select File to Import** button. The **Parse File As** menu displays **JSON List**, indicating that Couchbase Server has correctly recognized the file type. To the right of the **Parse File As** field, the number of records found in the file is displayed.  
Note that, under **Import With Document ID**, the **Value of Field** option has now become activated; and displays, as a default selection, a common _field_ it has encountered — which is `name`.  
Note also that the **cbimport** command-line display has changed, to incorporate the information so far entered by means of the user-interface.  
The **File Contents** field now shows the file contents — by default, as a **Parsed Table**.
3. Specify a destination bucket, using the **Destination Bucket** pulldown menu. In this case, `testBucket` is to be selected, with the `_default` scope and collection:  
![The Keyspace controls, selecting testBucket](../_images/import-documents/destinationBucketSelectTestBucket.png)
4. Select a form of _id_ for the documents to be imported. The **Import With Document ID** field provides two radio buttons. **UUID** specifies that an id is automatically generated for each document, by Couchbase Server. **Value of Field** allows choice of a field, common to all the listed documents: the value of the field, as it appears in each individual document, will be used as that document’s id.  
For this instance, leave the default selection, **UUID**, unchanged.  
Optionally, the **File Contents** can now be displayed in the available, alternative forms. To display `list.json` as unformatted JSON, left-click on the **Raw File** tab:  
![Raw File tab](../_images/import-documents/rawFileTab.png)  
The file `list.json` now appears, unformatted, in the **File Contents** panel:  
![list.json as a raw file](../_images/import-documents/fileContentsRawFile.png)  
Alternatively, left-click on the **Parsed JSON** tab:  
![Parsed JSON tab](../_images/import-documents/parsedJSONTab.png)  
The **File Contents** pane now shows a parsed version of the file `list.json`, the initial section of which appears as follows:  
![list.json as parsed JSON](../_images/import-documents/fileContentsAsParsedJSON.png)
5. Import the file. Left-click on the **Import Data** button, located in the lower center area of the **Import Documents** panel.  
![The Import Data button](../_images/import-documents/leftClickOnImportButton.png)  
The documents in the specified file are now imported. If the operation is successful, a notification appears at the lower left of the console:  
![Import notification successful](../_images/import-documents/importNotification.png)
6. Check the imported documents. Left-click on the **Workbench** tab, on the horizontal, upper navigation bar:  
![The Workbench tab](../_images/import-documents/leftClickOnWorkbenchTab.png)  
This brings up the **Edit** panel, which now appears as follows:  
![The imported data in the Documents Workbench](../_images/import-documents/documentEditorWithImportedDocuments.png)  
The five documents contained in the file `list.json` have been successfully imported. Each has been automatically assigned an id. The documents can now be inspected and edited, by means of the **Workbench**.

### [](#importing-into-scopes-and-collections)Import into Scopes and Collections

A _collection_ is a data container, defined on Couchbase Server, within a bucket whose type is either _Couchbase_ or _Ephemeral_. A _scope_ is a mechanism for the grouping of multiple collections. A bucket can contain multiple scopes. Scopes and collections are described in [Scopes and Collections](../../learn/data/scopes-and-collections.md). Step-by-step instructions for creating scopes and collections are provided in [Manage Scopes and Collections](../manage-scopes-and-collections/manage-scopes-and-collections.md).

The interactive **Keyspace** fields on the **Import** panel of the **Documents** screen allow scopes and collections, as well as buckets, to be specified as the target locations for document-import. In the previous example, the bucket **testBucket** was selected, but no change was made to the default scope and collection settings; which were both **\_default**. (See [Default Scope and Collection](../../learn/data/scopes-and-collections.md#default-scope-and-collection), for information.) However, administrator-created scopes and collections can be specified by means of the pulldown menus provided. For example, if the bucket **testBucket** contains a scope named **testScope**, within which is a collection named **testCollection**, these can be specified as follows:

![The Keyspace controls, selecting testCollection](../_images/import-documents/specifyScopeAndCollection.png) 

At this point, the generated command, displayed at the upper right of the **Import** panel, is as follows:

![Generated cbimport command](../_images/import-documents/generatedCommandWithScopeAndCollection.png) 

As this shows, `"testScope.testCollection"` appears as the value for the `--scope-collection-exp` flag. When the **Import Document** button is now left-clicked on, the contents of the `json.list` file are imported into the collection **testCollection**, which is within the scope **testScope**; which itself is within the bucket **testBucket**. This can be validated by accessing the **Documents** panel, and specifying the appropriate keyspace:

![The Document Workbench with imported data in the testCollection](../_images/import-documents/documentsImportedIntoCollection.png) 

## [](#importing-json-lines)Import JSON Lines

A _JSON Lines_ file is one that contains one or more JSON documents, each on a separate line. The following procedure demonstrates how to import such a file.

1. Save the following JSON lines file, as `lines.json`:  
```json  
{"lastName": "smith", "employeeNumber": "0003456"}  
{"lastName": "roberts", "employeeNumber": "0007584"}  
{"lastName": "jones", "employeeNumber": "0005811"}  
{"lastName": "davis", "employeeNumber": "0009324"}  
```  
The file thus contains four objects, each of which appears on its own line. Each object contains two fields, which are `lastName` and `employeeNumber`.
2. Access the **Import** panel of the **Documents** screen.
3. Left-click on the **Select File to Import** button, and select the `lines.json` file. On selection, the **Parse File As** field displays **JSON Lines**, and the **File Contents** field displays the following:  
![lines.json as a parsed table](../_images/import-documents/fileContentsWithJSONlinesParsedTable.png)
4. Select `testBucket` with _default_ scope and collection, as the destination **Keyspace**.
5. In the **Import With Document ID** panel, select the **Value of Field** option, and display the pulldown menu. This appears as follows:  
![Value of Field, selecting employeeNumber](../_images/import-documents/importWithEmployeeNumber.png)  
Each `employeeNumber` field contains a unique value, and can therefore be used as the document id: therefore, select **employeeNumber**, as the value to be used.
6. Import the document, by left-clicking on the **Import Data** button. When the **Import Complete** dialog confirms success, dismiss the dialog by left-clicking on its **Continue** button.
7. Examine the imported documents, by accessing the **Workbench** tab. The documents appear as follows:  
![The Document Workbench with lines.json imported](../_images/import-documents/importedDocumentsWithEmployeeNumberID.png)

Thus, each document has been imported, with its `employeeNumber` value as the id of the document.

## [](#importing-csv-and-tsv-files)Import CSV and TSV Files

To import a CSV (_comma-separated values_) file, proceed as follows:

1. Save the following, as `employees.csv`:  
```csv  
lname,empno  
smith,0003456  
roberts,0007584  
jones,0005811  
davis,0009324  
```
2. Access the **Import** panel, and use the select `employees.csv` for import, by means of the **Select File to Import** button. Select `testBucket` with _default_ scope and collection, as the destination **Keyspace**. The panel now appears as follows:  
![Preview of employees.csv](../_images/import-documents/importDocumentsWithCSVprepared.png)
3. Under **Import With Document ID**, specify `empno` as **Value of Field**.
4. Left-click on the **Import Data** button. The documents are imported, with the value of `empno` is used as the id for each.
5. Check the appearance of the documents, in the **Workbench** panel.

To import a TSV (_tab-separated values_) file, follow the same procedure, with a file named `employees.tsv`, containing the following:

```tsv
lname     empno
smith     0003456
roberts	  0007584
jones	  0005811
davis	  0009324
```

## [](#handling-errors)Handle Errors

If the contents of a file selected for import are inconsistent, Couchbase Server displays an error notification. For example:

JSON Parse Errors

![JSON Parse Errors dialog](../_images/import-documents/jsonParseErrors.png) 

Displayed when the JSON within a file is incorrect. For example, the JSON of a particular document is flawed (possibly due to a missing or redundant comma, or a missing curly brace); or the JSON array with a _list_ file is missing a square bracket; or more than one document within a _lines_ file appears on the same line.

Import Warning: No Records Found

![Import Warning dialog: no records found](../_images/import-documents/importWarning.png) 

Displayed when no records can be found within the specified file. This may be due to a file-naming error: for example, a JSON _list_ has been saved as a `*.lines` file.

Import Warning: Data-Type Unrecognized

![Import Warning dialog: data type unrecognized](../_images/import-documents/importWarning2.png) 

Displayed when Couchbase Server cannot identify the data within the file as being of any supported type.

In each case, to remedy the problem, inspect the data within the file, ensure that it is properly formatted per document, and correctly laid out in accordance with the file-type; then retry.