[View original HTML](/analytics/sources/manage-columnar.html)

> You can gather documents from one or more existing Capella Analytics collections into a standalone collection. You customize the content of your standalone collections by querying other collections. 

|  | For an example of creating standalone collections and populating them using a queries, see [Install the Commerce Dataset in Standalone Collections](../intro/examples.md#Install). |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

Role

To add a standalone collection, you must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your Capella Analytics cluster:

* [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
* [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)

Primary key

You must identify a primary key and its data type when you set up a standalone collection, so you must be familiar with the data you plan to insert into the collection. You supply the primary key as the name of the corresponding field or key in the data file and its data type. Each document inserted into the collection must have a field with this name and a value of this type.

Alternatively, you can choose to have Capella Analytics autogenerate values for the primary key. You supply a name for the primary key and a data type of UUID. For each document inserted into the collection, Capella Analytics generates a universally unique identifier and adds it with this key.

## [](#create-standalone)Create a Standalone Collection

To create a standalone collection:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope if necessary: see [Manage Capella Analytics Services Databases](manage-databases.md).
4. Click **Create** **Standalone Collection**. Alternatively, you can move your cursor over the name of a scope and then choose **⋮ (More)** **Add Standalone Collection**. The Create Standalone Collection dialog opens.
5. Select a **Database** and **Scope** for the new collection, or verify the supplied database and scope if you’re adding it to a specific scope.
6. In the **Collection Name** field, enter a name for the collection.  
The name must start with a letter (A-Z, a-z) and contain only upper- and lowercase letters, numbers (0-9), and underscore (\_) or dash (-) characters.
7. For the **Primary Key**, choose either:

  * **Enter Key Manually**: Enter the name of the primary key and select its data type (`int`, `double`, `string`).  
  To use a `keyName` that includes spaces or a `-` character, escape the name with backtick (``` `` ```) characters. To define a primary key made up of multiple fields, select **\+ Add Field**
  * **Autogenerate**: Enter a name for the primary key followed by `:UUID`.
8. Click **Create**. Your collection appears under the scope in the explorer.

## [](#work-with-a-standalone-collection)Work with a Standalone Collection

Standalone collections give you the flexibility to build a new dataset to store in Capella Analytics by querying other collections.

For example, you can copy in data from an external collection. Or, you can build a separate, long-lasting archive for documents from a remote Couchbase collection by periodically adding timestamped deltas.

* To populate a standalone collection, you can use queries to `INSERT INTO`, `COPY INTO`, and otherwise select data from other collections. You can also import data from a local data file.
* To manipulate the documents in the standalone collection to meet your needs, you use queries to `SELECT`, `INSERT INTO`, `UPSERT INTO`, `DELETE`, and so on.

For more information about using these SQL++ statements to write queries in Capella Analytics, see [DML Statements](../sqlpp/5%5Fdml.md).

## [](#view-metadata-for-a-collection)View Metadata for a Collection

Each time you add a collection, Capella Analytics records its metadata in the `System.Metadata.Dataset` collection. To view metadata for a collection, you query this system collection. See [Querying Metadata](../sqlpp/5%5Fddl%5Fmetadata.md).

## [](#see-also)See Also

* [Import Data to a Standalone Collection](import-data-standalone.md)
* [Query and Explore with the Workbench](../query/workbench.md)
* [DML Statements](../sqlpp/5%5Fdml.md)
* [Access Data](../intro/examples.md)