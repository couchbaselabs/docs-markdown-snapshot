[View original HTML](/server/7.6/fts/fts-supported-queries-DocID-query.html)

A DocID query returns the indexed document or documents among the specified set. This is typically used in conjunction queries, to restrict the scope of other queries’ output.

{
"query":{"ids":["airport_8850", "airport_8851"]}
}