---
layout: page
title: "TabSync"
group: show
description: ""
---

##TabSync Firefox Extension##

[g1]: https://github.com/jshum/addon-sdk
[f2]: https://addons.mozilla.org/en-US/firefox/addon/tabsync/

[Download link][f2]
[Github Repo][g1]

###Motivation###

I use multiple computers throughout the day and I get annoyed because I'm not able to sync my tabs across laptops. There are several halfway solutions that exist out there:

[t1]: https://chrometabcloud.appspot.com/
[f1]: https://support.mozilla.org/en-US/kb/how-do-i-set-up-firefox-sync
[x1]: https://helpdesk.xmarks.com/bookmark-manager-basics/open-tab-sync/

[Firefox][f1]/[Xmarks][x1] OpenTabs Sync : saves all your current opened tabs, but displays it in a window and you have to manually click each to open all of them.
[TabCloud][t1] : allows you to save and load all the tabs in any open window. But you have to press save and load every time.

Neither of these workflows are ideal for me because I often bring out my laptop for a few minutes to check something and won't be inclined to save my session every time I use it, as would be necessary for TabCloud.
Firefox on the other hand requires you to open every tab manually from the "OpenTabs Across Devices" window, which is not idle either.

The workflow I suggest automatically syncs your open tabs, then with one click will open all the tabs that are open in other browser in the current browser.

###Requirements###

* Firefox Browser
* Enable Firefox Sync/Xmarks, sync bookmarks across all browsers that you want it to work on. 

###Overview###

**On Computer 1**

Addon saves all your currently opened tabs as bookmarks inside the 'TabSync' folder every time you navigate to a new site on any of your tabs. 

**On Computer 2**

*Firefox Sync/Xmarks will sync all your bookmarks inside 'TabSync' across all your browsers that have it enabled. Thus, all the tabs that were open on Computer 1 are now bookmarks inside 'TabSync' on Computer 2*

Pressing the widget button will trigger a merge sync process. Addon will go through all the bookmarks inside 'TabSync' folder and if any of the bookmarks inside 'TabSync' are not open on Computer 2, they will be opened. 

###Technical Notes###

* The addon saves all its bookmarks inside the 'TabSync' folder so don't delete it otherwise you lose all your saved tabs.
* Addon saves a bookmark called 'TabSyncAnchor' inside the 'TabSync' bookmarks folder. **DON'T DELETE IT.** This is necessary for the addon to find the TabSync folder because neither the XUL and SDK have a feature which allows you to search for a folder inside your bookmarks. The only way is to search for a bookmark and get the folder by getting the bookmark's parent folder.
* There are two types of sync right now. MergeSync and PurgeSync. Whenever you open, load a new tab, you are performing Purge Sync. All the current tabs inside the 'TabSync' folder are removed and replaced with your open tabs. Whenever your press the button though, you are performing Merge Sync. All the current tabs inside the 'TabSync' folder are checked and ones that are not currently open will be opened. Ones that are open and not saved are now saved. 
* Therefore, you need to the press the widget button before you load a tab. Otherwise, all the tabs on your current computer will replace the existing tabs inside the 'TabSync' folder.

###Code Overview###

* Mozailla ships with two libraries to write extensions. The old one is the XUL and the new is the Addon SDK that they are now developing. I had wanted to use the SDK entirely for this project but it was proving very limiting in certain cases so I had to use XUL library for a lot of it.
* Nice things about the SDK though. Very simple and easy to use functions.

* Some issues that came up while trying to use the SDK.
* There is no folder search function but this is also the case for the XUL
* tab/save doesn't allow you to save into a certain folder, thus I have to use the XUL insertBookmark method.
* Note that tabs/search and tabs/save are asynchronous functions. So take note of that as in my case because I had to search for the anchor to find its parent folder after saving it. 

Missing Features

* folder search function in SDK
* retrieve all bookmark children of folder in SDK
* insert bookmark function that allows specifying a specific parent folder. 
* remove all bookmark children of folder in SDK

###Resources###

[s1]: https://developer.mozilla.org/en-US/Add-ons/SDK/Tutorials/Installation
[j1]: http://stackoverflow.com/questions/921789/how-to-loop-through-javascript-object-literal-with-objects-as-members
[j2]: http://www.iamcal.com/publish/articles/js/scoping/

* Installing and using [SDK][s1]
* Using Javascript objects as hashtables [SO][j1]
* Javascript scoping example [iamcal][j2]

