---
title: "Appendix 4: Example Data"
description: A description of the example data used in the Analytics documentation.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/appendix_4_examples.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/analytics/appendix_4_examples.html)

# Appendix 4: Example Data

In addition to the sample buckets supplied with Couchbase Server, the Analytics documentation also uses the `Commerce` example data described below.

The `Commerce` example data is used in most of the examples for the SQL++ for Analytics language reference. It consists of two collections: [customers](#Customers) and [orders](#Orders).

To install the `Commerce` example data, refer to [Installation](#Install) below.

## [](#Customers)Customers

The `customers` collection contains the following data:

```json
[
    {
        "custid": "C13",
        "name": "T. Cody",
        "address": {
            "street": "201 Main St.",
            "city": "St. Louis, MO",
            "zipcode": "63101"
        },
        "rating": 750
    },
    {
        "custid": "C25",
        "name": "M. Sinclair",
        "address": {
            "street": "690 River St.",
            "city": "Hanover, MA",
            "zipcode": "02340"
        },
        "rating": 690
    },
    {
        "custid": "C31",
        "name": "B. Pruitt",
        "address": {
            "street": "360 Mountain Ave.",
            "city": "St. Louis, MO",
            "zipcode": "63101"
        }
    },
    {
        "custid": "C35",
        "name": "J. Roberts",
        "address": {
            "street": "420 Green St.",
            "city": "Boston, MA",
            "zipcode": "02115"
        },
        "rating": 565
    },
    {
        "custid": "C37",
        "name": "T. Henry",
        "address": {
            "street": "120 Harbor Blvd.",
            "city": "Boston, MA",
            "zipcode": "02115"
        },
        "rating": 750
    },
    {
        "custid": "C41",
        "name": "R. Dodge",
        "address": {
            "street": "150 Market St.",
            "city": "St. Louis, MO",
            "zipcode": "63101"
        },
        "rating": 640
    },
    {
        "custid": "C47",
        "name": "S. Logan",
        "address": {
            "street": "Via del Corso",
            "city": "Rome, Italy"
        },
        "rating": 625
    }
]
```

## [](#Orders)Orders

The `orders` collection contains the following data:

```json
[
    {
        "orderno": 1001,
        "custid": "C41",
        "order_date": "2020-04-29",
        "ship_date": "2020-05-03",
        "items": [
            {
                "itemno": 347,
                "qty": 5,
                "price": 19.99
            },
            {
                "itemno": 193,
                "qty": 2,
                "price": 28.89
            }
        ]
    },
    {
        "orderno": 1002,
        "custid": "C13",
        "order_date": "2020-05-01",
        "ship_date": "2020-05-03",
        "items": [
            {
                "itemno": 460,
                "qty": 95,
                "price": 100.99
            },
            {
                "itemno": 680,
                "qty": 150,
                "price": 8.75
            }
        ]
    },
    {
        "orderno": 1003,
        "custid": "C31",
        "order_date": "2020-06-15",
        "ship_date": "2020-06-16",
        "items": [
            {
                "itemno": 120,
                "qty": 2,
                "price": 88.99
            },
            {
                "itemno": 460,
                "qty": 3,
                "price": 99.99
            }
        ]
    },
    {
        "orderno": 1004,
        "custid": "C35",
        "order_date": "2020-07-10",
        "ship_date": "2020-07-15",
        "items": [
            {
                "itemno": 680,
                "qty": 6,
                "price": 9.99
            },
            {
                "itemno": 195,
                "qty": 4,
                "price": 35
            }
        ]
    },
    {
        "orderno": 1005,
        "custid": "C37",
        "order_date": "2020-08-30",
        "items": [
            {
                "itemno": 460,
                "qty": 2,
                "price": 99.98
            },
            {
                "itemno": 347,
                "qty": 120,
                "price": 22
            },
            {
                "itemno": 780,
                "qty": 1,
                "price": 1500
            },
            {
                "itemno": 375,
                "qty": 2,
                "price": 149.98
            }
        ]
    },
    {
        "orderno": 1006,
        "custid": "C41",
        "order_date": "2020-09-02",
        "ship_date": "2020-09-04",
        "items": [
            {
                "itemno": 680,
                "qty": 51,
                "price": 25.98
            },
            {
                "itemno": 120,
                "qty": 65,
                "price": 85
            },
            {
                "itemno": 460,
                "qty": 120,
                "price": 99.98
            }
        ]
    },
    {
        "orderno": 1007,
        "custid": "C13",
        "order_date": "2020-09-13",
        "ship_date": "2020-09-20",
        "items": [
            {
                "itemno": 185,
                "qty": 5,
                "price": 21.99
            },
            {
                "itemno": 680,
                "qty": 1,
                "price": 20.5
            }
        ]
    },
    {
        "orderno": 1008,
        "custid": "C13",
        "order_date": "2020-10-13",
        "items": [
            {
                "itemno": 460,
                "qty": 20,
                "price": 99.99
            }
        ]
    },
    {
        "orderno": 1009,
        "custid": "C13",
        "order_date": "2020-10-13",
        "items": []
    }
]
```

## [](#Install)Installation

To install the `Commerce` example data:

1. First, use the following links to download the example data to your local system.

  * [Download customers](%5Fattachments/CommerceCustomers.json)
  * [Download orders](%5Fattachments/CommerceOrders.json)
2. If necessary, at the command line, use the [bucket-create](../cli/cbcli/couchbase-cli-bucket-create.md) tool to create a bucket for the example Analytics data:  
couchbase-cli bucket-create \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--bucket-type couchbase \
--bucket-ramsize 100
3. Use the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) tool to create a scope for the `Commerce` data:  
couchbase-cli collection-manage \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--create-scope Commerce
4. Use the [collection-manage](../cli/cbcli/couchbase-cli-collection-manage.md) tool to create a collection for the `customers` data:  
couchbase-cli collection-manage \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--create-collection Commerce.customers
5. Similarly, create a collection for the `orders` data:  
couchbase-cli collection-manage \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--create-collection Commerce.orders
6. Use the [cbimport](../tools/cbimport.md) tool to import the `customers` data to the Data service:  
cbimport json \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--scope-collection-exp Commerce.customers \
--format list \
--generate-key id::#UUID# \
--dataset file:///path/to/CommerceCustomers.json
7. Similarly, import the `orders` data to the Data service:  
cbimport json \
--cluster http://node1:8091 \
--username Administrator \
--password password \
--bucket analytics \
--scope-collection-exp Commerce.orders \
--format list \
--generate-key id::#UUID# \
--dataset file:///path/to/CommerceOrders.json
8. Now, using the Analytics service via the Analytics Workbench or the `cbq` shell, create an Analytics scope to shadow the `Commerce` scope:  
CREATE ANALYTICS SCOPE Commerce IF NOT EXISTS;
9. Create an Analytics collection for the `customers` data:  
CREATE ANALYTICS COLLECTION Commerce.customers  
  ON analytics.Commerce.customers;
10. Create an Analytics collection for the `orders` data:  
CREATE ANALYTICS COLLECTION Commerce.orders  
  ON analytics.Commerce.orders;

The Analytics service ingests the data. You can now use the `Commerce` scope.

## [](#travel-sample)Sample Buckets

The `travel-sample` bucket is used in the Analytics tutorial and the examples for the Data Definition Language.

To install the `travel-sample` bucket, refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).