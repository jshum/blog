---
layout: post
title: "data science job landscape"
tldr: "I talk about the reason of the reason for big data, how I see the available opportunities in the field and deciding what I think is appropriate to do at this point."
tags: [data science, data, cs, landscape, overview, industry]j
---

[9]: http://jshum.github.com/blog/2013/01/23/k-smallest/

I started off a [previous post][9] by sort of connecting the dots from my classes last semester.
I've mentioned before I want to work in big data and the past fall, I've tried to learn about the available openings in the industry. A lot of what I know is from my empirical experiences. It is therefore likely much of it will be biased, but I would love to hear from others.

[1]: http://mbwong.com

 At least from what I've seen lately, I think the hype for data scientists, which my friend [mbwong][1] had already warned me about a while back, is exaggerated. It's not apparent where the term data science came from but It's important to look at the context from which it arose. We started going digital when personal computers came around. The school secretary inputting student records into an early version of excel. When the internet came around, we could send the file to the local school board for them to add to their master student list. 

[6]: http://www.tracelytics.com/about-us

Every time we digitized something, it became a new data point. (Not to mention that machine generated data i.e. server logs, event logs are adding to this. A selfless promotion about [Tracelytics][6] a startup that intelligently monitors your logs to tell you if it is working properly. It was started by Brown alum. Automation and the digitalization of things plus the increasing reach of the internet created an explosion of data points. Instead of each Walmart branch doing sales figures for its own branch and submitting the findings, we now have all of the WalMart sales pumping into some data center at real time. These data sets were way too large for the conventional tools and called for the need of new systems and algorithms. 

[4]: http://jshum.github.com/blog/2013/01/15/big-data-landscape/

The technology is not that mature. I've talked about this before in [a previous post][4]. The data analytics portion of the market is still very segmented. The industry as a whole has only just developed somewhat mature systems that can handle the data warehousing i.e. Hadoop, which is only accomplishes the very first part of the whole big data process, storing. There simply isn't that much data that is conveniently available to be sliced and diced with various ML techniques. The next part is to build the ecosystem to support the data analytics. Information gathered from data mining and databases to store those as well. So that's the first reason. Most opportunities in the big data industry are still in distributed databases and systems which means the job titles even if they are writing distributed systems for large datasets will be called software engineers and not data scientists. 

Despite what some studies have found about how many data scientist jobs will be available in the next number of years, there don't seem to be that many on the market place yet. At the very least, entry level jobs in those areas are almost non-existent. 

[2]: https://www.facebook.com/careers/department?dept=engineering&req=a2KA0000000LjX4MAK 

A lot of the [job][2] descriptions I have read have at the very top of the requirements list:

> M.S. or Ph.D. in a relevant technical field, or 4+ years experience in a relevant role

[h2be]: http://www.quora.com/Career-Advice/How-do-I-become-a-data-scientist
[dplay]: http://www.hilarymason.com/blog/getting-started-with-data-science/

At first I was pretty disappointed but it took me some time to convince myself why this is true. I think [a lot][dplay] of people downplay how difficult it is to be a data scientist. You need to be well versed in the mathematics. This means traditional statistical analysis, machine learning (which some have argued to really be statistics with another name), and numerical methods that need to be used when the dataset is so large that the matrix representing it can't even be stored in memory. (This [quora answer][h2be] has provided to be invaluable in helping me choose classes.) Math is something you need to plonk down in a quiet place and learn.

[5]: http://www.wired.com/science/discoveries/magazine/16-07/pb_theory

 Math is also fairly universal. Unlike databases, you can't really develop proprietary machine learning algorithms.So in that regard, really what you need is to keep up with the research literature, in which case you want someone with a M.S or a PhD who knows the landscape well to navigate. Their job will also be a combination of reading newest research and re-implementing/tweaking algorithms they think can be used in industry. The math portions of the big data jobs are still in academia. There simply aren't code monkeys in data analysis.   

My APMA professor, Geman also reiterated that in contrast to [this Wired article][5] a lot of domain specific knowledge is still required. We don't yet have the math that will output the magic distribution given some data. A lot of what still needs to be done is to clean up whatever data you get, turn down the noise. 

The current challenge is to first build the systems that will run the algorithms at the desired scales, which is I decided to take O.S this semester instead of more math classes. Some interviewers had told me that that was what was missing from my resume.  

