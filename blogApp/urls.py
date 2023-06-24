from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogPost/<str:pk>', views.blogPost, name='blogPost')  ## Making each post dynamic with individual unique IDs.
]
