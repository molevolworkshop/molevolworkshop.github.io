---
layout: page
title: Workshop Notes for TAs
permalink: /tanote/
---

<!--written in 2024 MOLE workshop -->

This note contains some information that may be useful for future teaching assistants (TAs) at the Workshop for Molecular Evolution (MOLE), Woods Hole, MA.

# Before MOLE
## Updating profile on the website
Once TAs get access (granted by the director(s)) to contribute to the GitHub repository of the MOLE website, the profiles of TAs/instructors available in `faculty` folder in the repository [https://github.com/molevolworkshop/molevolworkshop.github.io/tree/master/faculty] can be edited -- good idea to keep the information up-to-date.

## Testing the tutorials
Once the testing version of the virtual machine (VM) is prepared, the lead TA can assign tutorials to each TA. Each TA is responsible for checking if the assigned tutorial works fine; for example, whether the required software is installed in VM, the provided code in the tutorial is executing without error, example data is uncorrupted, the results and the interpretation in the tutorial are consistent and makes sense, etc. 

TAs can let the lead TA know when testing the assigned tutorials is complete. Lead TA should track the progress. Then, TAs can try other tutorials that are not assigned to them. This will help TAs familiarize themselves to the other tutorials and also test if the tutorial works fine in different machines or OS.

If some issues were identified, it should be described in detail on Slack channel. If the issue is related to VM (e.g., software not installed), Paul and Analisa (in 2024) could fix; otherwise, in the case of the analysis giving different results from the tutorial, for example, TAs could let the instructor know and let them fix it. Sooner to get this step complete is better, in order to prevent last minute changes to VM.

## Sessions led by TAs
During the workshop, TAs are responsible to lead four 90-minute sessions: (1) introduction computing laboratory, (2) alignment lab, (3) IQ-TREE introduction, and (4) IQ-TREE lab and quiz. In 2024, the lead TA led the Intro Computing lab, each of the two experienced TAs led the alignment lab and IQ-TREE introduction, respectively, and two newer TAs worked together on IQ-TREE lab and quiz (more information below).

# At MOLE 
## Wi-Fi
May be this would change in the future, but as of 2024, Wi-Fi can be connected in MBL using
```
Wi-Fi: MBL-guest
Password: mblguest
```

and `eduroam`.


## T-shirts
It is important to consult the t-shirt shop as early as we can. In 2023 and 2024, we worked with *Howlingbird Studio* [https://howlingbird.com], located in Falmouth. In 2024, we have to order the t-shirts before May 28 morning (workshop Day 5) to get it before the end of workshop. Keep in mind the schedule is a little tight. In terms of payment, MBL can issue a purchase order to *Howlingbird*. We will need the number of each t-shirt of each size and the cost information. 


```
**Howlingbird Studio**
115 Palmer Ave Unit 2B
Falmouth MA, 02540
Open hours:
Monday-Friday 10:00 AM — 4:00 PM
Saturday 11:00AM - 4:00 PM Retail Only
Sunday CLOSED
508-540-3787
info@howlingbird.com
```

Extra information about the t-shirt design:

The design should include the following items:

* ``Marine Biological Laboratory, Woods Hole, MA"
* ``N^th (e.g., 35th) Workshop on Molecular Evolution"
* ``Current year"
* Preferrably related to the contents covered
* In high quality, with no excessively thin lines (printing will be difficult)
* Examples: https://molevolworkshop.github.io/tshirts/ 

Color of the T-shirts can be decided after the design is selected.

## Survey
To get information on the size of the t-shirts for each participant, as well as whether they would want to have a lobster for the course dinner party, we created a Google survey [e.g., https://docs.google.com/forms/d/1F0PLsQDkbpUwzcDr4vYRjnZd31H6qC1eqY8w97kC-1M] that contains the following questions:

* What is your name?
* For the "Course Dinner Party" on Wednesday, May 29 -- we are planning to get LOBSTERS. Do you want us to order one for you? (Y/N)
* Please let us know any allergies or dietary restrictions that we need to know to get alternative option for you.
* T-shirt size? (XS, S, M, L, XL, XXL)
* Which color do you prefer for your T-shirt? (consult with the shop)


## Introduction to Computing Laboratory
### Post-it system
Before the Intro Computing lab, TAs place one of each green (or blue/yellow) and pink post-it at each participant's desk. This is one good way to promote communication between the TAs and the participants on how they are doing during the tutorial. Green post-it means the participant is complete with the given task and pink means that they need a help. They can stick the post-it on top of their labtop or at the edge of the table, whichever easily visible by the TAs. Note the post-its are not provided by MBL.

### Some (unexpected) confusions during the lab
1. Setting the VM passwords confused some participants. Although it is straighforward once understand how it works, it would nice to list steps more specifically. For example:

```
1. On a participant's terminal, type:
    $ ssh moleuser@123.123.123.123 (their personal ip)

2. It will ask for a password, so type 
    Current password (which is given)
    Login success

3. Then, once in VM, type:
    $ passwd

4. When the prompt asks for the current password, re-type the password used above.

5. It will then ask for a new password. Here, participant can set their own password.

6. Re-type the new password; done
```

2. If a student forgets the password they set, TAs can login to their VM using TA's local laptop (no password needed), they can use the below. Because we become superuser using above commands, it will not ask us for the old password, so we can just type in some temporary password (e.g. nobska@capecod) twice and have them change it again (to one they will remember this time!):

```
sudo su
passwd moleuser
```


3. It is important to stress that a dot (.) and double dots (..) actually means something significant in Unix, which appear in the Unix-tutorial.

4. It is a good idea to stress to be at the local machine when using `scp`.

5. Setting `alias` for `moleuser@123.123.123.123` is a good idea. Most people got it easily by following the steps, but not everyone.

6. It might be a good idea to mention that there are many third party software that combine the command-line interface as well as interactive file transfer. A participant suggested MobaXTerm (https://mobaxterm.mobatek.net), but it is unclear if this is available for all mac, windows, and linux. 

7. This tutorial looked easy but took almost full 90 minutes, and lots of confusions.

8. Mention to utilize `tab` to autocomplete commands.


## Alignment lab
I think the activity was good and straightforward.

## IQ-TREE lab
### Lecture

### Tutorials


## Miscellaneous thoughts
* We thought of waiting for the students in front of Swope on the very first morning to guide participants to the classroom, but it was an unnecessary worry. They found their way pretty well.
* Meals: TAs are trying to actively site with the participants instead of sitting ourselves to promote communication. Seems like this is a good choice.
* Getting ice sounds not very too easy so far.
* There is a fridge with a lock on the second floor break room. It would be nice if MOLE can continue to use it in the coming years to store stuff in the future.
* Getting drinks are not funded by MBL so it is a good idea to encourage participants to contribute as the workshop goes. 
* Swim: Water is cold.
* Tried contributed playlist, but seems not going well.