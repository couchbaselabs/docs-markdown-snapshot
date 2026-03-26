---
title: Introduction
description: The Couchbase Apache Superset Connector lets you visualize data
  from Tabular Analytics Views (TAV) in Apache Superset.
editUrl: https://github.com/couchbase/docs-connectors-superset/edit/release/1.0/modules/ROOT/pages/index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:superset-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/superset-connector/current/index.html)

# Introduction

> The Couchbase Apache Superset Connector lets you visualize data from Tabular Analytics Views (TAV) in Apache Superset.
> 
> It works by connecting Capella Columnar to Apache Superset using SQLAlchemy, allowing you to create interactive visualizations from your tabular data.

## [](#install-the-couchbase-sqlalchemy-connector)Install the Couchbase SQLAlchemy Connector

To install the Couchbase SQLAlchemy Connector, open the command prompt (`cmd`), and enter the following:

```console
pip install couchbase-sqlalchemy
```

## [](#install-apache-superset)Install Apache Superset

Download and install [Apache Superset](https://superset.apache.org/docs/quickstart) following the official documentation.

## [](#setting-a-secure-connection)Setting a Secure Connection

Couchbase **strongly** recommends that you secure your Superset connection using SSL. This ensures encryption of the communication between Superset and the Couchbase Server/Capella.

* Capella Columnar

For details on creating a Capella Columnar instance, first see [Creating a Capella Columnar Cluster](../../analytics/admin/prepare-project.md).

You'll need to access the Capella administration console to get the connection string for your Columnar database.

1. Sign in to your Capella instance as an `Organization owner` or `Project owner`.
2. Select **Columnar** from the top-level page menu.
3. Select your Columnar cluster from the list.
4. Select **Settings** from the top-level page menu.  
![select columnar cluster settings](_images/select-columnar-cluster-settings.png)
5. Select **Connection String** from the left-hand menu.  
![get capella columnar connection string](_images/get-capella-columnar-connection-string.png)
6. Make a note of the connection string.

Next, you need to add the IP address of the machine from which you're running Superset, so that Capella allows the machine to access the Columnar data.

1. Click on **Allowed IP Addresses** in the left-hand menu.
2. Click the **Add Allowed IP** button.  
![capella columnar add allowed ip](_images/capella-columnar-add-allowed-ip.png)
3. Enter the IP address of the Superset host machine.  
> [!TIP]  
> You can use the **Add Current IP Address** button to fill in the address of the machine currently running the web console.

Now, you will need to create a user account for Superset to access the columnar data.

1. Return to the **Settings** page, then click on **Access Control** in the left-hand menu.
2. Click on **Create Account**.
3. Add a `username` and `password` for the new account.
4. Make sure you set assign `sys_view_reader` to the list of roles.  
![capella columnar user account](_images/capella-columnar-user-account.png)
5. Click **Create Account** to finish setting up the user account.

## [](#configure-the-connection-in-superset)Configure the Connection in Superset

Launch Apache Superset and set up a new database connection. Select Couchbase as the database type and provide the necessary connection details.

* Capella Columnar

1. Open the Superset portal.
2. Add Database Connection:
3. Go to: Settings → Database Connections → Add Database
4. Select Couchbase from the list of databases.

Fill connection details:

| **Host**                  | Fill in the connection string you copied here.              |
| ------------------------- | ----------------------------------------------------------- |
| **Port**                  | Not required.                                               |
| **Database Name**         | Optional; specify the database name if needed.              |
| **Username**              | Enter the username you created in the User Account section. |
| **Password**              | Enter the password you allocated to the user here.          |
| **Display Name**          | Enter a name for this connection.                           |
| **Additional Parameters** | Not required.                                               |
| **SSL**                   | Must be enabled.                                            |

## [](#create-tabular-analytics-view)Create Tabular Analytics View

In Couchbase Analytics, define [Tabular Analytics Views](https://docs.couchbase.com/columnar/sqlpp/5a%5Fviews.html#TAV). These views act as non-materialized views, specifying schemas along with primary and foreign keys for collections or subqueries.

## [](#use-the-couchbase-superset-connector)Use the Couchbase Superset Connector

1. Create an [External Collection](https://docs.couchbase.com/columnar/sqlpp/5%5Fddl%5Fexternal.html) using [video\_games\_sales.json](https://www.kaggle.com/datasets/gregorut/videogamesales) file into Columnar.
2. On querying Select \* from `Default.Default.video_game_sales limit 1`.  
```console  
[  
  {  
   "video_game_sales": {  
     "_columnar_ID": "691c68ce-1dd3-9e94-7a47-c041eb87fe8c",  
     "rank": "74",  
     "name": "Animal Crossing: New Leaf",  
     "platform": "3DS",  
     "year": "2012",  
     "genre": "Simulation",  
     "publisher": "Nintendo",  
     "na_sales": "2.01",  
     "eu_sales": "2.32",  
     "jp_sales": "4.36",  
     "other_sales": "0.41",  
     "global_sales": "9.09"  
   }  
 }  
]  
```
3. To create a tabular analytics view from the `video_game_sales` collection, execute the following command:  
```console  
CREATE OR REPLACE ANALYTICS VIEW  
video_game_sales_1 (_columnar_ID string, rank int, name string, platform string, year string, genre string, publisher string, na_sales double, eu_sales double, jp_sales double, other_sales double, global_sales double)  
DEFAULT NULL PRIMARY KEY (__id)  
NOT ENFORCED AS  
SELECT video_game_sales.* FROM video_game_sales;  
```

### [](#visualization)Visualization

To visualize the data, follow these steps in Apache Superset:

1. Navigate to the Dataset section in the Superset dashboard.
2. From the **DATABASE** drop-down, choose the **Display Name** of the Couchbase connection you configured in Superset.
3. Choose **Default** as the schema.
4. Look for the view named **video\_game\_sales\_1** to proceed with the data visualization.

**Sample Chart 1 - Bar Chart Legacy**

![Bar Chart Legacy](_images/chart-1-bar-chart-legacy.png) 

**Sample Chart 2 - Tree Map**

![Tree map](_images/chart-2-tree-map.png)