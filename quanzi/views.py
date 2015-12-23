# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response , RequestContext
from django.template import Template, Context
from  django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import json
from util import setJsonGuanZhu
from django.views.decorators.csrf import csrf_protect
from quanzi_forms import RegisterForm
from quanzi.models import *
from PIL import Image
import random
# Create your views here.

def inbox(request):
    return render_to_response('index.html')
def index(request):
   # return render_to_response('index.html', {})
    try:
        
        useremail = request.COOKIES.get('useremail')
        username = User.objects.get(email = useremail).name
        t = get_template('index.html')
        html = t.render(Context({'username':username}))
        return HttpResponse(html)
    except:
        return HttpResponseRedirect('/quanzi/login/')
    
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
            user[0].save()
            return response

        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(req))
    else:
        #登录
        t = get_template('login.html')
        html = t.render(Context({}))
        return HttpResponse(html)
def logout(request):
    response = HttpResponseRedirect('/quanzi/login/')
    response.delete_cookie('useremail')
    return response 
def haoyou(request):
    #try:
    useremail = request.COOKIES.get('useremail')
    username = User.objects.get(email = useremail).name
    if request.method=="POST" :
        new_share = Share()
        new_share.host = User.objects.get(email=useremail)
        new_share.content = request.POST['new_dongtai']
        new_share.praise_count = 0
        new_share.save()
       
    
    follows=Followship.objects.filter(fans__email=useremail)
    friends=[]
    for follow in follows:
        
        friend=follow.followed
        friends.append(friend)
    fri_num=len(friends)
    fri1_num=len(Followship.objects.filter(followed__email=useremail))
    friends.append(User.objects.get(email=useremail))
    dongtais = []
    for friend in friends:
        
        shares = Share.objects.filter(host__email = friend.email)
        for share in shares:
            dic = {}
            dic['name'] = share.host.name
            dic['email'] = str(share.host.email)
            dic['dong'] = share
            dongtais.append(dic)
    users=User.objects.all()
    user_list = []
    for user in users:
        if user.email != useremail:
           user_list.append(user)
    number=len(user_list)
    #return HttpResponse(len(user_list))
    people = []
    if number <= 3:
        people = user_list
    else:
        a=random.randrange(number)
        people.append(user_list[a])
        del user_list[a]
        a=random.randrange(number-1)
        people.append(user_list[a])
        del user_list[a]
        a=random.randrange(number-2)
        people.append(user_list[a])
        del user_list[a]
    
    return render_to_response('haoyoudongtai2.html',{'dongtais':dongtais,'friends':fri_num,\
    'friendeds':fri1_num, 'peoples':user_list,'username':username })
        
#    except:
 #      return HttpResponseRedirect('/quanzi/login/')
def myword(request):
    try:
        useremail = request.COOKIES.get('useremail')
        username = User.objects.get(email = useremail).name
        if request.method=="POST" :
            new_share = Share()
            new_share.host = User.objects.get(email=useremail)
            new_share.content = request.POST['new_dongtai']
            new_share.praise_count = 0
            new_share.save()
        follows=Followship.objects.filter(fans__email=useremail)
        friends=[]
        for follow in follows:
            
            friend=follow.followed
            friends.append(friend)
        fri_num=len(friends)
        fri1_num=len(Followship.objects.filter(followed__email=useremail))
        
        dongtais=[]  
        shares = Share.objects.filter(host__email = useremail).order_by("-datetime")
        for share in shares:
            dic = {}
            dic['name'] = share.host.name
            dic['email'] = share.host.email
            dic['dong'] = share
            dongtais.append(dic)
        users=User.objects.all()
        user_list = []
        for user in users:
            if user.email != useremail:
               user_list.append(user)
        number=len(user_list)
        people = []
        if number <= 3:
            people = user_list
        else:
            a=random.randrange(number)
            people.append(user_list[a])
            del user_list[a]
            a=random.randrange(number-1)
            people.append(user_list[a])
            del user_list[a]
            a=random.randrange(number-2)
            people.append(user_list[a])
            del user_list[a]
        return render_to_response('wodedongtai.html',{'dongtais':dongtais,'friends':fri_num,\
        'friendeds':fri1_num,'peoples':user_list, 'username':username})
    except:
       return HttpResponseRedirect('/quanzi/login/')
def news(request):
    try:
        useremail= request.COOKIES['useremail']
        username = User.objects.get(email = useremail).name
        news=News.objects.all()
        twonews=[]
        length=len(news)
        l=length/2
        for i in range(l):
            twonew=[news[2*i],news[2*i+1]]
            twonews.append(twonew)
        if length%2 ==1:
            two=[news[length-1]]
            twonews.append(two)
        return render_to_response('news.html',{'twonews':twonews, 'username':username})
    except:
        return HttpResponseRedirect('/quanzi/login/')
def new_friend(request):
    try:
        useremail= request.COOKIES['useremail']
        username = User.objects.get(email = useremail).name
        return render_to_response('new_friend1.html',{'username':username})
    except:
        return HttpResponseRedirect('/quanzi/login/')
def me(request):
    try:
        useremail= request.COOKIES['useremail']
        user = User.objects.get(email = useremail)
        return render_to_response('me.html',{'username':user.name,'me':user})
    
    except:
        return HttpResponseRedirect('/quanzi/login/')
def show_followeds(request):
    try:
        useremail = request.COOKIES['useremail']
        user = User.objects.get(email=useremail)
        followships = Followship.objects.filter(fans=user)
        friends = []
        for followship in followships:
            friends.append(followship.followed)
        t = get_template('friends1.html')
        
        html = t.render(Context({'friends':friends, 'user':user,'username':user.name}))
        return HttpResponse(html)
    except:
        return HttpResponseRedirect('/quanzi/login/')
def comment(request,number):
    try:
        useremail = request.COOKIES.get('useremail')
        new=News.objects.get(number=number)
        if request.method=="POST" :
            new_talk=Talk()
            new_talk.auth= User.objects.get(email=useremail)
            new_talk.news_id=News.objects.get(number=number)
            #return HttpResponse(new_talk.new_id)
            new_talk.content=request.POST['new_dongtai']
            new_talk.save()
        talks=[]
        talks1=Talk.objects.filter(news_id__number=number).order_by("-datetime")
        length=1
        for talk2 in talks1:
            ta={}
            ta['talk1']=talk2
            name=talk2.auth.name
            ta['number']=length
            ta['name']=name
            length=length+1
            talks.append(ta)
        return render_to_response('comment.html',{'news':new,'talks':talks,'title':number})
    except:
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)

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
        reqfile = req.FILES['pic']#picfile要和html里面一致
        img = Image.open(reqfile)
        img.thumbnail((500,500),Image.ANTIALIAS)#对图片进行等比缩放
        img.save('.\quanzi\static\head_images\\'+str(new_user.email)+".png","png")#保存图片 
        if (len(User.objects.filter(email=new_user.email)) <= 0):
            new_user.save()
            return HttpResponseRedirect('/quanzi/login/')
        else:
            t = get_template('register4.html')
            html = t.render(Context({}))
            return HttpResponse(html)        
     else:
        #t = get_template('register.html')
        t = get_template('register4.html')
        html = t.render(Context({}))
        return HttpResponse(html)
def search_friend(req):
    try:
        useremail = req.COOKIES.get('useremail')
        if req.method=='POST':
            name=req.POST['ne']
            users=User.objects.filter(name=name)
            return render_to_response('find_friends.html',{'friends':users})
    except:
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)
def insert(req):
    try:
        email=req.GET["id"]
        user=User.objects.get(email=email)
        useremail = req.COOKIES.get('useremail')
        me=User.objects.get(email=useremail)
        follow=Followship()
        follow.fans=me
        follow.followed=user
        setJsonGuanZhu(user, me)
        follow.save()
        response = HttpResponseRedirect('/quanzi/friends/')
        return response
    except:        
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)
def test(req):
    return render_to_response('test.html',{})

def message_center(req):
    #try:
    useremail = req.COOKIES.get('useremail')
    path = "quanzi\static\messages\\"
    fp = open(path+useremail+'.json', 'r')
    #messages = json.load(fp)
    messages = json.loads(fp.read())
    fp.close()
    message_list = []
    if messages.has_key('zan'):
        zans = messages['zan']
        for zan in zans:
            praiserName =User.objects.get(email=zan['praiserEmail']).name
            content =Share.objects.get(id=zan['shareId']).content
            time = zan['dateTime']
            content = content.encode("utf-8") 
            praiserName = praiserName.encode("utf-8")
            message_list.append({'time':time, 'txt':praiserName+'赞了你的动态：'+content})
    if messages.has_key('ping'):
        pings = messages['ping']
        for ping in pings:
            pingerName =User.objects.get(email=ping['pingerEmail']).name
            content =Share.objects.get(id=ping['shareId']).content
            time = ping['dateTime']
           
            content = content.encode("utf-8") 
            pingerName = pingerName.encode("utf-8")
            ping_text = ping['ping_text'].encode("utf-8")
            message_list.append({'time':time, 'txt':pingerName+'评论了你的动态：'+content+'"'+ping_text+'"'})
    if messages.has_key('guanzhu'):
        guanzhus = messages['guanzhu']
        for guanzhu in guanzhus:
            fansName =User.objects.get(email=guanzhu['fansEmail']).name
            time = guanzhu['dateTime']
          
            fansName = fansName.encode("utf-8")
            message_list.append({'time':time, 'txt':fansName+'关注了你'})
    
    
    message_list = sorted(message_list, key=lambda x:x['time'], reverse=True)
    #fp = open(path+useremail+'.json', 'w')
    #fp.close()
    return render_to_response('message_center.html', Context({'message_list':message_list, "len":len(message_list)}))
    ##except:
   #     return HttpResponse('没有消息')