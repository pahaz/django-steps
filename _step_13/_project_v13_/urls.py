from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from customauth.urls import urlpatterns as auth_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^complaints/', include("complaints.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include("comments.urls")),
)

urlpatterns += auth_urlpatterns

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
