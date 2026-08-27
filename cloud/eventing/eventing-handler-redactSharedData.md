---
title: "Function: redactSharedData"
description: Redact Sensitive Data prior to sharing.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-handler-redactSharedData.adoc
  xref: xref:cloud:eventing:eventing-handler-redactSharedData.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-handler-redactSharedData.html)

# Function: redactSharedData

**Goal**: Redact Sensitive Data prior to sharing.

* This function **redactSharedData** will remove sensitive data and write "safe" redacted records.
* Requires Eventing Storage (or metadata collection), a "source" collection, and a "destination" collection.
* Will operate on all documents where doc.type === "master\_profile".
* Will create redacted documents in real-time of doc.type === "shared\_profile".
* The "destination" collection can be shared (or replicated via XCDR to a business partner) too the cloud (AWS, Azure or GCP).

* redactSharedData
* Input Data/Mutation
* Output Data/Mutation

```javascript
// To run configure the settings for this Function, redactSharedData, as follows:
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
//       "bucket alias", "aws_col",       "bulk.data.destination",   "read and write"
//
// Version 6.X
//   "Source Bucket"
//     source
//   "MetaData Bucket"
//     metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket",     "Access"
//       "bucket alias", "aws_col",       "destination", "read and write"

function OnUpdate(doc, meta) {
    // only process our profile documents
    if (doc.type !== "master_profile") return;
    // aws_col is a bucket alias to the target bucket to replicate to AWS via
    // XCDR. Write the minimal (non-sensitive) profile doc to the bucket for AWS.
    aws_col["shared_profile::"+doc.id] = {
        "type": "shared_profile",
        "first_name": doc.first_name,
        "id": doc.id,
        "basic_profile": doc.basic_profile,
        "timezone": doc.timezone
    };
}
```

```json
INPUT: KEY master_profile::80927079070

{
  "type": "master_profile",
  "first_name": "Peter",
  "last_name": "Chang",
  "id": 80927079070,
  "basic_profile": {
    "partner_id": 80980221,
    "services": [
      {
        "music": true
      },
      {
        "games": true
      },
      {
        "video": false
      }
    ]
  },
  "sensitive_profile": {
    "ssn": "111-11-1111",
    "credit_card": {
      "number": "3333-333-3333-3333",
      "expires": "01/09",
      "ccv": "111"
    }
  },
  "address": {
    "home": {
      "street": "4032 Kenwood Drive",
      "city": "Boston",
      "zip": "02102"
    },
    "billing": {
      "street": "541 Bronx Street",
      "city": "Boston",
      "zip": "02102"
    }
  },
  "phone": {
    "home": "800-555-9201",
    "work": "877-123-8811",
    "cell": "878-234-8171"
  },
  "locale": "en_US",
  "timezone": -7,
  "gender": "M"
}
```

```json
UPDATED/OUTPUT: KEY shared_profile::80927079070

{
  "type": "shared_profile",
  "first_name": "Peter",
  "id": 80927079070,
  "basic_profile": {
    "partner_id": 80980221,
    "services": [
      {
        "music": true
      },
      {
        "games": true
      },
      {
        "video": false
      }
    ]
  },
  "timezone": -7
}
```