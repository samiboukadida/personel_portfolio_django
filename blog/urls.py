from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/update', views.BlogUpdate.as_view(), name='blog_update'),
]