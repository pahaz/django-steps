from complaints.views import ComplaintIndexView, ComplaintDetailView

__author__ = 'pahaz'

from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', "complaints.views.index", name="complaints_index"),
   # url(r'^$', ComplaintIndexView.as_view(), name="complaints_index"),
   url(r'^page/(?P<page>[0-9]+)/$', ComplaintIndexView.as_view(), name="complaints_index_page"),
   # url(r'^(?P<pk>[0-9]+)/$', "complaints.views.detail", name="complaints_detail"),
   url(r'^(?P<pk>[0-9]+)/$', ComplaintDetailView.as_view(), name="complaints_detail"),
)
