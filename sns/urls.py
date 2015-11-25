"""sns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from sns import settings
from quanzi.views import*

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',                   

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^quanzi/logout/$', 'quanzi.views.logout'),
    url(r'^quanzi/login/$', 'quanzi.views.login'),
    url(r'^quanzi/register/$', 'quanzi.views.register'),
    url(r'^quanzi/index/$', 'quanzi.views.index'),
    
)