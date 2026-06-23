# Updating faculty webpages

Each faculty member will have a workshop webpage.
We recommend copying the `Template` folder, renaming it to your lastname in lowercase, and editing as needed.
This webpage is meant to give a brief overview of your research program and the content you will be covering at the workshop.

Any educational material should be uploaded to the [moledata](https://github.com/molevolworkshop/moledata) repository, **not** here.

## FAQ for Faculty


### How do I edit my personal page?

Click on your markdown page and click the pencil icon in the upper right (just to the left 
of the trashcan icon) to create a fork and start a Pull Request

### What are those lines at the top between lines of hyphens?

This web site is built by [Jekyll](https://jekyllrb.com), and these first few lines (the 
frontmatter) tell Jekyll what page layout to use, what title should be displayed, and what 
permalink should be used to access the page. Please leave the frontmatter as-is, because 
that ensures consistency across all faculty web pages.

### How do I add a heading

Headings in markdown are indicated by starting a line with several hash characters. One hash
 (#) produces a level 1 heading (probably too big for your personal page), two
hashes (##) represent a level 2 heading, three hashes (###) produce a level-3 heading, etc.

### How do I add a link to an email address?

Either of the constructs below would make a link to Paul's email address, with the only difference
being that the second would not show _Paul O. Lewis_ to the user rather than the actual email address:
~~~~~~
[paul.lewis@uconn.edu](mailto:paul.lewis@uconn.edu)
[Paul O. Lewis](mailto:paul.lewis@uconn.edu)
~~~~~~

### How do I add a link to an external site?

The following would add a link to the [University of Connecticut EEB Department](https://eeb.uconn.edu/) to  page. The 
part in square brackets is the link text (what the view of the web page sees):
~~~~~~
[University of Connecticut EEB Department](https://eeb.uconn.edu/)
~~~~~~

### How do I add a link to another page within this web site?

This would produce a link to [Peter Beerli](/faculty-beerli/)'s personal page:
~~~~~~
[Peter Beerli](/faculty-beerli/)
~~~~~~

### How do I add an image?

The simplest way to add an image is to start a normal link with an exclamation point:
~~~~~~
![Moi]({{ 'img/headshot.jpg' | relative_url }})
~~~~~~
This would show the image at its actual size (which might be much to large or much too small) and 
place the caption _Moi_ below it. We have created a custom [Liquid Tag](https://jekyllrb.com/docs/liquid/tags/)
to make it easier to place images on your personal page that are sized correctly. 

To use the custom Liquid tag, add something like this:
~~~~~~
{% include figure.html description="Paul" url="/faculty/lewis/img/300px-Irobot.jpg" height="300px" css="image-right" %}
~~~~~~
The initial part `{% include figure.html` should not be modified. You can change the 
description, url, height, and css attributes however to suit your purposes. 

**Important:**
* Note that the only options for `css` are `image-left`, `image-center` and `image-right`.
* Note that the url provided must be the actual path from the root of the web site 
to the image file (don't be tempted to use the permalink specified in the frontmatter
of your personal page as part of this url)\

### Is there a limit to the size of files I can upload?

Short answer, yes! If we don't want to pay for hosting our site on GitHub Pages (and we don't), then we need
to be frugal with respect to content. Scroll down to the Usage Limits section of the 
[About GitHub Pages](https://help.github.com/en/github/working-with-github-pages/about-github-pages) 
section for the details, but the bottom line is that there must be less than 1 GB of 
content in the published site. Thus, please try to **reduce the size** of any PDF file 
you add (ask for help with this if you don't know how to do this) and pre-shrink your image
files to reasonable sizes (e.g. 500 pixels in width/height) and specifying screen resolution (72 dpi).
Do not use this repository to store lectures from past years!





