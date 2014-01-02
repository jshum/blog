# jshum's blog

## Jekyll-Bootstrap

The quickest way to start and publish your Jekyll powered blog. 100% compatible with GitHub pages

## Usage

* gem install jekyll
* gem install indextank nokogiri
* It should now be indexing when you build or run a server.

## Version

0.2.13 - stable and versioned using [semantic versioning](http://semver.org/).

## Log

1. 2012-11-26: ignored the posterous posts from tags.html and JB/tags_list using {{unless tag[0] == 'posterous }}. There must be a better way to do it
2. 2013-01-03: added post.tldr to the front matter. So now if you specify tldr, it will appear at the bottom of the post. Will add a page with only tldrs soon hopefully.
3. 2013-01-21: added search using indextank-jquery and jekyll_indextank. Search is accessed through search.html now, links to google's hosted libraries are added to default.html in layouts/default.html. Next step: switch to a search box on the navigation bar.
4. 2013-01-29: added {% unless post.nosocial %} to the atom.xml page
5. 2013-02-06: added a tldr.html page which is quite nice. 
6. 2013-05-08: fixed the search problem by adding a "blog".concat(item.url || item.link)
7. 2012-05-12: changed from pagination to landing page. Switched color scheme, successfully installed theme dinky and played around with it.
8. 2013-11-12: fixed search problem by removing the "blog" concat thing
9. 2013-12-28: concat still not fied. need to check some syntax. Also added Gemfile. because indextank hasn't been updated in so long, have to stop yajl-ruby at 1.1.0

## TODO
1. switch to disqus for commenting. *DONE*
2. get top posts section
3. fix search, url doesn't work right *DONE*
4. allow organic presentation of blog posts, pinterest wall style?
5. related posts feature : https://github.com/LawrenceWoodman/related_posts-jekyll_plugin
6. make search more modular. move referneces only to search.html. requires fixing relative paths. 

## relevancy graph
1. get top 50-100 common words for each post
2. compare with other posts, make score between each pair the # of overlaps in common words
3. use chord diagram in d3.js

## Blog post ideas
* the importance of interests
* the big 21, the birth of a legend
* the importance of positioning, and brave new world conditioning you to like what you do
* technology keeps moving on
