from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="blogHome"),
    path('blogpostrajat/<int:id>', views.blogpostrajat,name="blogPost"),
]