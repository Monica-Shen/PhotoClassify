#from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.home),
    url(r'^register', views.register),
    url(r'^home',views.home),
    url(r'^login',views.login),
    url(r'^menu',views.menu),
]