---
layout: page
title: Machine learning tutorial
permalink: /machine-learning-tutorial/
---
# Introduction

In this activity, we will apply machine learning to a simple question in population genetics. Specifically, we will simulate data under two simple demographic models using msprime. Then, we will calculate Site Frequency Spectra (SFS) from these data, and store them as numpy matrices. We will use these matrices to train a convolutional neural network (CNN) using tensorflow and keras. Finally, we will generate an independent test dataset and test the classifier. This is a simple example that could be solved without using machine learning, but it should illustrate the basic principles of using machine learning in python to analyze genomic data.

## Activating your python environment

In order to gain access to the python libraries needed for this tutorial, you will need to activate your python environment. Issue this command from your bash prompt on your virtual machine:

    source /var/pyenv/bin/activate
    
You will need to use the python3 executable inside your python environment (_/var/pyenv/bin/python3_) each time the instructions below ask you to invoke python. This is because the libraries needed by the tutorial are only available inside this python environment, and, if you use the default python3 executable (i.e. _/usr/bin/python3_), it will not look in the right place for those libraries.

Rather than typing _/var/pyenv/bin/python3 Machine_Learning_for_Population_Genetics_V2.py_ each time you need to run the python script used for this tutorial, you can make an alias that will do all that typing for you:

    alias runml="/var/pyenv/bin/python3 Machine_Learning_for_Population_Genetics_V2.py"
    
Note: this alias will exist only until you exit your current terminal session. To make the alias permanent (probably not necessary in this case since you will only be doing this tutorial once), you would need to add the above command to your _.bash_profile_ file so that it is executed each time you open a new connection to your virtual machine.
    
## Navigate to the _machinelearning_ folder

Use the `cd` (change directory) command to position yourself inside the _machinelearning_ folder where the files for this tutorial are located:

    cd ~/moledata/machinelearning
    
## Simulating genetic data in msprime

There are many simulators we could use to simulate data, and different problems require different simulators. For example, when we want to simulate selection, SLiM (Haller and Messer, 2022) may be a good choice. In this simple example, we will use msprime (Baumdicker et al., 2022). msprime integrates well into python pipelines, since it is a python package. It is also used in stdpopsim, a library for standardized population genetic simulations for many species (Adrion et al., 2020). We will keep it simple for the point of illustration and simulate data under two models: a divergence-only model and a divergence-with-gene-flow model. Our question is: do these two sister species have a history of gene flow?

{% comment %}
The figure.html referenced below is in the _includes folder 
{% endcomment %}
{% include figure.html description="Demographic models" url="/assets/img/Models-01.png" css="image-center" height="200px" %}

To simulate data, type

    /var/pyenv/bin/python3 Machine_Learning_for_Population_Genetics_V2.py --simulate

If you've set up your the `runml` alias, you need only type:

    runml --simulate

## Training the model

Now, we can train a machine learning algorithm to distinguish amongst the two models using the SFS as our data. We will use a Convolutional Neural Network (CNN). 

To train a network with 2 hidden layers, a dropout rate of 0.2, 10 epochs, and a learning rate of 1e-05, type

    /var/pyenv/bin/python3 Machine_Learning_for_Population_Genetics_V2.py --train \
    --layers 2 --dropout 0.2 --epochs 10 --learning_rate 1e-05
    
or, using your alias,

    runml --train --layers 2 --dropout 0.2 --epochs 10 --learning_rate 1e-05

Experiment with the different parameters!

* What happens if you use only one layer? three layers?
* What happens if you change dropout to 0? 0.5?
* What happens if you increase the learning rate to 1e-03? decrease it to 1e-07?
* What happens if you decrease the number of epochs to 5? increase it to 15?

## Testing the model on an independent dataset.

After you've settled on the number of layers, dropout, number of epochs, and learning rate you want to use, you need to test your network on an independent test set! Don't run this part until you've settled on your hyperparameters!

    /var/pyenv/bin/python3 Machine_Learning_for_Population_Genetics_V2.py --test

or, using your alias,

    runml --test

