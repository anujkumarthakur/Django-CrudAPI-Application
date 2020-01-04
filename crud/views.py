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

#Detail view (view post detail)
class PostDetailView(DetailView):
    model = Post
    template_name = 'crud/post-detail.html'

#New Post view(create new post)
def postview(request):
    if request.method == 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'crud/post.html',{'form':form})
































