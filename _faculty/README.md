# Updating faculty webpages

Each faculty member will have a workshop webpage.
This webpage is meant to give a brief overview of your research program and the content you will be covering at the workshop.

Any educational material should be uploaded to the [moledata](https://github.com/molevolworkshop/moledata) repository, **not** here.

## FAQ for Faculty


### How do I edit my personal page?

You can fill out the Github Issue template [here](https://github.com/molevolworkshop/molevolworkshop.github.io/issues/new?template=faculty-profile.yml). 
Submitting an issue using the template will automatically create a Pull Request with an updated faculty bio page that maintainers can review before modifying the site.

Alternatively, each faculty member should already have a faculty page at a url specific to thier name (e.g., https://github.com/molevolworkshop/molevolworkshop.github.io/blob/main/_faculty/firstname-lastname.md) that you can edit directly and create a PR.
If you go this route please be sure to follow the frontmatter formatting (the lines at the top between the lines of hyphens)that you find in existing faculty pages to ensure it renders correctly.
Specifically, contact information, home institution, department, faculty position, photo, and arrival/departure dates are a part of the frontmatter.



### What are those lines at the top between lines of hyphens?

This web site is built by [Jekyll](https://jekyllrb.com), and these first few lines (the 
frontmatter) tell Jekyll what page layout to use, what title should be displayed, and some core information.
A template of the frontmatter looks like this:
```
---
layout: faculty
title: ""
name: "First Last"
role: ""
department: ""
institution: ""
headshot: "path/to/file.png or a url with the photo"
github: ""
email: ""
website: ""
arrival_date: "MM/DD/YY"
departure_date: "MM/DD/YY"
other_links:
  - label: "Wikipedia"
    url: "https://www.wikipedia.org/"
---
```

### How do I add an image for my head shot?

If you update your faculty page using the issue template you can drag and drop an image from your computer to the text box and it will automatically create a link for you.

Otherwise you could upload an image directly to this repo in the `_faculty/img` folder and adjust the frontmatter accordingly:
```
headshot: "/_faculty/img/name.png"
```

### Is there a limit to the size of files I can upload?

Short answer, yes! If we don't want to pay for hosting our site on GitHub Pages (and we don't), then we need
to be frugal with respect to content. Scroll down to the Usage Limits section of the 
[About GitHub Pages](https://help.github.com/en/github/working-with-github-pages/about-github-pages) 
section for the details, but the bottom line is that there must be less than 1 GB of 
content in the published site. Thus, please try to **reduce the size** of any PDF file 
you add (ask for help with this if you don't know how to do this) and pre-shrink your image
files to reasonable sizes (e.g. 500 pixels in width/height) and specifying screen resolution (72 dpi).
Do not use this repository to store lectures from past years!


