---
layout: post
title: "Find majority element of random list"
tldr: "Three ways to solve the question Given a list of numbers, how do you find the one that is the majority of the list (, has more than N/2 elements in N size list)?"
tags: [cs, interview, algorithms]
---

*Given a list of numbers, how do you find the one that is the majority of the list (, has more than N/2 elements in N size list)?*

**1. sort then get middle number. Runtime: O(n log n)**

**2. quickselect, which is actually part of the quicksort algorithm. Gets the kth smallest number in unsorted list in O(n) time.**

a. Reminder of Quicksort:
1. choose pivot. put everything less than pivot in one list, and everything greather than pivot in one list.
2. recursively quicksort the two sublists.

b. Runtime Analysis of Quicksort:
1. comparing each sublist with the pivot value depends on size of sublist
2. then you call the algorithm on the sublist
3. the basic recurrence relation looks like *T(n) = 2\*T(n/2) + cn*

T(n) = 2\*T(n/2) + cn  
\= 2 \* ( 2\*T(n/4) + c(n/2) ) + cn  
\= 2^2\*T(n/4) +  2cn  
\= 2^2\* (2\*T(n/8) + c(n/4)) +  2cn  
\= 2^3\*T(n/8) +  3cn  
\= 2^k\*T(n/2^k) +  kcn  
Continues until n=2^k, in which case expression becomes  
\= nT(1) +  cn log_2 n  

Runtime Analysis for Quickselect  
T(n) = T(n/2) + n  
\= T(n/4) + n/2 + n  
\= \Sigma_0^k n/2^k   
\= n  
Because you know how many are less than the pivot and how many are greater than the pivot, you know exactly where the number is in the ordered list.  
Insight is that it only is performing partitions on log_2 n of the n partitions  

**3. And there is an algorithm called Boyer-Moore majority vote**  
a. Overview  
Iterate over the list. You need to keep track of the current candidate and a counter. The rules for updating both things are:
1. If the counter is 0, switch to the current letter.
2. If the counter is not 0, increment the counter if curr letter is same as curr candidate. decrement otherwise.

b. Informal analysis
1. I can think of three edge cases. 
2. If all occurences of majority-letter of them are grouped at the beginning of the list, since it's majority, counter will be greater than n/2 after all majority-letters, counter will still be non-zero until end even after all decrements.
3. If all are grouped at end of list, since it's majority, after going through all non-majority letters in the front, there will still be enough majority-letters to make the majority letter the current candidate
4. Interspersed: a b a b a. candidate and counter will be a:1 at the end

[1]: http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html

For a pretty good animation, check [this][1]

