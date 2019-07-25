from django.shortcuts import render
from django.utils import timezone
from .models import Post
from datetime import datetime
from django.http import HttpResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt



'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})
'''

def a_view(request):
    return render(request, 'blog/post_list.html',{'time':datetime.now()})
