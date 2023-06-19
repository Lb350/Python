from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce

class Author(models.Model):
    user_rating = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def update_rating(self):
        articles_rating = Post.objects.filter(author_id=self.pk).aggregate(sum_articles = Coalesce(Sum('rating_post') * 3, 0))['sum_articles']
        comments_rating = Comment.objects.filter(comment_user_id=self.user).aggregate(sum_articles=Coalesce(Sum('rating_comment'), 0))['sum_articles']
        comments_articles_rating = Comment.objects.filter(comment_post__author__user=self.user).aggregate(sum_posts=Coalesce(Sum('rating_comment'), 0))['sum_posts']
        self.rating = articles_rating + comments_rating + comments_articles_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name.title()


class Post(models.Model):

    news = 'NWS'
    articles = 'ART'

    TYPE_PAPER = [
        (news, 'Новости'),
        (articles, 'Статьи')
    ]

    type_paper = models.CharField(max_length=3,
                                  choices=TYPE_PAPER,
                                  default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    connect_categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return f'{self.text_post[:125]}...'

    def __str__(self):
        return self.text_post.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.CharField(max_length=1000, default=True)
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
