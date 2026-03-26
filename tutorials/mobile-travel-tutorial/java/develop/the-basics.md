---
title: The Basics
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/java/develop/the-basics.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:mobile-travel-tutorial:java/develop/the-basics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/java/develop/the-basics.html)

# The Basics

## [](#initialization)Initialization

To get started, you must initialize Couchbase Lite with the relevant application context **Open the file** `DatabaseManager.java`. [DatabaseManager.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/DbManager.java#L107)

```java
public DbManager(@Nonnull DbExecutor exec) {
    this.exec = exec;

    CouchbaseLite.init();

    final ConsoleLogger logger = Database.log.getConsole();
    logger.setLevel(LogLevel.DEBUG);
    logger.setDomains(LogDomain.ALL_DOMAINS);
}
```

## [](#create-a-database)Create a Database

There is no limit to how many databases can be created or opened on the device. You can think of a database as a namespace for documents and several databases can be used in the same app (one database per user of the app is a common pattern).

The snippet below creates an empty database for the `guest` user in a directory named `guest`.

**Open the file** `DatabaseManager.java`. We will review the `openGuestDb()` method.

[DatabaseManager.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/DbManager.java#L187)

```java
 public void openGuestDb() {
   ...
 }
```

We create a folder for the `guest` user database if one does not exist and specify that as the database `directory` in the `DatabaseConfiguration` object.

```java
  final DatabaseConfiguration config = new DatabaseConfiguration();
  config.setDirectory(new File(DB_DIR, GUEST_USER).getCanonicalPath());
```

The Couchbase Lite Database is created with specified name and `DatabaseConfiguration` object.

```java
  database = new Database(DB_NAME, config);
```

Try it out

1. Build and Run the Travel Sample Mobile App
2. On the Login screen select the "Proceed as Guest" option.
3. This will log you into the app in Guest Mode. Signing in as Guest will create a new empty database for the "guest" account if one does not exist.
4. Confirm that you see the "Bookmarks" page. It will be empty the very first time.

## [](#create-and-update-a-document)Create and Update a Document

Bookmarked hotels are persisted in a separate document with a `type` of `bookmarkedhotels`.

The first time a hotel is bookmarked, the `bookmarkedhotels` document is created with the document ID of that hotel document in the `hotels` property. The hotel's information is persisted in a separate `hotels` type document.

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

**Open the file** `BookmarkDao.java`. You will review the `addBookmarksAsync` method.

[BookmarkDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/BookmarkDao.java#L104)

```java
@Nullable
    private Void addBookmarksAsync(@Nonnull Set<Hotel> hotels) throws CouchbaseLiteException {
      ...
}
```

First, you need to get an instance of the database.

```java
  final Database database = db.getDatabase();
```

The following snippet persists the hotel instance (`Set<Hotel>`) as a new `Document` in the database. This will allow us to access bookmarked hotel documents while being offline.

```java
  final Set<String> ids = new HashSet<>();
  for (Hotel hotel : hotels) {
  final String id = hotel.getId();

  final Document hotelDoc = database.getDocument(id);
  if (hotelDoc == null) { database.save(Hotel.toDocument(hotel)); }
     ids.add(id);
  }

  bookmarkIds(database, ids);
```

Next you will get the document with ID `user::guest` or create one if it doesn't exist.

This is implemented in the `bookmarkIds` private method.

[BookmarkDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/BookmarkDao.java#L151)

```java
private void bookmarkIds(@Nonnull Set<String> ids) throws CouchbaseLiteException {

  ...
}
```

The document is created with the `type` property set to `bookmarkedhotels` and a new `hotels` array to store the document IDs of the bookmarked hotels.

```java
  final MutableDocument guestDoc = db.getGuestDoc();

  final Set<String> currentBookmarks = new HashSet<>();

  final MutableArray bookmarks = guestDoc.getArray(PROP_BOOKMARKS);
  if (bookmarks != null) {
      for (int i = 0; i < bookmarks.count(); i++) { currentBookmarks.add(bookmarks.getString(i)); }
  }

  currentBookmarks.addAll(ids);
```

Next, the selected hotel's ID is added to the `hotels` array.

```java
  final MutableArray newBookmarks = new MutableArray();
  for (String bookmark : currentBookmarks) { newBookmarks.addString(bookmark); }

  guestDoc.setArray(PROP_BOOKMARKS, newBookmarks);
```

Finally, you will save the document.

```java
  db.getDatabase().save(guestDoc);
```

Try it out

1. As a Guest User, tap on the "ADD" button.
2. In "location" text field , enter "L" as if you were starting to type "London". You will see list of hotels.
3. The list of hotels is pulled from Couchbase Server via the Travel Sample Web Services API. When searching for hotels in **Guest mode**, the app sends a GET request to the Python Web App which performs a Full-Text Search query on Couchbase Server. Search results will not be displayed unless there is an open connection to the Python web app and the Full-Text Search index has been created in Couchbase Server.
4. Tap on the first hotel cell to bookmark it.
5. Click on "ADD" button
6. Click on "DONE" button
7. Verify that you see the bookmarked hotel in the "Bookmarks" screen — see: [Figure 1](#fig-java-save-bookmk)

![java save doc](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/java-save-doc.gif) 

Figure 1\. Save Bookmark

## [](#delete-a-document)Delete a Document

A document can be deleted using the `delete` method. This operation actually creates a new `tombstoned` revision in order to propagate the deletion to other clients.

**Open the file** `BookmarkDao.java`. You will review the `removeBookmarksAsync` method.

[BookmarkDao.java](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/java/TravelSample/src/main/java/com/couchbase/travelsample/db/BookmarkDao.java#L129)

```java
@Override
Void removeBookmarksAsync(@Nonnull Set<Hotel> hotels) throws CouchbaseLiteException {

    ...
}
```

When a hotel is bookmarked, it gets inserted in the Couchbase Lite database for offline access. So when the user unbookmarks a hotel, the document needs to be removed from the database. That's what the code below is doing.

```java
  final Database database = db.getDatabase();

  final Set<String> ids = new HashSet<>();
  for (Hotel hotel : hotels) { ids.add(hotel.getId()); }

  unbookmarkIds(ids);

  for (String id : ids) {
      final Document hotelDoc = database.getDocument(id);
      if (hotelDoc == null) {
          LOGGER.log(Level.WARNING, "Hotel not found in remove bookmark: " + id);
          continue;
      }
      database.delete(hotelDoc);
  }
```

In addition to deleting the document of type "hotel" as shown above, the unbookmarking process removes the hotel ID from the `hotels` array in the "bookmarkedhotels" document.

Try it out

1. On BOOKMARKS page, select the first row to unbookmark
2. Click on "REMOVE" button
3. Verify that you do not see the hotel in the list — see: [Figure 2](#fig-java-unbookmk).

![java unbookmark](https://raw.githubusercontent.com/couchbaselabs/mobile-travel-sample/master/content/assets/java-unbookmark.gif) 

Figure 2\. Remove Hotel Bookmark