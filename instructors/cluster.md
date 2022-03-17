---
layout: page
title: Cluster
permalink: /cluster/
---
If you are a participant, these notes are not intended for you, but you are welcome to read them. They are intended for the current directors and TAs of the workshop.

# Notes on using the Jetstream cluster

Starting in 2022, the Workshop will use a "cluster in the cloud" for its computing needs.

The cluster we will be using is from the [Jetstream](https://jetstream-cloud.org) project at Indiana University. Jetstream is NSF's first science and engineering research cloud, completed in early 2016 at a cost of $6.6M. Jetstream is one source of computing infrastructure provided under the umbrella of [Xsede](https://www.xsede.org), the Extreme Science and Engineering Discovery Environment, an NSF-sponsored program that provides cloud computing for researchers in academia. 

We (Paul Lewis and Peter Beerli) applied to Xsede for an allocation to provide enough computing resources for the Workshop in 2020. [Here](/assets/pdf/jetstream-proposal.pdf) is our proposal. We were awarded 207360.0 SUs (Service Units), which would allow 120 4-core virtual machines to run continuously for 18 days (120*4*24*18 = 207360 core*hours). 

See the [Jetstream Setup notes](/jetstream-setup/) for how the cluster was set up with software used for the Workshop. [Mike Lee's notes](https://hackmd.io/tU79TQPpQqi1IUiK__mRvg) for the STAMPS course have also been (and continue to be) very useful.

This document will concentrate on practical aspects useful to TAs such as how to login to the cluster and where to find tutorial materials.

# Workshop cluster

## Service Units (SUs)

There are 46 participants this year, 4 TAs, and 12 faculty who will need access to a machine. That totals 46 + 4 + 12 = 62 VMs (Virtual Machines) needed. Assuming we run 62 4-core VMs continuously from May 26 - June 6 (12 days), we will burn through 62*4*24*12 = 71424 SUs. This means we have 207360 - 71424 = 135936 SUs to use for testing, which should be more than enough.

See the [Virtual machine sizes and configurations](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/17465371/Virtual+Machine+Sizes+and+Configurations) page for more information about SU burn rates.

## Images and instances

An **instance** is a Virtual Machine started from an **image**. An instance acts as if it was a stand-alone Ubuntu Linux computer. Paul has created an image named "MOLE2022" that can be used to start instances that come pre-installed with all the software and data sets needed for the Workshop. The MOLE2022 image was created by first creating an instance of the "Ubuntu 20.04 Devel and Docker" image created March 3, 2022 by jfischer and then following the instructions in the [Jetstream Setup notes](/jetstream-setup/) to install everything. Those instructions also explain how to create an image once the VM is set up the way you want.

## Shelving

Before the week prior to the Workshop, it is **vitally** important to **shelve** any running instances when they are no longer being actively used. Shelving is the only option that does not burn SUs, and the only cost to shelving is that the IP address will change once it is unshelved.

In the week before the Workshop begins, we will start 62 or more instances from the MOLE2022 image and just leave them running 24/7 until the Workshop is over. Hence, shelving is only important before the Workshop so that we end up having enough SUs to enable full time access for all VMs during the Workshop.

# Jetstream issues

## Issue 1

In March of 2022, I (Paul) had problems starting an instance. I sent the following support request on 2022-03-16:

> I don't understand why I get the error "You do not have enough resources." after "A total 4 of 2 alloted CPUs" and am encouraged to request more resources when attempting to launch an instance of the MOLE2020 image. The Allocation Source I am using is TG-DEB190022, which seems to have plenty of resources: 0% of 207360 SUs from TG-DEB190022. I just want to make sure I'm understanding why I need to request more resources for such a small instance.

Here is the response I got back from Brian Beck later the same day:

> The limits were from you being on the Jetstream Trial Allocation. I removed you from the allocation and set your quota back to default: 

|    Field     | Value  | 
| ------------ | ------ |
| cores        |    132 | 
| floating-ips |     25 | 
| gigabytes    |    800 | 
| instances    |     25 | 
| ports        |     25 | 
| ram          | 368640 | 
| snapshots    |     10 | 
| volumes      |     10 | 

Now I no longer see the trial allocation and things seem to be working, although the number of instances above will need to be increased for the workshop itself:

|    Field     |    Value     |  
| ------------ | ------------ |
| cores        | 248 = 62*4   | 
| gigabytes    | 1240 = 62*20 | 
| ram          | 620 = 62*10  | 
| floating-ips |     62       | 
| instances    |     62       | 
| ports        |     62       | 

# Xsede allocation renewals

We have applied every 6 months for extensions because of the COVID19-related cancellation of the Workshop in both 2020 and 2021. Unfortunately, the End Date for our allocation is currently listed on the Xsede site as 2022-5024 (3 days before the Workshop begins!). Paul submitted one last extension request March 16, 2022.

# Xsede retirement

Note that Xsede will be retiring at the end of August, 2022. It will be replaced by ACCESS (Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support). Here is the message sent out from er@xsede.org March 1, 2022:

> The XSEDE project is scheduled to end operations on August 31, 2022, giving way to a new National Science Foundation program, Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS), set to launch September 1, 2022.

> While access to XSEDE-allocated resources will continue under the ACCESS program, there will be changes in how the new program is managed.

> ACCESS aims to establish a suite of cyberinfrastructure coordination services – meant to support a broad and diverse set of requirements, researchers and modes from all areas of science and engineering research and education – set up as five independently managed yet tightly cooperative service tracks supported by a coordination office. It’s anticipated ACCESS will continue for five years. 

> Allocations to support Science Gateways are expected to be available under the ACCESS program. Additionally, the Campus Champions Leadership Team has been working towards sustainability of the program beyond the XSEDE operational period. 
The Extended Collaborative Support Services (ECSS) program and much of the Community Engagement and Enrichment (CEE) program, do not explicitly appear in the ACCESS solicitations. ACCESS awardees may choose to continue these services; however, that is unclear at this time. Those groups are working with their constituencies to make preparations for the transition.

> Researchers may apply for allocations via XSEDE (transitioning to ACCESS) from March 15 – April 15 for allocations with a July 1, 2022 start date and June 15 – July 15 for allocations with an October 1, 2022 start date. This latter opportunity will be the last XSEDE allocation event.

> XSEDE leadership has created a website – accessible here, and from the XSEDE homepage and the Inside XSEDE and XSEDE Impact newsletters – to provide information about this transition as it becomes available. Please look for the Advance to ACCESS logo for the latest information about the transition.

> The XSEDE vision is of a world of digitally enabled scholars, researchers, and engineers participating in multidisciplinary collaborations while seamlessly accessing advanced computing resources and sharing data to tackle society's grand challenges.
Over the course of nearly 11 years, the XSEDE community – staff, Service Providers, students and so many others – has risen to the challenge of its mission:

> To enhance the productivity of a growing community of scholars, researchers and
engineers through access to advanced digital services that support open research
by coordinating and adding value to the leading cyberinfrastructure resources
funded by the NSF and other agencies.

> We look forward to transitioning the outstanding work of XSEDE to the new ACCESS environment and doing all in our power to help this community experience continued success.