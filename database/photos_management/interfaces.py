# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, django
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PhotoClassify.settings")
django.setup()

#照片信息管理模块


from backend.models import *


#接口1：增加照片 输入：账户id，照片文件名，照片分类
#返回内容包括：注册操作信息状态码，注册操作信息内容，账户id
def photoAdd(userID, photoName, phoType):
    select_result = Photo.objects.filter(photo_account_id=userID, photo_type=phoType)
    userID_rt = ''
    content_rt = ''
    if select_result:
        #已创建该用户对该图片类别的记录，直接在photo后增加新加入的图片名字
        the_model = select_result[0]
        the_model.photo_photo += photoName
        the_model.save()
        status = True
        content_rt = 'photo add successfully!'
        userID_rt = userID
    else:
        #注册网页成功
        the_model = Photo(photo_account_id=userID, photo_type=phoType, photo_photo=photoName)
        the_model.save()
        status = True
        content_rt = "photo register success!"
        userID_rt = userID

    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict

#接口2：向网页增加控件  输入：网页id，控件内容，账户id
#返回内容包括：增加操作信息状态码，增加操作信息内容，网页id
def insertWedget(pageID, pageContent, userID):
    select_result = Photo.objects.filter(webPage_pageid=pageID)
    userID_rt = ''
    content_rt = ''
    if not select_result:
        #网页不存在
        content_rt = "Page doesn't exist!"
        status = False
    elif(select_result[0].webPage_account_id != userID):
        #网页所对应传过来的账户id不一致
        content_rt = "Page and account doesn't match!"
        status = False
    else:
        #添加成功
        the_model = select_result[0]
        the_model.webPage_widget = pageContent
        the_model.save()
        content_rt = "insert successfully!"
        status = True
        userID_rt = userID

    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict

#接口3：查询网页控件  输入：网页id，账户id
#返回内容包括：查询操作信息状态码，查询操作信息内容，网页id
def queryWedget(pageID, userID):
    select_result = Photo.objects.filter(webPage_pageid=pageID)
    status = False
    content_rt = ''
    userID_rt = ''
    if not select_result:
        # 网页不存在
        content_rt = "Page doesn't exist!"
    elif (select_result[0].webPage_account_id != userID):
        # 网页所对应传过来的账户id不一致
        content_rt = "Page and account doesn't match!"
    else:
        # 查询成功
        status = True
        userID_rt = userID
        content_rt = select_result[0].webPage_widget  #查询成功返回控件内容
        print(content_rt)

    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict

#接口4：查询账户已拥有网页列表 输入：账户id
#返回内容包括：查询操作信息状态码，查询操作信息内容，账户id
def queryPage(userID):
    select_result = Photo.objects.filter(webPage_account_id=userID)
    status = False
    content_rt = ''
    userID_rt = ''
    if not select_result:
        # 网页不存在
        content_rt = "You have no page!"
    else:
        # 查询成功
        status = True
        userID_rt = userID
        content_rt = select_result  # 查询成功返回控件内容

    result_dict = {
        'status': status,
        'content': content_rt,
        'userID': userID_rt,
    }
    return result_dict


def demo(userID):
    select_result = Photo.objects.filter(webPage_account_id=userID)
    if not select_result:
        the_model = Photo(webPage_account_id=userID, webPage_pageid='001')
        the_model.save()
