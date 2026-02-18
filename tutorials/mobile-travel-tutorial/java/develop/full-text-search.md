---
title: Full Text Search
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/java/develop/full-text-search.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tutorials/mobile-travel-tutorial/java/develop/full-text-search.html)

# Full Text Search

## [](#full-text-search)Full Text Search

Couchbase Lite \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] supports Full Text Search (FTS). FTS is accomplished using the `match` query. FTS matches are case-sensitive. In the Travel App, the FTS query is against local "travel-sample" documents that is pre-built with the app.

In order to do FTS queries, an FTS index must be created.

**Open the file**`HotelsDao.java`. We will review the `searchHotelsAsync()` method. This code snippet creates an FTS index on the property named `description`.

[HotelsDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/HotelsDao.java#L59)

```java
  @Nonnull
    private List<Hotel> searchHotelsAsync(@Nonnull String location, @Nonnull String desc) {
        ...
    }
```

```java
    final ResultSet results = QueryBuilder
        .select(SelectResult.expression(Meta.id), SelectResult.all())
        .from(DataSource.database(db.getDatabase()))
        .where(Expression.property(DbManager.PROP_DOC_TYPE).equalTo(Expression.string(Hotel.DOC_TYPE))
        .and(FullTextExpression.index(DbManager.FTS_INDEX_DESC).match(desc)
            .and(Expression.property(Hotel.PROP_ADDRESS).like(Expression.string(loc))
            .or(Expression.property(Hotel.PROP_CITY).like(Expression.string(loc)))
            .or(Expression.property(Hotel.PROP_STATE).like(Expression.string(loc)))
            .or(Expression.property(Hotel.PROP_COUNTRY).like(Expression.string(loc))))))
            .orderBy(Ordering.property(Hotel.PROP_NAME).ascending())
            .execute();
```

This is a fairly involved query expression.

* You will create an FTS `Expressions` using the `match()` operator. In this particular example, the `match` expression looks for the `desc` value in the `description` property.
* This `match` expression is logically ANDed with an `equalTo` comparison expression which looks for the `location` in the `country`,`city`,`state` or `address` properties.
* This expression is then used in the `where` clause of the query the usual way.

We build the query using the different expressions from above and parse the `ResultSet` object into a `List<Hotel>` object

```java
  for (Result result : results.allResults()) {
            if (result.count() < 2) { continue; }
            final Hotel hotel = Hotel.fromDictionary(result.getString(0), result.getDictionary(1));
            if (hotel != null) { hotels.add(hotel); }
        }
```

Try it out

1. Log into the Travel Sample Mobile app as “demo” user and password as “password”
2. Tap on "hotels" button
3. In the description text field enter “Pets”.
4. In the Location text field enter "London" (Note the search is **case sensitive**)
5. Verify that you see one hotel listed named "Novotel London West" — see [Figure 1](#fig-java-hotel-list)

![java fts](../../_images/java-fts.gif) 

Figure 1\. Hotel List

---

[1](#%5Ffootnoteref%5F1). From 2.0