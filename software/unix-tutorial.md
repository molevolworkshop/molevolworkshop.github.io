---
layout: page
title: Linux tutorial
permalink: /linux-tutorial/
---
## Navigation

Start by entering

    pwd
    
This will print your **present working directory** (the directory you are currently in). You will probably see this:

    /home/moleuser
    
indicating that you are in your home directory.

Next, type:

    ls
    
This lists the contents of your working directory (which is currently empty unless you have created some files already).

You can also look at the contents of any other directory by supplying the path. For instance,

    ls /usr/local/share/examples/mole
    
will list the contents of the directory in which most of the example data files we will be using are stored.

To create a new folder (directory) inside your present working directory, type

    mkdir myfolder

Type ```ls``` and then enter. Your newly created folder should be listed. 

We can also use the ls command with flags at this point. Typing

    ls -l

will list the contents of the current directory in _long_ format which includes information about permissions and file size.

    ls -ltr

will list the contents of the current directory in long format, and in time (**t**) reversed (**r**) order. This makes it easy to see what files are newest.

You can move into the new folder you made by typing

    cd myfolder
    
You can use ```pwd``` to confirm you've moved and are now in a new working directory. You can move back to your home directory by typing ```cd``` with no arguments. This is a handy trick if you are lost in the filesystem and want to get home!

    cd 

Confirm you are in your home directory using ```pwd```. 

## Copying, renaming, and moving files

Move into the _myfolder_ directory that you just created:

    cd ~/myfolder
    
Create a file called _tmp1.txt_ in the nano editor and put whatever you want inside of it:

    nano tmp1.txt
   
After typing something, use Ctrl-X to exit (hold down the control key and type x). Type 'Y' and enter to save your changes.

Use the **head** command to look at the beginning of the file you created:

    head tmp1.txt
    
The concatenated (**cat**) command can be used to spit out the entire file (when head does not show enough of the file). The cat command can be used to concatenate several files, but if you give it just one file it will show you the contents of the file:

    cat tmp1.txt
 
The copy command (**cp**) is used to copy files to new places. Make a copy of _tmp1.txt_ called _tmp2.txt_ by typing:

    cp tmp1.txt tmp2.txt
    
We can also cp a file from the shared directory using absolute and relative paths:

    cp /usr/local/share/examples/mole/MSAlab/example.tre .
    
will copy the file named _example.tre_ to your current directory but will not change its name. Use ```ls``` to verify that your _myfolder_ directory now contains the file _example.tre_.

The move command (**mv**) can be used to move or rename files. Try renaming _tmp2.txt_ to _example.txt_:

    mv tmp2.txt example.txt

You can move the _example.txt_ file to your home folder using mv as well:

    mv example.txt ..
    
The above command moves the _example.txt_ file to the parent directory of your current directory. Use 

    ls ..

to check that it is in the parent directory.

**NOTE:** Do not move files that are not in your home directory or a subdirectory thereof. All files in shared or root folders are to be copied, never moved.

## Downloading files from the internet

In order to get a file from an online source you can use the **curl** command. Type:

    curl -O <url>

Where the ```<url>``` stands for the web address of the file you wish to download. For example

    curl -O https://molevolworkshop.github.io/assets/data/yule.tre
    
This will download the file _yule.tre_ to your present working directory. The **-O** flag is important: it tells curl that you wish to save the file under the same name as on the remote web site. Without specifying <tt>-O</tt>, curl will simply spill out the file contents to the console, which is not what you want in most cases.

For more info on using the linux shell check out the [Software Carpentry tutorial](https://swcarpentry.github.io/shell-novice/)

## Creating an alias for the example data directory

You can create an alias (known as a symbolic link, or symlink for short) to a directory to save a lot of future typing. Start by typing

    cd
    
to return to your home directory. Now type the following command to create a symbolic link named _eg_ that points to the directory _/usr/local/share/examples/mole_:

    ln -s /usr/local/share/examples/mole eg

Use the ls command to confirm that the symlink was indeed created:

    ls -l
    
Note that the long format shows the directory to which a symlink points. You can now show the contents of the _/usr/local/share/examples/mole_ directory with very little typing:

    ls eg

## Tips for making things easier

* Use the up arrow to see commands you have typed previously. This can save a lot of typing

* Type ```history``` to see a list of all your old commands. If you see the one you want, you can run it again using an exclamation point followed by the command number. For example, ```!24``` would re-execute command number 24.

* You can type Ctrl-R to search for a command you typed previously. Just start typing and, when you see the command you want, press enter to run it.

* If you use ```cd``` to navigate to a new directory, typing ```cd -`` takes you back to the previous directory.


