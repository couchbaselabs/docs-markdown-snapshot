---
title: Start Using the Ottoman ODM
description: Installing the Ottoman ODM &amp; a Hello World program.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/hello-world/pages/start-using-ottoman.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.3@nodejs-sdk:hello-world:start-using-ottoman.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/hello-world/start-using-ottoman.html)

# Start Using the Ottoman ODM

> Installing the Ottoman ODM & a Hello World program. 

Ottoman is an open-source Object Document Mapper(ODM) library, built for Node.js and Couchbase, that aspires to give developers an even better experience when building modern applications.

Ottoman ODM adds an abstraction layer over Couchbase Node.js SDK and significantly reduces the level of boilerplate needed during application development. It provides features such as the ability to define document schemas and perform validations on your data in a NoSQL landscape — which is inherently schema-less or schema-flexible by nature.

> [!NOTE]
> Whether you are building your application with JavaScript or TypeScript, Ottoman will work seamlessly with either.

Ottoman fully supports the [Scopes and Collections](../../../server/7.6/learn/data/scopes-and-collections.md) features introduced in Couchbase Sever 7.0\. We recomend familiarizing yourself with these concepts before proceeding with this guide.

For a full feature comparison between Ottoman ODM and the Couchbase Node.js SDK you can read more [here](https://ottomanjs.com/docs/advanced/sdk-comparison).

## [](#node-js-sdk-4-x-support)Node.js SDK 4.x Support

[Ottoman.js](https://ottomanjs.com/#introduction) version 2.3.0 and above are compatible with Couchbase Node.js SDK 4.2.0 and above. Earlier versions of Ottoman ODM 2.x are only compatible with the 3.2 Node.js SDK.

## [](#additional-resources)Additional Resources

To learn more about Ottoman ODM you can head over to the official [Ottoman](https://ottomanjs.com/) page. You can also find more in-depth information on some of the topics we touched on:

* [Schemas](https://ottomanjs.com/docs/basic/schema)
* [Models](https://ottomanjs.com/docs/basic/model)
* [Documents](https://ottomanjs.com/docs/basic/document)
* [Query Builder](https://ottomanjs.com/docs/basic/query-builder)

If you are evaluating whether to use Ottoman in your next project, the FAQs [here](https://ottomanjs.com/docs/faq) should also answer some questions.

Links to each release are to be found in the [individual release notes](../project-docs/ottoman-release-notes.md).

Couchbase welcomes community contributions to the Ottoman ODM. The Ottoman ODM source code is available on [GitHub](https://github.com/couchbaselabs/node-ottoman).