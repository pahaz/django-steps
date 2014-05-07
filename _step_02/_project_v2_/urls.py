from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^complaints$', "complaints.views.index", name="complaints_index"),
    url(r'^complaints/add$', "complaints.views.post", name="complaints_post"),

)
