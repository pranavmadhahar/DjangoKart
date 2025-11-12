from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    totalPosts = Blogpost.objects.all()
    print(totalPosts)
    return render(request, 'blog/index.html', {'totalPosts': totalPosts} )

def blogpost(request, id):
    # filter returns a list, and we need the post it contains.
    post = Blogpost.objects.filter(post_id = id)[0] 
    print(post)
    return render(request, 'blog/blogpost.html', {'post':post} )

