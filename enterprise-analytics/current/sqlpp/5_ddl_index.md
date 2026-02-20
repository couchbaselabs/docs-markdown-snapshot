---
title: CREATE INDEX Statements
description: This topic describes how to use a <code>CREATE</code> statement to
  create an index on a remote or standalone collection.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sqlpp:5_ddl_index.adoc[]
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_index.html)

# CREATE INDEX Statements

> This topic describes how to use a `CREATE` statement to create an index on a remote or standalone collection. 

## [](#syntax)Syntax

**CreateIndex EBNF** 

```EBNF
CreateIndex ::= "CREATE" "ANALYTICS"? "INDEX" Identifier ("IF" "NOT" "EXISTS")?
                "ON" QualifiedName
                "(" IndexElement ( "," IndexElement )* ")"
                IndexUnknown?
                IndexCastDefault?
```

**CreateIndex Diagram** 

!["CREATE" "INDEX" Identifier ("IF" "NOT" "EXISTS")? "ON" QualifiedName "(" IndexField ( "," IndexField )* ")" IndexCastDefault?](_images/CreateIndex.png) 

**Show IndexElement Diagram** 

![ArrayIndexElement | IndexField | "(" ( ArrayIndexElement | IndexField ) ")"](_images/IndexElement.png) 

IndexElement

**Show ArrayIndexElement Diagram** 

![( "UNNEST" NestedField )+ ( ":" IndexTypeRef | "SELECT" NestedField ":" IndexTypeRef ( "," NestedField ":" IndexTypeRef )* )](_images/ArrayIndexElement.png) 

ArrayIndexElement

**Show IndexField Diagram** 

![NestedField ":" IndexTypeRef](_images/IndexField.png) 

IndexField

**Show NestedField Diagram** 

![Identifier ( "." Identifier )*](_images/NestedField.png) 

NestedField

**Show IndexTypeRef Diagram** 

!["BIGINT" | "INT" | "DOUBLE" | "STRING" | "DATE" | "TIME" | "DATETIME"](_images/IndexTypeRef.png) 

IndexTypeRef

**Show IndexUnknown Diagram** 

![( "EXCLUDE" | "INCLUDE" ) "UNKNOWN" "KEY"](_images/IndexUnknown.png) 

IndexUnknown

**Show IndexCastDefault Diagram** 

!["CAST" "(" "DEFAULT" "NULL" DateTimeFormatSpec? ")"](_images/IndexCastDefault.png) 

IndexCastDefault

## [](#examples)Examples

The following example creates standard indexes on the identified fields for the specified types.

```SQL++
 CREATE INDEX song_title_idx on music.myPlaylist.countrySongs (title: string);
 CREATE INDEX artist_name_idx on music.myPlaylist.countrySongs (name: string);
 CREATE INDEX release_date_idx on music.myPlaylist.countrySongs (release_date: date);
```

**Show additional examples** 

The following example creates an array index on an array of primitive data types—in this case, an array of strings.

```SQL++
 CREATE INDEX countrySongLikesIdx
 ON music.myPlaylist.countrySongs (UNNEST public_likes: string)
 EXCLUDE UNKNOWN KEY;
```

The following example creates an array index on two nested integer fields in an array of objects.

```SQL++
 CREATE INDEX myPlaylistSongsRatingsIdx
 ON music.myPlaylist.countrySongs (UNNEST reviews
                   SELECT ratings.Lyrics: bigint,
                          ratings.Instrumentals: bigint)
 EXCLUDE UNKNOWN KEY;
```

The following example creates an array index on one string field which is outside of an array and two nested integer fields in a nested array of objects.

```SQL++
 CREATE INDEX myPlaylistArtistSongsRatingsIdx
 ON music.myPlaylist.countrySongs (artist,
                   UNNEST reviews
                   SELECT ratings.Lyrics: bigint,
                          ratings.Instrumentals: bigint)
 EXCLUDE UNKNOWN KEY;
```

## [](#arguments)Arguments

Identifier

For the `CREATE INDEX` statement, the first `Identifier` is the index name.

QualifiedName

The `QualifiedName` identifies the collection to build the index on.

Index Definition

The index definition is contained within brackets, and consists of a list of index elements. Within the index definition, each `IndexElement` can be either an `ArrayIndexElement`, or an `IndexField`. If the index definition contains one or more array index elements, Enterprise Analytics creates an array index. If the index definition contains only index fields, it creates a standard, non-array index. To eliminate ambiguity, you can parenthesize the `IndexElement` itself, as in cases where the index definition contains both array index elements and index fields.

UNNEST

Within an `ArrayIndexElement`, the UNNEST keyword denotes a field or nested field that contains an array, and the SELECT denotes one or more fields or nested fields inside an object of the aforementioned array. If an array contains only primitive types—strings, integers, etc.—then you specify only UNNEST. Each indexed field in the array index element must have a type identifier.

IndexField

The `IndexField` consists of a `NestedField` that specifies a field path into the indexed JSON document. Specify a type when using array indexes or a CAST modifier.

IndexUnknown

The `IndexUnknown` modifier enables you to specify whether you want the system to make an entry or not in a standard, non-array index when the indexed key’s value is NULL or MISSING.

> [!NOTE]
> Array indexes cannot include NULL or MISSING values. For this reason, you must specify EXCLUDE UNKNOWN KEY when defining an array index.