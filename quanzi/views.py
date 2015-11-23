# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response , RequestContext
from django.template import Template, Context
from  django.http import HttpResponse
from django.template.loader import get_template

from django.views.decorators.csrf import csrf_protect
from quanzi_forms import RegisterForm
from models import User
# Create your views here.
def index(request):
   # return render_to_response('index.html', {})
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)
    
def login(req):
    if req.method == 'POST':
        #登录验证跳转
        loginer = req.GET
        email = loginer.email
        pw = loginer.pw
        user = User.objects.filter(email)
        if(len(user) == 1 and user.pw ==pw):
            return render_to_response('index.html', user)
        else:
            return render_to_response('login.html', {})
    else:
        #登录
        t = get_template('login.html')
        html = t.render(Context({}))
        return HttpResponse(html)
    
@csrf_protect 
def register(req):
    #注册认证  
    if req.method=='POST':
       
        rf = RegisterForm(req.GET)
        user = User()
        user.email = rf.cleaned_data['user_email']
        user.name = rf.cleaned_data['user_name']
        user.pw = rf.cleaned_data['user_password']
        user.birthday = rf.cleaned_data['user_birthday']
        user.school = rf.cleaned_data['user_school']
        user.is_boy = rf.cleaned_data['user_gender']
        user.save()
        return HttpResponse('hello')
        
    else:
        #t = get_template('register.html')
        rf = RegisterForm()
        return render_to_response('register.html', rf, context_instance=RequestContext(req))
      