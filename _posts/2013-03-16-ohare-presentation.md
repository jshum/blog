---
layout: post
title: "ohare presentation"
tldr: "chicago ohare presentation"
tags: [cs, data science, airport, analytics]
---
{% include JB/setup %}

1. exploratory data analysis
   * trying to look for any interesting patterns
   * most of the data is concerned with time
   * if i was Chicago O'Hare airport, I would want to look at why my flights are being delayed
   * did a scatter plot matrix to see which variables correlated with which ones.
   * looked at the distribution in R, found some interesting patterns by conditioning on day of year
2. Try to do prediction
   * want to use something that is robust. Trying to predict whether an arrival will be delayed or not
   * can't cheat, so can only use the information that we know before the flight has taken off, i.e. CRSArrival, CRSDeparture, Distance, Carrier, Month, day of year
   * separated half of the data. test on half and train on the other half.
   * then trained logistic regression
   * got a curve that correctly predicted 75%
3. Reflection
   * Looking back, probably not such a great choice because already saw in the distribution by conditioning on day of year that it isn't a straight linear pattern 
   * Other interesting variables to condition on, Indicator for peak/non-peak season, how many flights on that day, whether the number of flights passed the critical value
   * better decision would have been to use Decision Tree, even more robust but would need to take some time to figure out what indicators or ranges to use
