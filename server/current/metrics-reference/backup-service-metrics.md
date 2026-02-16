[View original HTML](/server/current/metrics-reference/backup-service-metrics.html)

> A list of the metrics provided by the Backup Service. 

The following Backup Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

Histograms

Note that each histogram metric will generate three time series, with the following suffixes:

* `_count`
* `_sum`
* `_bucket`

Please refer to [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) for more information.

| Tip | The x.y.z badge shows the Couchbase Server version the metric was added in. The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present). |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| backup\_data\_size7.0.0gauge / bytes Repository backed up data size                                     |
| ------------------------------------------------------------------------------------------------------- |
| backup\_dispatched7.0.0counter Number of tasks dispatched to be run                                     |
| backup\_location\_check7.0.0counter Number of location checks performed                                 |
| backup\_request\_duration\_seconds8.0.0histogram Histogram of the request duration                      |
| backup\_task\_duration\_seconds7.0.0histogram Histogram of the task duration                            |
| backup\_task\_orphaned7.0.0counter Number of tasks that were triggered to run but the status is unknown |
| backup\_task\_run7.0.0counter Number of tasks run                                                       |