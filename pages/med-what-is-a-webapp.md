---
layout: page
title: "What is a webapp?"
description: ""
---

This is a high level description guide of the components of a *webapp*. This is mainly intended for a non-technical audience so will not stick to any specific language or methodology. Instead, it will serve as an introduction to many of the buzzwords you will often hear technical people use. Many of the definitions, categorizations I employ are only rule of thumbs and are meant to help you see the big picture rather than serve as precise definitions. 

As a guideline, a webapp is as an application where all the interactions take place on the internet, on a URL, so there is no downloading of any software. The interaction should also be dynamic, meaning that it should not just be a presentation of information, but your interactions with the app should be able change the state of the application and it should respond accordingly.

Many of the URLs we go to everyday can be considered webapps, including but not limited to Facebook, Gmail. Note that it does not necessarily require the use of a database. For example : having a paint webapp which has no save function would not necessarily require a database. 

The application is usually *code* that sits on a *server*. The application code is the one that receives the user's actions and performs the right behavior if that means retrieving and returning the right data, changing the state of the application. If you want to have persistent storage, meaning that the data will stay even after the machine turns off, you have to write to disk (meaning the harddrive.) You can use textfiles, but reading and writing to textfiles require a lot of time because you can only add to the end of them. A *database* is software that has been optimized for reading and writing of data. There are multiple kinds of databases, but in general, people will use *relational database management system*, which you can think of as a fancier version of a spreadsheet (rows and columns).

Software development can be separated into frontend and backend. Frontend is everything you can see and backend is everything you can't. Another distinction that can be made for a webapp is client side and server side. Client-side is code that is received and executed on your browser and server-side is everything that isn't. 

Using an example, I will explain how the pieces fit together. Let's say you have a photo album webbapp, where you can upload and view all your photos. Let's say the photo album webapp stores your photos on a database. When you click the link to your photos, your client-side browser will submit a request to the server. The request is almost always an HTTP request (GET,POST). The request is received by the server-side application code. Then, the application code will determine what the correct course of action is. In this case, the application will talk to the database and obtain the set of relevant photos you want to see. The image files are sent back as the response of the HTTP request, and then the browser renders and displays these images to the user.

I will now go into a little more detail about each component of the entire ecosystem starting from the front.

Application Code :

There's multiple ways to organize your application.

The main building block of the internet are HTML pages. HTML pages aren't too difficult. It is a markup language, which just means there's some extra syntax to create formatting effects like bolding, aligning, numbered lists and tables and so on. The most basic website is just a collection of static HTML pages. 

Let's again return to the photo album webapp. Obviously, you can't create HTML page for every combination of photos before hand and serve the right one when the user asks for it. Thus, you need something dynamic, so you need a template for what the webpage will generally look like and parts of the website will change depending on what data the user wants to see. This is generally what dynamic webpages do. There are two ways to do this.

The first is having a server-side-heavy application, which means that all the dynamic loading of the data is done on the server, so then the browser only receives straight up HTML pages with all the data in it already.

The second is having a client-side-heavy application, meaning that the HTML pages you get are actually templates when you get them with no content. But as soon as you load the page, your browser makes a request for the relevant data, and then your browser renders that information into the blank HTML pages it originally had. Obviously, HTML itself doesn't have such capabilities which brings us to javascript, a scripting language that your browser is able to execute. Client-side-heavy application usually rely on a lot of javascript to do most of the logic. In this scenario, Javascript will send the appropriate request to the server to get the relevant data.

Why are the differences between these two options? 

Server-side heavy applications
* more flexibility
* less business logic is revealed to the user, because the user only receives HTML pages which are mostly visual. 

Client-side heavy applications
* less strain on the server, because client browser does most of the heavy lifting. Server only has to return the relevant data. (True in general, not necessarily true)
* Clean interface between front end and back end. Usually, people will choose to write APIs for the backend. This is immensely useful because this allows you to swap out the frontend to anything you want. You can have multiple frontends connecting to the same backend. 
* Obviously, if you make a change to an API, then everything will break.

There is a flame war as to which is better but these are all fad based. It isn't an binary option. Most apps are a combination of both methods. But it has increasingly become standard practice to choose the more client-side heavy application. This is because with a variety of form factors, it becomes too troublesome to have to determine what form factor the requester is before the page is created. With a client-side heavy application, the application will make the appropriate request denoting that it is a tablet, smartphone or whatever. 
APIs also make it easier for 3rd party developers to develop applications as well. Finally, if business logic is a problem, obfuscation to the javascript can be done.

Feature development on applications usually requires a coordination of two things. The database and the visuals. The correct tables need to be created in the database. The visual should have efficient and easy access to items inside the database for editing and displaying purposes.

The standard webapp architecture is called MVC framework (Model, View and Controller). Model is the database stuff, View is the visuals and Controller is the layer of glue in between. The visuals and database/logic should be as separate as possible so that either can be easily switched out. 

Backend :

As I said before, *databases* come in many shapes, sizes and forms. You want to choose the best tool for you. One of the greatest dichotomies in databases is between structured data and unstructured data. You can think of structured data as an excel spreadsheet. You know exactly how many columns you need for each row. Unstructured data is when there is a highly variable amount of information you need to store per data point. One example would be books, because pages/chapters/sentences are always of different sizes from book to book. 

Choosing the right database also depends on what your service requirements and what your workload is. Most people start off with a well-known RDBMS like MySQL or Postgresql, which have been optimized over decades of use. Then, they may pivot to other best databases as they understand their service requirements better. 

*Backups* are particularly important when users are trusting you with some important info. Backups usually requires you to take a snapshot of what is at the db at specific times. If the material is super important ie bank account balances, then backups usually happen by the second, or after every transaction so that no information is ever lost.

Developers don't develop on live code, meaning that when they change a file on their deskop, the webapp won't change accordingly. They usually first develop on their local environment (their laptop/desktop). Once they feel that the changes made are sufficient, they can start *testing*.

*Testing* is a really huge and important thing in software engineering. A well functioning webapp is like a well oiled machine that is entirely interdependent. If one little piece breaks, the the machines ceases to function. Thus, software engineers spend an incredible amount of effort to create test suites so that automated checking can be done. Testing varies from application to application. But testing should start from bottom to top, small to largest. You should test the smallest individual component first using unit tests, then test multiple components using integration tests, before final user tests. 

Once the app is thorougly tested, one can ahead and *deploy* it. Server side code has to reside on a server. In the old days, people used to have actual physical machines in their boxes. But that required too much hardware expertise and time. Today, there are multiple companies offering cloud hosting services meaning that they own the physical machines but will let you use those machines to host your application/code. Amazon EC2 is one of the most well known in the business for its low costs and wide range of offerings. Amazon offers what we call VPS (virtual private server) meaning that you have entire control of the machine. (In reality, they actually share a machine between multiple computers but they make it s that it seems like you have control of the entire thing). Heroku offers what we call cloud platform as a service meaning that you only have to give them code of a specific framework, and it will do the wiring in the back for you. Heroku is a good choice to start out with because it reduces a lot of the hassle, supports most popular languages, database types and has a wide range of add-ons. When, you scale in size, either the cost exceed your budgets, or your service requirements exceed their performance capabilities. 

Deployment tends to fall under system administration tasks. Once deployment is finished, the cycle starts itself again. But while the app is running, a lot of monitoring also still happens in the back. Machines fail. Harddrives fail, Motherboards fail. It's easy to monitor manually when you have 5 people working on 1 machine. But when you have 20 machines and 5 people talking to 8 different databases, then you have a attention focus problem. Most of the time, the monitoring is resource related. You want to understand what the strain of the current usage is on the available resources. The point of monitoring tools and automated alerts is to help us filter out all the non-essential parts. 

Finally, there also is logging, which is really similar to monitoring. My definition for logging is that the information is recorded and stored for later analysis or use. Logging can take many forms but can be in general divided into user-related or resources-related. User-related logging just looks for some way to get a cumulative understanding of how users are using the application. 

That is in essence the anatomy of a webapp development. Email `js at shumjason dot com` with suggestions and changes.  
