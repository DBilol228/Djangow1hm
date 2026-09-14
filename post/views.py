from django.shortcuts import render,redirect,get_object_or_404
from .models import * 

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'detail.html',{'post':post})

def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        video = request.FILES.get('video')
        Post.objects.create(title=title,description=description,photo=photo,video=video)
        return redirect('home')
    return render(request,'create.html')

def update(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method=='POST':
        post.title=request.POST.get('title')
        post.description=request.POST.get('description')
        if request.FILES.get('photo'):
            post.photo = request.FILES.get('photo')
        if request.FILES.get('video'):
            post.video = request.FILES.get('video')
        post.save()
        return redirect('detail',id=post.id)
    return render(request,'update.html',{'post':post})

def delete(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request,'delete.html',{'post':post})