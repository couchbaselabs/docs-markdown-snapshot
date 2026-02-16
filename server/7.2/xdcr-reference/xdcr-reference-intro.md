[View original HTML](/server/7.2/xdcr-reference/xdcr-reference-intro.html)

> XDCR can be configured by means of _Advanced Settings_, and the replicated content determined through _Advanced Filtering Expressions_. This section provides a reference to each. 

## [](#xdcr-settings-and-filtering-expressions)XDCR Settings and Filtering Expressions

XDCR (_Cross Datacenter Replication_) allows data to be replicated across clusters that are potentially locaed in different datacenters. For a conceptual overview, see [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md). For information on managing XDCR, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).

XDCR replications are supported by:

* _Advanced Settings_. The performance of XDCR can be fine-tuned, by means of configuration-settings, specified when a replication is defined. These settings modify compression, source and target nozzles (worker threads), checkpoints, counts, sizes, network usage limits, and more. A detailed reference is provided in [XDCR Advanced Settings](xdcr-advanced-settings.md).
* _Advanced Filtering_. This allows specified subsets of documents to be replicated from the source bucket. Subsets are determined by achieving matches on fields and their values, within documents. Matches are established by means of [Regular Expressions](xdcr-regular-expressions.md) and [Filtering Expressions](xdcr-filtering-expressions.md). General configuration information is provided in [XDCR Advanced Filtering](xdcr-filtering-reference-intro.md).  
Matches that involve different data types are handled implicitly, through either _data-type conversion_ or _collation comparison_. The procedures, as they apply to different data-type combinations, are described in [XDCR Data-Type Conversion](xdcr-filtering-data-type-conversion.md).