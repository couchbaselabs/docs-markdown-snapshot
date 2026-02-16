[View original HTML](/enterprise-analytics/current/reference/rest-cluster-manualfailover-intro.html)

> Manual failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Manual Failover_. A complete overview is provided in [Failover](#learn:clusters-and-availability/failover.adoc).

The APIs described in this section are listed in the following table.

| HTTP Method | URI                               | Documented at                                                           |
| ----------- | --------------------------------- | ----------------------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)                       |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](#reference:rest-failover-graceful.adoc)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](#reference:rest-node-recovery-incremental.adoc) |