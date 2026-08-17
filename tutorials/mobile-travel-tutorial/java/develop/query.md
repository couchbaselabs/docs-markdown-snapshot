---
title: Query
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/java/develop/query.adoc
  xref: xref:tutorials:mobile-travel-tutorial:java/develop/query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/java/develop/query.html)

# Query

## [](#overview)Overview

Couchbase Lite includes support for a N1QL like query interface \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. Database can be queried by constructing a query using a Query builder and then executing that query.

The Query interface in Couchbase Lite is powerful and includes support for the following among others

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

**Open the file** `FlightsDao.java`. We will review the `searchAirportsAsync(@Nonnull String prefix, int maxResults)` method.

[FlightsDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/FlightsDao.java#L114)

```java
@Nonnull
    private List<String> searchAirportsAsync(@Nonnull String prefix, int maxResults) throws CouchbaseLiteException {
  ...
}
```

The query below **selects** the "name" property in documents **from** the database **where** the **type** property is equal to **airport** and the "airportname" property is equal to the search term. The query is executed using the `execute()` method.

```java
  final String target = "%" + prefix + "%";
  final ResultSet results = QueryBuilder.select(SelectResult
      .expression(Expression.property(PROP_AIRPORT_NAME)))
      .from(DataSource.database(db.getDatabase()))
      .where(Expression.property(DbManager.PROP_DOC_TYPE).equalTo(Expression.string(TYPE_AIRPORT))
          .and(Function.lower(Expression.property(PROP_AIRPORT_NAME))
              .like(Function.lower(Expression.string(target))))
          .or(Function.lower(Expression.property(PROP_FAA))
              .like(Function.lower(Expression.string(target)))))
      .orderBy(Ordering.property(PROP_AIRPORT_NAME).ascending())
      .limit(Expression.intValue(maxResults))
      .execute();
```

Each row in the result will contain a single property called "airportname".

```java
final List<String> airports = new ArrayList<>();
for (Result result : results.allResults()) {
    final String airportName = result.getString(PROP_AIRPORT_NAME);
    if (airportName != null) { airports.add(airportName); }
}
```

Try it out

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Click the "FLIGHTS" button to make a flight reservation
3. In the "From" airport textfield, enter "Detroit"
4. Verify that the first item in the drop down list is "Detroit Metro Wayne Co"

![java simple query](../../_images/java-simple-query.gif) 

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

**Open the file**`BookmarkDao.java`. We will review the `queryBookmarksAsync()` method.

[BookmarkDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/BookmarkDao.java#L78)

```java
  @Nonnull
  private List<Hotel> queryBookmarksAsync() throws CouchbaseLiteException {
    ...
  }
```

The query object uses a join expression to find all the hotel document referenced in the "hotels" array of the bookmark document.

```java
  final ResultSet results = QueryBuilder
      .select(SelectResult.all().from("bookmark"), SelectResult.all().from("hotel"))
      .from(DataSource.database(database).as("bookmark"))
      .join(Join.join(DataSource.database(database).as("hotel"))
          .on(ArrayFunction.contains(Expression.property(PROP_BOOKMARKS)
              .from("bookmark"), Meta.id.from("hotel"))))
      .where(Expression.property(DbManager.PROP_DOC_TYPE).from("bookmark")
          .equalTo(Expression.string(DbManager.DOC_TYPE_HOTEL_BOOKMARKS)))
      .execute();
```

We use the `execute()` method to get the results back

```java
 for (Result result : results) {
            final Hotel hotel = Hotel.fromDictionary(result.getDictionary(1));
            if (hotel != null) { bookmarks.add(hotel); }
        }
```

Try it out

1. Log into the Travel Sample Mobile app as "Guest" user by selecting "Proceed as Guest"
2. Click on "ADD"" button
3. In the "Location" text field, enter "London"
4. In the "Description" text field, enter "Pets"
5. Verify that you see the "Novotel London West" listed
6. Select the entry by clicking on it
7. Click "DONE" button to bookmark
8. Verify that the Novatel hotel shows up in the list on the "Bookmarks" page — see [Figure 1](#fig-java-adv-query)

![java advanced query](../../_images/java-advanced-query.gif) 

Figure 1\. Advanced Query

---

[1](#%5Ffootnoteref%5F1). From 2.0