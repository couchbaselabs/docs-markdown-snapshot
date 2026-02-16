[View original HTML](/server/current/manage/manage-nodes/manage-data-service-and-rebalance.html)

> You can add or remove the Data Service on an existing node of a cluster by adding or removing the node from the cluster, and then completing the addition or removal of the node by running a rebalance operation. 

Unlike other services, you cannot dynamically add or remove the Data Service on an existing node of a cluster.

You can add any service, including the Data Service (kv), when you add or join a new node to a cluster. Also, when you remove a node, you are removing all the services on that node. To complete the process of adding or removing a node, the rebalance operation must be run. For more information about adding or removing a node and rebalacing using the UI, REST API, or CLI, see:

* [Add a Node and Rebalance](add-node-and-rebalance.md)
* [Remove a Node and Rebalance](remove-node-and-rebalance.md)

## [](#add-the-data-service-on-an-existing-node)Add the Data Service on an Existing Node

To add the Data Service on an existing node of a cluster:

1. Remove the node that you want to add the Data Service to using [Remove a Node and Rebalance](remove-node-and-rebalance.md).
2. Then [add the node](#manage:manage-nodes/add-node-and-rebalance.html) back to the cluster after enabling the Data Service.

Alternatively, you can add a new node with the necessary services configuration, including the Data Service, using [Add a New Node and Rebalance](add-node-and-rebalance.md). Then remove the extraneous node that you no longer need using [Remove a Node and Rebalance](remove-node-and-rebalance.md).

## [](#remove-the-data-service-from-an-existing-node)Remove the Data Service from an Existing Node

To remove the Data Service from an existing node of a cluster:

1. Remove the node with the Data Service that you want to remove using [Remove a Node and Rebalance](remove-node-and-rebalance.md).
2. Then [add the node](#manage:manage-nodes/add-node-and-rebalance.html) back to the cluster after disabling the Data Service.

|  | During the node removal operation, if there are other services on the node that you’re removing for the Data Service reconfiguration, and you do not want those services to be impacted when the node is removed from the cluster, you may need to add those services to another node temporarily. You can also add a new node temporarily with those services enabled. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#see-also)See Also

For more information about modifying non-Data Services on existing nodes, see [Modify Services and Rebalance](modify-services-and-rebalance.md).