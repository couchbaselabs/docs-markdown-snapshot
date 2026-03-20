---
title: The Basics
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/csharp/develop/the-basics.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:mobile-travel-tutorial:csharp/develop/the-basics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/csharp/develop/the-basics.html)

# The Basics

## [](#create-a-database)Create a Database

There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern).

The snippet below creates an empty database for a given user in a directory with the same name as the username.

**Open the file**`LoginModel.cs`. We will review the `Task<CouchbaseSession> StartSessionAsync(string username, string password)` method.

[LoginModel.cs](https://github.com/couchbaselabs/mobile-travel-samuwpple/blob/master/dotnet/TravelSample/TravelSample.Core/Models/LoginModel.cs#L54)

```csharp
public async Task<CouchbaseSession> StartSessionAsync(string username, string password) {
  ...
}
```

We create a folder for the user database if one does not exist and specify that as the database `Directory` in the `DatabaseConfiguration` object. Note the use of the service provider to find the default directory for the platform.

```csharp
var options = new DatabaseConfiguration();

// Borrow this functionality from Couchbase Lite
var defaultDirectory = Service.Provider.GetService<IDefaultDirectoryResolver>().DefaultDirectory();
var userFolder = Path.Combine(defaultDirectory, username);
if (!Directory.Exists(userFolder)) {
    Directory.CreateDirectory(userFolder);
}

options.Directory = userFolder;
```

The Couchbase Lite Database is created with specified name and `DatabaseConfiguration` object

```csharp
db = new Database(DbName, options);
```

Try it out

1. Build and Run the Travel Sample Mobile App
2. On Login screen select “Proceed as Guest” option.
3. This will log you into app in Guest Mode. Signing in as Guest will create a new empty database for “guest” account if one does not exist
4. Confirm that you see the “Bookmarked Hotels” page. It will be empty the very first time.

## [](#create-and-update-a-document)Create and Update a Document

Bookmarked hotels are persisted in a separate document with `type` of `bookmarkedhotels`.

The first time a hotel is bookmarked, the `bookmarkedhotels` document is created with the document ID of that hotel document in the `hotels` property. The hotel’s information is persisted in a separate `hotels` type document.

Subsequently, every time a hotel is bookmarked, the process repeats.

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

**Open the file**`HotelListModel.cs`. We will review the `void ToggleBookmark(HotelListCellModel hotel)` method.

[HotelListModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/HotelListModel.cs#L90)

```csharp
public void ToggleBookmark(HotelListCellModel hotel) {
    ...
}
```

Fetch the document of type `bookmarkedhotels`. Don’t worry too much about how you query for document of specific type from the database. We will examine `queries` in a future lesson.

Create document of type `bookmarkedhotels` if one does not exist.

```csharp
using (var document = UserSession.FetchGuestBookmarkDocument()?.ToMutable()) {
  var doc = document;
  if (document == null) {
      ...

      doc = new MutableDocument(new Dictionary<string, object> {["type"] = "bookmarkedhotels"});
  }
```

Next, add the ID of the passed hotel to the current list of bookmarked hotel Ids from the `hotels` property of the `bookmarkedhotels` document, or remove it based on the current action.

```csharp
var bookmarked = doc.GetArray("hotels") ?? new MutableArrayObject();
if (hotel.IsBookmarked) {
    // Remove the bookmark
    for (int i = 0; i < bookmarked.Count(); i++) {
        if (bookmarked.GetString(i) == (hotel.Source.ContainsKey("id") ? hotel.Source["id"] as String : null) ){
            bookmarked.RemoveAt(i);
            break;
        }
    }
} else {
    bookmarked.AddString(hotel.Source.ContainsKey("id") ? hotel.Source["id"] as String : null);
}

doc.SetArray("hotels", bookmarked);
UserSession.Database.Save(doc);
```

Persist the hotel information as separate documents of type `hotels` (or delete it if this is a bookmark removal). First, determine if the document with specified hotel Id already exists. If so, update it with the selected hotel details. If not, create a new hotel document.

```csharp
// Add the hotel details document
if (hotel.Source["id"] is string id) {
    using (var detailDoc = UserSession.Database.GetDocument(id)?.ToMutable() ?? new MutableDocument(id)) {
        detailDoc.SetData(hotel.Source.ToDictionary(x => x.Key, x => x.Value));
          UserSession.Database.Save(detailDoc);
    }
}
```

Try it out — add a bookmark

1. As Guest User, tap on “hotels” button
2. In "location" text field , enter "London"
3. You will see list of hotels.
4. The list of hotels is pulled from the Couchbase Server via the Travel Sample Web Services API. The list of hotels is not displayed unless there is an open connection the python web app so make sure you have your Travel Sample Web app running
5. Right click/tap on the first hotel cell
6. You will see the button to “Bookmark”
7. Tap “bookmark”
8. This should display a "bookmark" icon on the hotel cell
9. Tap "Back" button
10. Verify that you see the bookmarked hotel in the “Bookmarked Hotels” screen — see: [Figure 1](#fig-net-hotelsearch)A motivation for having separate docs for each bookmarked hotel is if they become sharable between users via the sync function.

![uwp basics add document](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/uwp_basics_add_document.gif) 

Figure 1\. Hotel Search \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

## [](#delete-a-document)Delete a Document

A document can be deleted using the `Delete` method. This operation actually creates a new `tombstoned` revision in order to propagate the deletion to other clients.

**Open the file**`BookmarkedHotelModel.cs`. We will review the `public void RemoveBookmark(HotelListCellModel bookmark)` method.

[BookmarkedHotelModel.cs](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/dotnet/TravelSample/TravelSample.Core/Models/BookmarkedHotelModel.cs#L102)

```csharp
public void RemoveBookmark(HotelListCellModel bookmark) {
  ...
}
```

The unbookmarking process removes the hotel Id from the "bookmarkedhotels" document and deletes the unbookmarked "hotels" document from the database. Note that in addition to deleting the "hotels" document, the unbookmarking process updates the "bookmarkedhotels" document by removing the the hotel Id from the `hotels` array.

```csharp
if (bookmark.Source["id"] is string idToRemove) {
    var doc = UserSession.Database.GetDocument(idToRemove);
    if (doc != null) {
        UserSession.Database.Delete(doc);
    }
}
```

Try it out

1. Follow the steps in [Try it out — add a bookmark](#lab-net-bookmk) section to bookmark a hotel
2. Confirm that you see the bookmarked hotels in the "Bookmarked Hotels" screen. If not, make sure you go through the instructions [Try it out — add a bookmark](#lab-net-bookmk) section
3. Right click/tap on the first Hotel cell
4. You will get button to “UnBookmark”
5. Tap “unbookmark”
6. Verify that the unbookmarked hotel does not show up in list — see: [Figure 2](#fig-net-unbookmk)

![uwp basics delete document](../../_images/uwp_basics_delete_document.gif) 

Figure 2\. Remove Hetel Bookmark \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

---

[1](#%5Ffootnoteref%5F1). The screen capture is for UWP version of the app.