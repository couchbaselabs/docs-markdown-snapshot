---
title: Build from Source
description: Build and run the Couchbase MCP Server from source, including
  Docker image builds.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/reference/pages/build-from-source.adoc
  xref: xref:mcp-server:reference:build-from-source.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/reference/build-from-source.html)

# Build from Source

> Build and run the Couchbase MCP Server from source, including Docker image builds. 

This page provides a step-by-step guide to building the Couchbase MCP Server from source when you want to run it locally, test the latest changes, or extend it directly from the GitHub repository. It covers cloning the repository, configuring your MCP client, and optionally building a Docker image from source.

## [](#prerequisites)Prerequisites

* **Python 3.10—3.14** installed — the server supports [Python versions](https://devguide.python.org/versions/#supported-versions) in security or bug-fix (maintenance) status; [End-of-Life](https://endoflife.date/python) versions are not supported.
* **[uv](https://docs.astral.sh/uv/)** installed
* **Git** installed

## [](#clone-the-repository)Clone the Repository

```bash
git clone https://github.com/couchbase/mcp-server-couchbase.git
cd mcp-server-couchbase
```

## [](#running-the-source-code-directly)Running the Source Code Directly

You can run the MCP server directly from the source using uv.

### [](#source-mcp-client-configuration)Source: MCP Client Configuration

When configuring an MCP client, use this command format:

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/cloned/repo/mcp-server-couchbase/",
        "run",
        "src/mcp_server.py"
      ],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-connection-string",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password"
      }
    }
  }
}
```

> [!NOTE]
> `path/to/cloned/repo/mcp-server-couchbase/` should be the absolute path to the cloned repository on your local machine. Do not forget the trailing slash.

> [!TIP]
> If you have other MCP servers configured, add the `couchbase` entry to the existing `mcpServers` object.

## [](#dockerize-from-source)Dockerize from Source

You can also build and run the server as a Docker container from the cloned repository.

### [](#build-the-image)Build the Image

```bash
docker build -t mcp/couchbase-src .
```

To include build metadata (git commit hash and build timestamp):

```bash
docker build --build-arg GIT_COMMIT_HASH=$(git rev-parse HEAD) \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  -t mcp/couchbase-src .
```

Or use the provided [build script](https://github.com/couchbase/mcp-server-couchbase/blob/main/build.sh):

#### [](#build-with-default-image-name-mcpcouchbase-src)Build with default image name (`mcp/couchbase-src`)

```bash
./build.sh
```

#### [](#build-with-custom-image-name)Build with custom image name

```bash
./build.sh my-custom/image-name
```

The script does the following:

* Accepts an optional image name parameter (defaults to `mcp/couchbase-src`)
* Generates git commit hash and build timestamp
* Creates multiple useful tags (`latest`, `<short-commit>`)
* Shows build information and results
* Uses the same arguments as CI/CD builds

### [](#verify-image-labels)Verify Image Labels

```bash
# View git commit hash
docker inspect --format='{{index .Config.Labels "org.opencontainers.image.revision"}}' mcp/couchbase-src:latest

# View all metadata labels
docker inspect --format='{{json .Config.Labels}}' mcp/couchbase-src:latest
```

### [](#docker-mcp-client-configuration)Docker: MCP Client Configuration

Once the image is built, configure your MCP client to use it:

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CB_CONNECTION_STRING=couchbases://your-connection-string",
        "-e", "CB_USERNAME=your-username",
        "-e", "CB_PASSWORD=your-password",
        "mcp/couchbase-src"
      ]
    }
  }
}
```

## [](#next-steps)Next Steps

See the [Quick Start](../get-started/quickstart.md) for client-specific configuration instructions.