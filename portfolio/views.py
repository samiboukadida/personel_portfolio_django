from django.shortcuts import render
from django.views import generic

from .models import Project
# Create your views here.

# def home(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/home.html', {'projects': projects})

class ProjectList(generic.ListView):
    paginate_by = 4
    model = Project
    queryset = Project.objects.all()
    template_name = 'portfolio/home.html'