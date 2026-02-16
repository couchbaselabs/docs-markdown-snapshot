[View original HTML](/server/7.2/fts/fts-query-string-syntax-match-phrase.html)

Placing the search terms in quotes performs a match phrase query.

This query searches for terms in the target that occur in the positions and offsets indicated by the input: this depends on _term\_vectors_, which must have been included in the creation of the index used for the search.

## [](#example)Example

`"continental breakfast"` performs a [match phrase query](fts-supported-queries-match-phrase.md) for the phrase `continental breakfast`.