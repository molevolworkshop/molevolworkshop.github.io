---
layout: page
title: Total-evidence analysis in RevBayes
permalink: /software-revbayes-total-evidence/
---
This tutorial was developed for RevBayes workshops and users at home. Here you will find instructions for getting the files and for executing RevBayes on the MBL servers.

## Background Reading

* Höhna et al. 2016. RevBayes: [Bayesian phylogenetic inference using graphical models and an interactive model-specification language.](http://sysbio.oxfordjournals.org/content/65/4/726) Systematic Biology, 65:726-736.

* Höhna et al. 2014. [Probabilistic graphical model representation in phylogenetics. ](http://sysbio.oxfordjournals.org/content/63/5/753) Systematic Biology 63:753–771.

## Tutorial PDF

* The detailed tutorial on the RevBayes repository: [download](https://github.com/revbayes/revbayes_tutorial/raw/master/tutorial_TeX/RB_TotalEvidenceDating_FBD_Tutorial/RB_TotalEvidenceDating_FBD_Tutorial.pdf)

## Getting Started 

For this tutorial, most of the work can be completed on your own machines using your favorite text editor. Then, you need to move the script files you create to the MBL cluster and get the data files.

### Get the Data Files

On the course cluster, create a new directory for the tutorial analysis:

    mkdir RB_TotalEvidenceDating_FBD_Tutorial

Move to that directory:

    cd RB_TotalEvidenceDating_FBD_Tutorial

Get the data files:

    cp /class/molevol-shared/revbayesTutorial/data.zip .

If you encountered a bug making the MCC tree, one is in the class shared drive and can be accessed like so:

Get the data files:

    cp /class/molevol-shared/revbayesTutorial/bears.mcc.tre .

Unzip the data folder:

    unzip data.zip

Create a directory to hold your RevBayes scripts:

    mkdir scripts

### Transfer Your RevBayes Scripts

Move all of the scripts you wrote to the _RB_TotalEvidenceDating_FBD_Tutorial/scripts_ folder using Cyberduck or scp.

### Running RevBayes on the MBL Cluster

Execute RevBayes while inside _RB_TotalEvidenceDating_FBD_Tutorial_ and run your MCMC script as described in section 3.11 of the tutorial:

    rb
