# molevolworkshop.github.io

This repository hosts the GitHub Pages web site for the
Workshop in Molecular Evolution, Marine Biological Laboratory, Woods
Hole, Massachusetts.

If you are instead interested in seeing the actual
web site, please visit
[molevolworkshop.github.io](https://molevolworkshop.github.io) instead.

For faculty wishing to update their workshop lectures or labs, please look at [this](https://github.com/molevolworkshop/moledata) repository instead.
For faculty wishing to update their profile page, please look at `README` in the `_faculty` folder.

## Organization of the web site

The web site has a landing page (the home page) and several other main
pages accessible via the main menu at the top (About, Faculty, Schedule,
and Other). The next sections point out which files contain the
information for these pages.

Lectures and lab materials are stored in [moledata](https://github.com/molevolworkshop/moledata) but are pulled onto the website files upon deployment. 

### Website data

Many pages of the website generates content from the information in the `_data` folder.
Please see the `_data/README.md` for more information on the data files and format.

### Home page

The home page is the page you land on when you visit
[molevolworkshop.github.io](https://molevolworkshop.github.io). It is
determined by the file _index.md_.

### About page

The _about.md_ file describes the workshop: when it began, the emphases
of the course, and the software introduced.

### People page

The _people.md_ is generates a page containing lists of current faculty, participants, and past faculty.
Where applicable, the names will be converted to hyperlinks to the appropriate faculty webpage or personal webpage.
This page uses `faculty-registry.csv`, `participants.csv`, and `former-faculty.csv` in the `_data` folder to generate the appropriate tables. 
The actual layout and style of the page is set in `_layouts/people.html`. Updating the contents of the people page only requires updating the corresponding data files.

### Faculty pages

Faculty have personal pages, which reside in the directory _\_faculty_.
Each faculty member page briefly describes their research, range of dates the faculty member will be at the
workshop, a head shot, and contact info.
See the `README.md` in the  _\_faculty_ folder for more information on these pages.


### Schedule page

The _schedule.md_ will generate a page that contains the daily schedule, and links to relevant materials to each presentation or lab.
This page uses `event-schedule.csv`, and `faculty-registry.csv` to generate the appropriate tables. 

Lecture materials stored in the `moledata` repo gets brought into the website upon deployment and is renamed to the `materials` folder.
This means that if you want to link to a specific file that has the directory structure `moledata/lectures/topic/lecture.pdf`, you can do so with `({{ site.baseurl }}/materials/lectures/topic/lecture.pdf)`.

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

**NOTE:** The website **is** updated when new commits are made to `moledata`, which the website clones prior to deploying. Additionally, the website can manually be rebuilt with Github Actions.

You can build the website locally with the following commands 
```
./scripts/prep_build.sh #downloads moledata and makes index files for labs
bundle exec jekyll serve 

```

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

