---
title: Feedback and support
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/support.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cmos::support.adoc[]
---

[View original HTML](/cmos/current/support.html)

# Feedback and support

Please use our official [JIRA board](https://issues.couchbase.com/projects/CMOS/issues) to report any bugs and issues with the appropriate components. We also encourage you to use the [Couchbase Forums](https://forums.couchbase.com) for posting any questions or feedback that you might have.

No official support is currently provided but best efforts will be made and we are keen to hear of any issues.

## [](#diagnostics)Diagnostics

All components of CMOS log their output to `/logs/<component>.log` inside the container. By default, they will also log to standard output, which you can access using `docker logs`, `kubectl logs`, or similar. This can be disabled by setting the environment variable `LOG_TO_STDOUT` to `false` when starting CMOS.

### [](#collecting-information)Collecting Information

If the CMOS web server is enabled, visit `/collect-info.html` to create a tar-ball of all CMOS logs and configuration. If you cannot access the web server or it is disabled, the same can be done by running `/collect-information.sh` in the container. The output will be saved to `/tmp/support` in the container. If the web server is enabled, it can also be accessed on `/support`.

> [!WARNING]
> No redaction or sanitization is performed on the output, and it is likely that it will include passwords or other credentials. We recommend inspecting the generated output before uploading it to Couchbase for review.

## [](#reporting-a-vulnerability)Reporting a Vulnerability

Refer to the [Couchbase security policy](https://www.couchbase.com/resources/security#VulnerabilityHandling) for full details.

Please contact [security@couchbase.com](mailto:security@couchbase.com) with details of any vulnerabilities found.