--- 
layout: page 
title: Alignment Lab 
permalink: /labs/alignment/ 
--- 

## Expected learning outcomes

The objective of this activity is to become familiar with the features
of multiple alignment and alignment visualization programs. This
includes data input and output, basic visualization and editing
functions, alignment options, and differences between nucleotide and
amino acid alignments.

Most importantly, you should be able to run analyses on your remote
Jetstream compute node and move files to and from the remote computer
and your local machine. Transferring data between your computer and a
remote machine is necessary in all following labs.

## About this lab

Software used in this workshop assumes that input data is aligned. If
you want to use your own sequencing data during the workshop, you will
need to go through the process of multiple sequence alignment (MSA). We
focus here on gene sequences, which can be from targeted Sanger data or
assembled genomic data. Many contemporary studies use reference-based
short read alignment, but at least some of the underlying theory is the
same. We do not cover short read alignment, but reference-based
alignment resources are provided at the end of the tutorial.

## Background

If you feel you need more background in MSA before starting the
tutorial, please consult the pages linked below:

* [General Background](/labs/alignment/general-background/) 
* [MAFFT Background](/labs/alignment/MAFFT-background/) 
* [MUSCLE Background](/labs/alignment/MUSCLE-background/)

## Getting started

While a large number of alignment programs have been developed, we are
going to focus on MAFFT and ‎MUSCLE. Alternatives may be more accurate
on small data sets, but these programs perform well even on fairly large
data sets and are thus part of many phylogenomic pipelines (e.g. Yang
and Smith 2014). The MAFFT algorithms and options can be viewed
[here](http://mafft.cbrc.jp/alignment/software/algorithms/algorithms.
html). The MUSCLE user guide is found at
[here](https://drive5.com/muscle5/manual/commands.html).

Both MAFFT and MUSCLE are available on your Jetsream node. You will
transfer sequences to the Jetsream node using scp or cyberduck, run the
programs as needed remotely, and then transfer back in the same way for
visualization on your own laptop. Remote nodes are great for analyses,
but if this is your first time using one, you will need to get
accustomed to using computers without a graphical user interface (GUI).

For visualization we will use the programs
[SeaView](http://doua.prabi.fr/software/seaview) or [MEGA](https://megasoftware.net/) (whichever works for you). Both programs are
relatively simple alignment viewers, but also allows you to estimate simple
distance-based trees and invoke alignment programs. You can access help
files at any time within the program by clicking on ‘Help’ in the top menu. Another good alternative is
[AliView](http://www.ormbunkar.se/aliview/). AliView is great for
looking at properties of very large alignments. Tree building options in
alignment viewers are not publication quality, but they can be useful if
checking for contamination or homology errors.

If you have not downloaded SeaView or MEGA, do so now using the following links:

SeaView:
* [Select your OS](http://doua.prabi.fr/software/seaview)

MEGA:
* [Select your OS](https://megasoftware.net/)

This activity is structured to be done either by yourself or with a
partner. Working with a partner is a great idea!

You will run the alignment software on your remote Jetstream node. Login to your node as explained in the [computer lab intro](/labs/intro/).

Create a new, empty directory named _MSAlab_ and use the following command to copy the tutorial files there:
~~~~~~
cp moledata/MSAlab/* MSAlab
~~~~~~

## Exercise 1: basic functions in SeaView and MEGA

Copy the _1ped.fasta_ file from your remote machine to your laptop. If you cannot
remember how to use the scp command, take a look at the [computer lab intro](/labs/intro/).
The _1ped.fasta_ file contains alcohol dehydrogenase
nucleotide sequences from a variety of organisms; modified from
BAliBASE. 

Start SeaView or MEGA. Load the data set _1ped.fasta_ by going to _File > Open_ (in MEGA, select _Align_ in the popup window after opening the file). Have a look at the data. Does it look like it's already been aligned? Try some of the basic
commands. To select a taxon, click on any taxon name on the left side.
You can copy the sequence using the _Copy selected sequences_ command in
the edit menu. These can then be pasted into a text editor (e.g.
Notepad++ on Windows or BBEdit on Mac) if needed. To select all sequences at once, on Macs
you can type Command-A. On Windows or Linux, you can use Control-A.
Explore the edit menu and observe how sequences can be reversed,
complemented, etc. Do not close the window, but move it aside for now.

## Exercise 2: comparison of two different alignment programs (MAFFT and MUSCLE) using nucleotide sequences

Programs such as MAFFT and MUSCLE and many others use _flags_ to
designate input options. These are usually a dash (-) before the
command, or in the case of MAFFT a double dash (--). Sometimes programs
will use a single dash with and abbreviation or a single letter to
invoke and option as well as a set of double dashes for more verbose
forms of those options. Examples are given throughout this lab and will
become intuitive throughout the workshop.

**Change directories into the MSAlab folder.** Refer to the [computer
lab intro page](/labs/intro/) if you have forgotten how to do this.

### Run MAFFT

Run a progressive alignment in MAFFT on the cluster by using the
command: 
~~~~~~
mafft --retree 2 1ped.fasta > mafft_dna.fasta
~~~~~~
The breakdown of this command is:
* `mafft` starts the program MAFFT
* `--retree 2` tells MAFFT to run a progressive alignment. MAFFT uses double
dashes (--) for its options. You can see why it is `--retree 2` on the
MAFFT webpage linked above.
* `1ped.fasta` is the input file name. Place it before the `>` and after all flags
* `mafft_dna.fasta` tells MAFFT to place the output alignment in the
file _mafft_dna.fasta_. For many programs a `>` designates where to
place the output. If the `>` symbol is unfamiliar to you, take a look
back at the [advanced UNIX tutorial](/unix-tutorial/).

Once the alignment process is completed, transfer the file to your own
computer (through scp or Cyberduck) and open it in an alignment viewer (e.g. Seaview or MEGA) as in
exercise 1. A new window with the aligned data will appear.

### Run MUSCLE

Run a standard alignment in MUSCLE on the cluster by using the command:
~~~~~~
muscle -log muscle_dna.log -align 1ped.fasta -output muscle_dna.fasta
~~~~~~
The breakdown of this command is:
* `muscle` starts the program MUSCLE
* `-log muscle_dna.log` instructs MUSCLE to place all the
output except the alignment itself to the log file called
*muscle_dna.log*. This file will then include things like the gap penalty
used, etc.
* `-align 1ped.fasta` specifies the input file to MUSCLE.
* `-output muscle_dna.fasta` instructs MUSCLE to place the alignment
in the file *muscle_dna.fasta*. Note that `-log` are not always
needed but it allows you to see the default options in MUSCLE.

### Compare MAFFT and MUSCLE alignments

Once the MUSCLE alignment is done, transfer the aligned fasta file to
your own computer (through scp or Cyberduck) and open it in your alignment viewer. A
new window with the aligned data will appear.

Compare the alignments resulting from MAFFT and MUSCLE. Are they
different? How many columns are in each the MAFFT or the MUSCLE
alignment? What may be wrong with both? (Hint: these are protein coding
genes).

Build 2 trees, one from each of your nucleotide
alignments: 
* Go to your aligned nucleotide sequences window (for both MAFFT and
MUSCLE alignments) and click on *Trees > Distance Methods > NJ*
* Use a J-C distance metric
* De-select the *ignore all gap sites* checkbox, then click to calculate
100 bootstraps.
* Note: these trees are easy for helping to evaluate your alignments,
but this program should never be your tree building method).

Compare the trees from both the MAFFT and MUSCLE alignments. Do the
topologies and/or branch lengths differ? (Hint: look up some species
names to get an idea of the expected topology!)

## Exercise 3: comparison of two different alignment approaches in MAFFT using protein sequences 

In this exercise we will convert the nucleotide sequences to their
equivalent protein sequences and align these instead. Note that because
we are running the alignment programs outside of our alignment viewers, you will not
be able to convert back to the original DNA sequences post alignment. If this were to be
run through SeaView or MEGA itself this could be done.

* Return to the alignment viewer window with the unaligned 1ped.fasta sequences.
* Click *Props > View as proteins* (SeaView) or select Translated Protein Sequences in the main alignment window (MEGA)
* Click *File > Save prot alignment* (SeaView) or *Data > Export alignment* (MEGA) and save the file as
*1ped_aa.fasta* with Fasta as the file format
* Transfer this file to the _MSAlab_ folder on the remote machine
* Run an iterative alignment in MAFFT by using the
command:
~~~~~~
mafft --maxiterate 1000 1ped_aa.fasta > mafft_aa_iter.fasta
~~~~~~
Comparing the command to the MAFFT command in exercise 2, you will
notice a new option, 
`--maxiterate 1000`, which instructs MAFFT to run an iterative alignment
with maximum 1000 cycles. 
* Load the *mafft_aa_iter.fasta* file into your alignment viewer
* Build a tree using your protein alignment by selecting *Trees >
Distance Methods > NJ*, selecting a Poisson distance metric, de-clicking
_ignore gaps_ and do a bootstrap test as above (SeaView) 
or select *Phylogeny > Construct/Test Neighbor-Joining Tree*, choose the *mafft_aa_iter.fasta* file and then 
select *Protein sequences*, followed by OK on the next window to choose the default Poisson distance metric (MEGA)
* Using the same _1ped_aa.fasta_ file, employ the MAFFT automatic selection
of alignment strategy by using the command: 
~~~~~~
mafft --auto 1ped_aa.fasta > mafft_aa_auto.fasta
~~~~~~
You can see that now we use the flag `--auto` to tell MAFFT to choose the
best alignment strategy. Can you determine what strategy was employed? (hint MAFFT outputs
data to the screen and the strategy should be listed near the end). Load
this file into your alignment viewer.
* Build a tree using your protein alignment by selecting *Trees >
Distance Methods > NJ*, select the Poisson distance metric, de-select
ignore gaps and use bootstrapping (SeaView) or click *Phylogeny > Construct/Test Neighbor-Joining Tree*, choose the *mafft_aa_auto.fasta* file and then 
select *Protein sequences*, followed by OK on the next window to choose the default Poisson distance metric (MEGA)

Compare amino acid alignments and trees. Which one do you prefer? Does
it make sense to align protein-coding sequences using the protein
translation, or should you instead build alignments from nucleotide
sequences?

## Exercise 4: exploring the difference in gap penalties using MUSCLE

We will now run MUSCLE with different gap penalties to observe how this
changes the alignment.

Run MUSCLE with a gap penalty of -20 using the command:
~~~~~~
muscle -verbose -log muscle_gap-20.log -align 1ped_aa.fasta -output muscle_aa_gap-20.fasta -gapopen -20
~~~~~~
A new flag has been added
here (`-gapopen -20`) to instruct MUSCLE to set the gap opening penatly to
-20. Load the alignment into your alignment viewer and build a tree as in exercise 3.

Run MUSCLE with a gap penalty of -1 using the command:
~~~~~~
muscle -verbose -log muscle_gap-1.log -align 1ped_aa.fasta -output muscle_aa_gap-1.fasta -gapopen -1
~~~~~~
The flag (`-gapopen -1`) instructs MUSCLE to set the gap opening penatly to -1. Load the
alignment into your alignment viewer and build a tree as in exercise 3.

Run MUSCLE with the default gap penalty using the command:
~~~~~~
muscle -verbose -log muscle_defGap.log -align 1ped_aa.fasta -output muscle_aa.fasta
~~~~~~

Load the alignment into your alignment viewer and build a tree as in exercise 3.

How do the modified gap penalty alignments compare to the default one?
Which alignment has the most gaps? The log files from MUSCLE will tell
you the gap penalty used for each alignment?

**Protip** Try moving all three MUSCLE amino acid alignments to your
laptop with scp! Assuming that the IP address of your remote machine is 123.45.67.89:
~~~~~~
scp username@123.45.67.89:MSAlab/muscle_aa*.fasta .
~~~~~~

## Codon Alignments

This is not part of the exercises, it's just for your future information.

As you now know, it is not appropriate to align nucleotides of protein
coding regions. In the exercises above, you translated the nucleotides
to amino acids which you could use to infer trees. But sometimes you
want to analyze nucleotides that have been aligned by codon. ([Joe
Bielawski](/faculty-bielawski/) will talk about some analyses that
necessitate this kind of alignment.) So how do you go from an amino acid
alignment back to codon-aligned nucleotides? You can use the [Pal2Nal
server](http://www.bork.embl.de/pal2nal/) for this. You will upload your protein
alignment and nucleotide sequences, and it will spit out the codon
alignment. Please be aware that your nucleotides must be multiples of
three (i.e. a full open reading frame).

Another great option is to use PRANK (Löytynoja and Goldman 2005), which
can use codon-aware data structures for alignment. Many people now write
their own scripts for back-translation of aligned amino acids.

{% comment %}
Here is a very ugly [Perl script](https://github.com/gtiley/Alignment_Tools/tree/master/
Codon_Alignment) I (George Tiley) wrote when starting grad school.
{% endcomment %}

## Filtering

There are various approaches to filter poorly aligned sites out of your
alignment
([Gblocks](http://molevol.cmima.csic.es/castresana/Gblocks.html);
Castresana 2000), but in some cases filtering does not improve and can
even worsen tree estimation (Tan et al. 2015). Another strategy is to
integrate over alignment uncertainty in a Bayesian framework ([BAli-Phy](http://www.bali-phy.org);
Redelings and Suchard 2005). All strategies can be justified on some
basis but will come with limitations, and it is ultimately up to you to
decide the most appropriate course of action for your data.

## Reference-Based Alignment

In some cases it is easier to generate low-coverage genomic data,
RADseq, or other subsamples of the genome and align to some
well-assembled reference, Especially for population genetics, but also
in species-level phylogenetic studies (e.g. Grewe et al. 2017;
Figueiró et al. 2017; Rochette et al. 2019). This process is a little
different than the progressive MSA discussed here, but a common short
read aligner is bwa (Li and Durbin 2009). This type of reference-based
alignment can then be followed by genotyping using various variant callers, including GATK (McKenna et al.
2010, Poplin et al. 2017) and mpileup (Danecek et al. 2012) to name just two, which use the quality information from massively parallell high throughput sequencers to call variants and heterozygotes. Other genotype callers with a
philosophically different approach to variant calling are ANGSD
(Korneliussen et al. 2014) and graphtyper (Eggertson et al. 2017), which have many population genetic
applications, but not many phylogenetic methods can leverage genotype
likelihoods. These topics fall outside of the scope of our workshop, but
the development teams for many of these software have fantastic tutorials that
you should be able to follow with skills developed here.

## References

Castresana, J. 2000. Selection of conserved blocks from multiple alignments for their use in phylogenetic analysis. Molecular Biology and Evolution 17:540-552.

Danecek P, Bonfield JK, Liddle J, Marshall J, Ohan V, Pollard MO, Whitwham A, Keane T, McCarthy SA, Davies RM, Li H. 2012. Twelve years of SAMtools and BCFtools, GigaScience 10(2):giab008

{% comment %}
DePristo M, Banks E, Poplin R, Garimella K, Maguire J, Hartl C, Philippakis A, del Angel G, Rivas MA, Hanna M, McKenna A, Fennell T, Kernytsky A, Sivachenko A, Cibulskis K, Gabriel S, Altshuler D, Daly M. 2011. A framework for variation discovery and genotyping using next-generation DNA sequencing data. Nature Genet. 43:491-498.
{% endcomment %}

Grewe F, Huang J-P, Leavitt SP, Lumbsch HT. 2017. Reference-based RADseq resolves robust relationships among closely related species of lichen-forming fungi using metagenomic DNA. Sci Rep. 7:9884

Eggertsson HP, Jonsson H, Kristmundsdottir S, Hjartarson E, Kehr B, Masson G, Zink F, Hjorleifsson KE, Jonasdottir A, Jonasdottir A, Jonsdottir I, Gudbjartsson DF, Melsted P, Stefansson K, Halldorsson BV. 2017. Graphtyper enables population-scale genotyping using pangenome graphs. Nat Genet 49:1654–1660.

Figueiró HV, et al. 2017. Genome-wide signatures of complex introgression and adaptive evolution in the big cats. Sci Adv. 7:1700299.

Korneliussen TS, Albrechtsen A, Nielsen R. 2014. ANGSD: Analysis of Next Generation Sequencing Data. BMC Bioinformatics. 15:356.

Li H, Durbin R. 2009. Fast and accurate short read alignment with Burrows–Wheeler transform. 25:1754-1760.

Löytynoja A, Goldman N. 2005. An algorithm for progressive multiple alignment of sequences with insertions. Proc Natl Acad Sci USA. 102:10557-10562.

McKenna A, Hanna M, Banks E, Sivachenko A, Cibulskis K, Kernytsky A, Garimella K, Altshuler D, Gabriel S, Daly M, DePristo MA. 2010. The Genome Analysis Toolkit: a MapReduce framework for analyzing next-generation DNA sequencing data. Genome Res. 20:1297-303.

Poplin R, Ruano-Rubio V, DePristo MA, Fennell TJ, Carneiro MO, Van der Auwera GA, Kling DE, Gauthier LD, Levy-Moonshine A, Roazen D, Shakir K, Thibault J, Chandran S, Whelan C, Lek M, Gabriel S, Daly MJ, Neale B, MacArthur DG, Banks E. 2017. Scaling accurate genetic variant discovery to tens of thousands of samples. bioRxiv. doi:10.1101/201178. 

Redelings BD, Suchard MA. 2005. Joint Bayesian estimation of alignment and phylogeny. Syst. Biol. 54:401-418.

Rochette NC, Rivera-Colón AG, Catchen JM. 2019. Stacks 2: Analytical methods for paired-end sequencing improve RADseq-based population genomics. bioRxiv. doi: 10.1101/615385.

Tan G, Muffato M, Ledergerber C, Herrero J, Goldman N, Gil M, Dessimoz C. 2015. Current methods for automated filtering of multiple sequence alignments frequently worsen single-gene phylogenetic inference. Syst. Biol. 64:778-791.

Yang Y, Smith SA. 2014. Orthology inference in nonmodel organisms using transcripts and low-coverage genomes: improving accuracy and matrix occupancy for phylogenetics. Mol. Biol. Evol. 31:3081-3092.
