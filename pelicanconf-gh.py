#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'James Dey'
SITENAME = 'Climate Solutions'
SITESUBTITLE='Articles'
SITEURL = 'https://www.climatesolutions.org.uk/

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UK Committee for Climate Change','https://www.theccc.org.uk/'),('UK Climate Assembly','https://www.climateassembly.uk/'),('UK Department of Energy & Climate Change','https://www.gov.uk/government/organisations/department-of-energy-climate-change'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ClimateSoluti10'),('Linkedin','https://www.linkedin.com/company/uk-climate-solutions'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='bootstrap2'

SEARCH_BOX = True

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'search','blog','dev_projects'))

DISQUS_SITENAME="climatesolutions"

MAINMENUITEMS=(('Articles','climate-solutions-overview.html'),('','index.html'))

PDF_PROCESSOR=True

PLUGIN_PATHS=['pelican-plugins',]
PLUGINS=['pdf','sitemap']

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

AUTHORS_URL = 'blog/authors.html'
AUTHORS_SAVE_AS = 'blog/authors.html'