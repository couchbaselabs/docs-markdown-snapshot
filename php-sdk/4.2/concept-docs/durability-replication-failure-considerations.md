[View original HTML](/php-sdk/4.2/concept-docs/durability-replication-failure-considerations.html)

> Data durability refers to the fault tolerance and persistence of data in the face of software or hardware failure. Even the most reliable software and hardware might fail at some point, and along with the failures, introduce a chance of data loss. Couchbase’s durability features include Synchronous Replication, and the possibility to use distributed, multi-document ACID transactions. It is the responsibility of the development team and the software architect to evaluate the best choice for each use case. 

Unresolved include directive in modules/concept-docs/pages/durability-replication-failure-considerations.adoc - include::7.5@sdk:shared:partial$durability-replication-failure-considerations.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/durability-replication-failure-considerations.adoc - include::7.5@sdk:shared:partial$durability-replication-failure-considerations.adoc\[\] Unresolved include directive in modules/concept-docs/pages/durability-replication-failure-considerations.adoc - include::7.5@sdk:shared:partial$durability-replication-failure-considerations.adoc\[\]

## [](#older-server-versions)Older Server Versions

If a version of Couchbase Server lower than 6.5 is being used then the fallback is 'client verified' durability.

|  | Client Verified durability is supported in [PHP SDK 3.2](#3.2@durability-replication-failure-considerations.adoc#older-server-versions) but not in 4.0\. Legacy support will be available in a later 4.x release. See the [SDK 4.0 migration considerations](../project-docs/migrating-sdk-code-to-3.n.md#sdk4-specifics). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Unresolved include directive in modules/concept-docs/pages/durability-replication-failure-considerations.adoc - include::7.5@sdk:shared:partial$durability-replication-failure-considerations.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/durability-replication-failure-considerations.adoc - include::7.5@sdk:shared:partial$durability-replication-failure-considerations.adoc\[\]