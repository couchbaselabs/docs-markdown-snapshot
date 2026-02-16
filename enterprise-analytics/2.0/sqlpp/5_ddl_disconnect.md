[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_disconnect.html)

> This topic describes how you use `DISCONNECT` statements to disconnects all remote collections on the given link or links. 

A `DISCONNECT` statement is the inverse of a `CONNECT` statement.

The `DISCONNECT` statement applies only to remote links, and is not applicable to external links.

|  | DISCONNECT statements cannot execute while the cluster is in a scaling state. The evaluation of such DDL statements fails. You can reattempt the action after scaling is complete. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#syntax)Syntax

**DisconnectStmnt EBNF** 

```EBNF
DisconnectStmnt ::= "DISCONNECT" "LINK" LinkSpecification
```

**DisconnectStmnt Diagram** 

!["DISCONNECT" "LINK" LinkSpecification](_images/DisconnectStmnt.png) 

The `LinkSpecification` is a comma-separated list of one or more link names to disconnect.

**Show LinkSpecification** 

![LinkName ( "," LinkName )*](_images/LinkSpecification.png) 

LinkSpecification

## [](#example)Example

The following example disconnects the remote link called `myCbLink` and stops receiving and shadowing data for all collections on that link.

```SQL++
 DISCONNECT LINK myCbLink;
```