---
title: "Function: convertXMLtoJSON"
description: Recursively and generically convert simple XML strings into JSON.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/eventing/pages/eventing-handler-convertXMLtoJSON.adoc
  xref: xref:7.6@server:eventing:eventing-handler-convertXMLtoJSON.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/eventing/eventing-handler-convertXMLtoJSON.html)

# Function: convertXMLtoJSON

**Goal**: Recursively and generically convert simple XML strings into JSON.

* This function **convertXMLtoJSON** shows how to convert simple XML strings into JSON.
* If you need to also convert XML attributes refer to **[convertAdvXMLtoJSON](eventing-handler-convertAdvXMLtoJSON.md)**
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Will operate on any mutation where the KEY or meta.id starts with "xml:".
* Will enrich the source document with a new JSON object representing the XML data.
* Maintains a checksum to prevent the overhead of conversion if the `in_xml` property is unchanged.

* convertXMLtoJSON
* Input Data/Mutation
* Output Data/Mutation

```javascript
// To run configure the settings for this Function, convertXMLtoJSON, as follows:
//
// Version 7.1+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
// Version 7.0+
//   "Listen to Location"
//     bulk.data.source
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket.scope.collection", "Access"
//       "bucket alias", "src_col",       "bulk.data.source",        "read and write"
//
// Version 6.X
//   "Source Bucket"
//     source
//   "MetaData Bucket"
//     metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket",     "Access"
//       "bucket alias", "src_col",       "source",     "read and write"

function OnUpdate(doc, meta) {
    // filter out non XML
    if (!meta.id.startsWith("xml:")) return;
    // The KEY started with "xml" try to process it
    // ===========================================================
    // *** Do other  work required here on non .in_xml changes ***
    // ===========================================================
    // let's see if we need to re-create our json representation.
    var xmlchksum = crc64(doc.in_xml);
    // ===========================================================
    // Don't reprocess if the doc.in_xml has not changed this could be
    // a big performance win if the doc has other fields that mutate.
    // We do this via a checksum of the .in_xml property.
    if (doc.xmlchksum && doc.xmlchksum === xmlchksum) return;
    // Either this is the first pass, or the .in_xml property changed.
    var jsonDoc = parseXmlToJson(doc.in_xml);
    log(meta.id,"1. INPUT  xml doc.in_xml :", doc.in_xml);
    log(meta.id,"2. CHECKSUM doc.in_xml   :", xmlchksum);
    log(meta.id,"3. OUTPUT doc.out_json   :", jsonDoc);
    doc.out_json = jsonDoc;
    doc.xmlchksum = xmlchksum;
    // ===========================================================
    // enrich the source collection with .out_json and .xmlchksum
    src_col[meta.id] = doc;
}

// 7.0.0 version uses String.matchAll eliminates the need to make our own MatchAll function
function parseXmlToJson(xml) {
    const json = {};
    for (const res of xml.matchAll(/(?:<(\w*)(?:\s[^>]*)*>)((?:(?!<\1).)*)(?:<\/\1>)|<(\w*)(?:\s*)*\/>/gm)) {
        const key = res[1] || res[3];
        const value = res[2] && parseXmlToJson(res[2]);
        json[key] = ((value && Object.keys(value).length) ? value : res[2]) || null;
    }
    return json;
}

/*
// need this for 6.6.0 version
function* MatchAll(str, regExp) {
  if (!regExp.global) {
    throw new TypeError('Flag /g must be set!');
  }
  const localCopy = new RegExp(regExp, regExp.flags);
  let match;
  while (match = localCopy.exec(str)) {
    yield match;
  }
}

// 6.6.0 version no String.matchAll need our own MatchAll function
function parseXmlToJson(xml) {
    const json = {};
    for (const res of MatchAll(xml,/(?:<(\w*)(?:\s[^>]*)*>)((?:(?!<\1).)*)(?:<\/\1>)|<(\w*)(?:\s*)*\/>/gm)) {
        const key = res[1] || res[3];
        const value = res[2] && parseXmlToJson(res[2]);
        json[key] = ((value && Object.keys(value).length) ? value : res[2]) || null;
    }
    return json;
}
*/
```

```json
INPUT: KEY xml::1

{
  "type": "xml",
  "id": 1,
  "in_xml": "<CD><TITLE>EmpireBurlesque</TITLE><ARTIST>BobDylan</ARTIST><COUNTRY>USA</COUNTRY><COMPANY>Columbia</COMPANY><PRICE>10.90</PRICE><YEAR>1985</YEAR></CD>"
}
```

```json
UPDATED/OUTPUT: KEY xml::1

{
  "type": "xml",
  "id": 2,
  "in_xml": "<CD><TITLE>EmpireBurlesque</TITLE><ARTIST>BobDylan</ARTIST><COUNTRY>USA</COUNTRY><COMPANY>Columbia</COMPANY><PRICE>10.90</PRICE><YEAR>1985</YEAR></CD>",
  "out_json": {
    "CD": {
      "TITLE": "EmpireBurlesque",
      "ARTIST": "BobDylan",
      "COUNTRY": "USA",
      "COMPANY": "Columbia",
      "PRICE": "10.90",
      "YEAR": "1985"
    }
  },
  "xmlchksum": "02087b7be275d0d8"
}
```