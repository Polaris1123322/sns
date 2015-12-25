#coding=utf-8
import urllib
import re
import os
import time
class NEWs:
    def getHtml(url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
    
    def gettitle(html):
          reg='/phb/0.htm([\w\W]*)recommend'
          total=re.compile(reg)
          find=total.search(html)
          str1= find.group()
          reg_2=r'title=\'(.+?)\''
          reg_3=re.compile(reg_2)
          reg_4='href=\'(.+?)\''
          reg_5=re.compile(reg_4)
          total_2=re.findall(reg_3,str1)
          total_3=re.findall(reg_5,str1)
          l=len(total_2)
          list=[]
          for i in range(0,l):
              str2="http://today.hit.edu.cn"+str(total_3[i])
              list.append(str(total_2[i]))
              list.append(str2)
          return list
    def getnews(html,hao):
        reg1='<div id="page_main">[\w\W]*<div id="page_share">'
        pat1=re.compile(reg1)
        res1=pat1.search(html)
        news=res1.group()
        # reg2='<.+?>'
        # pat2=re.compile(reg2)
        # k=re.sub(pat2,'',news)
        k=news
        reg3=r'height.+? src="(.+?\g)" /'
        pat3=re.compile(reg3)
        res3=pat3.findall(html)
        reg4='^http'
        pat4=re.compile(reg4)
        x=0
        time0=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        name='quanzi\static\\news'
        if(os.path.isdir(name)==False):
            os.mkdir(name) 
        PATH=name+'\\'+str(hao)+'_'+time0
        if(os.path.isdir(PATH)==False):
            os.mkdir(PATH)
        for i in res3:
            rst4=re.match(pat4,i)
            if(rst4):
                j=i
            else:
                j='http://today.hit.edu.cn'+i
            path=PATH+'\\'+str(x)+'.jpg'
            if(os.path.isfile(path)==False):
                urllib.urlretrieve(j,path)
            k=k.replace(i,'/static/news/'+str(hao)+'_'+time0+'/'+str(x)+'.jpg')
            x+=1
        reg5='<iframe[\w\W]*</iframe>'
        pat5=re.compile(reg5)
        k=re.sub(pat5,'',k)
        reg6='<a href=.+?>'
        pat6=re.compile(reg6)
        k=re.sub(pat6,'',k)
        pat7=re.compile('<\a>')
        k=re.sub(pat7,'',k)
        return k
    
    html_1 = getHtml('http://today.hit.edu.cn/')
    list=gettitle(html_1)
    title=[]
    url=[]
    html=[]
    news=[]
    Id=[]
    reg0='RL0'
    pat0=re.compile(reg0)
    reg1='-\d\d/(.+?)RL'
    pat1=re.compile(reg1)
    for i in range(0,len(list)):
        if(i%2==0):
            title.append(list[i])
        else:
            url.append(list[i])
    
    for i in url :
        res0=re.search(pat0,i)
        if(res0):
            html.append(getHtml(i))
            res1=re.findall(pat1,i)
            for j in res1:
                Id.append(j)
    l=len(html)
    for i in range(0,l):
        news.append(getnews(html[i],Id[i]))
