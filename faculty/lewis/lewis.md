---
layout: page
title: Paul O. Lewis
permalink: /faculty-lewis/
---
{% include figure.html description="Paul Lewis" url="/faculty/lewis/img/300px-Irobot.jpg" height="300px" css="image-right" %}

### Arrival and Departure

May 25 to June 6

### Contact Info 
E-mail: [paul.lewis@uconn.edu](mailto:paul.lewis@uconn.edu)

Address: Department of Ecology and Evolutionary Biology, University of Connecticut, 75 N. Eagleville Road, Unit 3043, Storrs, CT 06269-3043 U.S.A.

### Institutional home page 
[http://phylogeny.uconn.edu](http://phylogeny.uconn.edu/)

### Lecture Materials 

Lecture slides will be made available before the lecture, but maybe _just_ before.

#### Likelihood lecture (28 May 2022)
{% comment %}
* [Likelihood lecture slides (part 1)]({{ site.baseurl }}/faculty/lewis/pdf/lewis-likelihood-part1-2022-opt.pdf)

#### Likelihood lecture (29 May 2022)
* [Likelihood lecture slides (part 2)]({{ site.baseurl }}/faculty/lewis/pdf/lewis-likelihood-part2-2022-opt.pdf)

#### Model selection lecture (3 Aug 2019)
(Paul presented on this topic in the 2019 course; ordinarily this topic would be covered by David Swofford.)
* [Model selection slides](http://hydrodictyon.eeb.uconn.edu/people/plewis/downloads/wh2019/models.pdf)
{% endcomment %}

#### Bayesian lecture (29 May 2022)
{% comment %}
The link below leads to the 2019 version of the lecture. 
* [Bayesian lecture slides (part 1)]({{ site.baseurl }}/faculty/lewis/pdf/lewis-bayesian-part1-2022-opt.pdf)
* [Bayesian lecture slides (part 2)]({{ site.baseurl }}/faculty/lewis/pdf/lewis-bayesian-part2-2022-opt.pdf)

Here are a few slides that I use to explain how the Poisson probability formula arises (they help explain how the constant e sneaks into the JC69 transition probability formula):
* [Poisson slides](http://hydrodictyon.eeb.uconn.edu/people/plewis/downloads/wh2012/Poisson.pdf) (7 pages, 516 KB, PDF format)

MCMC Robot used in Bayesian lecture:
* Free iOS or Windows app available from the [http://mcmcrobot.org/ MCMC Robot web site]
The version of MCMC Robot I used in lecture is available at [http://phylogeny.uconn.edu/mcmc-robot/](http://phylogeny.uconn.edu/mcmc-robot/). Click outside an existing hill to move the starting point for a chain, and drag in an area outside a hill to create a new hill. Clicking on a hill to select it should allow you to delete it using the delete key. (It is currently easier to delete and recreate a hill than it is to change the diameter of an existing hill.)
{% endcomment %}

#### C++ Bayesian Phylogenetics Software Tutorial
If you took John Huelsenbeck's morning C++ class, you may wish to continue learning by working through this [http://phylogeny.uconn.edu/https://phylogeny.uconn.edu/tutorial-v2/ | C++ Bayesian phylogenetics tutorial]. This tutorial starts by teaching you how to set up your Windows or Mac laptop for compiling C++ programs and then explaining each step until you have a functioning Bayesian MCMC sampler for inferring phylogenies or estimating parameters of evolutionary models.

#### The Chain Swapping Question
During my demonstrations of the MCMC robot app, the question that is always asked is the following: Why does the swapping pattern of the cold chain appear concentrated between two of the three hills in the landscape; why is swapping not uniform and symmetrical between all three hills? The top figure below illustrates the pattern, with large magenta dots showing where each of the 3 chains are at the current time.

{% include figure.html description="" url="/faculty/lewis/img/MCMCRobotAsymmetrical.png" height="250" css="image-left" %}

As you can see, swaps seem to avoid one pair of hills in the landscape. One key clue is also shown by this (top) figure: the 3 robots are not evenly distributed with 1 per hill. Instead, one hill currently has 2 robots, and another hills has just 1, and the third hill has 0 robots. While this configuration of robots persists, all swaps will be between the 2 hills that have robots, and a "rut" between these hills will develop. Eventually, one of the robots will manage to get over to the hill with no robots (note that this is hard because swapping does not help with this process), and swaps can then begin again to accrue to this third hill.

About 1/5 of the time, the 3 robots should all be on different hills (see the lower figure), and thus only 1/5 of the time should we expect to see symmetrical swapping.
{:style="clear:both"}

{% include figure.html description="" url="/faculty/lewis/img/MCMCRobotSymmetrical.png" height="250" css="image-left" %}

Thus, we should expect ruts to develop, and it is not a problem because even in the top figure the cold chain robot is easily able to move between all three hills.
