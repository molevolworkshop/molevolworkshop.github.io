---
layout: page
title: Joe Bielawski
permalink: /faculty-bielawski/
---
{% include figure.html description="Joe Bielawski" url="/faculty/bielawski/img/JPB.jpg" css="image-right" height="250px" %}
## Institutional home pages

* [Research group page](http://www.bielawski.info)

* [Dept of Mathematics & Statistics](https://www.dal.ca/faculty/science/math-stats/faculty-staff/our-faculty.html)

* [Dept of Biology](http://www.dal.ca/faculty/science/biology/faculty-staff/our-faculty/joe-bielawski.html)]

* [GitHub](https://github.com/evoworks/)

<br>

## Arrival and Departure

* Arrival: 25 May 2024 (Sat)

* Depart:  04 June 2024 (Ts)

<br>

UPDATING TOC LINKS

## Content for workshop

* [Quick start: models & methods](#Quick-start-(models-&-methods))

* [Quick start: codon models](#Quick-start-(codon-models))

* [Lecture slides](#Lecture-slides)

* [PAML lab: English](#PAML-lab-(English))

* [PAML lab: Translated](#Translated-PAML-Tutorials)
  
* [Scientific ethics](#Scientific-ethics)

<br>

## Content for additional activties

* [Additional reading on codon models](#Getting-started)
  
* [Advanced PAML lab](#foo)

* [Best practices in genome scans](#foo)

* [Alternative software for codon models in the ML framework](#foo)


<br>
<br>

# Content for workshop
## Quick start (models & methods)

**Are you completely new to models of sequence evolution?**  Then [this review paper](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/00209.PUBLISHED.pdf) might be good for you.  Section 2 provides a great introduction to Markov models, but it can be skipped without any loss of continuity.

* **Citation:** Bielawski, J. P. (2016). Molecular Evolution, Models of. In Kliman, R.M. (ed.) Encyclopedia of Evolutionary Biology. Vol 1, pp. 61-70. Oxford: Academic Press.

**Do you some background in phylogenetics and DNA sequence models, but you are new to the are of detecting adaptive sequence evolution?**  Then [this review paper](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/00171.PUBLISHED.pdf) will give you a very broad starting point (population genetics, non-coding, codon and amino-acid-based methods).  

* **Citation:**  Bielawski, Joseph & Jones, Chris. (2016). Adaptive Molecular Evolution: Detection Methods. In Kliman, R.M. (ed.) Encyclopedia of Evolutionary Biology. Vol 1, pp. 16-25. Oxford: Academic Press.

<br>

## Quick start (codon models)

**Are you completely new to codon models?**  Then [this review paper](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/XXXXXXXXX.pdf) will give an accessible review of the theory of codon models and how they are used to investigate how protein coding genes evolve. 

* **Citation:**


**Do you want to take a deep dive into the theory and legitimate interpretation of codon models?** [This review paper](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Jones_etal_2019_Chapter13.pdf) combines evolutionary theory and statistical theory to explain the major inference challenges under codon models.  The paper concludes with a strong critique of the canonical interpretation of the dN/dS ratio (omega parameter) as a measure of adaptive change in protein function.

* **Citation:** Jones C.T., Susko E., Bielawski J.P.,  2019. Looking for Darwin in genomic sequences: validity and success depends on the relationship between model and data. In Evolutionary Genomics: Statistical and Computational Methods. Maria Anisimova (ed.) 2nd edition, Human press.]
  
<br>

## Lecture slides

From 2022 this lecture will provide a more general background on evolutionary forces, and the Neutral and Nearly-Neutral theories of molecular evolution. 

* **2023 Lecture slides (Part 1), Intro to Neutral & Nearly Neutral Theories of Molecular Evolution:** [slide set 1](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/slides/Bielawski_lecture_PART_1.pdf) (updated)

* **2023 Lecture slides (Part 2), Intro to Codon Models:** [slide set 2](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/slides/Bielawski_lecture_PART_2.pdf) (updated)

There will be minor updates to the slides in 2024, which will be posted soon.

<br>


## PAML lab (English)

The lab exercises (PAML demo) are available via small website (link below). The site contains some additional resources that are worth a look when you have time. Please note that slides may change a little prior to the lab. I will post modified PDFs as required. 

**PAML demo**: [PAML Lab website](https://awarnach.mathstat.dal.ca/~joeb/PAML_lab/lab.html)

**PAML demo resources**: [webpage](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/Resources.html)

**PAML demo slides**: [slides (PDF)](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/pamlDEMO_2023.pdf) (updated for 2023)

If you want doing the lab independently (at home, on your own time and on your own computer), then you can download all necessary files from an archive [here](https://bitbucket.org/EvoWorks/protocol-paml-lab-at-mbl-workshop/downloads/), or you can download the files individually [here](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/PAML_Lab_files.html).

**NOTE: If you are doing the PAML Lab at the workshop, then use the VM and the 
symlink in your home directory named "moledata" to obtain the course data files!!!**

<br>

## Translated PAML Tutorials

[Will add Portuguese and possibly Spanish language translations in Summer of 2024.]

<br>

## Scientific ethics

Beginning in 2022 we added a session dedicated to scientific ethics. Our discussions often touch on the many ways that science has “*unwritten rules*”, and how such rules can privilege members of some groups and serve as a barrier to members of other groups. If this is new to you, or if you just want to know more, here are a few resources.

One way that unwritten rules impact who succeeds in science is sometimes referred to as the “*hidden curriculum*”. These are best practices for success in STEM that first-generation and underrepresented minority students must navigate but are not taught in classrooms. With this in mind, we recently wrote a paper called ["Ten simple rules for succeeding as an underrepresented STEM undergraduate"](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010101) to help make explicit the hidden curriculum of science.

Many of the *unwritten rules* of science are the same as those that operate in society at large, including racism operating within people who adhere to egalitarian attitudes. In the essay [“Science in the Belly of the Beast: my Career in the Academy”](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Belly_of_the_Beast_2012.pdf) Joseph L. Graves, Jr. describes his personal experience with the unwritten rules of the academy, including the "one and one-quarter rule".

<br>
<br>

# Content for additional activties

## Additional readings and advanced topics 

* A novel phenotype+genotype codon-model (PG-BSM) formulated to test and identify sites within a gene involved in phenotypic adaptation.  This method does NOT require dN/dS>1 to infer adaptive molecular evolution!:<br>
(_[Jones, C. T., Youssef, N., Susko, E., & Bielawski, J. P. (2020). A Phenotype–Genotype Codon Model for Detecting Adaptive Evolution. Systematic biology, 69(4), 722-738.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Jones_Susko_Bielawski-2020_PG-BSM.pdf)_)

* Phenomenological load (PL) and biological conclusions under codon models:<br>
(_[Jones C.T., Youssef N., Susko E., Bielawski J.P., 2018. Phenomenological Load on Model Parameters Can Lead to False Biological Conclusions. Mol Biol Evol. 35(6):1473-1488.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Jones_PL_MBE2018.pdf)_)

* Review of major inference challenges under codon models:<br>
(_[Jones C.T., Susko E., Bielawski J.P.,  2019. Looking for Darwin in genomic sequences: validity and success depends on the relationship between model and data. In Evolutionary Genomics: Statistical and Computational Methods. Maria Anisimova (ed.) 2nd edition, Human press.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Jones_etal_2019_Chapter13.pdf)_)

* Positive selection, purifying selection, shifting balance & fitness landscapes:<br>
(_[Jones, C., Youssef, N., Susko, E. and Bielawski, J., 2017.  Shifting balance on a static mutation-selection landscape: a novel scenario of positive selection. Molecular Biology and Evolution, 34(2):391-407.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/ShiftBalance_MBE_2016.pdf)_)

* Improved inference of site-specific positive selection under a generalized parametric codon model when there are multi-nucleotide mutations and multiple nonsynonymous rates: <br>
(_[Dunn KA, Kenney T, Gu H, Bielawski JP. Improved inference of site-specific positive selection under a generalized parametric codon model when there are multinucleotide mutations and multiple nonsynonymous rates. BMC Evol Biol. 2019 Jan 14;19(1):22.](https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-018-1326-7)_)

* ModL: restoring regularity when testing for positive selection: <br>
(_[Mingrone J, Susko E, Bielawski JP. ModL: exploring and restoring regularity when testing for positive selection. Bioinformatics. 2019 Aug 1;35(15):2545-2554.](https://academic.oup.com/bioinformatics/article/35/15/2545/5239994)_)

* Smoothed Bootstrap Aggregation (SBA) for assessing and correcting parameter estimate uncertainty in codon models:<br>
(_[Mingrone, J., Susko, E. and Bielawski, J., 2016. Smoothed bootstrap aggregation for assessing selection pressure at amino acid sites. Molecular Biology and Evolution, 33(11):2976-2989.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Mingrone_SBA_MBE2016.pdf)_)

* Protocols, experimental design, and best practices for inference under complex codon models:<br>
(_[Bielawski, J.P., Baker, J.L. and Mingrone, J., 2016. Inference of episodic changes in natural selection acting on protein coding sequences via CODEML. Current Protocols in Bioinformatics, pp.6-15.](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/UNIT6.15.pdf)_)

<br>

## Alternative Lab (advanced inferences)

If you have some experience with codon models, and want to try out a tutorial for more advanced materials then use the link below to download an archive for a complete different set of PAML activities.  This tutorial focuses on detecting episodic protein evolution via **Branch-Site Model A**.  The tutorial also includes activities about (i) detecting **MLE instabilities**, (ii) carrying out **robustness analyses**, and (iii) use of **smoothed bootstrap aggregation (SBA)**.  The protocols for each activity are presented in Protocols in Bioinformatics UNIT 6.15.  The included PDF file for UNIT 6.16 also presents recommendations for "best practices" when carrying out a large-scale evolutionary survey for episodic adaptive evolution by using PAML.  The files required for this "alternative lab" are available via Bitbucket repository.  The repository link is given below.

**Advanced PAML demo:** [Bitbucket repository](https://bitbucket.org/EvoWorks/protocol-inference-of-episodic-selection/downloads)

**codeml_SBA:**  a program that implements Smoothed Bootstrap Aggregation (SBA) for assessing selection pressure at amino acid sites. [https://github.com/Jehops/codeml_sba](https://github.com/Jehops/codeml_sba)<br>

**DendroCypher:** a program to assist labelling the branches of a Newick-formatted tree-file for use with a “branch model” or a “branch-site codon model": [Bitbucket repository](https://bitbucket.org/EvoWorks/dendrocypher/downloads/)

<br>


## Best practices in large-scale evolutionary surveys

Large-scale evolutionary surveys are now commonplace. But with the use of progressively more complex codon models, these surveys are fraught with perils. Complex models are more prone to statistical problems such as MLE irregularities, and some can be quite sensitive to model misspecification.  UNIT 6.16 (see above) provides some recommended "best practices" for a **2-phase approach** to quality control and robustness in evolutionary surveys.  We have applied these to a large scale survey for functional divergence in nuclear receptors during homing evolution, and we used experimental approaches to investigate hypotheses about the role of a particular nuclear receptor (NR2C1) as a key modulator of developmental pluripotnetiality during hominid evolution. The paper that illustrates the power of such an evolutionary surgery, and the importance of an experimental design having explicit protocols for "best practices", is given below.

**Example large-scale survey**: [PDF](http://awarnach.mathstat.dal.ca/~joeb/PAML_lab/resources/Baker.905.full.pdf)

<br>

## Alternative software for codon models in the ML framework

**HyPhy:**  comparative sequence analysis using stochastic evolutionary models; [http://www.hyphy.org/](http://www.hyphy.org/)

**DataMonkey:**  a server that supports a variety of HYPHY tools at no cost; [http://www.datamonkey.org/](http://www.datamonkey.org/)

**COLD:**  a program that implements a general-purpose parametric (GPP) codon model. Most codon models are special cases of the GPP codon model. [https://github.com/tjk23/COLD](https://github.com/tjk23/COLD)

**codeml_SBA:**  a program that implements smoothed Bootstrap Aggregation for Assessing Selection Pressure at Amino Acid Sites.[https://github.com/Jehops/codeml_sba](https://github.com/Jehops/codeml_sba)

**ModL:**  a program for restoring regularity when testing for positive selection using codon models [https://github.com/jehops/codeml_modl](https://github.com/jehops/codeml_modl)

<br>

{% include figure.html description="At the Captain Kidd" url="/faculty/bielawski/img/TheKidd1b.jpg" css="image-center" height="250px" %}

{% include figure.html description="Workshop concept map" url="/faculty/bielawski/img/MOLE_concept_map_v2.jpg" css="image-center" height="250px" %}
