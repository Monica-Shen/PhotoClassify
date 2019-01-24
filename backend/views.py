# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from database.account_management import interfaces as accm
from database.photos_management import interfaces as phom
from django.views.decorators.csrf import csrf_exempt


# def index(request):
#     return render(request, 'server/login.html')
# Create your views here.


def home(request):
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
            response = HttpResponseRedirect('menu.html')
            response.set_cookie('user_id', request.POST.get('username'))
            return HttpResponse(result['content'])
        else:
            return HttpResponse(result['content'])


#账户注册  输入：用户名 密码 二次密码 email  输出：是否创建成功
def register(request):
    # request.Get
    if request.method=="GET":
        return render(request, 'register.html')
    # request.Post
    if request.method=="POST":
        user_id = request.POST.get('re_username')
        password = request.POST.get('re_password')
        pass_again = request.POST.get('re_passwordagain')
        email = request.POST.get('re_email')
        if(password != pass_again):
            return HttpResponse("password doesn't match!")
        else:
            result = accm.register(user_id, password, email)
            if result['status']:
                return HttpResponse(result['content'])
            else:
                return HttpResponse(False)


def menu(request):
    return render(request, 'menu.html')




