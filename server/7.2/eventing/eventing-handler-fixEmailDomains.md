---
title: "Function: fixEmailDomains"
description: Redact Sensitive Data prior to sharing.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-handler-fixEmailDomains.adoc
  xref: xref:7.2@server:eventing:eventing-handler-fixEmailDomains.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/eventing/eventing-handler-fixEmailDomains.html)

# Function: fixEmailDomains

**Goal**: Redact Sensitive Data prior to sharing.

* This function **fixEmailDomains** will fix email domains by ensuring only a top level domain is used.
* Example given an Email address like _jack.smith@mailhost.company.com_ we update it to use only the top level domain _jack.smith@company.com_.
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Will operate on all documents where doc.type === "employees".

* fixEmailDomains
* Input Data/Mutation
* Output Data/Mutation

```javascript
// To run configure the settings for this Function, fixEmailDomains, as follows:
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
//       "bucket alias", "src_col",       "bulk.data.source",   "read and write"
//
// Version 6.X
//   "Source Bucket"
//     source
//   "MetaData Bucket"
//     metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket",     "Access"
//       "bucket alias", "src_col",       "source", "read and write"

function fixEmailDomain(doc,fieldname,emaildomain) {
    /*
    * doc:         the mutated document
    * fieldname:   the name of the email field in "doc" to update
    * emaildomain: the domain to use, for example @mycompany.com
    */
    if (emaildomain.charAt(0) !== '@') return false;
    var domary = emaildomain.substr(1).split(".");
    var re = new RegExp('@.+?\.' + domary[0] +  '\.' + domary[1] + '$');
    if (re.test(doc[fieldname])) {
        var tmp = doc[fieldname].replace(re, emaildomain);
        doc[fieldname] = tmp;
        return true;
    }
    return false;
}

function OnUpdate(doc, meta) {
    if (doc.type !== "employees") return;

    // normalize email addresses
    if (fixEmailDomain(doc,'email',"@bigmovies.com")) {
        try {
            log('OnUpdate: updated field email',doc.email);
            src_col[meta.id] = doc;
        } catch (e) {
            log('OnUpdate: error',e);
        }
    }
}
```

```json
INPUT: KEY employees::1001

{
  "type": "employees",
  "id": 1001,
  "email": "will.smith@mailhost.bigmovies.com"
}
```

```json
UPDATED/OUTPUT: KEY employees::1001

{
  "type": "employees",
  "id": 1001,
  "email": "will.smith@bigmovies.com"
}
```