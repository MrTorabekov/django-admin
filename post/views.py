from django.shortcuts import render
from post.models import Post

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})
