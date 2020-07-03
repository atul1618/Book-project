"""Book_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Vendor.views import *


urlpatterns = [
    path('',getHome,name='home'),
    path('bookcreate',createBook,name="createbook"),
    path('categorycreate',createcategory,name='createcategory'),
    path('authorreg',createauthor,name='authorreg'),
    path('listbooks',listBooks,name='listbooks'),
    path('viewbooks/<int:pk>',bookView,name='bookview'),
    path('listauthor',listAuthor,name='listauthor'),
    path('viewauthor/<int:pk>',viewAuthor,name='viewauthor'),
    path('deleteauthor/<int:pk>',deleteauthor,name='del_author'),
    path('listcategory',listCategory,name='listcategory'),
    path('viewcategory/<int:pk>',viewCategory,name='viewcategory'),
    path('delecategory/<int:pk>',delCategory,name='del_category'),
    path('deletebook/<int:pk>',delBook,name='del_book'),
    path('updatebook/<int:pk>',updateBook,name='update_book'),
    path('updateauthor/<int:pk>',updateAuthor,name='update_author'),
    path('updatecategory/<int:pk>',updateCategory,name='update_category'),
    path('searchbooks',searchBooks,name='searchbook'),
]
