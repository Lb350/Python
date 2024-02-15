from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('posts/', include('maintable.urls')),
    path('sign/', include('allauth.urls')),
    path('auth/', include('sign.urls')),


]

