---
layout: page
title: Paul O. Lewis
permalink: /faculty-lewis/
---
{% include figure.html description="Paul Lewis" url="/faculty/lewis/img/300px-Irobot.jpg" height="300px" css="image-right" %}

### Arrival and Departure

* Arriving: May 22, 2025
* Departing: June 1, 2025

### Contact Info 
E-mail: [paul.lewis@uconn.edu](mailto:paul.lewis@uconn.edu)

Address: Department of Ecology and Evolutionary Biology, University of Connecticut, 75 N. Eagleville Road, Unit 3043, Storrs, CT 06269-3043 U.S.A.

### Institutional home page 
[https://phylogeny.uconn.edu](https://phylogeny.uconn.edu/)

### Lecture Materials 

#### Likelihood lecture (23 May 2025)

* [Likelihood lecture slides]({{ site.baseurl }}/faculty/lewis/pdf/lewis-likelihood-2025.pdf)

#### Bayesian lecture (25 May 2025)

* Slides for the Bayesian introduction lecture coming soon...

The version of MCMC Robot I used in lecture is available at [https://plewis.github.io/applets/mcmc-robot/](https://plewis.github.io/applets/mcmc-robot/). Click outside an existing hill to move the starting point for a chain, and drag in an area outside a hill to create a new hill. Clicking on a hill to select it should allow you to delete it using the delete key. (It is currently easier to delete and recreate a hill than it is to change the diameter of an existing hill.)

{% comment %}
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
{% endcomment %}
