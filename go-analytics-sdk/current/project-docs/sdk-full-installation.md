[View original HTML](/go-analytics-sdk/current/project-docs/sdk-full-installation.html)

> Installation instructions for the Couchbase Go Client. 

Analytics SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](#home:ROOT:sdk.adoc), they are purpose built for analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

## [](#installing-the-sdk)Installing the SDK

You can use `go get` to download the SDK:

```console
$ go get github.com/couchbase/gocbanalytics@v1.0.0
```

|  | In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), Couchbase supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Information about new features, fixes, and known issues — as well as information about how to install earlier release versions — is in the [release notes](#enterprise-analytics-sdk-release-notes.adoc).