---
title: A-Z Word List
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/word-list.adoc
  xref: xref:styleguide::word-list.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/styleguide/word-list.html)

# A-Z Word List

Use the following list to determine how to spell, capitalize, and use specific words and terms in Couchbase Documentation.

For terms not covered here, see the [Google Developer Style Guide's Word List](https://developers.google.com/style/word-list).

[#](#num) | [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

## [](#num)Numbers & Symbols

| .NET                | Add a period at the start of the acronym. Follow the official capitalization as set by Microsoft. For more information, see [Capitalization](capitalization.md).                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1; 1,000; 1,000,000 | Write all numbers as numerals, regardless of size. Use commas to separate every group of 3 digits in a large number. For more information about how to format numbers, see the [Google Developer Style Guide](https://developers.google.com/style/numbers#commas-and-decimal-points-in-numbers). |
| \->                 | If you want a \->, this will be fine inside a code block. Outside of a code block, Antora/AsciiDoc will convert it to → or &#8594;. To avoid this, escape the hyphen: \\->                                                                                                                       |
| % (UI Only)         | Never write out percent or percentage in the UI. Use the % symbol, and put it in brackets next to the name of the measurement. For example, Index Fragmentation (%).                                                                                                                             |

## [](#a)A

| Term                                                   | Notes                                                                                                                                                                                                                                |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| a / an                                                 | See [Articles (a, an, the)](articles.md).                                                                                                                                                                                            |
| about                                                  | When introducing a [Links](links.md), use information about, not information on.                                                                                                                                                     |
| Access List                                            | Use [allowlist](#allowlist).                                                                                                                                                                                                         |
| ACID Transactions                                      | See [Transactions](#transactions).                                                                                                                                                                                                   |
| adapter                                                | Always use adapter, not adaptor.                                                                                                                                                                                                     |
| ad hoc                                                 | Never add a hyphen to ad hoc. Use adhoc for the SQL++ parameter. Do not use [Italics](italic.md).                                                                                                                                    |
| admin                                                  | Do not use. Write out administrator.                                                                                                                                                                                                 |
| afterwards                                             | Use afterwards, not afterward.                                                                                                                                                                                                       |
| allowlist / denylist                                   | Write out allowlist and [denylist](#denylist) as 1 word. Do not add a hyphen.                                                                                                                                                        |
| Amazon cloud                                           | Follow the official capitalization as set by Amazon. For more information, see [Capitalization](capitalization.md).                                                                                                                  |
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) | Write out in full, capitalizing all nouns, for the first use on a page. Use Amazon MSK for short on subsequent uses.                                                                                                                 |
| Amazon MSK Kafka pipeline                              | Do not expand MSK when referring to a specific pipeline. Capitalize as shown. Do not capitalize pipeline.                                                                                                                            |
| Amazon S3                                              | Make sure to capitalize Amazon and the S in S3.                                                                                                                                                                                      |
| amber                                                  | If you need to refer to traffic lights or a health warning color, use amber, not [yellow](#yellow).                                                                                                                                  |
| Analytics Service                                      | Legacy product name. Use Capella Analytics or Enterprise Analytics, instead, depending on the product.                                                                                                                               |
| APAC                                                   | Write as a proper acronym. For more information, see [Capitalization](capitalization.md).                                                                                                                                            |
| API                                                    | Application Programming Interface. Do not write out for first use on a page.                                                                                                                                                         |
| app / application                                      | Use app for mobile applications. Use application for client software, such as Couchbase Server.                                                                                                                                      |
| as of                                                  | Use only when referring to dates or time. If talking about a software version, use a phrase such as beginning with Couchbase Server n.n                                                                                              |
| AsciiDoc                                               | Follow the official capitalization as set by Eclipse Foundation. For more information, see [Capitalization](capitalization.md).                                                                                                      |
| autocomplete                                           | Write as 1 word. Do not add a hyphen.                                                                                                                                                                                                |
| auto-failover                                          | Add the hyphen, unless using as part of a command name. Use automatically fails over or fails over automatically as the verb.                                                                                                        |
| automatic schema discovery                             | Do not add a hyphen. Do not capitalize.                                                                                                                                                                                              |
| auto-sharding                                          | Add the hyphen.                                                                                                                                                                                                                      |
| Availability Zone                                      | Capitalize Availability and Zone.                                                                                                                                                                                                    |
| AWS Identity and Access Management (IAM)               | Do not write as just IAM when referring to Amazon Web Services Identity and Access Management. Write as AWS IAM after the first expanded use on a page. It's okay to use AWS Identity and Access Management (IAM) for the first use. |

## [](#b)B

| Term                         | Notes                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| backend                      | Use backend as the noun. Use back-end as the adjective.                                                                |
| backup                       | Use backup as the noun and the adjective. Use back up as the verb.                                                     |
| \[Couchbase\] Backup Manager | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md). |
| backward-compatible          | Add the hyphen.                                                                                                        |
| beta release                 | Use beta release before the product name. Use only Beta after the product name (Couchbase Server 5.0 Beta)             |
| BI                           |                                                                                                                        |
| bidirectional                | Write as 1 word. Do not add a hyphen.                                                                                  |
| big data                     | Write as 2 words. Do not add a hyphen. Do not capitalize.                                                              |
| Blacklist                    | Do not use. See [denylist](#denylist).                                                                                 |
| Blocklist                    | Do not use. See [denylist](#denylist).                                                                                 |
| blog                         | Do not use weblog.                                                                                                     |
| bootstrap                    | Write as 1 word. Do not add a hyphen.                                                                                  |
| buckets                      |                                                                                                                        |
| bytes                        | kB / MB / GB / TB / PB for decimal bytes. Use KiB / MiB / GiB for 1024, 1 048 576, 1 073 741 824, and so on.           |

## [](#c)C

| Term                                                | Notes                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C++                                                 | Antora will sometimes interpret ++ as markup instructions, and leave only C on the page. Follow [asciidoctor recommendations](https://asciidoctor.org/docs/user-manual/#charref-attributes) and use {cpp}.                                                                                                                                                                                |
| Capella Analytics                                   | Proper product name for analytics on Capella. Write as written. Do not use Columnar. Refer to specific instances of Capella Analytics as [clusters](#cluster).                                                                                                                                                                                                                            |
| Compare and Swap (CAS)                              | Write out for the first use on a page. Capitalize as a proper product name.                                                                                                                                                                                                                                                                                                               |
| cbbackupmgr                                         | Follow the capitalization and spelling set in the code.                                                                                                                                                                                                                                                                                                                                   |
| cbcollect                                           | Follow the capitalization and spelling set in the code.                                                                                                                                                                                                                                                                                                                                   |
| cbc                                                 | Follow the capitalization and spelling set in the code. Couchbase CLI tools that come with libcouchbase (LCB). Variety of binaries installed as /usr/bin/cbc\*, for example, cbc-pillowfight, cbc-version                                                                                                                                                                                 |
| cbq                                                 | Follow the capitalization and spelling set in the code. Official product name for the query shell.                                                                                                                                                                                                                                                                                        |
| cbtransfer                                          | Follow the capitalization and spelling set in the code.                                                                                                                                                                                                                                                                                                                                   |
| CentOS                                              | Follow the official capitalization as set by Red Hat. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                      |
| cheat sheet                                         | Write as 2 words. Do not add a hyphen.                                                                                                                                                                                                                                                                                                                                                    |
| checkpoint                                          | Write as 1 word. Do not add a hyphen.                                                                                                                                                                                                                                                                                                                                                     |
| cloud                                               | Write in lowercase unless as part of a product name.                                                                                                                                                                                                                                                                                                                                      |
| cloud native                                        | Use cloud native as the noun. Use cloud-native as the adjective.                                                                                                                                                                                                                                                                                                                          |
| cloud service provider (CSP)                        | Write in all lowercase. Make sure to include the acronym in brackets. Use the acronym for subsequent uses on a page.                                                                                                                                                                                                                                                                      |
| cluster                                             | Preferred term, if referring to Couchbase Server or Couchbase Capella operational or Capella Analytics. We no longer use [database](#database).                                                                                                                                                                                                                                           |
| Cluster Manager                                     | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| codebase                                            | Write as 1 word. Do not add a hyphen.                                                                                                                                                                                                                                                                                                                                                     |
| collection                                          | Do not capitalize. Do not capitalize even when referring to a remote, external, or standalone collection.                                                                                                                                                                                                                                                                                 |
| Columnar                                            | Old product name for Capella Analytics. Do not use.                                                                                                                                                                                                                                                                                                                                       |
| command line                                        | Use command line as the noun. Use command-line as the adjective.                                                                                                                                                                                                                                                                                                                          |
| config(s)                                           | Do not use. Use configuration as the noun. Use configure as the verb.                                                                                                                                                                                                                                                                                                                     |
| Confluent Cloud                                     | Capitalize as a proper noun.                                                                                                                                                                                                                                                                                                                                                              |
| Confluent Cloud Kafka pipeline                      | Capitalize Confluent, Cloud, and Kafka as proper nouns. Do not capitalize pipeline.                                                                                                                                                                                                                                                                                                       |
| ConfigProviderBase                                  | Follow the capitalization and spelling set in the code.                                                                                                                                                                                                                                                                                                                                   |
| Couchbase                                           | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| Couchbase Autonomous Operator (CAO)                 | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| Couchbase Capella                                   | Couchbase Cloud or Couchbase Managed Cloud in legacy documentation. Use operational cluster if you need to specify which type of Capella instance, as opposed to Capella Analytics. Write as Couchbase Capella \+ operational cluster for the first use on a page. Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md). |
| Couchbase Cluster Connection Protocol (CCCP)        | Write out for the first use on a page. Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                             |
| Couchbase Columnar                                  | Old product name for Capella Analytics. Do not use.                                                                                                                                                                                                                                                                                                                                       |
| (the) Couchbase Data Platform                       | Write as data platform if not preceded by Couchbase. Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                               |
| Couchbase Eventing Service                          | When referring to Couchbase Services, use title case.                                                                                                                                                                                                                                                                                                                                     |
| Couchbase Functions                                 | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| Couchbase Managed Cloud                             | Legacy term for Couchbase Capella. Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                 |
| Couchbase Monitoring and Observability Stack (CMOS) | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| Couchbase Server n.n                                | Write as Couchbase Server n.n for the first use on a page. Use Server n.n afterwards. Do not refer to as the Couchbase Server.                                                                                                                                                                                                                                                            |
| Couchbase Server Enterprise Edition                 | Write as Couchbase Server Enterprise Edition.                                                                                                                                                                                                                                                                                                                                             |
| Couchstore                                          | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                    |
| cross datacenter replication (XDCR)                 | Write out for the first use on a page. Do not capitalize. Do not add a hyphen.                                                                                                                                                                                                                                                                                                            |
| curl                                                | Write in all lowercase, including on the command line.                                                                                                                                                                                                                                                                                                                                    |

## [](#d)D

| Term                             | Notes                                                                                                                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| database                         | Do not capitalize when referring to a database in Capella Analytics. Do not use to refer to Capella operational [clusters](#clusters).          |
| Database Change Protocol (DCP)   | Write out for the first use on a page.                                                                                                          |
| data center                      | Write as 2 words. Do not add a hyphen.                                                                                                          |
| datacenter replication           | Write as 2 words. Do not add a hyphen.                                                                                                          |
| data-centric                     | Add the hyphen.                                                                                                                                 |
| data-driven                      | Add the hyphen.                                                                                                                                 |
| data definition language (DDL)   | Do not write out for the first use on a page.                                                                                                   |
| data manipulation language (DML) | Do not write out for the first use on a page.                                                                                                   |
| data modeling                    | Write as 2 words. Do not add a hyphen.                                                                                                          |
| DataOps                          | Capitalize the D and O.                                                                                                                         |
| data provider                    | Do not use.                                                                                                                                     |
| dataset                          | Write as 1 word. Do not add a hyphen.                                                                                                           |
| datasheet                        | Write as 1 word. Do not add a hyphen.                                                                                                           |
| Data Service                     | When referring to Couchbase Services, use title case.                                                                                           |
| data source                      | Do not capitalize. Do not use data provider.                                                                                                    |
| data store                       | Write as 2 words. Do not add a hyphen.                                                                                                          |
| data structure                   | Write as 2 words. Do not add a hyphen.                                                                                                          |
| decrypter                        | Use the American English spelling rule and use an e.                                                                                            |
| deduplicate                      | Do not add a hyphen.                                                                                                                            |
| denylist                         | Write out [allowlist](#allowlist) and denylist as 1 word. Do not add a hyphen.                                                                  |
| Deprecated                       | Use to indicate that a feature will be removed in a future release. Do not use it to mean removed and specify that the feature will be removed. |
| design document                  | Do not capitalize. Do not add a hyphen.                                                                                                         |
| DevOps                           | Capitalize the D and O.                                                                                                                         |
| different from                   | Use different from, not different to.                                                                                                           |
| digitization                     | Use the American English spelling rule and use a z.                                                                                             |
| disassociate                     | Preferred term. Do not use dissociate or unassociate, when describing removing the association with a key.                                      |
| Distributed Transactions         | See [transactions](#transactions).                                                                                                              |

## [](#e)E

| Term                                      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| earlier/later                             | Use earlier/later to describe software versions. Do not use older/newer or lower/higher.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| e-commerce                                | Write as E-commerce if at the beginning of a sentence. Add the hyphen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| e.g.                                      | Do not use Latin abbreviations. Use for example, instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| elastic-scale                             | Add the hyphen to use as an adjective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Elasticsearch                             | Follow the official capitalization as set by Elastic. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                                                                                                                                                                     |
| em dash (—)                               | See [Dashes](dashes.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| email                                     | Do not add a hyphen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EMEA                                      | Write as a proper acronym. For more information, see [Capitalization](capitalization.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| encrypter                                 | Use the American English spelling rule and use an e.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| end user                                  | Use end user as the noun. Use end-user as the adjective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Engagement Database                       | Capitalize as a proper product name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ensure                                    | Do not use. Use make sure, instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Enterprise Analytics                      | Product name for the on-premise Couchbase Analytics solution. Do not use Analytics Service or Columnar.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ePayment                                  | Write as shown. Do not hyphenate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| error-free                                | Add the hyphen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| etc.                                      | Do not use Latin abbreviations. Use and so on, instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Event-Condition-Action model              | Add the hyphens. Capitalize Event, Condition, and Action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Eventing Service                          | When referring to Couchbase Services, use title case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| eviction, ejection, expiration            | Use **eviction** to refer to removing a record entirely from any system or cache. Items are evicted from ephemeral buckets when RAM is full. Use **ejection** to refer to removing a record from 1 layer, but still keeping it in a system. Items are ejected from Couchstore or Magma buckets when they're removed from RAM, but still stored on disk. Use **expiration** to refer to a record being deleted after a specific time period. Items are expired when their time to live (TTL) is greater than 0, and that time has passed. |
| external collection                       | Do not capitalize.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| extract, transform, load (ETL) operations | Write out for the first use on a page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## [](#f)F

| Term                         | Notes                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| failover                     | Write as 1 word for the noun. Write as 2 words for the verb.                                                            |
| FAQ                          | Write as a proper acronym. For more information, see [Capitalization](capitalization.md).                               |
| fewer                        | Use for countable nouns or to describe a noun that's plural. For example, fewer clusters. Otherwise, use [less](#less). |
| filename                     | Write as 1 word. Do not add a hyphen.                                                                                   |
| filesystem                   | Write as 1 word. Do not add a hyphen.                                                                                   |
| fine-grained                 | Add the hyphen.                                                                                                         |
| five nines                   | Add a hyphen to use as an adjective.                                                                                    |
| Function-as-a-Service (FaaS) | Write out for the first use on a page.                                                                                  |
| focused                      | Write with 1 s.                                                                                                         |
| ForestDB                     | Follow the official capitalization as set by Couchbase. For more information, see [Capitalization](capitalization.md).  |
| FQDN                         | Fully-Qualified Domain Name. Write out for the first use on a page.                                                     |
| free-form                    | Add the hyphen.                                                                                                         |
| full-stack                   | Add the hyphen to use as an adjective.                                                                                  |
| full-text indexes            | Add the hyphen.                                                                                                         |
| Full-Text Search (FTS)       | Use Search Service. When referring to Couchbase Services, use title case.                                               |

## [](#g)G

| Term                           | Notes                                                                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geo-distributed                | Add the hyphen.                                                                                                                                         |
| Geofencing                     | Do not add a hyphen. Write as 1 word. Use a capital G.                                                                                                  |
| GitHub                         | Follow the official capitalization as set by GitHub. For more information, see [Capitalization](capitalization.md).                                     |
| Global Secondary Indexes (GSI) | Write out for the first use on a page. Capitalize as a proper product name.                                                                             |
| Google Cloud Platform          | Follow the official capitalization as set by Google. For more information, see [Capitalization](capitalization.md).                                     |
| GUID                           | Globally Unique Identifier. Write in all caps as an acronym. For more information, see [Capitalization](capitalization.md).                             |
| gzip                           | Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names. |

## [](#h)H

| Term                                              | Notes                                                                                              |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| hard-coded                                        | Add the hyphen.                                                                                    |
| hard-wired                                        | Add the hyphen.                                                                                    |
| hash key                                          | Do not add a hyphen. Do not write as 1 word.                                                       |
| help desk                                         | Do not add a hyphen.                                                                               |
| hostname                                          | Write as 1 word.                                                                                   |
| HTML                                              | Follow the official capitalization. For more information, see [Capitalization](capitalization.md). |
| hybrid cloud                                      | Do not add a hyphen.                                                                               |
| hybrid transaction/analytical processing (HTAP)   | Write out for the first use on a page.                                                             |
| hybrid operational and analytic processing (HOAP) | Write out for the first use on a page.                                                             |

## [](#i)I

| Term                               | Notes                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------- |
| infrastructure as a service (IaaS) | Write out for the first use on a page.                                 |
| i.e.                               | Do not use Latin abbreviations. Use that is, instead.                  |
| indexes                            | Do not use indices.                                                    |
| IndexScan                          | Write as 1 word. Capitalize Index and Scan.                            |
| industry standard                  | Do not add a hyphen.                                                   |
| information about / information on | See [about](#about).                                                   |
| initargs                           | Write out in all lowercase as in the code.                             |
| in-memory                          | Add the hyphen.                                                        |
| install                            | Use install for the verb. Use installation for the noun.               |
| instance                           | Do not use. See [cluster](#cluster).                                   |
| intra-cluster replication          | Add the hyphen.                                                        |
| Internet                           | Capitalize as a proper noun.                                           |
| Internet of Things (IoT)           | Write out for the first use on a page. Make sure to use a lowercase o. |

## [](#j)J

| Term       | Notes                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JAR        | Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names. |
| Java       | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                                                      |
| JavaScript | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                                                      |
| JIRA       | Follow the official capitalization as set by Atlassian. For more information, see [Capitalization](capitalization.md).                                  |
| joins      | Do not capitalize.                                                                                                                                      |
| JSON       | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                                                      |

## [](#k)K

| Term       | Notes                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| Kafka      | Follow the official capitalization as set by Apache. For more information, see [Capitalization](capitalization.md). |
| keyspace   | Do not add a hyphen. Write as 1 word.                                                                               |
| key-value  | Add the hyphen.                                                                                                     |
| KV Service | Use [Data Service](#data). When referring to Couchbase Services, use title case.                                    |

## [](#l)L

| Term                  | Notes                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Last Write Wins (LWW) | Write out for the first use on a page.                                                                                                                                                                       |
| less                  | Use less for items that are measured, cannot be easily quantified or counted, or mass singular nouns. For example, less trouble, less time, less effort. For nouns that can be counted, use [fewer](#fewer). |
| libcouchbase (LCB)    | Write out for first use on a page.                                                                                                                                                                           |
| LDAP                  | Lightweight Directory Access Protocol. Do not write out for the first use on a page.                                                                                                                         |
| link                  | Do not use data link. Do not capitalize.                                                                                                                                                                     |
| livestream            | Do not add a hyphen or space.                                                                                                                                                                                |
| log in                | Use log in for the verb. Use log-in for the adjective. Use login for the noun.                                                                                                                               |
| low latency           | Do not add a hyphen.                                                                                                                                                                                         |
| low write latency     | Do not add a hyphen.                                                                                                                                                                                         |

## [](#m)M

| Term                                | Notes                                                                                                                                                           |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MapReduce                           | Do not add a hyphen. Write as 1 word. Capitalize Map and Reduce.                                                                                                |
| MapReduce views                     | Use [Views Service](#views). When referring to Couchbase Services, use title case.                                                                              |
| massively parallel processing (MPP) | Do not add a hyphen. Write out for the first use on a page.                                                                                                     |
| master/slave                        | Do not use. See [primary/secondary](#primary).                                                                                                                  |
| Memcached bucket                    | Only capitalize Memcached. Try to only use in legacy documentation.                                                                                             |
| memcached                           | Do not capitalize if not referring to a Memcached bucket. Used to describe the distributed memory object caching system from Memcached in legacy documentation. |
| memory-optimized indexes (MOI)      | Do not capitalize. Add the hyphen between memory and optimized. Write out for the first use on a page.                                                          |
| metadata                            | Do not add a hyphen.                                                                                                                                            |
| microservices                       | Do not add a hyphen.                                                                                                                                            |
| microservices architecture          | Do not add a hyphen. Do not capitalize.                                                                                                                         |
| microservices applications          | Do not add a hyphen. Do not capitalize.                                                                                                                         |
| millisecond (ms)                    | Write the number of milliseconds with a space, as in 50 ms.                                                                                                     |
| mission critical                    | Use mission critical as the noun. Use mission-critical as the adjective.                                                                                        |
| MongoDB™                            | Follow the official capitalization as set by MongoDB. Add the trademark symbol, ™. For more information, see [Capitalization](capitalization.md).               |
| multichannel                        | Do not add a hyphen.                                                                                                                                            |
| multi-datacenter                    | Add the hyphen.                                                                                                                                                 |
| Multi-Dimensional Scaling (MDS)     | Capitalize as a proper product name. Write out for the first use on a page. When used to refer to the capability, use multi-dimensional scaling.                |
| multilingual                        | Do not add a hyphen.                                                                                                                                            |
| Multi-master                        | Do not use. See [primary/secondary](#primary).                                                                                                                  |
| multi-model                         | Add the hyphen.                                                                                                                                                 |
| multi-region                        | Add the hyphen.                                                                                                                                                 |
| multi-threaded                      | Add the hyphen.                                                                                                                                                 |

## [](#n)N

| Term                    | Notes                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| N1QL                    | The old term for [SQL++](#sqlpp). Do not use, except in legacy documentation.                                            |
| nameservers             | Do not add a hyphen.                                                                                                     |
| nginx                   | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                       |
| Node.js                 | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                       |
| nonpersistent           | Do not add a hyphen.                                                                                                     |
| note that               | Do not use.                                                                                                              |
| not-recently-used (NRU) | Write out for the first use on a page. Add the hyphen between each word.                                                 |
| npm                     | Node Package Manager. Follow the official capitalization. For more information, see [Capitalization](capitalization.md). |
| numReplicas             | Use camel case as set in the code.                                                                                       |
| nxdomain                | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).                       |

## [](#o)O

| Term                           | Notes                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| OAuth                          | Capitalize the O and the A.                                                                                  |
| Objective-C                    | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).           |
| offline                        | Do not add a hyphen.                                                                                         |
| Omnichannel                    | Capitalize the O. Do not add a hyphen.                                                                       |
| on demand                      | Use on demand as the noun. Use on-demand as the adjective.                                                   |
| one can                        | Do not use. Address the user directly with you.                                                              |
| online                         | Do not add a hyphen.                                                                                         |
| on-premises                    | Use on premises as the noun. Use on-premises as the adjective.                                               |
| on-site/off-site               | Add a hyphen.                                                                                                |
| open source                    | Do not add a hyphen.                                                                                         |
| operational cluster            | Use when referring to a cluster on Couchbase Capella operational, as opposed to a Capella Analytics cluster. |
| opt-out                        | Add the hyphen.                                                                                              |
| Oxford comma                   | See [Commas](commas.md).                                                                                     |
| optimisticReplicationThreshold | Use camel case as set in the code.                                                                           |

## [](#p)P

| Term                                   | Notes                                                                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page                                   | Use to refer to what a user moves to or accesses from a [menu](menus.md) or [tab](tabs.md) in the UI. For more information, see [Page](pages.md).       |
| parameterized                          | Use the American English spelling rule and use a z.                                                                                                     |
| passlist                               | Do not use. See [allow list](#allowlist).                                                                                                               |
| peer to peer                           | Use peer to peer as the noun. Use peer-to-peer as the adjective.                                                                                        |
| PDF                                    | Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names. |
| PLAIN authentication                   | Write PLAIN in all caps. Do not capitalize authentication.                                                                                              |
| Pluggable Authentication Modules (PAM) | Write out for the first use on a page.                                                                                                                  |
| plug in                                | Use plugin as the noun. Use plug-in as the adjective. Use plug in as the verb.                                                                          |
| preload                                | Do not add a hyphen.                                                                                                                                    |
| primary/secondary                      | Use instead of [master/slave](#master).                                                                                                                 |

## [](#q)Q

| Term                  | Notes                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| query editor          | Do not capitalize.                                                                                    |
| query executor        | Do not capitalize.                                                                                    |
| Query History         | Capitalize as a proper product name.                                                                  |
| Query Monitor         | Capitalize as a proper product name. To refer to the act of monitoring a query, use query monitoring. |
| query plan            | Do not capitalize.                                                                                    |
| query plan visualizer | Do not capitalize.                                                                                    |
| Query Service         | When referring to Couchbase Services, use title case.                                                 |
| query shell           | Use the product name, CBQ.                                                                            |
| Query Workbench       | Capitalize as a proper product name.                                                                  |
| quick links           | Write as 2 separate words.                                                                            |
| quotation marks       | Do not use quotation marks outside of code. Do not use fancy quotes ("" '') characters.               |

## [](#r)R

| Term                             | Notes                                                                                                       |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| rack awareness (RA)              | Write out for the first use on a page. Do not write as Rack/Zone Awareness.                                 |
| Read Committed                   | When referring to the isolation level for transactions, do not add a hyphen. Capitalize Read and Committed. |
| Read-Your-Own-Writes (RYOW)      | Write out for the first use on a page. Add hyphens between each word.                                       |
| real time                        | Write as 2 separate words when used as a noun. Add the hyphen when used as an adjective.                    |
| rebalance                        | Write as all 1 word. Do not add a hyphen.                                                                   |
| refer to                         | Use [see](#see), instead.                                                                                   |
| reindexing                       | Write as all 1 word. Do not add a hyphen.                                                                   |
| remote collection                | Do not capitalize.                                                                                          |
| repo                             | Do not use. Write out the full word, repository.                                                            |
| retryable                        | Do not write as retriable.                                                                                  |
| risk-free                        | Add the hyphen.                                                                                             |
| Role-Based Access Control (RBAC) | Write out for the first use on a page. Capitalize the first letter of each word as a proper product name.   |
| RxJava                           | Follow the official capitalization. For more information, see [Capitalization](capitalization.md).          |

## [](#s)S

| Term                            | Notes                                                                                                                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| schema-less                     | Add the hyphen. Do not capitalize. You can also use flexible schema.                                                                                                                                  |
| scope                           | Do not capitalize.                                                                                                                                                                                    |
| SCRAM-SHA-256 and SCRAM-SHA-512 | Make sure to add the hyphens between each word. Write in all caps.                                                                                                                                    |
| screenshot                      | Do not add a hyphen.                                                                                                                                                                                  |
| SDK                             | Software Development Kit. Do not write out for the first use on a page.                                                                                                                               |
| SDKs                            | Treat acronyms as regular words when making them plural. For more information, see the [Google Developer Style Guide](https://developers.google.com/style/abbreviations#making-abbreviations-plural). |
| Search Service                  | When referring to Couchbase Services, use title case.                                                                                                                                                 |
| see                             | Use instead of [refer to](#refer) for introducing links.                                                                                                                                              |
| Service Group                   | When referring to Service Groups, capitalize Service and Groups.                                                                                                                                      |
| setup                           | Use setup as the noun. Use set-up as the adjective. Use set up as the verb.                                                                                                                           |
| sgcollect                       | Write as all 1 word in lowercase, as per the code for the sgcollect utility.                                                                                                                          |
| sign up                         | Use sign up as the verb. Use sign-up as the adjective.                                                                                                                                                |
| single node                     | Use single node as the noun. Use single-node as the adjective.                                                                                                                                        |
| Spark                           | Do not specify as Apache Spark. Capitalize Spark and Datasets. Follow the official capitalization as set by Apache. For more information, see [Capitalization](capitalization.md).                    |
| SQL++                           | The Couchbase query language. Pronounced as sequel plus plus. Write in documentation as a SQL++. For more information, see [Articles (a, an, the)](articles.md).                                      |
| standalone collection           | Do not capitalize.                                                                                                                                                                                    |
| startup                         | Use startup as the noun.                                                                                                                                                                              |
| Structured Streaming            | Write out as Structured Streaming API for the first use on a page.                                                                                                                                    |
| Storm                           | Do not specify as Apache Storm. Follow the official capitalization as set by Apache. For more information, see [Capitalization](capitalization.md).                                                   |
| sub-clause                      | Add the hyphen. Do not capitalize.                                                                                                                                                                    |
| Sub-Document                    | Add the hyphen and capitalize Sub and Document.                                                                                                                                                       |
| sub-millisecond                 | Add the hyphen.                                                                                                                                                                                       |
| subqueries                      | Do not add a hyphen.                                                                                                                                                                                  |
| sudo                            | Write in all lowercase as per the Linux command.                                                                                                                                                      |
| swappiness                      |                                                                                                                                                                                                       |

## [](#t)T

| Term                | Notes                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TAP                 |                                                                                                                                                             |
| tar                 | Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names.     |
| targetNozzlePerNode | Use camel case, as per the code.                                                                                                                            |
| tcpdump             | The command-line packet analyzer. Follow the official capitalization as set by Tcpdump Team. For more information, see [Capitalization](capitalization.md). |
| THP                 |                                                                                                                                                             |
| time series         | Write as 2 words, in sentence case. Do not capitalize, do not add a hyphen.                                                                                 |
| time to live (TTL)  | Do not capitalize time to live. Spell out the acronym the first time you use it on a page.                                                                  |
| touchpoint(s)       | Write as 1 word. Do not add a hyphen.                                                                                                                       |
| topology aware      | Add the hyphen when used as an adjective.                                                                                                                   |
| towards             | Use towards, not toward.                                                                                                                                    |
| Transactions        | Use Distributed ACID Transactions for the first use on a page. You can use Distributed Transactions or Transactions later on the page.                      |

## [](#u)U

| Term               | Notes                                                                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu             | Follow the official capitalization as set by Canonical. For more information, see [Capitalization](capitalization.md). Use the correct article: an, not a. For more information, see [Articles (a, an, the)](articles.md). |
| under construction | Use as a banner on incomplete or in process pages. Do not use wip or work in progress.                                                                                                                                     |
| uninstall          | Write as all 1 word. Do not add a hyphen.                                                                                                                                                                                  |
| UNNEST             | Capitalize SQL and SQL++ clauses. For more information, see [Capitalization](capitalization.md).                                                                                                                           |

## [](#v)V

| Term               | Notes                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| vBucket / vBuckets | Do not capitalize the v. Capitalize Bucket.                                                                         |
| vBucketMap         | Do not capitalize the v. Capitalize Bucket and Map.                                                                 |
| vBucketServerMap   | Do not capitalize the v. Capitalize Bucket, Server, and Map.                                                        |
| Views Service      | When referring to Couchbase Services, use title case.                                                               |
| virtualization     | Use the American English spelling rule and use a z.                                                                 |
| vmstat             | The virtual memory statistics reporter, which is built into Linux. Write in all lowercase.                          |
| VMware             | Follow the official capitalization as set by VMware. For more information, see [Capitalization](capitalization.md). |

## [](#w)W

| Term             | Notes                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| warmup           | Write as 1 word. Do not add a hyphen.                                                                            |
| web              | Do not use all capitals.                                                                                         |
| web page         | Do not use. Use [page](#page), instead. If you have to specify web page, do not write as 1 word or add a hyphen. |
| Whitelist        | See [allowlist](#allowlist).                                                                                     |
| whitepaper       | Write as all 1 word. Do not add a hyphen.                                                                        |
| Wi-Fi            | Use the proper capitalization and add a hyphen. Do not use wifi or WiFi.                                         |
| wip              | Do not use. See [under construction](#under).                                                                    |
| work in progress | Do not use work in progress as a banner on incomplete or in process pages. Use [under construction](#under).     |

## [](#x)X

| Term  | Notes                                                                                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X.509 | Capitalize the X, and do not forget the period when referring to X.509 certificates.                                                                                                                          |
| XDCR  | Cross Data Center Replication (XDCR). Spell out for the first use on a page.                                                                                                                                  |
| XML   | Use the formal name of the file type, as an XML file. Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names. |

## [](#y)Y

| Term   | Notes                |
| ------ | -------------------- |
| yellow | See [amber](#amber). |

## [](#z)Z

| Term    | Notes                                                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zendesk | Follow the official capitalization as set by Zendesk. For more information, see [Capitalization](capitalization.md).                                    |
| zip     | Follow the [Google Developer Style Guide](https://developers.google.com/style/filenames#file-type-names)'s guidance on how to refer to file type names. |