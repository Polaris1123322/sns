# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response , RequestContext
from django.template import Template, Context
from  django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from django.views.decorators.csrf import csrf_protect
from quanzi_forms import RegisterForm
from models import User
# Create your views here.
def index(request):
   # return render_to_response('index.html', {})
    useremail = request.COOKIES.get('useremail', '')
    t = get_template('index.html')
    html = t.render(Context({'useremail':useremail}))
    return HttpResponse(html)
    
def login(req):
    if req.method == 'POST':
        #登录验证跳转
        #loginer = req.GET
        e_mail = req.POST['email']
        pw = req.POST['password']
        user = User.objects.filter(email=e_mail)
        if(len(user) == 1 and user[0].pw == pw):
            response = HttpResponseRedirect('/quanzi/index/')
            response.set_cookie('useremail',user[0].email,3600)
            return response

        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(req))
    else:
        #登录
        t = get_template('login.html')
        html = t.render(Context({}))
        return HttpResponse(html)
    
def register(req):
    #注册认证  
    if req.method=='POST':
        new_user = User()
        new_user.email = req.POST['email']
        new_user.name = req.POST['name']
        new_user.pw = req.POST['pass']
        new_user.birthday = req.POST['birthday']
        new_user.is_boy = bool(req.POST['gender'])
        new_user.school = req.POST['school']
        
        if (len(User.objects.filter(email=new_user.email)) <= 0):
            new_user.save()
            return HttpResponseRedirect('/quanzi/login/')
        else:
            t = get_template('register1.html')
            html = t.render(Context({}))
            return HttpResponse(html)
            
    else:
        #t = get_template('register.html')
        t = get_template('register1.html')
        html = t.render(Context({}))
        return HttpResponse(html)
        
def logout(request):
    response = HttpResponse('logout!')
    response.delete_cookie('useremail')
    return response 