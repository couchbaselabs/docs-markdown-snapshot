---
title: The Basics
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/swift/develop/the-basics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:tutorials:mobile-travel-tutorial:swift/develop/the-basics.adoc[]
---

[View original HTML](/tutorials/mobile-travel-tutorial/swift/develop/the-basics.html)

# The Basics

## [](#create-a-database)Create a Database

There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern).

The snippet below creates an empty database for `guest` user in a directory named `guest`.

**Open the file** `DatabaseManager.swift`. We will review the `func openOrCreateDatabaseForGuest( handler:(_ error:Error?)→Void)` method.

[DatabaseManager.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Model/DatabaseManager.swift#L81)

```swift
func openOrCreateDatabaseForGuest( handler:(_ error:Error?)->Void) {
  ...
}
```

We create a folder for the `guest` user database if one does not exist and specify that as the database `directory` in the `DatabaseConfiguration` object.

```swift
var options = DatabaseConfiguration()
guard let defaultDBPath = _applicationSupportDirectory else {
    fatalError("Could not open Application Support Directory for app!")
  return
}
// Create a folder for Guest Account if one does not exist
let guestFolderUrl = defaultDBPath.appendingPathComponent("guest", isDirectory: true)
let guestFolderPath = guestFolderUrl.path
let fileManager = FileManager.default
if !fileManager.fileExists(atPath: guestFolderPath) {
  try fileManager.createDirectory(atPath: guestFolderPath,
                                withIntermediateDirectories: true,
                                attributes: nil)

}

options.directory = guestFolderPath
```

The Couchbase Lite Database is created with the specified name and `DatabaseConfiguration` object

```swift
// Gets handle to existing DB at specified path
_db = try Database(name: kGuestDBName, config: options)
```

Try it out

1. Build and Run the Travel Sample Mobile App
2. On the Login screen select “Proceed as Guest” option.
3. This will log you into the app in Guest Mode. Signing in as Guest will create a new empty database for “guest” account if one does not exist
4. Confirm that you see the "Bookmarked Hotels" page. It will be empty the very first time.

## [](#create-and-update-a-document)Create and Update a Document

Bookmarked hotels are persisted in a separate document with a `type` of `bookmarkedhotels`.

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

**Open the file** `HotelPresenter.swift`. We will review the `func bookmarkHotels(_ hotels: Hotels, handler:@escaping( _ error:Error?)→Void)` method.

[HotelsPresenter.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Presenter/HotelPresenter.swift#L36)

```swift
func bookmarkHotels(_ hotels: Hotels, handler:@escaping( _ error:Error?)->Void) {
    ...
}
```

First, you need to get an instance of the database.

```swift
guard let db = dbMgr.db else {
     handler(TravelSampleError.DatabaseNotInitialized)
  return
}
```

Then fetch documents of type `bookmarkedhotels`. Don’t worry too much about how you query for documents of a specific type from the database. We will examine the Query API in a future lesson.

Create a document of type `bookmarkedhotels` if one does not exist.

```swift
var document = try fetchGuestBookmarkDocumentFromDB(db)?.toMutable()

if document == nil {
  // First time bookmark is created for guest account
  // Create document of type "bookmarkedhotels"
  document = MutableDocument.init(withData: ["type":"bookmarkedhotels","hotels":[String]()])

}
```

Next, retrieve the Ids of hotels to be bookmarked and add it to the current list of bookmarked hotel Ids from the `hotels` property of the `bookmarkedhotels` document.

```swift
// Get the Ids of all hotels that need to be bookmarked
let ids:[String] = hotels.map({ (dict)  in
  if let idVal = dict["id"] as? String {
      return idVal
  }
  return ""
})

// Fetch the current list of bookmarked hotel Ids
var bookmarked = document?.array(forKey: "hotels")

// Add the new hotel ids to the bookmarked hotels array
for newId in ids {
  bookmarked = bookmarked?.addString(newId)
}
```

Update and save the document of type "bookmarkedhotels"

```swift
// Update and save the "bookmarkedhotels" document
if let document = document?.toMutable() {
  // Update and save the bookmark document
  document.setArray(bookmarked, forKey: "hotels")
  try db.saveDocument(document)

}
```

Persist the hotel information as separate documents of type `hotels`. First, determine if the document with the specified hotel Id already exists. If so, update it with the selected hotel details. If not, create a new hotel document.

```swift
// Add the hotel details documents
for hotelDoc in hotels {
  if let idVal = hotelDoc["id"] as? String {
      if let doc = db.document(withID: idVal)?.toMutable() {
          doc.setData(hotelDoc)
          try db.saveDocument(doc)
      }
      else {
          try db.saveDocument(MutableDocument.init(withID: idVal, data: hotelDoc))

      }
  }
}
```

Try it out — Bookmark a Hotel

1. As Guest User, tap on the "hotels" button.
2. In the "location" text field , enter "London".
3. You will see a list of hotels.
4. The list of hotels is pulled from the Couchbase Server via the Travel Sample Web Services API. The list of hotels is not displayed unless there is an open connection the python web app so make sure you have your Travel Sample Web app running.
5. Swipe left on the first hotel cell
6. You will get option to “Bookmark”
7. Tap “bookmark”
8. This should display a "bookmark" icon on the hotel cell
9. Tap "Cancel" button
10. Verify that you see the bookmarked hotel in the “Bookmarked Hotels” screen — see: [Figure 1](#fig-swift-bookmk)A motivation for having separate docs for each bookmarked hotel is if they become sharable between users via the sync function.

![basics add document](../../_images/basics_add_document.gif) 

Figure 1\. Add a Bookmark

## [](#delete-a-document)Delete a Document

A document can be deleted using the `delete` method. This operation actually creates a new `tombstoned` revision in order to propagate the deletion to other clients.

**Open the file** `HotelPresenter.swift`. We will review the `func unbookmarkHotels(_ hotels: Hotels, handler:@escaping( _ error:Error?)→Void)` method.

[HotelsPresenter.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Presenter/HotelPresenter.swift#L98)

```swift
func unbookmarkHotels(_ hotels: Hotels, handler:@escaping( _ error:Error?)->Void) {
  ...
}
```

When searching for hotels in **Guest mode**, the app sends a GET request to the Python Web App which performs a Full-Text Search query on Couchbase Server. Then, if a hotel is bookmarked, it gets inserted in the Couchbase Lite database for offline access. So when the user unbookmarks a hotel, the document needs to be removed from the database. That’s what the code below is doing.

```swift
// Remove unbookmarked hotel documents
for idOfDocToRemove in idsToRemove {
  if let doc = db.document(withID: idOfDocToRemove) {
      try db.deleteDocument(doc)
  }
}
```

In addition to deleting the document of type "hotel" as shown above, the unbookmarking process removes the hotel ID from the `hotels` array in the "bookmarkedhotels" document.

Try it out — Remove Bookmark

1. Follow the steps in [Try it out — Bookmark a Hotel](#lab-swift-bookmk) to bookmark a hotel
2. Confirm that you see the bookmarked hotels in the "Bookmarked Hotels" screen. If not, make sure you go through the instructions in [Try it out — Bookmark a Hotel](#lab-swift-bookmk)
3. Swipe left on a bookmarked hotel cell.
4. You will get an option to “UnBookmark”.
5. Tap "UnBookmark".
6. Verify that the unbookmarked hotel does not show up in the list — see: [Figure 2](#fig-swift-delbookmk)

![basics delete document](../../_images/basics_delete_document.gif) 

Figure 2\. Remove a Bookmark