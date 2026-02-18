---
title: Handling Errors in Javascript Functions
description: Error handling in Javascript user-defined functions use the same
  standard exception mechanism as part of the language standard.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/javascript-udfs/pages/handling-errors-javascript-udf.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/javascript-udfs/handling-errors-javascript-udf.html)

# Handling Errors in Javascript Functions

> Error handling in Javascript user-defined functions use the same standard exception mechanism as part of the language standard. 

Errors that occur during the execution of a SQL++ statement are usually handled by the runtime, which will return a JSON object giving details of the error. For example, if we execute a record insertion function with a key that already exists:

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

In most cases, it’s a lot better if the Javascript function itself can handle errors that are likely to occur. This gives the developer the option of responding with a more user-friendly message, or taking an alternative course of action.

The following function will add an airline record, but will return an `failure` message if the attempt isn’t successful.

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

If the record key already exists, then calling this method with `EXECUTE FUNCTION` will produce the following result:

```json
[
  "failure"
]
```

Alternatively, we can simply throw the error, rather than returning it as a string:

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

which will produce the following result:

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

As well as wrapping the expection in a detailed JSON object, there is another fundamental difference between throwing an error or returning it:

Throw vs Return

Aside from the data returned, throwing an error or returning a value/error will affect how subsequent SQL++ operations are processed.

**Returning an error**

If the JavaScript function _returns_ any value, then the SQL++ runtime will assume that the function completed successfully, and the caller will continue to run subsequent statements.

**Throwing an error**

If an error is _thrown_ then this is treated as an error condition, so further statements in the request will not be run.

You can, of course, throw the error object itself, rather than just a string.

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

which deliver a lot more useful information than just posting back a string:

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

Another approach is to parse the error using the `JSON.parse()` function and return the resulting object:

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
        const message = JSON.parse(error.message)    (1)
        return message
    }

}
```

| **1** | The error object contains a JSON string (message) detailing the nature of the error. It is much easier to interrogate the message if it’s converted back into a JSON object on its own. This code will send back the entire message structure. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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

Once we know the structure of the error message, there’s no reason why we can’t carry out alternative actions depending on the type of error encountered:

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

        if (message.cause.key == 'dml.statement.duplicatekey') {    (1)

            var myErrorObject = {}
            myErrorObject.error_type = 'duplicate key'
            myErrorObject.key_used = message.cause.message.replace('Duplicate Key: ', '')    (2)
            return myErrorObject
        } 
        else {
            return message
        }
    }
}
```

| **1** | Check to see if this is a message that can be handled by the function itself.         |
| ----- | ------------------------------------------------------------------------------------- |
| **2** | Strips out the "Duplicate Key: " part of the message, leaving just the duplicate key. |