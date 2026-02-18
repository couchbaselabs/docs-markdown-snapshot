---
title: Full Text Search
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/android/develop/full-text-search.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tutorials/mobile-travel-tutorial/android/develop/full-text-search.html)

# Full Text Search

## [](#full-text-search)Full Text Search

_Couchbase Lite_ \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] supports Full Text Search (FTS). FTS is accomplished using the `match` query. FTS matches are case-insensitive. In the Travel App, the FTS query is against local pre-built "travel-sample" database.

In order to do FTS queries, an FTS index must be created.

**Open the file**`app/src/android/java/…​/util/DatabaseManager.java`. We will review the `createFTSQueryIndex()` method. This code snippet creates an FTS index on the property named `description`.

[DatabaseManager.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/android/app/src/main/java/com/couchbase/travelsample/util/DatabaseManager.java#L76)

```java
private void createFTSQueryIndex() {
    try {
        database.createIndex("descFTSIndex", IndexBuilder.fullTextIndex(FullTextIndexItem.property("description")));
    } catch (CouchbaseLiteException e) {
        e.printStackTrace();
    }
}
```

Next you will write an FTS query that uses the index.

**Open the file**`app/src/android/java/…​/hotels/HotelsPresenter.java`. We will review the `queryHotels(String location, String description)` method.

[HotelsPresenter.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/android/app/src/main/java/com/couchbase/travelsample/hotels/HotelsPresenter.java)

```java
@Override
public void queryHotels(String location, String description) {
  ...
}
```

First, you get an instance of the database.

```java
Database database = DatabaseManager.getDatabase();
```

Next, you will create an FTS `Expressions` using the `match()` operator. In this particular example, the `match` expression looks for the `desciptionStr` value in the `description` property. This `match` expression is logically ANDed with an `equalTo` comparison expression which looks for the `location` in the `country`,`city`,`state` or `address` properties. This expression is then used in the `where` clause of the query the usual way.

```java
Expression descExp = FullTextFunction.match("descFTSIndex", description) ;

Expression locationExp = Expression.property("country")
  .like(Expression.string("%" + location + "%"))
  .or(Expression.property("city").like(Expression.string("%" + location + "%")))
  .or(Expression.property("state").like(Expression.string("%" + location + "%")))
  .or(Expression.property("address").like(Expression.string("%" + location + "%")));

Expression searchExp = descExp.and(locationExp);

Query hotelSearchQuery = QueryBuilder
  .select(SelectResult.all())
  .from(DataSource.database(database))
  .where(
      Expression.property("type").equalTo(Expression.string("hotel")).and(searchExp)
);
```

We build the query using the different expressions from above and transform the `ResultSet` object into a `List<Map<String, Object>>` object that is passed to the `RecyclerView`.

```java
ResultSet rows = null;
try {
    rows = hotelSearchQuery.execute();
} catch (CouchbaseLiteException e) {
    e.printStackTrace();
    return;
}

List<Map<String, Object>> data = new ArrayList<Map<String, Object>>();
Result row = null;
while((row = rows.next()) != null) {
    Map<String, Object> properties = new HashMap<String, Object>();
    properties.put("name", row.getDictionary("travel-sample").getString("name"));
    properties.put("address", row.getDictionary("travel-sample").getString("address"));
    data.add(properties);
}
mHotelView.showHotels(data);
```

Try it out

1. Log into the Travel Sample Mobile app as “demo” user and password as “password”
2. Tap on "hotels" button
3. In the description text field enter "\`Pets.
4. In the Location text field enter "London"
5. Verify that you see one hotel listed named "Novotel London West"

![android fts](https://cl.ly/192b1z2s3S3t/android-fts.gif) 

Figure 1\. Hotel List

---

[1](#%5Ffootnoteref%5F1). From 2.0