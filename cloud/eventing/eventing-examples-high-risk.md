---
title: Generate Credit Card Transaction Alerts
description: Use an Eventing Function to generate high-risk alerts whenever a
  customer makes certain credit card transactions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-examples-high-risk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-examples-high-risk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-examples-high-risk.html)

# Generate Credit Card Transaction Alerts

> Use an Eventing Function to generate high-risk alerts whenever a customer makes certain credit card transactions. 

This page walks you through generating high-risk transaction alerts whenever a credit card transaction exceeds the customer’s available credit limit or are made in a foreign currency.

The `OnUpdate` JavaScript handler listens to mutations or data changes within a specified `register` collection. When you create or modify data in a document of the type `transaction` inside the `register` collection, the Eventing Function executes its JavaScript code.

The Eventing Function then:

* Looks up details from the customer’s card information, like date, spending limits, location, and default currency. This data is collected from the `register` collection and has the type `card`.
* Looks up the exchange rates for the date of the transaction. This data is collected from the `register` collection and has the type `exchange_rates`.
* Transforms the currency of the transaction and the currency of the spending limit into USD, following the correct date’s exchange rate.
* Determines if the customer exceeded the spending threshold.
* Determines if the purchase was made in a foreign currency.
* Generates a new document for high-risk transactions that contains transaction information and calculated data.
* Writes the new document to the `review` collection with type `transaction`.
* (Optional) Uses custom applications written in a Couchbase SDK or a third-party integration like Kafka to read items in the `review` collection. This lets you create more automated actions.

## [](#prerequisites)Prerequisites

Before trying out the examples on this page, you must first:

* Create two buckets called `bulk` and `rr100` with a minimum size of 100MB.
* Inside the `bulk` bucket, create two keyspaces called `bulk.data.register` and `bulk.data.review`.
* Inside the `rr100` bucket, create one keyspace called `rr100.eventing.metadata`.

For more information about creating buckets, scopes, and collections, see [Manage Buckets](../clusters/data-service/manage-buckets.md).

> [!NOTE]
> Do not add, modify, or delete documents in the Eventing storage keyspace `rr100.eventing.metadata` while your Eventing Functions are in a deployed state.

## [](#example-generate-high-risk-credit-card-transaction-alerts)Example: Generate High Risk Credit Card Transaction Alerts

This example walks you through how to create an Eventing Function to cascade delete documents.

### [](#flush-items-from-the-ui)Flush Items from the UI

Flushing clears a bucket of all documents and resets it to an empty state while maintaining the bucket’s configuration and settings.

To enable Capella to flush documents:

1. Go to **Settings** **Buckets**.
2. Click **More Options (⋮)** next to the **bulk** bucket.
3. Click **Settings**.
4. In the **Settings** page, expand the **Advanced Settings** section.
5. Turn on the **Flush** toggle.
6. Click **Save** to save the bucket settings.

For more information about flushing, see [Configure Advanced Bucket Settings](#cloud:data-service:manage-buckets.adoc#configure-advanced-bucket-settings).

### [](#create-indexes)Create Indexes

To create indexes for the **register** and **review** collections:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket.
3. In the code editor, enter the following query to create indexes:  
```sqlpp  
CREATE INDEX `adv_type_rg` ON `bulk`.`data`.`register`(`type`);  
CREATE INDEX `adv_type_rv` ON `bulk`.`data`.`review`(`type`);  
CREATE PRIMARY INDEX `adv_prim_rv` ON `bulk`.`data`.`review`;  
```

### [](#create-an-eventing-function)Create an Eventing Function

To create a new Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **Add Function**.
3. In the **Settings** page, enter the following Function settings:

  * **high\_risk\_txns** under **Name**.
  * **Flag transactions that go over a credit threshold or are made in a foreign currency.** under **Description**.
  * The keyspace `bulk.data.register` under **Listen to Location**.
  * The keyspace `rr100.eventing.metadata` under **Eventing Storage**.
4. Click **Next**.
5. In the **Bindings** page, click **Add Binding** and create two bindings.

  * For the first binding:

    * Select **Bucket**.
    * Enter **register** as the **Alias Name**.
    * Enter the keyspace `bulk.data.register` under **Bucket**, **Scope**, and **Collection**.
    * Select **Read Only** under **Permission**.
  * For the second binding:

    * Select **Bucket**.
    * Enter **review** as the **Alias Name**.
    * Enter the keyspace `bulk.data.review` under **Bucket**, **Scope**, and **Collection**.
    * Select **Read and Write** under **Permission**.
6. Click **Next**.
7. In the code editor, replace the placeholder JavaScript code with the following code sample:  
```javascript  
function OnUpdate(doc, meta) {  
  if (doc.type != "transaction") return;  
  try {  
    var verbose = 0; // logging - 0: minimal, 1: moderate, 2: massive  
    if (verbose > 0) log(meta.id + ' Process transaction for doc.card: ' +  
      doc.card + ', doc.amount: ' + nformat(doc.amount, 0, 2));  
    // Loads the associated card info of this transaction  
    var card = register['card:' + doc.card];  
    if (!card) {  
      log(meta.id + ' warn card does not exist: ' + doc.card);  
      return;  
    }  
    // Loads the exchange rate table for the day of the transaction  
    var erid = 'exchange_rates:er-' + (doc.date).substr(0, 10);  
    var exchange_rates = register[erid];  
    if (!exchange_rates) {  
      log(meta.id + ' WARNING exchange_rates does not exist: ' + erid);  
      return;  
    }  
    var to_USD = exchange_rates['to_USD'];  
    var trxn_2_USD = to_USD[doc.currency];  
    var card_2_USD = to_USD[card['currency']];  
    if (!trxn_2_USD || !card_2_USD) {  
      log(meta.id + ' WARNING exchange_rates for either ' + card['currency'] +  
        ' or ' + doc.currency + ' does exist');  
      return;  
    }  
    // Converts transaction charge and credit card limit into USD  
    var trxn_amount_USD = doc.amount / trxn_2_USD;  
    var card_thresh_USD = card['threshold'] / card_2_USD;  
    if (verbose > 1) {  
      log(meta.id + ' doc   ', doc);  
      log(meta.id + ' card  ', card);  
      log(meta.id + ' rates ', exchange_rates)  
    }  
    if (verbose > 0) {  
      log(meta.id + ' 1 doc.amount       ' + nformat(doc.amount, 8, 2) +  
        ', card_limit       ' + nformat(card['threshold'], 8, 2));  
      log(meta.id + ' 2 trxn_currency    ' + sformat(doc.currency, 8) +  
        ', card_currency    ' + sformat(card['currency'], 8));  
      log(meta.id + ' 3 trxn_2_USD       ' + nformat(trxn_2_USD, 8, 6) +  
        ', card_2_USD       ' + nformat(card_2_USD, 8, 6));  
      log(meta.id + ' 4 trxn_amount_USD  ' + nformat(trxn_amount_USD, 8, 2) +  
        ', card_thresh_USD  ' + nformat(card_thresh_USD, 8, 2));  
    }  
    // Checks if transaction is high risk due to being over threshold limit  
    if (card_thresh_USD < trxn_amount_USD) {  
      var msg = 'High Risk Txn: amount: ' + nformat(doc.amount, 8, 2) + ' ' +  
        doc.currency + ' exceeds purchase threshold: ' +  
        nformat(card['threshold'], 8, 2) + ' ' + card['currency'];  
      log(meta.id + ' *** ' + msg);  
      doc["comments"] = msg; // Appends description to the document  
      doc["reason_code"] = 'X-CREDIT'; // Appends the code to the document  
      delete doc["city"]; // Removes city sub document  
      review[meta.id] = doc; // Saves the modified document for review  
      return;  
    }  
    // Checks if transacton is high risk due to being in a foreign currency  
    if (doc.currency != card['currency']) {  
      var msg = 'High Risk Txn: currency mismatch card: ' +  
        card['currency'] + ' != txn: ' + doc.currency;  
      log(meta.id + ' *** ' + msg);  
      doc["comments"] = msg; // Appends description to the document  
      doc["reason_code"] = 'X-MISMATCH'; // Appends the code to the document  
      delete doc["city"]; // Removes city sub document  
      review[meta.id] = doc; // Saves the modified document for review  
      return;  
    }  
    if (verbose > 0) log(meta.id + ' Charge by ' + card["firstname"] + ' ' +  
      card["lastname"] + ' appears normal in the amount of ' +  
      nformat(doc.amount, 0, 2) + ' ' + doc.currency);  
  } catch (e) {  
    // Notifies the user if there is a processing error or exception  
    log(meta.id + 'ERROR in OnUpdate:', e);  
  }  
}  
// Right justify string with given width  
function sformat(s, width) {  
  var str = s;  
  while (width > str.length) str = ' ' + str;  
  return str;  
}  
// Right justify number with given width with given precision  
function nformat(n, width, prec) {  
  return sformat(n.toFixed(prec), width, prec);  
}  
```
8. Click **Create function** to create your Eventing Function.

When a change happens to the data inside the source collection, the `OnUpdate` handler is triggered and checks if the transaction amount is under the customer’s credit limit and if the transaction has been made in a foreign currency. If any of these conditions are true, the Eventing Function flags the transaction as a high-risk transaction.

The Eventing Function then copies the transaction to the `review` bucket. The `OnUpdate` handler:

* Enriches the document with pre-defined `comments` and provides a `reason code`
* Performs currency validation
* Converts the credit limit and transaction amount to USD currency based on the exchange rate of the exact date of the transaction

### [](#populate-your-cluster-with-sample-data)Populate Your Cluster with Sample Data

To seed your data and populate your cluster, download the following data files:

| Data Set             | Description             | JSON Type Indicator    | Number of Records | File Link                                                         |
| -------------------- | ----------------------- | ---------------------- | ----------------- | ----------------------------------------------------------------- |
| cards.json           | Credit card information | type='card'            | 7                 | [Link](%5Fattachments/examples/high%5Frisk/cards.json)            |
| merchants.json       | Merchant information    | type='merchant'        | 5001              | [Link](%5Fattachments/examples/high%5Frisk/merchants.json)        |
| exchange\_rates.json | Daily exchange rates    | type='exchange\_rates' | 422               | [Link](%5Fattachments/examples/high%5Frisk/exchange%5Frates.json) |
| txns.json            | Credit card charges     | type='transaction'     | 417               | [Link](%5Fattachments/examples/high%5Frisk/txns.json)             |

Right-click the file link and choose **Save Link As…​** to download the files, or right-click the file link and choose **Copy Link Address** to download the files using cURL.

Example 1\. A record from the `cards.json` file, which contains the information from a credit card.

```json
{
  "type": "card",
  "cardnumber": "4273-6623-8686-4599",
  "firstname": "Winfred",
  "lastname": "Raftery",
  "street": "3965 I-80 E Off Ramp",
  "mobile": "+1-617-555-1371",
  "sms": true,
  "city": {
    "name": "Uxbridge",
    "code": "MA",
    "state": "Massachusetts",
    "county": "Worcester",
    "display": "Uxbridge"
  },
  "issued": "11/15",
  "expiry": "6/19",
  "ccv": 736,
  "issuer": "Helena National Bank",
  "maxcredit": 1000,
  "threshold": 9500,
  "country": "US",
  "currency": "USD"
}
```

Example 2\. A record from the `merchants.json` file, which contains the information from the merchant.

```json
{
 "type": "merchant",
 "merchantid": "merchant-501233450539197794-0",
 "name": "FlightAware Inc",
 "city": {
  "name": "Bentonville",
  "code": "IN",
  "state": "Indiana",
  "county": "Fayette",
  "display": "Bentonville"
 }
}
```

Example 3\. A record from the `exchange_rates.json` file, which contains the information from a set of exchange rates.

```json
{
  "type": "exchange_rates",
  "erid": "er-2017-09-01",
  "to_USD": {
    "CAD": 1.2441275168,
    "INR": 64.0331375839,
    "EUR": 0.8389261745,
    "USD": 1,
    "SGD": 1.3545302013,
    "GBP": 0.7724412752,
    "CNY": 6.5591442953,
    "AUD": 1.2601510067
  }
}
```

Example 4\. A record from the `txns.json` file, which contains the information from a transaction or a credit card charge.

```json
{
  "type": "transaction",
  "txnid": "tx-1526311379-002",
  "amount": 15.99,
  "product": "Thread Bore Brush: .22 Caliber, Centerfire",
  "card": "4273-6623-8686-4599",
  "merchant": "GoodGuide Inc",
  "city": {
    "name": "Waseca",
    "code": "MN",
    "state": "Minnesota",
    "county": "Waseca",
    "display": "Otisco"
  },
  "date": "2018-05-14T20:52:59+05:30",
  "currency": "USD"
}
```

After downloading the files, you must import them into your `register` collection. To import them into the collection:

1. Go to **Data Tools** **Import**.
2. Select **Load from your browser**.
3. In the **Choose your source** section, click **Upload** and select the files you want to import.
4. In the **Choose your target** section, select **bulk** for the bucket, **data** for the scope, and **register** for the collection.
5. Click **Import** to import and seed the data.

### [](#deploy-the-eventing-function)Deploy the Eventing Function

To deploy your Eventing Function:

1. Go to **Data Tools** **Eventing**.
2. Click **More Options (⋮)** next to **high\_risk\_txns**.
3. Click **Deploy** to deploy your Function.

After it’s deployed, the Eventing Function executes on all existing documents and any documents you create in the future.

The Eventing Function reads the data you loaded into the `register` collection and creates 40 new high-risk transaction alert documents in the `review` collection.

### [](#check-the-eventing-function-log)Check the Eventing Function Log

To check the Eventing Function log:

1. Go to **Data Tools** **Eventing**.
2. Click the **Log** icon next to the **high\_risk\_txns** Eventing Function. You should see something similar to the following:

2021-07-18T16:00:58.953-07:00 [INFO] "transaction:tx-1511710690-182 *** High Risk Txn: amount: 12506.00 USD exceeds purchase threshold: 12000.00 USD"
2021-07-18T16:00:58.952-07:00 [INFO] "transaction:tx-1505402809-074 *** High Risk Txn: currency mismatch card: USD != txn: EUR"
2021-07-18T16:00:58.938-07:00 [INFO] "transaction:tx-1514648212-166 *** High Risk Txn: amount: 12506.00 USD exceeds purchase threshold: 12000.00 USD"
2021-07-18T16:00:58.934-07:00 [INFO] "transaction:tx-1505315650-406 *** High Risk Txn: currency mismatch card: USD != txn: GBP"

### [](#check-the-results-in-the-review-collection)Check the Results in the `review` Collection

To check that the document in the `review` collection has been updated:

1. Go to **Data Tools** **Documents**.
2. Select the keyspace `bulk.data.review` in the **Get documents from** list. You should see 40 new high-risk alert documents in the `review` collection.
3. Click one of the 40 documents to open the **Edit Document** dialog. The JSON document indicates that a credit card transaction was either made in a currency different than USD, or that it has surpassed the customer’s credit limit.  
```json  
{  
  "type": "transaction",  
  "txnid": "tx-1505315650-403",  
  "amount": 5383.35,  
  "product": "Computer, iMac 64GB 4TB Nvme",  
  "card": "4273-6623-8686-4599",  
  "merchant": "Apple Regent Street",  
  "date": "2018-09-14T20:46:10+05:30",  
  "currency": "GBP",  
  "comments": "High Risk Txn: currency mismatch card: USD != txn: GBP",  
  "reason_code": "X-MISMATCH"  
}  
```

### [](#run-sql-queries-to-return-data)Run SQL++ Queries to Return Data

To run SQL++ queries to return data:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket.
3. In the code editor, enter the following queries:

  * To return the number of high-risk transactions:  
  ```sqlpp  
  SELECT COUNT(*) num_high_risk FROM `bulk`.`data`.`review` WHERE type='transaction';  
  ```
  * To return the data in a specific order:  
  ```sqlpp  
  SELECT * FROM `bulk`.`data`.`review` WHERE type='transaction'  
  ORDER BY currency, amount DESC;  
  ```
  * To return summarized data in a group and in a specific order:  
  ```sqlpp  
  SELECT COUNT(*) count, reason_code, SUM(amount) total_amount, currency  
  FROM `bulk`.`data`.`review` WHERE type='transaction'  
  GROUP BY reason_code, currency ORDER by count DESC;  
  ```
  * To return the transaction records by key:  
  ```sqlpp  
  SELECT * FROM `bulk`.`data`.`register` USE KEYS ('transaction:tx-1505315650-403');  
  ```
  * To return the credit card records by key:  
  ```sqlpp  
  SELECT * FROM `bulk`.`data`.`register` USE KEYS ('card:4273-6623-8686-4599');  
  ```
  * To return the flagged transaction record by key:  
  ```sqlpp  
  SELECT * FROM `bulk`.`data`.`review` USE KEYS ('transaction:tx-1505315650-403');  
  ```

### [](#run-the-eventing-function-again)Run the Eventing Function Again

To run your Eventing Function again:

1. Go to **Data Tools** **Query**.
2. For the **Query Context**, select **bulk** as the bucket.
3. In the code editor, enter the following query to delete all data from the bucket:  
```sqlpp  
DELETE FROM `bulk`.`data`.`review`;  
```
4. Go to **Data Tools** **Eventing**.
5. Click **More Options (⋮)** next to **high\_risk\_txns**.
6. Click **Pause** to pause your Function.
7. Click the **Settings** icon to edit the Function.
8. In the code editor, change `var verbose = 0` to `var verbose = 3`:  
```JavaScript  
function OnUpdate(doc, meta) {  
  if (doc.type != "transaction") return;  
  try {  
    var verbose = 3; // logging - 0: minimal, 1: moderate, 2: massive  
    // ...  
  }  
}  
```
9. Click **Save** to save your edits.
10. In the **Eventing** page, click **More Options (⋮)** next to **high\_risk\_txns**.
11. Click **Resume** to resume your Function. The Function resumes from the checkpoint created when you paused it. It then executes on all new documents and on any mutations that occur after the checkpoint.
12. Go to **Data Tools** **Documents**.
13. Select the keyspace `bulk.data.register` in the **Get documents from** list.
14. Click the document `transaction:tx-1505315650-403` to open the **Edit Document** dialog.
15. Change `"amount": 5383.35` to `"amount": 5383.36`.
16. Click **Save** to create a mutation.
17. Go to **Data Tools** **Eventing**.
18. Click the **Log** icon next to the **high\_risk\_txns** Eventing Function. You should see something similar to the following:

2021-07-18T16:41:20.522-07:00 [INFO] "transaction:tx-1505315650-403 Process transaction for doc.card: 4273-6623-8686-4599, doc.amount: 5383.36"
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 doc   " {"type":"transaction","txnid":"tx-1505315650-403","amount":5383.36,"product":"Computer, iMac 64GB 4TB Nvme","card":"4273-6623-8686-4599","merchant":"Apple Regent Street","city":{"name":"London","code":"W1B 2EL","county":"Westminster","display":"London Westminster"},"date":"2018-09-14T20:46:10+05:30","currency":"GBP"}
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 card  " {"type":"card","cardnumber":"4273-6623-8686-4599","firstname":"Winfred","lastname":"Raftery","street":"3965 I-80 E Off Ramp","mobile":"+1-617-555-1371","sms":true,"city":{"name":"Uxbridge","code":"MA","state":"Massachusetts","county":"Worcester","display":"Uxbridge"},"issued":"11/15","expiry":"6/19","ccv":736,"issuer":"Helena National Bank","maxcredit":1000,"threshold":9500,"country":"US","currency":"USD"}
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 rates " {"type":"exchange_rates","erid":"er-2018-09-14","to_USD":{"CAD":1.3008811703,"INR":71.8162374882,"EUR":0.8555051758,"USD":1,"SGD":1.3698348875,"GBP":0.7633501583,"CNY":6.8543074686,"AUD":1.3910514159}}
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 1 doc.amount        5383.36, card_limit        9500.00"
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 2 trxn_currency         GBP, card_currency         USD"
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 3 trxn_2_USD       0.763350, card_2_USD       1.000000"
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 4 trxn_amount_USD   7052.28, card_thresh_USD   9500.00"
2021-07-18T16:41:20.525-07:00 [INFO] "transaction:tx-1505315650-403 *** High Risk Txn: currency mismatch card: USD != txn: GBP"

The Eventing Function debug log displays the following:

* The transaction document or `doc` that has just mutated
* The credit card or `card` that the customer used to make the transaction
* Daily exchange rates or `rates` for the date of the transaction
* If the transaction is considered high-risk