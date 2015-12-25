import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from quanzi.models import News

import time
import shutil
path='quanzi/static/news'
if(os.path.isdir(path)):
	shutil.rmtree('quanzi/static/news')
news=News.objects.all()
for i in news:
	i.delete()
from pachong import NEWs	
A=NEWs()
len=A.l
for i in range(0,len):
	B=News()
	B.number=A.Id[i]
	B.title=((A.title[i]).decode('gbk'))#.encode('utf-8')
	B.content=((A.news[i]).decode('gbk'))#.encode('utf-8')
	B.save()

