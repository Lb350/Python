from django.contrib import admin
from .models import Category, Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_paper', 'author', 'time_in')
    list_filter = ('type_paper', 'author')
    search_fields = ('title', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_rating', )





admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)