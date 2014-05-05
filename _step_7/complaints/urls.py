__author__ = 'pahaz'

from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "complaints.views.index", name="complaints_index"),
)
