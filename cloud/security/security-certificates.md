---
title: Capella Root Certificates
description: Capella automatically generates a root certificate to allow you to
  connect to your cluster from an external application.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/security-certificates.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:security:security-certificates.adoc[]
---

[View original HTML](/cloud/security/security-certificates.html)

# Capella Root Certificates

> Capella automatically generates a root certificate to allow you to connect to your cluster from an external application. If your application needs to verify your connection to your Capella cluster with a certificate, you must use the root certificate provided in the Capella UI. 

## [](#use-your-capella-root-certificate)Use Your Capella Root Certificate

Capella provides an X.509 formatted root certificate as a `.txt` file. To use the root certificate to connect to your Capella cluster, you must re-save the file as a `.pem` or `.crt` file, depending on what certificate format your application is expecting.

To download or copy the root certificate from your Capella cluster:

1. From the **Operational Clusters** page, click the name of the cluster you want to connect to.
2. Go to **Settings** **Security Certificate**.
3. Click **Download** or **Copy**.

> [!TIP]
> If you’re connecting using one of the Couchbase SDKs, you should not need a certificate for your cluster. Authentication and trust should be automatically handled by the SDK.
> 
> If you run into issues, you can download the Capella root certificate and add it as a trusted certificate in your application’s trust store.
> 
> For more information about connecting and authenticating with a certificate through an SDK, see:
> 
> [.NET](../../dotnet-sdk/current/howtos/sdk-authentication.md#authenticating-a-net-client-by-certificate) | [C](../../c-sdk/current/howtos/sdk-authentication.md#certificate-authentication) | [Go](../../go-sdk/current/howtos/sdk-authentication.md#certificate-authentication) | [Java](../../java-sdk/current/howtos/sdk-authentication.md#certificate-authentication) | [Kotlin](#kotlin-sdk:howtos:secure-connections.html#parse-your-own) | [Node.js](../../nodejs-sdk/current/howtos/sdk-authentication.md#authenticating-a-node-js-client-by-certificate) | [PHP](../../php-sdk/current/howtos/sdk-authentication.md#authenticating-a-php-client-by-certificate) | [Python](../../python-sdk/current/howtos/sdk-authentication.md#authenticating-a-python-client-by-certificate) | [Ruby](../../ruby-sdk/current/howtos/sdk-authentication.md#authenticating-a-ruby-client-by-certificate) | [Scala](../../scala-sdk/current/howtos/sdk-authentication.md#authenticating-a-scala-client-by-certificate)

## [](#see-also)See Also

* [Security Best Practices](security.md)
* [Use Customer-Managed Encryption Keys (CMEK) at Rest](cmek.md)
* [Audit Events](auditing.md)