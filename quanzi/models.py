# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    email = models.EmailField() #邮箱地址，可变，登陆用,不可为空
    name = models.CharField(max_length=20) #用户名，可变，不可为空
    pw = models.CharField(max_length=30)#密码，可变，不可为空
    birthday = models.DateField(blank=True)#生日，可选项
    school = models.CharField(max_length=20)#学院，必填
    is_boy = models.BooleanField(blank=True)#性别
    last_login = models.DateTimeField(auto_now=True)#最后一次的登录时间
    hobby = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
class Commend(models.Model):
    #评论类，对于动态的评论
    share_id = models.ForeignKey('Share', related_name='share')#动态的id
    time = models.DateTimeField(auto_now = True)#评论的时间
    content = models.CharField(max_length=200, blank=False)#评论的内容
    Commender = models.ForeignKey('Commend', related_name='commender')#评论
   
class Followship(models.Model):
    #关注关系类
    fans = models.ForeignKey(User, blank=True, null=True, related_name='fans')#粉丝
    followed = models.ForeignKey(User, related_name='followed')#关注的人
    last_modified = models.DateTimeField(auto_now=True)#添加关注关系的时间
    def __unicode__(self):
        return u'%s 关注 %s'%(self.fans.name, self.followed.name)
class Share(models.Model):
    #动态类
    host = models.ForeignKey(User, related_name='host')#动态的分享者
    content = models.CharField(max_length=200, blank=False)#动态的内容
 #   praise = models.ManyToManyField(User, related_name='praise')
    praise_count = models.IntegerField(default = '0')#动态的赞数
    datetime = models.DateTimeField(auto_now = True)#动态的报道时间
    def __unicode__(self):
        return self.host.name

class News(models.Model):
    #新闻类
    title = models.CharField(max_length=50)#新闻的标题
    praise_count = models.IntegerField(default='0')#新闻的推荐书目
    number = models.IntegerField(blank=False, null=False)#新闻的编号
    content = models.CharField(max_length = 500)#新闻的内容（首段）
    datetime = models.DateTimeField()#新闻的报道时间
    padate = models.DateTimeField()#新闻的摘录时间

class Talk(models.Model):
    #讨论类
    news_id = models.ForeignKey(News, related_name='news')#新闻的id
    auth = models.ForeignKey(User, related_name='author')#帖子的作者
    content = models.CharField(max_length=140)#内容
    datetime= models.DateTimeField(auto_now = True)#时间
  

class Message(models.Model):
    #留言类
    fromer = models.ForeignKey(User, related_name='fromer')#留言者
    toer = models.ForeignKey(User, related_name='toer')#被留言者
    content = models.CharField(max_length=140)#内容
    datetime = models.DateField()#时间
    
    
 