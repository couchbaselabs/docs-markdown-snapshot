---
title: Logging
description: ""
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.0@cxx-sdk:howtos:collecting-information-and-logging.adoc[]
---

[View original HTML](/cxx-sdk/1.0/howtos/collecting-information-and-logging.html)

# Logging

> 

The Couchbase C++ SDK allows logging to be configured programmatically. Internally, the SDK uses the [spdlog](https://github.com/gabime/spdlog) logging library.

Once the logger has been initialized, The default log level is `info`.

The following log levels are supported (in order of increasing amount of information logged):

1. off
2. critical
3. error
4. warning
5. info
6. debug
7. trace

The C++ SDK can be configured to send logs to standard output, or to a file. The logger can be initialized and logging level changed like so:

```c++
#import <couchbase/logger.hxx>

void
initialize_logger()
{
    // Initialize logging to standard output
    couchbase::logger::initialize_console_logger();

    // Initialize logging to a file
    couchbase::logger::initialize_file_logger("/path/to/file");

    // Set log level
    couchbase::logger::set_level(couchbase::logger::log_level::warn);
}
```