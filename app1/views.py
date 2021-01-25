import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


from app1.models import Post,Comment


def register(request):
    return render(request,"signup.html")
def signup(request):
    if request.method=='POST':
        mail = request.POST.get('email', '')
        username = request.POST.get('username', '')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')

        userCheck = User.objects.filter(username=username) | User.objects.filter(email=mail)

        if userCheck:
            messages.error(request, "already taken")
            return render(request, "signup.html")
        user_obj = User.objects.create_user(first_name = name, password = password, email = mail, username = username)
        user_obj.save()
    return render(request,"signup.html")

def user_login(request):
    if request.method=='POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user  = authenticate(username=user_name, password=user_password)


        if user is not None:
            login(request, user)
            messages.success(request, "logged in")
            return redirect('/')
        else:
            messages.error(request, "no user exist with those credetials")
            return render(request,"signup.html")


def userpage(request):
    try:
      posts = Post.objects.filter(user_id=request.user).order_by('-pk')
      c = request.user.id
      p1 = Post.objects.filter(user_id=c).count()
      l1 = sum([i.likes.count() for i in posts])
      d1 = sum([i.dislikes.count() for i in posts])
      return render(request,"userpage.html",{"p1":p1,"data":posts,"l1":l1,"d1":d1})
    except TypeError:
      return redirect("/signup")

def user_logout(request):
    logout(request)
    messages.success(request, "logged out")
    return redirect("/")


def homepage(request):
    posts =Post.objects.all().order_by('-pk')
    data = {
          'posts': posts
    }
    return render(request, "homepage.html", data)



def post(request):
    try:
        title_ = request.POST.get('title','')
        content_ = request.POST.get('content','')
        user_ = request.user
        post_obj = Post(user=user_, caption=title_, content=content_)
        post_obj.save()
        messages.success(request, "Posted Successfully ")
        return redirect('/')
    except ValueError:
        return render(request,"signup.html")


def delPost(request, ID):
    post_ = Post.objects.filter(pk=ID)
    post_.delete()
    messages.info(request, "Post Deleted")
    return redirect('/')

def likePost(request):
    post = get_object_or_404(Post,id=request.GET.get('post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect('/')

def dislikePost(request):
    post = get_object_or_404(Post, id=request.GET.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect('/')

def comment(request):
    comment_ = request.POST.get("reply")
    postid = request.POST.get("cmntid")
    Comment(comment=comment_,user=request.user,post_id=postid).save()

    return redirect("/")


def usercmnt(request):
    p_id = request.POST.get("p_id", default=None)
    cmnt = Comment.objects.filter(post_id=p_id)
    pst = Post.objects.get(id=p_id)
    return render(request,"usercmnt.html",{"cmnt":cmnt,"pst":pst})