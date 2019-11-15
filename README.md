# molevolworkshop.github.io

This repository hosts the Jekyll-based GitHub Pages web site for the
Workshop in Molecular Evolution, Marine Biological Laboratory, Woods
Hole, Massachusetts.

This document provides information for the web site maintainers about
how everything works. If you are instead interested in seeing the actual
web site, please visit
[molevolworkshop.github.io](https://molevolworkshop.github.io) instead.

## Organization

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

