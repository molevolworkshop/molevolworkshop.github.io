---
layout: page
title: Computer Lab Introduction
permalink: /labs/intro/
---

> On the other side of the screen, it all looks so easy. (TRON, 1982)

## Goals

By the end of this introduction, you should be able to:
* Log in to the class cluster.
* Navigate and understand the directory structure.
* Create and edit files and directories on the cluster.
* Move files to the cluster.
Ask for help if any of these things aren't working by the end!

## Slack workspace

Slack is a messaging/discussion program that allows for large groups to interact as needed.<br/>
There is a slack workspace set up for people to ask questions and to have discussions.<br/>
The Slack Workspace is _MBL-MOLE-2022_<br/>
You can use the Slack app on your laptop and your phone. <br/> 
If you've lost your invitation to join this workspace, ask one of us and we'll resend the invitation to your email address.

## WiFi Login

You should have received instructions for connecting to wifi with your room key. If you have trouble connecting to the internet, let one of the TAs or course directors know and we'll help you get on the network. 

## Downloads

Please download and install the following programs if you haven't already:

### **Windows**

* [Cyberduck](http://cyberduck.ch/) (file transfer via sFTP)
* [Git for Windows](https://git-for-windows.github.io/) (This is a UNIX emulator for running command-line programs)
* [Notepad++](https://notepad-plus-plus.org/download/v7.7.1.html)
After you have installed Notepad++, open it. 
Go to Settings, Preferences, New Document, and set the line endings to Unix.
* [Seaview](http://doua.prabi.fr/software/seaview) (used to visualize small alignments)
* [FigTree](https://github.com/rambaut/figtree/releases) (used to visualize phylogenetic trees)
* [Tracer](https://github.com/beast-dev/tracer/releases/) (used for Bayesian divergence time analyses)

{% comment %}
I don't think this is needed if people install Git for Windows (POL)
* [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) (SSH client)
{% endcomment %}

### **macOS**

* SCP and SSH installed by default
* [Cyberduck](http://cyberduck.ch/) (file transfer via sFTP)
* [BBEdit](https://www.barebones.com/products/bbedit/) (BBEdit is the 64 bit version of TextWrangler for contemporary macOS)
* [Seaview](http://doua.prabi.fr/software/seaview) (used to visualize small alignments)
* [FigTree](https://github.com/rambaut/figtree/releases) (used to visualize phylogenetic trees)
* [Tracer](https://github.com/beast-dev/tracer/releases/) (used for Bayesian divergence time analyses)
* [iTerm2](https://iterm2.com/downloads.html) (optional, but many of us like this terminal program better than the one that comes with macOS)

### **Linux**

* SCP and SSH installed by default
* [Seaview](http://doua.prabi.fr/software/seaview) (used to visualize small alignments)
* [FigTree](https://github.com/rambaut/figtree/releases) (used to visualize phylogenetic trees)
* [Tracer](https://github.com/beast-dev/tracer/releases/) (used for Bayesian divergence time analyses)
* You're set!

We will be using more software throughout the workshop than what we're asking you to download here, all of which should be accessible on the remote servers. Feel free to download and use any and all software on your personal device as well, just know that not everything will necessarily finish running in the allotted time, depending on your device.

## Remote computer access software 

You will use Secure Shell (SSH) and sFTP to connect to your own personal virtual machine (VM). You will interact with your VM solely by typing or pasting commands into a terminal window. This way of interacting with a computer may not be familiar to you, but you will get some practice during this lab.

The virtual computing environment you will be using is provided through a (U.S.) National Science Foundation funded program called [Xsede](https://www.xsede.org/), which (at least for those of you at U.S. institutions) is good for you to know about because Xsede also provides (assuming your application is accepted) these same cloud computing resources to researchers to facilitate research. (Note that Xsede is currently winding down, but will be succeeded by a similar program called Access.)

## SSH 

SSH stands for **Secure SHell**. Shells are computer programs that represent the outermost (i.e. closest to you) layer of the operating system. Shells hide most of the gory details, allowing you to interact with the operating system via commands. Another (better) name for a shell is **command interpreter**. SSH represents a shell that is secure in that every bit of text that moves between your keyboard and the operating system (and _vice versa_) is encrypted.

{% comment %}
I don't think this is necessary this year (POL)
**You must be on the MBL-REGISTERED wifi network or this will not work**
{% endcomment %}

### SSH on Linux and macOS
First, open a terminal window:
* _Linux:_ Konsole (KDE), gnome-terminal (GNOME)
* _Mac:_ Terminal or iTerm2 (in _/Applications/Utilities_)

Login to your particular virtual machine (VM) using the IP address on the sticker attached to the back of your name tag. If, for example, your IP address was 123.456.789.321, you would type the following into the terminal on your local computer (i.e. your laptop) and press the enter key:

    ssh moleuser@123.456.789.321

### SSH on Windows

On Windows you should use Git for Windows to access your virtual machine (VM). Assuming you've installed Git for Windows, choose **Git BASH** from the **All Programs** section of the **Start** menu. This will open a terminal running the shell program bash. 

Now login to your particular virtual machine (VM) using the IP address on the sticker attached to the back of your name tag. If, for example, your IP address was 123.456.789.321, you would type the following into the terminal on your local computer (i.e. your laptop) and press the enter key:

    ssh moleuser@123.456.789.321

{% comment %}
For example if my username is jbloggs and my server name is class-02 I type:<br>
~~~~~~
jbloggs@class-02.jbpc-np.mbl.edu
~~~~~~
{:.bash}

Enter a name for this configuration (e.g. MolEvol) where it says "Saved Sessions" and click Save
Now you can access the cluster by clicking on that saved session.

PuTTy copy paste tip: [http://www.chiark.greenend.org.uk/~sgtatham/putty/faq.html#faq-cutpaste PuTTy FAQ]

Copy and paste works similarly to the X Window System. You use the left mouse button to select text in the PuTTY window. The act of selection automatically copies the text to the clipboard: there is no need to press Ctrl-Ins or Ctrl-C or anything else. In fact, pressing Ctrl-C will send a Ctrl-C character to the other end of your connection (just like it does the rest of the time), which may have unpleasant effects. The only thing you need to do, to copy text to the clipboard, is to select it.

To paste the clipboard contents into a PuTTY window, by default you click the right mouse button. If you have a three-button mouse and are used to X applications, you can configure pasting to be done by the middle button instead, but this is not the default because most Windows users don't have a middle button at all.

You can also paste by pressing Shift-Ins.
{% endcomment %}

{% comment %}
### Everyone 

You should have a black screen asking for your password, which is on the piece of paper. Type it in. You will not see the letters you are typing.
{% endcomment %}

#### Changing your password 

The first thing to do once you have successfully logged onto your VM is to change your password. This is done by typing:

    passwd

This will prompt you to enter a new password, so do so and press the enter/return key. Next you re-enter the new password and again press enter. 
{% comment %}
It may then ask you for your LDAP password and you should type in your original password given on the back of your card.
{% endcomment %}
Once you have done this every time you ssh in to your VM you will use the new password you just created (so don't forget it!).

#### Basic Syntax

Unix commands follow the general format of: 

    command -options target

Not all commands need options or targets. Options are sometimes called _flags_ and are generally preceded by a single hyphen (**-**) or a double hyphen (**--**).

For example:

* ```cd mydir``` uses the command **cd** (change directory) and the target **mydir** to move from the current directory into the subdirectory called **mydir**.

* ```ls -l mydir``` uses the command **ls** (list), the option **-l** for long-list, and the target **mydir** to list the contents of _mydir_ in the long list format, which provides more thorough descriptions than does the regular list command.

#### Notes on syntax for directory structure

* Two dots (**..**) represents the parent directory of the present working directory. So, for example, ```cd ..``` will move you back one directory

* One dot (**.**) represents the present working directory. So, for example, ```cd .``` will keep you where you are. There are times where the single dot can be more useful than this...

* The tilde (**~**) represents your home directory. On your virtual machine, your home directory is _/home/moleuser_. The tilde is very helpful if you get lost while using the terminal -- just type ```cd ~``` and you'll be back in your homedirectory.

* A forward slash (**/**) by itself or at the start of a path refers to the root of the directory structure -- the folder that contains all other folders.

## Intro-to-Unix tutorial

If you are not familiar with typical linux commands, please go to the [Linux tutorial](/linux-tutorial/) and go through the step by step guide there.

## Setting up Cyberduck

#### Creating a bookmark

When you open Cyberduck a screen should appear that has some default connections bookmarked such as Google Docs and Amazon.

Click the **+** button at the _BOTTOM LEFT_ to create a new bookmark (NOT the one with the globe at the top). Here we will put in the details of our virtual machine login and save it so that each time we open Cyberduck we don't have to re-enter the details.

* Click the dropdown menu that says FTP (File Transfer Protocol) and select **SFTP (SSH File Transfer Protocol)**;

* Create a nickname for this bookmark. For example mine is called 'mole vm';

* For **server** write the IP address of the virtual machine you were asssigned. For example, 123.456.789.321;

* For **username** type **moleuser**;

Once all these details are entered close that screen. (e.g. on a mac click the red circle or on windows click the X).

A new bookmark should have appeared named whatever you set as the nickname. Double click on this.

If you get a popup dialog box with a lot of ugly text in it, e.g.

    Unknown fingerprint
    
    The fingerprint for the ED25519 key sent by the server is 
    c6:41:86:61:7d:87:56:90:cc:c9:3a:a5:56:dc:dd:ac
    
just press the Allow button. This is just letting you know that you are logging into a machine that you've never connected to before. This would only be a concern if you see it a _second time_ (which may mean someone has swapped the computer you thought you were connecting to with a different machine).

Cyberduck should ask you for the password. Type in the password you created earlier. There should be a button asking for you to add to your keychain or something similar. Make sure this box is ticked. Once done, click to connect.

This may connect you directly to the virtual machine. If not double click on the bookmark again.

You now should see your home directory on the cluster. You should see the folder named _myfolder_ that we created earlier as well as the symlink named _eg_ (which looks like an ordinary folder except that the folder icon contains a tiny little arrow symbol, which clues you into the fact that this is an alias and not a real folder.

### Navigating the cluster on Cyberduck and transferring files

Navigating through the class cluster in cyberduck is easy.

Double click on a folder to open that folder.

Above the window that lists files you should see your path: e.g. _/home/moleuser_. This tells you where you are in the virtual machine's directory structure. If you click this dropdown menu you can see each nested folder in the directory hierarchy above that point. Clicking on any of these intermediate directories will allow you to navigate to that directory. If you get lost in folders you can click this dropdown and select _/home/moleuser_ to return to your home directory.

There are two ways to download files from the virtual machine to your computer.

1. If you double click on a file name, this file will be automatically downloaded to your default download folder. A transfer window should open up when you double click on a file. At the bottom there will be a line that starts **local file**. This is the location of that downloaded file on your own computer.

2. An easier way to get files both to and from the class cluster through Cyberduck is through drag and drop. If you have an open finder window (mac) or explorer window (windows) you can click and drag a file from the Cyberduck window to the finder/explorer window directly. You also can do this in the reverse (drag a file from finder/explorer to Cyberduck) to place a file on the cluster in that folder.

### Using Cyberduck for remote editing

Instead of using nano to edit files on the virtual machine you can use a text editor such as BBEdit (mac) or Notepad++ (windows) through Cyberduck.

In Cyberduck, select (mac) the _Cyberduck_ main menu item and then select _Preferences_  or (windows) the _Edit_ menu item and then _Preferences_.

Click the _Editor_ button.

There should be a dropdown menu where you can select a text editor. Select BBEdit on a Mac, Notepad++ on Windows.

Close this window.

Now when you single click on a file in Cyberduck, an _Edit_ button with the icon for the editor you selected should appear in the top right corner. Click this button to open that file in the editor. Now you can edit the file on the cluster without downloading to your local computer. When you save this file it will be automatically updated on the class cluster.

## Short Cyber Duck Exercise

The easiest way to transfer files using CyberDuck is with drag-and-drop. Try to drag a file from your desktop (or another folder of your choosing) from the CyberDuck window. This method allows you to choose unique destinations for each file you transfer.

In CyberDuck, double click _example.txt_ in your home directory on the virtual machine. To where does this file download? You can change the default download locations using the _Edit_, _Preferences_, _Transfers_ menu item.

Lastly, right clicking (Ctrl click on a mac) will allow you to select _Download To_ or _Download As_. This will allow you to choose a location, and, if you choose, a new file name for the file.

These methods will all work to get files from the cluster to your computer, and each has their own benefits. Generally, you will be fine using any of them throughout the course.

Make a folder on your local computer to hold all of your lab materials from this course!

## SCP is a command line alternative to Cyberduck

Navigate (using cd in a terminal window) to the folder (on your local computer) containing the file you wish to transfer to your virtual machine. Once there, type

    scp testfile moleuser@123.456.789.321:

This would transfer the local file named _testfile_to your home directory on your virtual machine (assuming that the IP address of your virtual machine is 123.456.789.321). You could also copy the file to a subdirectory:

    scp testfile moleuser@123.456.789.321:myfolder

To get files from your virtual machine to your local computer, type (from your local computer):

    scp moleuser@123.456.789.321:testfile .
    
The dot at the end is significant: it stands for your present working directory (on your local computer).

You may think that typing <tt>moleuser@123.456.789.321</tt> each time is a bit tedious, and you'd be correct. To simplify things, you can create an entry in your local computer's ssh configuration file that creates short alias for the whole <tt>moleuser@123.456.789.321</tt> combination.

Create, if necessary, a text file on your **local computer** as follows:

    nano ~/.ssh/config
    
Enter the following text in this file:

    Host molevm
        HostName 123.456.789.321
	    User moleuser
	    
Use the tab character to indent the second and third lines. Now make sure that your config file has the propoer (very limited) permissions:

    chmod 600 ~/.ssh/config
    
You should now be able to do this:
    
    scp testfile molevm:

Your scp command can look up _molevm_ in your _~/.ssh/config_ file to find what username and ip address to use!

## Useful links

The following table contains a list of commands that will allow us to navigate through the directory structure. The entries are linked to their [Wikipedia](http://www.wikipedia.org/) pages, which contain very useful examples.

Linux/Mac                                                  | Description                 | Syntax (Linux/Mac)
---------------------------------------------------------- | --------------------------- | ------------------
[pwd](http://en.wikipedia.org/wiki/Pwd)                    | print working directory     | **pwd**
[ls](http://en.wikipedia.org/wiki/Ls)                      | list directory contents     | **ls**
[history](https://en.wikipedia.org/wiki/History_(command)) | display command history     | **history**
[cd](http://en.wikipedia.org/wiki/Cd_(command))            | change directory            | **cd** *directory_name*
[mkdir](http://en.wikipedia.org/wiki/Mkdir)                | create directory            | **mkdir** *directory_name*
[cp](http://en.wikipedia.org/wiki/Cp_(Unix))               | copy file(s)                | **cp** *original_filename* *copied_filename*
[mv](http://en.wikipedia.org/wiki/Mv)                      | rename file(s)              | **mv** *original_filename* *new_filename*
[clear](http://en.wikipedia.org/wiki/Clear_(Unix))         | clear the screen            | **clear**
[exit](http://en.wikipedia.org/wiki/Exit_(command))        | quit command line           | **exit**
Ctrl-E                                                     | go to the end of line       | 
Ctrl-A                                                     | go to the beginning of line | 

* UNIX/Linux command line cheat-sheet:<br/>
[http://fosswire.com/post/2007/08/unixlinux-command-cheat-sheet/](http://fosswire.com/post/2007/08/unixlinux-command-cheat-sheet/)

* MS-DOS full command list:<br/>
[MS-DOS commands](http://en.wikipedia.org/wiki/List_of_MS-DOS_commands)

* A unix shell tutorial from Software Carpentry:<br/>
[http://swcarpentry.github.io/shell-novice/](http://swcarpentry.github.io/shell-novice/)

