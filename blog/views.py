from django.shortcuts import render
from django.views.generic.edit import UpdateView

# Create your views here.
from django.views import generic

from .models import Blog

class BlogList(generic.ListView):
    queryset  = Blog.objects.filter(status=1).order_by('-created_on')

# def index(request):
#     blogs = Blog.objects.filter(status=1).order_by('-created_on')
#     return render(request, 'blog/blog_list.html', {'blogs': blogs})

class BlogDetail(generic.DetailView):
    model = Blog
    #template_name = 'blog/blog_detail.html'
class BlogUpdate(UpdateView):
    model = Blog