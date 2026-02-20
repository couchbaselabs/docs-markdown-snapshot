---
title: Authorization API
description: Authorization by means of Role-Based Access Control can be manage
  with the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-authorization.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-authorization.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-authorization.html)

# Authorization API

> Authorization by means of Role-Based Access Control can be manage with the REST API. 

## [](#apis-in-this-section)APIs in this Section

_Role-Based Access Control_ can be managed by means of the REST API. The endpoints are described in this section, and are listed in the table below.

| HTTP Method | URI                                               | Documented at                                                                    |
| ----------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| GET         | /settings/rbac/roles                              | [List Roles](rbac.md#list-roles)                                                 |
| GET         | /settings/rbac/users                              | [List Current Users and Their Roles](rbac.md#list-current-users-and-their-roles) |
| POST        | /pools/default/checkPermissions                   | [Check Permissions](rbac.md#check-permissions)                                   |
| GET         | /settings/rbac/groups                             | [List Currently Defined Groups](rbac.md#list-currently-defined-groups)           |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PATCH       | /settings/rbac/users/local/<existing-username>    | [Create a Local User](rbac.md#create-a-local-user-and-assign-roles)              |
| PUT         | /settings/rbac/users/local/<new-username>         | [Create an External User](rbac.md#create-an-external-user-and-assign-roles)      |
| PUT         | /settings/rbac/groups/<new-groupname>             | [Create a Group](rbac.md#create-a-group-and-assign-it-roles)                     |
| DELETE      | /settings/rbac/users/local/<local-username>       | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/users/external/<external-username> | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |
| DELETE      | /settings/rbac/groups/<groupname>                 | [Delete Users and Groups](rbac.md#delete-users-and-groups)                       |