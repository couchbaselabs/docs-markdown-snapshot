---
title: Cross-Origin Resource Sharing (CORS)
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/cors-configuration-for-app-services.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:app-services::app-endpoints/cors-configuration-for-app-services.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/cors-configuration-for-app-services.html)

# Cross-Origin Resource Sharing (CORS)

> Use Cross-Origin Resource Sharing (CORS) Configuration per App Endpoint to enable granular access control to trusted domains for Origin and Login purposes in browser-based and hybrid applications. 

## [](#about-cors-configuration)About CORS Configuration

You can configure CORS per App Endpoint to relax the [Same-Origin](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin%5Fpolicy) access policy and enable granular access controls across different areas of your applications. Using CORS, you can:

* Define specific, trusted domains for loading of resources for use in your browser-based or hybrid applications.
* Define allowed HTTP headers for use in [pre-flight requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted%5Frequests).
* Set the max age of pre-flight requests in seconds.

Your application can run locally with its resources stored elsewhere on the cloud.

You can access and enable App Endpoint CORS configuration from the config page in App Endpoint settings and selecting the checkbox. Once enabled, you can set the permitted Origins, Login Origins, Max Age for requests and permissions for any custom HTTP headers. Origins and Login Origin are formatted as a comma separated list of URLs.

> [!CAUTION]
> At least one Origin must be configured upon confirmation of the CORS configuration.

### [](#cors-configuration-for-browser-based-applications)CORS Configuration for Browser-Based Applications

Enabling CORS is required for browser-based applications that synchronize data with App Services using the [Couchbase Lite JavaScript SDK](../../couchbase-lite-javascript/current/index.md).

When configuring CORS for your App Endpoint to support browser-based sync, configure the following settings:

| Setting                                       | Requirement                                                                                                                                           | Example                                          |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Origin(Access-Control-Allow-Origin)           | Specify the exact origin of your front-end application. **Do not use** the wildcard \*, as authentication requires that you specify explicit origins. | https://myapp.example.com https://localhost:3000 |
| Login Origin                                  | Provide the same specific domain(s) used in Origin. **Do not use** the wildcard \*.                                                                   | https://myapp.example.com https://localhost:3000 |
| Allowed Headers(Access-Control-Allow-Headers) | Must include Authorization to enable browsers to send authentication headers needed for sync.                                                         | Authorization, Content-Type                      |
| Max Age(Access-Control-Max-Age)               | Optional. Define how long (in seconds) browsers can cache pre-flight requests.                                                                        | 3600 (1 hour)Default: 5 seconds                  |

These settings ensure that browser-based clients using the Couchbase Lite JavaScript SDK can securely and reliably replicate data through App Services.

> [!IMPORTANT]
> Browser-based synchronization does not support private browsing mode.

### [](#benefits-of-cors-for-developers)Benefits of CORS for Developers

You can support more flexible architectures for your applications including web and hybrid mobile apps with CORS. CORS provides a method to relax the Same-Origin access policy selectively and safely. This enables access to client-side functions and provide the capability to interface directly with APIs such as the App Services Public REST API. Customize your applications further with separate CORS configurations for each of your App Endpoints. Configuring CORS per an individual App Endpoint allows you to explicitly define which domains can access the resources at each App Endpoint, which types of requests are permitted, and which headers each request can include.

You can configure your App Endpoints for different use cases with a specific CORS configuration, such as:

* Same-Origin Requests - CORS is not needed.
* Broad Browser Support - Keep in mind that some older versions of browsers may have limited or no CORS support.
* Low Latency - Endpoints that frequently require the use of HTTP requests could experience a latency overhead as requests are processed.
* High Security Demand - If applications are running on less secure origins such as HTTP, this could pose security risks for your users.

### [](#available-cors-configuration-options)Available CORS Configuration Options

After you enable CORS configuration, you can configure the following settings for CORS per each of your App Endpoints:

### [](#origin-access-control-allow-origin)Origin (Access-Control-Allow-Origin)

You can set allowed origin domains for your App Endpoint to consider trusted sources of data. You can also use the `*` wildcard symbol to permit any domain as the origin.

> [!NOTE]
> You cannot use the `*` wildcard if you also plan to authenticate users.

Do not use the wildcard  in production environments, due to the security vulnerabilities it can create in your application. You cannot use the wildcard `` with authenticated requests, including those from browser-based applications using the Couchbase Lite JavaScript SDK. 

### [](#login-origin)Login Origin

You can define domains permitted to manage sessions. This is useful if you want to [manage user sessions through the Public REST API.](../references/rest%5Fapi%5Fpublic.md#tag/Session)

> [!NOTE]
> For browser-based applications using the Couchbase Lite JavaScript SDK, specify the same explicit domain(s) used in Origin rather than using the wildcard `*`.

### [](#allowed-headers-access-control-allow-headers)Allowed Headers (Access-Control-Allow-Headers)

You can define and specify the headers permitted within pre-flight requests with your App Endpoints. This allows you to tailor request handling to the needs of your App Endpoint.

### [](#max-age-access-control-max-age)Max Age (Access-Control-Max-Age)

You can define the length of time in seconds a pre-flight request can be cached in the browser.

Altering this value to the needs of your App Endpoint can reduce server request latency.

> [!NOTE]
> The default value for Max Age is 5, with the range of values being 0 - 86400, or a day in seconds.

## [](#see-also)See Also

* [Public REST API](../references/rest%5Fapi%5Fpublic.md)
* [Access Control and Data Validation](access-control-data-validation.md)
* [Mozilla CORS documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)