#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'K. Jarrod Millman'
SITENAME = u'Stat 222 (Spring 2016)'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = '_theme/'
INDEX_SAVE_AS = 'announcements.html'
MD_EXTENSIONS = (['toc'])

## Title menu options (this isn't necessary, but I wanted to have more control)
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
#MENUITEMS = [#('Announcements',
             # 'http://www.jarrodmillman.com/stat159-fall2015/announcements.html'),
             #('Syllabus',
             # 'http://www.jarrodmillman.com/stat159-fall2015/syllabus.pdf'),
             #('Calendar',
             # 'http://www.jarrodmillman.com/stat159-fall2015/cal.pdf'),
             #('Lectures/Labs',
             # 'http://www.jarrodmillman.com/rcsds'),
             #('Project',
             # 'http://www.jarrodmillman.com/stat159-fall2015/pages/project.html'),]

DISPLAY_TAGS_ON_SIDEBAR = False

LINKS = (('Course GitHub site', 'https://github.com/berkeley-stat222'),
         ('Piazza discussion site', 'https://piazza.com/berkeley/spring2016/stat222/home'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#STATIC_PATHS = (['files'])

CC_LICENSE = "CC-BY-NC-SA"
