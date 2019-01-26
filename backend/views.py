# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from database.account_management import interfaces as accm
from database.photos_management import interfaces as phom
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext, loader

import os
import json
from photoRec import photo_classify as phocla

# def index(request):
# return render(request, 'server/login.html')
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def upload_img(request):
    print('Enter Upload Image Page!')
    return render(request,'upload_img.html')


@csrf_protect
def upload_action(request):
    # request.Get
    # if request.method == "GET":
    #     return render(request, 'upload_img.html')
    if request.method == "POST":
        img = request.FILES.get('img')
        # username = request.POST.get('username')
        # imgdir = open('../image/'+img.name,'wb+')
        # for chunk in img.chunks():
        #     imgdir.write(chunk)
        # imgdir.close()
        result = phocla.photo_classify('', img)
        if not result['success']:
            return HttpResponse("failure!")
        imgdir = result['path']
        type = result['type']
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        s = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        print(s)
        return render(request, 'upload_action.html', {'img_path':'../'+ img.name, 'class_result':type})
        #写入数据库
        # result = phom.photoAdd('', img.name, type)
        # if result['status']:
        #     return HttpResponse("success!")
        # else:
        #     return HttpResponse("failure!")
        return HttpResponse(type)
    # ---------------------------------------------------------------------
    # print("upload_action..")
    # img = request.FILES.get('img')
    # print(img.name)
    # print("xxxxxxxx")
    # path = BASE_DIR.replace("\\","/")+'/backend/static/'+img.name
    # dest = open(path,'wb+')
    # for chunk in img.chunks():
    #     dest.write(chunk)
    # dest.close()
    # class_result = infer_pack();
    # return HttpResponse(class_result)
    #return render(request, 'upload_action.html', {'img_path': path,'class_result':class_result})
    # ----------------------------------------------------------------------------

def infer_pack():
    return 'cat';



def home(request):
    print("home..")
    # request.Post
    # request.Get
    return render(request, 'home.html')

#账户登陆
@csrf_exempt #增加装饰器，作用是跳过 csrf 中间件的保护
def login(request):
    # request.Get
    if request.method== 'GET':
        return render(request, 'login.html')
    # request.Post
    if request.method=='POST':
        result = accm.login(request.POST.get('username'),request.POST.get('password'))
        if result['status']:
            response = HttpResponseRedirect('home.html')
            response.set_cookie('user_id', request.POST.get('username'))
            return HttpResponse(result['content'])
        else:
            return HttpResponse(result['content'])


#账户注册  输入：用户名 密码 二次密码 email  输出：是否创建成功
@csrf_exempt
def register(request):
    print("register")
    # request.Get
    if request.method=="GET":
        return render(request, 'register.html')
    # request.Post
    if request.method=="POST":

        print(request.POST.get('re_username'))
        user_id = request.POST.get('re_username')
        password = request.POST.get('re_password')
        pass_again = request.POST.get('re_passwordagain')
        email = request.POST.get('re_email')
        if(password != pass_again):
            # return ("hllllllll1111222")
            return HttpResponse("password doesn't match!")

        else:
            result = accm.register(user_id, password, email)
            if result['status']:
                return HttpResponse(result['content'])
            else:
                return HttpResponse(result['content'])


def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request,'about.html')

def contract(request):
    return render(request, 'contact.html')

def gallery(request):
    return  render(request,'gallery.html')




