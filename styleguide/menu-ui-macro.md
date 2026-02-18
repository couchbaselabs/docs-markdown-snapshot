---
title: Menu UI Macro
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/menu-ui-macro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/styleguide/menu-ui-macro.html)

# Menu UI Macro

Use Antora’s Menu UI Macro to render any menu navigation in your documentation.

For example, `menu:File[Save]` renders as **File** **Save** in the Couchbase Documentation.

The menu navigation can be inside the step for a procedure, but the text does not need to be in a procedure to use the macro.

The following situations are considered menu navigation:

* Any selections a user makes that causes a significant change to the base contents of a page.
* Any selections a user makes that brings the user to a new page.

More specifically, selections made in the following UI elements use the Menu UI Macro:

* Any sequence of [tab](tabs.md) and [menu](menus.md) navigation.  
For example, if you instruct the user to select the **Data Tools** tab and then the **Buckets** menu item.
* The Profile menu.
* Any hamburger or **More** menu (⋮ or …​).

![menu nav examples](_images/menu-nav-examples.png) 

![menu nav examples 2](_images/menu-nav-examples-2.png) 

![menu nav examples 3](_images/menu-nav-examples-3.png) 

For more information about how to use the Menu UI Macro to format your documentation, see [Button, Keyboard, and Menu UI Macros](#home:contribute:basics.adoc#ui-macros) in the Contributing to the Documentation guide.