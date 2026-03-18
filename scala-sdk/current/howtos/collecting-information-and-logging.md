---
title: Logging
description: The Scala SDK logs events and also provides an event bus that
  transmits information about the behavior of your database system, including
  system and metric events.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-03-18T03:49:18.767Z
link: xref:scala-sdk:howtos:collecting-information-and-logging.adoc[]
---

[View original HTML](/scala-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> The Scala SDK logs events and also provides an event bus that transmits information about the behavior of your database system, including system and metric events. It has no hard dependency on a specific logger implementation, but you should add one you are comfortable with. 

## [](#configuring-logging)Configuring Logging

The Couchbase Scala SDK has no hard dependency on a specific logger implementation. It tries to find a logger on the class path and uses that logger if it is supported by the SDK. If no logger implementation is found, the standard JDK logger is used.

The following loggers are supported (and tried in this order):

1. SLF4J
2. JDK Logger (java.util.logging)

### [](#configuring-slf4j)Configuring SLF4J

To enable SLF4J, put it on the class path, as well as one of the support logger implementations (like logback). If you want to use logback and include logback-classic, it will be pulled in automatically:

```xml
<dependency>
  <groupId>ch.qos.logback</groupId>
  <artifactId>logback-classic</artifactId>
  <version>1.2.3</version>
</dependency>
```

Or for SBT:

```none
libraryDependencies += "ch.qos.logback" % "logback-classic" % "1.2.3"
```

By default, the log level for logback is set to DEBUG, but with the addition of a logback configuration this can be configured (for example, as a `logback.xml` in the resources folder):

```xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{"yyyy-MM-dd'T'HH:mm:ss,SSSXXX", UTC} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="info">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

Consult the [SLF4J documentation](https://www.slf4j.org/docs.html) for advanced configuration.

### [](#configuring-log4j)Configuring Log4j

Log4j can also be used behind the SLF4J logging facade.

```xml
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.30</version>
</dependency>
```

Or for SBT:

```none
libraryDependencies += "org.slf4j" % "slf4j-log4j12" % "1.7.30"
```

If no configuration is applied, the following message appears:

```none
log4j:WARN No appenders could be found for logger (reactor.util.Loggers$LoggerFactory).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
```

Note that the `Reactor` library which the Scala SDK depends upon also uses the same strategy with SLF4J, so logging for both can be configured with the same strategies out of the box.

This `log4j.xml` sets it to INFO level:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE log4j:configuration SYSTEM "log4j.dtd">
<log4j:configuration xmlns:log4j='http://jakarta.apache.org/log4j/'>

    <appender name="console" class="org.apache.log4j.ConsoleAppender">
        <layout class="org.apache.log4j.PatternLayout">
            <param name="ConversionPattern"
                   value="%d{yyyy-MM-dd'T'HH:mm:ss.SSSZZZZ} %-5p %c{1}:%L - %m%n" />
        </layout>
    </appender>

    <root>
        <level value="INFO" />
        <appender-ref ref="console" />
    </root>

</log4j:configuration>
```

Consult the [Log4J documentation](https://logging.apache.org/log4j/2.x/javadoc.html) for more information and advanced configuration options.

### [](#configuring-the-jdk-logger)Configuring the JDK Logger

If no logging library is found on the class path, the JDK logger (also known as JUL from `java.util.logging`) is used as a fallback.

By default it logs INFO level and above. If you want to set it to DEBUG (or the JUL equivalent: Fine) you can do it like this programmatically before initializing the `Cluster` object (or creating a custom `ClusterEnvironment`):

```scala
import java.util.logging.{ConsoleHandler, Level, Logger}
val logger = Logger.getLogger("com.couchbase.client")
logger.setLevel(Level.FINE)
for (h <- logger.getParent.getHandlers) {
  h match {
    case x: ConsoleHandler => h.setLevel(Level.FINE)
    case _                 =>
  }
}
```

You should not use JUL in production because SLF4J and Log4J provide better configuration options and performance.

## [](#customizing-the-logger)Customizing the Logger

The logger is configured in a way that it should work out of the box for most users, but there might still be occasion where you want to tweak it. The behavior of the logger can be tuned by customizing the `LoggerConfig` on the `ClusterEnvironment`. For example, if you always want to log to `stderr` and ignore SLF4J (even if present on the classpath) and disable JUL you can configure it this way:

```scala
import com.couchbase.client.scala.env.{ClusterEnvironment, LoggerConfig}

val environment = ClusterEnvironment.builder
  .loggerConfig(
    LoggerConfig()
      .fallbackToConsole(true)
      .disableSlf4J(true)
  )
  .build
```

You can also use it to enable the [Mapped Diagnostic Context](http://logback.qos.ch/manual/mdc.html).

## [](#confirming-logging-is-working)Confirming Logging is Working

If logging is configured as recommended and storing at least INFO-level logs, then as a sanity check you should see in your logging a `CoreCreatedEvent` when creating the `Cluster`, looking something like this:

INFO: [com.couchbase.core][CoreCreatedEvent] {"clientVersion":"1.0.0","clientGitHash":"9a360a29","coreVersion":"2.0.1", // ... etc

## [](#the-event-bus)The Event Bus

> [!NOTE]
> Event Bus Stability
> 
> While the event bus functionality itself is considered stable, the events itself may not be. Please only consume the events you are interested in, and add error handling code in case of unexpected behaviour.

Log files are neither fun to wade through, nor do they have any kind of real-time aspect. To make them usable, normally their content is piped into systems such as [Graphite](http://graphite.wikidot.com) or [Logstash](https://www.elastic.co/products/logstash). Since most setups interleave all different kinds of log messages, it makes it very hard to see whats going on, let alone perform post-disaster analysis.

To make the situation better and ultimately improve supportability, the Scala SDK provides you with the ability to tap into all events before they get logged and consume them in "real-time".

You can subscribe to the event bus, and receive and react to events as they are happening; not when someone parses the logs, sends them into another system where an alarm is triggered, and eventually a sysadmin checks what is going on. The time delta between an event happening and reacting to it can thus be substantially decreased.

The following code subscribes to the event bus and prints out all events that are published on it with INFO or WARN level:

```scala
val environmentTry = ClusterEnvironment.builder.build

environmentTry match {
  case Success(env) =>
    env.core.eventBus.subscribe(event => {
      // handle events as they arrive
      if (event.severity() == Event.Severity.INFO || event
            .severity() == Event.Severity.WARN) {
        println(event)
      }
    })

    Cluster.connect(
      "127.0.0.1",
      ClusterOptions
        .create("Administrator", "password")
        .environment(env)
    ) match {
      case Success(cluster) =>
        val bucket = cluster.bucket("travel-sample")

        cluster.disconnect()
        cluster.env.shutdown()

      case Failure(err) => println(s"Failed to connect to cluster: ${err}")
    }

  case Failure(err) => println(s"Failed to create environment: ${err}")
}
```

This leads to output similar to this:

CoreCreatedEvent{severity=INFO, category=com.couchbase.core, duration=PT0S, createdAt=43700573062858, description={"clientVersion":"1.0.0","clientGitHash":"a3d7a770","coreVersion":"2.0.0","coreGitHash":"a3d7a770","userAgent":"couchbase-scala/3.0.0 (Mac OS X 10.14.6 x86_64; OpenJDK 64-Bit Server VM 1.8.0_202-b08)","maxNumRequestsInRetry":32768,"ioEnvironment":{"nativeIoEnabled":true,"eventLoopThreadCount":6,"eventLoopGroups":["KQueueEventLoopGroup"]},"ioConfig":{"captureTraffic":[],"mutationTokensEnabled":true,"networkResolution":"auto","dnsSrvEnabled":true,"tcpKeepAlivesEnabled":true,"tcpKeepAliveTimeMs":60000,"configPollIntervalMs":2500,"kvCircuitBreakerConfig":"disabled","queryCircuitBreakerConfig":"disabled","viewCircuitBreakerConfig":"disabled","searchCircuitBreakerConfig":"disabled","analyticsCircuitBreakerConfig":"disabled","managerCircuitBreakerConfig":"disabled","numKvConnections":1,"maxHttpConnections":12,"idleHttpConnectionTimeoutMs":30000,"configIdleRedialTimeoutMs":300000},"compressionConfig":{"enabled":true,"minRatio":0.83,"minSize":32},"securityConfig":{"tlsEnabled":false,"nativeTlsEnabled":true,"hasTrustCertificates":false,"trustManagerFactory":null},"timeoutConfig":{"kvMs":2500,"kvDurableMs":10000,"managementMs":75000,"queryMs":75000,"viewMs":75000,"searchMs":75000,"analyticsMs":75000,"connectMs":10000,"disconnectMs":10000},"loggerConfig":{"customLogger":null,"fallbackToConsole":false,"disableSlf4j":false,"loggerName":"CouchbaseLogger","diagnosticContextEnabled":false},"orphanReporterConfig":{"emitIntervalMs":10000,"sampleSize":10,"queueLength":1024},"retryStrategy":"BestEffortRetryStrategy","requestTracer":"OwnedSupplier"}, context=CoreContext{coreId=1}, cause=null}

NodeConnectedEvent{severity=INFO, category=com.couchbase.node, duration=PT0S, createdAt=43700609755560, description=Node connected, context=NodeContext{coreId=1, managerPort=8091, remote=127.0.0.1}, cause=null}

BucketOpenedEvent{severity=INFO, category=com.couchbase.core, duration=PT0.281625729S, createdAt=43701036027888, description=Opened bucket "travel-sample", context=CoreContext{coreId=1}, cause=null}

We recommend filtering on the specific events you are interested in, since most of the time only a subset of the published ones will be of use to you. Also, there are new events added between releases so make sure these new events do not break your functionality.

> [!WARNING]
> Blocking Warning
> 
> If you consume the `EventBus` you MUST NOT block inside the consumer callback. It will stall all other consumers. If you must write into a blocking sink like a blocking HTTP API you MUST write it onto a different thread with a non-blocking queue first.

## [](#sdk-telemetry-from-the-server)SDK Telemetry from the Server

In addition to Tracing and other metrics, and client logging, SDK telemetry is also sent to the Server — available from 8.0, and in new Capella Operational clusters — for ingestion with other Prometheus metrics. Capella Operatioal exposes these metrics through the UI.

For self-managed Server, collection can be disabled and enabled through the REST API:

```console
curl --user Administrator:password http://172.17.0.2:8091/settings/appTelemetry -d enabled=true
```

And the Prometheus-format metrics fetched with:

```console
curl --user Administrator:password http://172.17.0.2:8091/metrics
```

Further details can be found in the [Application Telemetry](../../../server/current/rest-api/application-telemetry.md) page.

There may be advantages to collecting information this way, but note that metrics are collected per node, and a central Prometheus instance should be set to collect all metrics so that information is not lost in case of a sudden failover.

Also note that if the cluster is behind a load balancer, the collected metrics may not accurately record the actual correct node with which the SDK interacts.