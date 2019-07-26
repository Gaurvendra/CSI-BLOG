from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registeru, userupdate ,profileupdate
from django.contrib.auth.decorators import login_required
from blog.models import post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registeru(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f' Account Created for {username}!')
            return redirect('login')

        else:
            print("sdgsdfg")


    else:
        form = registeru()
    return render(request,'register.html',{'form' : form})
@login_required
def profile(request):
    u = request.user
    posts =  post.objects.filter(auther = u)
    if request.method == 'POST':
        uform = userupdate(request.POST, instance = request.user)
        pform = profileupdate(request.POST , request.FILES, instance = request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            username = uform.cleaned_data.get('username')
            messages.success(request, f' Account Updated for {username}!')
            return redirect('profile')

    else:
        uform = userupdate(instance=request.user)
        pform = profileupdate(instance=request.user.profile)
    context = {
        'uform': uform,
        'pform': pform,
        'posts': posts
    }
    return render(request,'profile.html',context)

