---
layout: page
title: Jetstream2 Setup Notes
permalink: /jetstream2/
---
These are notes on setting up Jetstream2 virtual machines for the MOLE workshop. If you are a participant, these notes are not intended for you, but you are of course welcome to read them. They are intended for the current directors and head TA of the workshop, who must get the Jetstream virtual machines up and running before the workshop begins. 

[Paul Lewis](mailto:paul.lewis@uconn.edu) created the first version of this document 18-Mar-2022. Whenever "I" or "me" appears in this document, it is Paul speaking.

## Introduction

Starting in 2022, the Workshop will use a "cluster in the cloud" for its computing needs.

The cluster we will be using is from the [Jetstream2](https://jetstream-cloud.org) project at Indiana University. Jetstream was NSF's first science and engineering research cloud, completed in early 2016 at a cost of $6.6M. Jetstream is one source of computing infrastructure provided under the umbrella of [Xsede](https://www.xsede.org), the Extreme Science and Engineering Discovery Environment, an NSF-sponsored program that provides cloud computing for researchers in academia. 

We (Peter Beerli and I) applied to Xsede for an educational **allocation** to provide enough computing resources for the Workshop in 2020. [Here](/assets/pdf/jetstream-proposal.pdf) is our proposal. We were awarded 207360.0 SUs (Service Units), which would allow 120 4-core virtual machines to run continuously for 18 days (120*4*24*18 = 207360 core*hours). The Workshop was sidelined in 2020 and again in 2021, so these computing resources have never actually been used to date for the Workshop.

[Jetstream2](https://jetstream-cloud.org) is just coming online this spring (2022) and while we could have continued to use Jetstream through the 2022 workshop, we were encouraged to go ahead and switch over to Jetstream2, which has the benefit of being better prepared for next year when Jetstream2 will be the only version available.

A [separate web page](/jetstream-setup/) documents how an image was built on Jetsream. Those notes are now obsolete as of March 2022. This document takes its place.

### Helful links

These have proven to be useful resources to have handy.

* [Jetstream2 home page](https://jetstream-cloud.org)
* [Jetstream2 documentation](https://docs.jetstream-cloud.org)
* [Exosphere](https://jetstream2.exosphere.app/)
* [Exosphere documentation](https://docs.jetstream-cloud.org/ui/exo/exo/)
* [Horizon home page](https://js2.jetstream-cloud.org/)
* [Jetstream2 API tutorial](https://github.com/jlf599/JetstreamAPITutorial)

## Most important!

Be sure to **shelve** instance if not planning to work with it for several hours. Shelving is the only option that does not burn SUs. **Suspending** burns SUs at 75% of the normal rate and **stopping** burns SUs at 50% the normal rate. See [Instance management actions](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/537460754/Instance+management+actions) for more info.

## Logging into Xsede User Portal

Login to [Xsede](https://www.xsede.org/).

You can **View Projedt Usage** by going to "Allocations/Usage" under the "My Xsede" tab.

You can **Manage Users** by going to "Allocations/Usage" under the "My Xsede" tab. This allows you to add new Xsede users to the allocation.

You can **add a user** to the project if that user has an Xsede account by going to "Add User" under the "My Xsede" tab.

## Logging into Exosphere

The [Exosphere web site](https://jetstream2.exosphere.app/) does for Jetstream2 what Atmosphere did for Jetstream: it is a graphical user interface for managing your allocation. I was able to login using my Xsede credentials and add our allocation to the Jetstream2 platform.

## SSH stuff

Using the red Create button in the upper right corner of Exosphere, I chose "SSH Public Key" to upload my ssh public key. I named it "cormy" and pasted in the contents of the public key file _~/.ssh/id_rsa.pub_ on my local laptop.

Create an entry in your _~/.ssh/config_ file to make it easy to login.
~~~~~~
Host jet
    HostName 149.165.156.59
    User plewis
    IdentityFile /Users/plewis/.ssh/id_rsa
    Cipher blowfish
~~~~~~    
        
Now ssh into the instance using the jet host set up in _.ssh/config_ file:
~~~~~~
ssh jet
~~~~~~

## Creating a new instance

To create a new instance, click the red Create button in the upper right corner of Exosphere. Note that one only needs to create a new instance this way in order to set up a virtual machine to serve as an image. After that point, it makes more sense to use the command line tools to create bunches of instances from that image.

I used the **Ubuntu 20_04 (latest)** image source and specified **MOLE_2022_image_basis** as the name. I chose **m3.small** as the flavor, **20 GB** root disk size (default for selected flavor), **1** for number of instances, **no** for enable web desktop, and **Show** for Advanced Options.

Advanced Options:

| Name                                     | Value                  | Default? |
| ---------------------------------------- | ---------------------- | -------- |
| Install operating system updates?        | Yes                    | Yes      |
| Deploy Guacamole for easy remote access? | Yes                    | Yes      |
| Network                                  | auto_allocated_network | Yes      |
| Public IP Address                        | Automatic              | Yes      |
| SSH Public Key                           | cormy                  | No       |
| Boot Script                              | see below              | Yes      |

### Boot script used

    #cloud-config
    users:
      - default
      - name: exouser
        shell: /bin/bash
        groups: sudo, admin
        sudo: ['ALL=(ALL) NOPASSWD:ALL']{ssh-authorized-keys}
    ssh_pwauth: true
    package_update: true
    package_upgrade: {install-os-updates}
    packages:
      - python3-virtualenv
      - git{write-files}
    runcmd:
      - echo on > /proc/sys/kernel/printk_devkmsg || true  # Disable console rate limiting for distros that use kmsg
      - sleep 1  # Ensures that console log output from any previous command completes before the following command begins
      - >-
        echo '{"status":"running", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
      - chmod 640 /var/log/cloud-init-output.log
      - {create-cluster-command}
      - |-
        (which virtualenv && virtualenv /opt/ansible-venv) || (which virtualenv-3 && virtualenv-3 /opt/ansible-venv) || python3 -m virtualenv /opt/ansible-venv
        . /opt/ansible-venv/bin/activate
        pip install ansible-core
        ansible-pull --url "{instance-config-mgt-repo-url}" --checkout "{instance-config-mgt-repo-checkout}" --directory /opt/instance-config-mgt -i /opt/instance-config-mgt/ansible/hosts -e "{ansible-extra-vars}" /opt/instance-config-mgt/ansible/playbook.yml
      - ANSIBLE_RETURN_CODE=$?
      - if [ $ANSIBLE_RETURN_CODE -eq 0 ]; then STATUS="complete"; else STATUS="error"; fi
      - sleep 1  # Ensures that console log output from any previous commands complete before the following command begins
      - >-
        echo '{"status":"'$STATUS'", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
    mount_default_fields: [None, None, "ext4", "user,exec,rw,auto,nofail,x-systemd.makefs,x-systemd.automount", "0", "2"]
    mounts:
      - [ /dev/sdb, /media/volume/sdb ]
      - [ /dev/sdc, /media/volume/sdc ]
      - [ /dev/sdd, /media/volume/sdd ]
      - [ /dev/sde, /media/volume/sde ]
      - [ /dev/sdf, /media/volume/sdf ]
      - [ /dev/vdb, /media/volume/vdb ]
      - [ /dev/vdc, /media/volume/vdc ]
      - [ /dev/vdd, /media/volume/vdd ]
      - [ /dev/vde, /media/volume/vde ]
      - [ /dev/vdf, /media/volume/vdf ]

Press the Create button to create the instance. The Exosphere GUI will say "Building" in orange for about 5 minutes, then "running Setup" for another minute, then "Ready" in green. Clicking on "Instances" will take you to a screen that shows the MOLE_2022_image_basis instance and its IP address.

You can now log into the instance as **exouser** (specified in the boot script).

    ssh exouser@149.165.159.178
    
The SSH public key specified will be used for authentication, so no password is needed. However, that will not work for the Workshop. You can set a password for exouser as follows:

    sudo passwd exouser
    
We will need to do this for all 62 instances we start at the workshop unless I can find a better solution.

## Setting up the new instance

The newly created MOLE_2022_image_basis needs to be provisioned with the software and data files used during the workshop.

### Finding basic information

Get current date:

    $ TZ="EST5EDT" date
    Fri Mar 18 17:33:29 EDT 2022

Find processor info:

    $ more /proc/cpuinfo
    processor	    : 0
    vendor_id	    : AuthenticAMD
    cpu family	    : 25
    model		    : 1
    model name	    : AMD EPYC-Milan Processor
    stepping	    : 1
    microcode	    : 0x1000065
    cpu MHz		    : 1996.249
    cache size	    : 512 KB
    physical id	    : 0
    siblings	    : 1
    core id		    : 0
    cpu cores	    : 1
    apicid		    : 0
    initial apicid	: 0
    fpu		        : yes
    fpu_exception	: yes
    cpuid level	    : 13
    wp		        : yes
    flags		    : fpu vme de pse ...
    bugs		    : sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
    bogomips	    : 3992.49
    TLB size	    : 1024 4K pages
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 40 bits physical, 48 bits virtual
    power management:
    
    ...info for processor 1 not shown...
    
Find 32 vs 64 bit:
    $ uname -m
    x86_64    
    
Find installed packages:

    $ sudo dpkg -l
    
To remove a package:

    $ sudo dpkg -r packagename # remove package itself
    $ sudo dpkg -P packagename # purge files associated with package

### Update operating system before doing any work
~~~~~~
sudo apt update
sudo apt upgrade
~~~~~~

### Install unzip
Not really necessary, already installed.
~~~~~~
sudo apt install -y unzip
~~~~~~
Last updated 2022-03-18.

### Install [R](https://www.r-project.org)
R is needed in order to precompile PhyloPlots.
~~~~~~
sudo apt-get install -y r-base
~~~~~~
Last updated 2022-03-18.

### Install zlib
Needed for migrate-n. Not really necessary, already installed.
~~~~~~
sudo apt install -y zlib1g-dev
~~~~~~
Last updated 2022-03-18.

### Install openmpi
Needed for migrate-n-mpi. 
~~~~~~
sudo apt-get install -y openmpi-bin 
sudo apt-get install -y libopenmpi-dev
~~~~~~
Last updated 2022-03-18.

### Install [migrate-n](https://peterbeerli.com/migrate-html5/index.html)
Migrate has its own lab in the workshop.
~~~~~~
cd
curl -LO http://peterbeerli.com/migrate-html5/download_version4/migrate-newest-src.tar.gz
tar zxvf migrate-newest-src.tar.gz
rm migrate-newest-src.tar.gz
cd migrate-5.0.2/src
./configure
make
sudo make install
make clean
make mpis
make install
~~~~~~
Installed as _/usr/local/bin/migrate-n_. 
Last updated 2022-03-18.

make install produces the following output: not sure whether this is worrisome

    Create the PDF library (libharu 1.x): [linker warnings are OK]
    Using system zlib architecture
    /bin/sh: 1: .: showgit.sh: not found
    Compile the main source files and create the executable
    
Got lots of linker errors trying to install mpi version, but it compiled just fine using "make mpis". Here are the first few errors:

    $ sudo make install
    Create the PDF library (libharu 1.x): [linker warnings are OK]
    Using system zlib architecture
    /bin/sh: 1: .: showgit.sh: not found
    Compile the main source files and create the executable
    /usr/bin/ld: menu.o: in function `get_menu':
    menu.c:(.text+0xb394): undefined reference to `ompi_mpi_long'
    /usr/bin/ld: menu.c:(.text+0xb3ae): undefined reference to `MPI_Bcast'
    /usr/bin/ld: menu.c:(.text+0xb3c5): undefined reference to `ompi_mpi_char'
    /usr/bin/ld: menu.c:(.text+0xb3ca): undefined reference to `MPI_Bcast'
    /usr/bin/ld: menu.c:(.text+0xb3d7): undefined reference to `MPI_Finalize'
    /usr/bin/ld: main.o: in function `main':
    main.c:(.text.startup+0x9b): undefined reference to `MPI_Init'
    .
    .
    .

### Install [Julia](https://julialang.org)

~~~~~~
cd
curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.7/julia-1.7.2-linux-x86_64.tar.gz
tar zxvf julia-1.7.2-linux-x86_64.tar.gz
rm julia-1.7.2-linux-x86_64.tar.gz
sudo mv julia-1.7.2 /opt/
cd /usr/local/bin
sudo ln -s /opt/julia-1.7.2/bin/julia julia
~~~~~~
This places the julia directory in _/opt_ and creates a symbolic link to the executable in _/usr/local/bin_.
Last updated 2022-03-18.

### Install Julia packages needed by the [PhyloNetworks tutorial](https://github.com/crsl4/PhyloNetworks.jl/wiki)
This follows the [instructions](https://github.com/crsl4/PhyloNetworks.jl/wiki) on the PhyloNetworks site.
~~~~~~
cd
julia
julia> using Pkg                # to use functions that manage packages
julia> Pkg.add("PhyloNetworks") # to download and install package PhyloNetworks
julia> Pkg.add("PhyloPlots")    # to download and install package PhyloPlots
julia> Pkg.add("RCall")         # package to call R from within julia
julia> Pkg.add("CSV")           # to read from / write to text files, e.g. csv files
julia> Pkg.add("DataFrames")    # to create & manipulate data frames
julia> Pkg.add("StatsModels")   # for regression formulas
julia> using PhyloNetworks      # may take some time: pre-compiles functions in the package
julia> using PhyloPlots         # may take some time: pre-compiles functions in the package
# use Ctrl-d to quit julia
~~~~~~
Last updated 2022-03-18.

### Install [MrBayes](https://nbisweden.github.io/MrBayes/)
MrBayes is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
curl -LO https://github.com/NBISweden/MrBayes/archive/v3.2.7a.tar.gz
tar zxvf v3.2.7a.tar.gz
rm v3.2.7a.tar.gz
cd MrBayes-3.2.7a/
# do not run autoconf as this will create errors in the configure script!
./configure
make
sudo make install
~~~~~~
Installed as _/usr/local/bin/mb_. 
Last updated 2022-03-18.

### Install [BUCKy](http://pages.stat.wisc.edu/~ane/bucky/index.html)
BUCKy is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
curl -LO http://dstats.net/download/http://www.stat.wisc.edu/~ane/bucky/v1.4/bucky-1.4.4.tgz
tar zxvf bucky-1.4.4.tgz
rm bucky-1.4.4.tgz
cd bucky-1.4.4/src
make
sudo mv bucky /usr/local/bin
sudo mv mbsum /usr/local/bin
~~~~~~
Last updated 2022-03-18.

### Install [maxcut](http://research.haifa.ac.il/~ssagi/)
maxcut is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
curl -LO http://research.haifa.ac.il/~ssagi/software/QMCN.tar.gz
# caution! QMCN.tar.gz does not create its own directory, so create a directory for it before unpacking
mkdir QMCN
mv QMCN.tar.gz QMCN
cd QMCN
tar zxvf QMCN.tar.gz
rm QMCN.tar.gz
sudo cp find-cut-Linux-64 /usr/local/bin 
~~~~~~
Installed as _/usr/local/bin/find-cut-Linux-64_. 
Last updated 2022-03-18.

### Install [RAxML](https://github.com/stamatak/standard-RAxML)
RAxML is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
cd 
git clone https://github.com/stamatak/standard-RAxML.git
cd standard-RAxML
make -f Makefile.AVX.PTHREADS.gcc
sudo mv raxmlHPC-PTHREADS-AVX /usr/local/bin/raxml
~~~~~~
Installed as _/usr/local/bin/raxml_. 
Last updated 2022-03-18.

### Install [Java](https://www.java.com/en/)
The Java Runtime Environment is needed for ASTRAL.
~~~~~~
cd
sudo apt install default-jre 
~~~~~~
Last updated 2022-03-18.

### Install [ASTRAL](https://github.com/smirarab/ASTRAL)
ASTRAL is used in the SNaQ tutorial. These instructions install the binary in _/opt/astral_. Note that the _/opt/astral/astral.5.7.3.jar_ jar file and the _/opt/astral/lib_ directory need to be owned by an ordinary user, otherwise the jar must be executed as root.
~~~~~~
#decided against using this version: curl -LO https://github.com/smirarab/ASTRAL/raw/master/Astral.5.7.3.zip
curl -LO https://github.com/smirarab/ASTRAL/archive/refs/tags/v5.7.1.zip
unzip v5.7.1.zip
rm v5.7.1.zip
sudo mkdir /opt/astral
cd ASTRAL-5.7.1
unzip Astral.5.7.1.zip
cd Astral
sudo cp astral.5.7.1.jar /opt/astral
sudo cp -r lib /opt/astral
~~~~~~
Last updated 2022-03-18.

### Create MOLE directory
This directory will be used to store example data needed by students for tutorials.
~~~~~~
sudo mkdir /usr/local/share/examples/mole
~~~~~~
Last updated 2022-03-15.

### Install data for [PhyloNetworks](http://crsl4.github.io/PhyloNetworks.jl/latest/) tutorial
~~~~~~
cd 
git clone https://github.com/crsl4/PhyloNetworks.jl.wiki.git
cd PhyloNetworks.jl.wiki
sudo mkdir /usr/local/share/examples/mole/phylo-networks
sudo mv data_results /usr/local/share/examples/mole/phylo-networks
~~~~~~

Modify line 46 of /usr/local/share/examples/mole/phylo-networks/data_results/scripts/raxml.pl to say:
~~~~~~
my $raxml = '/usr/local/bin/raxml'; # executable
~~~~~~

Modify line 47 of /usr/local/share/examples/mole/PhyloNetworks.jl.wiki/data_results/scripts/raxml.pl to say:
~~~~~~
my $astral = '/opt/astral/astral.5.7.1.jar'; # adapt to your system
~~~~~~
Last updated 2022-03-18.

### Download datasets for alignment tutorial
~~~~~~
cd 
curl -LO https://molevolworkshop.github.io/assets/data/MSAlab.zip
unzip MSAlab.zip
sudo mv MSAlab /usr/local/share/examples/mole/
~~~~~~
Last updated 2022-03-18.

### Install [MAFFT](https://mafft.cbrc.jp/alignment/software/)
Instructions below work except the man page is not installed because the makefile
tries to create the directory _/usr/local/share/man/man1_ will and issues and error when it
finds that that directory already exists. I didn't think the man page was all that important and thus did not try to fix the makefile.
~~~~~~
cd
curl -LO https://mafft.cbrc.jp/alignment/software/mafft-7.490-with-extensions-src.tgz    
tar zxvf mafft-7.490-with-extensions-src.tgz
rm mafft-7.490-with-extensions-src.tgz
cd mafft-7.490-with-extensions/core
make
sudo make install
~~~~~~
Installed into _/usr/local/bin/_. 

Got error upon install having to do with installing man file:

    mkdir -p /usr/local/share/man/man1
    mkdir: cannot create directory ‘/usr/local/share/man/man1’: File exists
    make: *** [Makefile:573: install] Error 1

Last updated 2022-03-18.

### Install [MUSCLE](https://www.drive5.com/muscle/)
~~~~~~
cd
curl -LO https://github.com/rcedgar/muscle/releases/download/v5.1/muscle5.1.linux_intel64
sudo mv muscle5.1.linux_intel64 /usr/local/bin/muscle
sudo chmod +x /usr/local/bin/muscle
~~~~~~
Installed as _/usr/local/bin/muscle_. 
Last updated 2022-03-18.

### Install [IQ-TREE](http://www.iqtree.org)
~~~~~~
cd
# install standard version
curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz
tar zxvf iqtree-1.6.12-Linux.tar.gz
rm iqtree-1.6.12-Linux.tar.gz
sudo cp iqtree-1.6.12-Linux/bin/iqtree /usr/local/bin
# install beta version needed for computing concordance factors
#curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v2.0-rc1/iqtree-2.0-rc1-Linux.tar.gz
curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v2.0.6/iqtree-2.0.6-Linux.tar.gz
tar zxvf iqtree-2.0.6-Linux.tar.gz
rm iqtree-2.0.6-Linux.tar.gz
sudo cp iqtree-2.0.6-Linux/bin/iqtree2 /usr/local/bin
~~~~~~
Installed 1.6.12 as _/usr/local/bin/iqtree_ and 2.0.6 as _/usr/local/bin/iqtree2_. 
Last updated 2022-03-18.

### Install [Boost C++](https://www.boost.org)

Needed in order to build RevBayes.
~~~~~~
cd
sudo apt-get install -y libboost-all-dev   # this takes awhile
~~~~~~
Last updated 2022-03-18.

### Install [RevBayes](https://revbayes.github.io/compile-linux)
~~~~~~
cd
# not necessary to issue this command --> sudo apt install build-essential cmake libboost-all-dev
git clone https://github.com/revbayes/revbayes.git
cd revbayes/projects/cmake
./build.sh # this step takes a really long time (34 minutes)! started: 8:48
sudo cp rb /usr/local/bin
~~~~~~
Installed as _/usr/local/bin/rb_. 
Last updated 2022-03-16.

### Install dataset for RevBayes tutorial
~~~~~~
cd
curl -O https://molevolworkshop.github.io/assets/data/rblabs.zip
unzip rblabs.zip
cd rblabs
sudo mkdir /usr/local/share/examples/mole/revbayes
sudo mv divtime /usr/local/share/examples/mole/revbayes/
sudo mv genetree /usr/local/share/examples/mole/revbayes/
~~~~~~
Last updated 2022-03-18.

### Install [PAUP*](http://phylosolutions.com/paup-test/)
~~~~~~
cd
curl -LO http://phylosolutions.com/paup-test/paup4a168_ubuntu64.gz
gunzip paup4a168_ubuntu64.gz
sudo mv paup4a168_ubuntu64 /usr/local/bin/paup
sudo chmod +x /usr/local/bin/paup
~~~~~~
Installed as _/usr/local/bin/paup_. 
Last updated 2022-03-18.

### Install [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html)
~~~~~~
cd
curl -LO http://abacus.gene.ucl.ac.uk/software/paml4.9j.tgz
tar zxvf paml4.9j.tgz
rm paml4.9j.tgz
cd paml4.9j/src
make -f Makefile
sudo mv baseml basemlg chi2 codeml evolver infinitesites mcmctree pamp yn00 /usr/local/bin
~~~~~~
Installed baseml, basemlg, chi2, codeml, evolver, infinitesites, mcmctree, pamp, and yn00in _/usr/local/bin_. 
Last updated 2022-03-18.

### Install data files for PAML lab
~~~~~~
cd
curl -O https://molevolworkshop.github.io/assets/data/PamlLab.zip
unzip PamlLab.zip
rm PamlLab.zip
sudo mv PamlLab /usr/local/share/examples/mole/
~~~~~~
Last updated 2022-03-18.

### Create alias to mole folder

Allows students to type moledir to go to the example data directory for the course.
~~~~~~
cd
cat - > mole-setup.sh
alias moledir="cd /usr/local/share/examples/mole"
# Ctrl-d to close file
sudo mv mole-setup.sh /etc/profile.d
~~~~~~
Last updated 2022-03-18.

## Create MOLE_2022_image

From the Exosphere home page, 

* click on Allocation TG-DEB190022
* click on Instance
* click on MOLE_2022_image_basis
* choose Image from the Actions menu

Provide **MOLE_2022_image** as the image name and save the image. This works extremely fast compared to the original Jetsream (almost instantanous). The image can be found in Home > Project TG-DEB190022 > Images (may have to click on "and 3 more images" to see MOLE_2022_image. The image is private so no worries about licenses.

## Command line client

### Obtaining CLI credentials

These instructions copied from the illustrated and more complete instructions at the [Setting up application credentials and openrc.sh for the Jetstream2 CLI](https://docs.jetstream-cloud.org/ui/cli/openrc/) page.

* Login to [Horizon](https://js2.jetstream-cloud.org/) using Xsede credentials
* Be sure it says xsede * TG-DEB190022 at the top dropdown box
* Choose Identity, then Application Credentials from the left sidebar menu
* Click "Create Application Credential" towards the top right
* Filled out form using entries below, then pressed the Create Application Credential button

| Field                    | Value                                       |
| ------------------------ | ------------------------------------------- |
| Name                     | POL-CLI-MOLE-credential                     |
| Description              | For Woods Hole MOLE project                 |
| Secret                   | not shown here, stored in password manager  |
| Expiration Date          |  07/01/2023                                 |
| Expiration Time          | left blank                                  |
| Roles                    | left blank                                  |
| Access Rules             | left blan                                   |
| Unrestricted (dangerous) | left unchecked                              |

Copied the ID provided in my password manager. 

The file _clounds.yaml_ was generated and placed here on my local laptop:

    ~/.config/openstack/clouds.yaml

The file _app-cred-POL-CLI-MOLE-credential-openrc.sh_ was generated and saved on my local hard drive. This file can be sourced to provide these environmental variables needed for authentication:

    OS_AUTH_TYPE
    OS_AUTH_URL
    OS_IDENTITY_API_VERSION
    OS_REGION_NAME
    OS_INTERFACE
    OS_APPLICATION_CREDENTIAL_ID
    OS_APPLICATION_CREDENTIAL_SECRET

### Using CLI

I have not put a lot of effort into learning how to control things using the API from scripts because Exosphere makes all these operations pretty simple. Thus, there are still a lot of TODO entries below.

Most of these instructions come from the [Jetstream2 API tutorial](https://github.com/jlf599/JetstreamAPITutorial).

You will need to install the openstack client on your local laptop (see [installing openstack](https://pypi.org/project/python-openstackclient/)):

    pip3 install python-openstackclient
    
You will need to source your openrc file (see last section):

    . app-cred-POL-CLI-MOLE-credential-openrc.sh
    
To show a list of flavors:

    openstack flavor list
    
To show a list of images:

    openstack image list

To show details for one particular image:

    openstack image show MOLE_2022_image --fit-width

To create an launch an instance (see [Launch and Access Your Instance](https://docs.jetstream-cloud.org/ui/cli/launch/)):

    TODO
        
To shelve or unshelve an instance (see [Instance Management Actions in the CLI](https://docs.jetstream-cloud.org/ui/cli/manage/)):

    TODO
    
    
To delete an instance (see [Deleting items in the CLI](https://docs.jetstream-cloud.org/ui/cli/deleting/)):

    TODO 
    
## Open issues

### Migrate-n-mpi

Could not get migrate-n-mpi to install

### Password access

The [General FAQ page](https://docs.jetstream-cloud.org/faq/general-faq/) says that one must use 

    sudo passwd username
    
to set a password for a user. It sounds like we will need to create 62+ passwords this way so that students can login the first time at least.

### Passphrase

What is the passphrase for an instance used for? Does not work as password when logging in.

### Instance limits

Exosphere says up to 25 instances can be run from one account. Can this be increased to, say, 75, or do we need three separate Xsede accounts?






