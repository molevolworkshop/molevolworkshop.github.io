# molevolworkshop.github.io

This repository hosts the GitHub Pages web site for the
Workshop in Molecular Evolution, Marine Biological Laboratory, Woods
Hole, Massachusetts.

If you are instead interested in seeing the actual
web site, please visit
[molevolworkshop.github.io](https://molevolworkshop.github.io) instead.

For faculty wishing to update their workshop lectures or labs, please look at [this](https://github.com/molevolworkshop/moledata) repository instead.
For faculty wishing to update their profile page, please look at `README` in the `faculty` folder.



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
that briefly describes their research, range of dates the faculty member will be at the
workshop, and contact info.A head shot of that faculty member resides in the
_img_ subdirectory. 

~~~~~~
permalink: /faculty-lewis/
~~~~~~


### Schedule page

The _schedule.md_ file contains a giant table showing the current year's
schedule, with links to each presentation.

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

**NOTE:** The website is **not** updated when new commits are made to `moledata`, which the website clones prior to deploying. Instead, the website can manually be rebuilt with Github Actions.

### Markdown files

Jekyll generates HTML content using markdown files (which have the file
name extension .md). For purposes of finding markdown files to include,
Jekyll ignores any directory whose name begins with an underscore
character. Such directories are not completely ignored, but any markdown
files in them will not be converted to HTML content in the *_sites*
directory.

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

