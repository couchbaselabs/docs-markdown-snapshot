[View original HTML](/analytics/sqlpp/5_ddl_database.html)

> This topic describes how you use the `CREATE` statement to create Capella Analytics databases. 

For general `CREATE` statement syntax, see [CREATE Statements](5%5Fddl%5Fcreate.md).

## [](#syntax)Syntax

**CreateDatabase EBNF** 

```EBNF
CreateDatabase ::= "CREATE" "DATABASE" Identifier ("IF" "NOT" "EXISTS")?
```

**CreateDatabase Diagram** 

![CREATE](_images/CreateDatabase.png) 

For information about specifying a database name, see [Entities in Capella Analytics Services](1a%5Fentities.md).

## [](#example)Example

```SQL++
  CREATE DATABASE music;
```