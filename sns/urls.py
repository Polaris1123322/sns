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
from mysite import settings
from quanzi.views import *
from quanzi.util import zan, ping, getcommends, sendMessage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',                   

    url(r'^admin/', include(admin.site.urls)),
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
    url(r'^quanzi/comment/', 'quanzi.views.comment'),
    url(r'^quanzi/logout/$', 'quanzi.views.logout'),
    url(r'^quanzi/search_friend/$', 'quanzi.views.search_friend'),
    url(r'^quanzi/insert_friends/$', 'quanzi.views.insert'),
    url(r'^quanzi/dongtai/$', 'quanzi.views.oneshare'),
    url(r'^quanzi/message/$', 'quanzi.views.message'),
    url(r'^quanzi/see_friend/$', 'quanzi.views.see_friend'),
    url(r'^quanzi/edit/$', 'quanzi.views.edit'),
    url(r'^quanzi/change_image/$', 'quanzi.views.change'),
    url(r'^quanzi/searchm/$','quanzi.views.searchm'),
    url(r'^quanzi/delete/$','quanzi.views.delfriend'),
    url(r'^quanzi/deldong/$','quanzi.views.deldong'),
    url(r'^quanzi/fans/$','quanzi.views.fans'),
    url(r'^quanzi/add_comment/$', 'quanzi.views.add_comment'),
    url(r'^quanzi/add_dong/$', 'quanzi.views.add_dong'),
    url(r'^quanzi/add_dong2/$', 'quanzi.views.add_dong2'),
    url(r'^quanzi/add_mes/$', 'quanzi.views.add_mes'),
    url(r'^quanzi/show/$', 'quanzi.views.show'),
    url(r'^quanzi/xiaoxi/$', 'quanzi.views.message_center'),
    url(r'^zan/$', 'quanzi.util.zan'),
    url(r'^ping/$', 'quanzi.util.ping'),
    url(r'^getcommends/$', 'quanzi.util.getcommends'),
    url(r'^send_message/$', 'quanzi.util.sendMessage'),
    url(r'^quanzi/del_xiao/$', 'quanzi.views.del_xiao'),
  #  url(r'^quanzi/registeru/$', 'quanzi.views.register_user'),

)