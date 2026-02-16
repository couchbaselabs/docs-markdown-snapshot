[View original HTML](/cxx-sdk/1.1/howtos/provisioning-cluster-resources.html)

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. 

Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/).

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. Or through the REST API. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The C++ SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — `couchbase::bucket_manager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1bucket%5F%5Fmanager.html).
* QueryIndexManager — `couchbase::query_index_manager` — see <https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1query>_index_manager.html\[API docs\].
* CollectionManager — `couchbase::collection_manager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1collection%5F%5Fmanager.html).
* AnalyticsIndexManager — `couchbase::analytics_index_manager` — see <https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1analytics>_index_manager.html\[API docs\].
* SearchIndexManager — `couchbase::search_index_manager` — see <https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1search>_index_manager.html\[API docs\].