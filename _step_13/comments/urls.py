from comments.views import CommentCreateView
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

__author__ = 'pahaz'

urlpatterns = patterns('',
   url(r'^add$', CommentCreateView.as_view(), name="comments_add"),
)
