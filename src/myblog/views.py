from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.

# def home(request):
#     return HttpResponse("HELLO WORLD")



def post_list(request):
    qs = Post.objects.filter(status="p")
    context = {
        "object_list":qs
    }
    return render(request,"myblog/post_list.html", context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            # post = PostForm(file_field=request.FILES['filename'])
            post = form.save(commit=False)
            
            post.author = request.user
            
            
            post.save()
            return redirect("blog:list")
    
    context = {
        "forms":form
    }
    return render(request,"myblog/post_create.html", context)


def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        "obj" : obj
    }
    return render(request, "myblog/post_detail.html", context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blog:list")
    context = {
        "obj" : obj,
        "form" : form
    }
    
    return render(request, "myblog/post_update.html", context)

def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    # form = PostForm(request.POST or None, request.FILE or None, instance=obj)
    if request.method=="POST":
        obj.delete()
        messages.success(request, "Post deleted!!")
        return redirect("blog:list")
    
    context = {
       "obj" : obj
    }
    
    return render(request, "myblog/post_delete.html", context)