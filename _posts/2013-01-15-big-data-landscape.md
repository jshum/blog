---
layout: post
title: "big data landscape"
tldr: "A technological perspective of the big data landscape. Introduction of Hadoop, Vertica, ETL and Analytics market segment."
tags: [cs, big data, hadoop, vertica]
---
{% include JB/setup %}

[mbwong]: http://mbwong.com/2013/01/12/how-to-make-money-from-big-data.html

*This post is written from a more technological perspective. If you want a business perspective, take a look at my friend Michae's [post][mbwong]*

I spent most of the day browsing different big data sites. I keep telling people I want to work in big data but I haven't really looked at the industry offerings myself. 

**Motivation:** 
The first thing to talk about is why this big data revolution. I think there are a couple of reasons. A lot of things have become digital. Being digital means that data collection is a lot easier.  For example: a lot of applications are now delivered through the web and mobile so it's very simple to add a line of code where an application sends a data point to the server.  

[1]: http://www.capgemini.com/technology-blog/2012/06/nosql-hadoop/
[2]: http://www.capgemini.com/technology-blog/2012/09/big-data-vendors-technologies/
[3]: http://www.capgemini.com/technology-blog/2011/11/what-is-big-data/

**Definition of big data:**
The [common way to define it][3] seems to be volume, variety, need of velocity, or in other words petabtyes instead of gigabytes of unstructured data  
The four stages describing the flow of data is described [here][2] as  
acquisition -> marshalling -> analytics -> action

[4]: www.capgemini.com/technology-blog/2012/01/what-is-hadoop/
There is a lot of misconception that Hadoop = Big Data is but that is obviously not the case. Surely, Hadoop is used in a lot of big data stack but it doesn't equal big data. **What is Hadoop:** It is an open-source suite that tries to solve the problem of storing large amounts of data, possibly across lots of different machines. Hadoop is an open-source suite inspired by Google's MapReduce, GoogleFS and BigTable. Their Hadoop equivalents are HDFS, Hadoop MapReduce and HBase. HDFS is the file system, MapReduce is the thing that splits one request into smaller requests, HBase is a non-relational fault-tolerant database layered on top of HDFS. ZooKeeper is a centralized place to configure settings. Lucene is a search engine. You can interface with Hadoop using JDBC or you also use Pig, Hive which are languages for Hadoop.

[5]: http://wikibon.org/wiki/v/Enterprise_Big-data

**The parts of big data:** 
Let's return to the components of big data. Take a look at Figure 1 here. The technological developments in the storing of big data are mostly in databases and distributed systems. Since Hadoop has sort of been declared the winner by virtue of marketshare and by [these guys][1], there are unlikely major development that will happen on this front for a while. But there are still some battles being fought out now. One is SQL vs NoSQL.

The hype surrounding the buzzword NoSQL two years ago has mostly disappeared. SQL technologies has not at all disappeared as some have claimed. There is still impressive technology from the SQL camp. Another company that I've researched a little bit this past week is Vertica. They've written a relation database from scratch but with a few key optimizations that has given it some incredible benchmarks.

It's optimized for queries that mostly involve reading rather than writing. The optimial seems to be query consists of 10% writes.  The features it uses include:
1. Column storing
2. Row compression up to 90% deflation using  1. Key-hash style tabulating, 2. Delta values
3. Multiple projections
4. Hybrid store, read only store on harddrive, write only store in physical memory. Background process that batch moves the things in written only store to disk and recompressing things.
5. (Features:) physical database designer
6. (Features:) K-safe availability
 
But there are still market segments which are very fragmented. The first is companies dealing with ETL (extract transform load) stage. After extracting all the data, you need to transform it (remove duplicates, summarize it) and load it into a analytics database. Now, you can actually perform statistical tests on your analytics database which is hopefully optimized to be very fast.   

The other is the analytics segment.There is a natural desire for all analytic companies to move from reporting analytics to descriptive analytics to predictive analytics in order for Big Data to live up to the hype as being intelligent, and being able to inform and aid decision making. I predict this segment to continue to be fairly fragmented because it's more of a service solution rather than a technological solution. There are also a lot of possible niches to cater to business intelligence for different types of businesses. Some examples include web/mobile analytics, web/mobile/video advertising analytics, business-intelligence/consulting for different physical businesses. 

[6]: http://bigdatalandscape.com/

[bigdatalandscape.com][6] gives another, more feature-oriented description of the landscape from a business features perspective. For me, I need to take a look at all these different companies and decide perhaps the market segment I want to go into if I decide to enter this industry. My friend mbwong provides [a view][mbwong] on how to make money in Big data 

