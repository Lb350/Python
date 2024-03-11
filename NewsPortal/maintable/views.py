from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


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


class PostSearch(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('maintable.add_post',)
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


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('maintable.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'


class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('maintable.change_post',)
    model = Post
    form_class = PostForm
    template_name = 'news_edit.html'
    context_object_name = 'news_edit'


class ArticlesEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('maintable.change_post',)
    model = Post
    form_class = PostForm
    template_name = 'articles_edit.html'
    context_object_name = 'articles_edit'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_paper = 'ART'
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('maintable.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    context_object_name = 'news_delete'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('maintable.delete_post',)
    model = Post
    template_name = 'articles_delete.html'
    context_object_name = 'articles_delete'
    success_url = reverse_lazy('post_list')

@method_decorator(login_required, name='dispatch')
class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected_page.html'


class CategoryListView(PostList):
    model = Post
    template_name = 'posts/category_list.html'
    context_object_name = 'category_posts_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-time_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Активирована подписка на '
    return render(request, 'posts/subscribe.html', {'category': category, 'message': message})


def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'You have successfully unsubscribed from the category newsletter'
    return render(request, 'posts/subscribe.html', {'category': category, 'message': message})