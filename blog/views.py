from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def adopt(request, pk):
    context = {
        'posts': Post.objects.all()
    }
    post = Post.objects.get(id=pk)
    post.condition = 'Adoptado'
    post.save()
    return render(request, 'blog/adopt.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html/'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['name', 'breed', 'description', 'condition', 'picture']

    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.has_perm('post.change_post'):
            return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['name', 'breed', 'description', 'condition', 'picture']

    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.has_perm('post.change_post'):
            return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
