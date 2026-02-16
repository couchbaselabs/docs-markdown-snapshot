[View original HTML](/server/7.2/cli/cbstats/cbstats-hash.html)

> Provides information about the vBucket hash tables. 

## [](#syntax)Syntax

Request syntax:

cbstats [hostname]:11210 hash
cbstats [hostname]:11210 hash detail

## [](#description)Description

Requesting these stats does affect performance, so don’t do it too regularly, but it’s useful for debugging certain types of performance issues. For example, if your hash table is tuned to have too few buckets for the data load within it, the `max_depth` will be too large, and performance will suffer.

It is also possible to get more detailed hash tables stats by using ‘hash detail’. This prints per-vbucket stats. Each stat is prefixed with `vb_` followed by a number, a colon, then the individual stat name. For example, the stat representing the size of the hash table for vbucket 0 is `vb_0:size=.`

## [](#options)Options

None

## [](#examples)Examples

**Hash request**

cbstats 10.5.2.54:11210 hash

**Hash response**

 avg_count:    0
 avg_max:      0
 avg_min:      0
 largest_max:  0
 largest_min:  0
 max_count:    0
 min_count:    0
 total_counts: 0

__Table 1\. Hash response stats__
| Stat          | Description                                           |
| ------------- | ----------------------------------------------------- |
| avg\_count    | The average number of items per vbucket.              |
| avg\_max      | The average max depth of a vbucket hash table.        |
| avg\_min      | The average min depth of a vbucket hash table.        |
| largest\_max  | The largest hash table depth of in all vbuckets.      |
| largest\_min  | The largest minimum hash table depth of all vbuckets. |
| max\_count    | The largest number of items in a vbucket.             |
| min\_count    | The smallest number of items in a vbucket.            |
| total\_counts | The total number of items in all vbuckets.            |

**Hash detail**

cbstats 10.5.2.54:11210 hash detail

**Hash detail response**

 avg_count:                0
 avg_max:                  0
 avg_min:                  0
 largest_max:              0
 largest_min:              0
 max_count:                0
 min_count:                0
 total_counts:             0
 vb_0:counted:             0
 vb_0:locks:               5
 vb_0:max_depth:           0
 vb_0:mem_size:            0
 vb_0:mem_size_counted:    0
 vb_0:min_depth:           0
 vb_0:reported:            0
 vb_0:resized:             0
 vb_0:size:                3079
 vb_0:state:               replica
 ...

__Table 2\. Hash detail response stats__
| Stat               | Description                                      |
| ------------------ | ------------------------------------------------ |
| state              | The current state of this vbucket.               |
| size               | Number of hash buckets.                          |
| locks              | Number of locks covering hash table operations.  |
| min\_depth         | Minimum number of items found in a bucket.       |
| max\_depth         | Maximum number of items found in a bucket.       |
| reported           | Number of items this hash table reports having.  |
| counted            | Number of items found while walking the table.   |
| resized            | Number of times the hash table resized.          |
| mem\_size          | Running sum of memory used by each item.         |
| mem\_size\_counted | Counted sum of current memory used by each item. |