---
title: Encrypt a Database
description: Encrypt a Couchbase Edge Server database using a password or AES256
  key, and verify its encryption status.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/administer/pages/encrypt-database.adoc
  xref: xref:1.0@couchbase-edge-server:administer:encrypt-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/administer/encrypt-database.html)

# Encrypt a Database

> Encrypt a Couchbase Edge Server database using a password or AES256 key, and verify its encryption status. 

Couchbase Edge Server uses AES256 encryption to protect database contents at rest. You can encrypt a database at creation time by setting a password in the configuration file, or encrypt an existing unencrypted database using the `cblite` command-line tool.

## [](#before-you-begin)Before You Begin

* Couchbase Edge Server is installed and you have access to its configuration file.
* To encrypt an existing database: Couchbase Edge Server is stopped before you begin.
* To encrypt an existing database: the Enterprise Edition of the [cblite tool](https://github.com/couchbaselabs/couchbase-mobile-tools/releases/tag/cblite-4.0.0EE) is downloaded and available on the host machine.

## [](#encrypt-new-database)Encrypt a New Database

Set the password in the configuration file before Couchbase Edge Server creates the database. Couchbase Edge Server encrypts the database on first creation.

Procedure

1. Open the Couchbase Edge Server configuration file.
2. Add the `password` property to the database configuration:  
```json5  
{  
  databases: {  
    my-database: {  
      path: "/var/lib/edge-server/my-database.cblite2",  
      create: true,  
      enable_client_sync: true,  
      password: "<your-password>" (1)  
    }  
  }  
}  
```

| **1** | A plaintext password, or a raw AES256 key encoded as 64 hex digits. See [databases.{database\_name}.password](../configuration/edge-server-configuration.md#databases-{database%5Fname}-password). |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
3. Save the configuration file and start Couchbase Edge Server.  
Couchbase Edge Server creates the database in encrypted form.

> [!WARNING]
> Do not lose this password. There is no recovery mechanism. If the password is lost, the database contents are unrecoverable.

## [](#encrypt-existing-database)Encrypt an Existing Database

Use this procedure if your database already exists without encryption.

> [!IMPORTANT]
> Stop Couchbase Edge Server before encrypting an existing database. Running `cblite` against a database that Couchbase Edge Server has open may corrupt the database.

Procedure

1. Stop Couchbase Edge Server.
2. Use the `cblite` tool to encrypt the database file:  
```sh  
// NOTE FOR FORTUNE: Verify exact cblite encrypt command syntax with Jens before publishing.  
// Expected form is something like:  
// cblite encrypt --new-password <password> /path/to/db.cblite2  
```
3. Open the Couchbase Edge Server configuration file and add the `password` property to the database configuration:  
```json5  
{  
  databases: {  
    my-database: {  
      path: "/var/lib/edge-server/my-database.cblite2",  
      password: "<your-password>" // Must match the password used in step 2  
    }  
  }  
}  
```
4. Save the configuration file and start Couchbase Edge Server.

> [!WARNING]
> Do not lose this password. There is no recovery mechanism. If the password is lost, the database contents are unrecoverable.

## [](#verify-encryption)Verify Database Encryption

To confirm whether a database is encrypted, run the following command against the database's internal SQLite file:

```sh
file /path/to/db.cblite2/db.sqlite3
```

Interpret the output as follows:

* **`SQLite 3.x database`** — The database is not encrypted.
* **`data`** — The database is encrypted. Encrypted database files contain no recognizable header and appear as arbitrary binary data.

## [](#next-steps)Next Steps

* [Operational Logging](operational-logging.md)
* [Audit Logging](audit-logging.md)
* [Configuration reference: databases.{database\_name}.password](../configuration/edge-server-configuration.md#databases-{database%5Fname}-password)