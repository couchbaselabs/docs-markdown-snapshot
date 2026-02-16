[View original HTML](/dotnet-sdk/current/hello-world/platform-help.html)

> Discover how to get up and running developing applications with the Couchbase .NET SDK 3.0+ using `Visual Studio Code`. 

A simple .NET orientation intro for _non-_.NET folk who are evaluating the Couchbase .NET SDK.

|  | Is This Page for You? This page is to help evaluate the Couchbase .NET SDK, if .NET is not where you spend the majority of your working day. It is aimed at Software Architects, QE folk, managers, and anyone else who needs to run through using the .NET SDK without necessarily being comfortable with C# and the .NET environment. If this is not you, head back to the [rest of the Couchbase .NET SDK documentation](overview.md). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#installing-net-sdk-core)Installing .NET SDK Core

|  | VSCode requires installing the .NET SDK Core. Full IDEs like Visual Studio or Jetbrains Rider instead install a .NET SDK by default. |
|  | ------------------------------------------------------------------------------------------------------------------------------------ |

|  | The latest Short Term Support (STS) version, .NET 7, isn’t tested against version 3.4.0 of the Couchbase .NET SDK. If you have any issues with this version, switch to a supported version. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

* Start at the .NET [download page](https://dotnet.microsoft.com/download)
* Windows and Mac run an installer, for Linux you have to navigate to the specific instructions for your distribution.
* Couchbase recommends .NET 6, and the sample code generally targets this.
* You may prefer to use an earlier version used in your organization. See [compatibility](../project-docs/compatibility.md#dotnet-compatibility) for more information.
* You can install multiple SDKs, to be able to run code targeting different versions. Use the `dotnet` command to list which versions are available. Here’s an example output with 5.0 and 3.1 SDKs installed:

```console
❯ dotnet --list-runtimes
Microsoft.AspNetCore.App 3.1.16 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 5.0.3 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
Microsoft.NETCore.App 3.1.16 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
Microsoft.NETCore.App 5.0.3 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
❯ dotnet --list-sdks
3.1.410 [/usr/local/share/dotnet/sdk]
5.0.103 [/usr/local/share/dotnet/sdk]
```

If you’re just starting with .NET or C# then <https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/intro> is a great starting point into the ecosystem.

## [](#vscode)Using a Code Editor (Visual Studio Code)

Visual Studio Code is a free code editor which runs on Windows, Linux, and MacOS and can be downloaded [here](https://code.visualstudio.com/). Once downloaded, follow the installation details for the relevant platform:

* <https://code.visualstudio.com/docs/setup/setup-overview>

|  | We’ve given instructions for VS Code as it’s a currently popular, cross-platform, multi-language editor that’s seeing widespread use, and is easy to set up and get started. If you’re planning to primarily develop in C#, you may prefer to look into using a full IDE like [Visual Studio](https://visualstudio.microsoft.com/) (the 2019 Community edition and the Mac edition are both free) or [JetBrains Rider](https://www.jetbrains.com/rider/). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#adding-c-development-support)Adding C# Development Support

VSCode is a flexible editor, with support for various programming languages. Though basic syntax highlighting for .NET languages is included in the box, you’ll find it useful to add an extension with support for development — debugging, discovery, and navigation — in your chosen programming language.

For .NET, we suggest using `ms-dotnettools.csharp`, "C# for Visual Studio Code (powered by OmniSharp)" by Microsoft, which facilitates development in [C#](https://code.visualstudio.com/docs/languages/csharp), the most commonly used .NET language.

1. You can install from within VSCode itself:

  * Open VSCode

    * When you first open a C# project, you will be auto-prompted to install the recommended package.
    * Alternatively, select the `Extensions` button on the left hand side.
    * Type `ms-dotnettools.csharp` into the `Search Extensions in Marketplace` textbox and hit enter.
    * Select and install the language extension into the editor.
2. Alternatively, use the VSCode marketplace:

  * Start by opening <https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp>
  * Clicking on the `Install` button will prompt you to `Open Visual Studio Code` which will then install the extension.

### [](#adding-the-code-command)Adding the `code` command

If you work from the command-line, you’ll want to add the `code` command to allow you to edit a file directly.

In VSCode, View the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and search for `Shell command: Install 'code' command in PATH` and press Enter.

You can now type `code MyExample.cs` to open a single file in VSCode, or `code .` to view the current directory.

### [](#creating-a-project)Creating a project

An increasingly common way of setting up projects, building, and running code, is by using the `dotnet` executable that is installed along with the .NET SDK.

In the following example, we’ll open our terminal, make a new directory, set up a bare-bones "console" project, install the Couchbase client library, and run the scaffolding code.

```console
$ mkdir CouchbaseExample
$ cd CouchbaseExample

# create a basic "console" application
$ dotnet new console

$ dotnet run
Hello World!

$ dotnet add package CouchbaseNetClient

$ ls
CouchbaseExample.csproj
Program.cs
bin
obj

$ cat CouchbaseExample.csproj
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net5.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CouchbaseNetClient" Version="3.2.0" />
  </ItemGroup>
</Project>

$ code Program.cs
```

You should see a `Hello World` message printed in your terminal, which means the application has run successfully.

Now you can launch VSCode and open the `CouchbaseExample` directory to start editing the `Program.cs` file.

## [](#running-couchbase-examples)Running Couchbase examples

As you read through the docs, you will see that many code examples link to the [.NET SDK docs Github repository](https://github.com/couchbase/docs-sdk-dotnet/). If you wish to run those examples to try things out for yourself, you can clone this repository and run the examples in any directory that contains a .csproj file:

```console
$ dotnet run
```

You can read the .csproj file to check which external libraries (such as the Couchbase SDK) are included.

Some examples have been tweaked to use [dotnet script](https://github.com/filipw/dotnet-script), which allows you to run a single `.csx` file from the command-line, without the full overhead of the project/solution wrapper. This is an extension, so you will have to install it first.

```console
$ dotnet tool install -g dotnet-script

$ dotnet script modules/howtos/examples/EncryptingUsingSdk.csx
```

## [](#next-steps)Next steps

That’s it! You are now ready to [start developing your Couchbase application](start-using-sdk.md).