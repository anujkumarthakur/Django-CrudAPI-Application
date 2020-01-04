from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from .models import Post
from django.views.generic import ListView, DetailView

#Home view for posts. Poss are displayed in a list
class IndexView(ListView):
    template_name = 'crud/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.all()































