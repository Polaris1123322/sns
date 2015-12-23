"""mysite URL Configuration

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
from quanzi.views import *
from quanzi.util import zan, ping, getcommends
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',                   

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quanzi/admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^quanzi/inbo/$', 'quanzi.views.inbox'),
    url(r'^quanzi/login/$', 'quanzi.views.login'),
    url(r'^quanzi/register/$', 'quanzi.views.register'),
    url(r'^quanzi/index/$', 'quanzi.views.index'),
    url(r'^quanzi/haoyoudongtai/$', 'quanzi.views.haoyou'),
    url(r'^quanzi/wodedongtai/$', 'quanzi.views.myword'),
    url(r'^quanzi/news/$', 'quanzi.views.news'),
    url(r'^quanzi/friends/$', 'quanzi.views.show_followeds'),
    url(r'^quanzi/new_friend/$', 'quanzi.views.new_friend'),
    url(r'^quanzi/me/$', 'quanzi.views.me'),
    url(r'^quanzi/comment/(\d+)/', 'quanzi.views.comment'),
    url(r'^quanzi/logout/$', 'quanzi.views.logout'),
    url(r'^quanzi/search_friend/$', 'quanzi.views.search_friend'),
    url(r'^quanzi/insert_friends/$', 'quanzi.views.insert'),
  #  url(r'^quanzi/registeru/$', 'quanzi.views.register_user'),
    url(r'^test/$', 'quanzi.views.test'),
    url(r'^zan/$', 'quanzi.util.zan'),
    url(r'^ping/$', 'quanzi.util.ping'),
    url(r'^getcommends/$', 'quanzi.util.getcommends'),
    url(r'^quanzi/message_center/$', 'quanzi.views.message_center'),
)