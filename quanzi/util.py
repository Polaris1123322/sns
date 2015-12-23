
# -*- coding: utf-8 -*-

from  django.http import HttpResponse, HttpResponseRedirect
from  models import Praise, User, Share, Commend
from django.template import Template, Context
from django.template.loader import get_template
import time
import json
ISOTIMEFORMAT='%Y-%m-%d %X'
def zan(req):
    useremail = req.COOKIES.get('useremail')
    share_id = req.GET['share']
	#c = int(a)+int(b)
    user = User.objects.get(email=useremail)
    share = Share.objects.get(id=share_id)
    if len(Praise.objects.filter(praiser=user,praised=share_id)) == 0:
        praise = Praise()
        praise.praiser = user
        praise.praised = share
        setJsonZan(user, share)
        praise.save()
        count = share.praise_count+1
        share.praise_count = count
        share.save()
        #setJsonZan(user, share)
        return HttpResponse(str(count))
    return HttpResponse(str(share.praise_count))

def ping(req):
    useremail = req.COOKIES.get('useremail')
    share_id = req.GET['share_id']
    ping_text = req.GET['ping']
    user = User.objects.get(email=useremail)
    share = Share.objects.get(id=share_id)
    commend = Commend()
    commend.Commender = user
    commend.content = ping_text
    commend.share_id = share
    setJsonPing(user, share, ping_text)
    commend.save()
    commends = Commend.objects.filter(share_id = share)
    t = get_template('commends.html')
    html = t.render(Context({'commends':commends}))
    return HttpResponse(html)

def getcommends(req):
     share_id = req.GET['share']
     share = Share.objects.get(id=share_id)
     commends = Commend.objects.filter(share_id = share)
     t = get_template('commends.html')
     html = t.render(Context({'commends':commends}))
     return HttpResponse(html)
     

def setJsonZan(user, share):
    userEmail = user.email
    myEmail = share.host.email
    myShareId = share.id
    current_time = time.strftime( ISOTIMEFORMAT, time.localtime() )
    newItem = {'praiserEmail':str(userEmail), 'shareId':str(myShareId), 'dateTime':str(current_time)}
    path = "quanzi\static\messages\\"
    fileName = path+ myEmail+'.json'
    try:
        fp = open(fileName, 'r')
        message = json.load(fp)
    except:
        fp = open(fileName, 'w')
        message = {}
    fp.close()
    if(message.has_key('zan')):
        message['zan'].append(newItem)
    else:
        message['zan'] = [newItem]
    fp = open(fileName, 'w')
    json.dump(message, fp)
    fp.close()
    return
def setJsonPing(user, share, text):
    userEmail = user.email
    myEmail = share.host.email
    myShareId = share.id
    current_time = time.strftime( ISOTIMEFORMAT, time.localtime() )
    newItem = {'pingerEmail':str(userEmail), 'shareId':str(myShareId), 'dateTime':str(current_time), 'ping_text':text}
    path = "quanzi\static\messages\\"
    fileName = path+ myEmail+'.json'
    try:
        fp = open(fileName, 'r')
        message = json.load(fp)
    except:
        fp = open(fileName, 'w')
        message = {}
    fp.close()
    if(message.has_key('ping')):
        message['ping'].append(newItem)
    else:
        message['ping'] = [newItem]
    fp = open(fileName, 'w')
    json.dump(message, fp)
    fp.close()
    return
def setJsonGuanZhu(followed, fans):
    followedEmail = followed.email
    fansEmail = fans.email
    current_time = time.strftime( ISOTIMEFORMAT, time.localtime() )
    newItem = {'fansEmail':str(fansEmail), 'dateTime':str(current_time)}
    path = "quanzi\static\messages\\"
    fileName = path+ followedEmail+'.json'
    try:
        fp = open(fileName, 'r')
        message = json.load(fp)
    except:
        fp = open(fileName, 'w')
        message = {}
    fp.close()
    if(message.has_key('guanzhu')):
        message['guanzhu'].append(newItem)
    else:
        message['guanzhu'] = [newItem]
    fp = open(fileName, 'w')
    json.dump(message, fp)
    fp.close()
    return