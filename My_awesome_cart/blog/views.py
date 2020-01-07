from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    myposts=Blogpost.objects.all()
    return render(request,"blog/index.html",{'myposts':myposts})

def blogpostrajat(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,"blog/blogpostrajat.html",{'post':post})    

