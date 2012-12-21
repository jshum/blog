---
layout: post
title: "hastily written down"
description: ""
category: 
tags: [paper, uncollected, thoughts, cs,posterous]
---

Sheets 1
* Dremel
* Tenzing : SQL on steroids
* Google decision platform
        * analytical brains
        * big data analysis
        * PB: what kind of ads

Sheets 2
* Alignment
        * global, local, multiple, star alignment
        * affine gap penalities
* Pattern Matching
        * Motivation: BLAST : they do keyword search on hash table
        * local fitting alignment
        * pre-compute by solving pattern matching problem instead
        * KMP - linear time for one pattern in text
        * Multiple patterns in text, solving K pattern matching problems
        * keyword trees : all keywords go onto tree, sliding window along text
        * suffix trees: contains all substring of text. threads all patterns
        * Better approaches : spaced seeds, ignore errors
* Motif finding problem
        * pattern has length k, instnaces not necessarily identical
        * to find motifs that allow mutations, build distance
        * Formulation, give DNA sequence, find a set of motifs that maximizes consensus score
        * Suffix Tree for all:
                * regular all fits
                * select one which will give highest score
        * Brute Force: exponential number of combinations. (length of sequence)^( of setences)
        * Brute force: find all approxmiate matches of P in sequences. 4^l * #of strings * O(checkApproximateMatch)
        * Randomized algorithms
* HMM
        * see if in spectral region
        * evaluation, how likely is sequence, backward and forward
        * decoding, most probable sequence of states
        * learning, learn the parameters, find by doing maximum likelihood

Sheets 3:
* empty-env in python-setup, scopes in bind-arg, add a globalContext version
* necessary but better constructs for class checking in python-lib.rkt

Sheet 4:
* why the products are the way they are?
* where are they going now and in the future?
* something you like to think about all the time if you're PM.

ideal PMs
* smart
* interested in products
* thinking about landscape, technology, strategy to promote the value of product 

sheet 5:
* data science 
        * from development of algorithms and data to the applied side : econ data, corporate data, compbio data
* SE vs PM
        * exprts vs generalists
        * expert in some area vs team lubricant
* data industry 
        * stats & cs, data scientist, technical
        * economics & modeling, academic, simulating business data
        * industry stack, making corporations behave more scientifically
* statistical methods vary when you go from dense to sparse data, form Mb to Tb

sheet 6:
* jobs are the next stage of your life.
* realistic picture: jobs are hard to get
* try things, don't do the safe thing
* the cycle is try something, learn about it, reflect
* try to allocate your time efficiently, maximize your trying, learning
* who you are determines the culture fit
* your 20s are to be usd to figure out what you want to do, do w/ your life
* don't get stuck about doing the meaningful thing, just make sure you are learning what you want to learn
* don't stop thinking about what you want to do k, where you want to go until you're 30.
* you can only know what diff jobs do by doing it day in day out.
* optimize your life according to who you are. whatever you land in, you'll make the best out of it.
* it's all about opportunity. you can only locally optimize not globally optimize.
                
