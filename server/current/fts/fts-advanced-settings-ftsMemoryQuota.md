[View original HTML](/server/current/fts/fts-advanced-settings-ftsMemoryQuota.html)

The `ftsMemoryQuota` setting controls the maximum usable memory, in MiB, available to the Search Service on each node in your cluster. This RAM allocation applies to each node that has the Search Service in 1 of its Service Groups.

You can configure the `ftsMemoryQuota` from the Couchbase Server Web Console at any time.

If you’re using the Search Service as the only Service on a node, set the `ftsMemoryQuota` to 80% or less of the total available RAM for that node. This guideline leaves enough RAM for your operating system to manage its on-demand filesystem cache. The search process memory maps your index files to support fast access to indexed content.

## [](#configure-the-ftsmemoryquota)Configure the ftsMemoryQuota

To configure the `ftsMemoryQuota` setting:

1. From the Couchbase Server Web Console, go to **Settings**.
2. Under **Memory Quotas**, in the **Search** field, enter a value, in MiB, for the total amount of RAM you want to allocate to the Search Service for each node in your cluster.
3. Click **Save**.