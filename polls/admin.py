#!/usr/bin/env python
# coding=utf-8

""" Admin for polls application

Polls Admin
***********

.. module:: polls
   :synopsis: admin for polls application

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

from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)