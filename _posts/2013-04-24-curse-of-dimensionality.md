---
layout: post
title: "curse of dimensionality"
tldr: "the key reasoning behind curse of dimensionality"
nosocial : ""
tags: [ml, data, data science]
---

[1]: http://en.wikipedia.org/wiki/Curse_of_Dimensionality#Distance_functions

Dimensionality is an interesting thing. Math theorems are often generalized to higher or infinite dimensions to make more powerful theorems. 

It took us two years in high school to learn single variable calculus, but we're expected to learn multi-variable (two independent variables) calculus in a semester and Linear algebra, arguably n-dimensional math, also in a semester. 

Last semester I took a class where we learnt about computational probability and statistics. And computational probability basically involves a lot of Monte Carlo methods.

One of the problems that I remember that we had to do was approximate the volume of a specific small portion of a hypersphere.

The problem is that in high dimensions, the hypersphere is so large that it is unlikely even with a lot of samples that you will get a good handful of samples in the specific portion. 

People call this the 'curse of dimensionality'. Following is a fairly succinct synopsis about the problems of high dimensions from [Wikipedia][1]

>The common theme of these problems is that when the dimensionality increases, the volume of the space increases so fast that the available data becomes sparse. This sparsity is problematic for any method that requires statistical significance. In order to obtain a statistically sound and reliable result, the amount of data needed to support the result often grows exponentially with the dimensionality. Also organizing and searching data often relies on detecting areas where objects form groups with similar properties; in high dimensional data however all objects appear to be sparse and dissimilar in many ways which prevents common data organization strategies from being efficient.

[2]: http://upload.wikimedia.org/math/2/7/c/27c42cc52616ed4ba0b69b1c930e53a3.png
[3]: http://upload.wikimedia.org/math/0/6/1/061bfe5a98a8a6cb539062c7e2073ce6.png

I'm just going to summarize parts of the Wikipedia article
* combinatorial explosion, space grows exponentially.
    * even in the case of binary variables, combinations grows as O(2^d)
* running time overall increases because the objective function must be computed for each combination of values
* training data needs to grow exponentially as well so that the space has sufficient coverage
* distance functions : if we consider the volume of a hypersphere with radius r and dimension d compared to the hypercube, it is true that this portion goes to 0 as d goes to infinity. In other words, in nearly all of high-dimensional space consists almost entirely of corners of the hypercube with almost no 'middle', the hypersphere. 

There's this lemma that comes out of no where on the Wikipedia page attributed to [Bayer][3]. It doesn't make a lot of sense. 

There are multiple spots where it references that the L\_p distance metric is at fault.  I tried reasoning it with the unit cube, plotting the maximum and minimum distance in a unit cube. 
Maximum distance  is {1,1...1}. L2 dist = \root\_p{1^p + 1^p} = p^(1/p)
Minimum distance is eg. {0.1, 0.1 ... 0.1}. L2 dist = \root_p{p\*(0.1)^p}= p^(1/p)\*0.1

I plotted the function on wolframAlpha, I just got a curve that maxed out at 2 then slowly converged to 1. The min was the same but just one order of magnitude smaller. Basically, this was all to say my intuition didn't work and the reason must be a little more complicated.

Then, I started a crazy tangent reading up on the literature mentioned in the Wikipedia article.

[4]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.31.1422
[5]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.7409
1. First started with the person who proved that theorem, [Beyer][4]. They key theorem is that if the variance of the random variable divided by its expected value goes to 0 as the limit increases, the difference between the max and min distances becomes neglible.
    * I follow the math behind the proof but there's two things I don't understand: why add the limit m to infinity and why it has to be exponentiated to a constant p. 
    * The hardest thing to understand is that we have to find a sequence of random variables that has the property of converging to a constant vector. The examples in the paper are quite confusing and don't make any sense to me.
2.  This seems to be the only other [paper][5] which I've found which uses more concrete example but I still really don't understand what's going on there. It's somewhat confusing because you're trying at the same time to show that the distance metric converges to a constant before you can that it has this property of negligible difference between max and min distance.

[6]: http://www.cs.yale.edu/homes/el327/datamining2013aFiles/11_nearest_neighbor_search.pdf

[This][6] is lecture notes from Yale I suppose. It made sense but it also uses the hypercube example and doesn't really connect it all. 

I think there's two things going on here for curse of dimensionality
* need exponential number of training data points
* exponential time to search
* The simple distance argument is that nothing is close together because the hypersphere is so small, so you have to check other points. 
* But that only shows that some algorithms that worked in low dimensionality like kd-trees are not efficient anymore
* The thing I'm trying to wrap around seems a lot more powerful. They're claiming that there's something about the way the distance metric behaves as the number of dimensions increases that causes the max-min dist to tend to 0.


