from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import Q

class ListNews(ListView):
    model = Post
    ordering = 'post_title'
    template_name = 'news_test.html'
    context_object_name = 'news_list'
   
    queryset = Post.objects.filter(post_type='NW').order_by('-id')

class DetailNews(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news'
    
