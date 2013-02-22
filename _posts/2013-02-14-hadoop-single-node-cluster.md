---
layout: post
title: "Hadoop single node cluster"
tldr: "resources to install Hadoop on your local machine"
tags: [hadoop, big data, cs, distributed systems, guide, tutorial]
---

[hadoop-tutorial]: http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/
[hadoop-java]: http://wiki.apache.org/hadoop/HadoopJavaVersions
[hadoop-config]: http://hadoop.apache.org/docs/current/cluster_setup.html#Configurationml

[Hadoop Tutorial][hadoop-tutorial]

I follow the hadoop tutorial to install hadoop on your local machine.

**Setup:**
* Download Java. It recommends sun-java but openjdk-java can also be [used][hadoop-java].
* Add a user and group specifically for Hadoop on your machine, hduser and hadoop respectively
* Hadoop requires SSH access to manage its nodes, i.e. remote machines plus your local machines if you want to use Hadoop on it. (interesting. didn't think they would use ssh as the network protocol. 
* Configuring ssh so hduser can access localhost (itself) since we're only doing single node cluster
* Disabling IPv6 which is apparently a problem.

**Install Hadoop**
* Download hadoop from one of the mirrors (surprised they still download by release instead of an apt repository ?)
* Unzip it, I installed it in /usr/local/hadoop
* Also chown -R it so that the user and group of all the files are hduser and hadoop
* Add some configurations to .bashrc of hduser
* Change JAVA_HOME in /usr/local/hadoop/conf/hadoop-env.sh
* Add configurations to conf/\*-site.xml . These are just the configuration files. You will see that the job.tracker or fs.default.name will be localhost since we're just using one node.
* For more info, I think I will read [this][hadoop-config]

**Start Hadoop**
* /usr/local/bin/hadoop/start-all.sh
* /usr/local/bin/hadoop/stop-all.sh
* jps - tells you what Java processes are running, similar to ps

**You can now use Hadoop**
* There are some examples that come with hadoop in /usr/local/hadoop/hadoop-\*.\*-examples.jar
* There is dfs and fs, they're basically the same. Just file system commands
* Copy data from local machine to HDFS using fs - copyFromLocal /tmp/gutenberg /user/hduser/gutenberg. (the second one is actually a path on the "virtual" HDFS)
* Run the job bin/hadoop jar hadoop\*examples\*.jar
* To retrive the results use bin/hadoop dfs -getmerge /user/hduser/gutenberg-output destdir

**Monitoring**

* You can check the status by using these
* http://localhost:50070/ – web UI of the NameNode daemon
* http://localhost:50030/ – web UI of the JobTracker daemon
* http://localhost:50060/ – web UI of the TaskTracker daemon

**Next steps**
* Write some map/reduce jobs
* Figure out what's happening under the hood.
* Learn to type Hadoop instead of Haddop
