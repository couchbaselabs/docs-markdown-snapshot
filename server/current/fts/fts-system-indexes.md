[View original HTML](/server/current/fts/fts-system-indexes.html)

Use the following command to find all the FTS indexes in the system table that can be queried from SQL++.

SELECT * FROM system:indexes

An additional link describes various scenarios in which the FTS Index becomes ineligible to be queried by SQL++.

[Scenarios where FTS Index becomes ineligible to be queried by SQL++](#n1ql/pages/n1ql-language-reference/searchfun.adoc#limitations)

|  | Querying system:indexes only returns indexes on non-system keyspaces. To return all indexes, including indexes on system keyspaces, use the query system:all\_indexes. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |