---
layout: page
title: Jetstream2 Setup Notes
permalink: /jetstream2024/
---
{% comment %}
https://www.webfx.com/tools/emoji-cheat-sheet/
{% endcomment %}

## Jetstream2 notes (2024 Workshop)

These are notes on setting up Jetstream2 virtual machines for the 2023 MOLE workshop. If you are a participant, these notes are not intended for you, but you are of course welcome to read them. They are intended for the current directors and head TA of the workshop, who must get the Jetstream virtual machines up and running before the workshop begins. 

[Paul Lewis](mailto:paul.lewis@uconn.edu) created this document 26-Apr-2024. Whenever "I" or "me" appears in this document, it is Paul speaking.

This document supersedes the original [Jetstream Setup Notes](/jetstream-setup/) and the later [Jetstream2 Setup Notes](/jetstream2022/).

## Introduction

Starting in 2022, the Workshop began using a "cluster in the cloud" for its computing needs.

The cluster we will be using is from the [Jetstream2](https://jetstream-cloud.org) project at Indiana University. Jetstream was NSF's first science and engineering research cloud, completed in early 2016 at a cost of $6.6M. Jetstream is one source of computing infrastructure provided under the umbrella of [Xsede](https://www.xsede.org), the Extreme Science and Engineering Discovery Environment, an NSF-sponsored program that provides cloud computing for researchers in academia. 

### History 

Peter Beerli and I applied to Xsede for an educational **allocation** to provide enough computing resources for the Workshop in 2020. [Here](/assets/pdf/jetstream-proposal.pdf) is our proposal. We were awarded 207360.0 SUs (Service Units), which would allow 120 4-core virtual machines to run continuously for 18 days (120*4*24*18 = 207360 core*hours). The Workshop was sidelined in 2020 and again in 2021.

[Jetstream2](https://jetstream-cloud.org) was just coming online in the spring of 2022 and, while we could have continued to use Jetstream through the 2022 workshop, we were encouraged to go ahead and switch over to Jetstream2, which had the benefit of being better prepared for the 2023 Workshop when Jetstream2 is the only version available.

Between the 2022 and 2023 Workshops, Xsede was replaced by [Access](https://access-ci.org). The Workshop directors (Peter Beerli, Laura Kubatko) and I submitted an [Explore ACCESS proposal](/assets/pdf/2022-11-24-ACCESS-proposal.pdf) in November 2022 asking for 68,080 SUs for the 2023 Workshop. We were actually granted 100,000 SUs.

For the 2024 workshop, we were granted an extension because we had used less than half of the SUs allocated for the 2023 workshop.

### Helful links

These have proven to be useful resources to have handy.

* [Jetstream2 status](https://jetstream.status.io/)
* [Jetstream2 home page](https://jetstream-cloud.org)
* [Jetstream2 documentation](https://docs.jetstream-cloud.org)
* [Exosphere](https://jetstream2.exosphere.app/)
* [Exosphere documentation](https://docs.jetstream-cloud.org/ui/exo/exo/)
* [Horizon home page](https://js2.jetstream-cloud.org/)
* [Jetstream2 API tutorial](https://github.com/jlf599/JetstreamAPITutorial)
* [Cloud-init examples](https://cloudinit.readthedocs.io/en/latest/reference/examples.html)

## Most important!

Be sure to **shelve** instance if not planning to work with it for several hours. Shelving is the only option that does not burn SUs. **Suspending** burns SUs at 75% of the normal rate and **stopping** burns SUs at 50% the normal rate. See [Instance management actions](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/537460754/Instance+management+actions) for more info.

{% comment %}
## Logging into Xsede User Portal

Login to [Xsede](https://www.xsede.org/).

You can **View Projedt Usage** by going to "Allocations/Usage" under the "My Xsede" tab.

You can **Manage Users** by going to "Allocations/Usage" under the "My Xsede" tab. This allows you to add new Xsede users to the allocation.

You can **add a user** to the project if that user has an Xsede account by going to "Add User" under the "My Xsede" tab.
{% endcomment %}

## Logging into Exosphere

[Exosphere](https://jetstream2.exosphere.app/) is a graphical user interface for managing your allocation. I was able to login using my Xsede credentials and add our allocation to the Jetstream2 platform.

## SSH stuff

Using the red Create button in the upper right corner of Exosphere, I chose "SSH Public Key" to upload my ssh public key. I named it "cormy" and pasted in the contents of the public key file _~/.ssh/id_rsa.pub_ on my local laptop.

Once you have created an instance to login to (see below), you can create an entry in your _~/.ssh/config_ file to make it easy to login.
~~~~~~
Host molevm
    HostName 149.165.156.59
    User plewis
    IdentityFile /Users/plewis/.ssh/id_rsa
    Cipher blowfish
~~~~~~    
        
Now you can ssh into the instance using the _molevm_ host set up in _.ssh/config_ file:
~~~~~~
ssh molevm
~~~~~~

## Creating the instance to be used as the base image

To create a new instance, click the red Create button in the upper right corner of Exosphere. 

I used the **Ubuntu 22.04 (latest)** image source and specified **MOLE-2023-base** as the name. I chose **m3.small** as the flavor, **20 GB** root disk size (default for selected flavor), **1** for number of instances, **no** for enable web desktop, **cormy** for SSH public key, and **Show** for Advanced Options.

Advanced Options:

| Name                                     | Value                  | Default? |
| ---------------------------------------- | ---------------------- | -------- |
| Install operating system updates?        | Yes                    | Yes      |
| Deploy Guacamole for easy remote access? | Yes                    | Yes      |
| Network                                  | auto_allocated_network | Yes      |
| Public IP Address                        | Automatic              | Yes      |
| Boot Script (see below)                  | used default           | Yes      |

Press the Create button to create the instance. The Exosphere GUI will say "Building" in lemon yellow for about 5 minutes, then "running Setup" for another minute, then "Ready" in green. Clicking on "Instances" will take you to a screen that shows the MOLE-2023-base instance and its IP address.

You can now log into the instance as **exouser**.

    ssh exouser@149.165.171.228
    
### Default boot script

For reference, here is the default boot script used to create MOLE-2023-base. 

~~~~~~
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
  - git{write-files}
runcmd:
  - echo on > /proc/sys/kernel/printk_devkmsg || true  # Disable console rate limiting for distros that use kmsg
  - sleep 1  # Ensures that console log output from any previous command completes before the following command begins
  - >-
    echo '{"status":"running", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
  - chmod 640 /var/log/cloud-init-output.log
  - {create-cluster-command}
  - (which apt-get && apt-get install -y python3-venv) # Install python3-venv on Debian-based platforms
  - (which yum     && yum     install -y python3)      # Install python3 on RHEL-based platforms
  - |-
    python3 -m venv /opt/ansible-venv
    . /opt/ansible-venv/bin/activate
    pip install --upgrade pip
    pip install ansible-core
    ansible-pull \
      --url "{instance-config-mgt-repo-url}" \
      --checkout "{instance-config-mgt-repo-checkout}" \
      --directory /opt/instance-config-mgt \
      -i /opt/instance-config-mgt/ansible/hosts \
      -e "{ansible-extra-vars}" \
      /opt/instance-config-mgt/ansible/playbook.yml
  - ANSIBLE_RETURN_CODE=$?
  - if [ $ANSIBLE_RETURN_CODE -eq 0 ]; then STATUS="complete"; else STATUS="error"; fi
  - sleep 1  # Ensures that console log output from any previous commands complete before the following command begins
  - >-
    echo '{"status":"'$STATUS'", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
~~~~~~

### Setting up the new instance

The newly created MOLE-2023-base needs to be provisioned with the software and data files used during the workshop.

First create a _TARs_ folder in which to store downloaded tar files (useful for backup purposes if, next year, some can't be downloaded). Also, create a _clones_ folder for git working directories.

~~~~~~
cd
mkdir TARs
mkdir clones
~~~~~~

### Finding basic information

Get current date:

    $ TZ="EST5EDT" date
    Sat Apr 29 12:48:00 EDT 2023

Find processor info:

    $ more /proc/cpuinfo
    processor	: 0
    vendor_id	: AuthenticAMD
    cpu family	: 25
    model		: 1
    model name	: AMD EPYC-Milan Processor
    stepping	: 1
    microcode	: 0x1000065
    cpu MHz		: 1996.250
    cache size	: 512 KB
    physical id	: 0
    siblings	: 1
    core id		: 0
    cpu cores	: 1
    apicid		: 0
    initial apicid	: 0
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm rep_good nopl cpuid extd_apicid tsc_kno
    wn_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetc
    h osvw topoext perfctr_core invpcid_single ssbd ibrs ibpb stibp vmmcall fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsa
    veerptr wbnoinvd arat npt nrip_save umip pku ospke vaes vpclmulqdq rdpid arch_capabilities
    bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
    bogomips	: 3992.50
    TLB size	: 1024 4K pages
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 40 bits physical, 48 bits virtual
    power management:

    processor	: 1
    vendor_id	: AuthenticAMD
    cpu family	: 25
    model		: 1
    model name	: AMD EPYC-Milan Processor
    stepping	: 1
    microcode	: 0x1000065
    cpu MHz		: 1996.250
    cache size	: 512 KB
    physical id	: 1
    siblings	: 1
    core id		: 0
    cpu cores	: 1
    apicid		: 1
    initial apicid	: 1
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm rep_good nopl cpuid extd_apicid tsc_kno
    wn_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetc
    h osvw topoext perfctr_core invpcid_single ssbd ibrs ibpb stibp vmmcall fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsa
    veerptr wbnoinvd arat npt nrip_save umip pku ospke vaes vpclmulqdq rdpid arch_capabilities
    bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
    bogomips	: 3992.50
    TLB size	: 1024 4K pages
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 40 bits physical, 48 bits virtual
    power management:
    
Find 32 vs 64 bit:
    $ uname -m
    x86_64    
    
Find installed packages:

    $ sudo dpkg -l
    
To remove a package (note: I didn't use this feature, but thought it good to keep the instructions):

    $ sudo dpkg -r packagename # remove package itself
    $ sudo dpkg -P packagename # purge files associated with package

### Update operating system before doing any work  

~~~~~~
$ sudo apt-add-repository universe
$ sudo apt update
$ sudo apt upgrade -y
~~~~~~
Last updated 2024-04-19.

### Install apt-file

This allows us to find out what files are installed by a package using "apt-file list packagename"
~~~~~~
sudo apt install -y apt-file
~~~~~~
This may pop up a graphical interface: use tab and arrow keys to navigate. May need to reboot, which can be done from the Exosphere interface.
Last updated 2024-04-19.

### Install python2

Some tutorials (e.g. SVDQuartets) still require python2.
~~~~~~
sudo apt install -y python2
~~~~~~
Last updated 2024-04-19.

### Install python-is-python3

This ensures that whenever someone types python they are using python3
~~~~~~
sudo apt install -y python-is-python3
~~~~~~
Last updated 2024-04-19.

### Install whois

This enables use of the mkpasswd command used to create the hashed password used in the cloud-init script.
~~~~~~
sudo apt install -y whois
~~~~~~
Last updated 2024-04-19.

### Install mlocate

This provides the locate command, useful for finding where libraries and other system files are installed.
~~~~~~
sudo apt install -y mlocate
~~~~~~
Last updated 2024-04-19.

### Install unzip

Not really necessary, already installed.
~~~~~~
sudo apt install -y unzip
~~~~~~
Last updated 2024-04-19.

### Install [R](https://www.r-project.org)

R is needed in order to precompile PhyloPlots.
~~~~~~
sudo apt-get install -y r-base
~~~~~~
Last updated 2024-04-19.

### Install zlib

Needed for migrate-n. Not really necessary, already installed.
~~~~~~
sudo apt install -y zlib1g-dev
~~~~~~
Last updated 2024-04-19.

### Install openmpi

Needed for migrate-n-mpi. 
~~~~~~
sudo apt-get install -y openmpi-bin 
sudo apt-get install -y libopenmpi-dev
sudo apt-get install -y openmpi-common
~~~~~~
Last updated 2024-04-19.

### Install [migrate-n](https://peterbeerli.com/migrate-html5/index.html)

Migrate has its own lab in the workshop.
~~~~~~
cd
curl -LO https://peterbeerli.com/migrate-html5/download_version4/migrate-newest.src.tar.gz
tar xvf migrate-newest.src.tar.gz  # note had to leave off z even though file ends in .gz
mv migrate-5.0.4.src.tar.gz TARs
cd migrate-5.0.4/src
./configure
make
sudo make install
make clean
make mpis
sudo make installmpi
~~~~~~
Installed as _/usr/local/bin/migrate-n_ and _/usr/local/bin/migrate-n-mpi_. Version 5.0.4 installed.
Last updated 2024-04-19.

### Install [Julia](https://julialang.org)

Julia is needed for Claudia's PhyloNetworks tutorial.

From [Julia downloads](https://julialang.org/downloads/) web site, select the Generic Linux and x86 64-bit (glibc) version.
~~~~~~
cd
curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-x86_64.tar.gz
tar zxvf julia-1.10.2-linux-x86_64.tar.gz
mv julia-1.10.2-linux-x86_64.tar.gz TARs
sudo mv julia-1.10.2 /opt/
cd /usr/local/bin
sudo ln -s /opt/julia-1.10.2/bin/julia julia
~~~~~~
This places the julia directory in _/opt_ and creates a symbolic link to the executable in _/usr/local/bin_.
Last updated 2024-04-19.

### Install Julia packages needed by the [PhyloNetworks tutorial](https://github.com/crsl4/PhyloNetworks.jl/wiki)

This follows the [instructions](https://github.com/crsl4/PhyloNetworks.jl/wiki) on the PhyloNetworks site. Also see [instructions in this post](https://stackoverflow.com/questions/32338701/install-just-one-package-globally-on-julia) and [this post](https://stackoverflow.com/questions/61273734/setting-up-a-centralized-julia-library-repository) on installing Julia packages globally. In particular, defining the JULIA_DEPOT_PATH environmental variable specifies the location where Julia packages will be installed.

To 
~~~~~~
cd
export JULIA_DEPOT_PATH=/opt/julia-1.8.5/usr/share/julia/site
julia
julia> using Pkg                # to use functions that manage packages
julia> Pkg.add("PhyloNetworks") # to download/install PhyloNetworks (precompiling takes a few minutes)
julia> Pkg.add("PhyloPlots")    # to download/install PhyloPlots (precompiling takes a few minutes)
julia> Pkg.add("RCall")         # package to call R from within julia
julia> Pkg.add("CSV")           # to read from / write to text files, e.g. csv files
julia> Pkg.add("DataFrames")    # to create & manipulate data frames
julia> Pkg.add("StatsModels")   # for regression formulas
julia> using PhyloNetworks      # check whether it loads
julia> using PhyloPlots         # check whether it loads
julia> Pkg.status()             # useful for seeing what packages are installed
julia> pathof(PhyloNetworks)    # useful for seeing where the package was installed
# use Ctrl-d to quit julia
~~~~~~
Last updated 2024-04-19.

### Install [Boost C++](https://www.boost.org)

Needed in order to build RevBayes and BUCKy.
~~~~~~
cd
sudo apt install -y libboost-all-dev
~~~~~~
Last updated 2024-04-19.

### Install [RevBayes](https://revbayes.github.io/compile-linux)

This install takes a long time (30 minutes), so start it in one console and open another to work on other installs while this is running.
~~~~~~
cd ~/clones
# not necessary to issue this command --> sudo apt install build-essential cmake libboost-all-dev
git clone https://github.com/revbayes/revbayes.git
cd revbayes/projects/cmake
./build.sh 
sudo mv rb /usr/local/bin
~~~~~~
Installed as _/usr/local/bin/rb_. This is RevBayes version 1.2.1.
Last updated 2024-04-19.

### Install [MrBayes](https://nbisweden.github.io/MrBayes/)

MrBayes is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
cd
curl -LO https://github.com/NBISweden/MrBayes/archive/v3.2.7a.tar.gz
tar zxvf v3.2.7a.tar.gz
mv v3.2.7a.tar.gz TARs
cd MrBayes-3.2.7a/
# do not run autoconf as this will create errors in the configure script!
./configure
make
sudo make install
~~~~~~
Installed as _/usr/local/bin/mb_. 
Last updated 2024-04-19.

### Install [BUCKy](http://pages.stat.wisc.edu/~ane/bucky/index.html)

BUCKy is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
cd
curl -LO http://dstats.net/download/http://www.stat.wisc.edu/~ane/bucky/v1.4/bucky-1.4.4.tgz
tar zxvf bucky-1.4.4.tgz
mv bucky-1.4.4.tgz TARs
cd bucky-1.4.4/src
make
sudo mv bucky /usr/local/bin
sudo mv mbsum /usr/local/bin
~~~~~~
Note: in order to get BUCKy to compile, I had to qualify `unordered_map` as `boost::unordered_map` in two lines (line 163 and 357) in _TGM.h_ because an `unordered_map` template is defined in both _./boost/unordered/unordered_map_fwd.hpp_ and _/usr/include/c++/11/bits/unordered_map.h_.
Last updated 2024-04-19.

### Install [RAxML](https://github.com/stamatak/standard-RAxML)

RAxML is used in the Solis-Lemus SNaQ and McTavish gene tree updating tutorial. These instructions install the binary in _/usr/local/bin_. Note: it is easier to just use "sudo apt-get install raxml" to do this install, but I didn't realize this at the time.
~~~~~~
cd ~/clones
git clone https://github.com/stamatak/standard-RAxML.git
cd standard-RAxML
make -f Makefile.AVX.PTHREADS.gcc
sudo mv raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC
rm *.o  # no make clean available
~~~~~~
Installed as _/usr/local/bin/raxmlHPC_.
Last updated 2024-04-19.

### Install [Java](https://www.java.com/en/)

The Java Runtime Environment is needed for ASTRAL and jModelTest.
~~~~~~
cd
sudo apt install default-jre  # not really necessary, already installed
~~~~~~
Last updated 2024-04-19.

### Install [ASTRAL](https://github.com/smirarab/ASTRAL)

ASTRAL is used in the SNaQ tutorial. These instructions install the binary in _/opt/astral_. Note that the _/opt/astral/astral.5.7.3.jar_ jar file and the _/opt/astral/lib_ directory need to be owned by an ordinary user, otherwise the jar must be executed as root.
~~~~~~
cd
curl -LO https://github.com/smirarab/ASTRAL/archive/refs/tags/v5.7.1.tar.gz
tar zxvf v5.7.1.tar.gz
mv v5.7.1.tar.gz TARs
sudo mkdir /opt/astral
cd ASTRAL-5.7.1
unzip Astral.5.7.1.zip
cd Astral
sudo cp astral.5.7.1.jar /opt/astral
sudo cp -r lib /opt/astral
~~~~~~

You should now be able to start ASTRAL as follows:
    sudo java -jar /opt/astral/astral.5.7.1.jar
An alias will be created by the [cloud init script](#boot-script-used) to make this easier.
    alias astral="java -jar /opt/astral/astral.5.7.1.jar"
The [cloud init script](#boot-script-used) will also change ownership to moleuser:
    sudo chown moleuser.moleuser /opt/astral/astral.5.7.1.jar
    sudo chown moleuser.moleuser /opt/astral/lib -R
Last updated 2024-04-19.

### Create MOLE directory

This directory will be used to store example data needed by students for tutorials.
~~~~~~
sudo mkdir /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install data for [PhyloNetworks](http://crsl4.github.io/PhyloNetworks.jl/latest/) tutorial

~~~~~~
cd ~/clones
git clone https://github.com/crsl4/PhyloNetworks.jl.wiki.git
cd PhyloNetworks.jl.wiki
sudo mkdir /usr/local/share/examples/mole/phylo-networks
sudo cp -R data_results /usr/local/share/examples/mole/phylo-networks
~~~~~~

Modify line 46 of /usr/local/share/examples/mole/phylo-networks/data_results/scripts/raxml.pl to say:
~~~~~~
my $raxml = '/usr/local/bin/raxmlHPC'; # executable
~~~~~~

Modify line 47 of /usr/local/share/examples/mole/phylo-networks/data_results/scripts/raxml.pl to say:
~~~~~~
my $astral = '/opt/astral/astral.5.7.1.jar'; # adapt to your system
~~~~~~
Last updated 2024-04-19.

### Download and install various datasets used in tutorials

The repository [github.com/molevolworkshop/moledata](https://github.com/molevolworkshop/moledata) stores many data sets used in the workshop.
~~~~~~
cd ~/clones
git clone https://github.com/molevolworkshop/moledata.git
~~~~~~
Should add phylo-networks to this repository.
Last updated 2024-04-19.

### Install datasets for alignment tutorial

~~~~~~
cd clones/moledata
sudo unzip MSAlab.zip -d /usr/local/share/examples/mole 
~~~~~~
Last updated 2024-04-19.

### Install datasets for the migrate tutorial

~~~~~~
cd clones/moledata
sudo unzip migrate_tutorial.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install datasets for the Model Selection/Simulation tutorial

~~~~~~
cd clones/moledata
sudo unzip modsel_sim_tutorial.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install datasets for the SVDQuartets tutorial

~~~~~~
cd clones/moledata
sudo unzip svdquartets_tutorial.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install data files for the PAML lab

~~~~~~
cd clones/moledata
sudo unzip PamlLab.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install data files for the IQ-TREE lab

~~~~~~
cd clones/moledata
sudo unzip iqtreelab.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install dataset for RevBayes tutorial

~~~~~~
cd clones/moledata
sudo unzip revbayes.zip -d /usr/local/share/examples/mole
~~~~~~
Last updated 2024-04-19.

### Install data files for the phylogenomics lab

These files are used in the McTavish tree updating and tree comparison labs. They depend on opentree and RAxML. Note that the git repository cloned here may not actually be needed: the tutorial will be accessed by participants via the [Phylogenomics tutorial web site](https://github.com/snacktavish/Mole2023), which has them clone from the same git repostory. The setup below just provides a backup of these files on the virtual machines themselves.
~~~~~~
cd ~/clones
git clone  https://github.com/snacktavish/Mole2023.git
sudo cp -R Mole2023 /usr/local/share/examples/mole/
~~~~~~
Last updated 2024-04-19.

### Set permissions and remove mac-specific dir
~~~~~~
cd /usr/local/share/examples/mole
sudo rm -rf __MACOSX
sudo chmod 755 modsel_sim_tutorial
~~~~~~

### Install [MAFFT](https://mafft.cbrc.jp/alignment/software/)

~~~~~~
cd
curl -LO https://mafft.cbrc.jp/alignment/software/mafft-7.505-with-extensions-src.tgz    
tar zxvf mafft-7.505-with-extensions-src.tgz
mv mafft-7.505-with-extensions-src.tgz TARs
cd mafft-7.505-with-extensions/core
make
sudo make install
~~~~~~
Installed into _/usr/local/bin/_. 
Last updated 2024-04-19.

### Install [MUSCLE](https://www.drive5.com/muscle/)

MUSCLE is used in the alignment lab as well as the McTavish gene tree updating lab. 
~~~~~~
sudo apt install -y muscle
~~~~~~
Last updated 2024-04-19.

### Install seqtk

seqtk is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt install -y seqtk 
~~~~~~
Last updated 2024-04-19.

### Install samtools

samtools is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt install -y samtools 
~~~~~~
Last updated 2024-04-19.

### Install bcftools

bcftools is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt install -y bcftools
~~~~~~
Last updated 2024-04-19.

### Install fastx

The fastx toolkit is used in McTavish gene tree updating lab. fastx toolkit and bwa-mem are not available through apt.
~~~~~~
cd
curl -LO http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
tar -xjf fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
mv fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2 TARs
sudo mv bin/* /usr/local/bin/
rm -rf bin
~~~~~~

Installs the following executables in _/usr/local/bin_:
~~~~~~
fasta_clipping_histogram.pl
fasta_formatter
fasta_nucleotide_changer
fastq_masker
fastq_quality_boxplot_graph.sh
fastq_quality_converter
fastq_quality_filter
fastq_quality_trimmer
fastq_to_fasta
fastx_artifacts_filter
fastx_barcode_splitter.pl
fastx_clipper
fastx_collapser
fastx_nucleotide_distribution_graph.sh
fastx_nucleotide_distribution_line_graph.sh
fastx_quality_stats
fastx_renamer
fastx_reverse_complement
fastx_trimmer
fastx_uncollapser
~~~~~~
Last updated 2023-04-29.

### Install bwa-mem2

bwa-mem2 is used in McTavish gene tree updating lab.
~~~~~~
cd ~/clones
git clone --recursive https://github.com/bwa-mem2/bwa-mem2
cd bwa-mem2
make
sudo mv ./bwa-mem2* /usr/local/bin/
rm ./src/*.o
~~~~~~
This installs the following binaries in _/usr/local/bin/_:
~~~~~~
bwa-mem2
bwa-mem2.avx
bwa-mem2.avx2
bwa-mem2.avx512bw
bwa-mem2.sse41
bwa-mem2.sse42
~~~~~~
Last updated 2023-04-29.

### Install [maxcut](https://sagi-snir.wixsite.com/snir-lab/maxcut)

#### TODO

Sagi Snir's maxcut is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
The software (v. 2.1) is no longer available from [here](http://research.haifa.ac.il/~ssagi/software/QMCN.tar.gz). Sagi suggested we use version 3.0 from [this dryad repository](https://datadryad.org/stash/dataset/doi:10.5061/dryad.r9k57). While that may work, the SNaQ tutorial has not been tested with this version of MaxCut, so this year we are using an archived copy of the `QMCN.tar.gz` file that I scp'd onto the virtual machine.
~~~~~~
# caution! QMCN.tar.gz does not create its own directory, so create a directory for it before unpacking
cd
mkdir QMCN
cp ./TARs/QMCN.tar.gz QMCN
cd QMCN
tar zxvf QMCN.tar.gz
rm QMCN.tar.gz
sudo cp find-cut-Linux-64 /usr/local/bin 
~~~~~~
Installed as _/usr/local/bin/find-cut-Linux-64_. 
Last updated 2023-04-29.

### Install [IQ-TREE](http://www.iqtree.org)

Used for the IQ-TREE tutorial.
~~~~~~
cd
# install standard version
curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz
tar zxvf iqtree-1.6.12-Linux.tar.gz
mv iqtree-1.6.12-Linux.tar.gz TARs
sudo mv iqtree-1.6.12-Linux/bin/iqtree /usr/local/bin

# install beta version needed for computing concordance factors
curl -LO https://github.com/iqtree/iqtree2/releases/download/v2.2.0/iqtree-2.2.0-Linux.tar.gz
tar zxvf iqtree-2.2.0-Linux.tar.gz
mv iqtree-2.2.0-Linux.tar.gz TARs
sudo mv iqtree-2.2.0-Linux/bin/iqtree2 /usr/local/bin
~~~~~~
Installed 1.6.12 as _/usr/local/bin/iqtree_ and 2.0.6 as _/usr/local/bin/iqtree2_. 
Last updated 2023-04-29.

### Install [libpython2.7.so.1.0 shared library](https://askubuntu.com/questions/1213461/cant-locate-libpython2-7-so-1-0)

The file _libpython2.7.so.1.0_ is required for PAUP*. 
~~~~~~
sudo apt install -y libpython2.7
~~~~~~

Installed as _/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0_. 
Last updated 2023-04-29.

### Install [jModelTest](https://github.com/ddarriba/jmodeltest2/)

Used in the PAUP tutorial.
~~~~~~
cd
curl -LO https://github.com/ddarriba/jmodeltest2/files/157117/jmodeltest-2.1.10.tar.gz
tar zxvf jmodeltest-2.1.10.tar.gz
mv jmodeltest-2.1.10.tar.gz TARs
sudo cp -r jmodeltest-2.1.10 /opt
~~~~~~

You should now be able to start jModelTest as follows, but will spit out error message `ERROR: You are trying to run a GUI interface in a headless server.`:
    sudo java -jar /opt/jmodeltest-2.1.10/jModelTest.jar    
An alias will be created by the [cloud init script](#boot-script-used) to make this easier.
    alias jmodeltest="java -jar /opt/jmodeltest-2.1.10/jModelTest.jar"
The [cloud init script](#boot-script-used) will also change ownership
    sudo chown -R moleuser.moleuser /opt/jmodeltest-2.1.10
Last updated 2023-05-06.

### Install [PAUP*](http://phylosolutions.com/paup-test/)

~~~~~~
cd
curl -LO http://phylosolutions.com/paup-test/paup4a168_ubuntu64.gz
cp paup4a168_ubuntu64.gz TARs
gunzip paup4a168_ubuntu64.gz
sudo mv paup4a168_ubuntu64 /usr/local/bin/paup
sudo chmod +x /usr/local/bin/paup
~~~~~~
Installed as _/usr/local/bin/paup_. 
Last updated 2023-04-29.

### Install [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html)

Downloaded the linux version 4.9j from the old-versions page. Hopefully next year we'll be
able to use the most recent version on the github site. 

Version 4.9j failed to link due to the inclusion of a couple of enum definitions (`SeqTypes` and `OutTreeOptions`) in _paml.h_. I copied those definitions to a new file _enums.c_, included that file in each target of the Makefile, and added `extern` in front of each of these in _paml.h_ and the build went smoothly.
~~~~~~
cd
#curl -LO https://github.com/abacus-gene/paml/releases/download/v4.10.7/paml-4.10.7-linux-X86_64.tgz
tar zxvf paml4.9j.tgz
mv paml4.9j.tgz TARs
cd paml4.9j/src
make -f Makefile
sudo mv baseml basemlg chi2 codeml evolver infinitesites mcmctree pamp yn00 /usr/local/bin
~~~~~~
Installed baseml, basemlg, chi2, codeml, evolver, infinitesites, mcmctree, pamp, and yn00in _/usr/local/bin_. 
Last updated 2023-05-10.

### Create pyenv python virtual environment

Python modules used in the McTavish tree comparison tutorial are installed into a virtual environment named pyenv. This may not be used, as the tutorial specify for the students to install python modules themselves (which will be installed in _~/.local_), but it is installed if we end up needing it.
~~~~~~
sudo chown -R exouser.exouser /usr/local/share/examples/mole/Mole2024
cd /usr/local/share/examples/mole/Mole2024
python -m venv pyenv
~~~~~~

### Install DendroPy ([DendroPy](https://dendropy.org/downloading.html))

DendroPy is used in the McTavish gene tree updating lab.
~~~~~~
source /usr/local/share/examples/mole/Mole2023/pyenv/bin/activate    # activate the python environment pyenv
python -m pip install git+https://github.com/jeetsukumaran/DendroPy.git
python -m pip list
deactivate
~~~~~~
Last updated 2023-04-29.

### Install opentree

opentree is used in the McTavish gene tree updating lab.
~~~~~~
source /usr/local/share/examples/mole/Mole2023/pyenv/bin/activate    # activate the python environment pyenv
python -m pip install opentree
python -m pip list
deactivate
~~~~~~
Last updated 2023-04-29.

### Install the machine learning Jupyter notebook

The machine learning tutorial is in the form of a Jupyter notebook. The notebook itself is saved to the `/usr/local/share/examples/mole/machinelearning` directory (but is also available on Megan Smith's faculty page).
~~~~~~
cd
curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Machine_Learning_for_Population_Genetics.ipynb
curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Models-01.png
sudo mkdir -p /usr/local/share/examples/mole/machinelearning
sudo mv Machine_Learning_for_Population_Genetics.ipynb /usr/local/share/examples/mole/machinelearning
sudo chown -R exouser.exouser /usr/local/share/examples/mole/machinelearning
~~~~~~
Last updated 2024-04-25.

#### Create a virtual python environment mlenv

The following installs the python packages required by the notebook. Just to be safe, I created a different virtual python environment (mlenv) for these installs. The specific versions of each module were specified in the Jupyter script used for the tutorial, so I stuck to those versions to make sure everything was compatible.
~~~~~~
module list   # ensure anaconda is not loaded
cd /usr/local/share/examples/mole/machinelearning
python -m venv mlenv            # create python virtual environment mlenv
source ./mlenv/bin/activate     # activate the python virtual environment mlenv
python -m pip install msprime==1.2.0
python -m pip install numpy==1.23.5
python -m pip install scipy==1.9.3
python -m pip install scikit-learn==1.2.0
python -m pip install tensorflow==2.10.0
python -m pip install keras==2.10.0   # not really needed; already installed by tensorflow
python -m pip install ipykernel
deactivate
~~~~~~
Last updated 2024-04-25.

While the mlenv is activated, calling
    python -m pip freeze > mlmodules.txt
will save the versions of all modules currently loaded to a file. If you need to recreate the environment later, you can install all of these at once using (again, while mlenv is activated)
    python -m pip install -r mlmodules.txt
You can use 
    python -m pip list
to list modules installed in the virtual environment.

Last updated 2024-04-25.

#### Create a Jupyter kernel that uses mlenv 

Jupyter comes with the anaconda module, but the anaconda module specifies a default Jupiter kernel that does not have the modules needed by the machine learning tutorial installed. Thus, we need to create a Jupyter kernel that uses the python virtual environment mlenv that we set up in the previous step. The easiest way to create the new kernel is to copy the default one and change the name and path to the python interpreter.

~~~~~~
mkdir -p /usr/local/share/examples/mole/machinelearning/jupyter/molekernel
cd /usr/local/share/examples/mole/machinelearning/jupyter/molekernel
module load anaconda
jupyter kernelspec list  # shows location of default kernel
#Available kernels:
#  python3       /software/u22/anaconda/python3.9/share/jupyter/kernels/python3
cp -r /software/u22/anaconda/python3.9/share/jupyter/kernels/python3/* .
# Edit the kernel.json file to look like this:
{
 "argv": [
  "/usr/local/share/examples/mole/machinelearning/mlenv/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "MOLE",
 "language": "python",
 "metadata": {
  "debugger": true
 }
}
~~~~~~

#### Create setup.sh script to start Jupyter notebook

Create a _setup.sh_ script to make it easier for students to start Jupyter. The `jupyter-ip.sh` script comes with the virtual machines and is available once anaconda is loaded. It starts a server and displays various ways to access the Jupyter notebook in your browser (I normally use the last URL listed).

The students will have to be told to choose the **MOLE** kernel once Jupyter starts up and they have loaded the notebook (which they should see when Jupyter starts).

I found that the sample sizes specified in the notebook were large enough that the kernel ran out of memory and crashed after the data was simulated and the analyses began. Cutting fragments to 10 (instead of 20), replicates to 500 (instead of 1000), and SNPs to 2000 (instead of 5000) was sufficient to allow it to run to completion.

~~~~~~
cd /usr/local/share/examples/mole/machinelearning
cat - > doof.sh << EOF
#!/bin/bash

echo "Ensuring anaconda is loaded (to make Jupyter available)..."
module unload anaconda
module load anaconda

echo "Activating the python environment for this tutorial..."
source /usr/local/share/examples/mole/machinelearning/mlenv/bin/activate

if [ ! -d "/home/moleuser/.local/share/jupyter/kernels/molekernel" ]
then
	echo "Installing molekernel for use with Jupyter..."
	jupyter kernelspec install /usr/local/share/examples/mole/machinelearning/jupyter/molekernel --user
else
	echo "No need to install molekernel because it already exists."
fi

echo "Starting up Jupyter server..."
jupyter-ip.sh
EOF
~~~~~~

### Creating a shared read-only volume for the python virtual environment

**Note: need to remove instructions about creating mlenv above and will need a script to mount this volume on all VMs **

The python virtual environment used in the machine learning tutorial is large (1.8GB) and thus locating it on each VM brings these machines 1.8GB closer to their 20GB maximum disk space. To save space on the individual VMs used by participants and faculty, I created a volume to hold just the python virtual environment that is used for both the machine learning and opentree labs. This volume is attached to MOLE-2023-base and shared with all other VMs via NFS.

#### Creating and populating a volume

In Exosphere, choose Create > Volume using the red Create button at the top right. Attach the volume to MOLE-2023-base using the Attach Volume button under the Volumes panel when viewing the details of the MOLE-2023-base instance. The volume will be mounted at _/media/volume/sdb_.

Assuming you are logged into MOLE-2023-base as exouser, create a python virtual environment as follows:
~~~~~~
cd /media/volume/sdb
python -m venv pyenv            # create python virtual environment
source ./pyenv/bin/activate     # activate the python virtual environment
python -m pip install msprime==1.2.0
python -m pip install numpy==1.23.5
python -m pip install scipy==1.9.3
python -m pip install scikit-learn==1.2.0
python -m pip install tensorflow==2.10.0
python -m pip install keras==2.10.0   # not really needed; already installed by tensorflow
python -m pip install ipykernel
python -m pip install opentree
python -m pip install git+https://github.com/jeetsukumaran/DendroPy.git
deactivate
sudo chown -R moleuser.moleuser pyenv
~~~~~~

#### Setting up the NFS server on MOLE-2023-base

See [this explanation](https://bluexp.netapp.com/blog/azure-anf-blg-linux-nfs-server-how-to-set-up-server-and-client#H_H9) for basic NFS setup and [this one](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking) for an explanation of specifying IP ranges.
~~~~~~
sudo apt install -y nfs-kernel-server
sudo vi /etc/exports
# The example below shows exporting to just one VM
#   /media/volume/sdb/mole 149.165.173.134(ro,sync,no_subtree_check)
# The example below exports to a range of IP addresses (specifically 149.165.173.132, 149.165.173.133, 149.165.173.134, 149.165.173.135)
#   /media/volume/sdb/mole 149.165.173.134/30(ro,sync,no_subtree_check)
# The same example as above but spread across 4 lines
#   /media/volume/sdb/mole 149.165.173.132(ro,sync,no_subtree_check)
#   /media/volume/sdb/mole 149.165.173.133(ro,sync,no_subtree_check)
#   /media/volume/sdb/mole 149.165.173.134(ro,sync,no_subtree_check)
#   /media/volume/sdb/mole 149.165.173.135(ro,sync,no_subtree_check)
# The same example but on one long line:
#   /media/volume/sdb/mole 149.165.173.132(ro,sync,no_subtree_check) 149.165.173.133(ro,sync,no_subtree_check) 149.165.173.134(ro,sync,no_subtree_check) 149.165.173.135(ro,sync,no_subtree_check)
sudo systemctl restart nfs-kernel-server
~~~~~~

#### Setting up the NFS client

Assuming 149.165.173.177 is the ip address of MOLE-2023-base:
~~~~~~
sudo mkdir /var/pyenv
sudo chown moleuser.moleuser /var/pyenv
sudo mount -t nfs 149.165.173.177:/media/volume/sdb/pyenv /var/pyenv
# use the following command to unmount
# sudo umount /var/pyenv  # can also use -f (force) and/or -l (lazy) switches
~~~~~~

(Not sure this is necessary or desirable.) The above mount command sets up NFS sharing temporarily. To automate this so that the share is mounted on startup:
~~~~~~
sudo vi /etc/fstab
# Insert line similar to the following
# 149.165.173.177:/media/volume/sdb/mole /var/mole nfs defaults 0 0
sudo mount /var/mole
sudo mount 149.165.173.177:/media/volume/sdb/mole
~~~~~~

## Locking an instance

It is wise to lock the _MOLE-2023-base_ instance as soon as you are finished setting it up. To do this, choose **Lock** from the **Actions** menu when you are viewing the details of the _MOLE-2023-base_ instance. Locking prevents you from doing something stupid, like deleting this image accidentally. It is easy to unlock it any time you need to, but it is much harder to recreate it after accidentally deleting it! I tend to keep all instances locked unless I find there is some action that requires unlocking.

## Create MOLE-2023-snapshot

Once the **MOLE-2023-base** VM is set up and running, you can create a **snapshot** image using the Actions menu. I name these snapshot images something like **MOLE-2023-snapshot-05-12** (where the 05-12 part is the date) and make additional snapshots (deleting the really old ones) as changes are made to MOLE-2023-base.

Note that MOLE-2023-snapshot-05-12 will show `0 B` initially when viewed in the Images list. Not to worry; the size will be updated when the image is fully created.

## Creating instances based on MOLE-2023-snapshot-05-12

To create new instances, click the red _Create_ button in the upper right corner of Exosphere, then choose _Instance_ and then, in the _Choose an Instance Source_ section, click the _By Image_ tab and hit the _Create Instance_ button beside MOLE-2023-snapshot-05-12.

Choose a base name (e.g. "amphioxus"), **m3.small** as the flavor, **20 GB** root disk size (default for selected flavor), **62** for number of instances, **no** for enable web desktop, and **Show** for Advanced Options.

Advanced Options:

| Name                                     | Value                  | Default? |
| ---------------------------------------- | ---------------------- | -------- |
| Install operating system updates?        | Yes                    | Yes      |
| Deploy Guacamole for easy remote access? | Yes                    | Yes      |
| Network                                  | auto_allocated_network | Yes      |
| Public IP Address                        | Automatic              | Yes      |
| Boot Script                              | see below              | No       |

Be sure to change `<not shown>` to a real password in the boot script before pressing the Create button to create the instances. The Exosphere GUI will say "Building" in orange, then "running Setup", then "Ready" in green. Clicking on "Instances" will take you to a screen that shows each instance created and its IP address.

You (or a student) can now log into an instance as **moleuser** with a command like this:

    ssh moleuser@149.165.159.178
    
### NFS

You will need to mount the shared /var/pyenv directory on each instance. This involves:
* adding a line to `/etc/exports` on MOLE-2023-base for each VM instance (allowing that VM instance to access the share);
* restart the server on MOLE-2023-base (`sudo systemctl restart nfs-kernel-server`)
* you will probably want to add each VM to the known_hosts file on your local laptop to avoid getting asked it is OK to connect for each:

    ssh-keyscan 149.165.172.121 >> ~/.ssh/known_hosts
    
* mount the folder `/var/pyenv` on each VM instance

You can use a script such as the following to mount the folder on all VMs at once (assuming MOLE-2023-base is exporting to all of them):

~~~~~~
#!/bin/bash

IPADDRESSES=(149.165.172.121)

for ip in ${IPADDRESSES[@]}
do
    ssh -t moleuser@$ip "bash -c 'sudo mount -t nfs 149.165.173.177:/media/volume/sdb/pyenv /var/pyenv'"
done
~~~~~~

For this to work, you will need to:
* set up the array IPADDRESSES in this script to contain all the IP addresses beforehand;
* change 149.165.173.177 to the IP address of the MOLE-2023-base machine
* be set up for using openstack (see section entitled "Command line client" below).

### Boot script used

This is the default cloud-config boot script with some modifications for MOLE. 

* One modification is the addition of the moleuser. Note that SSH public keys for the co-directors as well as the TAs are automatically saved to the _~moleuser/.ssh/authorized_keys_ directory on each instance, making it easy for the TAs to log in to any instance, even if the student has changed the moleuser password (will be communicated to students in the first (intro) computer lab).

* Another modification is the addition of 14 lines to the runcmd section. These lines do the following:

 1. makes moleuser the owner of everything inside _/usr/local/share/examples/mole_ 
 2. makes moleuser the owner of everything inside _/opt/astral_ (needed for ASTRAL to be started without using sudo) 
 3. makes moleuser the owner of everything inside _/opt/jmodeltest-2.1.10_ (needed for jModelTest to be started without using sudo) 
 4. makes moleuser the owner of everything inside _/opt/julia-1.8.5_  
 5. creates an alias named _astral_ (makes it easier to start ASTRAL)
 6. creates an alias named _jmodeltest_ (makes it easier to start jModelTest)
 7. creates an alias named _phyml_ (which points to the phyml executable inside jModelTest)
 8. adds a line exporting the environmental variable JULIA_DEPOT_PATH to moleuser's .bash_profile (this allows Julia to find the packages needed for the PhyloNetworks tutorial)
 9. creates a symlink named _iqtree-beta_ in /usr/local/bin that points to /usr/local/bin/iqtree2 (the IQTREE tutorial uses iqtree-beta rather than iqtree2)
10. creates a symlink named _raxml_ in /usr/local/bin that points to /usr/local/bin/raxmlHPC (the PAUP* tutorial specifies raxml rather than raxmlHPC)
11. makes moleuser the owner of its own .bash_profile (created as a result of the alias definitions above)
12. creates a symbolic link named _moledata_ (makes it easier to find example datasets)
13. creates a directory /var/pyenv to use as a mount point for nfs
14. makes moleuser the owner of /var/pyenv

~~~~~~
#cloud-config
users:
  - default                 # preserve the standard default user
  - name: moleuser          # MOLE-specific: adds a user moleuser common to all
    shell: /bin/bash        #   VMs in addition to the exouser added by default
    groups: sudo, admin    
    sudo: ['ALL=(ALL) NOPASSWD:ALL']{ssh-authorized-keys}
    ssh_authorized_keys:    # moleuser has public keys for directors and TAs allowing easy login
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpAtnEa/ULxAsa7HWP9puJfq8iTaMmkMxqEsu7f+psbmYTSmxH3QmAgWmPraNR0GQ+TG0uZUw9dR30jGn4e4+J6NCQ0H/qvoB3KIyIaFJzeg48skz0paGX+SfrdM2IEGd3ciIoKPnvx0xUZQot0DZfT6KTRm341G/u9tXzmMz/KIRmOokFmfNh4Bwt+qna5YLLBQs8GDyaLP6Sz/uabDi+k8S2BpVTV8OIGT0pFDkZ1Og8S5eJ0Rc7QHsrLfBijmB/XRtXmfMEuT7xNcvtKtQm7T/pGSy8eNhogJZX72GFCLAv/mHInBKk6qtU4wuHxan8yE2zGNhno7T8N87D0l4pxvev+kMfeUK7QvUKvxJuzGBY7SyiLlrPC3sfFTqLriOZvQg7d/o3BFyWFDFvfH3jTXe1rRdK9iHNwt9Qd7ARtKyVSKD3ZeQ3x33x9RPtDppOSEVY4oGAQ0YKVat1GmVVhiklDBoQYs13arIwHlEWoPr7xXqUlW8kQeRTn2epLAk= adetunjiadesina@BIOF-SAWYER-AA.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMpNe5iim6O1x93lNkJw5ZLF6f5Kd9KIMaNuifz3MY1K4+NIFQHgrbENAaimuvwNCQDCUDgOY2u4v92O2PQLmPjO5NR9Yl1vOhpzb3EFe1EM7lwFSIKNl6S2jNd4mghUXImaXT6vtS/V6X9HwB6/qhFwHrb3ic+7RPxUplMRhnflatIGWk7V+OaSBvC1AuswXqGAeBeOItJJKeGqerWDq8ytbeUbp3qFtzyHT+z08m0UnSYIIyPfV5lxztCpw22xmkReQ2pc1FtwJKmxCa3QxegsQ30X/r9fjiVS7K2CPJSTwqWbs33GfSnYgYyynjch0pQt0ByOPB1ncpfbLZWbw3 plewis@cormoran.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC6StAassFQ415BcyUxfTMG5cbziIxVn/E+KCbhx4/Csm1GjJmpCwSgxDqp2gXjQLprElASMIygnQMdZ1m6U8/CcbEPzviZdWeM+NHn/ELCa4OxL0MTPDLpnHC2Dyvi6RnM9UJYwnCIT1/U/R7ZVMXRtPU5xBhf+087HTLdMZ4gXx6yWWCynmrXpwbwJULhodDxkY9kouLudLHSNDjEfbI7PErvFLslOvCPnivgeEueJoJwpIvatpWFykohOn5UwXzZNmI9GWCQ1wtliZzhROKre1AnVfmHW8oO7QVQOGNxPfqSV6zKLnTpBfWsykqOYEVqR6M1kV+QjQHThxLCvLzrKoyLayuE0xdY8lbMzuw2LbWmsDv2rLKWiorH3rZRRH2NWi5EZEuNrQqPUug/kxCjAY5/jPHeavX6PdnyS2PwW4N7et1gRPcI64RwaQNofPUqbPrEFP+PYxEjJQw4B36tFRXvV+qs95TiMZ4Zuy7IUI/12phZqz5tvClI8i3O6sE= analisamilkey@MacBook-Air.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDIulLE6a+QGh/JE9mjGmTwRWtmcK29mbB1MJEN728+gLRnHV8oRfE5ahZVp4k0+h0onBn3Br8hVTkqQqC3GJmRe2PMlocqIJULe3hFvtXZqGh+w8QUj//+C3kTg6Lptc2m4f9JimjUjFNPnfX5sioJp2mHOjNbYXYbXb0zx1Y5jKVmi6r0NifcuZ+ObfIFG5+o1kytAq/J+8f6evBUKlTR8Gsk7V9zuZmGcffGZe5HA+3ilkUGd2Uyx18nbgE4VZTXC9K7RA7AFPtkLRH/ivaMGESUteH5Wqe1Bj46ORjapRV+hmU1t/VeOmHVWknkaTM3/yZpMKAiFYxWADDXsSNSNck38zMmDmWxzW+wcrNcCysKUZU60DxD4Czvk4VEUgFSVg/YmN1tJDqVse7GfcvYxzgC9R5qDItXPY3YBjq9ykOIGmn9C30lVqh4nELu3LujrmHmf0VTDtexc/4T+YPJlmVxr64UP4YTInLw5wBgQ89Thj6ahx+QnfC6m5Uv+ws= blakefauskee@Blakes-MacBook-Pro-3.local               
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0lGJQrxeZ8wjpxwFvgAW+1gnHzB7cre8ejkAdBHR8rQjz+htA9U+nsgNvaSHoD4q0TzObhobdwOlkCVstJNYz1KKDH61Rbn61MToO5h1n4Ow1slHNl/Cy0NKwEg+YnyPULrMb1z5h+yzUUFgMpwzzQsutrcN9Im3HuAnRGD3giJFHKYhhEMl92EPgEf9/xs3b/0B1FdXIotFiuGkk3FkhZIA+1Ga+nNE6CEhjEHY2YQd3PsFRZWqo/FxujUQTS5hvy/5BOGpGo3LyRFiHiNWXcHXVLak+0SJzrDEcpoX1A1ezzJIvQbdGV3KNxxFPsX9T48oi5r50WRRiG3tmjUQjRm+tx41yUl/ZmZEISv8CQtn2p4h02sTLLOntIP3GBjiIok/zgTH2OHihMlqoahKbfoadWZLhkG05pnZ71YA0hFs8QQxPXNycf8zHxp8PmMAzKL9M4jtH+KRH+XVj9zoq9D0uU7WA5kyUVOjHYRMy8yvGBtFHbW3TH7BgMP7aYcM= khaosan@Sungsiks-MacBook-Pro.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkpuLKyLQpqg8TF0iCRQXJg2z+/F/YBYnd4BVlupJhpZpbViLWulByYLMetC/7UT57CjX8i518CfpwbCP4dMEiQR+93AxZhBvKZM4Mtz0Me6SWmSnFV8cVF5c23UZoqOeVInABe14hLEZBdbyWck5QTy0k/CQrYSIToYqdZA6G/G8PKAk6db2rQuiwHi0Q5qE7RQ7S2qRgq4n9G0zPDelV8myyzduo7bOY3BaNMKwj5Yi/soMUBvOX7Do9R5+5XjpOuqnPbPX2NeMvIZJZ/ZwvBmbjQievhaX7COISWw77wUboaqpn2aEnewEc9Kt4gfx0gzDvznsCZRe+XCV1Q2xv3zVRut4FZfv0DhDEfL42vFEhahF728npFjyIo5cidMTBek9oCuqg58B3Umr/bFJEhjCaGhBJVqeDRERha8fbO7c8aAW3WdoTqaJJAIshztWhLotJaM77nt35dMrmOlOwRs3rHi4fxk5r+6tLxardNGKOBWHyQ4CneYPUkxWKcN0= kubatko.2@STAT-NC247353
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqJeFU3sEcA72fyYD2LCzDsfHqPmZonnATiXDKYeutIzQ+iVREIG3EMUNjeps8JS9oWw11ojXLFDZCHdg/z87qBZn7ilGgXZ6/PRhGaDx3kjPr5Mek10bV3BwB0O9Gws9rmepD/akuXY7wTS5M++YqCkwU1Ia9oAEW4QWDuc1Bdj3L1DqSYbI+xg38EA5TpRL2N968OPuu1xhGT9cPkRgOQAcTbFyknoeEXKwSUKamii8q8Lv+Zi9nA1nRYa0xZdJSGZNxso41FJkEmNfF6o/IKMtAJ0DHcg1B3aJpS8o2+cgyR+L0NqVHrJeBIagm4n3H8xP40pUCj5PyphdZam5L jpbielawski@Josephs-MacBook-Air.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA1D6eflrh3q3daop2orqL0pXrAqOUt8AaYWaC/d+iZQutHiroByNjpSETkmEd1yw8NpF6gVkh8oNqvTH1ERlJtX1BETipUvJAlvV67ZwWDSoYVqM+RwFiUT4cIC2No0V3ETI9pd4D0Dnq/9l4V9pYaunnbvIaAUsQiDRPMcRq+aOZRB/fH9nTQ5jfWKWEAu2m77T6esXe0bFX6cMhoZdk4HQSc+Wdsfn5TZEoi7+0YVK7973ZmIHYRRl9a/80NtIIHQVOOjPve3mUxv5/dlFBvPVLVHe91XqD4DnXnjXytBgNpqjPHNY28yy/UZ7Ba8XXIxGzWEDy3p1+dJzXni/hOQ== DavidSwofford
ssh_pwauth: true             # allow password authentication (for students)
chpasswd:
    expire: false            # do not force user to change passwd on first login
    users:
        - name: moleuser     # mkpasswd --method=SHA-512 --rounds=4096 <passwd> -s /gyk3ST/YBZpL/wh
          password: $6$rounds=4096$/gyk3ST/YBZpL/wh$GbjLz08E2xaEky9eSTH/uVmui2K2ZCBHWPPGBi7cVEgrvNKzUTEPqhdgXK74wqi8WWqtwKDi3nxgUWzw8bFbJ/
package_update: true
package_upgrade: {install-os-updates}
packages:
  - python3-virtualenv
  - git{write-files}
runcmd:
  - chown -R moleuser.moleuser /usr/local/share/examples/mole                                                 # MOLE
  - chown -R moleuser.moleuser /opt/astral                                                                    # MOLE
  - chown -R moleuser.moleuser /opt/jmodeltest-2.1.10                                                         # MOLE
  - chown -R moleuser.moleuser /opt/julia-1.8.5                                                               # MOLE
  - echo 'alias astral="java -jar /opt/astral/astral.5.7.1.jar"' >> /home/moleuser/.bash_profile              # MOLE
  - echo 'alias jmodeltest="java -jar /opt/jmodeltest-2.1.10/jModelTest.jar"' >> /home/moleuser/.bash_profile # MOLE
  - echo 'alias phyml="/opt/jmodeltest-2.1.10/exe/phyml/PhyML_3.0_linux64"' >> /home/moleuser/.bash_profile   # MOLE
  - echo 'export JULIA_DEPOT_PATH=/opt/julia-1.8.5/usr/share/julia/site' >> /home/moleuser/.bash_profile      # MOLE
  - sudo ln -s /usr/local/bin/iqtree2 /usr/local/bin/iqtree-beta                                              # MOLE
  - sudo ln -s /usr/local/bin/raxmlHPC /usr/local/bin/raxml                                                   # MOLE
  - sudo chown -R moleuser.moleuser /home/moleuser/.bash_profile                                              # MOLE
  - ln -s /usr/local/share/examples/mole /home/moleuser/moledata                                              # MOLE
  - mkdir /var/pyenv                                                                                          # MOLE
  - chown -R moleuser.moleuser /var/pyenv                                                                     # MOLE
  - echo on > /proc/sys/kernel/printk_devkmsg || true  # Disable console rate limiting for distros that use kmsg
  - sleep 1  # Ensures that console log output from any previous command completes before the following command begins
  - >-
    echo '{"status":"running", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
  - chmod 640 /var/log/cloud-init-output.log
  - {create-cluster-command}
  - (which apt-get && apt-get install -y python3-venv) # Install python3-venv on Debian-based platforms
  - (which yum     && yum     install -y python3)      # Install python3 on RHEL-based platforms
  - |-
    python3 -m venv /opt/ansible-venv
    . /opt/ansible-venv/bin/activate
    pip install --upgrade pip
    pip install ansible-core
    ansible-pull \
      --url "{instance-config-mgt-repo-url}" \
      --checkout "{instance-config-mgt-repo-checkout}" \
      --directory /opt/instance-config-mgt \
      -i /opt/instance-config-mgt/ansible/hosts \
      -e "{ansible-extra-vars}" \
      /opt/instance-config-mgt/ansible/playbook.yml
  - ANSIBLE_RETURN_CODE=$?
  - if [ $ANSIBLE_RETURN_CODE -eq 0 ]; then STATUS="complete"; else STATUS="error"; fi
  - sleep 1  # Ensures that console log output from any previous commands complete before the following command begins
  - >-
    echo '{"status":"'$STATUS'", "epoch": '$(date '+%s')'000}' | tee --append /dev/console > /dev/kmsg || true
~~~~~~

{% comment %}
## Things to do differently in 2023 Workshop

* (done in 2023) By default, Julia packages are installed in the _~/.julia_ directory of a particular user, not globally. Find out how to install PhyloNetworks, PhyloPlots, and the other packages needed for the PhyloNetworks tutorial globally, or add the necessary setup to the cloud-init script. In 2022, I had to ssh into each VM separately and add Julia packages under the user moleuser. They were present in /home/exouser/.julia, but simply copying that directory to /home/moleuser and chown moleuser.moleuser did not do the trick.
{% endcomment %}

## Command line client

### Obtaining CLI credentials

Beware: these instructions have not been tested in 2023.

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

    openstack image show MOLE-2023-snapshot --fit-width

To show a list of instances:

    openstack server list
    
To show details for one particular instance, provide the ID:

    openstack server show 9a3b295c-eede-4930-8661-3003eb264ed9 --fit-width

To create an launch an instance (see [Launch and Access Your Instance](https://docs.jetstream-cloud.org/ui/cli/launch/)):

    (normally done using exosphere interface)

{% comment %}    
openstack server create <my-server-name> \
--flavor FLAVOR \
--image IMAGE-NAME \
--key-name <my-keypair-name> \
--security-group <my-security-group-name> \
--wait
{% endcomment %}    
        
To shelve or unshelve an instance (see [Instance Management Actions in the CLI](https://docs.jetstream-cloud.org/ui/cli/manage/)), get ID using `openstack server list` and then issue a command like this:

    openstack server unshelve ea2f87ea-3cce-4987-a489-e0b9850f743c
      
To delete an instance (see [Deleting items in the CLI](https://docs.jetstream-cloud.org/ui/cli/deleting/)):

    openstack server delete ea2f87ea-3cce-4987-a489-e0b9850f743c
    
{% comment %}
    1  cd .ssh
    2  ls
    3  cat - >> authorized_keys
    4  ls -la
    5  cd .ssh
    6  ls
    7  cat - > authorized_keys
    8  vi authorized_keys
    9  cat - > authorized_keys
   10  ls
   11  cat authorized_keys
   12  vi authorized_keys
   13  cd
   14  mkdir TARs
   15  mkdir clones
   16  ls
   17  TZ="EST5EDT" date
   18  more /proc/cpuinfo
   19  uname -m x86_64
   20  sudo dpkg -l
   21  !
   22  sudo apt-add-repository universe
   23  sudo apt update
   24  sudo apt upgrade -y
   25  sudo apt install -y apt-file
   26  sudo apt install -y python2
   27  ls
   28  uname -m x86_64
   29  uname --help
   30  sudo apt install -y apt-file
   31  sudo apt install -y python2
   32  sudo apt install -y python-is-python3
   33  sudo apt install -y whois
   34  whois
   35  whoami
   36  sudo apt install -y mlocate
   37  sudo apt install -y unzip
   38  sudo apt-get install -y r-base
   39  sudo apt install -y zlib1g-dev
   40  sudo apt-get install -y openmpi-bin
   41  sudo apt-get install -y libopenmpi-dev
   42  sudo apt-get install -y openmpi-common
   43  curl -LO https://peterbeerli.com/migrate-html5/download_version4/migrate-newest.src.tar.gz
   44  ls
   45  tar zxvf migrate-newest.src.tar.gz
   46  ls
   47  curl -LO https://peterbeerli.com/migrate/download_version4/migrate-5.0.6.src.tar.gz
   48  ls
   49  tar zxvf migrate-5.0.6.src.tar.gz
   50  ls
   51  rm migrate-newest.src.tar.gz
   52  tar zxvf migrate-5.0.6.src.tar.gz
   53  file migrate-5.0.6.src.tar.gz
   54  tar xvf migrate-5.0.6.src.tar.gz
   55  ls
   56  mv migrate-5.0.6.src.tar.gz TARs/
   57  ls
   58  cd migrate-5.0.6/
   59  ls
   60  cd src
   61  ./configure
   62  make
   63  sudo make install
   64  make clean
   65  make mpis
   66  sudo make installmpi
   67  ls -la /usr/local/bin/
   68  cd
   69  curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.5-linux-x86_64.tar.gz
   70  tar zxvf julia-1.8.5-linux-x86_64.tar.gz
   71  mv julia-1.8.5-linux-x86_64.tar.gz TARs
   72  sudo mv julia-1.8.5 /opt/
   73  cd /usr/local/bin
   74  sudo ln -s /opt/julia-1.8.5/bin/julia julia
   75  cd
   76  ls
   77  cd ~/usr/local/bin
   78  cd /usr/local/bin/
   79  ls
   80  rm julia
   81  sudo rm julia
   82  cd /opt
   83  ls
   84  sudo rm -rf julia-1.8.5/
   85  cd
   86  curl -fsSL https://install.julialang.org | sh
   87  vi .bashrc
   88  vi .profile
   89  curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-x86_64.tar.gz
   90  ls
   91  tar zxvf julia-1.10.2-linux-x86_64.tar.gz
   92  mv julia-1.10.2-linux-x86_64.tar.gz TARs/
   93  sudo mv julia-1.10.2 /opt/
   94  cd /usr/local/bin
   95  sudo ln -s /opt/julia-1.10.2/bin/julia julia
   96  julia
   97  cd
   98  export JULIA_DEPOT_PATH=/opt/julia-1.10.2/usr/share/julia/site
   99  julia
  100  cd ~/clones/
  101  git clone https://github.com/revbayes/revbayes.git
  102  cd revbayes/projects/cmake/
  103  ./build.sh
  104  cd
  105  sudo apt install -y libboost-all-dev
  106  cd clones/
  107  cd revbayes/projects/cmake/
  108  ./build.sh
  109  sudo mv rb /usr/local/bin
  110  curl -LO https://github.com/NBISweden/MrBayes/archive/v3.2.7a.tar.gz
  111  tar zxvf v3.2.7a.tar.gz
  112  mv v3.2.7a.tar.gz TARs
  113  cd MrBayes-3.2.7a/
  114  ./configure
  115  make
  116  sudo make install
  117  cd
  118  curl -LO http://dstats.net/download/http://www.stat.wisc.edu/~ane/bucky/v1.4/bucky-1.4.4.tgz
  119  tar zxvf bucky-1.4.4.tgz
  120  mv bucky-1.4.4.tgz TARs/
  121  cd bucky-1.4.4/src/
  122  make
  123  ls
  124  make
  125  sudo mv bucky /usr/local/bin/
  126  sudo mv mbsum /usr/local/bin/
  127  cd
  128  cd clones/
  129  git clone https://github.com/stamatak/standard-RAxML.git
  130  cd standard-RAxML/
  131  make -f Makefile.AVX.PTHREADS.gcc
  132  sudo mv raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC
  133  rm *.o
  134  cd
  135  sudo apt install default-jre
  136  curl -LO https://github.com/smirarab/ASTRAL/archive/refs/tags/v5.7.1.tar.gz
  137  tar zxvf v5.7.1.tar.gz
  138  mv v5.7.1.tar.gz TARs
  139  sudo mkdir /opt/astral
  140  cd ASTRAL-5.7.1
  141  unzip Astral.5.7.1.zip
  142  cd Astral/
  143  sudo cp astral.5.7.1.jar /opt/astral
  144  sudo cp -r lib /opt/astral
  145  sudo java -jar /opt/astral/astral.5.7.1.jar
  146  cd
  147  sudo mkdir /usr/local/share/mole
  148  cd clones/
  149  git clone https://github.com/crsl4/PhyloNetworks.jl.wiki.git
  150  cd PhyloNetworks.jl.wiki/
  151  sudo mkdir /usr/local/share/mole/phylo-networks
  152  sudo cp -R data_results /usr/local/share/mole/phylo-networks
  153  cd /usr/local/share/mole/phylo-networks/data_results/scripts/
  154  ls
  155  nano raxml.pl
  156  sudo nano raxml.pl
  157  nano raxml.pl
  158  cd ~/clones/
  159  git clone https://github.com/molevolworkshop/moledata.git
  160  cd moledata/
  161  sudo unzip MSAlab.zip -d /usr/local/share/mole
  162  sudo unzip migrate_tutorial.zip -d /usr/local/share/mole
  163  sudo unzip modsel_sim_tutorial.zip -d /usr/local/share/mole
  164  sudo unzip svdquartets_tutorial.zip -d /usr/local/share/mole
  165  sudo unzip PamlLab.zip -d /usr/local/share/mole
  166  sudo unzip iqtreelab.zip -d /usr/local/share/mole
  167  sudo unzip revbayes.zip -d /usr/local/share/mole
  168  cd ..
  169  git clone  https://github.com/snacktavish/Mole2023.git
  170  sudo cp -R Mole2023 /usr/local/share/mole/
  171  cd /usr/local/share/mole
  172  sudo rm -rf __MACOSX
  173  sudo chmod 755 modsel_sim_tutorial
  174  cd
  175  curl -LO https://mafft.cbrc.jp/alignment/software/mafft-7.505-with-extensions-src.tgz
  176  tar zxvf mafft-7.505-with-extensions-src.tgz
  177  mv mafft-7.505-with-extensions-src.tgz TARs
  178  cd mafft-7.505-with-extensions/core
  179  make
  180  sudo make install
  181  sudo apt install -y muscle
  182  sudo apt install -y seqtk
  183  sudo apt install -y samtools
  184  sudo apt install -y bcftools
  185  cd
  186  curl -LO http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
  187  tar -xjf fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
  188  mv fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2 TARs
  189  sudo mv bin/* /usr/local/bin/
  190  pwd
  191  ls
  192  cd bin/
  193  ls
  194  cd ..
  195  rm -rf bin
  196  ls /usr/local/bin
  197  cd clones/
  198  git clone --recursive https://github.com/bwa-mem2/bwa-mem2
  199  cd bwa-mem2/
  200  make
  201  sudo mv ./bwa-mem2* /usr/local/bin/
  202  rm ./src/*.o
  203  ls /usr/local/bin/
  204  cd
  205  curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz
  206  tar zxvf iqtree-1.6.12-Linux.tar.gz
  207  mv iqtree-1.6.12-Linux.tar.gz TARs
  208  sudo mv iqtree-1.6.12-Linux/bin/iqtree /usr/local/bin
  209  curl -LO https://github.com/iqtree/iqtree2/releases/download/v2.2.0/iqtree-2.2.0-Linux.tar.gz
  210  tar zxvf iqtree-2.2.0-Linux.tar.gz
  211  mv iqtree-2.2.0-Linux.tar.gz TARs
  212  sudo mv iqtree-2.2.0-Linux/bin/iqtree2 /usr/local/bin
  213  ls /usr/local/bin
  214  sudo apt install -y libpython2.7
  215  cd
  216  curl -LO https://github.com/ddarriba/jmodeltest2/files/157117/jmodeltest-2.1.10.tar.gz
  217  tar zxvf jmodeltest-2.1.10.tar.gz
  218  mv jmodeltest-2.1.10.tar.gz TARs
  219  cp -r jmodeltest-2.1.10 /opt
  220  sudo cp-r jmodeltest-2.1.10 /opt
  221  sudo cp -r jmodeltest-2.1.10 /opt
  222  sudo java -jar /opt/jmodeltest-2.1.10/jModelTest.jar
  223  ls
  224  mkdir QMCN
  225  cp wQMC.tar.gz QMCN/
  226  cd QMCN/
  227  ls
  228  tar zxvf wQMC.tar.gz
  229  rm wQMC.tar.gz
  230  ls
  231  cd
  232  ls
  233  cp wQMC.tar.gz TARs/
  234  cd QMCN/
  235  sudo cp find-cut-Linux-64 /usr/local/bin
  236  ls
  237  sudo cp max-cut-tree /usr/local/bin/
  238  max-cut-tree
  239  sudo max-cut-tree
  240  ls /usr/local/bin/
  241  cd /usr/local/bin
  242  ls -la
  243  sudo chmod +x max-cut-tree
  244  max-cut-tree
  245  pwd
  246  ./max-cut-tree
  247  ls
  248  ./max-cut-tree
  249  cd
  250  curl -LO http://phylosolutions.com/paup-test/paup4a168_ubuntu64.gz
  251  cp paup4a168_ubuntu64.gz TARs
  252  gunzip paup4a168_ubuntu64.gz
  253  sudo mv paup4a168_ubuntu64 /usr/local/bin/paup
  254  sudo chmod +x /usr/local/bin/paup
  255  curl -LO https://github.com/abacus-gene/paml/releases/download/4.10.7/paml-4.10.7-linux-X86_64.tgz
  256  ls
  257  tar zxvf paml-4.10.7-linux-X86_64.tgz
  258  ls
  259  cd paml-4.10.7/
  260  ls
  261  cd src
  262  make -f Makefile
  263  ls
  264  nano Makefile
  265  make -f Makefile
  266  sudo mv baseml basemlg chi2 codeml evolver infinitesites mcmctree pamp yn00 /usr/local/bin
  267  cd
  268  ls
  269  mv paml-4.10.7-linux-X86_64.tgz TARs/
  270  ls
  271  mv wQMC.tar.gz TARs/
  272  ls
  273  cd /usr/local/share/mole/
  274  ls
  275  sudo mv Mole2023/ Mole2024
  276  ls
  277  sudo chown -R exouser.exouser /usr/local/share/mole/Mole2024
  278  cd Mole2024/
  279  python -m venv pyenv
  280  source /usr/local/share/mole/Mole2024/pyenv/bin/activate
  281  python -m pip install git+https://github.com/jeetsukumaran/DendroPy.git
  282  python -m pip list
  283  deactivate
  284  source /usr/local/share/mole/Mole2024/pyenv/bin/activate
  285  python -m pip install opentree
  286  python -m pip list
  287  deactivate
  288  cd
  289  curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Machine_Learning_for_Population_Genetics.ipynb
  290  curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Models-01.png
  291  sudo mkdir -p /usr/local/share/mole/machinelearning
  292  sudo mv Machine_Learning_for_Population_Genetics.ipynb /usr/local/share/mole/machinelearning
  293  sudo chown -R exouser.exouser /usr/local/share/examples/mole/machinelearning
  294  cd /usr/local/share/
  295  ls
  296  cd examples/
  297  ls
  298  cd ..
  299  cd mole/
  300  ls
  301  cd ..
  302  ls
  303  sudo mv mole/ examples/
  304  ls
  305  cd examples/
  306  ls
  307  ls -la
  308  cd mrbayes/
  309  ls
  310  vi .bashrc
  311  man history
  312  history
  313  ls
  314  cd /usr/local/share/examples/
  315  ls
  316  cd mole
  317  ls
  318  cd ..
  319  ls
  320  ls -la
  321  cd mrbayes/
  322  ls
  323  cd ..
  324  ls
  325  cd examples/
  326  ls
  327  cd mole
  328  ls
  329  cd phylo-networks/
  330  ls
  331  cd data_results/
  332  ls
  333  cd ..
  334  ls
  335  cd ..
  336  ls
  337  cd ..
  338  ls
  339  pwd
  340  sudo mv mrbayes mole
  341  cd mole
  342  ls
  343  ifconfig
  344  ls
  345  cd /usr/local/share/
  346  ls
  347  cd examples/
  348  ls
  349  cd mole/
  350  ls
  351  cd Mole2024/
  352  ls
  353  cd ..
  354  ls
  355  cd
  356  ls
  357  curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Machine_Learning_for_Population_Genetics.ipynb
  358  ls
  359  ls -la Models-01.png
  360  mkdir temp
  361  mv Models-01.png temp
  362  curl -LO https://molevolworkshop.github.io/faculty/smith/tutorial/Models-01.png
  363  ls
  364  diff Models-01.png temp/Models-01.png
  365  rm -rf temp
  366  ls
  367  sudo mkdir -p /usr/local/share/examples/mole/machinelearning
  368  sudo mv Machine_Learning_for_Population_Genetics.ipynb /usr/local/share/examples/mole/machinelearning/
  369  sudo chown -R exouser.exouser /usr/local/share/examples/mole/machinelearning
  370  module list
  371  cd /usr/local/share/examples/mole/machinelearning/
  372  python -m venv mlenv
  373  source ./mlenv/bin/activate
  374  python -m pip install msprime==1.2.0
  375  python -m pip install numpy==1.23.5
  376  python -m pip install scipy==1.9.3
  377  python -m pip install scikit-learn==1.2.0
  378  python -m pip install tensorflow==2.10.0
  379  python -m pip install keras==2.10.0
  380  python -m pip install ipykernel
  381  deactivate
  382  mkdir -p /usr/local/share/examples/mole/machinelearning/jupyter/molekernel
  383  cd /usr/local/share/examples/mole/machinelearning/jupyter/molekernel/
  384  module load anaconda
  385  jupyter kernelspec list
  386  cp -r /software/u22/anaconda/python3.9/share/jupyter/kernels/python3
  387  cp -r /software/u22/anaconda/python3.9/share/jupyter/kernels/python3/* .
  388  nano kernel.json
  389  cd /usr/local/share/examples/mole/machinelearning/
  390  cat - > doof.sh << EOF
  391  nano doof.sh
  392  sudo apt install -y nfs-kernel-server
  393  sudo vi /etc/exports
  394  sudo systemctl restart nfs-kernel-server
  395  cd /media/volume
  396  cd /media/volume/moledata
  397  ls
  398  sudo systemctl restart nfs-kernel-server
  399  cat /etc/exports
  400  ls -la /media/volume/sdb/mole
  401  cd /media/volume/
  402  ls
  403  cd moledata/
  404  ls
  405  sudo nano /etc/exports
  406  sudo systemctl restart nfs-kernel-server
  407  history
{% endcomment %}
