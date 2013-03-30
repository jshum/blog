---
layout: post
title: "big data in the industry"
tldr: "all the big data developments will be driven by speed-ups in computation, rather than improvements in mathematical methods"
tags: [big data, cs, statistics]
nosocial: ""
---
I gave a process-oriented view of big data last time but let's take a look at it from a more big picture perspective this time. 

How should we best try to explain the term big data? 

Big data is statistics applied to large data sets. Statistics has been around for a bit but statistics applied at such a large scale is a relatively new thing. How large is large? Excel can handle tens of thousands of points in a spreadsheet. But large today is in the terabyte, petabyte range, tens of  millions of points. 

Statistics is a lot older than we think it is

Statistics as a mathematical field is quite mature already. Laplace was the first do a study on homicide rates in Paris in the 17th century. We've had data science for a long time. It's just that it's not been called that until very recently. In the past twenty years, it has been called Excel in the business world. 

I think I have incorrectly placed more emphasis on the word 'data' than on the word 'big' in my previous blog posts. But this correction has brought me two realizations: 

### a ###
Most of the challenges in big data are on the computational side. The big advances will be on the processing speed, on pushing the envelope on how much data we can process in a second, on how much of the process we can parallelize to speed things up.  

Most of the math has been developed already. Unless we're trying to do something very specific, the math stays the same. The big in big data is likely going to dominate future developments in the field. The developments in database in distributed systems, distributed databases are the ones that are going to be dictating the industry.

So what's the use of the statistics?

In a very general sense, it is to figure out the function that is outputting the data points. 
For retail sales data, it is to understand why people buy.
For web analytics, this means connecting user behavior and features of the site.

What are the purposes of data?
Here are some from a statician at Google:

Which brings me to my second thought.

### b ###
There really isn't that much need for new analytic methods in the industry, at least in business intelligence. As much as I would like, businesses are more likely going to use linear regression rather than k-means on their data.
The advanced methods of analytics will only come into use when we're trying to model complex relationships that aren't possible using simple methods, like in computer vision, computational-enabled something.

Methods are only as useful as their applications. Therefore, the only way to learn analytic methods is to go to study areas where they are needed. In some ways, this indirectly means that you have to go to grad school since the business intelligence sector is unlikely to required anthing that advanced. 

What does this mean about opportunities in big data though?

It's a difficult answer. I don't think a lot of people in this field know the answer either since data scientists roles in software companies are relatively new things. 
[mbwong]: http://mbwong.com/2013/01/12/how-to-make-money-from-big-data.html

This is a blog post from a friend [on the ways to make money in big data][mbwong]. You can figure out opportunities by understanding how money can be made in certain fields. 

The only way to figure out what the opportunities are and the skills you need for them is to read the job requirements and descriptions on careers pages. Talk to people who work in those areas. But even before that. 

Another very simple way to figure this out is to simply look at the page for LinkedIn's data team. Just scanning down and you'll realize that the roles are about half software engineering and half senior data scientists.

My hypothesis is that the industry has't figured out good training for data science yet. They've decided for now at least that PhD's in relevant fields are the best training, which is why most people have PhDs, thus senior data scientist titles.

Software engineering is definitely a possibility if you want to work in the data realm, but your expertise will have to be in databases and distributed systems. 

A link to another post I talked about software engineering. Software engineering is like building a bridge with tools and materials that didn't exist five years ago. And it also means maintaining the bridge and adding more flowers and bells. When the existing bridge becomes too small for the traffic, you have to rebuild it with tools that just popped up.

The nature of the job means you have to be learning all the time because things are always changing. The industry standard library/technology for doing a particular thing changes very frequently. And it scares me to consider software engineering because Mark Zuckerberg himself said" like young programmers more" 

Data scientist roles I think are a lot more difficult to get because they want you have the skills when you join the company already.

### edit March 4th, 2013 ###

I think there's two ways to join the big data industry. You join either as a   

i. statiscian  

* which means you need to have all the analytical skills already, likely accquired from a PhD.
* you should have at least produced some original research involving data analysis. 
* programming abilities matter but not to such a large extent. the pre-requisite is the necessary math

ii. software engineer

* be familiar with the current most popular computational model for doing things on large datasets. MapReduce, Dremel.
* have good software engineering chops.
* should start thinking about the whole flow of data and decide on a subarea you want to focus on. 

(iii. magic unicorns)
these are the magic unicorns jobs because they don't exist
* find a software engineering job which requires you to learn all the difficult mathematical techniques
* while still working in a fast-paced business environment and have exposure to the data products that work and don't. 
