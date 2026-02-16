[View original HTML](/enterprise-analytics/current/migration/post-migration.html)

> This section outlines the cutover plan and post-migration validation steps to verify a smooth transition from Couchbase Analytics Service (CBAS) to Couchbase Enterprise Analytics. 

This section outlines the cutover plan and post-migration validation steps to verify a smooth transition from Couchbase Analytics Service (CBAS) to Couchbase Enterprise Analytics. This cutover plan minimizes downtime and makes sure that all applications and services continue to function during and after the migration.

## [](#cutover-plan-for-dual-cluster-environment)Cutover Plan for Dual-Cluster Environment

To set up and run 2 or more clusters simultaneously, use 1 of the following approaches:

* Parallel Cluster Configuration
* Application Cutover Approach

The parallel cluster configuration utilizes both CBAS (within an existing Couchbase Server OLTP cluster) and Couchbase Enterprise Analytics (dedicated OLAP cluster) to operate simultaneously during the transition period.

* **Production Environment**: Analytics applications continue using CBAS through SDK connections and JDBC drivers for Couchbase Server Analytics Service and Capella Operational Analytics Service.
* **Development/Test Environment**: You’re advised to create a replica of your applications using the new Analytics SDK. The new replica application must connect to Couchbase Enterprise Analytics cluster for validation and testing. For more information, see [Migration](migration-process.md).
* **Data Synchronization**: Real-time data replication from operational Couchbase Server to both CBAS and Enterprise Analytics clusters.

* Preparation and Validation

  * Deploy Couchbase Enterprise Analytics cluster in parallel to existing CBAS infrastructure
  * Configure data synchronization from Couchbase Server to both analytics platforms
  * Update development and test application instances to connect to Enterprise Analytics cluster
  * Validate query compatibility and performance in non-production environments
* Gradual Application Migration

  * SDK-based Analytics Applications: You’re advised to create a replica of your applications using the new Analytics SDK. All the CBAS analytics features are available in the new enterprise analytics SDK. The new replica application should connect to Couchbase Enterprise Analytics cluster for validation and testing. For more information, see [Migration](#migration:migration-process.aodc).
  * BI Tools with JDBC: Modify JDBC connection URLs to target Enterprise Analytics JDBC driver and endpoints. You need to use the existing connectors for JDBC with the new endpoints for existing BI tools.
  * Implement feature flags or configuration switches to enable rapid rollback if needed.
  * Monitor both clusters for performance, data consistency, and application behavior.
* Production Cutover

  * Migrate the new application to production environment.
  * Execute planned maintenance window for production application cutover.
  * Switch production applications from CBAS to Enterprise Analytics using pre-validated connection configurations.
  * Maintain CBAS cluster in standby mode for immediate rollback capability.
  * Implement monitoring and alerting for both clusters during transition period.
* CBAS Decommissioning

  * Monitor Enterprise Analytics cluster stability and performance for minimum 2 weeks post-cutover.
  * Validate all critical business processes and reporting functions.
  * After successful validation period, begin CBAS cluster decommissioning:

    * Stop CBAS Analytics Service on Couchbase Server nodes.
    * Remove CBAS-specific configurations and indexes.
    * Reclaim resources (CPU, memory, storage) allocated to CBAS.
    * Update monitoring and backup procedures to remove CBAS references.
  * Document final decommissioning steps and resource reclamation for audit purposes.

## [](#final-checklist)Final Checklist

Make sure all essential tasks are complete and verify before declaring migration success and transitioning operations to the new database. This is a critical step that serves as a final validation.

* **Application Connectivity Verification**: Confirm that all applications can connect to the new database environment.
* **Initial Data Verification**: Confirm that a representative sample of data is migrated.
* **Performance sanity validation**: Test some critical, high-impact queries to verify that initial performance is within acceptable limits and there are no regressions in performance.
* **Security Validation**: Verify that basic security configurations are in place and functioning (For example, RBAC).
* **Sign-off**: Obtain formal sign-off from designated stakeholders that migration activity is complete.