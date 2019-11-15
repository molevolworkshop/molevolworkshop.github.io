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

## Slack group

Slack is a messaging/discussion program that allows for large groups to interact as needed.<br/>
There is a slack group set up for people to ask questions and to have discussions.<br/>
The slack team is _MBL-MOLE-2019_<br/>
You can use the Slack app on your laptop and your phone. <br/> 
If you can't join through the app/website, you can click on 
[this link](https://join.slack.com/t/mbl-mole-2019/shared_invite/enQtNzA4NDY2NzQ3MzMzLTBhNWZiNzMzZTg4ZGI0NTVhN2MxMzYyNzY5ZDJhYTYzZWIyNDk1M2Q1OTA3ODgxNGZmNDJmODY5MDViODgzNDc) 
(note that until Sunday, 28 July 2019, this link was for the 2018 version of the course, but it is now fixed).

## WiFi Login

TODO 

Some people have been having trouble, if it isn't working find or email [George](mailto:george.tiley@gmail.com) or any TA, 
or ask on the Slack group.

## Downloads

Please download and install the following programs:

### **Windows**

* [Cyberduck](http://cyberduck.ch/) (file transfer via sFTP)
* [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) (SSH client)
* [Git for Windows](https://git-for-windows.github.io/) (This is a UNIX emulator for running command-line programs)
* [Notepad++](https://notepad-plus-plus.org/download/v7.7.1.html)
After you have installed Notepad++, open it. 
Go to Settings, Preferences, New Document, and set the line endings to Unix.
* [Seaview](https://web.archive.org/web/20141007105432/http://pbil.univ-lyon1.fr/software/seaview_data/seaview4.exe)
* [figtree](https://github.com/rambaut/figtree/releases) (use the v1.4.4.zip release)

### **Mac Os X**

* SCP and SSH installed by default
* [Cyberduck](http://cyberduck.ch/) (file transfer via sFTP)
* [BBEdit](https://www.barebones.com/products/bbedit/) (BBEdit is the 64 bit version of TextWrangler for contemporary Mac OS)
* [Seaview](https://web.archive.org/web/20141007105432/http://pbil.univ-lyon1.fr/software/seaview_data/seaview4.zip)
* [figtree](https://github.com/rambaut/figtree/releases) (use the v1.4.4.dmg release)

### **Linux**

* SCP and SSH installed by default
* [Seaview](https://web.archive.org/web/20141007105432/http://pbil.univ-lyon1.fr/software/seaview_data/seaview4.tgz)
* [figtree](https://github.com/rambaut/figtree/releases) (use the v1.4.4.tgz release)
* You're set!

Everybody should download Tracer too, which will be used for Bayesian divergence time analyses: 
[Tracer](https://github.com/beast-dev/tracer/releases/tag/v1.7.1)

We will be using more software throughout the workshop than what we're asking you to download here, all of which should be accessible on the remote servers. Feel free to download and use any and all software on your personal device as well, just know that not everything will necessarily finish running in the allotted time, depending on your device.

## Remote computer access software 

We will use Secure Shell (SSH) and sFTP to connect to the servers.
The servers are powerful computers where we can run the programs much faster than would be possible on your laptop.
In order to access these you need to log in to your assigned server

## SSH 

SSH stands for "Secure Shell." These are programs that provide a Unix shell so that one 
can enter commands and log onto other computers (i.e., those on the server where we will be doing our analyses).

**You must be on the MBL-REGISTERED wifi network or this will not work**

### SSH on Linux and Mac Os X
First, open a terminal window:
* _Linux:_ Konsole (KDE), gnome-terminal (GNOME)
* _Mac:_ Terminal (in /Applications/Utilities)
<br>
First we want to log on to the class servers.<br>
In the following command replace <username> and <server name> with the user 
(first initial plus last name) and server name (class-##) which you can find on the 
sticker attached to the back of your name tag:<br>
~~~~~~
ssh username@servername
~~~~~~
{:.bash}

For example if my username is  jbloggs and my server name is class-04 I type:<br>
 ssh jbloggs@class-04.jbpc-np.mbl.edu
It will then ask for your password which is on the back of your card under your username

### SSH on Windows

On windows you can use git for windows or PuTTY for accessing the class servers.<br>
If using git for windows, follow the Linux/Mac approach above. <br>
To set up SSH on PuTTY 
Enter your username and servername in the "Host Name or IP Address" field
You can find your username and servername on the piece of paper:
~~~~~~
username@servername
~~~~~~
{:.bash}

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

### Everyone 

You should have a black screen asking for your password, which is on the piece of paper. Type it in. You will not see the letters you are typing.

#### Changing your password 

The first thing to do once you have successfully logged on to a server is to change your password. This is done by typing:<br>
~~~~~~
passwd
~~~~~~
{:.bash}

This will prompt you to enter a new password so do so and press the enter key. Next you re-enter the new password and again press enter. It may then ask you for your LDAP password and you should type in your original password given on the back of your card.<br>
Once you have done this every time you ssh in to the server you will use the new password created.

#### Basic Syntax

Unix commands follow the general format of: 
~~~~~~
command -options target
~~~~~~
{:.bash}

Not all commands need options (sometimes called flags, and generally preceded by a single or double hyphen ("-" or "--")) or targets, but others require them.

*For example:
**cd homedirectory uses the command "cd" (change directory) and the target "homedirectory" to move from the current directory into the subdirectory called "homedirectory"
**ls -l homedirectory uses the command "ls" (list), the option "-l" for long-list, and the target "homedirectory" to list the contents of homedirectory in the "long list" format, which provides more thorough descriptions than does the regular "ls".

#### Notes on syntax for directory structure

*Two dots (..) indicates the parent directory of the present working directory. So, for example, "cd .. will move you back one directory.
*One dot (.) indicates the present working directory. So, for example, "cd ." will keep you where you are. There are times where the single dot can be more useful than this...
*The tilde (~) refers to your home directory. On the class machines your home directory is /class/yourusername. You'll also have a unique home directory on your laptop, etc. The tilde is very helpful if you get lost while using the terminal -- just type "cd ~" and you'll be back in your homedirectory.
*A forward slash (/) by itself or at the start of a path refers to the root of the filing system -- the folder that contains all other folders.
*NOTE: do not make changes on the class server in the root folder or any shared folders. All your work is to be done in your home directory or a subdirectory.

## Intro-to-Unix tutorial

Please go to the [[UNIX tutorial]] and go through the step by step guide there.

## Downloading files

In order to get a file from an online source you can use wget. Type:
~~~~~~
wget <URL>
~~~~~~
{:.bash}

Where the url is the website address of the file you wish to download. For example
~~~~~~
wget https://raw.githubusercontent.com/gtiley/misc/master/mbl2019.txt
~~~~~~
{:.bash}

Will download the file mbl2019.txt to the directory you are in.
Note: If you are on OSX and trying to do this locally to your machine, this won't work. Curl is an alternative for doing this. See if you can figure out using google how curl works. Wget will still work on the class servers, regardless of your operating system.

Copy this file to a file named <yourname.txt> (remember! No spaces!)

Edit the statement in the file using nano, to a fact about yourself.

Copy it to the /class/molevol-shared/facts/2019 directory.

_Ask a person next to you their name, and find and read their fact!_

## Setting up Cyberduck

#### Creating a bookmark

When you open Cyberduck a screen should appear that has some default connections bookmarked such as Google Docs and Amazon.<br />
Click the _'+'_ button at the _BOTTOM LEFT_ to create a new bookmark (NOT the one with the globe at the top). Here we will put the details of our cluster login and save it so that each time we open Cyberduck we don't have to re-enter the details.
* Click the dropdown menu that says FTP (file Transfer Protocol) and select SFTP. <br />

* Create a nickname for this bookmark. For example mine is called 'MBL cluster'.<br />

* In 'server' write the class number of the server you were given. For example, I am rwilliams@class-04 so I put class-04 in here. <br />

* In the username box place the username you were given. This is likely your first initial and your last name. For example mine is rwilliams. <br />

Once all these details are entered close that screen. (e.g. on a mac click the red circle or on windows click the X).<br />
A new bookmark should have appeared named whatever you set as the nickname. Double click on this.<br />
Cyberduck should ask you for the password. Type in the password you changed it to earlier. There should be a button asking for you to 'add to your keychain' or something similar. Make sure this box is ticked. Once done, click to connect.<br />
This may connect you directly to the cluster. If not double click on the bookmark again.<br />
You now should see your home directory on the cluster. You should see the file "yourname.txt" that we created earlier.

### Navigating the cluster on Cyberduck and transferring files

Navigating through the class cluster in cyberduck is easy. <br />
Double click on a folder to open that folder.<br />
Above the window that lists files there should be your path. For example when I login my path shows '/classfs/rwilliams'. This tells me where I am on the cluster right now. If you click this dropdown menu you can see each folder you are in. For example when I click on the dropdown I have a line that says /classfs/rwilliams, one that says /class and one that just says /. Clicking on any of these will allow you to navigate to that folder. If you get lost in folders you can click this dropdown and select /class/username (where username is your own username) and this will bring you to your home directory.<br />
An alternative way to go to a specific folder is click the _'Go'_ menu at the top of Cyberduck and click _'Go to folder'_. Here you can write the full path and go to a specific folder. For example, if you are logged in to the cluster through a terminal/putty you can type 'pwd' and then copy that path into the 'go to folder' box and now Cyberduck will be in the same folder as your terminal window.

There are two ways to download files from the class cluster to your computer.<br />
_1._ If you double click on a file name, this file will be automatically downloaded to your default download folder. A transfer window should open up when you double click on a file. At the bottom there will be a line that starts 'local file'. This is the location of that downloaded file on your own computer<br />
_2._ An easier way to get files both to and from the class cluster through Cyberduck is through drag and drop. If you have an open finder window (mac) or explorer window (windows) you can click and drag a file from the Cyberduck window to the finder/explorer window directly. You also can do this in the reverse (drag a file from finder/explorer to Cyberduck) to place a file on the cluster in that folder.

### Using Cyberduck for remote editing

Instead of using nano or similar to edit files on the class cluster you can use a GUI text editor like TextWrangler through Cyberduck.<br />
In cyberduck click _'Cyberduck'_->_'Preferences'_ on a Mac or _'Edit'_-> _'Preferences'_ on Windows.<br />
Click the _'Editor'_ button.<br />
There should be a dropdown menu where you can select a text editor. Select TextWrangler on a Mac, Notepad++ on Windows.<br />
Close this window.<br />
Now when you single click on a file in Cyberduck, a 'Edit' button with the icon for the editor you selected should appear in the top right corner. Click this button to open that file in the editor. Now you can edit the file on the cluster without downloading to your local computer. When you save this file it will be automatically updated on the class cluster.

## Short Cyber Duck Exercise

The easiest way to transfer files using CyberDuck is with drag-and-drop. Try to drag a file from your desktop (or another folder of your choosing) from the CyberDuck window. This method allows you to choose unique destinations for each file you transfer.

In CyberDuck, double click example.txt your 'myfolder' on the cluster. To where does this file download? CyberDuck also allows for more permanent modification to how files are downloaded, you can set automatic download locations.  If you want to change this, under Edit -> Preferences -> Transfers, you can edit this.

Lastly: Right clicking (Ctrl click on a Mac) will allow you to select Download to or Download As. This will allow you to choose a location, and if you choose, a new file name for the file.

These methods will all work to get files from the cluster to your computer, and each have their own benefits. Generally, you will be fine using any of them throughout the course.

Make a folder on your computer to hold all of your lab materials from this course!

## SCP is a good alternative to Cyberduck for linux and Mac's

There are two places you may need to get files on to the class server from: your own computer or an online source<br>
In order to get files from your computer to the server open a terminal window and navigate to the folder on your computer using the commands like cd. Once in the folder containing the file you want to upload you type
~~~~~~
scp filename username@classServername.jbpc-np.mbl.edu:~
~~~~~~
{:.bash}
e.g.
just like cp, the format is scp <from> <to>

To get files from your computer to the cluster:

    scp text.txt gtiley@class-04.jbpc-np.mbl.edu:/class/gtiley

To get files from the cluster to your computer:

    scp gtiley@class-04.jbpc-np.mbl.edu:/class/gtiley/testfile.txt .

## Useful links

The following table contains a list of commands that will allow us to navigate through the directory structure. The entries are linked to their [http://www.wikipedia.org/ Wikipedia] pages, which contain very useful examples.

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
