---
layout: page
title: Workshop Notes for TAs
permalink: /tanote/
---

<!--written in 2024 workshop -->

This note contains some information that may be useful for future teaching assistants (TAs) participating at the Workshop for Molecular Evolution (MOLE), Woods Hole, MA.

# Before MOLE
## Updating profile on the website
Once TAs get access to contribute to the GitHub repository of the MOLE website, the profiles (or information) of TAs are available in `faculty` folder in the repository [https://github.com/molevolworkshop/molevolworkshop.github.io/tree/master/faculty]. TAs can go to their folder and make changes accordingly.

## Testing the tutorials
Once the testing version of the virtual machine (VM) is prepared, the lead TA assigns tutorials to each TA. Each TA is responsible for checking the assigned tutorial works fine. Some things to pay attention are, for example, weather the required software is installed in VM the provided code is working without error, example data is uncorrupted, the result and the interpretation in the tutorial are consistent etc. 

Once testing the assigned tutorials are complete, TAs can check other tutorials that are not assigned, to find missed issue, trying the tutorial in different machine (e.g, mac or window), and to familiarize the material beforehand.

The identified issues were described in detail on Slack channel. If the issue is related to VM (e.g., software not installed), Paul and Analisa (in 2024) could fix; otherwise, in the case of the analysis giving different results from the tutorial, for example, TAs could let the instructor know and let them fix it. Sooner to get this step complete is better, in order to prevent last minute changes to VM.

## Sessions led by TAs
During the workshop, TAs are responsible to lead four 90-minute sessions: Introduction Computing Laboratory, Alignment lab, IQ-TREE introduction, and IQ-TREE lab and quiz. In 2024, the lead TA led the Intro Computing lab, each of the two experienced TAs led the Alignment lab and IQ-TREE introduction, and two newer TAs worked together on IQ-TREE lab and quiz (more information below).

# At MOLE 
## Wi-Fi
May be this would change in future but as of 2024, Wi-Fi can be connected in MBL using
```
Wi-Fi: MBL-guest
Password: mblguest
```

and `eduroam`.


## T-shirts
It is important to consult the t-shirt shop as early as we can. In 2023 and 2024, we called Howlingbird Studio [https://howlingbird.com], located in Falmouth. In 2024, we have to order the t-shirts along with the design before May 28 morning (workshop Day 5) to get it before the end of workshop. Keep in mind the schedule is a little tight. In terms of payment, MBL can issue a purchase order to Howlingbird. We will need the number of each t-shirt of each size and the cost information. 


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

Extra information for the T-shirt design:

The design should include the following terms:

* Marine Biological Laboratory, Woods Hole, MA
* N^th (e.g., 35th) Workshop on Molecular Evolution
* Current year
* Preferrably related to the contents covered
* In high quality, without too thin lines (printing will be difficult)
* Examples: https://molevolworkshop.github.io/tshirts/ 

Color of the T-shirts can be decided after the design is select.

## Survey
In order to get information on the size of the t-shirts for each participant, as well as weather they would want to have lobster for the course dinner party, we created a Google survey that contains the following questions:

* What is your name?
* For the "Course Dinner Party" on Wednesday, May 29 -- we are planning to get LOBSTERS. Do you want us to order one for you? (Y/N)
* Please let us know any allergies or dietary restrictions that we need to know to get alternative option for you.
* T-shirt size? (XS, S, M, L, XL, XXL)
* Which color do you prefer for your T-shirt? (consult with the shop)


## Introduction to Computing Laboratory
### Post-it system
Before this session, TAs placed one of each green (or blue/yellow) and pink post-it at each participant's seat. These are one of the ways for the participants to easily communicate with the TAs on how they are doing with the tutorial. Green post-it means the participant is complete with the given task and pink means that they need a help. They can stick the post-it on their labtop or at the edge of the table, whichever visible by TAs.

## Some (unexpected) confusions
1. Setting VM passwords confused some participants. Although it is straighforward once understand how it works, it would nice to list steps more explicitly. For example:

```
On a participant's terminal, type:
    $ ssh moleuser@123.123.123.123 (their personal ip)
It will ask for a password, so type 
    Current password (given)
Login success

Then, once in VM, type:
    $ passwd
When it asks for the current password, re-type the password used above.
Then, it will ask for the new password, participant will set their own password.
Re-type the new password
done
```

2. If a student forgets the password they set, TAs can login to their VM using TA's local laptop (no password needed) and do this:
```
sudo su
passwd moleuser
```
Because we become superuser using above commands, it will not ask us for the old password, so we can just type in some temporary password (e.g. nobska@capecod) twice and have them change it again (to one they will remember this time!).

3. It was important to stress that a dot (.) and double dots (..) actually means something significant in unix. These appear in the Unix-tutorial.

4. It is a good idea to stress to be at the local machine when using `scp`.

5. Setting `alias` for `moleuser@123.123.123.123` was a good idea. Most people got it easily by following the steps, but not everyone.

6. It might be a good idea to mention that there are other third party softwares that incorporates the command-line interface as well as interactive file transfer, like terminal and cyberduck in the same framework. Some participant suggested MobaXTerm (https://mobaxterm.mobatek.net) but it is unclear if this is available for all mac, windows, and linux. 

7. The tutorial looks easy but to almost full 90 minutes.

8. Mention to utilize `tab` to autocomplete commands.


## Alignment lab
I think the activity was good and straightforward.

## IQ-TREE lab
### Lecture

### Tutorials


## Miscellaneous thoughts
* We thought of waiting for the students in from of Swope on the very first morning to guide participants to the classroom, but it seemed unnecessary worry. They found their way pretty well.
* Meals: TAs are trying to actively site with the participants instead of sitting ourselves to promote communication. Seems like this is a good choice.
* Getting ice sounds not very too easy so far.
* There is a fridge with a lock on the second floor break room. It would be nice if MOLE can continue to use it in the coming years to store stuff in the future.
* Getting drinks are not funded by MBL so it is a good idea to encourage participants to contribute as the workshop goes. 
* Swim: Water is cold.
* Tried contributed playlist, but seems not going well.