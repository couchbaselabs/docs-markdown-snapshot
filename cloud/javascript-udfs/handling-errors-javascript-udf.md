[View original HTML](/cloud/javascript-udfs/handling-errors-javascript-udf.html)

> You can handle errors in JavaScript user-defined functions with the same standard exception mechanism you would use in any JavaScript code. 

For more information about user-defined functions in Capella, see [User-Defined Functions with JavaScript](../guides/javascript-udfs.md).

You can also choose to handle errors [with the runtime](#runtime) or [with your JavaScript function](#function).

SQL++ also supports using the [ABORT()](../n1ql/n1ql-language-reference/metafun.md#abort) function inside a query or a user-defined function to return an error.

## [](#runtime)Handle Errors with the Runtime

If you run into an error during the execution of a SQL++ statement, you can handle those errors with the runtime.

The runtime returns a JSON object with the details of the error that occurred. For example, if you execute a record insertion function with a key that already exists:

```sqlpp
EXECUTE FUNCTION AddAirlineWithDate(1220, 'Raz Air', 'RAZ-AIR', 'United Kingdom');
```

then an error object is returned:

```json
[
  {
    "code": 10109,
    "msg": "Error executing function 'AddAirlineWithDate' (MyLibrary:addAirlineWithDate)",
    "reason": {
      "details": {
        "Code": "    var q = N1QL('insert into `travel-sample`.`inventory`.`airline` values(\\n' +", 
        "Exception": {
          "caller": "couchbase:2098",
          "cause": {
            "caller": "couchbase:1971",
            "code": 17012,
            "key": "dml.statement.duplicatekey",
            "message": "Duplicate Key: airline_1220"
          },
          "code": 12009,
          "icause": "Duplicate Key: airline_1220",
          "key": "datastore.couchbase.DML_error",
          "message": "DML Error, possible causes include concurrent modification. Failed to perform INSERT on key airline_1220",
          "retry": false
        },
        "Location": "functions/MyLibrary.js:11",
        "Stack": "   at addAirlineWithDate (functions/MyLibrary.js:11:13)"
      },
      "type": "Exceptions from JS code"
    }
  }
]
```

## [](#function)Handle Errors with the Function

In most cases, it’s better to use your JavaScript function to handle likely errors. You can provide a more user-friendly message or take an alternative course of action.

For example, the following function will add an airline record, but will return a `failure` message if the `try` SQL++ statement fails:

```javascript
function addAirlineWithCheckReturn(id, name, callsign, country) {

    const full_id = "airline_" + id   
    const d = new Date().toJSON();    

    try {
        
        var q = insert into `travel-sample`.`inventory`.`airline` values(
            $full_id,
            {"id": $id,
                "type": "airline",
                "name": $name,
                "ca1": "Q5",
                "icao": "MLA",
                "callsign": $callsign,
                "country": $country,
                "opdate": $d}); 
        
        return "success"
    }
    catch (error) {
        return "failure"
    }

}
```

If the document with the given `id` value already exists in the `travel-sample`.`inventory`.`airline` collection, then the function would return the following:

```json
[
  "failure"
]
```

You can also choose to throw the error, rather than returning it as a string:

```javascript
function addAirlineWithCheckThrow(id, name, callsign, country) {

    const full_id = "airline_" + id   
    const d = new Date().toJSON();    

    try {
        
        var q = insert into `travel-sample`.`inventory`.`airline` values(
            $full_id,
            {"id": $id,
                "type": "airline",
                "name": $name,
                "ca1": "Q5",
                "icao": "MLA",
                "callsign": $callsign,
                "country": $country,
                "opdate": $d}); 
        
        return "success"
    }
    catch (error) {
        throw "failure"
    }

}
```

Running the preceding function with an `id` value that already exists would return the following:

```javascript
[
  {
    "code": 10109,
    "msg": "Error executing function 'AddAirlineWithCheckThrow' (travel-sample/inventory/my-library:addAirlineWithCheckThrow)",
    "reason": {
      "details": {
        "Code": "        throw \"failure\"",
        "Exception": "failure",
        "Location": "functions/travel-sample/inventory/my-library.js:49"
      },
      "type": "Exceptions from JS code"
    }
  }
]
```

When you throw the error, the exception is returned as a detailed JSON object.

### [](#throwing-or-returning-errors)Throwing or Returning Errors

The data the JavaScript engine returns is different on a throw vs. a return. Throw and return also affect how subsequent SQL++ operations are processed in a function.

**Returning an error**

If the JavaScript function returns any value, including an error, then the SQL++ runtime will assume that the function completed successfully, and the caller will continue to run subsequent statements.

**Throwing an error**

If an error is thrown, then this is treated as an error condition. Further statements in the request will not run.

You can also choose to throw the error object, rather than just the string. For example, the following function throws the entire error object, rather than just a string:

```javascript
function addAirlineWithCheckThrowObject(id, name, callsign, country) {

    const full_id = "airline_" + id   
    const d = new Date().toJSON();    

    try {
        
        var q = insert into `travel-sample`.`inventory`.`airline` values(
            $full_id,
            {"id": $id,
                "type": "airline",
                "name": $name,
                "ca1": "Q5",
                "icao": "MLA",
                "callsign": $callsign,
                "country": $country,
                "opdate": $d}); 
        
        return "success"
    }
    catch (error) {
        throw error
    }

}
```

Throwing the error object returns more useful information than just returning a string. For example, the following response makes it clear that the function failed to run because of a duplicate key value:

```json
[
  {
    "code": 10109,
    "msg": "Error executing function 'AddAirlineWithCheckThrowObject' (travel-sample/inventory/my-library:addAirlineWithCheckThrowObject)",
    "reason": {
      "details": {
        "Code": "        throw error",
        "Exception": {
          "caller": "couchbase:2112",
          "cause": {
            "caller": "couchbase:1985",
            "code": 17012,
            "key": "dml.statement.duplicatekey",
            "message": "Duplicate Key: airline_10"
          },
          "code": 12009,
          "icause": "Duplicate Key: airline_10",
          "key": "datastore.couchbase.DML_error",
          "message": "DML Error, possible causes include concurrent modification. Failed to perform INSERT on key airline_10",
          "retry": false
        },
        "Location": "functions/travel-sample/inventory/my-library.js:75",
        "Stack": "   at addAirlineWithCheckThrowObject (functions/travel-sample/inventory/my-library.js:61:17)"
      },
      "type": "Exceptions from JS code"
    }
  }
]
```

### [](#parsing-errors)Parsing Errors

You can also choose to parse the error with the `JSON.parse()` function and return the resulting object.

For example, the following function takes the object from `error.message` and returns that if an error occurs:

```javascript
function addAirlineWithCheck(id, name, callsign, country) {

    const full_id = "airline_" + id
    const d = new Date().toJSON();

    try {

        var q = insert into `travel-sample`.`inventory`.`airline` values(
            $full_id,
            {"id": $id,
                "type": "airline",
                "name": $name,
                "ca1": "Q5",
                "icao": "MLA",
                "callsign": $callsign,
                "country": $country,
                "opdate": $d});

        return "success"
    }
    catch (error) {
        const message = JSON.parse(error.message)
        return message
    }

}
```

If you ran the function on an `id` value that already exists in your operational cluster, the function would return a JSON object like the following:

```json
[
  {
    "caller": "couchbase:2098",
    "cause": {
      "caller": "couchbase:1971",
      "code": 17012,
      "key": "dml.statement.duplicatekey",
      "message": "Duplicate Key: airline_1220"
    },
    "code": 12009,
    "icause": "Duplicate Key: airline_1220",
    "key": "datastore.couchbase.DML_error",
    "message": "DML Error, possible causes include concurrent modification. Failed to perform INSERT on key airline_1220",
    "retry": false
  }
]
```

### [](#complex-error-handling)Complex Error Handling

Using the structure of the error message returned by `catch (error)`, you can also use `JSON.parse()` to add more complex error handling to your JavaScript function.

You could parse out the specific cause of an error, and display a more user-friendly error message that tells the user of your function how to resolve their error, or other, more complex logic.

For example, in this function, if the error returned has a `message.cause.key` value of `dml.statement.duplicatekey`, the function returns only the duplicate key, without the `Duplicate Key:` part of the message:

```javascript
function addAirlineWithCheck(id, name, callsign, country) {

    const full_id = "airline_" + id
    const d = new Date().toJSON();

    try {

        var q = insert
        into`travel-sample`.`inventory`.`airline`
        values(
            $full_id,
            {
                "id": $id,
                "type": "airline",
                "name": $name,
                "ca1": "Q5",
                "icao": "MLA",
                "callsign": $callsign,
                "country": $country,
                "opdate": $d
            });

        return "success"
    } catch (error) {

        const message = JSON.parse(error.message)

        if (message.cause.key == 'dml.statement.duplicatekey') {    

            var myErrorObject = {}
            myErrorObject.error_type = 'duplicate key'
            myErrorObject.key_used = message.cause.message.replace('Duplicate Key: ', '')    
            return myErrorObject
        } 
        else {
            return message
        }
    }
}
```