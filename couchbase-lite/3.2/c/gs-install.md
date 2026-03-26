---
title: Install Couchbase Lite for C
description: Installing Couchbase Lite for C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/c/pages/gs-install.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.2@couchbase-lite:c:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/c/gs-install.html)

# Install Couchbase Lite for C

> Description — _Installing Couchbase Lite for C_  

Steps in Getting Started

**Install**| [Build and Run](gs-build.md)

## [](#lbl-get-binaries)Download

Couchbase Lite for C 3.2.4 is available for all supported platforms — see: [Platform Availability](#lbl-platforms).

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

### [](#downloading-vector-search)Downloading Vector Search

You can obtain the download for the Vector Search extension here:

* _Vector Search Extension_ — [Download Vector Search](#vs-release-1-0-1)

> [!IMPORTANT]
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

Installation:

[Install for Linux (APT)](#lbl-apt) | [Install for Linux (.deb)](#lbl-debt) | [Install for Windows](#lbl-windows) | [Install for macOS](#lbl-macos) | [Install for iOS](#lbl-ios) | [Install for Android](#lbl-android)

## [](#lbl-linux)Install for Linux

### [](#lbl-apt)Using APT

Using the Advanced Package Tool (apt) is the easiest way to install Couchbase Lite on Ubuntu and Debian platforms. Just download the meta package that _apt_ requires to automatically get and install Couchbase Lite, including any dependencies.

1. Download the meta package

  * curl
  * wget  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
wget https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb
2. Install the meta package

  * apt
  * dpkg  
sudo apt install ./couchbase-release-1.0-noarch.deb  
sudo dpkg -i ./couchbase-release-1.0-noarch.deb
3. Update the local package database  
sudo apt update
4. Install the required release package(s)

  * Enterprise
  * Community  
Runtime Only  
sudo apt install libcblite  
Development  
sudo apt install libcblite-dev  
Runtime Only  
sudo apt install libcblite-community  
Development  
sudo apt install libcblite-dev-community

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

### [](#lbl-deb)Using .deb Package

Use your package manager to install from a local `.deb` file.

1. Just `wget` the appropriate `.deb` package — see [downloads table](#lbl-downloads) for a package URL.
2. Install the package and its dependency, using `apt install`

  * For community version:  
  sudo apt install ./libcblite-community  
  sudo apt install ./libcblite-dev-community
  * For enterprise version:  
  sudo apt install ./libcblite  
  sudo apt install ./libcblite-dev
3. From here, you need to pass the `-lcblite` command-line flag to the compiler when you build.

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

### [](#install-vector-search-for-linux)Install Vector Search for Linux

Before you can use Vector Search, you must [download and install the Vector Search library](#vs-release-1-0-1) to the location in your project where the library can be accessed and loaded at run time. The Vector Search extension for the C platform ships with supported prebuilt libraries containing the required dependencies.

You need to set the `LD_LIBRARIES_PATH` to the extension location instead of installing the libraries yourself.

In the code, before opening the database and using the vector search extension, you must call the CBL\_SetExtensionPath function shown below to set the path to the installed location of the vector search library.

```c
CBLError error {};
if (!CBL_EnableVectorSearch(FLStr("/path/to/extension_dir"), &error)) {
    throw std::domain_error("Invalid / Not Found Extension Library");
}
```

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

### [](#install-vector-search-for-windows)Install Vector Search for Windows

To use the Vector Search extension:

1. Download and extract the [Vector Search extension](#vs-release-1-0-1).
2. Put the library in your development environment.

In the code, before opening the database and using the vector search extension, you must call the CBL\_SetExtensionPath function shown below to set the path to the installed location of the vector search library.

```c
CBLError error {};
if (!CBL_EnableVectorSearch(FLStr("/path/to/extension_dir"), &error)) {
    throw std::domain_error("Invalid / Not Found Extension Library");
}
```

> [!NOTE]
> Couchbase Lite Vector Search does not have any preferred installation path for the `.dll`. It is up to you to determine where best to place it so it is available during execution.

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
  2. **Add** `<path/to>/include` to the project's _Header Search Path_
  3. **Add** `<path/to>/lib` to the project's _Library Search Path_
  4. **Drag** `libcblite-community.dylib` into your Xcode project. Then, within the dialog:

    1. **Select** _Create Directory References If Needed_
    2. **Check** the correct target is selected

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

### [](#install-vector-search-for-macos)Install Vector Search for macOS

Before you can use Vector Search, you must [download and install the Vector Search library](#vs-release-1-0-1) to the location in your project where the library can be accessed and loaded at run time. The Vector Search extension for the C platform ships with supported prebuilt libraries containing the required dependencies.

In the code, before opening the database and using the vector search extension, you must call the CBL\_SetExtensionPath function shown below to set the path to the installed location of the vector search library.

```c
CBLError error {};
if (!CBL_EnableVectorSearch(FLStr("/path/to/extension_dir"), &error)) {
    throw std::domain_error("Invalid / Not Found Extension Library");
}
```

## [](#lbl-ios)Install for iOS

To install the Couchbase for C libraries for iOS from a downloaded release package:

1. Download and extract the release package here — [Mobile & Edge](https://www.couchbase.com/downloads/#extend-with-mobile?family=couchbase-lite)
2. **Drag** `CouchbaseLite.xcframework` into your Xcode project, then within the dialog:

  1. **Select** _Create Directory References If Needed_
  2. **Check** the correct target is selected

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

If you encounter a build error — Include of non-modular header inside framework module — You may need to change the build setting `allow non-modular includes in framework module` to `Yes`.

### [](#install-vector-search-for-ios)Install Vector Search for iOS

1. Download and extract the [Vector Search extension](#vs-release-1-0-1) into your XCode project location.
2. Select your target settings in XCode and drag **CouchbaseLiteVectorSearch.xcframework** from your Finder to the **Frameworks, Libraries, and Embedded Content** section.
3. Import the xcframework and start using it in your project.

* Objective-C
* Swift

```objective-c
[NSBundle bundleWithIdentifier: "com.couchbase.vectorSearchExtension"].bundlePath
```

```swift
Bundle(identifier: "com.couchbase.vectorSearchExtension").bundlePath
```

You can then set the extension path with the snippet below.

```c
CBLError error {};
if (!CBL_EnableVectorSearch(FLStr("/path/to/extension_dir"), &error)) {
    throw std::domain_error("Invalid / Not Found Extension Library");
}
```

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

### [](#install-vector-search-for-android)Install Vector Search for Android

To use Vector Search in your Android applications, follow the steps below:

1. Download and extract the [Vector Search extension](#vs-release-1-0-1) into your project location.
2. The package must be installed to the location in your project where the library can be accessed and loaded while the executable is running.

  1. The Vector Search download for CBL-C only contains the Vector Search libraries needed to include in your app.
  2. Steps to include the prebuilt native library can be found [here](https://developer.android.com/studio/projects/gradle-external-native-builds).
3. Create a Android app project in Android Studio
4. The location of the native library can be found using the following snippet:

* Default Packaging
* Legacy Packaging

```java
String getExtensionPath(Context context) {
  String packagePath = context.getPackageResourcePath();
  if (packagePath == null) { return null; }

  String arch = getArch();
  if (arch == null) { return null; }

  return packagePath + "!/lib/" + arch; // "!" is important for locating non-extracted library.
}

String getArch() {
  final List<String> abis = Arrays.asList(Build.SUPPORTED_ABIS);
  if (abis.contains()) { return "arm64-v8a"; }
  if (abis.contains("x86_64")) { return "x86_64"; }
  return null;
}
```

```java
static String getExtensionPath() {
  return context.getApplicationInfo().nativeLibraryDir
}
```

In the code, before opening the database and using the vector search extension, you must call the CBL\_SetExtensionPath function shown below to set the path to the installed location of the vector search library.

```c
CBLError error {};
if (!CBL_EnableVectorSearch(FLStr("/path/to/extension_dir"), &error)) {
    throw std::domain_error("Invalid / Not Found Extension Library");
}
```

At this point, you are ready to start building the [Getting Started](gs-build.md) app, or doing your own thing with _Couchbase Lite for C_

## [](#lbl-platforms)Platform Availability

Couchbase Lite for C is available on the platforms shown in the tables below.

> [!IMPORTANT]
> Deprecation Notice
> 
> Support for the following will be deprecated in this release and will be removed in a future release:
> 
> * macOS 12 (Monterey)
> * Ubuntu - 20.04 LTS
> * Raspbian - 9
> * Debian 9, 10
> 
> Please plan to migrate your apps to use an appropriate alternative version.

### [](#android)Android

| API | x86                        | x64                        | ARM 32                     | ARM 64                     |
| --- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 22+ | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#ios)iOS

| Version | x86                        | x64                        | ARM 32                     | ARM 64                     |
| ------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 12+     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#macos)macOS

| Version             | x64                        | ARM 64                     |
| ------------------- | -------------------------- | -------------------------- |
| macOS 14 (Sonoma)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| macOS 13 (Ventura)  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| macOS 12 (Monterey) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#linux)Linux

| Distro          | Version                    | x64                        | ARM 32                     | ARM 64                     |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Debian          | 9                          | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 10 (Buster)     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 11 (Bullseye)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 12 (Bookworm)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Raspberry Pi OS | 10                         |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| Raspbian        | 9                          |                            | ![yes](../_images/yes.png) |                            |
| Ubuntu          | 20.04 LTS                  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 22.04 LTS       | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |

### [](#embedded-linux)Embedded Linux

| Distro          | Version                    | x64                        | ARM 32                     | ARM 64                     |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Debian          | 9                          | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 10 (Buster)     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 11 (Bullseye)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 12 (Bookworm)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Raspberry Pi OS | 10                         |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| Raspbian        | 9                          |                            | ![yes](../_images/yes.png) |                            |
| Ubuntu          | 20.04 LTS                  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 22.04 LTS       | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |

### [](#windows)Windows

|         | Version | x64                        |
| ------- | ------- | -------------------------- |
| Desktop | 10+     | ![yes](../_images/yes.png) |

## [](#lbl-downloads)Download Links

### [](#release-3-2-4)Couchbase Lite Release 3.2.4

_Couchbase Lite for C_ is available for all [Supported Platforms](supported-os.md). You can obtain downloads for _Linux_ and _macOS_ from the links here in the downloads table. Ensure you select the correct package for your application's compiler and architecture.

Alternatively, check the [install](gs-install.md)page for instructions on how to get the software using a package manager.

Available platforms are:

[MacOS](#macos-3-2-4) | [Windows](#windows-3-2-4) | [Debian](#debian-3-2-4) | [Ubuntu](#ubuntu-3-2-4) |

#### [](#macos-3-2-4)MacOS

Example 1\. Download link table

Enterprise Edition

| Platform | Download                                                                                                                                                  | SHA                                                                                                                                                                     | Debug Symbols                                                                                                                                                             |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MacOS    | [couchbase-lite-c-enterprise-3.2.4-macos.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-macos.zip) | [couchbase-lite-c-enterprise-3.2.4-macos.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-macos.zip.sha256) | [couchbase-lite-c-enterprise-3.2.4-macos-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-macos-symbols.zip) |

Community Edition

| Platform | Download                                                                                                                                                | SHA                                                                                                                                                                   | Debug Symbols                                                                                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MacOS    | [couchbase-lite-c-community-3.2.4-macos.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-macos.zip) | [couchbase-lite-c-community-3.2.4-macos.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-macos.zip.sha256) | [couchbase-lite-c-community-3.2.4-macos-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-macos-symbols.zip) |

#### [](#windows-3-2-4)Windows

Example 2\. Download link table

Enterprise Edition

| Platform | Download                                                                                                                                                                       | SHA | Debug Symbols                                                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | [couchbase-lite-c-enterprise-3.2.4-windows-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-windows-x86%5F64.zip) |     | [couchbase-lite-c-enterprise-3.2.4-windows-x86\_64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-windows-x86%5F64-symbols.zip) |

Community Edition

| Platform | Download                                                                                                                                                                     | SHA | Debug Symbols                                                                                                                                                                                |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | [couchbase-lite-c-community-3.2.4-windows-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-windows-x86%5F64.zip) |     | [couchbase-lite-c-community-3.2.4-windows-x86\_64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-windows-x86%5F64-symbols.zip) |

#### [](#debian-3-2-4)Debian

Example 3\. Download link table

Enterprise Edition

| Platform                                                                                                                                                                                         | Download                                                                                                                                                                         | SHA                                                                                                                                                                                            | Debug Symbols                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Debian                                                                                                                                                                                           | [couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz)      | [couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz.sha256)      | [couchbase-lite-c-enterprise-3.2.4-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64-symbols.tar.gz) |
| <https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4>                                                                                                                                 | [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64.tar.gz) | [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64.tar.gz.sha256) |                                                                                                                                                                                             |
| [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64-symbols.tar.gz) | [libcblite-enterprise\_3.2.4-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Famd64.deb)              | [libcblite-enterprise\_3.2.4-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Famd64.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Famd64.deb)      | [libcblite-dev-enterprise\_3.2.4-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Famd64.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Farm64.deb)              | [libcblite-enterprise\_3.2.4-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Farm64.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Farm64.deb)      | [libcblite-dev-enterprise\_3.2.4-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Farm64.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Farmhf.deb)              | [libcblite-enterprise\_3.2.4-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian11%5Farmhf.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Farmhf.deb)      | [libcblite-dev-enterprise\_3.2.4-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian11%5Farmhf.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian10%5Famd64.deb)              | [libcblite-enterprise\_3.2.4-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian10%5Famd64.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian10%5Famd64.deb)      | [libcblite-dev-enterprise\_3.2.4-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian10%5Famd64.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian10%5Farm64.deb)              | [libcblite-enterprise\_3.2.4-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian10%5Farm64.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian10%5Farm64.deb)      | [libcblite-dev-enterprise\_3.2.4-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian10%5Farm64.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.1-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.1/libcblite-enterprise%5F3.2.1-debian10%5Farmhf.deb)              | [libcblite-enterprise\_3.2.1-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.1/libcblite-enterprise%5F3.2.1-debian10%5Farmhf.deb.sha256)              |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.1-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.1/libcblite-dev-enterprise%5F3.2.1-debian10%5Farmhf.deb)      | [libcblite-dev-enterprise\_3.2.1-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.1/libcblite-dev-enterprise%5F3.2.1-debian10%5Farmhf.deb.sha256)      |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian9%5Famd64.deb)                | [libcblite-enterprise\_3.2.4-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian9%5Famd64.deb.sha256)                |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian9%5Famd64.deb)        | [libcblite-dev-enterprise\_3.2.4-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian9%5Famd64.deb.sha256)        |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-enterprise\_3.2.4-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian9%5Farmhf.deb)                | [libcblite-enterprise\_3.2.4-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-debian9%5Farmhf.deb.sha256)                |                                                                                                                                                                                             |
|                                                                                                                                                                                                  | [libcblite-dev-enterprise\_3.2.4-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian9%5Farmhf.deb)        | [libcblite-dev-enterprise\_3.2.4-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-debian9%5Farmhf.deb.sha256)        |                                                                                                                                                                                             |

Community Edition

| Platform                                                                                                                                                                                | Download                                                                                                                                                                                | SHA                                                                                                                                                                                       | Debug Symbols                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Debian                                                                                                                                                                                  | [couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz)               | [couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz.sha256)   | [couchbase-lite-c-community-3.2.4-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz)               | [couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz.sha256) | [couchbase-lite-c-community-3.2.4-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf-symbols.tar.gz) |                                                                                                                                                                                           |
| [couchbase-lite-c-community-3.2.4-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-x86%5F64.tar.gz)          | <https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-x86%5F64.tar.gz.sha256>\[couchbase-lite-c-community-3.2.4-linux-x86\_64.tar.gz.  | [libcblite-community\_3.2.4-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Famd64.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Famd64.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian11\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Famd64.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian11\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Famd64.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Farm64.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Farm64.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian11\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Farm64.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian11\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Farm64.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Farmhf.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian11%5Farmhf.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian11\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Farmhf.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian11\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian11%5Farmhf.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Famd64.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Famd64.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian10\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Famd64.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian10\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Famd64.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Farm64.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Farm64.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian10\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Farm64.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian10\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Farm64.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Farmhf.deb)                         |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian10%5Farmhf.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian10\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Farmhf.deb)                 |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian10\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian10%5Farmhf.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian9%5Famd64.deb)                           |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian9%5Famd64.deb.sha256)           |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian9\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian9%5Famd64.deb)                   |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-debian9\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian9%5Famd64.deb.sha256)   |                                                                                                                                                                                         | [libcblite-community\_3.2.4-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian9%5Farmhf.deb)                           |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-debian9\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-debian9%5Farmhf.deb.sha256)           |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-debian9\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-debian9%5Farmhf.deb)                   |                                                                                                                                                                                           |

#### [](#ubuntu-3-2-4)Ubuntu

Example 4\. Download link table

Enterprise Edition

| Platform                                                                                                                                                                                        | Download                                                                                                                                                                                        | SHA                                                                                                                                                                                              | Debug Symbols                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu                                                                                                                                                                                          | [couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz)                     | [couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64.tar.gz.sha256)        | [couchbase-lite-c-enterprise-3.2.4-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-enterprise-3.2.4-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-armhf.tar.gz)                     | [couchbase-lite-c-enterprise-3.2.4-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-armhf.tar.gz.sha256)       | [couchbase-lite-c-enterprise-3.2.4-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-armhf-symbols.tar.gz)      |                                                                                                                                                                                             |
| [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64.tar.gz)                | [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64.tar.gz.sha256)  | [couchbase-lite-c-enterprise-3.2.4-linux-x86\_64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-enterprise-3.2.4-linux-x86%5F64-symbols.tar.gz) |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Famd64.deb)                       | [libcblite-enterprise\_3.2.4-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                  |                                                                                                                                                                                             |
| [libcblite-dev-enterprise\_3.2.4-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu22.04%5Famd64.deb)               | [libcblite-dev-enterprise\_3.2.4-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu22.04%5Famd64.deb.sha256) |                                                                                                                                                                                                  |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Farm64.deb)                       | [libcblite-enterprise\_3.2.4-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                  |                                                                                                                                                                                             |
| <https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu22.04%5Farm64.deb>\[libcblite-dev-enterprise\_3.2.4-ubuntu22.04\_arm6                    |                                                                                                                                                                                                 | [libcblite-enterprise\_3.2.4-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Farmhf.deb)                        |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu22.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                 | [libcblite-dev-enterprise\_3.2.4-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu22.04%5Farmhf.deb)                |                                                                                                                                                                                             |
| [libcblite-dev-enterprise\_3.2.4-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu22.04%5Farmhf.deb.sha256) |                                                                                                                                                                                                 | [libcblite-enterprise\_3.2.4-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Famd64.deb)                        |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Famd64.deb.sha256)         |                                                                                                                                                                                                 | [libcblite-dev-enterprise\_3.2.4-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu20.04%5Famd64.deb)                |                                                                                                                                                                                             |
| <https://packages.couchbase.com/releases/couchbase-lite->                                                                                                                                       |                                                                                                                                                                                                 | [libcblite-enterprise\_3.2.4-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Farm64.deb)                        |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Farm64.deb.sha256)         |                                                                                                                                                                                                 | [libcblite-dev-enterprise\_3.2.4-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu20.04%5Farm64.deb)                |                                                                                                                                                                                             |
| [libcblite-dev-enterprise\_3.2.4-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu20.04%5Farm64.deb.sha256) |                                                                                                                                                                                                 | [libcblite-enterprise\_3.2.4-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Farmhf.deb)                        |                                                                                                                                                                                             |
| [libcblite-enterprise\_3.2.4-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-enterprise%5F3.2.4-ubuntu20.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                                 | [libcblite-dev-enterprise\_3.2.4-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-enterprise%5F3.2.4-ubuntu20.04%5Farmhf.deb)                |                                                                                                                                                                                             |

Community Edition

| Platform                                                                                                                                                                                      | Download                                                                                                                                                                                | SHA                                                                                                                                                                                           | Debug Symbols                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu                                                                                                                                                                                        | [couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz)               | [couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64.tar.gz.sha256)       | [couchbase-lite-c-community-3.2.4-linux-arm64-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-arm64-symbols.tar.gz) |
| [couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz)                     | [couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf.tar.gz.sha256) | [couchbase-lite-c-community-3.2.4-linux-armhf-symbols.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-armhf-symbols.tar.gz)     |                                                                                                                                                                                           |
| [couchbase-lite-c-community-3.2.4-linux-x86\_64.tar.gz](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-x86%5F64.tar.gz)                | <https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/couchbase-lite-c-community-3.2.4-linux-x86%5F64.tar.gz.sha256>\[couchbase-lite-c-community-3.2.4-linux-x86\_64.tar      | [libcblite-community\_3.2.4-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Famd64.deb)                       |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Famd64.deb.sha256)         |                                                                                                                                                                                         | [libcblite-dev-community\_3.2.4-ubuntu22.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu22.04%5Famd64.deb)               |                                                                                                                                                                                           |
| [libcblite-dev-community\_3.2.4-ubuntu22.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu22.04%5Famd64.deb.sha256) |                                                                                                                                                                                         | [libcblite-community\_3.2.4-ubuntu22.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Farm64.deb)                       |                                                                                                                                                                                           |
| [libcblite-community\_3.2.4-ubuntu22.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Farm64.deb.sha256)         |                                                                                                                                                                                         | <https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu22.04%5Farm64.deb>\[libcblite-dev-community\_3.2.4-ubuntu22                             |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-community\_3.2.4-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Farmhf.deb)                 | [libcblite-community\_3.2.4-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu22.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-dev-community\_3.2.4-ubuntu22.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu22.04%5Farmhf.deb)         | [libcblite-dev-community\_3.2.4-ubuntu22.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu22.04%5Farmhf.deb.sha256) |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-community\_3.2.4-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Famd64.deb)                 | [libcblite-community\_3.2.4-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Famd64.deb.sha256)         |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-dev-community\_3.2.4-ubuntu20.04\_amd64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu20.04%5Famd64.deb)         | [libcblite-dev-community\_3.2.4-ubuntu20.04\_amd64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu20.04%5Famd64.deb.sha256) |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-community\_3.2.4-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Farm64.deb)                 | [libcblite-community\_3.2.4-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Farm64.deb.sha256)         |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-dev-community\_3.2.4-ubuntu20.04\_arm64.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu20.04%5Farm64.deb)         | [libcblite-dev-community\_3.2.4-ubuntu20.04\_arm64.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.4-ubuntu20.04%5Farm64.deb.sha256) |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-community\_3.2.4-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Farmhf.deb)                 | [libcblite-community\_3.2.4-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-community%5F3.2.4-ubuntu20.04%5Farmhf.deb.sha256)         |                                                                                                                                                                                           |
|                                                                                                                                                                                               | [libcblite-dev-community\_3.2.1-ubuntu20.04\_armhf.deb](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.1-ubuntu20.04%5Farmhf.deb)         | [libcblite-dev-community\_3.2.1-ubuntu20.04\_armhf.deb.sha256](https://packages.couchbase.com/releases/couchbase-lite-c/3.2.4/libcblite-dev-community%5F3.2.1-ubuntu20.04%5Farmhf.deb.sha256) |                                                                                                                                                                                           |

#### [](#raspbian-3-2-4)Raspbian

Please use the [Debian .deb download](#debian-3-2-4) choosing the appropriate version (`debian9` or `debian10`) and architecture.

### [](#vs-release-1-0-0)Vector Search Release 1.0.0

_Couchbase Lite Vector Search - C_ is available for all [Supported Platforms](supported-os.md). You can obtain downloads for _Linux_ and _macOS_ from the links here in the downloads table. Ensure you select the correct package for your application's compiler and architecture.

Alternatively, check the [install](gs-install.md)page for instructions on how to get the software using a package manager.

Available platforms are:

[Android](#android-1-0-0) | [MacOS](#macos-1-0-0) | [iOS](#ios-1-0-0) | [Windows](#windows-1-0-0) | [Linux](#linux-1-0-0) |

> [!IMPORTANT]
> You must have Couchbase Lite installed before you can use the Vector Search Extension. Vector Search is available only for 64-bit architectures. The Vector Search extension is an **Enterprise-only** feature.

#### [](#android-1-0-0)Android

Download link table

* Enterprise

| Platform                                                                                                                                                                                     | Download                                                                                                                                                                                                   | SHA                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Android                                                                                                                                                                                      | [couchbase-lite-vector-search-1.0.0-android-arm64-v8a.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-android-arm64-v8a.zip)            | [couchbase-lite-vector-search-1.0.0-android-arm64-v8a.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-android-arm64-v8a.zip.sha256) |
| [couchbase-lite-vector-search-1.0.0-android-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-android-x86%5F64.zip) | [couchbase-lite-vector-search-1.0.0-android-x86\_64.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-android-x86%5F64.zip.sha256) |                                                                                                                                                                                                               |

#### [](#macos-1-0-0)MacOS

Download link table

* Enterprise Edition

| Platform      | Download | SHA                                                                                                                                                                     |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Debug Symbols | MacOS    | [couchbase-lite-vector-search-1.0.0-macos.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-macos.zip) |

#### [](#ios-1-0-0)iOS

Download link table

* Enterprise Edition

| Platform | Download                                                                                                                                                                                  | SHA                                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| iOS      | [couchbase-lite-vector-search\_xcframework\_1.0.0.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search%5Fxcframework%5F1.0.0.zip) | [couchbase-lite-vector-search\_xcframework\_1.0.0.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search%5Fxcframework%5F1.0.0.zip.sha256) |

#### [](#windows-1-0-0)Windows

Download link table

* Enterprise Edition

| Platform                                                                                                                                                                                     | Download                                                                                                                                                                                            | SHA                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows                                                                                                                                                                                      | [couchbase-lite-vector-search-1.0.0-windows-arm64.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-windows-arm64.zip)             | [couchbase-lite-vector-search-1.0.0-windows-arm64.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-windows-arm64.zip) |
| [couchbase-lite-vector-search-1.0.0-windows-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-windows-x86%5F64.zip) | [couchbase-lite-vector-search-1.0.0-windows-x86\_64.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-windows-x86%5F64.zip) |                                                                                                                                                                                                |

#### [](#linux-1-0-0)Linux

Download link table

* Enterprise

| Platform                                                                                                                                                                                 | Download                                                                                                                                                                                               | SHA                                                                                                                                                                                                      | Debug Symbols                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux                                                                                                                                                                                    | [couchbase-lite-vector-search-1.0.0-linux-aarch64.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-aarch64.zip)                | [couchbase-lite-vector-search-1.0.0-linux-aarch64.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-aarch64.zip.sha256)    | [couchbase-lite-vector-search-1.0.0-linux-aarch64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-aarch64-symbols.zip) |
| [couchbase-lite-vector-search-1.0.0-linux-x86\_64.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-x86%5F64.zip) | [couchbase-lite-vector-search-1.0.0-linux-x86\_64.zip.sha256](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-x86%5F64.zip.sha256) | [couchbase-lite-vector-search-1.0.0-linux-x86\_64-symbols.zip](https://packages.couchbase.com/releases/couchbase-lite-vector-search/1.0.0/couchbase-lite-vector-search-1.0.0-linux-x86%5F64-symbols.zip) |                                                                                                                                                                                                         |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.