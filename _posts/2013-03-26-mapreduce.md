---
layout: post
title: "mapreduce"
tldr: "Simple synopsis of the original Mapreduce paper"
tags: [mapreduce, cs, hadoop, google, paper ]
---

[1]: http://research.google.com/archive/mapreduce.html
As we all know, Hadoop is kind of a big deal right now so I thought I would read the paper that inspired it all, [MapReduce: Simplified Data Processing on Large Clusters][1]. 
This is the first comp sci paper I've read through by myself. I'm trying to write a short synopsis of it to serve as a short textbook.

Readthroughs
1.  March 25, 2013

Motivation
* most data centers are made up of large clusters of commidity hardware
* what is the most optimal way to distribute a large job over this cluster for performance?
* things you have to consider are load distribution and
* mapreduce borrows two paradigms often used in functional languages. 
`
(map (f : (k1 -> k2)) (list : (listof k1))) : (listof k2)
(fold/reduce (g : (k1 (listof k2) -> (listof k2))) (base : (listof k2)) (list : (listof k1)))
`
But in MapReduce
* map : (k1, v1) -> list(k2, v2)
* reduce : (k2, list(v2)) -> list(v2)

* The two parameters of mapreduce are M, R  

The flow of MapReduce is
* MapReduce library first splits the input files into M pieces. It then starts up many instances of MapReduce on the different computers on the cluster
* One of the workers is the master (Cloudera's Hadoop now supports high availability 2012). The rest are workers that are assigned work by the master. There are M map tasks and R reduce tasks to assign.
* Worker who is assigned a map task reads the contents of the corresponding input split. Parsers the k,v pairs out of input and passes each pair to the user-defined Map function. The intermediate k,v pairs produced by the map function are buffered in memory
* Periodically, buffered pairs are written to local disk, partitioned into R regions by the partioning function. The locations of these files on local disk are passed back to master, who will need to forward these to reduce workers
* When reduce worker is notififed by the master, it uses remote procedure calls to read buffered data from the local disks of the map workers. When a reduce worker has read all intermediae data, it sorts it by the intermiediate keys so that occurences of the same key are grouped together. 
* Reduce worker iterates over the sorted intermiedate data and for each unique intermediate key encoutnered, passes the key and corresponding set of intermediate values to user-defined Reduce function. output of reduce is appended to one of R final output file

Example : word count (used in paper)
* split all input files into M pieces
* for each piece, run it on the following function
`
map(key,val)
//key : doc id
//val : doc content
for word in val
	emit(word, 1)
`
* for each worker, split output into R pieces. let's say R=4. so {(a-g), (h-n), (o-u), (v-z)}
* for each reduce worker number i, read all M of the i-th out of R intermediate files. Sort it so that they can be partitioned into intermediate keys and list of values
* Pass each of the intermediate keys to the user defined reduce function
`
reduce(key, list(val))
//key : word
//val : count
result = 0
for each val:
	result = result + 1
`
* finally output all results

Complexity bound
* time bound : O(M + R) scheduling decisions for the master. The bottlenecks of mapreduce are the latency of remote reads and the time on sorting large sets right? 
* space bound : O(M * R)
