---
layout: page
title: Peter Beerli
permalink: /faculty-beerli/
---
{% include figure.html description="Peter Beerli" url="/faculty/beerli/img/Peter.jpg" css="image-right" height="250px" %}

## Institutional home page

[http://people.sc.fsu.edu/~beerli](http://people.sc.fsu.edu/~beerli)

## Arrival and Departure

May 22 - June 2, 2025

## Lecture Materials

Note: *The presentations may change up until the moment the lecture or lab begins. I will try to post the modified the PDF before the lecture but will post the actual talk-PDF after each talk.*
<!-- , and Laura Kubatko will follow and talk about speciestrees/genetree estimation. -->

Coalescence lecture (Monday, May 26 2025): I will introduce the coalescent and its use for population genetics inference. The first section of the lecture will discuss basics;  in the second part I will discuss extensions of the basic coalescent. I will focus on neutral population processes, such as population structure, population size changes through time, population divergence, and problems and complications with inferences using the coalescence.

* May 26 (14:00-15:30): Introduction to the coalescent [Coalescence2024-talk1]({{ site.baseurl }}/faculty/beerli/pdf/coalescence1-mbl2024.pdf) (talk given earlier: [Coalescence2018-talk](https://peterbeerli.com/workshops/mbl/2018/talk1.pdf))
* May 26 (15:30-17:00): extending the basic coalescent [Coalescence2024-talk2]({{ site.baseurl }}/faculty/beerli/pdf/coalescence2-mbl2024.pdf)
* May 27 (9:00-12:00) *MIGRATE* tutorial and evolutionary model selection beyond mutation models, specific tutorial instructions [Tutorial-Intro]({{ site.baseurl }}/faculty/beerli/pdf/bayesfactor_presented2024.pdf) [Tutorial]({{ site.baseurl }}/faculty/beerli/migrate-tutorial-html/MIGRATEtutorial2023.html)

## Teaching Tools
{% include figure.html description="Wright-Fisher Model" url="/faculty/beerli/img/Wf.png" css="image-right" %}

* [Bugs_in_box](https://github.com/pbeerli/bugsinbox/archive/refs/heads/main.zip) is a python3 program that visualizes coalescence of bugs (well they are ladybugs and beetles) in a box. They crawl like crazy until they hit another bug, devour it and move on. There is a help menu (press H) that displays all options. This application has a few shortcomings: (1) it does not adjust well for different screen size (for example presentation beamers make the bugs huge); (2) No way to save or print directly out of the app, but Dave Swofford contributed a fun spin when there are two bugs left (see help menu in python bugsinbox.py).
* [PopVizard](https://github.com/pbeerli/popvizard/archive/refs/heads/main.zip) is a python program that allows to plot pictures of population genealogies like the ones on this page.

## Demo and Tutorials
{% include figure.html description="Canning Model" url="/faculty/beerli/img/Canning.png" css="image-right" %}

* [Population-model selection using MIGRATE on May 27 2025](http://peterbeerli.com/workshops/mbl/2024/tutorial). The tutorial guides you on estimating the most likely path of the Zika virus and discusses estimation of divergence times, gene flow, and model selection with MIGRATE 5.0.6. An older gene flow tutorial using the older version of migrate 3.x: [PDF](http://peterbeerli.com/workshops/mbl/2018/tutorial)).
* If students are interested I am also happy to talk about LAMARC and give a [Lamarc tutorial](https://molevol.mbl.edu/index.php/Lamarc_tutorial): Recombination estimation with LAMARC

## Bayes factors and effect of parallel runs of MIGRATE
{% include figure.html description="Moran Model" url="/faculty/beerli/img/Moran.png" css="image-right" %}

<!-- This year I will have less time to introduce Bayes factor analysis in MIGRATE (but you will hear about them in Paul Lewis lecture). I gave in 2011 this lecture:-->

* [Lecture on Bayes factor](http://people.sc.fsu.edu/~pbeerli/mbl2011_BF.pdf) that may help to understand the tasks in the MIGRATE lab.
MIGRATE can run on many different operating systems and hardware, most efficiently it can run on computers that have more than one core (almost all these days) using parallelization:

* [Lecture on parallel installation of MIGRATE and Slice sampling](http://people.sc.fsu.edu/~pbeerli/mbl2011_migrate_parallel.pdf).

### Even more talks on the coalescent

* [Several shorter talks on the coalescence](http://people.sc.fsu.edu/~pbeerli/Beerli_Lab/Talks.html)

### Software demonstrated in the course

[Migrate software](https://peterbeerli.com/migrate-html5)

## Other things I like

{% include figure.html description="Frogs and Toads"     url="/faculty/beerli/img/Frogs.jpg"          css="image-left"  targeturl="https://www.instagram.com/polliwoggles/" %}
{% include figure.html description="Mountains" url="/faculty/beerli/img/Mountains.jpg"      css="image-left"  targeturl="https://www.google.com/maps/place/S%C3%A4ntis,+9658+Schwende,+Switzerland/@47.2446468,9.343465,2611m/data=!3m1!1e3!4m2!3m1!1s0x479b264935825f1b:0x1df3ca80897719ba" %}
{% include figure.html description="Cooking"   url="/faculty/beerli/img/Tatsch.jpg"         css="image-left"  targeturl="https://peterbeerli.com/downloads/misc/tatsch.pdf" %}
{% include figure.html description="Art"       url="/faculty/beerli/img/Scherenschnitt.jpg" css="image-left"  targeturl="https://lubieler.com" %}
