from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def index(request):
    blogPosts = BlogPost.objects.all()      ## Access all objects from BlogPost class
    return render(request, 'index.html', {'blogPosts': blogPosts})