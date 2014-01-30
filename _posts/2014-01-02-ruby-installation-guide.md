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
`rbenv install 2.0.0` and `rbenv global 2.0.0` and do `rbenv rehash`

5) Before using zanhealth, install following packages on ubuntu

6) At this point in time, do `which ruby` and see that it points to the .shim one. You may have to open a new terminal.

7) Install the following as well if you intend to use heroku rails on Ubuntu
```bash
sudo apt-get install libpq-dev
sudo apt-get install libsqlite3-dev
sudo apt-get install nodejs
```

8) Check that `which gem` points to the .shims one

9) Install the bundler gem `gem install bundler`. (Additionally do `rbenv rehash`)

10) Again do `which bundler`, it should point to your .shims one. If it doesn't, then you may have to remove a current installation of bundler by `rm -rf ~/.bundler`

11) `cd` into project directory that contains Gemfile

(Alternatively, you can use a rbenv plugin called rbenv-bundler which will separate all your gemsets. I didn't see the necessity yet, until I get dependency conflicts.)

12) If this is the case, install gems for bundle (should install rails if you have RoR project)
`bundle install`

13) Test server out
`bundle exec rails server`

