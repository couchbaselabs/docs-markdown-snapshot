---
title: Run a Vector Search with a Couchbase SDK
description: Using a Couchbase SDK, you can run a simple or more complex vector
  search against a Search Vector Index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/vector-search/pages/run-vector-search-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/vector-search/run-vector-search-sdk.html)

# Run a Vector Search with a Couchbase SDK

> Using a Couchbase SDK, you can run a simple or more complex vector search against a Search Vector Index. 

> [!IMPORTANT]
> You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2.
> 
> You can still use other features of the [Search Service](../search/search.md).

> [!TIP]
> Not all available Couchbase SDK languages are covered by the examples on this page.
> 
> For additional Vector Search examples, see the SDK documentation:
> 
> [.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md#vector-search) | [C++](../../../cxx-sdk/current/howtos/vector-searching-with-sdk.md) | [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md#vector-search) | [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md#vector-search) | [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md#vector-search) | [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md#vector-search) | [Scala](../../../scala-sdk/current/howtos/vector-searching-with-sdk.md)

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](../search/run-searches.md#scoring).

## [](#prerequisites)Prerequisites

Choose your preferred programming language to view the applicable prerequisites for the examples on this page.

* Go
* Java
* Python

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).  
> [!TIP]  
> You can download a sample dataset to use with the procedure or examples on this page:  
>  
> [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)  
>  
> To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:  
>  
> * Use a bucket called `vector-sample`.  
> * Use a scope called `color`.  
> * Use a collection called `rgb` for `rgb.json`.  
> * To set your document keys, use the value of the `id` field from each JSON document.  
>  
> For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example).
* You have installed the Couchbase Go SDK.  
For more information about installing and using the Couchbase Go SDK, see [Start Using the Go SDK](../../../go-sdk/current/hello-world/start-using-sdk.md).

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).  
> [!TIP]  
> You can download a sample dataset to use with the procedure or examples on this page:  
>  
> [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)  
>  
> To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:  
>  
> * Use a bucket called `vector-sample`.  
> * Use a scope called `color`.  
> * Use a collection called `rgb` for `rgb.json`.  
> * To set your document keys, use the value of the `id` field from each JSON document.  
>  
> For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example).
* You have installed the Couchbase Java SDK.  
For more information about installing and using the Couchbase Java SDK, see [Hello World](../../../java-sdk/current/hello-world/start-using-sdk.md).

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).  
> [!TIP]  
> You can download a sample dataset to use with the procedure or examples on this page:  
>  
> [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)  
>  
> To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings:  
>  
> * Use a bucket called `vector-sample`.  
> * Use a scope called `color`.  
> * Use a collection called `rgb` for `rgb.json`.  
> * To set your document keys, use the value of the `id` field from each JSON document.  
>  
> For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example).
* You have installed the Couchbase Python SDK.  
For more information about installing and using the Couchbase Python SDK, see [Start Using the Python SDK](../../../python-sdk/current/hello-world/start-using-sdk.md).
* You have created and activated a virtual environment using `venv` and installed packages.  
For more information about how to set up your virtual environment, see [the Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
* You have made a `requirements.txt` file with the following:  
couchbase==4.1.12  
openai==1.12.0
* You have pulled in all dependencies for the Couchbase Python SDK by running:  
pip install -r requirements.txt

## [](#example-searching-for-a-similar-color-vector)Example: Searching for a Similar Color Vector

The sample dataset inside `rgb.json` has small embedding vectors inside the `colorvect_l2` field. These embedding vectors describe a color using RGB values. For example, the color red has an embedding vector of `[255, 0, 0]`.

The following example code searches for the color navy (`[0.0, 0.0, 128.0]`) in the `rgb.json` dataset:

* Go
* Java
* Python

```go
package main

import (
    "fmt"
    "log"
    "time"
    "os"
    "github.com/couchbase/gocb/v2"
    // Include this import if you want to run a Search query using regular Search index features.
    // "github.com/couchbase/gocb/v2/search"
    "github.com/couchbase/gocb/v2/vector"
)
// Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database.
func main() {
    connstr := "couchbases://" + os.Getenv("CB_HOSTNAME") 
    username := os.Getenv("CB_USERNAME")
    password := os.Getenv("CB_PASSWORD")
	// Make sure to change the bucket, and scope names to match where you stored the sample data in your database. 
    bucket_name := "vector-sample"
    scope_name := "color"

    cluster, err := gocb.Connect(connstr, gocb.ClusterOptions{
        Authenticator: gocb.PasswordAuthenticator{
            Username: username,
            Password: password,
        },
        SecurityConfig: gocb.SecurityConfig{
            TLSSkipVerify: true, // Disables TLS certificate verification
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    bucket := cluster.Bucket(bucket_name)
    err = bucket.WaitUntilReady(5*time.Second, nil)
    if err != nil {
        log.Fatal(err)
    }

    scope := bucket.Scope(scope_name)

    request := gocb.SearchRequest{
        VectorSearch: vector.NewSearch(
            []*vector.Query{
			//  You can change the RGB values {0.0, 0.0, 128.0} to search for a different color.
            vector.NewQuery("colorvect_l2", []float32{0.0, 0.0, 128.0}),
        },
        nil,
       ),
    }
	// Change the limit value to return more results. Change the fields array to return different fields from your Search index.
    opts := &gocb.SearchOptions{Limit: 3, Fields: []string{"color"}}

	// Make sure to change the index name to match your Search index. 
    matchResult, err := scope.Search("color-index", request, opts)
    if err != nil {
        log.Fatal(err)
    }

    for matchResult.Next() {
        row := matchResult.Row()
        docID := row.ID
        var fields interface{}
        err := row.Fields(&fields)
        if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("Document ID: %s, Fields: %v\n", docID, fields)
    }

    if err = matchResult.Err(); err != nil {
        log.Fatal(err)
    }
}
```

```Java
import com.couchbase.client.core.error.*;
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import com.couchbase.client.java.json.*;
import com.couchbase.client.java.search.*;
import com.couchbase.client.java.search.queries.*;
import com.couchbase.client.java.search.result.*;
import com.couchbase.client.java.search.vector.*;

import java.time.Duration;
import java.util.Map;

public class RunVectorSearchSimpleColor {

    public static void main(String[] args) {
    // Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database.
	String endpoint = "couchbases://" + System.getenv("CB_HOSTNAME") + "?tls_verify=none"; 
	String username = System.getenv("CB_USERNAME");
	String password = System.getenv("CB_PASSWORD");
    // Make sure to change the bucket, scope, collection, and index names to match where you stored the sample data in your database. 
	String bucketName = "vector-sample";
	String scopeName = "color";
	String collectionName = "rgb";
	String searchIndexName = "color-index";

	try {
	    // Connect to database/cluster with specified credentials
	    Cluster cluster = Cluster.connect(
		    endpoint,
		    ClusterOptions.clusterOptions(username, password).environment(env -> {
			    // Use the pre-configured profile below to avoid latency issues with your connection.
			    env.applyProfile("wan-development");
		    })
	    );

	    Bucket bucket = cluster.bucket(bucketName);
	    bucket.waitUntilReady(Duration.ofSeconds(10));
	    Scope scope = bucket.scope(scopeName);
	    Collection collection = scope.collection(collectionName);

	    SearchRequest request = SearchRequest
	        .create(VectorSearch.create(
                    // Change the floats in the array to search for a different color.
                    VectorQuery.create("colorvect_l2", new float[]{ 0.0f, 0.0f, 128.0f }
                ).numCandidates(3)));
        // Make sure to change the index name to match your Search index. 
	    SearchResult result = scope.search("color-index", request,
        // Change the limit value to return more results. Change the value or values in fields to return different fields from your Search index.
                SearchOptions.searchOptions().limit(3).fields("color","brightness"));

	    for (SearchRow row : result.rows()) {
	      System.out.println("Found row: " + row);
	      System.out.println("   Fields: " + row.fieldsAs(Map.class));
	    } 

	} catch (UnambiguousTimeoutException ex) {
	    boolean authFailure = ex.toString().contains("Authentication Failure");
	    if (authFailure) {
		    System.out.println("Authentication Failure Detected");
	    } else {
		    System.out.println("Error:");
		    System.out.println(ex.getMessage());
	    }
	}
    }
}
```

```python
#!/usr/bin/env python3

import os
import sys
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.search as search
from couchbase.options import SearchOptions
from couchbase.vector_search import VectorQuery, VectorSearch

# You can change the RGB values to search for a different color
vector = [0.0,0.0,128.0]

# Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database.                                                                                                     
pa = PasswordAuthenticator(os.getenv("CB_USERNAME"), os.getenv("CB_PASSWORD"))
cluster = Cluster("couchbases://" + os.getenv("CB_HOSTNAME") + "/?ssl=no_verify", ClusterOptions(pa))
# Make sure to change the bucket, scope, and index names to match where you stored the sample data in your database.  
bucket = cluster.bucket("vector-sample")
scope = bucket.scope("color")
search_index = "color-index"
try:
    search_req = search.SearchRequest.create(search.MatchNoneQuery()).with_vector_search(
        VectorSearch.from_vector_query(VectorQuery('colorvect_l2', vector, num_candidates=3)))
        # Change the limit value to return more results. Change the fields array to return different fields from your Search index.
    result = scope.search(search_index, search_req, SearchOptions(limit=13,fields=["color", "id"]))
    for row in result.rows():
        print("Found row: {}".format(row))
    print("Reported total rows: {}".format(
        result.metadata().metrics().total_rows()))
except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
```

## [](#semantic)Example: Semantic Search with Color Descriptions

> [!NOTE]
> The following code sample requires you to have a paid subscription to the OpenAI API to generate an embedding vector from a sample text string. For more information about pricing for the OpenAI API, see [OpenAI’s Pricing page](https://openai.com/pricing) for embedding models.
> 
> The `rgb.json` sample data contains ready-made embedding vectors for each color’s `description` text. For an example of how to use a ready-made vector with Vector Search, see [Run a Vector Search with the REST API and curl/HTTP](run-vector-search-rest-api.md) or [Run A Vector Search with the Server Web Console](run-vector-search-ui.md).

If you use the sample dataset inside `rgb.json`, you can use the OpenAI API to generate an embedding from any text string.

The following code generates an embedding vector with the question `What color hides everything like the night?`:

* Go
* Java
* Python

```go
package main

import (
    "fmt"
    "log"
    "time"
    "os"
    "github.com/couchbase/gocb/v2"
	// Include this import if you want to run a Search query using regular Search index features.
    // "github.com/couchbase/gocb/v2/search"
    "github.com/couchbase/gocb/v2/vector"
    "bytes"
    "encoding/json"
    "io/ioutil"
    "net/http"
)

type OpenAIResponse struct {
    Data []struct {
        Embedding []float32 `json:"embedding"`
    } `json:"data"`
}

// generateVector makes a request to OpenAI's API to get an embedding vector for the given input text.
// Make sure to replace OPENAI_API_KEY with your own API Key.
func generateVector(inputText string) ([]float32, error) {
    openaiAPIKey := os.Getenv("OPENAI_API_KEY")
    if openaiAPIKey == "" {
        return nil, fmt.Errorf("OPENAI_API_KEY environment variable is not set")
    }

    requestBody, err := json.Marshal(map[string]interface{}{
        "input":  inputText,
        "model": "text-embedding-ada-002",
    })
    if err != nil {
        return nil, fmt.Errorf("error marshaling request body: %w", err)
    }

    request, err := http.NewRequest("POST", "https://api.openai.com/v1/embeddings", bytes.NewBuffer(requestBody))
    if err != nil {
        return nil, fmt.Errorf("error creating request: %w", err)
    }

    request.Header.Set("Content-Type", "application/json")
    request.Header.Set("Authorization", "Bearer "+openaiAPIKey)

    client := &http.Client{}
    response, err := client.Do(request)
    if err != nil {
        return nil, fmt.Errorf("error making request: %w", err)
    }
    defer response.Body.Close()

    if response.StatusCode != http.StatusOK {
        bodyBytes, _ := ioutil.ReadAll(response.Body)
        return nil, fmt.Errorf("API request failed with status %d: %s", response.StatusCode, string(bodyBytes))
    }

    var openAIResponse OpenAIResponse
    if err := json.NewDecoder(response.Body).Decode(&openAIResponse); err != nil {
        return nil, fmt.Errorf("error decoding response: %w", err)
    }

    if len(openAIResponse.Data) == 0 || len(openAIResponse.Data[0].Embedding) == 0 {
        return nil, fmt.Errorf("no embedding vector found in response")
    }

    return openAIResponse.Data[0].Embedding, nil
}
// Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database.
func main() {
    connstr := "couchbases://" + os.Getenv("CB_HOSTNAME") 
    username := os.Getenv("CB_USERNAME")
    password := os.Getenv("CB_PASSWORD")
	// Make sure to change the bucket, and scope names to match where you stored the sample data in your database. 
    bucket_name := "vector-sample"
    scope_name := "color"

    cluster, err := gocb.Connect(connstr, gocb.ClusterOptions{
        Authenticator: gocb.PasswordAuthenticator{
            Username: username,
            Password: password,
        },
        SecurityConfig: gocb.SecurityConfig{
            TLSSkipVerify: true, // Disables TLS certificate verification
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    bucket := cluster.Bucket(bucket_name)
    err = bucket.WaitUntilReady(5*time.Second, nil)
    if err != nil {
        log.Fatal(err)
    }

    scope := bucket.Scope(scope_name)
	// Change the question to whatever you want to ask.
    question := "What color hides everything like the night?"
    vect, err := generateVector(question)
    if err != nil {
        log.Fatalf("Error generating vector: %v", err)
    }

    request := gocb.SearchRequest{
        VectorSearch: vector.NewSearch(
            []*vector.Query{
            vector.NewQuery("embedding_vector_dot", vect),
        },
        nil,
       ),
    }
	// Change the limit value to return more results. Change the fields array to return different fields from your Search index.
    opts := &gocb.SearchOptions{Limit: 2, Fields: []string{"color","description"}}
	
	// Make sure to change the index name to match your Search index. 
    matchResult, err := scope.Search("color-index", request, opts)
    if err != nil {
        log.Fatal(err)
    }

    for matchResult.Next() {
        row := matchResult.Row()
        docID := row.ID
        var fields interface{}
        err := row.Fields(&fields)
        if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("Document ID: %s, Fields: %v\n", docID, fields)
    }

    if err = matchResult.Err(); err != nil {
        log.Fatal(err)
    }
}
```

```java
import com.couchbase.client.core.error.*;
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import com.couchbase.client.java.json.*;
import com.couchbase.client.java.search.*;
import com.couchbase.client.java.search.queries.*;
import com.couchbase.client.java.search.result.*;
import com.couchbase.client.java.search.vector.*;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.List;

import java.time.Duration;
import java.util.Map;

public class RunVectorSearchGenerateEmbed {
    // Make sure to replace OPENAI_API_KEY with your own API Key.
    private static final String OPENAI_API_KEY = System.getenv("OPENAI_API_KEY");
    private static final String OPENAI_URL = "https://api.openai.com/v1/embeddings";

    public static float[] generateVector(String inputText) {
        HttpClient client = HttpClient.newHttpClient();

        JsonObject jsonBody = JsonObject.create()
                .put("input", inputText)
                .put("model", "text-embedding-ada-002");

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(OPENAI_URL))
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer " + OPENAI_API_KEY)
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody.toString()))
                .build();

        try {
            HttpResponse<String> response = client.send(request, BodyHandlers.ofString());

            JsonObject jsonResponse = JsonObject.fromJson(response.body());
            List<Object> embeddingList = jsonResponse.getArray("data")
                .getObject(0)
                .getArray("embedding")
                .toList();

            return toFloatArray(embeddingList);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            return null; // or handle more gracefully
        }
    }

    private static float[] toFloatArray(List<Object> list) {
        float[] result = new float[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = ((Number) list.get(i)).floatValue();
        }
        return result;
    }

    public static void main(String[] args) {
// Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database.
	String endpoint = "couchbases://" + System.getenv("CB_HOSTNAME") + "?tls_verify=none"; 
	String username = System.getenv("CB_USERNAME");
	String password = System.getenv("CB_PASSWORD");
// Make sure to change the bucket, scope, collection, and index names to match where you stored the sample data in your database. 
	String bucketName = "vector-sample";
	String scopeName = "color";
	String collectionName = "rgb";
	String searchIndexName = "color-index";

	try {
	    // Connect to database/cluster with specified credentials
	    Cluster cluster = Cluster.connect(
		    endpoint,
		    ClusterOptions.clusterOptions(username, password).environment(env -> {
			    // Use the pre-configured profile below to avoid latency issues with your connection.
			    env.applyProfile("wan-development");
		    })
	    );

	    Bucket bucket = cluster.bucket(bucketName);
	    bucket.waitUntilReady(Duration.ofSeconds(10));
	    Scope scope = bucket.scope(scopeName);
	    Collection collection = scope.collection(collectionName);
            // Change the question to whatever you want to ask.
            String question = "What color hides everything like the night?";
            float[] vector = generateVector(question);

	    SearchRequest request = SearchRequest
	        .create(VectorSearch.create(
                    VectorQuery.create("embedding_vector_dot", vector).numCandidates(2)));
        // Make sure to change the index name to match your Search index. 
	    SearchResult result = scope.search("color-index", request,
        // Change the limit value to return more results. Change the value or values in fields to return different fields from your Search index.
                SearchOptions.searchOptions().limit(3).fields("color","description"));

	    for (SearchRow row : result.rows()) {
	      System.out.println("Found row: " + row);
	      System.out.println("   Fields: " + row.fieldsAs(Map.class));
	    } 

	} catch (UnambiguousTimeoutException ex) {
	    boolean authFailure = ex.toString().contains("Authentication Failure");
	    if (authFailure) {
		    System.out.println("Authentication Failure Detected");
	    } else {
		    System.out.println("Error:");
		    System.out.println(ex.getMessage());
	    }
	}
    }
}
```

```python
#!/usr/bin/env python3

import os
import sys
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.search as search
from couchbase.options import SearchOptions
from couchbase.vector_search import VectorQuery, VectorSearch
from openai import OpenAI

# Change the question as desired
question = "What color hides everything like the night?"

# Make sure to replace OPENAI_API_KEY with your own API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Make sure to change CB_USERNAME, CB_PASSWORD, and CB_HOSTNAME to the username, password, and hostname for your database. 
pa = PasswordAuthenticator(os.getenv("CB_USERNAME"), os.getenv("CB_PASSWORD"))
cluster = Cluster("couchbases://" + os.getenv("CB_HOSTNAME") + "/?ssl=no_verify", ClusterOptions(pa))
# Make sure to change the bucket, scope, and index names to match where you stored the sample data in your database. 
bucket = cluster.bucket("vector-sample")
scope = bucket.scope("color")
search_index = "color-index"
try:
    vector = client.embeddings.create(input = [question], model="text-embedding-ada-002").data[0].embedding
    search_req = search.SearchRequest.create(search.MatchNoneQuery()).with_vector_search(
        VectorSearch.from_vector_query(VectorQuery('embedding_vector_dot', vector, num_candidates=2)))
        # Change the limit value to return more results. Change the fields array to return different fields from your Search index.
    result = scope.search(search_index, search_req, SearchOptions(limit=13,fields=["color", "description"]))
    for row in result.rows():
        print("Found row: {}".format(row))
    print("Reported total rows: {}".format(
        result.metadata().metrics().total_rows()))
except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
```

## [](#next-steps)Next Steps

You can [create a child field](../search/create-child-field.md) or [use the Quick Index editor](../search/create-quick-index.md) to update your Search Vector Index to include the `description` field with your search results.

For example, you could use the following JSON Search Vector Index payload to create your Search index. It includes two child field mappings, `colorvect_l2` and `embedding_vector_dot` on two different vector fields in the keyspace’s documents. It also adds 3 normal Search index fields (`brightness`, `color`, and `description`) to add more usable data to the Search Vector Index:

```json
{
  "type": "fulltext-index",
  "name": "vector-sample.color.color-index",
  "sourceType": "gocbcore",
  "sourceName": "vector-sample",
  "planParams": {
    "maxPartitionsPerPIndex": 512,
    "indexPartitions": 1
  },
  "params": {
    "doc_config": {
      "docid_prefix_delim": "",
      "docid_regexp": "",
      "mode": "scope.collection.type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_datetime_parser": "dateTimeOptional",
      "default_field": "_all",
      "default_mapping": {
        "dynamic": false,
        "enabled": false
      },
      "default_type": "_default",
      "docvalues_dynamic": false,
      "index_dynamic": false,
      "scoring_model": "bm25",
      "store_dynamic": false,
      "type_field": "_type",
      "types": {
        "color.rgb": {
          "dynamic": false,
          "enabled": true,
          "properties": {
            "brightness": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "index": true,
                  "name": "brightness",
                  "store": true,
                  "type": "number"
                }
              ]
            },
            "color": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "en",
                  "index": true,
                  "name": "color",
                  "store": true,
                  "type": "text"
                }
              ]
            },
            "colorvect_dot": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 3,
                  "index": true,
                  "name": "colorvect_dot",
                  "similarity": "dot_product",
                  "type": "vector"
                }
              ]
            },
            "colorvect_l2": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 3,
                  "index": true,
                  "name": "colorvect_l2",
                  "similarity": "l2_norm",
                  "type": "vector"
                }
              ]
            },
            "description": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "en",
                  "index": true,
                  "name": "description",
                  "store": true,
                  "type": "text"
                }
              ]
            },
            "embedding_vector_dot": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 1536,
                  "index": true,
                  "name": "embedding_vector_dot",
                  "similarity": "dot_product",
                  "type": "vector"
                }
              ]
            }
          }
        }
      }
    },
    "store": {
      "indexType": "scorch",
      "segmentVersion": 16
    }
  },
  "sourceParams": {}
}
```

Run the example in [Example: Semantic Search with Color Descriptions](#semantic) again to see the `description` paragraphs in your results.

If you did not get the search results you were expecting, you can try to recreate your Search Vector Index [with the REST API](create-vector-search-index-rest-api.md).

Search Vector Indexes can use the same settings and features as regular Search indexes. If you want to add additional fields and features to your index, see [Customize a Search Index with the Web Console](../search/customize-index.md).