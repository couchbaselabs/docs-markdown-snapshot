[View original HTML](/server/current/n1ql/n1ql-language-reference/select-syntax.html)

> This page enables you to drill down through the syntax of a SELECT query. 

select ::= [select-term](#select-term) ( [set-op](#set-op) [select-term](#select-term) )* [order-by-clause](#order-by-clause)? [limit-clause](#limit-clause)? [offset-clause](#offset-clause)?

![Syntax diagram](../_images/n1ql-language-reference/select.png) 

select-term ::= [subselect](#subselect) | '(' [select](#select) ')'

![Syntax diagram](../_images/n1ql-language-reference/select-term.png) 

subselect ::= [select-from](#select-from) | [from-select](#from-select)

![Syntax diagram](../_images/n1ql-language-reference/subselect.png) 

select-from ::= [with-clause](#with-clause)? [select-clause](#select-clause) [from-clause](#from-clause)? [let-clause](#let-clause)? [where-clause](#where-clause)?
                [group-by-clause](#group-by-clause)? [window-clause](#window-clause)?

![Syntax diagram](../_images/n1ql-language-reference/select-from.png) 

from-select ::= [with-clause](#with-clause)? [from-clause](#from-clause) [let-clause](#let-clause)? [where-clause](#where-clause)? [group-by-clause](#group-by-clause)?
                [window-clause](#window-clause)? [select-clause](#select-clause)

![Syntax diagram](../_images/n1ql-language-reference/from-select.png) 

set-op ::= ( 'UNION' | 'INTERSECT' | 'EXCEPT' ) 'ALL'?

![Syntax diagram](../_images/n1ql-language-reference/set-op.png) 

## [](#with-clause)WITH Clause

with-clause ::= 'WITH' [alias](identifiers.md#identifier-alias) 'AS' '(' ( [select](#select) | [expression](index.md#N1QL%5FExpressions) ) ')'
                 ( ',' [alias](identifiers.md#identifier-alias) 'AS' '(' ( [select](#select) | [expression](index.md#N1QL%5FExpressions) ) ')' )*

![Syntax diagram](../_images/n1ql-language-reference/with-clause.png) 

alias ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/alias.png) 

## [](#select-clause)SELECT Clause

select-clause ::= 'SELECT' [hint-comment](optimizer-hints.md)? [projection](#projection) [exclude-clause](#exclude-clause)?

![Syntax diagram](../_images/n1ql-language-reference/select-clause.png) 

projection ::= ( 'ALL' | 'DISTINCT' )?
               ( [result-expr](#result-expr) ( ',' [result-expr](#result-expr) )* |
               ( 'RAW' | 'ELEMENT' | 'VALUE' ) [expr](index.md#N1QL%5FExpressions) ( 'AS'? [alias](identifiers.md#identifier-alias) )? )

![Syntax diagram](../_images/n1ql-language-reference/projection.png) 

result-expr ::= ( ( [path](#path) '.' )? '*' | [expr](index.md#N1QL%5FExpressions) ( 'AS'? [alias](identifiers.md#identifier-alias) )? )

![Syntax diagram](../_images/n1ql-language-reference/result-expr.png) 

path ::= [identifier](identifiers.md) ( '[' [expr](index.md#N1QL%5FExpressions) ']' )* ( '.' [identifier](identifiers.md) ( '[' [expr](index.md#N1QL%5FExpressions) ']' )* )*

![Syntax diagram](../_images/n1ql-language-reference/path.png) 

exclude-clause ::= 'EXCLUDE' [exclude-term](#exclude-term) ( ',' [exclude-term](#exclude-term) )*

![Syntax diagram](../_images/n1ql-language-reference/exclude-clause.png) 

exclude-term ::= [identifier](identifiers.md) | [string-expr](literals.md#strings)

![Syntax diagram](../_images/n1ql-language-reference/exclude-term.png) 

## [](#from-clause)FROM Clause

from-clause ::= 'FROM' [from-terms](#from-term)

![Syntax diagram](../_images/n1ql-language-reference/from-clause.png) 

from-terms ::= ( [from-keyspace](#from-keyspace) | [from-subquery](#from-subquery) | [from-generic](#from-generic) )
               ( [join-clause](#join-clause) | [nest-clause](#nest-clause) | [unnest-clause](#unnest-clause) )*  [comma-separated-join](#comma-separated-join)*

![Syntax diagram](../_images/n1ql-language-reference/from-terms.png) 

from-keyspace ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )? [use-clause](#use-clause)?

![Syntax diagram](../_images/n1ql-language-reference/from-keyspace.png) 

keyspace-ref ::= [keyspace-path](#keyspace-path) | [keyspace-partial](#keyspace-partial)

![Syntax diagram](../_images/n1ql-language-reference/keyspace-ref.png) 

keyspace-path ::= ( [namespace](#namespace) ':' )? [bucket](#bucket) ( '.' [scope](#scope) '.' [collection](#collection) )?

![Syntax diagram](../_images/n1ql-language-reference/keyspace-path.png) 

keyspace-partial ::= [collection](#collection)

![Syntax diagram](../_images/n1ql-language-reference/keyspace-partial.png) 

namespace ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/namespace.png) 

bucket ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/keyspace.png) 

scope ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/keyspace.png) 

collection ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/keyspace.png) 

from-subquery ::= [subquery-expr](#subquery-expr) 'AS'? [alias](identifiers.md#identifier-alias)

![Syntax diagram](../_images/n1ql-language-reference/from-subquery.png) 

subquery-expr ::= '(' [select](#select) ')'

![Syntax diagram](../_images/n1ql-language-reference/subquery-expr.png) 

from-generic ::= [expr](index.md#N1QL%5FExpressions) ( 'AS' [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/generic-expr.png) 

## [](#join-clause)JOIN Clause

join-clause ::= [ansi-join-clause](#ansi-join-clause) | [lookup-join-clause](#lookup-join-clause) | [index-join-clause](#index-join-clause)

![Syntax diagram](../_images/n1ql-language-reference/join-clause.png) 

### [](#ansi-join-clause)ANSI JOIN

ansi-join-clause ::= [ansi-join-type](#ansi-join-type)? 'JOIN' [ansi-join-rhs](#ansi-join-rhs) [ansi-join-predicate](#ansi-join-predicate)

![Syntax diagram](../_images/n1ql-language-reference/ansi-join-clause.png) 

ansi-join-type ::= 'INNER' | ( 'LEFT' 'OUTER'? ) | ( 'RIGHT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/ansi-join-type.png) 

ansi-join-rhs ::= [rhs-keyspace](#rhs-keyspace) | [rhs-subquery](#rhs-subquery) | [rhs-generic](#rhs-generic)

![Syntax diagram](../_images/n1ql-language-reference/ansi-join-rhs.png) 

rhs-keyspace ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )? [ansi-join-hints](#ansi-join-hints)?

![Syntax diagram](../_images/n1ql-language-reference/rhs-keyspace.png) 

rhs-subquery ::= [subquery-expr](#subquery-expr) 'AS'? [alias](identifiers.md#identifier-alias)

![Syntax diagram](../_images/n1ql-language-reference/rhs-subquery.png) 

rhs-generic ::= [expr](index.md#N1QL%5FExpressions) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/rhs-generic.png) 

ansi-join-hints ::= [use-hash-hint](#use-hash-hint) | [use-nl-hint](#use-nl-hint) | [multiple-hints](#multiple-hints)

![Syntax diagram](../_images/n1ql-language-reference/ansi-join-hints.png) 

use-hash-hint ::= 'USE' [use-hash-term](#use-hash-term)

![Syntax diagram](../_images/n1ql-language-reference/use-hash-hint.png) 

use-hash-term ::= 'HASH' '(' ( 'BUILD' | 'PROBE' ) ')'

![Syntax diagram](../_images/n1ql-language-reference/use-hash-term.png) 

use-nl-hint ::= 'USE' [use-nl-term](#use-nl-term)

![Syntax diagram](../_images/n1ql-language-reference/use-nl-hint.png) 

use-nl-term ::= 'NL'

![Syntax diagram](../_images/n1ql-language-reference/use-nl-term.png) 

multiple-hints ::= 'USE' ( [ansi-hint-terms](#ansi-hint-terms) [other-hint-terms](#other-hint-terms) ) | ( [other-hint-terms](#other-hint-terms) [ansi-hint-terms](#ansi-hint-terms) )

![Syntax diagram](../_images/n1ql-language-reference/multiple-hints.png) 

ansi-hint-terms ::= [use-hash-term](#use-hash-term) | [use-nl-term](#use-nl-term)

![Syntax diagram](../_images/n1ql-language-reference/ansi-hint-terms.png) 

other-hint-terms ::= [use-index-term](#use-index-term) | [use-keys-term](#use-keys-term)

![Syntax diagram](../_images/n1ql-language-reference/other-hint-terms.png) 

ansi-join-predicate ::= 'ON' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/ansi-join-predicate.png) 

### [](#lookup-join-clause)Lookup JOIN

lookup-join-clause ::= [lookup-join-type](#lookup-join-type)? 'JOIN' [lookup-join-rhs](#lookup-join-rhs) [lookup-join-predicate](#lookup-join-predicate)

![Syntax diagram](../_images/n1ql-language-reference/lookup-join-clause.png) 

lookup-join-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/lookup-join-type.png) 

lookup-join-rhs ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/lookup-join-rhs.png) 

lookup-join-predicate ::= 'ON' 'PRIMARY'? 'KEYS' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/lookup-join-predicate.png) 

### [](#index-join-clause)Index JOIN

index-join-clause ::= [index-join-type](#index-join-type)? 'JOIN' [index-join-rhs](#index-join-rhs) [index-join-predicate](#index-join-predicate)

![Syntax diagram](../_images/n1ql-language-reference/index-join-clause.png) 

index-join-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/index-join-type.png) 

index-join-rhs ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/index-join-rhs.png) 

index-join-predicate ::= 'ON' 'PRIMARY'? 'KEY' [expr](index.md#N1QL%5FExpressions) 'FOR' [alias](identifiers.md#identifier-alias)

![Syntax diagram](../_images/n1ql-language-reference/index-join-predicate.png) 

## [](#nest-clause)NEST Clause

nest-clause ::= [ansi-nest-clause](#ansi-nest-clause) | [lookup-nest-clause](#lookup-nest-clause) | [index-nest-clause](#index-nest-clause)

![Syntax diagram](../_images/n1ql-language-reference/nest-clause.png) 

### [](#ansi-nest-clause)ANSI NEST

ansi-nest-clause ::= [ansi-nest-type](#ansi-nest-type)? 'NEST' [ansi-nest-rhs](#ansi-nest-rhs) [ansi-nest-predicate](#ansi-nest-predicate)

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-clause.png) 

ansi-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-type.png) 

ansi-nest-rhs ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-rhs.png) 

ansi-nest-predicate ::= 'ON' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-predicate.png) 

### [](#lookup-nest-clause)Lookup NEST

lookup-nest-clause ::= [lookup-nest-type](#lookup-nest-type)? 'NEST' [lookup-nest-rhs](#lookup-nest-rhs) [lookup-nest-predicate](#lookup-nest-predicate)

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-clause.png) 

lookup-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-type.png) 

lookup-nest-rhs ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-rhs.png) 

lookup-nest-predicate ::= 'ON' 'KEYS' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-predicate.png) 

### [](#index-nest-clause)Index NEST

index-nest-clause ::= [index-nest-type](#index-nest-type)? 'NEST' [index-nest-rhs](#index-nest-rhs) [index-nest-predicate](#index-nest-predicate)

![Syntax diagram](../_images/n1ql-language-reference/index-nest-clause.png) 

index-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/index-nest-type.png) 

index-nest-rhs ::= [keyspace-ref](#keyspace-ref) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/index-nest-rhs.png) 

index-nest-predicate ::= 'ON' 'KEY' [expr](index.md#N1QL%5FExpressions) 'FOR' [alias](identifiers.md#identifier-alias)

![Syntax diagram](../_images/n1ql-language-reference/index-nest-predicate.png) 

## [](#unnest-clause)UNNEST Clause

unnest-clause ::= [unnest-type](#unnest-type)? ( 'UNNEST' | 'FLATTEN' ) [expr](index.md#N1QL%5FExpressions) ( 'AS'? [alias](identifiers.md#identifier-alias) )?

![Syntax diagram](../_images/n1ql-language-reference/unnest-clause.png) 

unnest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )

![Syntax diagram](../_images/n1ql-language-reference/unnest-type.png) 

## [](#comma-separated-join)Comma-Separated Join

comma-separated-join ::= ',' ( [rhs-keyspace](#rhs-keyspace) | [rhs-subquery](#rhs-subquery) | [rhs-generic](#rhs-generic) )

![Syntax diagram](../_images/n1ql-language-reference/comma-separated-join.png) 

## [](#use-clause)USE Clause

use-clause ::= [use-keys-clause](#use-keys-clause) | [use-index-clause](#use-index-clause)

![Syntax diagram](../_images/n1ql-language-reference/use-clause.png) 

use-keys-clause ::= 'USE' [use-keys-term](#use-keys-term)

![Syntax diagram](../_images/n1ql-language-reference/use-keys-clause.png) 

use-keys-term ::= 'PRIMARY'? 'KEYS' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/use-keys-term.png) 

use-index-clause ::= 'USE' [use-index-term](#use-index-term)

![Syntax diagram](../_images/n1ql-language-reference/use-index-clause.png) 

use-index-term ::= 'INDEX' '(' [index-ref](#index-ref) ( ',' [index-ref](#index-ref) )* ')'

![Syntax diagram](../_images/n1ql-language-reference/use-index-term.png) 

index-ref ::= [index-name](#index-name)? [index-type](#index-type)?

![Syntax diagram](../_images/n1ql-language-reference/index-ref.png) 

index-name ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/index-name.png) 

index-type ::= 'USING' ( 'GSI' | 'FTS' )

![Syntax diagram](../_images/n1ql-language-reference/index-type.png) 

## [](#let-clause)LET Clause

let-clause ::= 'LET' [alias](identifiers.md#identifier-alias) '=' [expr](index.md#N1QL%5FExpressions) ( ',' [alias](identifiers.md#identifier-alias) '=' [expr](index.md#N1QL%5FExpressions) )*

![Syntax diagram](../_images/n1ql-language-reference/let-clause.png) 

## [](#where-clause)WHERE Clause

where-clause ::= 'WHERE' [cond](#cond)

![Syntax diagram](../_images/n1ql-language-reference/where-clause.png) 

cond ::= [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/cond.png) 

## [](#group-by-clause)GROUP BY Clause

group-by-clause ::= 'GROUP' 'BY' [expr](index.md#N1QL%5FExpressions) ( ',' [expr](index.md#N1QL%5FExpressions) )* [letting-clause](#letting-clause)? [having-clause](#having-clause)? | [letting-clause](#letting-clause)

![Syntax diagram](../_images/n1ql-language-reference/group-by-clause.png) 

letting-clause ::= 'LETTING' [alias](identifiers.md#identifier-alias) '=' [expr](index.md#N1QL%5FExpressions) ( ',' [alias](identifiers.md#identifier-alias) '=' [expr](index.md#N1QL%5FExpressions) )*

![Syntax diagram](../_images/n1ql-language-reference/letting-clause.png) 

having-clause ::= 'HAVING' [cond](#cond)

![Syntax diagram](../_images/n1ql-language-reference/having-clause.png) 

## [](#window-clause)WINDOW Clause

window-clause ::= 'WINDOW' [window-declaration](#window-declaration) ( ',' [window-declaration](#window-declaration) )*

![Syntax diagram](../_images/n1ql-language-reference/window-clause.png) 

window-declaration ::= [window-name](#window-name) 'AS' '(' [window-definition](#window-definition) ')'

![Syntax diagram](../_images/n1ql-language-reference/window-declaration.png) 

window-name ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/window-name.png) 

window-definition ::= [window-ref](#window-ref)? [window-partition-clause](#window-partition-clause)? [window-order-clause](#window-order-clause)?
                      [window-frame-clause](#window-frame-clause)?

![Syntax diagram](../_images/n1ql-language-reference/window-definition.png) 

window-ref ::= [identifier](identifiers.md)

![Syntax diagram](../_images/n1ql-language-reference/window-ref.png) 

window-partition-clause ::= 'PARTITION' 'BY' [expr](index.md#N1QL%5FExpressions) ( ',' [expr](index.md#N1QL%5FExpressions) )*

![Syntax diagram](../_images/n1ql-language-reference/window-partition-clause.png) 

window-order-clause ::= 'ORDER' 'BY' [ordering-term](#ordering-term) ( ',' [ordering-term](#ordering-term) )*

![Syntax diagram](../_images/n1ql-language-reference/window-order-clause.png) 

window-frame-clause ::= ( 'ROWS' | 'RANGE' | 'GROUPS' ) [window-frame-extent](#window-frame-extent) [window-frame-exclusion](#window-frame-exclusion)?

![Syntax diagram](../_images/n1ql-language-reference/window-frame-clause.png) 

window-frame-extent ::= 'UNBOUNDED' 'PRECEDING' | [valexpr](literals.md#numbers) 'PRECEDING' | 'CURRENT' 'ROW' |
                        'BETWEEN' ( 'UNBOUNDED' 'PRECEDING' | 'CURRENT' 'ROW' |
                                     [valexpr](literals.md#numbers) ( 'PRECEDING' | 'FOLLOWING' ) )
                            'AND' ( 'UNBOUNDED' 'FOLLOWING' | 'CURRENT' 'ROW' |
                                     [valexpr](literals.md#numbers) ( 'PRECEDING' | 'FOLLOWING' ) )

![Syntax diagram](../_images/n1ql-language-reference/window-frame-extent.png) 

window-frame-exclusion ::= 'EXCLUDE' ( 'CURRENT' 'ROW' | 'GROUP' | 'TIES' | 'NO' 'OTHERS' )

![Syntax diagram](../_images/n1ql-language-reference/window-frame-exclusion.png) 

## [](#order-by-clause)ORDER BY Clause

order-by-clause ::= 'ORDER' 'BY' [ordering-term](#ordering-term) ( ',' [ordering-term](#ordering-term) )*

![Syntax diagram](../_images/n1ql-language-reference/order-by-clause.png) 

ordering-term ::= [expr](index.md#N1QL%5FExpressions) ( 'ASC' | 'DESC' )? ( 'NULLS' ( 'FIRST' | 'LAST' ) )?

![Syntax diagram](../_images/n1ql-language-reference/ordering-term.png) 

## [](#limit-clause)LIMIT Clause

limit-clause ::= 'LIMIT' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/limit-clause.png) 

## [](#offset-clause)OFFSET Clause

offset-clause ::= 'OFFSET' [expr](index.md#N1QL%5FExpressions)

![Syntax diagram](../_images/n1ql-language-reference/offset-clause.png) 

## [](#%5Frelated-links)Related Links

* [Conventions](conventions.md)