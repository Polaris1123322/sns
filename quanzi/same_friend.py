# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:36:22 2015

@author: ANYOHAO
"""

from quanzi.models import *
def find_friends(user_list,useremail,friends):
    number=len(user_list)
    if number <= 5:
        renwu = user_list
    else:
        same_friends=[]
        for user in user_list:
            i=0
            follows=Followship.objects.filter(fans__email=useremail)
            for follow in follows:
                his_friend=follow.followed
                n=0
                for friend in friends:
                    if friend.email==his_friend.email:
                        n=1
                        break
                if n==1:
                   i+=1
        same_friends.append((user,i))
        sort=sorted(same_friends,key=lambda e:e[1],reverse=True)
        renwu=[]
        for i in range(len(sort)):
            renwu.append(sort[i][0])
    return renwu
