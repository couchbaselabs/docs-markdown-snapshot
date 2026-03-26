---
title: Installing Couchbase Lite JavaScript
description: How to install Couchbase Lite JavaScript
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/gs-install.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite-javascript::gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/gs-install.html)

# Installing Couchbase Lite JavaScript

> Description — _How to install Couchbase Lite JavaScript_  
> _Abstract — Getting you up and running quickly with Couchbase Lite JavaScript_  

## [](#introduction)Introduction

Couchbase Lite JavaScript is distributed as an npm package and supports development in both JavaScript and TypeScript.

## [](#installation)Installation

Add Couchbase Lite JavaScript to your web application project using npm:

```bash
npm install @couchbase/lite-js
```

Then import Couchbase Lite in your JavaScript/TypeScript code:

```javascript
import { Database, Replicator } from '@couchbase/lite-js';
```

That's it! You're all set to begin developing offline-first web applications.

## [](#verify-installation)Verify Installation

After installing, verify that Couchbase Lite is correctly installed.

### [](#check-import)Verify Import

Create a simple test file:

```javascript
// test.js
import { Database, Version } from '@couchbase/lite-js';

console.log('Couchbase Lite version:', Version);
```

### [](#basic-functionality-test)Test Basic Functionality

Test creating a database:

```javascript
import { Database } from '@couchbase/lite-js';

async function test() {
  try {
    const db = await Database.open({
      name: 'test-db',
      version: 1,
      collections: {
      items: {}
      }
    });

    console.log('✓ Database created successfully');

    await db.close();
    console.log('✓ Database closed successfully');

    // Clean up
    await Database.deleteDatabase('test-db');
    console.log('✓ Database deleted successfully');

  } catch (error) {
    console.error('✗ Installation test failed:', error);
  }
}

test();
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](#)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.