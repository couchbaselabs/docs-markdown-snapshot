---
title: Eventing REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/eventing-rest-api/pages/index.adoc
  xref: xref:7.6@server:eventing-rest-api:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/eventing-rest-api/index.html)

# Eventing REST API

## [](#overview)Overview

The Eventing REST API provides methods to work with and manipulate Couchbase Eventing functions.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                |
| ---------- | ------------------------------------------------------------------------------------------ |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                       |
| **host**   | The host name or IP address of a node running the Eventing Service. **Example:** localhost |
| **port**   | The Eventing Service REST port. Use 18096 for secure access. **Values:** 8096, 18096       |

### Examples on this page

In the HTTP request examples:

* `$HOST` is the host name or IP address of a node running the Eventing Service.
* `$ADMIN` is the user name of an administrator — see [Security](#security).
* `$USER` is the user name of any authorized user — see [Security](#security).
* `$PASSWORD` is the password to connect to Couchbase Server.

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Activation](#tag-Activation)  
[Advanced](#tag-Advanced)  
[Global Config](#tag-GlobalConfig)  
[List](#tag-List)  
[Logging](#tag-Logging)  
[Statistics](#tag-Statistics)  
[Status](#tag-Status)

### [](#tag-Activation)Activation

**Table of Contents**

[Deploy a Function](#basic%5Fdeploy)  
[Pause a Function](#basic%5Fpause)  
[Resume a Function](#basic%5Fresume)  
[Undeploy a Function](#basic%5Fundeploy)

#### [](#basic%5Fdeploy)Deploy a Function

POST /api/v1/functions/{function}/deploy

##### [](#basic%5Fdeploy-description)Description

Deploys an undeployed function. This is the preferred invocation.

##### [](#basic%5Fdeploy-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#basic%5Fdeploy-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#basic%5Fdeploy-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests)Example HTTP Requests

Deploy a global function

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/deploy"
```

Deploy a scoped function

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/deploy?bucket=bulk&scope=data"
```

#### [](#basic%5Fpause)Pause a Function

POST /api/v1/functions/{function}/pause

##### [](#basic%5Fpause-description)Description

Pauses a function and creates a DCP checkpoint such that on a subsequent resume no mutations will be lost. This is the preferred invocation.

##### [](#basic%5Fpause-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#basic%5Fpause-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#basic%5Fpause-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-2)Example HTTP Requests

Pause a global function

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/pause"
```

Pause a scoped function

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/pause?bucket=bulk&scope=data"
```

#### [](#basic%5Fresume)Resume a Function

POST /api/v1/functions/(function}/resume

##### [](#basic%5Fresume-description)Description

Resumes a paused function from its paused DCP checkpoint. This is the preferred invocation.

##### [](#basic%5Fresume-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#basic%5Fresume-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#basic%5Fresume-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-3)Example HTTP Requests

Resume a global function

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/resume"
```

Resume a scoped function

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/resume?bucket=bulk&scope=data"
```

#### [](#basic%5Fundeploy)Undeploy a Function

POST /api/v1/functions/{function}/undeploy

##### [](#basic%5Fundeploy-description)Description

Undeploys a function. This is the preferred invocation.

##### [](#basic%5Fundeploy-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#basic%5Fundeploy-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |

##### [](#basic%5Fundeploy-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-4)Example HTTP Requests

Undeploy a global function

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/undeploy"
```

Undeploy a scoped function

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/undeploy?bucket=bulk&scope=data"
```

### [](#tag-Advanced)Advanced

**Table of Contents**

[Create or Import a Function](#adv%5Ffunction%5Fimport)  
[Create or Import Multiple Functions](#adv%5Ffunction%5Fimport%5Fall)  
[View a Function](#adv%5Ffunction%5Fview)  
[View Multiple Functions](#adv%5Ffunction%5Fview%5Fall)  
[Delete Function](#adv%5Ffunction%5Fzap)  
[Delete Multiple Functions](#adv%5Ffunction%5Fzap%5Fall)  
[Export Multiple Functions](#adv%5Fmultiple%5Fexport)  
[Import Multiple Functions](#adv%5Fmultiple%5Fimport)  
[View Function Settings](#adv%5Fsettings%5Fget)  
[Update Function Settings](#adv%5Fsettings%5Fupdate)  
[View Function Config](#adv%5Fstructure%5Fget)  
[Update Function Config](#adv%5Fstructure%5Fupdate)  
[View Function Code](#adv%5Ftext%5Fget)  
[Update Function Code](#adv%5Ftext%5Fupdate)

#### [](#adv%5Ffunction%5Fimport)Create or Import a Function

POST /api/v1/functions/{function}

##### [](#adv%5Ffunction%5Fimport-description)Description

Creates or imports a single function.

Consumes

* application/json

##### [](#adv%5Ffunction%5Fimport-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

Body Parameter

| Name             | Description                                                                                                                                                                              | Schema                           |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **Body**required | A single function definition object, or an array containing a single function definition object. The function name in the definition object must match that given by the path parameter. | [Function Request](#AddFunction) |

##### [](#adv%5Ffunction%5Fimport-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Ffunction%5Fimport-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-5)Example HTTP Requests

Import a global function

curl request

```sh
curl -X POST -d @./my_function.json \
  "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function"
```

Import a scoped function

curl request

```sh
curl -X POST -d @./my_function.json \
  "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function?bucket=bulk&scope=data"
```

#### [](#adv%5Ffunction%5Fimport%5Fall)Create or Import Multiple Functions

POST /api/v1/functions

##### [](#adv%5Ffunction%5Fimport%5Fall-description)Description

Creates or imports multiple functions.

If any function's `language_compatibility` field is missing, the value will be set to the highest version supported by the server, unlike [Import Multiple Functions](#adv%5Fmultiple%5Fimport).

Consumes

* application/json

##### [](#adv%5Ffunction%5Fimport%5Fall-parameters)Parameters

Body Parameter

| Name             | Description                                                                                                                                                                                           | Schema                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Body**required | A single function definition object, or an array containing one or more function definition objects. Function names must be unique. When multiple functions have the same name, an error is reported. | [Functions Request](#AddFunctions) |

##### [](#adv%5Ffunction%5Fimport%5Fall-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Ffunction%5Fimport%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-6)Example HTTP Requests

Import multiple functions

curl request

```sh
curl -X POST -d @./array_of_functions.json \
  "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions"
```

#### [](#adv%5Ffunction%5Fview)View a Function

GET /api/v1/functions/{function}

##### [](#adv%5Ffunction%5Fview-description)Description

Provides a listing of a complete function definition available in the cluster. The function could be in any state: deployed, undeployed, or paused. If saved to a file the function definition can be imported into the cluster or a different cluster. However any changes to the function definition made to the file outside the UI are discouraged.

Produces

* application/json

##### [](#adv%5Ffunction%5Fview-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#adv%5Ffunction%5Fview-responses)Responses

| HTTP Code | Description                                  | Schema                                   |
| --------- | -------------------------------------------- | ---------------------------------------- |
| 200       | Returns a single function definition object. | [Function Definition](#handler%5Fschema) |
| 404       | Failure.                                     |                                          |

##### [](#adv%5Ffunction%5Fview-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-7)Example HTTP Requests

View a global function definition

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function"
```

View a scoped function definition

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function?bucket=bulk&scope=data"
```

Save a global function definition to file

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function" \
  -o my_function.json
```

Save a scoped function definition to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function?bucket=bulk&scope=data" \
  -o my_function.json
```

#### [](#adv%5Ffunction%5Fview%5Fall)View Multiple Functions

GET /api/v1/functions

##### [](#adv%5Ffunction%5Fview%5Fall-description)Description

Provides an array of definitions of all functions available in the cluster. The functions may be in any state: deployed, undeployed, or paused. If saved to a file the function definitions can be imported into the cluster or a different cluster. However any changes to the function definition made to the file outside the UI are discouraged.

If this API is run as a non-Administrator, the results are filtered via RBAC to include only the function scopes the user has access to.

Produces

* application/json

##### [](#adv%5Ffunction%5Fview%5Fall-responses)Responses

| HTTP Code | Description                                                          | Schema                                         |
| --------- | -------------------------------------------------------------------- | ---------------------------------------------- |
| 200       | Returns an array containing one or more function definition objects. | [Function Definition](#handler%5Fschema) array |
| 404       | Failure.                                                             |                                                |

##### [](#adv%5Ffunction%5Fview%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-8)Example HTTP Requests

View all function definitions

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions"
```

Save all function definitions to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions" \
  -o array_of_functions.json
```

#### [](#adv%5Ffunction%5Fzap)Delete Function

DELETE /api/v1/functions/{function}

##### [](#adv%5Ffunction%5Fzap-description)Description

Deletes a specific function from the cluster.

Use this API with caution, as it's irreversible.

##### [](#adv%5Ffunction%5Fzap-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#adv%5Ffunction%5Fzap-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Ffunction%5Fzap-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-9)Example HTTP Requests

Delete a global function

curl request

```sh
curl -XDELETE "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function"
```

Delete a scoped function

curl request

```sh
curl -XDELETE "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function?bucket=bulk&scope=data"
```

#### [](#adv%5Ffunction%5Fzap%5Fall)Delete Multiple Functions

DELETE /api/v1/functions

##### [](#adv%5Ffunction%5Fzap%5Fall-description)Description

Deletes **all functions** from the cluster. Use this API with caution, as it's irreversible.

If this API is run as a non-Administrator the deleted set will be filtered via RBAC to include only the function scopes the user has access to.

##### [](#adv%5Ffunction%5Fzap%5Fall-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Ffunction%5Fzap%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-request)Example HTTP Request

Delete all functions

curl request

```sh
curl -XDELETE "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions"
```

#### [](#adv%5Fmultiple%5Fexport)Export Multiple Functions

GET /api/v1/export

##### [](#adv%5Fmultiple%5Fexport-description)Description

This is a convenience method to export all function definitions. Exported functions are always set to the undeployed state at the time of export, regardless of their state in the cluster. If saved to a file the function definitions can be imported into the cluster or a different cluster. However any changes to the function definition made to the file outside the UI are discouraged.

If this API is run as a non-Administrator the results are filtered via RBAC to include only the function scopes the user has access to.

Produces

* application/json

##### [](#adv%5Fmultiple%5Fexport-responses)Responses

| HTTP Code | Description                                                          | Schema                                         |
| --------- | -------------------------------------------------------------------- | ---------------------------------------------- |
| 200       | Returns an array containing one or more function definition objects. | [Function Definition](#handler%5Fschema) array |
| 404       | Failure.                                                             |                                                |

##### [](#adv%5Fmultiple%5Fexport-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-10)Example HTTP Requests

View all function definitions

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/export"
```

Save all function definitions to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/export" \
  -o array_of_functions.json
```

#### [](#adv%5Fmultiple%5Fimport)Import Multiple Functions

POST /api/v1/import

##### [](#adv%5Fmultiple%5Fimport-description)Description

Imports multiple functions.

If any function's `language_compatibility` field is missing, the value will be set to 6.0.0, unlike [Create or Import Multiple Functions](#adv%5Ffunction%5Fimport%5Fall).

Consumes

* application/json

##### [](#adv%5Fmultiple%5Fimport-parameters)Parameters

Body Parameter

| Name             | Description                                                                                                                                                                                           | Schema                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Body**required | A single function definition object, or an array containing one or more function definition objects. Function names must be unique. When multiple functions have the same name, an error is reported. | [Functions Request](#AddFunctions) |

##### [](#adv%5Fmultiple%5Fimport-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Fmultiple%5Fimport-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-11)Example HTTP Requests

Import multiple functions

curl request

```sh
curl -X POST -d @./array_of_functions.json \
  "http://$USER:$PASSWORD@$HOST:8096/api/v1/import"
```

#### [](#adv%5Fsettings%5Fget)View Function Settings

GET /api/v1/functions/{function}/settings

##### [](#adv%5Fsettings%5Fget-description)Description

Return or export the full settings for one eventing function in the cluster. The settings can be subsequently imported. However any changes to the function settings made to the file outside the UI are discouraged.

Produces

* application/json

##### [](#adv%5Fsettings%5Fget-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#adv%5Fsettings%5Fget-responses)Responses

| HTTP Code | Description                                                    | Schema                                  |
| --------- | -------------------------------------------------------------- | --------------------------------------- |
| 200       | Returns an object showing settings for the specified function. | [Function Settings](#settings%5Fschema) |
| 404       | Failure.                                                       |                                         |

##### [](#adv%5Fsettings%5Fget-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-12)Example HTTP Requests

View global function settings

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

View scoped function settings

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Save global function settings to file

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings" \
  -o my_function.json
```

Save scoped function settings to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data" \
  -o my_function.json
```

#### [](#adv%5Fsettings%5Fupdate)Update Function Settings

POST /api/v1/functions/{function}/settings

##### [](#adv%5Fsettings%5Fupdate-description)Description

Updates an undeployed or paused function with the provided settings. You can only alter settings when the function is paused or undeployed; attempting to adjust a deployed function will result in an error. During an edit, settings provided are merged. Unspecified attributes retain their prior values.

You must always specify `deployment_status` and `processing_status` when using this REST endpoint to update any option or set of options. To get the current values of `deployment_status` and `processing_status`, see [View All Functions Status](#status%5Fall) or [View Function Status](#status%5Ffunction).

By adjusting `deployment_status` and `processing_status` this command can also deploy or resume a function; however, it cannot pause or undeploy a function.

Consumes

* application/json

##### [](#adv%5Fsettings%5Fupdate-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

Body Parameter

| Name             | Description                                              | Schema                                  |
| ---------------- | -------------------------------------------------------- | --------------------------------------- |
| **Body**required | An object providing settings for the specified function. | [Function Settings](#settings%5Fschema) |

##### [](#adv%5Fsettings%5Fupdate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Fsettings%5Fupdate-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-13)Example HTTP Requests

Update global function settings

This example updates the `worker_count` setting.

curl request

```sh
curl -X POST -d '{
  "deployment_status": false,
  "processing_status": false,
  "worker_count": 6
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

Update scoped function settings

This example updates the `worker_count` setting.

curl request

```sh
curl -X POST -d '{
  "deployment_status": false,
  "processing_status": false,
  "worker_count": 6
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Update undeployed global function settings

This example updates the `app_log_max_files` and `app_log_max_size` settings. The function is currently undeployed.

curl request

```sh
curl -X POST -d '{
  "deployment_status": false,
  "processing_status": false,
  "app_log_max_files": 5
  "app_log_max_size":10485760
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

Update undeployed scoped function settings

This example updates the `app_log_max_files` and `app_log_max_size` settings. The function is currently undeployed.

curl request

```sh
curl -X POST -d '{
  "deployment_status": false,
  "processing_status": false,
  "app_log_max_files": 5,
  "app_log_max_size": 10485760
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Update paused global function settings

This example updates the `timer_context_size` setting. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": false,
  "timer_context_size": 2048
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

Update paused scoped function settings

This example updates the `timer_context_size` setting. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": false,
  "timer_context_size": 2048
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Update paused global function settings and resume

This example updates the `worker_count` setting and resumes. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": true,
  "worker_count": 8
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

Update paused scoped function settings and resume

This example updates the `worker_count` setting and resumes. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": true,
  "worker_count": 8
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Enable Sync Gateway compatibility for a global function

Couchbase Server 7.6.4

This example sets `allow_sync_documents` to `false`, to enable compatibility with Sync Gateway. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": false,
  "allow_sync_documents": false
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

For details, see [Eventing — Server Compatibility](../../../sync-gateway/current/server-compatibility/server-compatibility-eventing.md).

Enable Sync Gateway compatibility for a scoped function

Couchbase Server 7.6.4

This example sets `allow_sync_documents` to `false`, to enable compatibility with Sync Gateway. The function is currently paused.

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": false,
  "allow_sync_documents": false
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

For details, see [Eventing — Server Compatibility](../../../sync-gateway/current/server-compatibility/server-compatibility-eventing.md).

Deploy an undeployed global function — deprecated

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": true
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"
```

Deprecated. See [Deploy a Function](#basic%5Fdeploy) for the preferred invocation.

Deploy an undeployed scoped function — deprecated

curl request

```sh
curl -X POST -d '{
  "deployment_status": true,
  "processing_status": true
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"
```

Deprecated. See [Deploy a Function](#basic%5Fdeploy) for the preferred invocation.

#### [](#adv%5Fstructure%5Fget)View Function Config

GET /api/v1/functions/{function}/config

##### [](#adv%5Fstructure%5Fget-description)Description

Export or return the configuration of the source keyspace and the eventing storage (metadata) keyspace for the specified function. The definition can be subsequently imported. However any changes to the function definition made to the file outside the UI are discouraged.

Produces

* application/json

##### [](#adv%5Fstructure%5Fget-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#adv%5Fstructure%5Fget-responses)Responses

| HTTP Code | Description                                                            | Schema                                |
| --------- | ---------------------------------------------------------------------- | ------------------------------------- |
| 200       | Returns an object showing the configuration of the specified function. | [Deployment Config](#depcfg%5Fschema) |
| 404       | Failure.                                                               |                                       |

##### [](#adv%5Fstructure%5Fget-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-14)Example HTTP Requests

View global function config

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config"
```

View scoped function config

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config?bucket=bulk&scope=data"
```

Save global function config to file

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config" \
  -o my_function.json
```

Save scoped function config to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config?bucket=bulk&scope=data" \
  -o my_function.json
```

#### [](#adv%5Fstructure%5Fupdate)Update Function Config

POST /api/v1/functions/{function}/config

##### [](#adv%5Fstructure%5Fupdate-description)Description

Import the configuration and alter the source keyspace and the eventing storage (metadata) keyspace for the specified function. You can only change these values if a function is in the undeployed state and the two keyspaces exist.

Consumes

* application/json

##### [](#adv%5Fstructure%5Fupdate-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

Body Parameter

| Name             | Description                                                       | Schema                                |
| ---------------- | ----------------------------------------------------------------- | ------------------------------------- |
| **Body**required | An object providing the configuration for the specified function. | [Deployment Config](#depcfg%5Fschema) |

##### [](#adv%5Fstructure%5Fupdate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Fstructure%5Fupdate-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-15)Example HTTP Requests

Update global function config

This example alters the source and eventing storage keyspaces.

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config" \
  -d '{
  "source_bucket": "bulk",
  "source_scope": "orders",
  "source_collection": "customer01",
  "metadata_bucket": "rr100",
  "metadata_scope": "eventing",
  "metadata_collection": "metadata"
}'
```

Update scoped function config

This example alters the source and eventing storage keyspaces.

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config?bucket=bulk&scope=data"\
  -d '{
  "source_bucket": "bulk",
  "source_scope": "orders",
  "source_collection": "customer01",
  "metadata_bucket": "rr100",
  "metadata_scope": "eventing",
  "metadata_collection": "metadata"
}'
```

Update global function config from file

This example alters the source and eventing storage keyspaces from a file.

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config" \
  -d @./my_function.json
```

Update scoped function config from file

This example alters the source and eventing storage keyspaces from a file.

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/config?bucket=bulk&scope=data" \
  -d @./my_function.json
```

#### [](#adv%5Ftext%5Fget)View Function Code

GET /api/v1/functions/{function}/appcode

##### [](#adv%5Ftext%5Fget-description)Description

Export only the JavaScript code for the specified function. Unlike [View a Function](#adv%5Ffunction%5Fview), the JavaScript is not escaped, and the code is runnable in other environments. The JavaScript code can be subsequently imported. However any changes to the function definition made to the file outside the UI are discouraged.

Produces

* application/json

##### [](#adv%5Ftext%5Fget-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#adv%5Ftext%5Fget-responses)Responses

| HTTP Code | Description                                                   | Schema |
| --------- | ------------------------------------------------------------- | ------ |
| 200       | Returns a string showing the code for the specified function. | String |
| 404       | Failure.                                                      |        |

##### [](#adv%5Ftext%5Fget-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-16)Example HTTP Requests

View global function code

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode"
```

View scoped function code

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode?bucket=bulk&scope=data"
```

Save global function code to file

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode" \
  -o my_function.json
```

Save scoped function code to file

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode?bucket=bulk&scope=data" \
  -o my_function.json
```

#### [](#adv%5Ftext%5Fupdate)Update Function Code

POST /api/v1/functions/{function}/appcode

##### [](#adv%5Ftext%5Fupdate-description)Description

Import only the JavaScript code for the specified function. Unlike [Create or Import Function](#adv%5Ffunction%5Fimport), the JavaScript is not escaped and could come from other environments. It's highly recommended that you use the flag `--data-binary` or `--upload-file` when importing your JavaScript appcode fragments to avoid potential encoding issues due to string escaping.

Consumes

* application/json

##### [](#adv%5Ftext%5Fupdate-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

Body Parameter

| Name             | Description                                             | Schema |
| ---------------- | ------------------------------------------------------- | ------ |
| **Body**required | A string providing the code for the specified function. | String |

##### [](#adv%5Ftext%5Fupdate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#adv%5Ftext%5Fupdate-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-17)Example HTTP Requests

Update global function code

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode" \
  --data-binary 'function OnUpdate(doc, meta) { log("id",meta.id); }'
```

Update scoped function code

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/appcode?bucket=bulk&scope=data" \
  --data-binary 'function OnUpdate(doc, meta) { log("id",meta.id); }'
```

Update global function code from file

This example uses the `--data-binary` option. Do not use `-d`.

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/import" \
  --data-binary @./my_function.json
```

Update scoped function code from file

This example uses the `--data-binary` option. Do not use `-d`.

curl request

```sh
curl -X POST "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/import?bucket=bulk&scope=data" \
  --data-binary @./my_function.json
```

Update global function code from file — alternative

This example uses the `--upload-file` option.

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/import" \
  --upload-file ./my_function.json
```

Update scoped function code from file — alternative

This example uses the `--upload-file` option.

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/import?bucket=bulk&scope=data" \
  --upload-file ./my_function.json
```

### [](#tag-GlobalConfig)Global Config

**Table of Contents**

[List Global Config](#config%5Fget)  
[Modify Global Config](#config%5Fupdate)

#### [](#config%5Fget)List Global Config

GET /api/v1/config

##### [](#config%5Fget-description)Description

Shows all global configuration settings. The `enable_debugger` and `ram_quota` settings can also be adjusted via the UI.

Produces

* application/json

##### [](#config%5Fget-responses)Responses

| HTTP Code | Description                                                  | Schema                       |
| --------- | ------------------------------------------------------------ | ---------------------------- |
| 200       | Returns an object showing the global configuration settings. | [Global Config](#UnivConfig) |
| 404       | Failure.                                                     |                              |

##### [](#config%5Fget-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-18)Example HTTP Requests

View global configuration

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/config"
```

#### [](#config%5Fupdate)Modify Global Config

POST /api/v1/config

##### [](#config%5Fupdate-description)Description

Modify global configuration settings. During an edit, settings provided are merged. Unspecified attributes retain their prior values. The response indicates whether the Eventing service must be restarted for the new changes to take effect.

Consumes

* application/json

> [!NOTE]
> Interbucket Recursion
> 
> If you need to turn off infinite recursion protection for Eventing functions, you can use an alternative REST API endpoint to enable interbucket recursion. For details, see [Troubleshooting and Best Practices](../eventing/troubleshooting-best-practices.md#cyclicredun).
> 
> Allowing interbucket recursion is highly discouraged unless you have an advanced use case and follow strict non-production coding and verification.

##### [](#config%5Fupdate-parameters)Parameters

Body Parameter

| Name             | Description                                            | Schema                       |
| ---------------- | ------------------------------------------------------ | ---------------------------- |
| **Body**required | An object providing the global configuration settings. | [Global Config](#UnivConfig) |

##### [](#config%5Fupdate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#config%5Fupdate-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-19)Example HTTP Requests

Alter RAM quota

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/config" \
  -d '{"ram_quota": 512}'
```

Enable debugger

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/config" \
  -d '{"enable_debugger": true}'
```

Set cursor limit

Couchbase Server 7.6.4

curl request

```sh
curl -X POST "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/config" \
  -d '{"cursor_limit": 10}'
```

Allow interbucket recursion

This example disables the safety checks that prevent basic infinite recursive Eventing functions.

curl request

```sh
curl -X POST -u $ADMIN:$PASSWORD "http://$HOST:8091/_p/event/api/v1/config" \
  -d '{"allow_interbucket_recursion": true}'
```

Disallow interbucket recursion

This example restores the default setting, which applies some sanity checks to prevent basic infinite recursive Eventing functions.

curl request

```sh
curl -X POST -u $ADMIN:$PASSWORD "http://$HOST:8091/_p/event/api/v1/config"
  -d '{"allow_interbucket_recursion": false}'
```

### [](#tag-List)List

**Table of Contents**

[List All Functions](#list%5Fall)  
[List Filtered Functions](#list%5Fquery)

#### [](#list%5Fall)List All Functions

GET /api/v1/list/functions

##### [](#list%5Fall-description)Description

Returns a list (array) of the names of all Eventing functions in the cluster. The returned list can also be filtered — see [List Filtered Functions](#list%5Fquery).

If this API is run as a non-Administrator the results are filtered via RBAC to include only the function scopes the user has access to.

##### [](#list%5Fall-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#list%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-20)Example HTTP Requests

List all functions

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/list/functions"
```

#### [](#list%5Fquery)List Filtered Functions

GET /api/v1/list/functions/query

##### [](#list%5Fquery-description)Description

Returns a list (array) of the names of all Eventing functions in the cluster. The returned list can be filtered by the following:

* Deployed status : in this case, paused is considered deployed.
* Source bucket: the listen to keyspace.
* Function type: whether the function modifies its own listen to keyspace.

If this API is run as a non-Administrator the results are filtered via RBAC to include only the function scopes the user has access to.

##### [](#list%5Fquery-parameters)Parameters

Query Parameters

| Name                       | Description                                                                                                                                                                                                                                                    | Schema  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **deployed**optional       | If true, returns the names of all deployed (or paused) functions. If false, returns the names of all undeployed functions.                                                                                                                                     | Boolean |
| **source\_bucket**optional | The name of a bucket. Returns the names of Eventing functions in the cluster that have a source keyspace under the specified bucket.                                                                                                                           | String  |
| **function\_type**optional | The function type. sbm: Returns the names of Eventing functions in the cluster that modify their own source keyspace. notsbm: Returns the names of Eventing functions in the cluster that do not modify their own source keyspace. **Values:** "sbm", "notsbm" | String  |

##### [](#list%5Fquery-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#list%5Fquery-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-21)Example HTTP Requests

List all deployed functions

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/list/functions/query?deployed=true"
```

If you had specified `deployed=false`, you would get all undeployed functions.

List all functions with source keyspace in a specific bucket

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/list/functions/query?source_bucket=bulk"
```

List all functions that do not modify their source keyspace

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/list/functions/query?function_type=notsbm"
```

### [](#tag-Logging)Logging

**Table of Contents**

[Get Log for a Function](#log%5Fview)

#### [](#log%5Fview)Get Log for a Function

GET /getAppLog

##### [](#log%5Fview-description)Description

Returns the most recent application log messages for the specified function.

##### [](#log%5Fview-parameters)Parameters

Query Parameters

| Name                  | Description                                                                                                                                                                                                                      | Schema  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **name**required      | The name of a function.                                                                                                                                                                                                          | String  |
| **bucket**optional    | For scoped functions only. The bucket to which the function belongs.                                                                                                                                                             | String  |
| **scope**optional     | For scoped functions only. The scope to which the function belongs.                                                                                                                                                              | String  |
| **aggregate**optional | If false, the API accesses a single Eventing node. If true, the API accesses all Eventing nodes. **Default:** false                                                                                                              | Boolean |
| **size**optional      | The approximate amount of logging information returned. When fetching from more than one Eventing node, the amount of logging information returned from each node is the size divided by the number of nodes. **Default:** 40960 | Integer |

##### [](#log%5Fview-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#log%5Fview-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-22)Example HTTP Requests

View global function log from a single node

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getAppLog?name=my_function"
```

View scoped function log from a single node

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getAppLog?name=my_function&bucket=bulk&scope=data"
```

View global function log from all Eventing nodes

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getAppLog?name=my_function&aggregate=true"
```

View scoped function log from all Eventing nodes

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getAppLog?name=my_function&aggregate=true&bucket=bulk&scope=data"
```

View size-limited global function log

This example fetches recent Application log info from all Eventing nodes, limited to 2048 bytes.

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getAppLog?name=my_function&aggregate=true&size=2048"
```

View size-limited scoped function log

This example fetches recent Application log info from all Eventing nodes, limited to 2048 bytes.

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getAppLog?name=my_function&aggregate=true&size=2048&bucket=bulk&scope=data"
```

### [](#tag-Statistics)Statistics

**Table of Contents**

[Get All Statistics](#stats%5Fall)  
[Get Execution Statistics](#stats%5Fexecution)  
[Get Failure Statistics](#stats%5Ffailure)  
[Get Latency Statistics](#stats%5Flatency)  
[Reset Statistics](#stats%5Freset)

#### [](#stats%5Fall)Get All Statistics

GET /api/v1/stats

##### [](#stats%5Fall-description)Description

Retrieve all statistics for the node.

If this API is run as a non-Administrator the results are filtered via RBAC to include only the function scopes the user has access to.

##### [](#stats%5Fall-parameters)Parameters

Query Parameters

| Name             | Description                                                                                                                                                                                                                                                                                                                                                    | Schema |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type**optional | Including this parameter returns the full statistics set, inclusive of events processing, events remaining, execution, failure, latency, worker PIDs and sequence processed. Omitting this parameter excludes dcp\_event\_backlog\_per\_vb, doc\_timer\_debug\_stats, latency\_stats, plasma\_stats, and seqs\_processed from the response. **Values:** "full" | String |

##### [](#stats%5Fall-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#stats%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-23)Example HTTP Requests

Get basic statistics

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/stats"
```

Get full statistics

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/stats?type=full"
```

#### [](#stats%5Fexecution)Get Execution Statistics

GET /getExecutionStats

##### [](#stats%5Fexecution-description)Description

Retrieve only execution statistics. This returns the subset of statistics for the node.

##### [](#stats%5Fexecution-parameters)Parameters

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **name**required   | The name of a function.                                              | String |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#stats%5Fexecution-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#stats%5Fexecution-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-24)Example HTTP Requests

View execution statistics for global function

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getExecutionStats?name=my_function"
```

View execution statistics for scoped function

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getExecutionStats?name=my_function&bucket=bulk&scope=data"
```

#### [](#stats%5Ffailure)Get Failure Statistics

GET /getFailureStats

##### [](#stats%5Ffailure-description)Description

Retrieve only failure statistics. This returns the subset of statistics for the node.

##### [](#stats%5Ffailure-parameters)Parameters

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **name**required   | The name of a function.                                              | String |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#stats%5Ffailure-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#stats%5Ffailure-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-25)Example HTTP Requests

View failure statistics for global function

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getFailureStats?name=my_function"
```

View failure statistics for scoped function

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getFailureStats?name=my_function&bucket=bulk&scope=data"
```

#### [](#stats%5Flatency)Get Latency Statistics

GET /getLatencyStats

##### [](#stats%5Flatency-description)Description

Retrieve only latency statistics. This returns the subset of statistics for the node.

##### [](#stats%5Flatency-parameters)Parameters

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **name**required   | The name of a function.                                              | String |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#stats%5Flatency-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#stats%5Flatency-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-26)Example HTTP Requests

View latency statistics for global function

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/getLatencyStats?name=my_function"
```

View latency statistics for scoped function

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/getLatencyStats?name=my_function&bucket=bulk&scope=data"
```

#### [](#stats%5Freset)Reset Statistics

GET /resetStatsCounters

##### [](#stats%5Freset-description)Description

Resets statistics for the specified function.

##### [](#stats%5Freset-parameters)Parameters

Query Parameters

| Name                | Description                                                          | Schema |
| ------------------- | -------------------------------------------------------------------- | ------ |
| **bucket**optional  | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional   | For scoped functions only. The scope to which the function belongs.  | String |
| **appName**required | The name of a function.                                              | String |

##### [](#stats%5Freset-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#stats%5Freset-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-27)Example HTTP Requests

Reset statistics for global function

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/resetStatsCounters?appName=my_function"
```

Reset statistics for scoped function

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/resetStatsCounters?appName=my_function&bucket=bulk&scope=data"
```

### [](#tag-Status)Status

**Table of Contents**

[View All Functions Status](#status%5Fall)  
[View Function Status](#status%5Ffunction)

#### [](#status%5Fall)View All Functions Status

GET /api/v1/status

##### [](#status%5Fall-description)Description

Returns a list (array) of all eventing functions, showing their corresponding `composite_status`. A function's status can have one of the following values: undeployed, deploying, deployed, undeploying, paused, and pausing. There's no value of resuming; when resuming a paused eventing function, the `composite_status` returns `deploying` until it reaches the deployed state.

If this API is run as a non-Administrator, the results are filtered via RBAC to include only the function scopes the user has access to.

##### [](#status%5Fall-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#status%5Fall-security)Security

| Type         | Name                           |
| ------------ | ------------------------------ |
| http (basic) | [Unscoped](#security-Unscoped) |

##### [](#example-http-requests-28)Example HTTP Requests

View status of all functions

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/status"
```

#### [](#status%5Ffunction)View Function Status

GET /api/v1/status/{function}

##### [](#status%5Ffunction-description)Description

Returns the specified function, showing its corresponding `composite_status`. It can have one of the following values: undeployed, deploying, deployed, undeploying, paused, and pausing. There's no value of resuming; when resuming a paused eventing function, the `composite_status` returns `deploying` until it reaches the deployed state.

##### [](#status%5Ffunction-parameters)Parameters

Path Parameters

| Name                 | Description             | Schema |
| -------------------- | ----------------------- | ------ |
| **function**required | The name of a function. | String |

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped functions only. The bucket to which the function belongs. | String |
| **scope**optional  | For scoped functions only. The scope to which the function belongs.  | String |

##### [](#status%5Ffunction-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success.    |        |
| 404       | Failure.    |        |

##### [](#status%5Ffunction-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scoped](#security-Scoped) |
| http (basic) | [Global](#security-Global) |

##### [](#example-http-requests-29)Example HTTP Requests

View global function status

curl request

```sh
curl -X GET "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/status/my_function"
```

View scoped function status

curl request

```sh
curl -X GET "http://$USER:$PASSWORD@$HOST:8096/api/v1/status/my_function?bucket=bulk&scope=data"
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Function Request](#AddFunction)  
[Functions Request](#AddFunctions)  
[Deployment Config](#depcfg%5Fschema)  
[Deployment Constants](#depcfg%5Fschema%5Fconstants%5Finner)  
[Deployment Keyspace](#depcfg%5Fschema%5Fbuckets%5Finner)  
[Deployment URL](#depcfg%5Fschema%5Fcurl%5Finner)  
[Function Definition](#handler%5Fschema)  
[Function Scope](#function%5Fscope%5Fschema)  
[Function Settings](#settings%5Fschema)  
[Global Config](#UnivConfig)

> [!NOTE]
> Changes to the Eventing function definition files made outside of this REST API or the interactive UI are only supported if you adhere to the Eventing schemas described here.

### [](#AddFunction)Function Request

 Composite Schema

| One of …​ |                                                                                                    | Schema                                         |
| --------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
|           | An object which defines a function.                                                                | [Function Definition](#handler%5Fschema)       |
| or        | An array containing a single function definition object. **Minimum items:** 1 **Maximum items:** 1 | [Function Definition](#handler%5Fschema) array |

### [](#AddFunctions)Functions Request

 Composite Schema

| One of …​ |                                                                                   | Schema                                         |
| --------- | --------------------------------------------------------------------------------- | ---------------------------------------------- |
|           | An object which defines a function.                                               | [Function Definition](#handler%5Fschema)       |
| or        | An array containing one or more function definition objects. **Minimum items:** 1 | [Function Definition](#handler%5Fschema) array |

### [](#depcfg%5Fschema)Deployment Config

 Object

| Property                         |                                                                       | Schema                                                             |
| -------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **buckets**optional              |                                                                       | [Deployment Keyspace](#depcfg%5Fschema%5Fbuckets%5Finner) array    |
| **curl**optional                 |                                                                       | [Deployment URL](#depcfg%5Fschema%5Fcurl%5Finner) array            |
| **metadata\_bucket**required     | bucket to store eventing checkpoints and timers **Minimum length:** 1 | String                                                             |
| **metadata\_scope**optional      | scope to store eventing checkpoints and timers                        | String                                                             |
| **metadata\_collection**optional | collection to store eventing checkpoints and timers                   | String                                                             |
| **source\_bucket**required       | bucket to listen to for document mutations **Minimum length:** 1      | String                                                             |
| **source\_scope**optional        | scope to listen to for document mutations                             | String                                                             |
| **source\_collection**optional   | collection to listen to for document mutations                        | String                                                             |
| **constants**optional            |                                                                       | [Deployment Constants](#depcfg%5Fschema%5Fconstants%5Finner) array |

#### Deployment Constants

 Object

| Property            |                                                                                                                                  | Schema |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **value**required   | alias name of the constant binding **Pattern:** /^\[a-zA-Z\_$\]\[a-zA-Z0-9\_$\]\*$/ **Minimum length:** 1 **Maximum length:** 64 | String |
| **literal**required | literal value bound to the alias name **Minimum length:** 1                                                                      | String |

#### Deployment Keyspace

 Object

| Property                     |                                                                                                                                                   | Schema |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **alias**required            | symbolic name used in code to refer to this binding **Pattern:** /^\[a-zA-Z\_$\]\[a-zA-Z0-9\_$\]\*$/ **Minimum length:** 1 **Maximum length:** 64 | String |
| **bucket\_name**required     | name of the bucket this binding maps to **Minimum length:** 1                                                                                     | String |
| **scope\_name**optional      | name of the scope this binding maps to                                                                                                            | String |
| **collection\_name**optional | name of the collection this binding maps to                                                                                                       | String |
| **access**required           | bucket access level (read or read+write) **Values:** "r", "rw"                                                                                    | String |

#### Deployment URL

 Object

| Property                               |                                                                                                                                                   | Schema    |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **hostname**required                   | full URL (including any path) that this binding connects **Pattern:** /^https?:\\/\\// **Minimum length:** 1                                      | URI (uri) |
| **value**required                      | symbolic name used in code to refer to this binding **Pattern:** /^\[a-zA-Z\_$\]\[a-zA-Z0-9\_$\]\*$/ **Minimum length:** 1 **Maximum length:** 64 | String    |
| **auth\_type**required                 | http authentication method to use with this endpoint **Values:** "no-auth", "basic", "bearer", "digest"                                           | String    |
| **username**optional                   | username for http auth methods that use it                                                                                                        | String    |
| **password**optional                   | password for http auth methods that use it                                                                                                        | String    |
| **bearer\_key**optional                | bearer key for bearer auth                                                                                                                        | String    |
| **allow\_cookies**required             | allow cookies on the session                                                                                                                      | Boolean   |
| **validate\_ssl\_certificate**required | validate remote server certificate using OS mechanisms                                                                                            | Boolean   |

### [](#handler%5Fschema)Function Definition

 Object

| Property                           |                                                                                                                                             | Schema                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **appcode**required                | handler code **Minimum length:** 1                                                                                                          | String                                       |
| **depcfg**required                 | deployment configuration                                                                                                                    | [Deployment Config](#depcfg%5Fschema)        |
| **version**required                | authoring tool. use 'external' if authored or edited outside eventing ui **Pattern:** /^evt-\[5-7\].\[0-9\]+.\[0-9\]+-\[0-9\]{4}-(ee\|ce)$/ | String                                       |
| **enforce\_schema**optional        | enforces stricter validation for all settings and configuration fields.                                                                     | Boolean                                      |
| **handleruuid**optional            | unique id of the the handler. generated by server **Minimum:** 0                                                                            | Integer                                      |
| **function\_instance\_id**optional | unique id of the deployment of the handler. generated by server                                                                             | String                                       |
| **appname**required                | **Pattern:** /^\[a-zA-Z0-9\]\[a-zA-Z0-9\_-\]\*$/ **Minimum length:** 1 **Maximum length:** 100                                              | String                                       |
| **settings**required               |                                                                                                                                             | [Function Settings](#settings%5Fschema)      |
| **function\_scope**optional        | function scope                                                                                                                              | [Function Scope](#function%5Fscope%5Fschema) |

#### Function Scope

 Object

| Property           |                                                        | Schema |
| ------------------ | ------------------------------------------------------ | ------ |
| **bucket**required | bucket to which function belongs **Minimum length:** 1 | String |
| **scope**required  | scope to which function belongs **Minimum length:** 1  | String |

### [](#settings%5Fschema)Function Settings

 Object

| Property                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Schema       |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **cpp\_worker\_thread\_count**optional     | number of threads each worker utilizes **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer      |
| **dcp\_stream\_boundary**optional          | indicates where to start dcp stream from (beginning of time, present point) 'from\_prior' is deprecated in 6.6.2 **Values:** "everything", "from\_now"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String       |
| **deployment\_status**optional             | indicates if the function is deployed. true=deployed, false=undeployed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean      |
| **description**optional                    | free form text for user to describe the handler. no functional role                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **execution\_timeout**optional             | maximum time the handler can run before it is forcefully terminated (in seconds) **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer      |
| **cursor\_checkpoint\_timeout**optional    | Couchbase Server 7.6.4 The maximum time the checkpoint writer can run before it's forcefully terminated (in seconds). **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer      |
| **on\_deploy\_timeout**optional            | maximum time the OnDeploy handler can run before it is terminated (in seconds) **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer      |
| **language\_compatibility**optional        | eventing language version this handler assumes in terms of syntax and behavior **Values:** "6.6.2", "6.0.0", "6.5.0", "7.2.0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **lcb\_inst\_capacity**optional            | maximum number of libcouchbase connections that may be opened and pooled **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer      |
| **lcb\_retry\_count**optional              | number of retries of retriable libcouchbase failures. 0 keeps trying till execution\_timeout **Minimum:** 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer      |
| **lcb\_timeout**optional                   | maximum time the lcb command is waited until completion before we terminate the request(in seconds) **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer      |
| **log\_level**optional                     | level of detail in system logging **Values:** "INFO", "ERROR", "WARNING", "DEBUG", "TRACE"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String       |
| **n1ql\_consistency**optional              | consistency level used by n1ql statements in the handler **Values:** "none", "request"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String       |
| **num\_timer\_partitions**optional         | number of timer shards. defaults to number of vbuckets **Values:** 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer      |
| **processing\_status**optional             | indicates if the function is running (i.e., not paused). true=running, false=paused                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean      |
| **sock\_batch\_size**optional              | batch size for messages from producer to consumer. normally, this must not be specified **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer      |
| **tick\_duration**optional                 | duration to log stats from this handler, in milliseconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer      |
| **timer\_context\_size**optional           | size limit of timer context object **Minimum:** 20 **Maximum:** 20971520                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer      |
| **user\_prefix**optional                   | key prefix for all data stored in metadata by this handler **Minimum length:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String       |
| **worker\_count**optional                  | number of worker processes handler utilizes on each eventing node **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **n1ql\_prepare\_all**optional             | automatically prepare all n1ql statements in the handler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **handler\_headers**optional               | code to automatically prepend to top of handler code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String array |
| **handler\_footers**optional               | code to automatically append to bottom of handler code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **enable\_applog\_rotation**optional       | enable rotating this handlers log() message files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean      |
| **app\_log\_dir**optional                  | directory to write content of log() message files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String       |
| **app\_log\_max\_size**optional            | rotate logs when file grows to this size in bytes approximately **Minimum:** 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer      |
| **app\_log\_max\_files**optional           | number of log() message files to retain when rotating **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer      |
| **checkpoint\_interval**optional           | number of seconds before writing a progress checkpoint **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer      |
| **bucket\_cache\_size**optional            | maximum size in bytes the bucket cache can grow to **Minimum:** 20971520                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer      |
| **bucket\_cache\_age**optional             | time in milliseconds after which a cached bucket object is considered stale **Minimum:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **curl\_max\_allowed\_resp\_size**optional | maximum allowable curl call response in 'MegaBytes'. Setting the value to 0 lifts the upper limit off. This parameters affects v8 engine stability since it defines the maximum amount of heap space acquired by a curl call                                                                                                                                                                                                                                                                                                                                                                                                             | Integer      |
| **allow\_transaction\_mutations**optional  | allow staged transaction mutations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean      |
| **allow\_sync\_documents**optional         | Couchbase Server 7.6.4 Specifies whether the function allows Sync Gateway mutations. By default, this setting is true, for compatibility with previous versions of Couchbase Server. When this setting is false, the specified function skips all internal Sync Gateway documents, whose IDs are prefixed with \_sync. This enables the function to work with Sync Gateway. You must ensure that none of the documents which contain your own working data have IDs which are prefixed with \_sync. (Internal Sync Gateway attachment documents, whose IDs are prefixed with \_sync:att, are still processed by the specified function.) | Boolean      |
| **cursor\_aware**optional                  | Couchbase Server 7.6.4 Specifies whether the function suppresses potential duplicate mutations caused by App Services or Sync Gateway book-keeping. Enabling this setting guarantees that the Eventing function will only trigger once for any given mutation received from App Services or Sync Gateway. Enabling this setting may have a noticeable effect on the performance of the Eventing function.                                                                                                                                                                                                                                | Boolean      |
| **high\_seq\_check\_interval**optional     | number of milliseconds before checking for high seq number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **max\_unacked\_bytes**optional            | max MBs to wait to send more bytes to c++ side                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer      |
| **max\_unacked\_count**optional            | max number of messages on c++ side                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer      |
| **message\_flush\_time**optional           | number of milliseconds before sending message to c++ side                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Integer      |
| **max\_parallel\_vb**optional              | number of parallel vb request per cpp thread                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer      |

### [](#UnivConfig)Global Config

 Object

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema  |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **ram\_quota**optional       | The memory allocation for the Eventing Service, per node. **Default:** 256 **Example:** 512                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer |
| **enable\_debugger**optional | Enables the Eventing service debugger. For details, see [Debugging and Diagnosability](/server/7.6/eventing/eventing-debugging-and-diagnosability.html). **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean |
| **cursor\_limit**optional    | Couchbase Server 7.6.4 The maximum number of cursor-aware Eventing functions that can coexist on a given source keyspace. (A cursor-aware Eventing function is one for which the cursor\_aware setting is true.) Increasing this setting enables more cursor-aware Eventing functions to register and listen to any given collection. Decreasing this setting prevents further cursor-aware Eventing functions from being registered on any given collection; however, it does not unregister already registered cursor-aware Eventing functions. **Default:** 5 **Minimum:** 1 **Maximum:** 20 | Integer |

## [](#security)Security

The Eventing REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Global)Global

Global functions with a function scope of `*.*` can only be made or managed by users with the Full Admin or Eventing Full Admin role. For global functions, you do not need to pass the `bucket` and `scope` query parameters to specify the function scope. The credentials must be an administrator username and password.

This is the default function scope for all functions after an upgrade from a prior version.

**Type:** http

### [](#security-Scoped)Scoped

For scoped functions, you must pass the `bucket` and `scope` query parameters to specify the function scope. The credentials are the username and password of any authorized user.

You can quote the REST call on the command line to escape the `&` and `?` characters.

**Type:** http

### [](#security-Unscoped)Unscoped

Unscoped REST API calls do not require you to specify the function scope. The action is fully determined by the username and password credentials passed to the REST call.

**Type:** http

For more information, see [Eventing Role-Based Access Control (RBAC)](../eventing/eventing-rbac.md).