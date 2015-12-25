# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response , RequestContext
from django.template import Template, Context
from  django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import json
from util import setJsonGuanZhu, setJsonQuGuan
from django.views.decorators.csrf import csrf_protect
from quanzi_forms import RegisterForm
from same_friend import find_friends
from quanzi.models import *
from PIL import Image
import time
import datetime
# Create your views here.

def inbox(request):
    return render_to_response('index.html')
def index(request):
   # return render_to_response('index.html', {})
    try:
        
        useremail = request.COOKIES.get('useremail')
        username = User.objects.get(email = useremail).name
        t = get_template('index.html')
        renwu=fengyun()
        news=News.objects.all()
        html = t.render(Context({'username':username,'peoples':renwu,'news':news}))
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
    try:
        useremail = request.COOKIES.get('useremail')
        username = User.objects.get(email = useremail).name
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
            
            shares = Share.objects.filter(host__email = friend.email).order_by("-datetime")
            for share in shares:
                dic = {}
                dic['name'] = share.host.name
                dic['email'] = str(share.host.email)
                dic['dong'] = share
                dongtais.append(dic)
        
        users=User.objects.all()
        user_list = []
        for user in users:
            n=0
            for friend in friends:
                if friend.email== user.email:
                    n=1
                    break;
            if user.email != useremail and n==0:
               user_list.append(user)
        people=find_friends(user_list,useremail,friends)
        if(len(people)>5):
            people=people[0:5]    
        return render_to_response('haoyoudongtai2.html',{'dongtais':dongtais,'friends':fri_num,\
        'friendeds':fri1_num, 'peoples':people,'username':username })
        
    except:
       return HttpResponseRedirect('/quanzi/login/')
def add_dong2(request):
	try:
		useremail = request.COOKIES.get('useremail')
		username = User.objects.get(email = useremail).name
		if request.method=="POST" :
			new_share = Share()
			new_share.host = User.objects.get(email=useremail)
			new_share.content = request.POST['new_dongtai']
			new_share.praise_count = 0
			new_share.save()
			return HttpResponseRedirect('/quanzi/haoyoudongtai/')
	except:
		return HttpResponseRedirect('/quanzi/login/')
def myword(request):
    #try:
        useremail = request.COOKIES.get('useremail')
        username = User.objects.get(email = useremail).name
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
            n=0
            for friend in friends:
                if friend.email== user.email:
                    n=1
                    break;
            if user.email != useremail and n==0:
               user_list.append(user)
        people=find_friends(user_list,useremail,friends)
        if(len(people)>5):
            people=people[0:5]
        
        return render_to_response('wodedongtai.html',{'dongtais':dongtais,'friends':fri_num,\
        'friendeds':fri1_num,'peoples':people, 'username':username})
    #except:
        return HttpResponseRedirect('/quanzi/login/')
def add_dong(request):
	try:
		useremail = request.COOKIES.get('useremail')
		username = User.objects.get(email = useremail).name
		if request.method=="POST" :
			new_share = Share()
			new_share.host = User.objects.get(email=useremail)
			new_share.content = request.POST['new_dongtai']
			new_share.praise_count = 0
			new_share.save()
			return HttpResponseRedirect('/quanzi/wodedongtai/')
	except:
		return HttpResponseRedirect('/quanzi/login/')
def news(request):
    try:
        useremail= request.COOKIES['useremail']
        username = User.objects.get(email = useremail).name
        news=News.objects.all()
        return render_to_response('news.html',{'twonew':news, 'username':username})
    except:
        return HttpResponseRedirect('/quanzi/login/')
def fengyun():
	users=User.objects.all()
	list=[]
	for i in users:
		list.append((i,i.fansnum))
	sort=sorted(list,key=lambda e:e[1],reverse=True)
	renwu=[]
	if(len(sort)>5):
		for i in range(0,5):
			renwu.append(sort[i][0])
	else:
		for i in range(0,len(sort)):
			renwu.append(sort[i][0])
	return renwu
def new_friend(request):
    try:
        useremail= request.COOKIES['useremail']
        username = User.objects.get(email = useremail).name
        renwu=fengyun()
        follows=Followship.objects.filter(fans__email=useremail)
        friends=[]
        for follow in follows:
            
            friend=follow.followed
            friends.append(friend)
        users=User.objects.all()
        user_list = []
        for user in users:
            n=0
            for friend in friends:
                if friend.email== user.email:
                    n=1
                    break;
            if user.email != useremail and n==0:
               user_list.append(user)
        people=find_friends(user_list,useremail,friends)
        if(len(people)>5):
            people=people[0:5]
        return render_to_response('new_friend1.html',{'username':username,'fpeoples':renwu,'peoples':user_list})
    except:
        return HttpResponseRedirect('/quanzi/login/')
def me(request):
    try:
        
        useremail= request.COOKIES['useremail']
        user = User.objects.get(email = useremail)
        #return HttpResponse(user.is_boy)
        messages1=Message.objects.filter(toer__email= useremail).order_by("-datetime")
        messages=[]
        for mess in messages1:
            message={}
            message['name']=mess.fromer.name
            message['mes']=mess
            message['email']=mess.fromer.email
            messages.append(message)
        return render_to_response('me.html',{'username':user.name,'me':user,'messages':messages})
    
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
def comment(request):
    try:
        useremail = request.COOKIES.get('useremail')
        user = User.objects.get(email = useremail).name
        number=request.GET["id"]
        new=News.objects.get(number=number)
        talks=[]
        talks1=Talk.objects.filter(news_id__number=number).order_by("datetime")
        length=1
        for talk2 in talks1:
            ta={}
            ta['talk1']=talk2
            name=talk2.auth.name
            ta['number']=length
            ta['name']=name
            ta['email']=talk2.auth.email
            length=length+1
            talks.append(ta)
        
        return render_to_response('comment.html',{'news':new,'talks':talks,'username':user,'title':number})
    except:
        return HttpResponseRedirect('/quanzi/login/')
def add_comment(req):
    if req.method=="POST" :
        number=req.GET["id"]
        new=News.objects.get(number=number)
        useremail = req.COOKIES.get('useremail')
        user = User.objects.get(email = useremail)
        new_talk=Talk()
        new_talk.auth= user
        new_talk.news_id=new
        new_talk.content=req.POST['new_dongtai']
        new_talk.save()
        return HttpResponseRedirect('/quanzi/comment/?id='+number)

def register(req):
    #注册认证
    	
     if req.method=='POST':
        new_user = User()
        new_user.email = req.POST['email']
        new_user.name = req.POST['name']
        new_user.pw = req.POST['pass']
        new_user.birthday = req.POST['birthday']
        new_user.fansnum=0
        new_user.friendsnum=0
        if req.POST['gender']=='True':
            new_user.is_boy=True
        else:
            new_user.is_boy=False
        
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

def edit(req):
    useremail = req.COOKIES.get('useremail')
    user = User.objects.get(email = useremail)
    if req.method=='POST':
        
        if req.POST['name']:
            user.name = req.POST['name']
        if req.POST['pass']:
            user.pw = req.POST['pass']
        if req.POST['birthday']:
            user.birthday = req.POST['birthday']
        if req.POST['hobby']:
            user.hobby = req.POST['hobby']
        if req.POST['gender']==True:
            user.is_boy=True
        else:
            user.is_boy=False
        #return HttpResponse(req.POST['gender'])    
        if req.POST['school']:
            user.school = req.POST['school']
        user.save()
#        return HttpResponse( User.objects.get(email = useremail).is_boy) 
        return HttpResponseRedirect('/quanzi/me/')
    else:
        
        return render_to_response('edit.html',{'username':user.name,'user':user})
def change(req):
    useremail = req.COOKIES.get('useremail')
    user = User.objects.get(email = useremail)
    if req.method=='POST': 
        try:
            reqfile = req.FILES['pic']#picfile要和html里面一致
            img = Image.open(reqfile)
            img.thumbnail((500,500),Image.ANTIALIAS)#对图片进行等比缩放
            img.save('.\quanzi\static\head_images\\'+str(user.email)+".png","png")#保存图片 
            time.sleep(10)
            return HttpResponseRedirect('/quanzi/me/')
        except:
            return HttpResponseRedirect('/quanzi/me/')
    else:
        return render_to_response('change_image.html',{'username':user.name})
def show(req):
	email=req.GET['id']
	ta=User.objects.get(email=email)
	useremail=req.COOKIES.get('useremail')
	me=User.objects.get(email=useremail)
	if(Followship.objects.filter(followed=ta,fans=me)):
		is_friend=True
	else:
		is_friend=False
	if(ta==me):
		is_friend=True
	users2=[ta]
	return render_to_response('find_friends.html',{'friends':users2,'username':me.name,'is_friend':is_friend})
def search_friend(req):
	try:
		useremail = req.COOKIES.get('useremail')
		me=User.objects.get(email=useremail)
		follows=Followship.objects.filter(fans__email=useremail)
		friends=[]
		for follow in follows:
			friend=follow.followed
			friends.append(friend)
		if req.method=='POST':
			name=req.POST['ne']
			users=User.objects.filter(name=name)
			users2=[]
			for i in users:
				if((i not in friends)and i !=me):
					users2.append(i)
			return render_to_response('find_friends.html',{'friends':users2,'username':me.name})
	except:
		response = HttpResponseRedirect('/quanzi/login/')
		return HttpResponse(response)
def see_friend(req):
    try:
        useremail = req.COOKIES.get('useremail')
        email=req.GET["id"]
       
        users=User.objects.filter(email=email)
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
        follow.save()
        me.friendsnum=me.friendsnum+1
        user.fansnum+=1
        setJsonGuanZhu(user, me)
        me.save()
        user.save()
        response = HttpResponseRedirect('/quanzi/friends/')
        return response
    except:        
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)
    
def oneshare(req):
    try:
        email=req.GET["id"]
        useremail= req.COOKIES['useremail']
        username = User.objects.get(email = useremail).name
        shares = Share.objects.filter(host__email = email).order_by("-datetime")
        
    
        dongtais=[]
        for share in shares:
            dic = {}
            dic['name'] = share.host.name
            dic['email'] = share.host.email
            dic['dong'] = share
            dongtais.append(dic)
        #return HttpResponse(len(dongtais))
        return render_to_response('oneshare.html',{'dongtais':dongtais,'username':username})
    except:        
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)
def message(req):
    try:
        
        email=req.GET["id"]
        useremail= req.COOKIES['useremail']
        friend=User.objects.get(email = email)
        username = User.objects.get(email = useremail).name
        messages1=Message.objects.filter(toer__email= email).order_by("-datetime")
        if req.method=="POST" :
            new_message = Message()
            new_message.fromer = User.objects.get(email=useremail)
            new_message.toer = User.objects.get(email=email)
            new_message.content = req.POST['new_message']
            new_message.save()
        messages=[]
        for mess in messages1:
            message={}
            message['name']=mess.fromer.name
            message['mes']=mess
            message['email']=mess.fromer.email
            messages.append(message)
        return render_to_response('message.html',{'messages':messages,'username':username,'friend':friend})
    except:        
        response = HttpResponseRedirect('/quanzi/login/')
        return HttpResponse(response)
def add_mes(req):
	email=req.GET["id"]
	useremail= req.COOKIES['useremail']
	if req.method=="POST" :
		new_message = Message()
		new_message.fromer = User.objects.get(email=useremail)
		new_message.toer = User.objects.get(email=email)
		new_message.content = req.POST['new_message']
		new_message.save()
		return HttpResponseRedirect('/quanzi/message/?id='+email)
		
def searchm(req):
	#try:
		useremail= req.COOKIES.get('useremail')
		follows=Followship.objects.filter(fans__email=useremail)
		friends=[]
		for follow in follows:
			friend=follow.followed
			friends.append(friend)
		user=User.objects.get(email=useremail)
		if(req.POST['gender']=='True'):
			gender=True
		else:
			gender=False
		school=req.POST['school']
		time=req.POST['time']
		num=req.POST['num']
		low=int(req.POST['low'])
		high=int(req.POST['high'])
		now=datetime.datetime.now()
		day=datetime.date.today()
		list=[]
		time=time.encode('utf-8')
		if time=='一分钟前':
			a=60
		elif time=='一个小时前':
			a=3600
		elif time=='一天前':
			a=86400
		elif time=='三天前':
			a=259200
		elif time=='一周前':
			a=604800
		else:
			a=2592000
		for i in User.objects.all() :
			old=((day-i.birthday).days)/365
			b=(i.last_login).replace(tzinfo=None)
			cha=(now-b).seconds
			if(i.is_boy==gender and i.school==school and old>=low and old<=high and cha<=a and i!=user and (i not in friends)):
				list.append(i)
		if(num=='越多越好'):
			list=find_friends(list,useremail,friends)
		return render_to_response('find_friends.html',{'friends':list,'username':user.name})
	#except:
		return HttpResponseRedirect('/quanzi/login/')
def delfriend(req):
	try:
		
		email=req.GET["id"]
		useremail= req.COOKIES['useremail']
		friend=User.objects.get(email = email)
		me=User.objects.get(email = useremail)
		ship=Followship.objects.filter(fans=me,followed=friend)
		ship.delete()
		me.friendsnum=me.friendsnum-1
		friend.fansnum=friend.fansnum-1
		setJsonQuGuan(friend, me)
		me.save()
		friend.save()
		return HttpResponseRedirect('/quanzi/friends/')
	except:        
		response = HttpResponseRedirect('/quanzi/login/')
		return HttpResponse(response)
def deldong(req):
	try:
		id=req.GET["id"]
		useremail= req.COOKIES['useremail']
		user=User.objects.get(email=useremail)
		dong=Share.objects.get(id=id)
		for i in Commend.objects.filter(share_id=dong):
			i.delete()
		dong.delete()
		return HttpResponseRedirect('/quanzi/wodedongtai/')
	except:        
		response = HttpResponseRedirect('/quanzi/login/')
		return HttpResponse(response)
def del_xiao(req):
	try:
		useremail= req.COOKIES['useremail']
		path = "quanzi\static\messages\\"
		fp = open(path+useremail+'.json', 'w')
		fp.write('')
		fp.close()
		return HttpResponseRedirect('/quanzi/xiaoxi/')
	except:        
		response = HttpResponseRedirect('/quanzi/login/')
		return HttpResponse(response)
def fans(request):
	try:
		useremail = request.COOKIES['useremail']
		user = User.objects.get(email=useremail)
		followships = Followship.objects.filter(followed=user)
		friends = []
		for followship in followships:
			friends.append(followship.fans)
		t = get_template('fans.html')
		
		html = t.render(Context({'friends':friends, 'user':user,'username':user.name}))
		return HttpResponse(html)
	except:
		return HttpResponseRedirect('/quanzi/login/')
def message_center(req):
	try:
		useremail = req.COOKIES.get('useremail')
		username=User.objects.get(email=useremail).name
		try:
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
					message_list.append({'time':time, 'txt':pingerName+'评论了你的动态：'+content+'    评论内容"'+ping_text+'"'})
			if messages.has_key('guanzhu'):
				guanzhus = messages['guanzhu']
				for guanzhu in guanzhus:
					fansName =User.objects.get(email=guanzhu['fansEmail']).name
					time = guanzhu['dateTime']
				  
					fansName = fansName.encode("utf-8")
					message_list.append({'time':time, 'txt':fansName+'关注了你'})
			if messages.has_key('quguan'):
				guanzhus = messages['quguan']
				for guanzhu in guanzhus:
					fansName =User.objects.get(email=guanzhu['fansEmail']).name
					time = guanzhu['dateTime']
				  
					fansName = fansName.encode("utf-8")
					message_list.append({'time':time, 'txt':fansName+'取消关注了你'})
			
			
			message_list = sorted(message_list, key=lambda x:x['time'], reverse=True)
			#fp = open(path+useremail+'.json', 'w')
			#fp.close()
			return render_to_response('xiaoxi.html', Context({'xiaoxis':message_list,'username':username}))
			##except:
		   #     return HttpResponse('没有消息')
		except :
			message_list=[]
			return render_to_response('xiaoxi.html', Context({'xiaoxis':message_list,'username':username}))
	except:
		return HttpResponseRedirect('/quanzi/login/')		