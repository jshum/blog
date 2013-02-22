---
layout: post
title: "mute spotify on ubuntu"
tldr: "Using a script to mute spotify on ubuntu"
tags: [hack, cs, ubuntu, spotify, ad, linux, music]
---

[1]: https://gist.github.com/pcworld/3198763
[2]: jshum.github.com/blog/assets/code/spotify-admute.sh 
This is a pretty geeky thing to do but I just spent about two hours searching for a way to mute Spotify on my Ubuntu desktop when the ads come on. I found a script [here][1] and uploaded my own version of it [here][2]

I don't think it's illegal. It just takes advantage of the metadata that Spotify sends to the client to figure out where the track being played is an ad or a song, which is really just like selective hearing I do everyday. It uses pactl (which is apparently the 'sound system for POSIX OS'es) to do the muting. The stupid bug that took me a long time to figure out is that my computer somehow isn't using the soundcard I have installed so the input to the command had to be changed. 

Try it out. Let me know if you have questions

