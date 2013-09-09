---
layout: post
title: "What Software Engineers do?"
tldr: "the three things software engineers need to learn, in increasing order of difficulty, various technologies, in-house codebase, management"
tags: [ cs, software, engineer, management, code, relationships, career]
---

What Software Engineers do? The simple answer that non-software engineers like to give is they write code.

But obviously the truth is a lot more nuanced than that. After working my internship this summer, I have some thoughts about what it means. Software Engineers have three major relationships to navigate and deal with, 1) with the technologies/tools they use 2) with the codebase, application itself and 3) with the organization they belong to.

####With technologies, tools####

(Regardless of organization)

I felt a little disillusioned during my internship searching process when it turns out that the software engineering is very buzz-word heavy too, and not as meritocratic as I had hoped. Simply having worked with certain tools makes you a lot more attractive than you would imagine, even though the job nature is heavily on-the-job training.

Tech changes every day. New open-source technologies are released every day, displacing old tech, and creating new buzzwords, frameworks and conventions. This cycle is particularly short in front-end development where every month there is a one new front-end JS library that everyone is using. But most people have beef with this, saying they jusy repackage the problem and put it somewhere else. The industry as a whole suffers from this, everyone solves the problem in a slightly different
way and claims massive benefits over other ways.

To put that into prespective, you have to analyze at all technologies as being on the hype curve. Demands for expertise of certain frameworks rise and drop dramatically over short periods of time. The key is to know enough to describe it on a high level, the situations which are most applicable for its use, but not worry too much about specific implementation details unless your job is 'subject x expert'. It is important to look back at the classics, the technologies that have remained after man years. 

But "you can't coast. you get burned in your ass if you do that". Technology keeps changing and rightly so. Technology is always going towards abstraction, making what was once hard easier.  It's still necessary to keep up if you want to stay relevant. I think it is necessary to dig under the covers to find out what is really happening, especially backend technologies, where the iteration speeds are much longer, because all of that has become fairly specialized. 

In my opinion, the experienced, mature software engineers are the ones who have the benefit of experience to pick out the technologies that are truly innovative and invest them into learning about those. 

####With the codebase####

(Specific to the organization)

Codebase sounds the same as technologies but I'm specifically referring to in-house technologies and tools. 
If you join any software company with existing code, you are inheriting legacy code which you have very little knowledge of. A codebase is a very specific Rube Goldberg machine. To add parts to this machine, you need to first understand everything it does, or everything that is affected by the part you will be working on. A lot of my onboarding was simply spent fitting the infrastructure inside my head, and learning the processes by which we did anything code-related, simply clicking
through source code to see how the code ran.  

But code is organic. It keeps being modified. It is logical like math, but it can become arbitrarily complicated, because the pieces are grown from a developer's relationship with it, a customers' relationship with it, and the interactions among different parts of the code. There is often a problem with legacy code in software engineering. Understanding the code base would take as long or longer than rewriting the whole thing in some cases, but no top-level executive is ever willing to
throw away legacy code because the new and original product will be different and the switch is always riddled with problems. It also means that all the money that was used to build the current code base has been gone to waste.

The senior,mature software engineers are the ones who are often able to abstract themselves away from the details, who can see how this class they are inserting will affect the entire code base. And every good CTO or even senior software engineer should be able to given a blank piece of paper draw out the entire technology stack from memory. They are the ones able to look at the existing code base and suggest software architectual changes that would make systems more modular, faster, cleaner. 

####With the organization####

(Specific to the peoplw within the organization)

[1]: http://en.wikipedia.org/wiki/The_Mythical_Man-Month

We still haven't automated humans out of writing code. The thing that is very different between writing code in school and writing for a company is the number of people who are working on the same codebase. The management of developers developing is difficult because each task is new/different and a different person working on the same task will have a different experience. Various workflow models have been suggested, agile, scrum, waterfall, test-driven. Each attemps to be more
effective than the past. In short, the [Mythical Man Month][1] has taught us that progress does not scale linearly with the number of developers you have, it's logarithmic or sublinear.

These skills are extremely hard to acquire. I don't expect software engineers to have this. The CTO should have a good understanding of the various capabilities of his team, assigning right tasks to the appropirate people in a suitable order so that they flow nicely.

In school, we write software following a very detailed spec according to a well thought-out planned-out assignment. Tech products on the other hand are messy. They have many stakeholders, and usually business considerations require things to be done in a way that is not suitable to future development. There are features that shouldn't really needed to be implemented if we knew this would happen before hand. Tech products have many stakeholders but engineers are the ones responsible for making them happen. Software Engineers are highly suspectible of being abused in the sense that they often have to do repetitive work that could have been avoided if there was more dialogue before work began, because often time they are more focused in the technology than the product.

A good software engineer should be able to open channels of communication with all the important stakeholders of the piece they are working in, usually with the product manager who asks as a proxy to the rest of the stakeholders. He/she should at least attempt to identify the key reasons for the feature/fix, and able to stand their ground, provide reasons and suggest alternatives if he/she does not sit this as an effective and appropriate measure. 
