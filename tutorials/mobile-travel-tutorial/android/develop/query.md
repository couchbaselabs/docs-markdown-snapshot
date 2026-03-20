---
title: Query
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/develop/query.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:android/develop/query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/android/develop/query.html)

# Query

## [](#overview)Overview

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] includes support for N1QL like query interface. Database can be queried by constructing a query using a Query builder and then executing that query.

The Query interface in Couchbase Lite powerful and includes support for:

* Pattern Matching
* Regex Matching
* Math Functions
* String Manipulation Functions
* Aggregate Functions
* Grouping
* Joins (within single database)
* Sorting
* NilOrMissing properties

## [](#simple-query)Simple Query

The travel app has many instances of querying the database. We will discuss a simple example here.

**Open the file** `app/src/android/java/…​/searchflight/SearchFlightPresenter.java`. We will review the `startsWith(String prefix, String tag)` method.

[SearchFlightPresenter.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/android/app/src/main/java/com/couchbase/travelsample/searchflight/SearchFlightPresenter.java#L53)

```java
@Override
public void startsWith(String prefix, String tag) {
  ...
}
```

The query below **selects** the "name" property in documents **from** the database **where** the **type** property is equal to **airport** and the "airportname" property is equal to the search term.

```java
Database database = DatabaseManager.getDatabase();
Query searchQuery = QueryBuilder
  .select(SelectResult.expression(Expression.property("airportname")))
  .from(DataSource.database(database))
  .where(
    Expression.property("type").equalTo(Expression.string("airport"))
      .and(Expression.property("airportname").like(Expression.string(prefix + "%")))
);
```

Next, the query is executed using the `execute()` method. Each row in the result will contain a single property called "airportname". The final result is passed to the `showAirports` method where the result will be displayed in a `RecyclerView`.

```java
ResultSet rows = null;
try {
    rows = searchQuery.execute();
} catch (CouchbaseLiteException e) {
    Log.e("app", "Failed to run query", e);
    return;
}

Result row;
List<String> data = new ArrayList<>();
while ((row = rows.next()) != null) {
    data.add(row.getString("airportname"));
}
mSearchView.showAirports(data, tag);
```

Try it out

* Log into the Travel Sample Mobile app as "demo" user and password as "password"
* Tap the "Flights" button to make a flight reservation
* In the "From" airport textfield, enter "Detroit"
* Verify that the first item in the drop down list is "Detroit Metro Wayne Co" — see — [Figure 1](#fig%5Fselfromair)

![android simple query](https://cl.ly/0b3q2T2t1R1J/android-simple-query.gif) 

Figure 1\. Airport Selection

## [](#advanced-query)Advanced Query

In this section we will discuss the JOIN query; intra-database joins.

If you recall from the Data Modeling section, the document with a **type** equal to "bookmarkedhotels" contains a **hotels** property which is an array of IDs of bookmarked hotels.

```json
{
  "_id": "hotel1",
  "name": "San Francisco Hotel",
  "address": "123, Park Street, San Francisco"
}

{
  "type": "bookmarkedhotels",
  "hotels": ["hotel1", "hotel2"]
}
```

We will review the query that fetches documents whose `\_id` is included in the "hotels" property array of the document of type "bookmarkedhotels".

**Open the file** `app/src/android/java/…​/hotes/BookmarksPresenter.java`. We will review the `fetchBookmarks()` method.

[BookmarksPresenter.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/android/app/src/main/java/com/couchbase/travelsample/bookmarks/BookmarksPresenter.java#L32)

```java
public void fetchBookmarks() {
  ...
}
```

First, we instantiate two data sources which corresponds to the two sides of the join query.

```java
DataSource bookmarkDS = DataSource.database(database).as("bookmarkDS");
DataSource hotelsDS = DataSource.database(database).as("hotelDS");
```

Next we write the query expressions. The first one gets the `hotels` property on the bookmarks data source. The seconds get the document ID on the hotels data source.

```java
Expression hotelsExpr = Expression.property("hotels").from("bookmarkDS");
Expression hotelIdExpr = Meta.id.from("hotelDS");
```

Next, we use a function expression to find document’s whose `\_id` property is in the `hotels` array. And build the join expression.

```java
Expression joinExpr = ArrayFunction.contains(hotelsExpr, hotelIdExpr);
Join join = Join.join(hotelsDS).on(joinExpr);
```

Finally, the query object uses that join expression to find all the hotel document referenced in the "hotels" array of the bookmark document.

```java
Expression typeExpr = Expression.property("type").from("bookmarkDS");

SelectResult bookmarkAllColumns = SelectResult.all().from("bookmarkDS");
SelectResult hotelsAllColumns = SelectResult.all().from("hotelDS");

Query query = QueryBuilder
  .select(bookmarkAllColumns, hotelsAllColumns)
  .from(bookmarkDS)
  .join(join)
  .where(typeExpr.equalTo(Expression.string("bookmarkedhotels")));
```

We use the `execute()` method to get the results and pass them on to the view.

```java
query.addChangeListener(new QueryChangeListener() {
    @Override
    public void changed(QueryChange change) {
        ResultSet rows = change.getRows();

        List<Map<String, Object>> data = new ArrayList<>();
        Result row = null;
        while((row = rows.next()) != null) {
            Map<String, Object> properties = new HashMap<>();
            properties.put("name", row.getDictionary("hotelDS").getString("name"));
            properties.put("address", row.getDictionary("hotelDS").getString("address"));
            properties.put("id", row.getDictionary("hotelDS").getString("id"));
            data.add(properties);
        }
        mBookmarksView.showBookmarks(data);
    }
});

try {
    query.execute();
} catch (CouchbaseLiteException e) {
    e.printStackTrace();
}
```

Try it out

1. Log into the Travel Sample Mobile app as "Guest" user by selecting "Proceed as Guest"
2. Tap on "Hotels"" button
3. In the "Location" text field, enter "London"
4. In the "Description" text field, enter "Pets"
5. Verify that you see the "Novotel London West" listed
6. Tap to "bookmark" the hotel
7. Verify that the Novatel hotel shows up in the list on the "BookmarksActivity" page — see [Figure 2](#fig-android-bookmark)

![android advanced query](../../_images/android-advanced-query.gif) 

Figure 2\. Bookmarking

---

[1](#%5Ffootnoteref%5F1). From 2.0