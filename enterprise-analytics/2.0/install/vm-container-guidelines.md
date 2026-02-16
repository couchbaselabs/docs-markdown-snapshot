[View original HTML](/enterprise-analytics/2.0/install/vm-container-guidelines.html)

> Use virtualized platforms such as AWS and Docker containers to get hardware scalability and complement Enterprise Analytics’s software scalability. 

When deploying Enterprise Analytics on a virtualized platform, some extra considerations should be made.

**Avoid a Single Point of Failure**

If you run multiple nodes on the same host or physical hardware in a virtualized environment, you can inadvertently re-introduce a single point of failure. In environments where you control the virtual machine (VM) placement, Couchbase recommends that you run each Enterprise Analytics node on a different piece of physical hardware.

**Sizing a Virtualized Deployment**

The performance characteristics of physical hardware are well understood. Even though VMs insert a lightweight layer between Enterprise Analytics and the underlying OS, there is an overhead when running Enterprise Analytics on a virtual platform.

For stability and better performance predictability, you should dedicate at least 2 CPU cores to a VM in development environments, and 4 CPU cores to a VM in production.

|  | One of the major benefits of virtualization is the ability to share physical resources and even over-commit these resources. This means each virtual instance can think it has more CPU, RAM, or disk space than is actually physically available. However, in an over-committed environment, you can end up with containers competing with each other causing unpredictable performance and sometimes stability issues. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

For Enterprise Analytics, you should dedicate physical resources to the VM, rather than shared across multiple VMs. For more information about hardware requirements, see [System Resource Requirements](sys-resource-req.md).

**Auto-Failover Threshold**

Due to the fact that the VM is running on top of a hypervisor or container engine, there is a minor CPU performance overhead. In certain circumstances, the default auto-failover timeout in Couchbase can cause some issues. Couchbase recommends that you change the threshold from 30 seconds (the default), to 45 or even 60 seconds, depending on how CPU-intensive your workload is.

**Live Migration**

Some virtualization environments allow you to migrate the VMs between physical nodes and storage backends. When moving the VM, there is the potential for small pauses and network disruption, which can affect the scheduler, and in turn could trigger a failover. When changing the backend storage, disk queues, compaction, or indexing may be affected, which could have a knock-on effect on general performance. Therefore, Couchbase recommends that you use its built-in rebalance mechanism for maintenance.

If it’s necessary to perform a migration, then disable auto-failover beforehand and be prepared for a performance impact during the migration. Pausing, resuming, and snapshotting virtual machines can also have the same effect. These actions should only be performed on an Enterprise Analytics node which has been removed from the cluster.

## [](#additional-considerations-for-containers)Additional Considerations for Containers

This section lists the additional considerations that are applicable only to containers.

**Map Couchbase Node Specific Data to a Local Folder**

An Enterprise Analytics container writes all persistent and node-specific data to `/opt/enterprise-analytics/var` by default. Couchbase recommends that you map this directory to a directory on the host filesystem using the `-v` option to get persistence and performance when using `docker run`.

By mapping the directory `/opt/enterprise-analytics/var` to a directory outside the container with the `-v` option, you can delete the container and recreate it later without losing your data from Enterprise Analytics. You can even update to a container running a later release/version of Enterprise Analytics without losing your data.

In a standard Docker environment using a union filesystem, leaving `/opt/enterprise-analytics/var` inside the container results in some amount of performance degradation.

|  | If you have SELinux enabled, mounting the host volumes in a container requires an extra step. Assuming you’re mounting the \~/couchbase directory on the host filesystem, you need to run the following command once before running your first container on that host: mkdir \~/couchbase && chcon -Rt svirt\_sandbox\_file\_t \~/couchbase |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Increase ULIMIT in Production Deployments**

Enterprise Analytics expects the following changes to `ulimits`:

ulimit -n 40960        # nofile: max number of open files
ulimit -c unlimited    # core: max core file size
ulimit -l unlimited    # memlock: maximum locked-in-memory address space

These `ulimit` settings are necessary when running under heavy load. If you’re just doing light testing and development, you can omit these settings. To set the ulimits in your container, you need to run Couchbase Docker containers with the following additional `--ulimit` flags:

docker run -d --ulimit nofile=40960:40960
--ulimit core=100000000:100000000 --ulimit memlock=100000000:100000000
--$ docker run -d --name ea -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 -p 11207:11207 -p 11210:11210 couchbase/enterprise-analytics

Since `unlimited` is not supported as a value, it sets the `core` and `memlock` values to 100 GB. If your system has more than 100 GB RAM, increase this value to match the available RAM on the system.

|  | The \--ulimit flags only work on Docker 1.6 or later. |
|  | ----------------------------------------------------- |