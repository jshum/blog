---
layout: post
title: "Add Custom Firefox Shortcuts"
tldr: ""
tags: []
---

[1]: http://evernote.com/webclipper/
[2]: http://kb.mozillazine.org/Keyconfig_extension
[3]: https://addons.mozilla.org/en-US/firefox/addon/dom-inspector-6622/
[4]: https://developer.mozilla.org/en-US/docs/DOM_Inspector/Introduction_to_DOM_Inspector

Installed [Evernote Web Clipper][1] and wanted a keyboard shortcut for the "Add to Evernote" Action. Unfortunately, the keyboard shortcut feature is only available for the Chrome addon so had to find a way to create one.

Solution : Use [keyconfig][2]. Keyconfig extension allows you to configure keyboard shortcuts. 

Step 1. Install keyconfig. 

Keyconfig isn't very user-friendly. There isn't a GUI for you to record/select the action you want to create a shortcut for so you have to find out what code triggers the same action. You can find this out by exploring the Browser's DOM tree but you can't do this by using the built-in Web Developer Tools. So you need to download another add-on called [DOM Inspector][3].

Step 2a. Install DOM Inspector. [Overview][4]

Step 2b. Acess it under Tools->Web Developer->Dom Inspector

Step 2c. A new window will appear. File->Inspect Chrome document->Click first item

Step 2d. Click *Inspect* on top right corner.

Step 2e. Click the top left icon with the little pointer, then select tools.

Step 2f. The DOM tree will expand and now try to find the corresponding element for "Add to Evernote". Make sure on the right panel, "Object - Dom Node" is selected. Look for the Attribute oncommand and copy and past the value.

If you're doing this for Evernote Web Clippber, the value for the oncommand attribute is "evernote_doAction( null );"

Step 3a. Open up keyconfig `Ctrl+Shift+F12`

Step 3b. "Add a new key"

Step 3c. Name it and paste "evernote_doAction( null);" inside the textbox. Press ok

Step 3d. Create a keyboard shortcut for it. 

Voila. You now have a custom keyboard shortcut for evernote. 

Context : I read a crap ton of articles and shit from Hacker News, Reddit everyday so I want a way to be able to log the stuff I read. I at first tried copying and pasting links to a text file but that proved to be too much inertia. So, I've decided to use Evernote Web Clipper which will not only add a snapshot of the page when I visited it, but also have the date of when it was created. I wanted it to be really easy to "Add to Evernote" so I had to do it using a keyboard shortcut.

[a1]: http://appcenter.evernote.com/
[a2]: https://developer.apple.com/library/ios/documentation/uikit/reference/UIActivityViewController_Class/Reference/Reference.html

I've been trying to do the same thing on iOS, trying to get the Hacker News iOS app I use to share to Evernote. But you can't 'Share to Evernote' anymore. You have to write an app that very specifically integrates with [Evernote][a1]'s functionality. Apparently, there is a default view for the share view you see on most apps on iOS when you click the box with the arrow coming out of it, which is governed by [UIActivityViewController][a2]. The only way to change it is to write your own custom one, which means it's not customizable through the iOS settings.

This means that I won't be able to add the "Share to Evernote" button to the HackerNews apps. Other solutions would include copying the URL to the iOS clipboard and sending that to the browser. But again, because there is no Firefox for iOS, this is difficult. Furthermore, syncing copy and paste clipboards only works on the OS level (between iOS + Mac OS X) but not on the browser level. 


