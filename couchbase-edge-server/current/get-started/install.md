[View original HTML](/couchbase-edge-server/current/get-started/install.html)

> Install Couchbase Edge Server for use in your applications. 

## [](#installation-process)Installation Process

You can install Couchbase Edge Server on any of the [supported platforms](../product-notes/supported-platforms.md).

## [](#install-for-linux)Install for Linux

### [](#download)Download

Download the required edition of Couchbase Edge Server from the [downloads page](https://www.couchbase.com/downloads/?family=edge-server).

### [](#lbl-linux-install)Install

Follow the appropriate install option from the methods shown.

* Ubuntu
* Debian
* Fedora

Install Couchbase Edge Server with apt:

```bash
apt install couchbase-edge-server_1.0.0_amd64.deb
```

Install the debug symbols:

```bash
apt install couchbase-edge-server-dbgsym_1.0.0_amd64.deb
```

Install Couchbase Edge Server with the dpkg package manager:

```bash
dpkg install couchbase-edge-server_1.0.0_amd64.deb
```

Install the debug symbols:

```bash
dpkg install couchbase-edge-server-dbgsym_1.0.0_amd64.deb
```

Install Couchbase Edge Server with the DNF package manager:

```bash
dnf install couchbase-edge-server-1.0.0-x86_64.rpm
```

Install the debug symbols:

```bash
dnf install couchbase-edge-server-debuginfo-1.0.0-x86_64.rpm
```

## [](#install-for-macos)Install for macOS

### [](#download-2)Download

Download the required edition of Couchbase Edge Server from the [downloads page](https://www.couchbase.com/downloads/?family=edge-server).

### [](#lbl-macos-install)Install

Unzip the package into your preferred file location using the following command:

```bash
unzip -d couchbase-edge-server-1.0.0-macos.zip
```

## [](#run-and-verify-your-installation)Run and Verify Your Installation

On Linux operating systems, an instance of Couchbase Edge Server starts running automatically post-installation. For macOS, invoke the binary using the path to your configuration file as an argument.

To start Couchbase Edge Server you invoke the executable with the path to its configuration file.

You can define a configuration file yourself or use this minimal configuration file as a starting point. Make sure you define the `path` variable as the file-path to your database file.

|  | The configuration file is parsed as [JSON5 format](https://json5.org/). |
|  | ----------------------------------------------------------------------- |

```json
{
    "$schema": "https://packages.couchbase.com/couchbase-edge-server/config_schema.json",
    "databases": {
        "db": {
            "path":  "/path/to/db.cblite2",
            "create": true,                     // database file will be created if missing
            "enable_client_writes": true,       // database is writeable by PUT, POST, DELETE
            "enable_client_sync": true          // Clients can push and/or pull
        },
    },
    "enable_anonymous_users": true              // no HTTP auth needed
}
```

|  | Couchbase does not recommend setting enable\_adhoc\_queries to true for production environments. |
|  | ------------------------------------------------------------------------------------------------ |

After creating your configuration file, you can run Couchbase Edge Server by invoking it at its file location.

```bash
./couchbase-edge-server /path/to/config.json
```

You can verify the installation by following this example to confirm Couchbase Edge Server is listening to a given port:

Verification Example

In this example:

* `$BASEURL` is the protocol and host for Couchbase Edge Server, for example `<http://localhost>`.

Request

```bash
curl "$BASEURL:59840"
```

### [](#running-couchbase-edge-server-with-fedora)Running Couchbase Edge Server with Fedora

When running the Edge Server on Fedora, external connections may be blocked due to firewall settings. If you encounter a connection refused error when accessing the server, ensure that the firewall allows traffic on the configured port.

Allowing External Connections

To open the necessary port (e.g., 59840):

```bash
sudo firewall-cmd --zone=FedoraServer --add-port=59840/tcp --permanent sudo firewall-cmd --reload
```

If you’re using FedoraWorkstation, make sure to assign your network interface to that zone:

```bash
sudo nmcli connection modify "your-network-interface" connection.zone "FedoraWorkstation"
```

```bash
sudo systemctl restart NetworkManager
```

After updating the firewall settings, restart the server and test connectivity by confirming whether Couchbase Edge Server is listening to a given port:

In this example:

* `$BASEURL` is the protocol and host for Couchbase Edge Server, for example `<http://localhost>`.

Request

```bash
curl "$BASEURL:59840"
```

## [](#see-also)See Also

* [Getting Started](get-started-landing.md)
* [Prerequisites](prereqs.md)