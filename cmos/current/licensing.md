---
title: Licensing
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/licensing.adoc
  xref: xref:cmos::licensing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/licensing.html)

# Licensing

> CMOS is composed of primarily other OSS software, not linked but used directly. This page provides an overview of the relevant licensing. 

## [](#background)Background

Before diving into this page, it is worth reviewing existing guidance and information from industry or standards organizations on container licensing. A good place to start is with the [Linux Foundation blog post](https://www.linuxfoundation.org/tools/docker-containers-what-are-the-open-source-licensing-considerations/).

## [](#components)Components

This software uses the following components with their associated licensing also captured:

__Table 1\. Component licenses__
| Component                     | License                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Grafana                       | [AGPL 3.0](https://github.com/grafana/grafana/blob/main/LICENSE)                                                                   |
| Grafana JSON API Plugin       | [Apache 2.0](https://github.com/marcusolsson/grafana-json-datasource/blob/main/LICENSE)                                            |
| Loki                          | [AGPL 3.0](https://github.com/grafana/loki/blob/main/LICENSE)                                                                      |
| Prometheus                    | [Apache 2.0](https://github.com/prometheus/prometheus/blob/main/LICENSE)                                                           |
| Alert Manager                 | [Apache 2.0](https://github.com/prometheus/alertmanager/blob/master/LICENSE)                                                       |
| Jaeger                        | [Apache 2.0](https://github.com/jaegertracing/jaeger/blob/master/LICENSE)                                                          |
| Nginx                         | [Custom](http://nginx.org/LICENSE)                                                                                                 |
| Prometheus Merge Tool         | [Apache 2.0](https://github.com/lablabs/prometheus-alert-overrider/blob/master/LICENSE)                                            |
| Alpine.js                     | [MIT](https://github.com/alpinejs/alpine/blob/main/LICENSE.md)                                                                     |
| Couchbase Cluster Monitor     | [Couchbase License Agreement](https://www.couchbase.com/LA03012021)                                                                |
| Various open-source libraries | [notices.txt](https://github.com/couchbase/product-metadata/blob/master/couchbase-observability-stack/blackduck/1.0.0/notices.txt) |

All licences (with the exception of notices.txt for our bespoke code, as it is automatically generated) are in the CMOS source repository and the container in the [/licenses](https://github.com/couchbaselabs/observability/blob/main/microlith/licenses/) directory.

A statement is printed out to standard output/console at start up to indicate acceptance of licensing and where you can find them all.

A simple [helper script](https://github.com/couchbaselabs/observability/blob/main/tools/build-oss-container.sh) is provided as well to build without any proprietary components.

Some of the components can also provide licensing information via a specific endpoint or API call, an example would be [Grafana](https://grafana.com/docs/grafana/latest/packages%5Fapi/data/licenseinfo/).

## [](#binary-licensing)Binary licensing

The various external components are reused directly from the container layers already published by the entities responsible (e.g. Grafana publish the Loki image layers): this container is not redistributing or repackaging them but using as-is.

The container layers used in the deliverable image are:

__Table 2\. Container image licenses__
| Container image | DockerHub URL                                       | License                                                                       |
| --------------- | --------------------------------------------------- | ----------------------------------------------------------------------------- |
| Grafana         | <https://hub.docker.com/r/grafana/grafana>          | [AGPL 3.0](https://github.com/grafana/grafana/blob/HEAD/LICENSING.md)         |
| Loki            | <https://hub.docker.com/r/grafana/loki>             | [AGPL 3.0](https://github.com/grafana/loki/blob/HEAD/LICENSING.md)            |
| Prometheus      | <https://hub.docker.com/r/prom/prometheus>          | [Apache 2.0](https://github.com/prometheus/prometheus/blob/main/LICENSE)      |
| Alert Manager   | <https://hub.docker.com/r/prom/alertmanager>        | [Apache 2.0](https://github.com/prometheus/prometheus/blob/main/LICENSE)      |
| Jaeger          | <https://hub.docker.com/r/jaegertracing/all-in-one> | [Apache 2.0](https://gitlab.cncf.ci/jaegertracing/jaeger/blob/master/LICENSE) |
| Nginx           | <https://hub.docker.com/%5F/nginx>                  | [Custom](http://nginx.org/LICENSE)                                            |

The base image for this container is the Nginx one.

These can all be seen in this example excerpt from the [Dockerfile](https://github.com/couchbaselabs/observability/blob/main/microlith/Dockerfile):

```Dockerfile
FROM grafana/grafana:8.2.7 as grafana-official
FROM grafana/loki:2.4.1 as loki-official
FROM prom/prometheus:v2.31.0 as prometheus-official
FROM prom/alertmanager:v0.23.0 as alertmanager-official
FROM jaegertracing/all-in-one:1.27.0 as jaegaer-official

FROM nginx:alpine

COPY --from=grafana-official /usr/share/grafana /usr/share/grafana
COPY --from=grafana-official /etc/grafana /etc/grafana

COPY --from=loki-official /usr/bin/loki /usr/bin/loki

COPY --from=prometheus-official /bin/prometheus /bin/prometheus
COPY --from=prometheus-official /bin/promtool /bin/promtool
COPY --from=prometheus-official /etc/prometheus/prometheus.yml /etc/prometheus/prometheus.yml
COPY --from=prometheus-official /usr/share/prometheus/console_libraries/ /usr/share/prometheus/console_libraries/
COPY --from=prometheus-official /usr/share/prometheus/consoles/ /usr/share/prometheus/consoles/
```

In each case we use or copy the contents direct from the container layer provided remotely, i.e. published by the provider.

## [](#source-licensing)Source licensing

In addition to the container layers there is reuse of some aspects of configuration in the [Dockerfile](https://github.com/couchbaselabs/observability/blob/main/microlith/Dockerfile) from each component, i.e. source and binary usage. The licensing links for all the source code are as follows:

__Table 3\. Dockerfile licenses__
| Container image | Github repository                            | License                                                                      |
| --------------- | -------------------------------------------- | ---------------------------------------------------------------------------- |
| Grafana         | <https://github.com/grafana/grafana>         | [AGPL 3.0](https://github.com/grafana/grafana/blob/main/LICENSE)             |
| Loki            | <https://github.com/grafana/loki>            | [AGPL 3.0](https://github.com/grafana/loki/blob/main/LICENSE)                |
| Prometheus      | <https://github.com/prometheus/prometheus>   | [Apache 2.0](https://github.com/prometheus/prometheus/blob/main/LICENSE)     |
| Alert Manager   | <https://github.com/prometheus/alertmanager> | [Apache 2.0](https://github.com/prometheus/alertmanager/blob/master/LICENSE) |
| Jaeger          | <https://github.com/jaegertracing/jaeger>    | [Apache 2.0](https://github.com/jaegertracing/jaeger/blob/master/LICENSE)    |

This is direct reuse but combined into a single file with minimal modification (e.g. addition of comments or removal of unnecessary lines).

A good example is Loki configuration taken directly from the [offical Loki Dockerfile](https://github.com/grafana/loki/blob/main/cmd/loki/Dockerfile):

```Dockerfile
# LOKI:
# From https://github.com/grafana/loki/blob/main/cmd/loki/Dockerfile
RUN addgroup -g 10001 -S loki && \
    adduser -u 10001 -S loki -G loki && \
    mkdir -p /loki/rules && \
    mkdir -p /loki/tmprules && \
    mkdir -p /loki/rules-temp && \
    chown -R loki:loki /etc/loki /loki

# See https://github.com/grafana/loki/issues/1928
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

EXPOSE 3100
# USER loki
```

The Loki binary requires some extra configuration but this is taken directly from the official Dockerfile "recipe" for each component. We do comment out unnecessary aspects just to keep aligned with the original and for simpler updates.

CMOS also contains some components written in Golang and other languages which use various open source libraries. Their licenses are included in `notices.txt` in the container images, as well as [on GitHub](https://github.com/couchbase/product-metadata/blob/master/couchbase-observability-stack/blackduck/1.0.0/notices.txt). If the Couchbase Cluster Monitor is included, its notices.txt file can be found in the same locations and [online](https://github.com/couchbase/product-metadata/blob/master/couchbase-cluster-monitor/blackduck/1.0.0/notices.txt).

## [](#license-analysis)License analysis

Licensing documentation of the various container images is not always present on the DockerHub pages or it is linked to documentation site so requires a bit of analysis to extract. If the container image does not provide a license then the initial assumption is it is the same as the source license.

However, the whole image needs to be considered including all software it covers as this is our responsibility - rather then just relying on what the image says. To this end a [Tern](https://github.com/tern-tools/tern) [helper script](https://github.com/couchbaselabs/observability/blob/main/tools/tern-report.sh) is also available in the repository.

The full Tern report can be found [here](http://localhost:8080/tern-licensing-report.html). Note that the Tern report is a full scan of everything in the container and not necessarily how it is used or linked.

### [](#grafana-and-loki)Grafana and Loki

For Grafana and Loki there is a recent blog post: <https://grafana.com/blog/2021/04/20/grafana-loki-tempo-relicensing-to-agplv3/>. This then links out to the source repositories covering the specific components within each that are still Apache 2:

* <https://github.com/grafana/grafana/blob/HEAD/LICENSING.md>
* <https://github.com/grafana/loki/blob/HEAD/LICENSING.md>

In each case they indicate the default license is AGPL-3.

### [](#prometheus-and-alertmanager)Prometheus and Alertmanager

Both Prometheus and Alert Manager link from DockerHub to the documentation site which does cover licensing as Apache 2: <https://prometheus.io/docs/introduction/faq/#what-license-is-prometheus-released-under>Prometheus also says it explicitly on the DockerHub page with an incorrect link, presumably as the information comes directly from the Github repo with the same relative link: <https://github.com/prometheus/prometheus/blob/main/LICENSE>

### [](#jaeger)Jaeger

The Jaeger image has no details on the DockerHub page at all. The source repo indicates it is Apache 2: <https://gitlab.cncf.ci/jaegertracing/jaeger/blob/master/LICENSE>

### [](#nginx)Nginx

The Nginx image license is a custom one linked directly from DockerHub: <http://nginx.org/LICENSE>Whilst it is a specific one, it is essentially a public domain one with the requirement of copyright being included:

```cpp
/*
 * Copyright (C) 2002-2021 Igor Sysoev
 * Copyright (C) 2011-2021 Nginx, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
```