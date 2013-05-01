---
layout: post
title: "matlab idiosyncrasies"
tldr: "the pluses and minuses of matlab and what to pay attention for"
tags: [matlab, cs, code, programming]
---

matlab idiosyncrasies

* MATrix LABratories, written with a backend in c. started as an replacement package that was easier to learn than Fortan
* MATLAB is popular among image processing crowd because images are really just matrices of color values.

pluses

* Matrix, no loops
* has in-built support for matrix operations with normal operators \* and \\
* debugging is easy, just remove the semicolon
* plotting is super sick in MATLAB.
* you can write extremely terse code in matlab. we had a QWOP simulation with about 20-30 lines of code

But it sort of bits you in the behind when you don't pay attention

minuses

* the benefits are actually the source of the problem
* MATLAB doesn't tell you when it does scalar/matrix operations
* depends on the variable after the operator if it's a scalar or a matrix
* A/B = A\*B^-1 , which is terrifying when you want it in the scalar case
* built-in functions have confusing syntax

Some of the built-in functions are also very confusing. I was trying to get a random value between 1 and 3 and wrote randi(1,3). It took us forever to figure out that the syntax for that was actually randi(\[1,3\]). What it gave us was a 3 by 3 matrix of 1's. The problem isn't so much matlab itself but user behavior that often assumes an unrelated part of the program is at fault.

There is also this question of optimizing your code. There is a non-trivial performance increase when you write your code using matrix operations rather than loops. But then you have run the risk of getting unintended effects of using the operators.

Then, you have catch-22 of whether you should optimize or not optimize because writing fast code lets you troubleshoot faster, especially important if you're running a
fairly complicated program. At the same time, it very likely increases the number of bugs.

Debugging is frustrating because there will be lots of little things like that like matrix sizes, the wrong index being reused that lead to really dumb but incredibly difficult to find bugs. Just by the complex nature of programs that tend to be written in matlab, it's hard to debug because it's really hard to make easy test cases with matrices.

So I've decided from now on to first write all my code in loops. Make sure the code works before I vectorize it.
