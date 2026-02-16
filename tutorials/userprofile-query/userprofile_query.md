[View original HTML](/tutorials/userprofile-query/userprofile_query.html)

## [](#introduction)Introduction

Couchbase Lite brings powerful querying and Full-Text-Search(FTS) capabilities to the edge. The new query interface is based on [N1QL](https://www.couchbase.com/products/n1ql), Couchbase’s declarative query language that extends [SQL](https://www.sqlite.org/index.html) for JSON. If you are familiar with SQL, you will feel right at home with the semantics of the new API. The query API is designed using the [Fluent API Design Pattern](https://en.wikipedia.org/wiki/Fluent%5Finterface), and it uses method cascading to read to like a Domain Specific Language (DSL). This makes the interface very intuitive and easy to understand.

Couchbase Lite can be used as a standalone embedded database within your mobile app.

What You Will Learn

This tutorial will walk through a simple swift app that will

* Demonstrate how you can bundle, load and use a **_prebuilt_** instance of Couchbase Lite
* Introduce you to the basics of the `QueryBuilder` interface

You can learn more about Couchbase Mobile [here](https://developer.couchbase.com/mobile)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building Swift apps with Xcode and with Couchbase Lite.

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you walk through the tutorial _Fundamentals of using Couchbase Lite as a [Standalone](../userprofile-standalone/userprofile%5Fbasic.md) database_
* iOS (Xcode)  
Download the latest version from the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)

|  | If you are on an older version of Xcode, which you need to retain for other development needs, make a copy of your existing version of Xcode and install the latest Xcode version. That way you can have multiple versions of Xcode on your Mac. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
* git (Optional)  
This is required if you would prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com) if you don’t already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## [](#app-overview)App Overview

We will be working with a very simple _User Profile_ app. If you have walked through the [Standalone](../userprofile-standalone/userprofile%5Fbasic.md) tutorial, you will recognize that this version extends the functionality introduced in the app introduced in that tutorial.

This app does the following

* Allows users to log in and create or update his/her user profile information. Just as you could in the [Standalone](../userprofile-standalone/userprofile%5Fbasic.md) tutorial.
* Includes a second record type. As part of profile information, users can now select a "university" from a list of possible options.  
The list of matching universities is found by quering (using the new Query API) a local _prebuilt_ "University" Database, which is bundled in the app.
* The user profile information is persisted as a Document in the local Couchbase Lite Database. So subsquently, when the user logs out and logs back in again, the profile information is loaded from the Database.

![The sample user profile application running in a simulator](_images/university_app_overview.gif) 

Figure 1\. The sample user profile application running in a simulator

## [](#installation)Installation

### [](#fetching-app-source-code)Fetching App Source Code

Clone the **_query_** branch of the `User Profile Demo` project from GitHub. Type the following command in your terminal

```bash
git clone -b query https://github.com/couchbaselabs/userprofile-couchbase-mobile.git
```

### [](#installing-couchbase-lite-xcframework)Installing Couchbase Lite XCFramework

Next, we will download the Couchbase Lite 3.0 XCFramework.

The Couchbase Lite iOS XCFramework is distributed via SPM, CocoaPods, Carthage or you can download the pre-built framework — see the [Get Started - Install](#3.0@couchbase-lite:swift:gs-install.adoc) documentation for more information.

In our example, we will download the pre-built version of the XCFramework, using a script. To do this, type the following in a command terminal:

```bash
cd /path/to/UserProfileDemo/content/modules/userprofile/examples

sh install_tutorial.sh 3.0.0 (1)
```

| **1** | Where 3.0.0 is the required Couchbase Lite release number. |
| ----- | ---------------------------------------------------------- |

Next, let’s verify the installation.

Try it Out

1. Open the `UserProfileDemo.xcodeproj`. The project would be located at `/path/to/UserProfileDemo/content/modules/userprofile/examples`  
```bash  
open UserProfileDemo.xcodeproj  
```
2. Build and run the project using the _simulator_ in Xcode.  
While you can run the app on a real device, we recommend the Simulator so you can see the debug logs in the output console.
3. Verify that you see the login screen

![User Profile Login Screen Image](_images/user_profile_login.png) 

Figure 2\. User Profile Login Screen Image

## [](#data-model)Data Model

Couchbase Lite is a JSON Document Store. A Document is a logical collection of named fields and values. The values are any valid JSON types.

In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related documents.

The app deals with two Document types: _User Profile_ and _University_.

### [](#the-user-profile-document)The User Profile Document

The _User Profile_ Document has a `type` property of _user_ as shown in [Example 1](#ex-user-profile-doc). Its document ID is of the form _"user::demo@example.com"_.

Example 1\. A user profile document

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jame.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg),
    "university":"Rensselaer Polytechnic"
}
```

#### [](#the-user-record)The User Record

The _"user"_ Document is encoded to a native struct named _UserRecord_ as shown in [Example 2](#ex-user-rec)

Example 2\. The encoding of a UserRecord to a native structure

let kUserRecordDocumentType = "user"
typealias ExtendedData = [[String:Any]]
struct UserRecord : CustomStringConvertible{
    let type = kUserRecordDocumentType
    var name:String?
    var email:String?
    var address:String?
    var imageData:Data?
    var university:String?
    var extended:ExtendedData? // future
  
    var description: String {
        return "name = \(String(describing: name)), email = \(String(describing: email)), address = \(String(describing: address)), imageData = \(imageData)"
    }
    

}

### [](#the-university-document)The University Document

The app comes bundled with a collection of Documents of type _"university"_. Each Document represents a university — see [Example 3](#ex-university-doc)

Example 3\. A university document

```json
{
    "type":"university","web_pages": [
      "http://www.rpi.edu/"
    ],
    "name": "Rensselaer Polytechnic Institute",
    "alpha_two_code": "US",
    "state-province": null,
    "domains": [
      "rpi.edu"
    ],
    "country": "United States"
}
```

#### [](#universityrecord)UniversityRecord

The _"university"_ Document is encoded to a native struct named _UniversityRecord_ — as shown in [Example 4](#ex-university-rec)

Example 4\. The encoding of a UniversityRecord to a native structure

```swift
typealias Universities = [UniversityRecord]
// Native object
struct UniversityRecord : CustomStringConvertible{
    
    var alphaTwoCode:String?
    var country:String?
    var domains:[String]?
    var name:String?
    var webPages:[String]?
    
    var description: String {
        return "name = \(String(describing: name)), country = \(String(describing: country)), domains = \(String(describing: domains)), webPages = \(webPages), alphaTwoCode = \(String(describing: alphaTwoCode)) "
    }
    
}
```

## [](#using-a-prebuilt-database)Using a Prebuilt Database

There are several reasons why you may want to bundle your app with a prebuilt database. This would be suited for data that does not change or change that often, so you can avoid the bandwidth and latency involved in fetching/syncing this data from a remote server. This also improves the overall user experience by reducing the start-up time.

In our app, the instance of Couchbase Lite that holds the pre-loaded _"university"_ data is separate from the Couchbase Lite instance that holds _"user"_ data hold the pre-loaded data. A separate Couchbase Lite instance is not required. However, in our case, since there can be many users potentially using the app on a given device, it makes more sense to keep it separate. This is to avoid duplication of pre-loaded data for every user.

### [](#location-of-the-cblite-file)Location of the cblite file

The pre-built database will be in the form of a `cblite` file. It should be be in your app project bundle.

* In the `UserProfileDemo.xcodeproj` project explorer, locate the `universities.cblite2` file  
![Prebuilt Database Location](_images/cblite_location.png)

### [](#loading-the-prebuilt-database)Loading the Prebuilt Database

* Open the **DatabaseManager.swift** file and locate the `openPrebuiltDatabase()` function. The prebuilt database is common to all users of the app (on the device). So it will be loaded once and shared by all users on the device.  
```swift  
func openPrebuiltDatabase(handler:(_ error:Error?)->Void) {  
```
* First, we create an instance of `DatabaseConfiguration` object and specify the path where the database would be located  
```swift  
var options = DatabaseConfiguration()  
guard let universityFolderUrl = _applicationSupportDirectory else {  
    fatalError("Could not open Application Support Directory for app!")  
    return  
}  
let universityFolderPath = universityFolderUrl.path  
let fileManager = FileManager.default  
if !fileManager.fileExists(atPath: universityFolderPath) {  
    try fileManager.createDirectory(atPath: universityFolderPath,  
                                    withIntermediateDirectories: true,  
                                    attributes: nil)  
      
}  
// Set the folder path for the CBLite DB  
options.directory = universityFolderPath  
```
* Then we determine if the "universities" database already exists at the specified location. It would not be present if this is the first time we are using the app, in which case, we locate the _"universities.cblite"_ resource in the App’s main bundle and we copy it over to the Database folder.  
If the database is already present at the specified Database location, we simply open the database.  
```swift  
// Load the prebuilt "universities" database if it does not exist as the specified folder  
if Database.exists(withName: kUniversityDBName, inDirectory: universityFolderPath) == false {  
    // Load prebuilt database from App Bundle and copy over to Applications support path  
    if let prebuiltPath = Bundle.main.path(forResource: kUniversityDBName, ofType: "cblite2") {  
        try Database.copy(fromPath: prebuiltPath, toDatabase: "\(kUniversityDBName)", withConfig: options)  
          
    }  
    // Get handle to DB  specified path  
    _universitydb = try Database(name: kUniversityDBName, config: options)  
      
    // Create indexes to facilitate queries  
    try createUniversityDatabaseIndexes()  
      
}  
else  
{  
    // Gets handle to existing DB at specified path  
    _universitydb = try Database(name: kUniversityDBName, config: options)  
      
}  
```

### [](#indexing-the-prebuilt-database)Indexing the Prebuilt Database

* Creating indexes for non-FTS based queries is optional. However, in order to speed up queries, you can create indexes on the properties that you would query against. Indexing is handled eagerly.
* In the **DatabaseManager.swift** file, locate the `createUniversityDatabaseIndexes()` function. We create an index on the `name` and `location` properties of the documents in the _university_ database.  
```swift  
fileprivate func createUniversityDatabaseIndexes()throws {  
    // For searches on type property  
    try _universitydb?.createIndex(IndexBuilder.valueIndex(items:  ValueIndexItem.expression(Expression.property("name")),ValueIndexItem.expression(Expression.property("location"))), withName: "NameLocationIndex")  
   
}  
```

### [](#closing-the-database)Closing the Database

When a user logs out, we close the Prebuilt Database along with other user-specific databases

* In the **DatabaseManager.swift** file, locate the `closePrebuiltDatabase()` function.  
```swift  
func closePrebuiltDatabase() -> Bool {  
```
* Closing the database is pretty straightforward  
```swift  
try db.close()  
try universitydb.close()  
```

Try Out the App

The app should be running in the simulator.

1. Log into the app with any email Id and password. Let’s use the values _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_ for user Id and password fields respectively. If this is the first time that _any_ user is signing in to the app, the pre-built database will be loaded from the App Bundle. In addition, new user-specific Database will be created / opened.
2. Confirm that the console log output has a message similar to the one shown in [Example 5](#ex-sample-output). This output also indicates the location of the Prebuilt database as well as the Database for the user. This would be within the _Application Support_ folder see: [Figure 3](#img-dbloc)  
In this example, we are logging in with a user email Id of _"[demo@example.com](mailto:demo@example.com)"_.
3. Open the folder in your Finder app and verify that a Database with name _"univerities"_ exists along with a user specific Database with name _"userprofile"_

Example 5\. Sample output

```bash
Will open Prebuilt DB  at path /Users/priya.rajagopal/Library/Developer/CoreSimulator/Devices/E4E62394-9940-4AF8-92FC-41E3C794B216/data/Containers/Data/Application/A9425551-7F52-461D-B4F5-CC04315154D6/Library/Application Support

2018-05-04 17:04:16.319360-0400 UserProfileDemo[54115:13479070] CouchbaseLite/2.0.0 (Swift; iOS 11.3; iPhone) Build/806 Commit/2f2a2097+CHANGES LiteCore/2.0.0 (806)

2018-05-04 17:04:16.319721-0400 UserProfileDemo[54115:13479070] CouchbaseLite minimum log level is Verbose
Will open/create DB  at path /Users/priya.rajagopal/Library/Developer/CoreSimulator/Devices/E4E62394-9940-4AF8-92FC-41E3C794B216/data/Containers/Data/Application/A9425551-7F52-461D-B4F5-CC04315154D6/Library/Application Support/demo@example.com
```

![Database Locations](_images/db_locations.png) 

Figure 3\. Database location

## [](#exploring-the-query-api)Exploring the Query API

The Query API in Couchbase Lite is extensive.

In our app, we will be using the `QueryBuilder` API to make a simple _pattern matching_ query using the `like` operator.

### [](#fetching-university-document)Fetching University Document

From the "Your Profile" screen, when the user taps on the "University" cell, a search screen is displayed where the user can enter the search criteria (name and optionally, the location) for the university.

When the search criteria is entered, the local _"universities"_ Database is queried for [\[The "University" Document\]](#The ) documents that match the specified search criteria.

* Open the **UniversityPresenter.swift** file and locate the `fetchUniversityRecords()` function.  
```swift  
func fetchUniversitiesMatchingName( _ name:String,country countryStr:String?, handler:@escaping(_ universities:Universities?, _ error:Error?)->Void) {  
    do {  
```
* We build the Query using the `QueryBuilder` API that will look for Documents that match the specified criteria.  
```swift  
var whereQueryExpr = Function.lower(Expression.property(UniversityDocumentKeys.name.rawValue))  
    .like(Expression.string("%\(name.lowercased())%")) (1)  
if let countryExpr = countryStr {  
    let countryQueryExpr = Function.lower(Expression.property(UniversityDocumentKeys.country.rawValue))  
        .like(Expression.string("%\(countryExpr.lowercased())%"))  
    whereQueryExpr = whereQueryExpr.and(countryQueryExpr) (2)  
}  
let universityQuery = QueryBuilder.select(SelectResult.all()) (3)  
    .from(DataSource.database(db)) (4)  
    .where(whereQueryExpr) (5)  
print(try? universityQuery.explain())  
```

| **1** | Build a QueryExpression that uses the like operator to look for the specified _"name"_ string in the _"name"_ property. Notice couple of things here:(a) The use of **wildcard "%" operator** to denote that we are looking for the presence of the string anywhere in the _"name"_ property and(b) The use of Function.lowercase() to convert the search string into lowercase equivalent. Since like operator does _case-senstive matching_, we convert the search string and the property value to lowercase equivalents and compare the two. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | If the location criteria was specified in the search, then Build a QueryExpression that uses the like operator to look for the specified _"location"_ string in the _"location"_ property.                                                                                                                                                                                                                                                                                                                                                       |
| **3** | The SelectResult.all() specifiees that we are interested in all properties in Documents that match the specified criteria                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **4** | The DataSource.database(db) specified the Data Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **5** | We include the where clause that is the logical ANDing of the QueryExpression in <1> and <2>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
* We run the Query by calling the `execute()` method on the Query that was constructed in the previous step  
```swift  
var universities = Universities()  
for result in try universityQuery.execute() {  
    if let university = result.dictionary(forKey: "universities"){  
        var universityRecord = UniversityRecord() (1)  
        universityRecord.name =  university.string(forKey: UniversityDocumentKeys.name.rawValue) (2)  
        universityRecord.country  =  university.string(forKey: UniversityDocumentKeys.country.rawValue)  
        universityRecord.webPages  =  university.array(forKey: UniversityDocumentKeys.webPages.rawValue)?.toArray() as? [String] (3)  
        universities.append(universityRecord)  
    }  
}  
```

| **1** | Create an instance of [UniversityRecord](#universityrecord) type                                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Use specific type getters to fetch property values. The [UniversityRecord](#universityrecord) instance is populated with these property values.                                   |
| **3** | Getters also available for array types. This returns a Couchbase Lite ArrayObject type. So you would have to use toArray() to convert the Couchbase Lite native array equivalent. |

Try Out the Query

You should have followed the steps discussed in the "Try It Out" section under [Loading the Prebuilt Database](#loading-the-prebuilt-database)

1. Tap on "University" table cell
2. You should see a screen show that allows you enter the search criteria for the university
3. Enter "Harv" for name . You can optionally enter "united states" for location
4. Confirm that you see a list of universities that match the criteria — see: [Example 6](#ex-try-out-query) — _List_ tab
5. Select a university
6. Press "Done" button
7. Confirm that the university you selected shows up in the University table cell — see: [Example 6](#ex-try-out-query) — _Selection_ tab  
You can optionally fill in other entries in the User Profile screen
8. Tap "Done" button
9. Confirm that you see an alert message "Successfully Updated Profile".  
The Document will be updated this time.
10. Tap "Log Off" and log out of the app
11. Log back into the app with the same user email Id and password that you used earlier. In my example, I used _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_. So I will log in with those credentials again.
12. Confirm that you see the profile screen with the _university_ value that you set earlier — see: [Example 6](#ex-try-out-query) — _Log Off/On_ tab

Example 6\. Try Out the Query

* List
* Selection
* Log Off/On

![University List](https://raw.githubusercontent.com/couchbaselabs/userprofile-couchbase-mobile/query/content/modules/userprofile/assets/images/university_list.gif) 

![University Selection](https://raw.githubusercontent.com/couchbaselabs/userprofile-couchbase-mobile/query/content/modules/userprofile/assets/images/university_selection.gif) 

![Log Off and Log Back On](https://raw.githubusercontent.com/couchbaselabs/userprofile-couchbase-mobile/query/content/modules/userprofile/assets/images/profile_update.gif) 

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to use a pre-built Couchbase Lite database. We looked at a simple Query example. Check out the following links for further details on the Query API including a Xcode playground for testing the APIs.

### [](#further-reading)Further Reading

* [Xcode Playground For Couchbase Lite](https://blog.couchbase.com/xcode-playground-couchbase-mobile/)
* [Fundamentals of the Couchbase Lite Query API](https://blog.couchbase.com/sql-for-json-query-interface-couchbase-mobile/)
* [Handling Arrays in Queries](https://blog.couchbase.com/querying-array-collections-couchbase-mobile/)
* [Couchbase Lite Full Text Search API](https://blog.couchbase.com/full-text-search-couchbase-mobile-2-0/)
* [Couchbase Lite JOIN Query](https://blog.couchbase.com/join-queries-couchbase-mobile/)