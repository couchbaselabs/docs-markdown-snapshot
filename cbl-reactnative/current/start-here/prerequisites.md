---
title: Prerequisites
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite React Native
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/start-here/pages/prerequisites.adoc
  xref: xref:cbl-reactnative:start-here:prerequisites.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/start-here/prerequisites.html)

# Prerequisites

Couchbase Lite for React Native is provided as a [Native Module](https://reactnative.dev/docs/legacy/native-modules-intro). Version 1.1 supports [React Native New Architecture](https://reactnative.dev/architecture/overview) through TurboModules on iOS and Android.

The Native Module can be found at the following repository: [Couchbase Lite for React Native](https://github.com/couchbase/couchbase-lite-react-native). npm package: [@couchbase/couchbase-lite-react-native](https://www.npmjs.com/package/@couchbase/couchbase-lite-react-native). Shared TypeScript and JavaScript code lives in [cblite-js](https://github.com/couchbase/couchbase-lite-js-common).

A developer using this plugin should have a basic understanding of the following technologies:

* [React Native](https://reactnative.dev/)
* [React Native - Native Modules](https://reactnative.dev/docs/legacy/native-modules-intro)
* [React Native - New Architecture](https://reactnative.dev/architecture/overview)
* [Expo Framework](https://docs.expo.dev/)
* [Couchbase Lite](https://docs.couchbase.com/couchbase-lite/current/index.html)

## [](#expo-note)Expo Note

React Native's recommmendation is to use [Expo](https://reactnative.dev/blog/2024/06/25/use-a-framework-to-build-react-native-apps) for development . The example app that comes with the repository is an Expo based app, thus this Native Module can work in Expo apps. Note using Expo Go is not supported due to Expo Go not supporting loading 3rd party Native Modules. You will need to be familiar with the [Expo Dev Client](https://docs.expo.dev/guides/local-app-development/#local-builds-with-expo-dev-client) process to use this Native Module in an Expo app.

## [](#supported-platforms)Supported Platforms

* The React Native - Native Module is supported on iOS and Android platforms. MacOS, Windows, and Web support is not available at this time.

## [](#react-native-version)React Native Version

* The plugin is built using React Native 0.76.3\. Support for older versions of React Native is not guaranteed and apps should be based on 0.76.3 or higher.
* Version 1.1 supports TurboModules through [React Native New Architecture](https://reactnative.dev/architecture/overview). Apps should enable New Architecture when using the TurboModule implementation.

Please review the React Native [Support documentation](https://github.com/reactwg/react-native-releases/blob/main/docs/support.md) for a full listed of supported platform versions.

## [](#development-environment)Development Environment

* Javascript

  * [Node >= 20](https://formulae.brew.sh/formula/node@18)
* React Native

  * [React Native Docs](https://reactnative.dev/)
  * [Understanding React Native - Native Modules](https://reactnative.dev/docs/legacy/native-modules-intro)
* Expo (if you choose to use Expo, not required but recommended)

  * [Expo Docs](https://docs.expo.dev/)
  * [Expo Dev Client](https://docs.expo.dev/guides/local-app-development/#local-builds-with-expo-dev-client)
  * [Expo Mono Repos](https://docs.expo.dev/guides/monorepos/)
  * [Expo Plugin and mods](https://docs.expo.dev/config-plugins/introduction/)
* IDEs

  * [Visual Studio Code](https://code.visualstudio.com/download)
  * [IntelliJ IDEA](https://www.jetbrains.com/idea/download/)
* iOS Development

  * A modern Mac
  * [XCode 15.1](https://developer.apple.com/xcode/) or higher installed and working
  * \[iOS 15.1 or higher\]. Any apps using the plugin must be upgraded to iOS 15.1 or higher.
  * [XCode Command Line Tools](https://developer.apple.com/download/more/) installed
  * [Simulators](https://developer.apple.com/documentation/safari-developer-tools/installing-xcode-and-simulators) downloaded and working
  * [Homebrew](https://brew.sh/)
  * [Cocopods](https://formulae.brew.sh/formula/cocoapods)
  * A valid Apple Developer account and certificates installed and working
* Android Development

  * \[API 24 (Android 7)\] or higher. Any apps using the plugin must be upgraded to API 24 or higher. Any older versions of Android are not supported by React Native and Expo.
  * [Android Studio](https://developer.android.com/studio?gad%5Fsource=1&gclid=CjwKCAjwzN-vBhAkEiwAYiO7oALYfxbMYW%5FzkuYoacS9TX16aItdvLYe6GB7%5Fj1QwvXBjFDRkawfUBoComcQAvD%5FBwE&gclsrc=aw.ds) installed and working
  * Android SDK 34 >= installed and working (with command line tools)
  * Java SDK v17 installed and configured to work with Android Studio
  * An Android Emulator downloaded and working