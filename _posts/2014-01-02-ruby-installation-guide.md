---
layout: post
title: "Ruby Dev Env Installation Guide"
tldr: ""
tags: [cs, ruby, rails, code, dev, rbenv, bundle, install, setup]
---

Setting up local environment to run rails server with rbenv, ruby-build and dunble

Ruby benefits and suffers from a lot of dependency mangement so there are many tools out there to help overcome this. On the macro level, the major problem is ruby version dependencies and the two major tools are `rbenv` and `rvm`. On a project level, for solving gem dependencies, the best tool is `bundle`. The following is the guide I used to setup my RoR development environment.

Based on [source][source]

[source]: https://gist.github.com/MicahElliott/2407918
[1]: https://github.com/sstephenson/rbenv#basic-github-checkout
[2]: https://github.com/sstephenson/ruby-build
[3]: https://github.com/sstephenson/ruby-build/wiki

Ruby version management system

1)Install  rbenv. 
a) (Mac) Use brew `brew install rbenv`
b) (Linux) Use git. [Instructions][1]
	
2) Install ruby-build -  is an rbenv plugin that provides an rbenv install command to compile and install different versions of Ruby on UNIX-like systems.
    a) (Mac) Use brew `brew install ruby-build`
	b) (Linux) Use git [Instructions][2]

3) Install dependencies for various versions of Ruby
a) (Mac) + (Linux) : [Instructions][3]

4) Install desired version of ruby 
`ruby install 2.0.0`

5) Before using zanhealth, install following packages on ubuntu
```bash
sudo apt-get install libpq-dev
sudo apt-get install libsqlite3-dev
sudo apt-get install nodejs
```

6) `cd` into project directory

7) Install gems for bundle (should install rails if you have RoR project)
`bundle install`

7) Test server out
`bundle exec rails server`

