# molevolworkshop.github.io

This repository hosts the Jekyll-based GitHub Pages web site for the
Workshop in Molecular Evolution, Marine Biological Laboratory, Woods
Hole, Massachusetts.

This document provides information for the web site maintainers about
how everything works. If you are instead interested in seeing the actual
web site, please visit
[molevolworkshop.github.io](https://molevolworkshop.github.io) instead.

This README file is organized so that information needed by faculty who just want 
to know how to update their personal page is at the top (see the next section). As you scroll down, the
information gets more and more detailed such that the material at the bottom will only
be useful to someone charged with maintaining the site and who thus needs to know about
all the tweaks that have been done to the basic theme.

## FAQ for Faculty

### Where do I find my personal page?

Scroll to the top of this page and click on the _faculty_ folder and then your folder within
the _faculty_ folder. You should now see an _img_ folder, a _pdf_ folder, and a markdown file
(e.g. _lewis.md_). Put images that you link to in your page in the _img_ folder, PDF files 
from your lectures into the _pdf_ folder, and edit your markdown file to change the content 
of your personal web page.

### How do I edit my personal page?

Click on your markdown page and click the pencil icon in the upper right (just to the left 
of the trashcan icon). If no edit (pencil) icon is present, it means that you do not yet 
have permission to edit anything. Send your GitHub account username to the 
[directors](mailto:moledirectors@mbl.edu) and we will be happy to add you as a collaborator.

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

You can also create a link relative to the location of the page where the link is being added. 
For example, to link to a PDF file named _mylecture.pdf_ inside your _pdf_ folder, you could
use this construct:
~~~~~~
[My Lecture]({{ 'pdf/mylecture.pdf' | relative_url }})
~~~~~~
This makes use of something known as a [Liquid filter](https://jekyllrb.com/docs/liquid/filters/), which
is the part inside the parentheses (and including the paired double curly brackets). 

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

### How do I create a simple table?

Tables couldn't be simpler to create in markdown:
~~~~~~
Lecturer    |       Affiliation                 
----------  | ----------------------------------
Beerli      | Florida State University          
Bielawski   | Dalhousie University              
Chang       | University of Toronto             
Edwards     | Harvard University University     
Heath       | Iowa State University             
Huelsenbeck | University of California-Berkeley 
Knowles     | University of Michigan            
Kubatko     | Ohio State University             
Lewis       | University of Connecticut         
McTavish    | University of California-Merced   
Minh        | Australian National University    
Solís-Lemus | University of Wisconsin           
Swofford    | University of Florida             
Tiley       | Duke University                   
Yoder       | Duke University                   
~~~~~~

The vertical bar (created using pipe `|` characters) is the boundary between columns, and
the horizontal bar (created using hyphen `-` characters) is the boundary between the header
line and the ordinary table lines. You can justify particular columns using colons in 
the line of hyphens defining the boudary separating header and table. For example, this
woud cause lecturar names to be right justified and affiliation to be left justified:
~~~~~~
Lecturer    |       Affiliation                 
----------: | :-------------------------------
Beerli      | Florida State University          
Bielawski   | Dalhousie University              
Chang       | University of Toronto   
  .         |        .          
  .         |        .          
  .         |        .          
Yoder       | Duke University                   
~~~~~~

The spacing is irrelevant: you do not need to be tidy as long as you get a vertical bar
between your columns. Also, the number of hyphens in each column of the header separator
does not matter (but you do need at least 3).

You may desire to have more control over your tables (e.g. want a particular column to be
wider or narrower), but markdown only allows pretty simple tables. Talk to the [directors](mailto:moledirector@mbl.edu)
if you feel you really need to do something more complicated and we can add CSS to the site
to do some simple tweaking of table format.

### Is there a limit to the size of files I can upload?

Short answer, yes! If we don't want to pay for hosting our site on GitHub Pages (and we don't), then we need
to be frugal with respect to content. Scroll down to the Usage Limits section of the 
[About GitHub Pages](https://help.github.com/en/github/working-with-github-pages/about-github-pages) 
section for the details, but the bottom line is that there must be less than 1 GB of 
content in the published site. Thus, please try to **reduce the size** of any PDF file 
you add (ask for help with this if you don't know how to do this) and pre-shrink your image
files to reasonable sizes (e.g. 500 pixels in width/height) and specifying screen resolution (72 dpi).
Do not use this repository to store lectures from past years!

### What if I have other questions?

Please contact the [workshop directors](mailto:moledirector@mbl.edu). Chances are that
if you have a question, then others have the same question and we should add another
entry to this FAQ.

## Organization of the web site


The web site has a landing page (the home page) and several other main
pages accessible via the main menu at the top (About, Faculty, Schedule,
and Other). The next sections point out which files contain the
information for these pages.

### Home page

The home page is the page you land on when you visit
[molevolworkshop.github.io](https://molevolworkshop.github.io). It is
determined by the file _index.md_.

### About page

The _about.md_ file describes the workshop: when it began, the emphases
of the course, and the software introduced.

### Faculty page

The _faculty.md_ page contains a listing of current faculty, in
alphabetical order, along with their affiliations and links to their
personal pages, which reside in subdirectories under the directory
_faculty_. Each faculty member subdirectory contains a markdown page
that describes the range of dates the faculty member will be at the
workshop, contact info, and links to lectures, tutorials, data sets, and
other materials referenced by that faculty member during their
lecture/lab. PDF files of lectures reside in the faculty member's own
_pdf_ subdirectory and a head shot of that faculty member resides in the
_img_ subdirectory. For example, _/faculty/lewis/lewis.md_ is Paul
Lewis' markdown page, Paul's lectures are in _/faculty/lewis/pdf_ and
Paul's photo is in _/faculty/lewis/img/ (along with other images
referenced in _/faculty/lewis/lewis.md_.

Note that faculty markdown files specify permalinks that follow the
convention _/faculty-lastname/_. For example, the front matter in
_/faculty/lewis/lewis.md_ contains.
~~~~~~
permalink: /faculty-lewis/
~~~~~~
{:.bash}

### Schedule page

The _schedule.md_ file contains a giant table showing the current year's
schedule, with links to each presentation. The presentation links are
either links to PDF files in a faculty member's _pdf_ subdirectory, or
are external links to tutorials stored on another web site.

### Other page

The _other.md_ contains links to all other material related to the
workshop, e.g. tshirt designs/contest, past group photos, etc. 

* The _tshirts.md_ file contains all known past t-shirt designs
* The _groupphotos.md_ file contains links to past group photos and
their keys, which are stored as markdown files in the _group-photos_
directory.

## Under the Hood

This section contains information about how the web site functionality
is implemented.

### Jekyll

This web site uses [Jekyll](https://jekyllrb.com) to generate a static
web site that is published as a GitHub Pages site. Jekyll creates the directory
*_site*, which can be deleted at any time because it is regenerated every time
a new commit is pushed to the repository that affects the web site content. 

### Markdown files

Jekyll generates HTML content using markdown files (which have the file
name extension .md). For purposes of finding markdown files to include,
Jekyll ignores any directory whose name begins with an underscore
character. Such directories are not completely ignored, but any markdown
files in them will not be converted to HTML content in the *_sites*
directory.

Markdown cheatsheets are available (links provied below) that show you
how to create links, show images, create lists and tables, etc. You may
be disappointed in how limited markdown seems to be. For example, you
cannot have lists within lists, and only very basic tables are possible
(no merging of rows or columns). It is possible to use CSS to achieve
some desired effects (i.e. make some table columns wider than they
ordinarily would be), but the simplicity of markdown encourages you to
write content that is easier to comprehend by your readers.

### Cheatsheet links

* [Devhints Jekyll Cheatsheet](https://devhints.io/jekyll)
* [Cloudcannon Jekyll Cheatsheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/)
* [Mark Dunkley Liquid Cheatsheet](http://cheat.markdunkley.com)
* [Adam Pritchard Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [GitHub Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)

### Liquid

Jekyll allows and makes heavy use of Shopify
[Liquid](https://help.shopify.com/en/themes/liquid/tags) tags,
variables, and filters, and adds some filters not documented on the
Shopify web site.

### Main menu

Pages that are featured on the main navigation menu at the top of each
page must be listed in the *_config.yml* file's *header_pages* list. The
order that the pages appear there determines their order in the menu at
the top.

Each page featured in the main menu must have an attribute in the front
material named _menutitle_ listing the word to use in the menu for that
page (it may be desirable to use a multiword _title_ attribute for the
page, but multiword menu items are just confusing).

The *_includes/header.html* file (included in all layouts) contains the
code for generating the menu. The *site.header_pages* array is assigned
to the liquid variable *page_paths*, unless *header_pages* has not been
defined, in which case the default behavior is to include all web site
pages in *page_paths*. The link in the menu is generated further down in
the file for only pages that possess a *menutitle* attribute. Thus, the
only penalty for failing to define *header_pages* in the *_config.yml*
file is that you don't get to determine the order in which the menu
items will occur.

### More coming soon...

