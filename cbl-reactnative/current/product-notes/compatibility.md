---
title: Compatibility
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite React Native
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/product-notes/pages/compatibility.adoc
  xref: xref:cbl-reactnative:product-notes:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/product-notes/compatibility.html)

# Compatibility

> [!NOTE]
> Supported iOS and Android versions are dependent on React Native. See the [React Native Documentation](https://github.com/reactwg/react-native-releases/blob/main/docs/support.md) documentation for more information.

The @couchbase/couchbase-lite-react-native library is built against Couchbase Lite Enterprise for iOS and Android. Version 1.1 uses Couchbase Lite Android Enterprise 3.3.3 and Couchbase Lite Swift Enterprise 3.3.3.

Version 1.1 supports [React Native New Architecture](https://reactnative.dev/architecture/overview) through TurboModules. Apps should use React Native 0.76.3 or higher and enable New Architecture for the TurboModule path.

## [](#platform-support)Platform Support

| Environment | Support Status |
| ----------- | -------------- |
| iOS         | Supported      |
| Android     | Supported      |
| Web         | Not supported  |
| Windows     | Not supported  |
| macOS       | Not supported  |

## [](#native-sdk-compatibility)Native SDK Compatibility

To see the compatibility notes for the native SDK, see the following documentation:

* [Couchbase Mobile Compatibility Guide - iOS](https://docs.couchbase.com/couchbase-lite/current/swift/supported-os.html).
* [Couchbase Mobile Compatibility Guide - Android](https://docs.couchbase.com/couchbase-lite/current/android/supported-os.html).