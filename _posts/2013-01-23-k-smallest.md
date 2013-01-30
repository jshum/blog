---
layout: post
title: "k smallest"
tldr: "I start by writing out the solutions to an interview problem I was given. Then, I mention the connection that systems are just algorithms compounded together. Connect the dots with programming languages at the end"
tags: [algorithms, systems, class, academics, cs]
---

1. Given a list of integers, how do you find the k smallest numbers?

*1. sort it in ascending order, and then take the first k*
Runtime: O(n log n + k)
*2. iterate over list while keeping track of a list of the smallest k numbers encountered so far*
Allocate an array of k numbers, and also a variable max_k that will be the largest number in the size k array.  
Fill up the size k array in the first k iterations and sort them.  
At each subsequent iteration, compare current element and max_k.  
If curr. ele. is less than max_k, insert current value into the sorted list (similar to insertion sort). Updated max_k.  
Else, move on.

Analysis: for each iteration, takes at most k steps to insert new value.  
Runtime: O(n k)

*3. minor modication on the previous one by using a max heap*
Instead of using a size k array, create a max heap.  
At each iteration, peek the max and compare with current element.  
If curr. ele is less than max_k, pop and max and insert the current element into the heap.

Analysis: for each iteration, deleting and inserting elements take O(log k) each.  
Runtime: O(n log k)

*4. quickselect, which is actually part of quicksort algorithm.*

[1]: 2013/01/17/cool-interview-question/
An introduction of this is already provided in a previous [post][1] but the runtime is essentially O(n). 

This is a classic example of algorithmic analysis. You have some computational problem and you're trying to come up with some set of instructions that accomplishes the goal. Then you count how many "steps" each algorithm takes and iteratively improve.

Computer Science as a field has a very good hold on these algorithmic problems. We have developed a lot of tools and methods to discuss algorithms. When the problem involves multiple algorithms, we call this a program. For programs, we can still usually add all the runtimes together for a somewhat clear picture on the performance. When you have to support multiple commands, then this is a system. The analysis becomes difficult because there are a lot of moving parts. 

(Following was lifted from the first lecture of the fundamentals of computer systems class)

Why are systems hard?
* hard because of emergent behavior, behavior that only becomes apparent when all pieces are put together. Therefore, these are hard to predict.
* propogation of effects, butterly effect.
* bottlenecks change when systems are scaled

What is complexity?
* large # number of components, depdencies, features, irregularities (corner cases), people managing, interactions between components
* lack of compact description

Principle of escalating complexity states that as the number of features increase, the complexity increases exponentially. Idea is that interactions between componenets make their combined behavior hard to model and predict. Related ideas incldue law of diminishing returns and excessive generality. 

There's a subtle but important difference between trying to add a feature to some module that already does something well and trying to consturct a system from scratch that does many different things. In the first case, you could end up creating complexity by introducing interactions that the system wasn't designed for. Obviously complex systems need to be built but they can be architect in a way that avoids emergent behaviors. The two guiding principles are modularity and abstraction. Organizing and combining features logically into stand-alone entities, modules. Building abstractions so that implementation can be hidden from the interface, also benefits information hiding and functional clarity. 

 
We've only started writing big systems in the past decade. We haven't had operating systems for very long. It's only since the internet and the proliferation of web apps is where we've seen now lots of "complex" systems. I've heard a lot of people and a great [reddit discussion][2] mentioning the software crisis and I think they are referring to this. Software is given a lot more leeway than things like infrastructure and medicine. In that regard, software engineering is still very young as an engineering field. We don't really know what the critical points of failure are. Unlike structural engineers who can tell you exactly how much load some building can sustain, we don't really know that about our programs. Bugs  are really the manifestations of what you think your program does but doesn't actually.  

Part of what I learnt from programming languages last semester or what my professor was trying to advocate is that functional languages are a lot more powerful in the sense they hide away a lot of the details. This allows you to focus on the higher level ideas, providing yet another level of abstraction. Recursion itself also provides a much better mathematical analogue for proving properties about your program. 

[2]: http://www.reddit.com/r/programming/comments/16qbxn/if_carpenters_were_hired_like_programmers/c7ykc1m?context=2
[3]: http://thismyonelife.wordpress.com/2012/08/05/computer-science-thoughts-before-the-fall/

I guess that sort of ties it in together with [this post][3] I wrote before the beginning of last semester. I ended up dropping Topics in Logic: Incompleteness after realizing I really didn't have any of the pre-requisite knowledge. I ended up taking an easier Intro to Logic, which I enjoyed a lot more. And I've descending from the lofty heavens of computability theory and am going to take more practical systems courses. More on that [later][4]. 

[4]: http://jshum.github.com/blog/2013/01/29/data-science-job-landscape

