---
layout: post
title: "statistics software"
tldr: ""
tags: []
---

[linux-r]: http://cran.r-project.org/bin/linux/ubuntu/README
[SO]: http://stackoverflow.com/questions/1097367/what-ides-are-available-for-r-in-linux
[overview]: http://brenocon.com/blog/2009/02/comparison-of-data-analysis-packages-r-matlab-scipy-excel-sas-spss-stata/
[2]: http://www.reddit.com/r/programming/comments/7fg6i/why_are_sasstata_the_default_statistical_tools/?sort=top

Taking a stats class which is making me learn Stata but I've heard R is the up and coming solution. Trying to figure out whether or not I should learn both or if it is hard to learn both. Installed R yesterday. Instructions on how to install R on ubuntu are [here][linux-r]

As for editors for R, RStudio is immensely popular on [SO][SO]

So I looked for some sources for comparisons.  Unless otherwise stated, this is all lifted from [this site][overview]

R       Library support; visualization  Steep learning curve
Stata   Easy statistical analysis       Costs money and closed-source  

Overview
* Two big divisions on the table: The more programming-oriented solutions are R, Matlab, and Python. More analytic solutions are Excel, SAS, Stata, and SPSS. 

R
* R’s is surprisingly good (Scheme-derived, smart use of named args, etc.) if you can get past the bizarre language constructs and weird functions in the standard library.

Stata and SPSS
* SPSS and Stata in the same category: they seem to have a similar role so we threw them together.  Stata is a lot cheaper than SPSS, people usually seem to like it, and it seems popular for introductory courses.  I personally haven’t used either…
* SPSS and Stata for “Science”: we’ve seen biologists and social scientists use lots of Stata and SPSS.  My impression is they get used by people who want the easiest way possible to do the sort of standard statistical analyses that are very orthodox in many academic disciplines.  (ANOVA, multiple regressions, t- and chi-squared significance tests, etc.)  Certain types of scientists, like physicists, computer scientists, and statisticians, often do weirder stuff that doesn’t fit into these traditional methods.


* SAS is used by something like 95% of Fortune 500 companies. There are very few jobs requiring someone to know R, although some industries obviously may have greater demand than others.[Reddit][2]
* But: is there ANY package besides SAS that can do analysis for datasets that don’t fit into memory?  That is, ones that mostly have to stay on disk?  And exactly how good as SAS’s capabilities here anyway? [Reddit][2]
