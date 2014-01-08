---
layout: post
title: "21st century hacks"
tldr: "how to get whatsapp on your pc and get a custom domain name email for free"
tags: [cs, hack, lifehacker, whatsapp, email, custom domain]
---

###Whatsapp on PC###

[w1]: https://github.com/tgalal/yowsup/wiki/yowsup-cli
[w2]: https://coderus.openrepos.net/whitesoft/whatsapp_sms
[w3]: https://github.com/davidgfnet/whatsapp-purple

1. [yowsup-cli][w1] - command line interface for you to request a whatsapp account
2. [yowsup online][w2] - same as yowsup but always works
3. [whatsapp-purple][w3] - plugin for pidgin to take whatsapp accounts

Start by following the instructions on yowsup-cli to create and register your whatsapp account. Then, install pidgin and the plugin if you want to use it on your laptop

####Troubleshooting####

1. Each number is a whatsapp account. You can't have one number connected to more than one device at once. Only one whatsapp number per one device. Once you register another device, it kills your account on the old device. 
2. The workaround is having a groupchat where you have one number representing your phone and another number representing your pidgin client.
3. Before we even worry about the fact that this is slightly socially awkward. Pidgin doesn't work well with group chats either. There's some problems related to being added to a group.

###Windows Live Email with Custom Domain###

[1]: shumjason.com
[2]: domains.live.com
[3]: http://office.microsoft.com/en-001/office365-suite-help/what-is-mx-priority-HA104086710.aspx?CTT=5&origin=HA103106254

If you own a domain name like me for your [own][1] personal website, then you can actually also have your own custom email on that domain for free. Outlook provides 50 free email accounts per domainname for free. 

1. Create a new account on [domains.live.com][2]
2. Create appropriate MX records on the DNS record. Remember to remove everything of higher [priority][3], meaning smaller numbers.
3. This just verifies to Microsoft that you own the domain name. Afterwards, you have your emails.

Guide

* http://betanews.com/2013/08/26/how-to-use-outlook-com-as-a-free-custom-domain-email-host/






