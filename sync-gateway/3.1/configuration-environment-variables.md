---
title: Configuration Environment Variables
description: Using environment variables in the configuration of Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/configuration-environment-variables.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::configuration-environment-variables.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/configuration-environment-variables.html)

# Configuration Environment Variables

> Using environment variables in the configuration of Sync Gateway  

Topic Group

[Configuration Schema](configuration-properties-legacy.md)| [Javascript Functions](configuration-javascript-functions.md)| Environment Variables | [REST API](configuration-rest-api.md)| [Persistent Configuration](configuration-overview.md)

## [](#introduction)Introduction

Sync Gateway configuration is extended to allow the use of defined _environment variables_ as substitution values inside the configuration file. This allows users to determine, pick-up and substitute appropriate values during Sync Gateway start-up.

The use of environment variables within the configuration file increases the flexibility of the configuration process. It makes the switching of the runtime behavior — for example during development, experimentation or testing — much easier.

## [](#syntax)Syntax

To use environment variables in your configuration file, insert the variable name — prefixed by a `$` symbol — wherever you would normally put the configuration value you are substituting for — see [Example 1](#ex-syntax).

You can define inline default values using the notation `${var:-default}`. The default value is used if the referenced environment variable is empty or undefined.

If you need to include a string containing one or more literal `$` symbols, use `$$` instead of `$`. This enables the parser to differentiate between a literal `$` and the start of a variable name; so `pa$$$$` resolves to the value `pa$$`.

Variable names are case-sensitive in this context. So `${username}` and `${USERNAME}` are not the same variable

Example 1\. Configuring with Environment Variables

```JSON
{
  "bootstrap": {
    "server": "couchbases://localhost", (1)
    "username": "${USERNAME}", (2)
    "password": "${PASSWORD}"
    "server_tls_skip_verify": true, (3)
    "use_tls_server": false (4)
  },
  "logging": { (5)
    "console": {
      "enabled": true,
      "log_level": "${var_loglevel:-info}", (6)
      "log_keys": ["*"]
    }
  }
}
```

{ "databases": { "db1": { "bucket": "bucket1", "server": "couchbase://localhost", } "db2": { "server": "couchbase://localhost", "username": "${USERNAME}", "password": "pa$$$$word" // <.> } } }

```json
<.> Here we provide a reference to the environment variables `USERNAME` footnote:[On Windows systems USERNAME is already in use as a System Variable used by the operating system] and `PASSWORD`.
The values of those variable are substituted here immediately prior to the parsing of the configuration file.

<.> The variable `var_loglevel` is given a default value of 'info', if the `var_loglevel` environment variable itself is empty or undefined.

<.> If, for example. the password value contains dollar symbols.
We can use the double-dollar notation ({double-dollar}.
So, the value `pa{double-dollar}{double-dollar}word` is interpreted as `pa{double-dollar}word`.
```

## [](#usage)Usage

Insert the required environment variable references in a [Bootstrap Configuration](configuration-schema-bootstrap.md), or in a [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md) with `disable_persistent_config=true`.

Sync Gateway will replace each variable occurrence immediately prior to the parsing of the configuration file at each startup.

The variables are immutable. This means changes to the values of the environment variables are not detected by Sync Gateway whilst it is running. Such changes only become effective after a restart of Sync Gateway.

Any references to undefined variables found in the configuration will cause sync gateway to throw an error. This will prevent an invalid configuration being processed.

## [](#variable-definition)Variable Definition

How you define the environment variables in your runtime environment will depend on the platform used to host Sync Gateway.

As with the configuration file, you may need to define strings containing meta-characters (for example, symbols such as `$\*/`).

Depending on the shell environment you can use a number of options:

* Enclose the string in single-quotes, which will remove the special meaning of every character between the quotes. Everything inside single quotes becomes a literal string.
* Precede the meta-character with an escape character, typically a reverse solidus (`\`) (a backtick (`` ` ``) in Powershell). Note — This works in double-quote enclosed strings or in strings with no enclosing quotes, but not in single-quotes since as stated above, the remove the special meaning of the enclosed characters including any escape characters.

* Linux/Mac OS
* Windows CLI
* Windows System Properties
* Powershell

```bash
export USERNAME=Administrator
export PASSWORD='pa$$word' (1)
```

| **1** | Use quotes to prevent interpolation of the literal string’s $ symbols, alternatively use "pa\\$\\$word" |
| ----- | ------------------------------------------------------------------------------------------------------- |

```dos
setx USERNAME Administrator (1)
set PASSWORD='pa$$word' (2)
```

| **1** | Permanently set the USERNAME variable. Note setx does not require the \= symbol                                                                                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Sets the PASSWORD variable, but only for the duration of the current 'Command Line' session. This may not be what you want. Note we use single-quotes because of the password value’s $$ symbols, alternatively use "pa\\$\\$word" |

1. Open a _System Properties_ panel
2. On the _Advanced System Settings_ tab, select **Environment Variables**  
This displays the _Environment Variables_ panel
3. Here you can create **NEW** variables as well as **EDIT** and **DELETE** existing variables

```powershell
$ENV:USERNAME=Administrator
$ENV:PASSWORD='pa$$word' (1)
```

| **1** | Note we use single-quotes because of the password value’s $$ symbols, alternatively use "pa\`$\`$word" |
| ----- | ------------------------------------------------------------------------------------------------------ |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)