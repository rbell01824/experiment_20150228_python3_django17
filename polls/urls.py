#!/usr/bin/env python
# coding=utf-8

""" URLs for polls application

Polls URLs
**********

.. module:: polls
   :synopsis: URLs for polls application

.. moduleauthor:: Richard Bell <rbell01824@gmail.com>

Polls is a test application to get back into development with pycharm and django.

2/27/15 - Initial creation

Overview
========

TBD

.. note:: TBD

Base Classes
============
"""

# noinspection PyUnresolvedReferences
import logging

log = logging.getLogger(__name__)

__author__ = 'rbell01824'
__date__ = '2/27/15'
__copyright__ = "Copyright 2014, Richard Bell"
__credits__ = ['rbell01824']
__license__ = 'All rights reserved'
__version__ = '0.1'
__maintainer__ = 'rbell01824'
__email__ = 'rbell01824@gmail.com'

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
