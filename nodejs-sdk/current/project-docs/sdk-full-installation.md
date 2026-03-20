---
title: Full Installation
description: Installation instructions for the Couchbase Node.js Client.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:nodejs-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Node.js Client. 

The Couchbase Node.js Client will run on any [supported LTS version of Node.js](https://github.com/nodejs/Release) — currently, 16.x and 18.x.

## [](#installing-the-sdk)Installing the SDK

The Couchbase Node.js Client will run on any [supported LTS version of Node.js](https://nodejs.org/en/download/).

```console
$ npm install couchbase --save
```

Note: This will download the latest Couchbase Node.js SDK, and add a dependency to your `package.json`.

Information on new features, fixes, known issues, as well as information on how to install older release versions is in the [release notes](sdk-release-notes.md).

### [](#typescript-support)TypeScript Support

> [!NOTE]
> Follow this section only if you intend to use `TypeScript` instead of `JavaScript`.

Since release 3.2, the Node.js SDK has added full support for the [TypeScript](https://www.typescriptlang.org/) programming language.

```console
$ npm install -g typescript ts-node
```

This will install TypeScript globally on your machine and allow you to run commands with the `tsc` cli. You will have noticed that we also install [ts-node](https://typestrong.org/ts-node/) which is a handy execution utility that will help us run the example later on.

Run `tsc --init` in your project directory to generate a `tsconfig.json` file. This will set you up with some initial configurations, which should suffice for our purposes.

Should you wish to make changes in future you can simply edit the file:

```json
{
  "compilerOptions": {
   "disableReferencedProjectLoad": true,             
    "target": "es5",                                   
    "module": "commonjs",                                
    "esModuleInterop": true,                             
    "forceConsistentCasingInFileNames": true,            
    "strict": true,                                     
    "skipLibCheck": true                                 
  }
}
```

Note that the example above does not include the generated comments for readability.