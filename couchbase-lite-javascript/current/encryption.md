---
title: Database Encryption
description: Encrypting Couchbase Lite Databases in JavaScript
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/encryption.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite-javascript::encryption.adoc[]
---

[View original HTML](/couchbase-lite-javascript/current/encryption.html)

# Database Encryption

> Description — _Encrypting Couchbase Lite Databases in JavaScript_  
> Related Content — [Databases](database.md) | [Documents](document.md)

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

Couchbase Lite JavaScript includes the ability to encrypt databases stored in IndexedDB. This allows browser applications to secure data at rest. The encryption uses the Web Crypto API with AES-GCM algorithm.

## [](#encryption-limitations)Encryption Limitations

Unlike native Couchbase Lite SDKs, browser-based encryption has limitations due to IndexedDB:

* **Indexed properties cannot be encrypted**: IndexedDB requires these properties to remain accessible for indexing
* **Document IDs and metadata are not encrypted**: IndexedDB uses these for document lookup
* **Field-level encryption**: By default, all document properties are encrypted. Properties specified in the `indexes` array are automatically left unencrypted to allow indexing

What is Encrypted

* All document properties except those specified in the `indexes` array
* All blobs (binary attachments)

What is Not Encrypted

* Document IDs and revision IDs
* Properties listed in the `indexes` array
* Database metadata

## [](#enabling-encryption)Enabling Encryption

To enable encryption, provide a password in the [DatabaseConfig](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/interfaces/DatabaseConfig.html) when opening the database. Provide this encryption password every time the database is opened — see [Example 1](#ex-sdb-encrypt).

Example 1\. Configure Database Encryption

```javascript
const database = await Database.open({
  name: 'secure-app',
  password: 'my-secure-password',
  collections: {
    users: {
      // Index properties are not encrypted by default
      indexes: ['username', 'email', 'createdAt']
    }
  }
});

// Get the users collection
const users = database.getCollection("users");

await users.save({
  username: 'alice',        // Not encrypted (indexed property)
  email: 'alice@example.com', // Not encrypted (indexed property)
  createdAt: '2025-01-15',  // Not encrypted (indexed property)
  ssn: '123-45-6789',      // Encrypted
  creditCard: '4111-1111', // Encrypted
  address: {               // Encrypted (entire object)
    street: '123 Main St',
    city: 'Springfield'
  }
});
```

## [](#persisting-key)Persisting the Encryption Key

Couchbase Lite does not persist the encryption key. It is the application’s responsibility to manage the key.

> [!IMPORTANT]
> There is no secure cross-session storage available in browsers. The encryption password must be obtained from the user each time the application loads, or stored using browser-specific mechanisms with appropriate security considerations.

## [](#opening-encrypted)Opening Encrypted Databases

An encrypted database must be opened with the correct password:

```javascript
try {
  const database = await Database.open({
    name: 'secure-app',
    password: userEnteredPassword,
    collections: { users: {} }
  });
} catch (error) {
  if (error instanceof EncryptionError) {
    console.error('Incorrect password');
  }
}
```

## [](#changing-key)Changing the Encryption Key

To change an existing encryption key, open the database with its current password and use [Database.changeEncryptionKey()](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/classes/Database.html#changeEncryptionKey):

Example 2\. Change encryption key

```javascript
// Open database with current password
const database = await Database.open('secure-app', {
  password: 'old-password',
  collections: { users: {} }
});

// Change to new password
await database.changeEncryptionKey('new-password');

console.log('Encryption key changed');
```

## [](#removing-encryption)Removing Encryption

To remove encryption, open the database with its current password and call `changeEncryptionKey()` with `undefined`:

Example 3\. Remove encryption

```javascript
// Open encrypted database
const database = await Database.open('secure-app', {
  password: 'current-password',
  collections: { users: {} }
});

// Remove encryption
await database.changeEncryptionKey(undefined);

console.log('Encryption removed');
```

## [](#security-best-practices)Security Best Practices

When using database encryption in browser applications:

* **Password Management**: Never hardcode encryption passwords. Always obtain them from user input or secure key management systems.
* **HTTPS Only**: Always serve encrypted database applications over HTTPS to prevent password interception.
* **Memory Considerations**: Be aware that decrypted data exists in browser memory during use.
* **Storage Clearing**: Educate users that clearing browser data will delete encrypted databases.
* **Indexed Properties**: Be aware that indexed properties are not encrypted. Only index properties that don’t contain sensitive data.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.