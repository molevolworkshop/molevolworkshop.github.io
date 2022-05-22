---
layout: page
title: Jetstream2 Setup Notes
permalink: /jetstream2/
---
{% comment %}
https://www.webfx.com/tools/emoji-cheat-sheet/
{% endcomment %}

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

* [Jetstream2 status](https://jetstream.status.io/)
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

## Creating the instance to be used as the master image

To create a new instance, click the red Create button in the upper right corner of Exosphere. 

I used the **Ubuntu 20_04 (latest)** image source and specified **MOLE_2022_image_basis** as the name. I chose **m3.small** as the flavor, **20 GB** root disk size (default for selected flavor), **1** for number of instances, **no** for enable web desktop, and **Show** for Advanced Options.

Advanced Options:

| Name                                     | Value                  | Default? |
| ---------------------------------------- | ---------------------- | -------- |
| Install operating system updates?        | Yes                    | Yes      |
| Deploy Guacamole for easy remote access? | Yes                    | Yes      |
| Network                                  | auto_allocated_network | Yes      |
| Public IP Address                        | Automatic              | Yes      |
| SSH Public Key                           | none specified         | Yes      |
| Boot Script                              | used default           | Yes      |

Press the Create button to create the instance. The Exosphere GUI will say "Building" in orange for about 5 minutes, then "running Setup" for another minute, then "Ready" in green. Clicking on "Instances" will take you to a screen that shows the MOLE_2022_image_basis instance and its IP address.

You can now log into the instance as **exouser**.

    ssh exouser@149.165.159.178
    
### Setting up the new instance

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
sudo apt-add-repository universe
sudo apt update
sudo apt upgrade -y
~~~~~~

### Install apt-file
This allows us to find out what files are installed by a package using "apt-file list packagename"
~~~~~~
sudo apt install -y apt-file
~~~~~~
Last updated 2022-05-22.

### Install python-is-python3
This ensures that whenever someone types python they are using python3
~~~~~~
sudo apt install python-is-python3
~~~~~~
Last updated 2022-05-22.

### Install mlocate
This provides the locate command, useful for finding where libraries and other system files are installed.
~~~~~~
sudo apt install -y mlocate
~~~~~~
Last updated 2022-04-19.

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
sudo apt-get install -y openmpi-common
~~~~~~

Above didn't work, led to link errors in migrate-mpi-n. Trying to build from scratch...
~~~~~~
sudo apt-get --purge remove openmpi-bin
sudo apt-get --purge remove libopenmpi-dev
sudo apt-get --purge remove openmpi-common

curl -LO https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.2.tar.gz
tar zxvf openmpi-4.1.2.tar.gz
mv openmpi-4.1.2.tar.gz TARs
./configure --prefix=/usr/local
make all install
~~~~~~
Last updated 2022-03-22.

### Install [migrate-n](https://peterbeerli.com/migrate-html5/index.html)
Migrate has its own lab in the workshop.
~~~~~~
cd
curl -LO http://peterbeerli.com/migrate-html5/download_version4/migrate-newest-src.tar.gz
tar zxvf migrate-newest-src.tar.gz
rm migrate-newest-src.tar.gz
cd migrate-5.0.3/src
./configure
make
sudo make install
make clean
make mpis
sudo make installmpi
~~~~~~
Installed as _/usr/local/bin/migrate-n_. 
Last updated 2022-04-03.

make produces the following output:

    Create the PDF library (libharu 1.x): [linker warnings are OK]
    Using system zlib architecture
    Compile the main source files and create the executable
Produces many warnings but will compile
sudo make install proceeds fine

make clean; make mpis
generates lots of warnings but will compile; if there are errors, for example 'undefined reference to 'MPI_Init' openmpi may be misconfigured.
sudo make installmpi works fine 

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
RAxML is used in the Solis-Lemus SNaQ and McTavish gene tree updating tutorial. These instructions install the binary in _/usr/local/bin_. Note: it is easier to just use "sudo apt-get install raxml" to do this install, but I didn't realize this at the time.
~~~~~~
cd 
git clone https://github.com/stamatak/standard-RAxML.git
cd standard-RAxML
make -f Makefile.AVX.PTHREADS.gcc
sudo mv raxmlHPC-PTHREADS-AVX /usr/local/bin/raxml
~~~~~~
Installed as _/usr/local/bin/raxml_. 
Last updated 2022-05-22.

### Install [Java](https://www.java.com/en/)
The Java Runtime Environment is needed for ASTRAL and jModelTest.
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

Change ownership (note: this is now handled by the [cloud init script](#boot-script-used))
~~~~~~
sudo chown moleuser.moleuser /opt/astral/astral.5.7.1.jar
sudo chown moleuser.moleuser /opt/astral/lib -R
~~~~~~
You should now be able to start ASTRAL as follows:
    java -jar /opt/astral/astral.5.7.1.jar
An alias will be created by the [cloud init script](#boot-script-used) to make this easier.
    alias astral="java -jar /opt/astral/astral.5.7.1.jar"
Last updated 2022-05-05.

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
MUSCLE is used in the alignment lab as well as the McTavish gene tree updating lab. Note: easier to just use "sudo apt-get install muscle" but didn't realize this at the time.
~~~~~~
cd
curl -LO https://github.com/rcedgar/muscle/releases/download/v5.1/muscle5.1.linux_intel64
sudo mv muscle5.1.linux_intel64 /usr/local/bin/muscle
sudo chmod +x /usr/local/bin/muscle
~~~~~~
Installed as _/usr/local/bin/muscle_. 
Last updated 2022-05-22.

### Install seqtk

seqtk is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt-get install seqtk 
~~~~~~
Last updated 2022-05-22.

### Install samtools

samtools is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt-get install -y samtools 
~~~~~~
Last updated 2022-05-22.

### Install bcftools

bcftools is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt-get install bcftools
~~~~~~
Last updated 2022-05-22.

### Install dendropy

dendropy is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt-get install dendropy 
~~~~~~
Last updated 2022-05-22.

### Install opentree

opentree is used in the McTavish gene tree updating lab.
~~~~~~
sudo apt-get install opentree 
~~~~~~
Last updated 2022-05-22.

### Install fastx

The fastx toolkit is used in McTavish gene tree updating lab. fastx toolkit and bwa-mem are not available through apt-get.
~~~~~~
wget http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
tar -xjf fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
sudo cp bin/* /usr/local/bin/
rm -rf bin
mv fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2 TARs
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
Last updated 2022-05-22.

### Install bwa-mem2

bwa-mem2 is used in McTavish gene tree updating lab.
~~~~~~
git clone --recursive https://github.com/bwa-mem2/bwa-mem2
cd bwa-mem2
make
sudo cp ./bwa-mem2* /usr/local/bin/
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
Last updated 2022-05-22.

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

### Install [libpython2.7.so.1.0 shared library](https://askubuntu.com/questions/1213461/cant-locate-libpython2-7-so-1-0)

The file _libpython2.7.so.1.0_ is required for PAUP*. 

    sudo apt install -y libpython2.7

Installed as _/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0_. 
Last updated 2022-04-19.

{% comment %}
This section commented out because it turns out Apache ant is not needed after all. jModelTest.jar can be downloaded and does not need to be compiled.
### Install [Apache ant](https://ant.apache.org)

Apache ant is needed to compile jModelTest, which is, in turn, needed for the PAUP* tutorial. Note that there appear to be no instructions on the Ant web site about installing using apt on Ubuntu, which is how I installed it.

    sudo apt install -y ant

Version 1.10.7 installed as _/usr/bin/ant_.
Last updated 2022-05-05.
{% endcomment %}

### Install [jModelTest](https://github.com/ddarriba/jmodeltest2/)

    curl -LO https://github.com/ddarriba/jmodeltest2/files/157117/jmodeltest-2.1.10.tar.gz
    tar zxvf jmodeltest-2.1.10.tar.gz
    cd jmodeltest-2.1.10
    sudo mkdir /opt/jModelTest
    sudo cp jModelTest.jar /opt/jModelTest
    sudo cp -r lib /opt/jModelTest

Change ownership (note: this is now handled by the [cloud init script](#boot-script-used))
~~~~~~
sudo chown moleuser.moleuser /opt/jModelTest/jModelTest.jar
sudo chown moleuser.moleuser /opt/jModelTest/lib -R
~~~~~~
You should now be able to start jModelTest as follows:
    java -jar /opt/jModelTest/jModelTest.jar
An alias will be created by the [cloud init script](#boot-script-used) to make this easier.
    alias jmodeltest="java -jar /opt/jModelTest/jModelTest.jar"
Last updated 2022-05-05.

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

## Create MOLE-2022-master snapshot

Once the **MOLE_2022_image_basis** VM is set up and running, you can create a **snapshot** image using the Actions menu. I named this snapshot image **MOLE-2022-master** and keep this image up-to-date (as changes are made to MOLE_2022_image_basis) by deleting the old snapshot and creating a new one.

## Creating instances based on MOLE-2022-master

To create new instances, click the red _Create_ button in the upper right corner of Exosphere, then choose _Instance_ and then, in the _Choose an Image Source_ section, click the _By Image_ tab and hit the _Create Instance_ button beside MOLE-2022-master.

Choose **m3.small** as the flavor, **20 GB** root disk size (default for selected flavor), **62** for number of instances, **no** for enable web desktop, and **Show** for Advanced Options.

Advanced Options:

| Name                                     | Value                  | Default? |
| ---------------------------------------- | ---------------------- | -------- |
| Install operating system updates?        | Yes                    | Yes      |
| Deploy Guacamole for easy remote access? | Yes                    | Yes      |
| Network                                  | auto_allocated_network | Yes      |
| Public IP Address                        | Automatic              | Yes      |
| SSH Public Key                           | none specified         | Yes      |
| Boot Script                              | see below              | No       |

Press the Create button to create the instances. The Exosphere GUI will say "Building" in orange, then "running Setup", then "Ready" in green. Clicking on "Instances" will take you to a screen that shows each instance created and its IP address.

You (or a student) can now log into an instance as **moleuser**.

    ssh moleuser@149.165.159.178

### Boot script used

This is the default cloud-config boot script with some modifications for MOLE: 

:small_blue_diamond: One modification is the addition of the moleuser. Note that SSH public keys for the co-directors as well as the TAs are automatically saved to the _~moleuser/.ssh/authorized_keys_ directory on each instance, making it easy for the TAs to log in to any instance, even if the student has changed the moleuser password, which is not shown in the cloud-config script below for security reasons (you should replace <tt><not shown></tt> with a meaningful password that will be communicated to students in the first (intro) computer lab.

:small_blue_diamond: Another modification is the addition of 8 lines to the runcmd section. These lines do the following:

1. makes moleuser the owner of _/opt/astral/astral.5.7.1.jar_ (needed for ASTRAL to be started without using sudo) 
2. makes moleuser the owner of _/opt/astral/lib_ (ditto)
3. makes moleuser the owner of _/opt/jModelTest/jModelTest.jar_ (needed for jModelTest to be started without using sudo) 
4. makes moleuser the owner of _/opt/jModelTest/lib_ (ditto)
5. creates an alias named _astral_ (makes it easier to start ASTRAL)
6. creates an alias named _jmodeltest_ (makes it easier to start jModelTest)
7. creates an alias named _raxmlHPC_ (some tutorials use raxmlHPC rather than raxml)
8. creates a symbolic link named _moledata_ (makes it easier to find example datasets)

~~~~~~
#cloud-config
users:
  - default                 # preserve the standard default user
  - name: moleuser          # MOLE-specific: adds a user moleuser common to all
    shell: /bin/bash        # VMs in addition to the exouser added by default
    groups: sudo, admin    
    sudo: ['ALL=(ALL) NOPASSWD:ALL']{ssh-authorized-keys}
    ssh_authorized_keys:    # moleuser has public keys for directors and TAs allowing easy login
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMpNe5iim6O1x93lNkJw5ZLF6f5Kd9KIMaNuifz3MY1K4+NIFQHgrbENAaimuvwNCQDCUDgOY2u4v92O2PQLmPjO5NR9Yl1vOhpzb3EFe1EM7lwFSIKNl6S2jNd4mghUXImaXT6vtS/V6X9HwB6/qhFwHrb3ic+7RPxUplMRhnflatIGWk7V+OaSBvC1AuswXqGAeBeOItJJKeGqerWDq8ytbeUbp3qFtzyHT+z08m0UnSYIIyPfV5lxztCpw22xmkReQ2pc1FtwJKmxCa3QxegsQ30X/r9fjiVS7K2CPJSTwqWbs33GfSnYgYyynjch0pQt0ByOPB1ncpfbLZWbw3 plewis@cormoran.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCouLhDpekh1GQMpx1oyMKhAzbl2bINJMaW6N0G6Kp1kYuaQddK3TGHNhQ/BcIHli7uVHlGD1Q5ABuJI+X66bh4k02/DDDhGqbtqw18IfufMRTsSyOvrvZ2QWMw9xHNg5J+2n+hfuuCyXZuay+DYyXShq4FvMqBfd2c0GeMWBNqpyH6QicsfMc/JyNFZdCdm0G86E61Y9QLM1cgGe8oUA3/85AaT0X/yCUdkbX6QZPZEfrBtMilXDV9oCGqrLUR/ZBp/EdEmxz0a39aU6xzZamPbRC1gYeVvzg2QfQeM1t2zYRIGc8ssJ39AbI6Kk1ZDrNqYFRQUk5ywqjixyqXpWbL akijarl@Akis-MacBook.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCwLwDmVCAamrG+cUzsv93qNO83TBymqimSCF+q9CD0zVXve6oYcKqKWt+nJqwYfeP1iLzi0NAEVcYpu9u34De9ortuWflMEZoh+1R32q0zqOkULMBCol4yXC7ou0+t23DFwkiavTn7ggQtmFKZ06/TGMSHdILaiFptpkKdadg7/qEKnuXXL3BZ7Jw9ZYrCr2oIEJ0expAEmf3xURFUwS23DcsJJTH2UJcipq7yucjjb+5YvAaMBc5NaT+q3j4otBjc9/mEiJUFgFwtu8KmZ5czUgnVMUi4dIkxxjVgtDnmChTA9P150yZ0YMXipyQPpKRbQ17ZCWTAvR5mWGqi2UGQA+etXxtopLdGref9OqNUA/6szVMZsFAYT2gUgLobkWtsX17WSjM+G3py4Kl5EBdbGChtqlbFth3X9J3/yzyt+Q3NKpsxeSE9b5FTCn5zD1Sqsx34tOByyeGDIAVbUXqhGvDJLTXLqqqkMmbabzHYNcXOwJVFxYFvbyfIe6d8Wuk= beerli@cornelius.local
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzNnLX1WagNRL8pZaaB5zMrrSBmondVSKfAtiNGd7z++WT/2UonvDzxOEpfo61dvPqY/NP+wNdRJ2+gDxUuUNQsFZEVZpFWt+rAjtVbfKF7V+qfB4crKDVsPV92FlbzyD2Z8azc3rrJMl4Oxl16/d8vpZMSeM8q35cpqif75+Yyc0pPB/kCiwRfzifgCLouK23tUwuCLRTY0nK3Mwd41Jbvt+xoFlRhBbw1iou2SR0yhl6C+DrLwgcaEp1I9oUX8EBWR7Hp/Pfw3qESk4sEIInX3aEZQq1WJRxnKJynyo9E2WlBuL4eotF1en/ppCRDYLQw6ySn/fRncCRr6X9CNijoog7HZdjMiBMk1EteJaso7fHqsALeTcLonR9WnGoirNfFQJr2g6LYdNjrhYA5pWzgEwPuZrNnYaHZj1JW2Bj9XRx/SKFlkKE4oooAgdopZLA6AngjMXqFJ5pXVsrxRnqV+vWSKE25pyRzGJ7heahtHfzaB6U+QMB+wCUxxmaAy0= kate@Kates-MacBook-Air
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDF5GNcJcMm42xJSCCkI0w8pDNgGSXWEtBCJAFMEvrNDYxYOAl8W8fZvAxT7/1B/ZBXt8ASiDTtMuZkWHv/wPkywKPDa1dVyQ6aBa5uU7h6K3FaP1OM+c9xqHMN0H/54mXRFxSESfVuRpvxwiw9oOKZ2xSphs8+e+8pv4GziPeOuxrheat9jcjfY6EIm6zwVvNEM4rgaW+jCK2xn89tbmKlrT+wh7PwD9bzSwIvAHCpf8EaiJrdueNBILGYewmGykffIVVeH8GKIxqfSTLIUiyFwYnwQydGkT/ceXuty9ML+QQIw81FbYhTf9+1GfZC85UyXkfI35HujJfSMUrvhxq7 Jordan@Jordans-MacBook-Pro-7.local 
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqJeFU3sEcA72fyYD2LCzDsfHqPmZonnATiXDKYeutIzQ+iVREIG3EMUNjeps8JS9oWw11ojXLFDZCHdg/z87qBZn7ilGgXZ6/PRhGaDx3kjPr5Mek10bV3BwB0O9Gws9rmepD/akuXY7wTS5M++YqCkwU1Ia9oAEW4QWDuc1Bdj3L1DqSYbI+xg38EA5TpRL2N968OPuu1xhGT9cPkRgOQAcTbFyknoeEXKwSUKamii8q8Lv+Zi9nA1nRYa0xZdJSGZNxso41FJkEmNfF6o/IKMtAJ0DHcg1B3aJpS8o2+cgyR+L0NqVHrJeBIagm4n3H8xP40pUCj5PyphdZam5L jpbielawski@Josephs-MacBook-Air.local               
        - ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOvS4hXxZfIIIxDiU0p5I7eazXO7MBeTJXI+wY2YPfnIwqSB7dr5pw98mocoqQAGiNdq7LD2lvtHOlAy3wlDhzs=
ssh_pwauth: true             # allow password authentication (for students)
chpasswd:
    expire: false            # do not force user to change passwd on first login
    list:
        - moleuser: <not shown>  # specify starting password for moleuser
package_update: true
package_upgrade: {install-os-updates}
packages:
  - python3-virtualenv
  - git{write-files}
runcmd:
  - chown moleuser.moleuser /opt/astral -R              # MOLE
  - chown moleuser.moleuser /opt/jModelTest -R          # MOLE
  - echo 'alias astral="java -jar /opt/astral/astral.5.7.1.jar"' >> /home/moleuser/.bash_profile       # MOLE
  - echo 'alias jmodeltest="java -jar /opt/jModelTest/jModelTest.jar"' >> /home/moleuser/.bash_profile # MOLE
  - echo 'alias phyml="/opt/jModelTest/exe/phyml/PhyML_3.0_linux64"' >> /home/moleuser/.bash_profile # MOLE
  - echo 'alias raxmlHPC="/usr/local/bin/raxml"' >> /home/moleuser/.bash_profile # MOLE
  - ln -s /usr/local/share/examples/mole /home/moleuser/moledata                 # MOLE
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
~~~~~~

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

To show a list of instances:

    openstack server list

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






