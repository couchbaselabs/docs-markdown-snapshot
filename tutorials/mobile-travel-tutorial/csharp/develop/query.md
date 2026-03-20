---
title: Query
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/csharp/develop/query.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:csharp/develop/query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/csharp/develop/query.html)

# Query

## [](#overview)Overview

Couchbase Lite 2.0 includes support for N1QL like query interface. Database can be queried by constructing a query using a Query builder and then executing that query.

The Query interface in Couchbase Lite 2.0 is poweful and includes support for the following among others - Pattern Matching - Regex Matching - Math Functions - String Manipulation Functions - Aggregate Functions - Grouping - Joins (within single database) - Sorting - NilOrMissing properties

### [](#implementation-pattern)Implementation Pattern

The `select` clause and `where` clause in the `Query` statement require a `CouchbaseLite.Expression` type. Consider the following query

```csharp
var hotelSearchQuery = Query
    .Select(SelectResult.Expression(Meta.ID),
            SelectResult.Expression(Expression.Property("name")))
    .From(DataSource.Database(UserSession.Database))
    .Where(
        Expression.Property("description").Like("%\(descriptionStr)%")
       .And(Expression.Property("type").EqualTo("hotel"))
       .And(Expression.Property("country").EqualTo(locationStr)
       .Or(Expression.Property("city").EqualTo(locationStr))
       .Or(Expression.Property("state").EqualTo(locationStr))
       .Or(Expression.Property("address").EqualTo(locationStr))))
```

Often types, the same `Expression` may be required across multiple queries. This can quickly become tedious and difficult to maintain. The recommended pattern is to define constants corresponding to the Expressions and to reuse them across queries.

As an example, Open the [AddBookingModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/AddBookingModel.cs#L43)file. This file defines some of the CouchbaseLite expressions that are used for flight reservations

```csharp
private static readonly IExpression AirportNameProperty = Expression.Property("airportname");
private static readonly ISelectResult AirportNameResult = SelectResult.Expression(AirportNameProperty);
private static readonly IExpression FaaProperty = Expression.Property("faa");
private static readonly IExpression IcaoProperty = Expression.Property("icao");
```

## [](#simple-query)Simple Query

The travel app has many instances of querying the database. We will discuss a simple example here.

**Open the file**`AddBookingModel.cs`. We will review the `FetchMatchingAirports` method.

[AddBookingModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/AddBookingModel.cs#L124)

```csharp
public Airports FetchMatchingAirports(string searchStr) {
  ...
}
```

There are 3 different queries in this function body. The query that is ran depends on the length of the search term. You can ignore this specificity, in this section we will look at the 3rd query.

The query below **selects** the "name" property in documents **from** the database **where** the **type** property is equal to **airport** and the "airportname" property is equal to the search term.

```csharp
searchQuery = QueryBuilder
         .Select(AirportNameResult)
         .From(DataSource.Database(UserSession.Database))
         .Where(
             TypeProperty.EqualTo(Expression.String("airport"))
             .And(AirportNameProperty.Like(Expression.String($"{searchStr}%")))
         );
```

Next, the query is executed using the `Run()` method. Each row in the result will contain a single property called "airportname".

```csharp
var results = searchQuery.Execute().ToList();
return results.Select(x => x.GetString("airportname")).Where(x => x != null).ToList();

// Don't forget to Dispose the query object when finished
```

Try it out

1. Log into the Travel Sample Mobile app as “demo” user and password as “password”
2. Tap on "+"" button to make a flight reservation
3. In the “From” airport textfield, enter "San""
4. Verify that the first item in the drop down list is "San Diego Intl" — see: [Figure 1](#fig-net-flightsearch)

  * Note \*\* that this is not currently functioning in Xamarin iOS since the custom drop down view has not been implemented

The screen recording is for UWP app.

![uwp prebuilt](../../_images/uwp_prebuilt.gif) 

Figure 1\. Flight Search \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

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

**Open the file**`BookmarkedHotelModel.cs`. We will review the `FetchBookmarkedHotels` method.

[BookmarkedHotelModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/BookmarkedHotelModel.cs#L76)

```csharp
public Hotels FetchBookmarkedHotels() {
    ...
}
```

First, we instantiate two data sources which corresponds to the two sides of the join query.

```csharp
var bookmarkSource = DataSource.Database(UserSession.Database).As(BookmarkDbName);
var hotelsSource = DataSource.Database(UserSession.Database).As(HotelsDbName);
```

Next we use query expressions. The first one gets the `hotels` property on the bookmarks data source. The seconds get the document ID on the hotels data source.

```csharp
// Static variables of the class
private static readonly IExpression HotelsProperty = Expression.Property("hotels").From(BookmarkDbName);
private static readonly IExpression HotelIdProperty = Meta.ID.From(HotelsDbName);
```

Next, we use a function expression to find document’s whose `\_id` property is in the `hotels` array. And build the join expression.

```csharp
// Static variable of the class
private static readonly IFunction JoinExpression = Function.ArrayContains(HotelsProperty, HotelIdProperty);

// In the function
var join = Join.DefaultJoin(hotelsSource).On(JoinExpression);
```

Finally, the query object uses that join expression to find all the hotel document referenced in the "hotels" array of the bookmark document.

```csharp
using (var query = QueryBuilder
  .Select(AllBookmarks, AllHotels)
  .From(bookmarkSource)
  .Join(join)
     .Where(TypeProperty.EqualTo(Expression.String("bookmarkedhotels")))) {
```

And we use the `Run()` method to get the results back pass them on to the view.

```csharp
var results = query.Execute().ToList();

foreach (var result in results ){
     bookmarkedHotels.Add(result.GetDictionary(HotelsDbName).ToDictionary(x => x.Key, x => x.Value));
}
```

Try it out

1. Log into the Travel Sample Mobile app as "Guest" user by selecting "Proceed as Guest"
2. Tap on "Hotels" button
3. In the "Description" text field, enter "pets"
4. In the "Location" text field, enter "London"
5. Verify that you see the "Novotel London West" listed
6. Right click/tap on the hotel cell. The "Bookmark" button should appear.
7. Tap/click "bookmark" button
8. Tap/click "back" button
9. Verify that the Novatel hotel that you bookmarked earlier shows up in the list

The screen recording is for UWP version of app

![uwp join query](../../_images/uwp_join_query.gif) 

Figure 2\. Bookmark Hotel \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

---

[1](#%5Ffootnoteref%5F1). The screen capture is for UWP version of the app.