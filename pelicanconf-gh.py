#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'James Dey'
SITENAME = 'Climate Solutions'
SITESUBTITLE='Articles'
SITEURL = 'https://deytalytics.github.io/climatesolutions'

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
LINKS = (('Deytalytics.com','http://www.deytalytics.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/climatesolutions'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='bootstrap2'

SEARCH_BOX = True

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'search','blog','dev_projects'))

DISQUS_SITENAME="climatesolutions"

MAINMENUITEMS=(('Articles','blog.html'),('Development Projects','dev_projects.html'))

PDF_PROCESSOR=True

PLUGIN_PATHS=['pelican-plugins',]
PLUGINS=['pdf',]

AUTHORS_URL = 'blog/authors.html'
AUTHORS_SAVE_AS = 'blog/authors.html'