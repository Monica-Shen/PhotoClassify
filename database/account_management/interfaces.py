# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PhotoClassify.settings")
django.setup()

# 账户信息管理模块


from backend.models import *


# 接口1：登录 输入：用户名，密码
# 返回内容包括：登录操作信息状态码，登录操作信息内容，用户名，职位
def login(userID, password):
    #在数据库中找出userID匹配项
    select_result = Account.objects.filter(account_id=userID)
    #获取登录状态
    userID_rt = ''
    content_rt = ''
    if not select_result:
        # id不存在
        content_rt = "id doesn't exist!"
        status = False
    elif(select_result[0].account_pass != password):
        # 密码错误
        content_rt = "wrong password!"
        status = False
    else:
        # 登录成功
        status = True
        content_rt = 'success!'
        userID_rt = userID
    #构造返回的字典
    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict

# 接口2：注册 输入：用户名，密码，姓名，邮箱
# 返回内容包括：注册操作信息状态码，注册操作信息内容，用户名
def register(userID, password, email):
    # 在数据库中寻找ID是否重复
    select_result = Account.objects.filter(account_id=userID)
    userID_rt = ''
    content_rt = ''
    if select_result:
        #id已存在
        status = False
        content_rt = 'ID existed!'
    else:
        #注册成功
        the_model = Account(account_id=userID, account_pass=password, account_email=email)
        the_model.save()
        status = True
        content_rt = "register success!"
        userID_rt = userID

    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict

