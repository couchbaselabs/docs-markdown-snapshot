---
title: Who Am I?
description: An Operational Insights user can check their id (or
  <em>username</em>), domain, roles, and other details.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-whoami.adoc
  xref: xref:enterprise-analytics:reference:rest-whoami.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-whoami.html)

# Who Am I?

> An Operational Insights user can check their id (or _username_), domain, roles, and other details. 

## [](#http-method-and-uri)HTTP method and URI

GET /whoami

## [](#description)Description

The call returns an object that contains the following:

* `roles`. An object containing a key-value pair for every role assigned to the user. For example, `"role": "analytics_reader"`.
* `id`. The user's id (or _username_).
* `domain`. The user's _authentication domain_, which can be `local` or `external`. For information, see [Authentication](../manage/manage-security/manage-authentication.md).
* `name`. The user's full name, if specified.
* `password_change_date`. The date on which the user's password was last changed. For example, `"2020-02-13T04:08:31.000Z"`.

## [](#responses)Responses

If successful, the call returns `200 OK`, and an object that contains information about the user's id, domain, name, roles, and date of last password-change.

A malformed URI returns `404 Object Not Found`. Failure to authenticate returns `401 Unauthorized`.

## [](#example)Example

The following call returns information about a user whose id is `multiRoleAdmin`. Note that the output is piped to the [jq](https://jqlang.org/) command, to facilitate output-readability.

curl -X GET -u multiRoleAdmin:multiRoleAdminPassword \
http://10.143.194.101:8091/whoami | jq

If successful, the command returns output such as the following:

{
  "roles": [
    {
      "role": "analytics_reader"
    },
    {
      "role": "analytics_access"
    },
    {
      "role": "security_admin"
    }
  ],
  "id": "multiRoleAdmin",
  "domain": "local",
  "name": "John Smith",
  "password_change_date": "2020-02-13T04:08:31.000Z"
}

## [](#see-also)See Also

An overview of Operational Insights authentication, and of authentication _domains_, is provided in [Authentication](../manage/manage-security/manage-authentication.md).