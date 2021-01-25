"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('signup/',views.signup,name="signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('userpage/',views.userpage,name="userpage"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('',views.homepage,name="homepage"),
    path('post/',views.post,name="post"),
    path("delete/<int:ID>", views.delPost, name='deletepost'),
    path('like_post', views.likePost, name='like_post'),
    path('dislike_post', views.dislikePost, name='dislike_post'),
    path('comment', views.comment, name='comment'),
    path('usercmnt', views.usercmnt, name='usercmnt'),
]
