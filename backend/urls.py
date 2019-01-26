#from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.home),
    url(r'^home', views.home),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^menu', views.menu),
    url(r'^upload_action', views.upload_action),
    url(r'^upload', views.upload_img),
    url(r'^about', views.about),
    url(r'^contact', views.contract),
    url(r'^gallery', views.gallery),
]