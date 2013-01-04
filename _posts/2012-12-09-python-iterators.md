---
layout: post
title: "python iterators"
tldr: "how python as a language implemented iterators."
tags: [iterator, python, cs173, programming languages]
---

How do different languages implement iterators?  
For those who have programmed in Java, Java requires an iterator class to implement Iterator interface
which has getNext() and hasNext() defined.

For python, there's no base class : iterator.  
sgord says it makes sense because there's really no shared functionality between iterators of different classes.

Instead, each class just has a specific iterator object for its class.  
In python, there exists list\_iterator, set\_ierator and dict\_iterator




