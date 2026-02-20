---
title: Quick Start
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/quickstart.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cmos::quickstart.adoc[]
---

[View original HTML](/cmos/current/quickstart.html)

# Quick Start

You will need a Docker daemon - on Linux use your respective package manager, on macOS or Windows you can use [Docker Desktop](https://www.docker.com/products/docker-desktop).

You will also need a Couchbase Server cluster running and accessible - if you do not already have a test cluster available, we recommend using [Vagrant](https://github.com/couchbaselabs/vagrants) or [Docker](https://docs.couchbase.com/cloud-native-database/containers/docker-basic-install.html) to start one up. Note that CMOS is built for Couchbase Server 7.0 and above, and Prometheus metrics may not be available on versions below 7.0.

1. Run the container: `docker run --rm -d -p 8080:8080 --name cmos couchbase/observability-stack:latest` (if your Couchbase Server is running in Docker, you may need to set [extra options](https://docs.docker.com/network/) to permit them to communicate)
2. Browse to <http://localhost:8080>
3. Click "Add Cluster" and follow the instructions

When you are done testing, run `docker stop cmos` to clean up.

## [](#next-steps)Next steps

* [Architecture overview](architecture.md)
* [Microlith container deployment](deployment-microlith.md)
* [On-premise deployment](deployment-onpremise.md)