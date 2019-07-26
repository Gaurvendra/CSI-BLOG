from django.contrib import admin
from django.urls import path
from . import views
from .views import PostCreateView,UpdatePost,PostDelete
urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
    path('new/', PostCreateView.as_view() , name='new'),
    path('blogpost/<int:pk>/update', UpdatePost.as_view() , name='update'),
    path('blogpost/<int:pk>/delete', PostDelete.as_view() , name='delete'),


]
