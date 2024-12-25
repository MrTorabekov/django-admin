from django.urls import path
from post.views import post

urlpatterns = [
    path('', post, name='post'),
]
