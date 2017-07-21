# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)
admin.site.register(Choice)


# Let’s see how this works by reordering the fields on the edit form. Replace the admin.site.register(Question) line with:

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# '''
# This isn’t impressive with only two fields, but for admin forms with dozens of fields, choosing an intuitive order is an important usability detail.
#
# And speaking of forms with dozens of fields, you might want to split the form up into fieldsets:
# '''
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)

'''
It’d be better if you could add a bunch of Choices directly when you create the Question object. Let’s make that happen.

Remove the register() call for the Choice model. Then, edit the Question registration code to read:
'''

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


    '''
    By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. 
    To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object:
    '''
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    '''
    add an improvement to the Question change list page: filters using the list_filter.
    '''
    list_filter = ['pub_date']

    '''
    That adds a search box at the top of the change list. When somebody enters search terms, Django will search the question_text field. 
    '''
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)