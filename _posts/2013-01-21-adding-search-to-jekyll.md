---
layout: post
title: "Adding IndexTank search to jekyll"
tldr: "way to add IndenDen powered search to jekyll blog using github projects"
tags: [jekyll, search, cs, hack, indexden, javascript, jquery]
---

I added full text search to my blog. It was quite triumphant and I probably broke a ton of good coding practices along the way.

When I was searching for solutions, I found a few offerings. 

[gse-1]: http://www.google.com/cse/manage/all

1. [Google Custom Search][gse-1]

The first thing I obviously looked at was google because they are known to have a lot of pretty amazing products and corresponding APIs. The 'Hello World' version is actually really easy:

```
 <script>
  (function() {
    var cx = '017271879301176231845:grhogvs-w3e';
    var gcse = document.createElement('script'); gcse.type = 'text/javascript'; gcse.async = true;
    gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
        '//www.google.com/cse/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(gcse, s);
  })();
</script>
<gcse:search></gcse:search> 
```

It's also really cool because you can choose how the results pop up, if they overlay on top of the current website as a in-page pop up or two column or whatever. But changing the appearence of the code was horrifying so I gave up. 

[marran]: http://www.marran.com/tech/jquery-full-text-indexing-on-jekyll/

2. In [this blog post][marran], the author basically builds his own Jekyll plugin to do it, which I thought was a brave undertaking but difficult to use. 

[so]: http://stackoverflow.com/questions/10131541/how-can-i-add-a-site-search-feature-to-a-jekyll-blog 

3. Then, I kept seeing IndexTank popping around on various sites including [SO][so]. 

I couldn't find IndexTank anymore (because apparently LinkedIn bought IndexTank and shutthem down. But at least it's opensource now.) After some more inquisitive google searching, it turns out IndexTank is basically a hosted indexing servie. You give to them the text you want indexed, and then they'll do it for you. So when you search with a specific query, they'll rank the results for you, which I think is pretty genius.

[iden]: http://indexden.com/
The first IndexTank alternative I found was [IndexDen][iden] because it has IndexTank alternative in the site title. Even with the free plan, you get unlimited daily queries and capacity of indexing 15000 documents, which is a lot better than the API for Google's CSE. Making an account is pretty easy.

[1]: https://github.com/PascalW/jekyll_indextank
[2]: https://github.com/flaptor/indextank-jquery

Now for the next two pieces of the puzzle. IndexDen supports many different languages, so I think it's theoretically possible to write your own code to sent the text to IndexDen for them to index and make it fairly convenient by adding a post-commit hook or sth of that sort. But there was a brilliant PascalW who wrote it as a jekyll plugin making my life a lot easier.

So following the instructions on [the project's github page][1] and copy the .rb file into the _plugins folder of your site. If you look at the code, it pretty intelligently only reindexes files which have been modified after the last-indexed date and avoids all the index pages. If you run jekyll --server on your website, you'll see Indexing PostTitle after you save any file. That part was easy.

Now the difficult portion is getting the results to show up on your webpage. Because all github code is static, it had to be javascript/jquery. The API is all HTTP requests so I don't think it would be too difficult to write your own PHP code or backend code to make those requests. Here is where another github project comes to the rescue, flaptor's [indextank-jquery][2]. It's basically a javascript library that abstracts out all the AJAX HTTP requests and even gives you autocomplete in the search form.

[jq]: http://api.jquery.com/category/manipulation/dom-insertion-inside/
The hardwork has been done for you. Hooking up the jquery isn't that difficult. The more difficult part is in configuring how you want the results to appear. This will require some amount of wrangling with [jquery's DOM insertion methods][jq] eg. append(ele), text(ele), html(ele) to get it the way you want it. (One thing that took me really long to debug is that you need to enable public api queries on the IndexDen dashboard or you'll be getting HTTP 404 responses.)

The next challenge is to insert the search box and results onto the page. I started with a simple solution to have a search page. But if you know a little about jekyll, you know what you put inside markdown files for posts and pages only get put into the body part of the html file so it's impossible to add the headfiles onto only one page. So I had to add it to the default layout. But I will consider having it part of the header or menus as the next iteraton.

[search]: http://jshum.github.com/blog/search.html
It took around two nights of serious hacking to figure it out but I like the end result and I think [it][search] looks good.  
