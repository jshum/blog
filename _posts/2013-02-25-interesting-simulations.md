---
layout: post
title: "interesting simulations"
tldr: "brainstorm on algorithm to find street corner to find optimal location to place food cart"
tags: [cs, data science, simulation, statistics]
---

Setup
* Client: food cart, street vendor
* Goal: write program to find out what street corner is the optimal location to place the card

Steps
* Come up with the metrics that need to be measured
* Build the corresponding data structures and algorithms for it

Approach #1: Simulation
* buildings are nodes
* street corners are also nodes
* streets are weighted directed edges, based on some function of distance, factors like closeness to other restaurants, transportation stops
* buildings have people in them. each person has some probability distribution of visiting a street depending on its weight

Algorithm
* for every each timestep t
   * for each node  
      * get list of streets streetcorner is connected to
      * get the building's outflowing population at time t
      * get the number of people going on a particular street depending on the distribution
      * update the count of every street corner (probably a temporary value, since you want to simulate discrete time units and separate each iteration of t)
* store the state of the graph at this point. 
* after t iterations, sum the results or show how it changes.

Problems
* becomes Brownian motion because 'people' don't stop walking unless we make each person into an object with some record of how far it walks
* can't really codify competitors

Approach #2: Slightly More Analytic
* imagine we had at the population level a distribution on how far people will walk

Algorithm
* for each building (since we can assume people from same building are same distance away from everything else)
   * for each corner
      * calculate the the probability of the people that will go
      * update the corresponding value for the street corner for a hashtable

Suggestions
* how to codify competitors: have the distribution of a street corner change based on the complemtnary relationship between two restaurants. something like a correlation coefficient.

         
