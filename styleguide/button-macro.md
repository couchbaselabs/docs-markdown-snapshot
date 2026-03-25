---
title: Button Macro
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/button-macro.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:styleguide::button-macro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/styleguide/button-macro.html)

# Button Macro

Use the Antora `btn:[]` Macro for buttons and named items that the user clicks in the UI. The button can be inside the step for a procedure, but the text does not need to be in a procedure to use the macro.

For example, `btn:[Submit]` renders as **Submit**.

The following UI elements are considered buttons:

* Any clickable element that opens a dialog or pane.
* Any clickable element that causes an action to happen.
* Any clickable element that contains an icon.

![buttons examples](_images/buttons-examples.png) 

> [!NOTE]
> A button might or might not have a defined border and color.

When you need to describe a button in the UI:

* Refer to the button by its name only. Do not add "button."  
For example, **Submit**.
* Use the `btn:[]` macro to format the button.

If a clickable element changes the screen or navigates the user away from their current location in the UI, use the [Menu UI Macro](menu-ui-macro.md), instead.

For more information about how to use the Button Macro to format your documentation, see [Button, Keyboard, and Menu UI Macros](../home/contribute/basics.md#ui-macros) in the Contributing to the Documentation guide.