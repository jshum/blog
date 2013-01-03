---
layout: post
title: "python iterators"
description: ""
category: 
tags: []
---

How do different languages implement iterators?
For those who have programmed in Java, Java requires an iterator class to implement Iterator interface
which has getNext() and hasNext() defined.

For python, there's no base class : iterator. 
sgord says it makes sense because there's really no shared functionality between iterators of different classes.

instead, each class just has a specific iterator object for its class.
so list define a list_iterator.




