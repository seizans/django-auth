from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', 'bacon.views.home', name='home'),
    # url(r'^bacon/', include('bacon.foo.urls')),
    url(r'^app1/', include('app1.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='profile.html')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
