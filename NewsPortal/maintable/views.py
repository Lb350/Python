from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django import forms
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    time_in = 'time_in'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(PostList):
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_create.html'
    context_object_name = 'news_create'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == 'posts/articles/create/':
            post.type_paper = 'ART'
        post.save()
        return super().form_valid(form)


class NewsEdit(UpdateView):
    form_class = PostForm
    template_name = 'news_edit.html'
    context_object_name = 'news_edit'


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('post_list')


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_paper = 'ART'
        return super().form_valid(form)


class ArticlesEdit(UpdateView):
    form_class = PostForm
    template_name = 'articles_edit.html'
    context_object_name = 'articles_edit'






