---
layout: post
title: "oozie intro"
tldr: "One of the big three hadoop tools : Oozie"
tags: []
---

[vig]: viglink.com

Been using a lot of oozie this summer for my work at [Viglink][vig]

####One liner####

* Oozie jobs is a job scheduler through xml that creates and executes scheduled runs of analytics jobs, basically automating your analytics pipeline . 

####Overview####

[oozie-actions]: http://oozie.apache.org/docs/3.3.1/index.html#Action_Extensions

coordinator.xml is used to schedule runs of workflows. It defines when the workflows are to be run, whether at regular intervals, or when certain files appear in file directories. workflow.xml defines a workflow which is a DAG (directed acyclic graph) of mapreduce jobs, originally only Pig/Java/FileSystem jobs, but they have since added a bunch of [Action extensions][oozie-actions] and you can even write your own action extension. Finally, you have to define a *.properties files that gives the configurations to the workflow (but you can also define these inside coordinator.xml as <param>...</param>

####Submitting/Running jobs####

* oozie job -oozie <oozie/url>-config <job.properties> -run
  * will return a job id
*oozie job -kill <job-id>

####Checking job satutus####

* Oozie console - master-node-ip:11000/oozie/
  * Easiest to check the status of jobs here or you can do
* oozie job -info <job-id>

####Relation between job ids####

* <Coordinator job id>  = [0-9]+-[0-9]+-oozie-oozi-C
* Each instance of a workflow = <coordinator-job-id>@[0-9]
* Workflow id = [0-9]+-[0-9]+-oozie-oozi-W
* Then use mapped job -status  job_[0-9+]_[0-9+] to check status of map reduce jobs

####Notes####

* The apppath has to be an hdfs directory
* also parameters are case sensitive inside any scripts you use
  * You define lower case parameters in coordinator.xml
  * and uppercase in *.properties
