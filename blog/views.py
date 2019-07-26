from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView ,UpdateView ,DeleteView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def index(request):
    context={
       'post' :  post.objects.all() ,
       'recent' : post.objects.order_by('create_date').reverse()[0:6],
        'cat' : post.objects.values('category').distinct(),
       'slide': post.objects.order_by('create_date')[0:3],
    }

    return render(request ,'index.html', context)
def blogpost(request , id):
    context={
    'post' : post.objects.filter(id = id)[0],
    'recent': post.objects.order_by('create_date').reverse()[0:6],
    'cat': post.objects.values('category').distinct()[0:6]
    }
    print(post.id)
    return render(request ,'blogpost.html' , context)


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = post
    fields  = ['title','content', 'head_image','category']
    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

class UpdatePost(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
    model = post
    fields  = ['title','content', 'head_image','category']
    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False
class PostDelete(LoginRequiredMixin ,UserPassesTestMixin , DeleteView):
    model = post
    success_url = '/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False






