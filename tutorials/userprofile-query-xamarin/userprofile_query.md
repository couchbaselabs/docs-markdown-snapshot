---
title: "User Profile Sample: Couchbase Lite Query Introduction"
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/edit/query/content/modules/userprofile-query-xamarin/pages/userprofile_query.adoc
  xref: xref:tutorials:userprofile-query-xamarin:userprofile_query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/userprofile-query-xamarin/userprofile_query.html)

# User Profile Sample: Couchbase Lite Query Introduction

## [](#introduction)Introduction

Couchbase Lite brings powerful querying and Full-Text-Search(FTS) capabilities to the edge.

The query interface is based on [N1QL](https://www.couchbase.com/products/n1ql), Couchbase's declarative query language, which implements the emerging SQL++ standard. If you are familiar with SQL, you will feel right at home with the semantics of the new API.

The query API is designed using the [Fluent API Design Pattern](https://en.wikipedia.org/wiki/Fluent%5Finterface), and it uses method cascading to read to like a Domain Specific Language (DSL). This makes the interface very intuitive and easy to understand.

Couchbase Lite can be used as a standalone embedded database within your iOS, Android, and UWP mobile apps.

What You Will Learn

This tutorial will walk through a simple swift app that will

* Demonstrate how you can bundle, load and use a **_prebuilt_** instance of Couchbase Lite
* Introduce you to the basics of the `QueryBuilder` interface

You can learn more about Couchbase Mobile [here](https://developer.couchbase.com/mobile)

## [](#prerequisites)Prerequisites

This tutorial assumes familiarity with building Xamarin apps and with the basics of Couchbase Lite

* If you are unfamiliar with the basics of Couchbase Lite, it is recommended that you walk through the [Standalone tutorial](../userprofile-standalone-xamarin/userprofile%5Fbasic.md), which covers the fundamentals of using Couchbase Lite as a standalone database
* iOS (Xcode 12.5+)
* Android (SDK 22+)

* git (Optional)  
This is required if you would prefer to pull the source code from GitHub repo.

  * Create a [free github account](https://github.com)if you don't already have one
  * git can be downloaded from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## [](#app-overview)App Overview

We will be working with a very simple "User Profile" app. If you had walked through the [Standalone tutorial](../userprofile-standalone-xamarin/userprofile%5Fbasic.md), you would quickly realize that this version extends the functionality introduced in the version introduced in that tutorial.

This app does the following

* Allows users to log in and create or update his/her user profile information. You could also do this in the [Standalone tutorial](../userprofile-standalone-xamarin/userprofile%5Fbasic.md).
* As part of profile information, users have the ability to select a `University` from a list of possible options.

The list of matching universities is queried (using the new Query API) from a local _prebuilt_ "University" Couchbase Lite database that is bundled in the app. The user profile information is persisted as a `Document` in the local Couchbase Lite database. So subsequently, when the user logs out and logs back in again, the profile information is loaded from the `Database`.

![App Overview](_images/university_app_overview.gif) 

## [](#installation)Installation

Clone the **_query_** branch of the `User Profile Demo` project from GitHub. Type the following command in your terminal

```bash
git clone -b query https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin.git
```

Try it out

1. Open the `UserProfileDemo.sln`. The project would be located at `/path/to/UserProfileDemo/modules/userprofile/examples/src`.  
```bash  
open UserProfileDemo.sln  
```
2. Build the solution using your preferred IDE (e.g. [Visual Studio for Windows or Mac](https://visualstudio.microsoft.com/)) or [directly through command line](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-build?tabs=netcore2x).
3. [Run the app](https://docs.microsoft.com/en-us/xamarin/get-started/first-app/index?pivots=windows)on a device or simulator/emulator.
4. Verify that you see the login screen.  
![User Profile Login Screen Image](_images/user_profile_login.png)

## [](#solution-overview)Solution Overview

The User Profile demo app is a Xamarin.Forms based solution that supports iOS, Android, and UWP mobile platforms. The solution utilizes various design patterns and principles such as [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel), [IoC](https://en.wikipedia.org/wiki/Inversion%5Fof%5Fcontrol), and the Repository Pattern.

The solution consists of seven projects.

* **UserProfileDemo**: A .NET Standard project responsible for maintaining view-level functionality.
* **UserProfileDemo.Core**: A .NET Standard project responsible for maintaining viewmodel-level functionality.
* **UserProfileDemo.Models**: A .NET Standard project consisting of simple data models.
* **UserProfileDemo.Repositories**: A .NET Standard project consisting of repository classes responsible for Couchbase Lite database initialization, interaction, etc.
* **UserProfileDemo.iOS**: A Xamarin.iOS platform project responsible for building the `.ipa` file.
* **UserProfileDemo.Android**: A Xamarin.Android platform project responsible for building the `.apk` file.
* **UserProfileDemo.UWP**: A UWP platform project responsible for building the `.exe` file.

Now that you have an understanding of the solution architecture let's dive into the app!

## [](#couchbase-lite-nuget)Couchbase Lite Nuget

Before diving into the code for the apps, it is important to point out the Couchbase Lite dependencies within the solution. The [Couchbase.Lite Nuget package](https://www.nuget.org/packages/Couchbase.Lite/)is included as a reference within four projects of this solution:

* UserProfileDemo.Repositories
* UserProfileDemo.iOS
* UserProfileDemo.Android
* UserProfileDemo.UWP

The `Couchbase.Lite` Nuget package contains the core functionality for Couchbase Lite. In the following sections you will dive into the capabilities it the package provides.

## [](#data-model)Data Model

Couchbase Lite is a JSON Document Store. A `Document` is a logical collection of named fields and values.The values are any valid JSON types. In addition to the standard JSON types, Couchbase Lite supports some special types like `Date` and `Blob`. While it is not required or enforced, it is a recommended practice to include a _"type"_ property that can serve as a namespace for related.

### [](#the-user-profile-document)The User Profile Document

The app deals with a single `Document` with a _"type"_ property of _"user"_. The document ID is of the form _"user::<email>"_.

An example of a document would be.

```json
{
    "type":"user",
    "name":"Jane Doe",
    "email":"jane.doe@earth.org",
    "address":"101 Main Street",
    "image":CBLBlob (image/jpg),
    "university":"Missouri State University"
}
```

### [](#userprofile-encoding)UserProfile Encoding

The _"user"_ `Document` is encoded to a `class` named _UserProfile_.

```c#
public class UserProfile
{
    public string type => "user";
    public string Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Address { get; set; }
    public byte[] ImageData { get; set; }
    public string Description { get; set; }
    public string University { get; set; }
}
```

### [](#university-document)The University Document

The app comes bundled with a collection of documents of type _"university"_. Each `Document` represents a university.

```json
{
    "type":"university","web_pages": [
      "http://www.missouristate.edu/"
    ],
    "name": "Missouri State University",
    "alpha_two_code": "US",
    "state-province": MO,
    "domains": [
      "missouristate.edu"
    ],
    "country": "United States"
}
```

### [](#university-encoding)University Encoding

The _"university"_ `Document` is encoded to a `class` named _University_.

```c#
public class University
{
    public string Name { get; set; }
    public string Country { get; set; }
}
```

## [](#prebuilt-database)Using a Prebuilt Database

### [](#reasons)Reasons

There are several reasons why you may want to bundle your app with a prebuilt database. This would be suited for data that does not change or change that often, so you can avoid the bandwidth and latency involved in fetching/syncing this data from a remote server. This also improves the overall user experience by reducing the start-up time.

In our app, the instance of Couchbase Lite that holds the pre-loaded _"university"_ data is separate from the Couchbase Lite instance that holds _"user"_ data.

A separate Couchbase Lite instance is not required. However, in our case, since there can be many users potentially using the app on a given device, it makes more sense to keep it separate. This is to avoid duplication of pre-loaded data for every user.

### [](#location)Location

The pre-built database will be in the form of a `cblite` file. It should be be in your app project bundle

iOS

In the `UserProfileDemo.iOS` project, locate the `universities.cblite2` folder at the root

![Prebuilt Database Location](_images/cblite_location_ios.png) 

Android

* In the `UserProfileDemo.Android` cfrtg project, locate the `universities.zip` file within the `Assets` folder. Note that the cblite folder will be extracted from the zip file.  
![Prebuilt Database Location](_images/cblite_location_android.png)

### [](#loading)Loading

* Open the [DatabaseManager.cs](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/query/content/modules/userprofile-query-xamarin/examples/src/UserProfileDemo.Repositories/DatabaseManager.cs)file and locate the `GetDatabaseAsync` method. The prebuilt database is common to all users of the app (on the device). So it will be loaded once and shared by all users on the device.  
```c#  
public async Task<Database> GetDatabaseAsync()  
```
* First, we create an instance of `DatabaseConfiguration` object and specify the path where the database would be located  
```c#  
var options = new DatabaseConfiguration();  
var defaultDirectory = Service.GetInstance<IDefaultDirectoryResolver>().DefaultDirectory();  
options.Directory = defaultDirectory;  
```
* Then we determine if the "universities" database already exists at the specified location. It would not be present if this is the first time we are using the app, in which case, we locate the _"universities.cblite"_ resource within the platform project and we copy it over to the database folder.  
```c#  
// The path to copy the prebuilt database to  
var databaseSeedService = ServiceContainer.GetInstance<IDatabaseSeedService>();  
if (databaseSeedService != null)  
{  
    // Use a (resolved) platform service to copy the database to 'defaultDirectory'  
    await databaseSeedService.CopyDatabaseAsync(defaultDirectory);  
    _database = new Database(_databaseName, options);  
    CreateUniversitiesDatabaseIndexes();  
}  
```  
If the database is already present at the specified Database location, we simply open the database.  
```c#  
_database = new Database(_databaseName, options);  
```

### [](#indexing)Indexing

* Creating indexes for non-FTS based queries is optional. However, in order to speed up queries, you can create indexes on the properties that you would query against. Indexing is handled eagerly.
* In the [**DatabaseManager.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/query/content/modules/userprofile-query-xamarin/examples/src/UserProfileDemo.Repositories/DatabaseManager.cs)file, locate the `CreateUniversitiesDatabaseIndexes` method. We create an index on the `name` and `location` properties of the documents in the _university_ database.  
```c#  
void CreateUniversitiesDatabaseIndexes()  
{  
    _database.CreateIndex("NameLocationIndex",  
                          IndexBuilder.ValueIndex(ValueIndexItem.Expression(Expression.Property("name")),  
                                                  ValueIndexItem.Expression(Expression.Property("location"))));  
}  
```

### [](#closing-the-database)Closing the Database

When a user logs out, we close the pre-built database along with other user-specific databases

* In the [**BaseRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/query/content/modules/userprofile-query-xamarin/examples/src/UserProfileDemo.Repositories/BaseRepository.cs)file, locate the `Dispose` function.  
```c#  
public virtual void Dispose()  
```
* Closing the database is pretty straightforward  
```c#  
_database.Close();  
```

Try It Out

1. Run the app in a simulator
2. Log into the app with any email Id and password. Let's use the values _"demo@example.com"_ and _"password"_ for user Id and password fields respectively. If this is the first time that _any_ user is signing in to the app, the pre-built database will be loaded from the App Bundle. In addition, new user-specific Database will be created / opened.
3. Confirm that the console log output has a message similar to the one below. In my example, I am logging in with a user email Id of _"demo@example.com"_.  
```none  
Will open Prebuilt DB  at path /Users/[user_id]/Library/Developer/CoreSimulator/Devices/[unique_device_id]/data/Containers/Data/Application/[unique_app_id]/Library/Application Support  
2018-05-04 17:04:16.319360-0400 UserProfileDemo[54115:13479070] CouchbaseLite/2.0.0 (Swift; iOS 11.3; iPhone) Build/806 Commit/2f2a2097+CHANGES LiteCore/2.0.0 (806)  
2018-05-04 17:04:16.319721-0400 UserProfileDemo[54115:13479070] CouchbaseLite minimum log level is Verbose  
Will open/create DB  at path /Users/[user_name]/Library/Developer/CoreSimulator/Devices/[unique_device_id]/data/Containers/Data/Application/[unique_app_id]/Library/Application Support/demo@example.com  
```
4. The above log message indicates the location of the Prebuilt database as well as the Database for the user.  
This will normally be within the _Application Support_ folder.
5. Open the folder in your Finder app and verify that a Database with name _"universities"_ exists along with a user specific Database with name _"userprofile"_  
![Database Locations](_images/db_locations.png)

## [](#exploring-the-query-api)Exploring the Query API

The Query API in Couchbase Lite is extensive. In our app, we will be using the `QueryBuilder` API to make a simple _pattern matching_ query using the `like` operator.

### [](#fetching-university-document)Fetching University Document

From the "Your Profile" screen, when the user taps on the "University" cell, a search screen is displayed where the user can enter the search criteria (name and optionally, the location) for the university. When the search criteria is entered, the local _"universities"_ database is queried for the [University](#university-document) documents that match the specified search criteria.

* Open the [**UniversityRepository.cs**](https://github.com/couchbaselabs/userprofile-couchbase-mobile-xamarin/tree/query/content/modules/userprofile-query-xamarin/examples/src/UserProfileDemo.Repositories/UniversityRepository.cs)file and locate the `SearchByName` method.  
```c#  
public async Task<List<University>> SearchByName(string name, string country = null)  
```
* We build the Query using the `QueryBuilder` API that will look for Documents that match the specified criteria.  
```c#  
var whereQueryExpression = Function.Lower(Expression.Property("name")).Like(Expression.String($"%{name.ToLower()}%")); (1)  
if (!string.IsNullOrEmpty(country))  
{  
    var countryQueryExpression = Function.Lower(Expression.Property("country")).Like(Expression.String($"%{country.ToLower()}%")); (2)  
    whereQueryExpression = whereQueryExpression.And(countryQueryExpression);  
}  
var query = QueryBuilder.Select(SelectResult.All()) (3)  
                        .From(DataSource.Database(database)) (4)  
                        .Where(whereQueryExpression); (5)  
```

| **1** | Build a QueryExpression that uses the like operator to look for the specified _"name"_ string in the _"name"_ property. Notice couple of things here:(a) The use of **wildcard "%" operator** to denote that we are looking for the presence of the string anywhere in the _"name"_ property and(b) The use of Function.Lower() to convert the search string into lowercase equivalent. Since like operator does _case-sensitive matching_, we convert the search string and the property value to lowercase equivalents and compare the two. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If the location criteria was specified in the search, then Build a QueryExpression that uses the Like operator to look for the specified _"location"_ string in the _"location"_ property.                                                                                                                                                                                                                                                                                                                                                    |
| **3** | The SelectResult.All() specifies that we are interested in all properties in Documents that match the specified criteria                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **4** | The DataSource.Database(database) specified the Data Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **5** | We include the Where clause that is the logical ANDing of the QueryExpression in <1> and <2>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
* We run the Query by calling the `Execute()` method on the Query that was constructed in the previous step  
```c#  
var results = query.Execute().AllResults();  
if (results?.Count > 0)  
{  
    universities = new List<University>(); (1)  
    foreach (var result in results)  
    {  
        var dictionary = result.GetDictionary("universities");  
        if (dictionary != null)  
        {  
            var university = new University  
            {  
                Name = dictionary.GetString("name"), (2)  
                Country = dictionary.GetString("country") (2)  
            };  
            universities.Add(university);  
        }  
    }  
}  
```

| **1** | Create an instance of [University](#university-document) type                                                                                |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Use specific type getters to fetch property values. The [University](#university-document) instance is populated with these property values. |

Try It Out

1. You should have followed the steps discussed in the "Try It Out" section under [Loading the Prebuilt Database](#prebuilt-database)
2. Tap on the "Select University" button
3. You should see a screen show that allows you enter the search criteria for the university
4. Enter "Missouri" for name . You can optionally enter "United States" for location
5. Confirm that you see a list of universities that match the criteria  
![University List](_images/university_list.gif)
6. Select a university
7. Press "Done" button
8. Confirm that the university you selected shows up as the selected university  
![University Selection](_images/university_selection.gif)
9. You can optionally fill in other entries in the User Profile screen
10. Tap "Done" button
11. Confirm that you see an alert message "Successfully Updated Profile". The Document will be updated this time.
12. Tap "Logout" and log out of the app
13. Log back into the app with the same user credentials you used earlier. In my example, I used _"[demo@example.com](mailto:demo@example.com)"_ and _"password"_. So I will log in with those credentials again.
14. Confirm that you see the profile screen with the _university_ value that you set earlier.  
![Log Out and Log In](_images/profile_update.gif)

## [](#learn-more)Learn More

Congratulations on completing this tutorial!

This tutorial walked you through an example of how to use a pre-built Couchbase Lite database. We looked at a simple Query example. Check out the following links for further details on the Query API.

Further Reading

* [Fundamentals of the Couchbase Lite Query API](https://blog.couchbase.com/sql-for-json-query-interface-couchbase-mobile/)
* [Handling Arrays in Queries](https://blog.couchbase.com/querying-array-collections-couchbase-mobile/)
* [Couchbase Lite Full Text Search API](https://blog.couchbase.com/full-text-search-couchbase-mobile-2-0/)
* [Couchbase Lite JOIN Query](https://blog.couchbase.com/join-queries-couchbase-mobile/)