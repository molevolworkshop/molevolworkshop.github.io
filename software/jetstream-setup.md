---
layout: page
title: Jetstream Setup Notes
permalink: /jetstream-setup/
---
These are notes on setting up Jetstream virtual machines for the MOLE workshop. If you are a participant, these notes are not intended for you, but you are of course welcome to read them. They are intended for the current directors and head TA of the workshop, who must get the Jetstream virtual machines up and running before the workshop begins. 

[Paul Lewis](mailto:paul.lewis@uconn.edu) created the first version of this document 5-Feb-2020.

### Helful links

* [Virtual machine sizes](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/17465371/Virtual+Machine+Sizes+and+Configurations)
* [Online tutorial](https://cvw.cac.cornell.edu/jetstream/default)
* [Jetstream FAQ](https://wiki.jetstream-cloud.org/Troubleshooting+and+FAQ)
* [Getting Started with a new Instance](https://iujetstream.atlassian.net/wiki/spaces/JWT/overview)
* E-mail Support: [Atmosphere RT <help@jetstream-cloud.org>](mailto:help@jetstream-cloud.org)

### Most important!

Be sure to **shelve** instance if not planning to work with it for several hours. Shelving is the only option that does not burn SUs. **Suspending** burns SUs at 75% of the normal rate and **stopping** burns SUs at 50% the normal rate. See [Instance management actions](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/537460754/Instance+management+actions) for more info.

### Logging into Jetstream Atmosphere

Login to Jetstream at this address (click on "Login with XSEDE" button): [https://use.jetstream-cloud.org/](https://use.jetstream-cloud.org/). In order to do anything described below, you will need to have an [Xsede portal](portal.xsede.org) account and be added to the project.

### Starting an instance once in Jetstream Atmosphere  
  
* In the Dashboard, you should see the educational allocation for MOLE (TG-DEB190022)
* Go to Projects and click on plewis to see details (this may have your username instead of plewis)
* Click the check box beside a shelved instance and press unshelve button that appears

### Creating a new instance

To create a new instance, click the New button from the project. Note that there is no need to create a new instance if one have already been created and set up - just unshelve it. These notes are just a record of what has been done already.

I used the _Ubuntu 18_04 Devel and Docker_ image and specified an instance size of m1.quad (CPU: 4, Mem 10 GB, Disk: 20 GB) when setting up the virtual machine serving as the template for MOLE 2020. Press the Launch Instance button to create the instance.

### Unshelving an instance

While unshelving or before starting for the first time, see details by clicking on name of instance. The most important bit of information provided here is the IP address, which will change each time you shelve/unshelve. The instance is ready to use when status is Active N/A.

### SSH stuff

Create an entry in your _~/.ssh/config_ file to make it easy to login.
~~~~~~
Host jet
    HostName 149.165.156.59
    User plewis
    IdentityFile /Users/plewis/.ssh/id_rsa
    Cipher blowfish
~~~~~~    
See the [Adding SSH keys to the Jetstream Atmosphere environment](https://iujetstream.atlassian.net/wiki/spaces/JWT/pages/17465474/Adding+SSH+keys+to+the+Jetstream+Atmosphere+environment) for information about adding SSH keys. The short version is: Jetstream Dashboard > Settings > Show More > SSH Configuration.
        
Now ssh into the instance using the jet host set up in _.ssh/config_ file:
~~~~~~
ssh jet
~~~~~~

## Initial setup of Ubuntu 18.04 m1.quad instance used to create custom image

### Update operating system before doing any work
~~~~~~
sudo apt update
sudo apt upgrade
~~~~~~

### Grant sudo access
See [How to Add User to Sudoers in Ubuntu](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/) for good instructions. 

You can grant sudo access to user pbeerli (for example) by editing the _/etc/sudoers_ file as follows:
~~~~~~
sudo visudo
~~~~~~
Once in the editor, add lines like this:
~~~~~~
pbeerli ALL=(ALL) ALL
pbeerli ALL=(ALL) NOPASSWD:ALL
~~~~~~

### Install unzip
~~~~~~
sudo apt install unzip
~~~~~~

### Install [R](https://www.r-project.org)
R is needed in order to precompile PhyloPlots.
~~~~~~
sudo apt-get install r-base
~~~~~~

### Install [migrate-n](https://peterbeerli.com/migrate-html5/index.html)
Install _migrate-n_ to _/usr/local/bin_.
~~~~~~
cd
sudo apt install zlib1g-dev
curl -LO http://peterbeerli.com/migrate-html5/download_version4/migrate-newest-src.tar.gz
tar zxvf migrate-newest-src.tar.gz
rm migrate-newest-src.tar.gz
cd migrate-4.4.4/src
./configure
make
sudo make install
~~~~~~

### Install [Julia](https://julialang.org)
This places the julia directory in _/opt_ and creates a symbolic link to the executable in _/usr/local/bin_.
~~~~~~
cd
curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.3/julia-1.3.1-linux-x86_64.tar.gz
tar zxvf julia-1.3.1-linux-x86_64.tar.gz
rm julia-1.3.1-linux-x86_64.tar.gz
sudo mv julia-1.3.1 /opt/
cd /usr/local/bin
sudo ln -s /opt/julia-1.3.1/bin/julia julia
~~~~~~

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

### Install [RAxML](https://github.com/stamatak/standard-RAxML)
RAxML is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
cd 
git clone https://github.com/stamatak/standard-RAxML.git
cd standard-RAxML
make -f Makefile.AVX.PTHREADS.gcc
sudo mv raxmlHPC-PTHREADS-AVX /usr/local/bin
~~~~~~

### Install [ASTRAL](https://github.com/smirarab/ASTRAL)
ASTRAL is used in the SNaQ tutorial. These instructions install the binary in _/usr/local/bin_.
~~~~~~
curl -LO https://github.com/smirarab/ASTRAL/raw/master/Astral.5.7.3.zip
unzip Astral.5.7.3.zip
rm Astral.5.7.3.zip
sudo mkdir /opt/astral
sudo cp astral.5.7.3.jar /opt/astral
sudo cp lib /opt/astral
~~~~~~

### Create MOLE directory
This directory will be used to store example data needed by students for tutorials.
~~~~~~
sudo mkdir /usr/local/share/examples/mole
~~~~~~

### Install data for [PhyloNetworks](http://crsl4.github.io/PhyloNetworks.jl/latest/) tutorial
~~~~~~
cd 
git clone https://github.com/crsl4/PhyloNetworks.jl.wiki.git
sudo mv PhyloNetworks.jl.wiki /usr/local/share/examples/mole/
~~~~~~
Modify line 47 of /usr/local/share/examples/mole/PhyloNetworks.jl.wiki/data_results/scripts/raxml.pl to say:
~~~~~~
my $astral = '/opt/astral/astral.5.7.3.jar'; # adapt to your system
~~~~~~

### Download datasets for alignment tutorial
~~~~~~
cd 
curl -O http://molevol.mbl.edu/images/3/3c/MSAlab.zip 
# omitted the usual L switch in the curl command because of SSL certificate problems on the MBL server
unzip MSAlab.zip
# above command failed, so I resorted to unzipping the file on my mac and rsync'ing directory to instance
sudo mv MSAlab /usr/local/share/examples/mole/
~~~~~~

### Install [MAFFT](https://mafft.cbrc.jp/alignment/software/)
Instructions below work except the man page is not installed because (strangely) the makefile
tries to create the directory _/usr/local/share/man/man1_ will and issues and error when it
finds that that directory already exists!
~~~~~~
cd
curl -LO https://mafft.cbrc.jp/alignment/software/mafft-7.453-with-extensions-src.tgz    
tar zxvf mafft-7.453-with-extensions-src.tgz
rm mafft-7.453-with-extensions-src.tgz
cd mafft-7.453-with-extensions/core
make
sudo make install
~~~~~~

### Install [MUSCLE](https://www.drive5.com/muscle/)
~~~~~~
curl -LO https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
tar zxvf muscle3.8.31_i86linux64.tar.gz
rm muscle3.8.31_i86linux64.tar.gz
sudo mv muscle3.8.31_i86linux64 /usr/local/bin/muscle
~~~~~~

### Install [IQ-TREE](http://www.iqtree.org)
~~~~~~
curl -LO https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz
tar zxvf iqtree-1.6.12-Linux.tar.gz
rm iqtree-1.6.12-Linux.tar.gz
sudo cp iqtree-1.6.12-Linux/bin/iqtree /usr/local/bin
~~~~~~

### Install Boost C++
Needed in order to build RevBayes.
~~~~~~
cd
sudo apt-get install libboost-all-dev   # this takes awhile
~~~~~~

### Install [RevBayes](https://revbayes.github.io/compile-linux)
~~~~~~
# not necessary to issue this command --> sudo apt install build-essential cmake libboost-all-dev
git clone https://github.com/revbayes/revbayes.git
cd revbayes/projects/cmake
./build.sh # this step takes a really long time!
~~~~~~

### Install dataset for RevBayes tutorial
~~~~~~
cd
curl -LO https://revbayes.github.io/tutorials/ctmc/data/primates_and_galeopterus_cytb.nex
sudo mkdir /usr/local/share/examples/mole/revbayes
sudo mv primates_and_galeopterus_cytb.nex /usr/local/share/examples/mole/revbayes/
~~~~~~
    
### Install [PAUP*](http://phylosolutions.com/paup-test/)
~~~~~~
cd
curl -LO http://phylosolutions.com/paup-test/paup4a166_ubuntu64.gz
gunzip paup4a166_ubuntu64.gz
sudo mv paup4a166_ubuntu64 /usr/local/bin/paup
sudo chmod +x /usr/local/bin/paup
~~~~~~

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

### Install data files for PAML lab
~~~~~~
cd
wget https://molevol.mbl.edu/images/d/df/PamlLab.zip --no-check-certificate
unzip PamlLab.zip
rm PamlLab.zip
rm -rf __MACOSX
sudo mv PamlLab /usr/local/share/examples/mole/
~~~~~~

### Create alias to mole folder
Allows students to type moledir to go to the example data directory for the course.
~~~~~~
cd
cat - > mole-setup.sh
alias moledir="cd /usr/local/share/examples/mole"
# Ctrl-d to close file
sudo mv mole-setup.sh /etc/profile.d
~~~~~~

{% comment %}
Date: 08/11/2019

Your Instance Information: 
* Name: Ubuntu 18_04 Devel and Docker 
* IP Address: 149.165.157.190 
* SSH Username: plewis 
* SSH Keys deployed for root: cormy 
* UUID: b3668757-f1a6-4aec-b786-87f074241ae5 
* Cloud Provider: Jetstream - Indiana University 
* Launched at: Aug, 11 2019 18:58:31 UTC (Aug, 11 2019 13:58:31 Arizona time) 

Xsede portal:
portal.xsede.org

Info from the intro video:
1-866-907-2383
"allocation" associated with a project
"account" associated for a person
ssh login.xsede.org
[31 min mark]
gsissh <machine-name>
after login, type "interact" (Ctrl-d to exit) to use interactive mode
batch mode: sbatch, sinfo, squeue, scancel (slurm.schedmd.com for help with slurm)
[36 min mark]
slurm script example: 
  #!/bin/bash
  #SBATCH -J "Hello MPI"
  #SBATCH -N 8
  #SBATCH --ntasks-per-node=24
  #SBATCH -t 1:00:00
  ibrun ./hellompi.exe
User "#SBATCH --account=<account>" or "#SBATCH -A <account>" to charge to correct account if more than one
squeue: P (pending), R (running), CG (completing), F (failed), C (canceled)
"scancel jobid" or "scancel -u username"
"sinfo -s"
[48 min mark]
$HOME filesystem: permanent but small (good for building software)
$WORK filesystem: more space, but temporary (good for running jobs)
$SCRATCH filesystem ?
rsync -rltpDv -e 'ssh -l joeuser' source_directory data.bridges.psc.edu:target_directory
[51 min mark]
Dec 15 thru Jan 15 --> April 1 allocation begin date

https://use.jetstream-cloud.org/application/images
Ubuntu 18.04 Devel and Docker
{% endcomment %}
