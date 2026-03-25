---
title: Install Couchbase Lite for C
description: Installing Couchbase Lite for C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/c/pages/gs-install.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:c:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/c/gs-install.html)

# Install Couchbase Lite for C

> Description — _Installing Couchbase Lite for C_  

Steps in Getting Started

**Install**| [Build and Run](gs-build.md)

## [](#lbl-get-binaries)Download

_Couchbase Lite for C 3.1.10_ is available for all supported platforms — see: [Platform Availability](#lbl-platforms).

You can obtain the downloads here:

* _Android_, _iOS_ and _Windows_ — [Mobile & Edge](https://www.couchbase.com/downloads/#extend-with-mobile?family=couchbase-lite)
* _Linux_ and _macOS_ — [downloads table](#lbl-downloads)

The binary release download comprises a root directory (libcblite-community), which contains:

* For Linux, Windows, Android, and Mac OS:

  * `lib` — the core library binaries
  * `include` — the header files for _inclusion_
  * `bin` — the Couchbase Lite for C `.dll` files (Microsoft Windows-only) .
* For iOS, an xcframework.

> [!TIP]
> Debug Symbols
> 
> Debug symbol versions are available for all desktop variants of C (Windows, macOS, Debian, Ubuntu and Raspbian) - see: [downloads table](#lbl-downloads).
> 
> For Android and iOS the symbols are incorporated in the standard release package.

Installation:

[Install for Linux (APT)](#lbl-apt) | [Install for Linux (.deb)](#lbl-debt) | [Install for Windows](#lbl-windows) | [Install for macOS](#lbl-macos) | [Install for iOS](#lbl-ios) | [Install for Android](#lbl-android)

## [](#lbl-linux)Install for Linux

### [](#lbl-apt)Using APT

Using the Advanced Package Tool (apt) is the easiest way to install Couchbase Lite on Ubuntu and Debian platforms. Just download the meta package that _apt_ requires to automatically get and install Couchbase Lite, including any dependencies.

1. Download the meta package

  * curl
  * wget  
```bash  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
```  
```bash  
wget https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
```
2. Install the meta package

  * apt
  * dpkg  
```bash  
sudo apt install ./couchbase-release-1.0-noarch.deb  
```  
```bash  
sudo dpkg -i ./couchbase-release-1.0-noarch.deb  
```
3. Update the local package database  
```bash  
sudo apt update  
```
4. Install the required release package(s)

  * Enterprise
  * Community  
Runtime Only  
```bash  
sudo apt install libcblite  
```  
Development  
```bash  
sudo apt install libcblite-dev  
```  
Runtime Only  
```bash  
sudo apt install libcblite-community  
```  
Development  
```bash  
sudo apt install libcblite-dev-community  
```

That’s it. At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

### [](#lbl-deb)Using .deb Package

Use your package manager to install from a local `.deb` file.

1. Just `wget` the appropriate `.deb` package — see [downloads table](#lbl-downloads) for a package URL.
2. Install the package and its dependency, using `apt install`

  * For community version:  
  ```bash  
  sudo apt install ./libcblite-community  
  sudo apt install ./libcblite-dev-community  
  ```
  * For enterprise version:  
  ```bash  
  sudo apt install ./libcblite  
  sudo apt install ./libcblite-dev  
  ```
3. That’s it.  
You just need to pass the `-lcblite` command-line flag to the compiler when you build.

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

## [](#lbl-windows)Install for Windows

To install the Couchbase for C libraries on Windows from a downloaded release binary:

1. Download and extract the release package — see: [Mobile & Edge](https://www.couchbase.com/downloads/#extend-with-mobile?family=couchbase-lite)
2. From within the root directory, libcblite-community, deploy the `lib`, `include` and `bin` libraries to a location accessible to your compiler.
3. Within _Visual Studio_:

  1. **Create** a new C++ project  
  Be sure to select x64 for 64-bit builds
  2. Within **Project Properties** → **C++ directories** → **Library Directories**, **Add** `<path-to-deployed-directories>/lib`
  3. Within **Project Properties** → **C++ directories** → **Include Directories**, **Add** `<path-to-deployed-directories>/include`
  4. Within **Project Properties** → **Linker** → **Input** → **Additional Dependencies**, **Add** `cblite.lib`
4. **Copy** `<path-to-deployed-directories>/bin/cblite.dll` to your build location  
Couchbase Lite for C does not have any preferred installation path for the `.dll`. It is up to you to determine where best to place it so it is available during execution, though copying to a location on the system path is not recommended on Windows

## [](#lbl-macos)Install for macOS

Install with Homebrew

Simplified installation using Homebrew  

* `brew install libcblite`
* `brew install libcblite-community`

To install the Couchbase for C libraries on macOS from a downloaded release package:

1. Download and extract the release package here — [downloads table](#lbl-downloads).
2. Optionally …​ From within the root directory, libcblite-community, **Copy** the `include` and `lib` directories to `/usr/local/`
3. Within _Xcode_:

  1. **Create** a new project
  2. **Add** `<path/to>/include` to the project’s _Header Search Path_
  3. **Add** `<path/to>/lib` to the project’s _Library Search Path_
  4. **Drag** `libcblite-community.dylib` into your Xcode project. Then, within the dialog:

    1. **Select** _Create Directory References If Needed_
    2. **Check** the correct target is selected

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

## [](#lbl-ios)Install for iOS

To install the Couchbase for C libraries for iOS from a downloaded release package:

1. Download and extract the release package here — [Mobile & Edge](https://www.couchbase.com/downloads/#extend-with-mobile?family=couchbase-lite)
2. **Drag** `CouchbaseLite.xcframework` into your Xcode project, then within the dialog:

  1. **Select** _Create Directory References If Needed_
  2. **Check** the correct target is selected

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

If you encounter a build error — Include of non-modular header inside framework module — You may need to change the build setting `allow non-modular includes in framework module` to `Yes`.

## [](#lbl-android)Install for Android

This install assumes use of the _Android Studio_ IDE. In addition to the Couchbase Lite for C download you also require the following tool chain dependencies, all installable from within _Android Studio_ if necessary:

* CMake 3.18.1
* NDK 21.4.7075529
* Build tools 30.0.2

In this instance the release comprises a _ready to adapt_ application project.

1. **Download** and **Unpack** the binary release here — [Mobile & Edge](https://www.couchbase.com/downloads/#extend-with-mobile?family=couchbase-lite)
2. Within _Android Studio_, select and open the project folder (within the libcblite-community folder)
3. **Tools** **SDK Manager** **SDK Tools**
4. Check the above dependencies are installed, select any that are not  
**OK** to Continue

Once the install is finished, you can build and run this skeleton app.

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

## [](#lbl-platforms)Platform Availability

Couchbase Lite for C is available on the platforms shown in the tables below.

> [!IMPORTANT]
> Deprecation Notice
> 
> Support for the following will be deprecated in this release and will be removed in a future release:
> 
> * macOS
> 
>   * 11 - Big Sur
> * Apple OS X
> 
>   * v10.14 - Mojave
>   * v10.15 - Catalina
> * iOS - 10,11
> * CentOS - All versions
> * RedHat - 7/8
> * Ubuntu - 16, 18.04
> * Microsoft Server - 2016,2019
> * Debian - 9
> * Raspbian - 9
> 
> Please plan to migrate your apps to use an appropriate alternative version.

### [](#android)Android

| API | x86                        | x64                        | ARM 32                     | ARM 64                     |
| --- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 22+ | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#ios)iOS

| Version | x86                        | x64                        | ARM 32                     | ARM 64                     |
| ------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 10+     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#mac-os)Mac OS

| Version            | x64                        | ARM 64                     |
| ------------------ | -------------------------- | -------------------------- |
| OSX 10.14 (Mojave) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#linux)Linux

| Distro          | Version                    | x64                        | ARM 32                     | ARM 64                     |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Debian          | 9                          | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 10              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Raspberry Pi OS | 10                         |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| Raspbian        | 9                          |                            | ![yes](../_images/yes.png) |                            |
| Ubuntu          | 20.04                      | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#windows)Windows

|         | Version | x64                        |
| ------- | ------- | -------------------------- |
| Desktop | 10+     | ![yes](../_images/yes.png) |

## [](#lbl-downloads)Download Links

_Couchbase Lite for C_ is available for all [Supported Platforms](supported-os.md). You can obtain downloads for _Linux_ and _macOS_ from the links here in the downloads table.

### [](#release-3-1-10)Release 3.1.10

Available platforms are:

[MacOS](#macos-3-1-10) | [Windows](#windows-3-1-10) | [Debian](#debian-3-1-10) | [Ubuntu](#ubuntu-3-1-10) |

#### [](#macos-3-1-10)MacOS

Download link table

* Enterprise Edition
* Community Edition

| Platform | Download                                                                                                                                                     | SHA                                                                                                                                                                        | Debug Symbols                                                                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MacOS    | [couchbase-lite-c-enterprise-3.1.10-macos.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-macos.zip) | [couchbase-lite-c-enterprise-3.1.10-macos.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-macos.zip.sha256) | [couchbase-lite-c-enterprise-3.1.10-macos-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-macos-symbols.zip) |

| Platform | Download                                                                                                                                                   | SHA                                                                                                                                                                      | Debug Symbols                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MacOS    | [couchbase-lite-c-community-3.1.10-macos.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-macos.zip) | [couchbase-lite-c-community-3.1.10-macos.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-macos.zip.sha256) | [couchbase-lite-c-community-3.1.10-macos-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-macos-symbols.zip) |

#### [](#windows-3-1-10)Windows

Download link table

* Enterprise Edition
* Community Edition

| Platform | Download                                                                                                                                                                          | SHA | Debug Symbols                                                                                                                                                                                     |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | [couchbase-lite-c-enterprise-3.1.10-windows-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-windows-x86%5F64.zip) |     | [couchbase-lite-c-enterprise-3.1.10-windows-x86\_64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-windows-x86%5F64-symbols.zip) |

| Platform | Download                                                                                                                                                                        | SHA | Debug Symbols                                                                                                                                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | [couchbase-lite-c-community-3.1.10-windows-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-windows-x86%5F64.zip) |     | [couchbase-lite-c-community-3.1.10-windows-x86\_64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-windows-x86%5F64-symbols.zip) |

#### [](#debian-3-1-10)Debian

Download link table

* Enterprise Edition
* Community Edition

| Platform                                                                                                                                                                            | Download                                                                                                                                                                                          | SHA                                                                                                                                                                                                 | Debug Symbols                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Debian                                                                                                                                                                              | [couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz)                    | [couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz.sha256)        | [couchbase-lite-c-enterprise-3.1.10-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz)      | [couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz.sha256)      | [couchbase-lite-c-enterprise-3.1.10-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf-symbols.tar.gz)      |                                                                                                                                                                                                |
| [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64.tar.gz) | [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64.tar.gz.sha256) | [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64-symbols.tar.gz) |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Famd64.deb)              | [libcblite-enterprise\_3.1.10-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Famd64.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Famd64.deb)      | [libcblite-dev-enterprise\_3.1.10-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Famd64.deb.sha256)      |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Farm64.deb)              | [libcblite-enterprise\_3.1.10-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Farm64.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Farm64.deb)      | [libcblite-dev-enterprise\_3.1.10-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Farm64.deb.sha256)      |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Farmhf.deb)              | [libcblite-enterprise\_3.1.10-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian11%5Farmhf.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Farmhf.deb)      | [libcblite-dev-enterprise\_3.1.10-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian11%5Farmhf.deb.sha256)      |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Famd64.deb)              | [libcblite-enterprise\_3.1.10-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Famd64.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Famd64.deb)      | [libcblite-dev-enterprise\_3.1.10-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Famd64.deb.sha256)      |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Farm64.deb)              | [libcblite-enterprise\_3.1.10-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Farm64.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Farm64.deb)      | [libcblite-dev-enterprise\_3.1.10-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Farm64.deb.sha25)       |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Farmhf.deb)              | [libcblite-enterprise\_3.1.10-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian10%5Farmhf.deb.sha256)              |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Farmhf.deb)      | [libcblite-dev-enterprise\_3.1.10-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian10%5Farmhf.deb.sha256)      |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian9%5Famd64.deb)                | [libcblite-enterprise\_3.1.10-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian9%5Famd64.deb.sha256)                |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian9%5Famd64.deb)        | [libcblite-dev-enterprise\_3.1.10-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian9%5Famd64.deb.sha256)        |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian9%5Farmhf.deb)                | [libcblite-enterprise\_3.1.10-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-debian9%5Farmhf.deb.sha256)                |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian9%5Farmhf.deb)        | [libcblite-dev-enterprise\_3.1.10-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-debian9%5Farmhf.deb.sha256)        |                                                                                                                                                                                                     |                                                                                                                                                                                                |

| Platform                                                                                                                                                                          | Download                                                                                                                                                                                        | SHA                                                                                                                                                                                               | Debug Symbols                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Debian                                                                                                                                                                            | [couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz)                    | [couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz.sha256)        | [couchbase-lite-c-community-3.1.10-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz)      | [couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz.sha256)      | [couchbase-lite-c-community-3.1.10-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf-symbols.tar.gz)      |                                                                                                                                                                                              |
| [couchbase-lite-c-community-3.1.10-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64.tar.gz) | [couchbase-lite-c-community-3.1.10-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64.tar.gz.sha256) | [couchbase-lite-c-community-3.1.10-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64-symbols.tar.gz) |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Famd64.deb)              | [libcblite-community\_3.1.10-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Famd64.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Famd64.deb)      | [libcblite-dev-community\_3.1.10-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Famd64.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Farm64.deb)              | [libcblite-community\_3.1.10-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Farm64.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Farm64.deb)      | [libcblite-dev-community\_3.1.10-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Farm64.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Farmhf.deb)              | [libcblite-community\_3.1.10-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian11%5Farmhf.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Farmhf.deb)      | [libcblite-dev-community\_3.1.10-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian11%5Farmhf.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Famd64.deb)              | [libcblite-community\_3.1.10-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Famd64.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Famd64.deb)      | [libcblite-dev-community\_3.1.10-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Famd64.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Farm64.deb)              | [libcblite-community\_3.1.10-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Farm64.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Farm64.deb)      | [libcblite-dev-community\_3.1.10-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Farm64.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Farmhf.deb)              | [libcblite-community\_3.1.10-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian10%5Farmhf.deb.sha256)              |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Farmhf.deb)      | [libcblite-dev-community\_3.1.10-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian10%5Farmhf.deb.sha256)      |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian9%5Famd64.deb)                | [libcblite-community\_3.1.10-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian9%5Famd64.deb.sha256)                |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian9%5Famd64.deb)        | [libcblite-dev-community\_3.1.10-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian9%5Famd64.deb.sha256)        |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian9%5Farmhf.deb)                | [libcblite-community\_3.1.10-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-debian9%5Farmhf.deb.sha256)                |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian9%5Farmhf.deb)        | [libcblite-dev-community\_3.1.10-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-debian9%5Farmhf.deb.sha256)        |                                                                                                                                                                                                   |                                                                                                                                                                                              |

#### [](#ubuntu-3-1-10)Ubuntu

Download link table

* Enterprise Edition
* Community Edition

| Platform                                                                                                                                                                             | Download                                                                                                                                                                                           | SHA                                                                                                                                                                                                 | Debug Symbols                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu                                                                                                                                                                               | [couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz)                     | [couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64.tar.gz.sha256)        | [couchbase-lite-c-enterprise-3.1.10-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz)       | [couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf.tar.gz.sha256)       | [couchbase-lite-c-enterprise-3.1.10-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-armhf-symbols.tar.gz)      |                                                                                                                                                                                                |
| [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64.tar.gz)  | [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64.tar.gz.sha256)  | [couchbase-lite-c-enterprise-3.1.10-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-enterprise-3.1.10-linux-x86%5F64-symbols.tar.gz) |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Famd64.deb)         | [libcblite-enterprise\_3.1.10-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Famd64.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Famd64.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Farm64.deb)         | [libcblite-enterprise\_3.1.10-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Farm64.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Farm64.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Farmhf.deb)         | [libcblite-enterprise\_3.1.10-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu22.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Farmhf.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu22.04%5Farmhf.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Famd64.deb)         | [libcblite-enterprise\_3.1.10-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Famd64.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Famd64.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Farm64.deb)         | [libcblite-enterprise\_3.1.10-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Farm64.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Farm64.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-enterprise\_3.1.10-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Farmhf.deb)         | [libcblite-enterprise\_3.1.10-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-enterprise%5F3.1.10-ubuntu20.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                     |                                                                                                                                                                                                |
| [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Farmhf.deb) | [libcblite-dev-enterprise\_3.1.10-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-enterprise%5F3.1.10-ubuntu20.04%5Farmhf.deb.sha256) |                                                                                                                                                                                                     |                                                                                                                                                                                                |

| Platform                                                                                                                                                                           | Download                                                                                                                                                                                         | SHA                                                                                                                                                                                               | Debug Symbols                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu                                                                                                                                                                             | [couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz)                     | [couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64.tar.gz.sha256)        | [couchbase-lite-c-community-3.1.10-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz)       | [couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf.tar.gz.sha256)       | [couchbase-lite-c-community-3.1.10-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-armhf-symbols.tar.gz)      |                                                                                                                                                                                              |
| [couchbase-lite-c-community-3.1.10-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64.tar.gz)  | [couchbase-lite-c-community-3.1.10-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64.tar.gz.sha256)  | [couchbase-lite-c-community-3.1.10-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/couchbase-lite-c-community-3.1.10-linux-x86%5F64-symbols.tar.gz) |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Famd64.deb)         | [libcblite-community\_3.1.10-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Famd64.deb) | [libcblite-dev-community\_3.1.10-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Famd64.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Farm64.deb)         | [libcblite-community\_3.1.10-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Farm64.deb) | [libcblite-dev-community\_3.1.10-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Farm64.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Farmhf.deb)         | [libcblite-community\_3.1.10-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu22.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Farmhf.deb) | [libcblite-dev-community\_3.1.10-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu22.04%5Farmhf.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Famd64.deb)         | [libcblite-community\_3.1.10-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Famd64.deb) | [libcblite-dev-community\_3.1.10-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Famd64.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Farm64.deb)         | [libcblite-community\_3.1.10-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Farm64.deb) | [libcblite-dev-community\_3.1.10-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Farm64.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-community\_3.1.10-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Farmhf.deb)         | [libcblite-community\_3.1.10-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-community%5F3.1.10-ubuntu20.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                   |                                                                                                                                                                                              |
| [libcblite-dev-community\_3.1.10-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Farmhf.deb) | [libcblite-dev-community\_3.1.10-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.1.10/libcblite-dev-community%5F3.1.10-ubuntu20.04%5Farmhf.deb.sha256) |                                                                                                                                                                                                   |                                                                                                                                                                                              |

#### [](#raspbian-3-1-10)Raspbian

Please use the [Debian .deb download](#debian-3-1-10) choosing the appropriate version (`debian9` or `debian10`) and architecture.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)