---
title: Add Autocomplete to Your Application
description: Use autocomplete to add suggestions for a user's Search query as
  they type in your application.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/search-query-auto-complete-code.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:search:search-query-auto-complete-code.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/search-query-auto-complete-code.html)

# Add Autocomplete to Your Application

> Use autocomplete to add suggestions for a user’s Search query as they type in your application. 

After you [create and configure a Search index that supports autocomplete](search-query-auto-complete-ui.md), configure your application to return results from the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* You have created a compatible Search index. For more information, see [Configure an Autocomplete Search Index](search-query-auto-complete-ui.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you created the Search index.
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).

## [](#procedure)Procedure

To add autocomplete with the Search Service to your application:

1. To test that your Search index was configured correctly, do one of the following:

  1. [Run a Search query from the REST API](simple-search-rest-api.md) with 2-8 characters in the `query` property.
  2. [Run a Search query from the Web Console](simple-search-ui.md) with 2-8 characters in the **Search** field.  
For example, with the `travel-sample` bucket, you could enter the strings `Be`, `Bea`, `Beau`, and `Beauf` to find a document with the text `Beaufort Hotel`.
2. Configure your application to return results from the Search Service.  
The following examples simulate a user typing an input string and return search results for each partial string:

  * C#
  * Go
  * Java
  * JavaScript
  * Python  
```csharp  
using Couchbase;  
using Couchbase.Search.Queries.Simple;  
await using var cluster = await Cluster.ConnectAsync(new ClusterOptions  
{  
    ConnectionString = "CB_HOSTNAME",  
    UserName = "CB_USERNAME",  
    Password = "CB_PASSWORD",  
    Buckets = new List<string>{"travel-sample"}  
}.ApplyProfile("wan-development"));  
var searchString = "Beaufort Hotel";  
for (var i = 2; i <= 8; i++)  
{  
    var lettersEntered = searchString.Substring(0, i);  
    Console.WriteLine($"Input <{lettersEntered}>, len: {lettersEntered.Length}");  
    await FtsMatchPrefix(lettersEntered);  
}  
async Task FtsMatchPrefix(string letters)  
{  
    try  
    {  
        var results = await cluster.SearchQueryAsync("e-ngram-2-8",  
            new QueryStringQuery(letters),  
            options =>  
            {  
                options.Limit(8);  
                options.Fields("name");  
            });  
        results.Hits.ToList().ForEach(row => { Console.WriteLine($"{row.Id}, {row.Fields}"); });  
        Console.WriteLine(results);  
    }  
    catch (Exception e)  
    {  
        Console.WriteLine(e);  
    }  
}  
```  
```go  
package main  
import (  
    "os"  
    "fmt"  
    "math"  
    "log"  
    "github.com/couchbase/gocb/v2"  
    "github.com/couchbase/gocb/v2/search"  
)  
func main() {  
    cluster, err := gocb.Connect(  
	os.Getenv("CB_HOSTNAME"),  
	gocb.ClusterOptions{  
        Authenticator: gocb.PasswordAuthenticator{  
            Username: os.Getenv("CB_USERNAME"),  
            Password: os.Getenv("CB_PASSWORD"),  
        },  
    })  
    if err != nil {  
        log.Fatal(err)  
    }  
    iterStr := "Beaufort Hotel"  
    maxsz := int(math.Min(float64(len(iterStr)), float64(8)))  
    for i := 2;  i <= maxsz; i++ {  
        testStr := iterStr[0:i]  
	fmt.Printf("Input <%s>, len: %d\n", testStr, len(testStr));  
	results, err := cluster.SearchQuery(  
	    "e-ngram-2-8",  
	    search.NewQueryStringQuery(testStr),  
	    &gocb.SearchOptions { Fields: []string{"name"}, Limit: 8, },  
	)  
	if err != nil {  
	    log.Fatal(err)  
	}  
	for results.Next() {  
	    row := results.Row()  
	    docID := row.ID  
	    var fields interface {}  
	    err := row.Fields( & fields)  
	    if err != nil {  
		panic(err)  
	    }  
	    fmt.Printf("Document ID: %s, fields: %v\n", docID, fields)  
	}  
	err = results.Err()  
	if err != nil {  
	    log.Fatal(err)  
	}  
    }  
}  
```  
```java  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.search.SearchOptions;  
import com.couchbase.client.java.search.SearchQuery;  
import com.couchbase.client.java.search.result.SearchResult;  
import com.couchbase.client.java.search.result.SearchRow;  
public class MockTypeAheadEnGram {  
  static String connstrn = System.getenv("CB_HOSTNAME");  
  static String username = System.getenv("CB_USERNAME");  
  static String password = System.getenv("CB_PASSWORD");  
    
  public static void main(String... args) {  
    Cluster cluster = Cluster.connect(connstrn, username, password);  
      
    String iterStr = "Beaufort Hotel";  
    for (int i=2; i<=Math.min(8, iterStr.length());i++) {  
    	String testStr = iterStr.substring(0, i);  
    	System.out.println("Input <" + testStr + ">, len: " + testStr.length());  
      
    	SearchQuery query = SearchQuery.queryString(testStr);  
    	SearchOptions options = SearchOptions.searchOptions().limit(8).skip(0).explain(false).fields("name");  
    	SearchResult result = cluster.searchQuery("e-ngram-2-8" , query, options);  
    	for (SearchRow row : result.rows()) {  
    		System.out.println(row.id() + "," + row.fieldsAs(JsonObject.class) );  
    	}  
    }  
  }  
}  
```  
```javascript  
const couchbase = require('couchbase')  
const main = async () => {  
  const hostname = process.env.CB_HOSTNAME  
  const username = process.env.CB_USERNAME  
  const password = process.env.CB_PASSWORD  
  const bucketName = 'travel-sample'  
  const cluster = await couchbase.connect(hostname, {username: username, password: password })  
  const ftsMatchPrefix = async (term) => {  
    try {  
      const result =  await cluster.searchQuery(  
        "e-ngram-2-8",  
        couchbase.SearchQuery.queryString(term), { limit: 8, fields: ["name"] }  
      )  
      result.rows.forEach((row) => { console.log(row.id,row.fields)})  
    } catch (error) {  
      console.error(error)  
    }  
  }  
  const inputStr = "Beaufort Hotel"  
  for (let i = 2; i <= 8; i++) {  
    var testStr = inputStr.substring(0, i);  
    console.log("Input <" + testStr + ">, len: " + testStr.length)  
    const res = await ftsMatchPrefix(testStr)  
  }  
}  
main()  
```  
```python  
from couchbase.cluster import Cluster, ClusterOptions  
from couchbase.auth import PasswordAuthenticator  
from couchbase.exceptions import CouchbaseException  
import couchbase.search as search  
import os  
username = os.getenv("CB_USERNAME", default=None)  
password = os.getenv("CB_PASSWORD", default=None)  
hostname = os.getenv("CB_HOSTNAME", default=None)  
cluster = Cluster.connect(  
    "couchbase://" + hostname,  
    ClusterOptions(PasswordAuthenticator(username,password)))  
try:  
    inputStr = "Beaufort Hotel"  
    for i in range(2, min(8,len(inputStr))):  
        testStr = inputStr[0:i]  
        print("Input <" + testStr + ">, len: " + str(len(testStr)));  
        result = cluster.search_query(  
            "e-ngram-2-8",  
            search.QueryStringQuery(testStr),  
            search.SearchOptions(limit=8, fields=["name"]))  
        for row in result.rows():  
            print(row.id,row.fields)  
except CouchbaseException as ex:  
    import traceback  
    traceback.print_exc()  
```

## [](#next-steps)Next Steps

After you add autocomplete to your application, to improve your search results, you can:

* [Customize your Search index with the Web Console](customize-index.md).
* Change the [JSON payload](search-index-params.md) for your Search index.