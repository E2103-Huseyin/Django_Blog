from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post,Like, PostView
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# def home(request):
#     return HttpResponse("HELLO WORLD")



def post_list(request):
    qs = Post.objects.filter(status="p")
    context = {
        "object_list":qs
    }
    return render(request,"myblog/post_list0.html", context)

@login_required()
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
            messages.success(request, "Post created succesfully")
            return redirect("blog:list")
    
    context = {
        "forms":form
    }
    return render(request,"myblog/post_create.html", context)

@login_required()
def post_detail(request, slug):
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)
    #views counter
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=obj)#get_or_create=>eğer varsa create etmiyor. yoksa create ediyor 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user  = request.user
            comment.post = obj
            comment.save()
            
            return redirect("blog:detail", slug=slug)
    context = {
        "obj" : obj,
        "form" : form
    }
    return render(request, "myblog/post_detail0.html", context)

@login_required()
def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if request.user.id != obj.author.id:
        messages.warning(request, "You're not a writer of this post")
        return redirect("blog:list")
    if form.is_valid():
        form.save()
        messages.success(request, "Post updated succesfully")
        return redirect("blog:list")
    context = {
        "obj" : obj,
        "form" : form
    }
    
    return render(request, "myblog/post_update.html", context)

@login_required()
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    # form = PostForm(request.POST or None, request.FILE or None, instance=obj)
    if request.user.id != obj.author.id:
        # return HttpResponse("You're not a writer of this post")
        messages.warning(request, "You're not a writer of this post")
        return redirect("blog:list")
    if request.method=="POST":
        obj.delete()
        messages.success(request, "Post deleted!!")
        return redirect("blog:list")
    
    context = {
       "obj" : obj
    }
    
    return render(request, "myblog/post_delete.html", context)

@login_required()
def like(request, slug):
    
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj )
        if like_qs:
            like_qs.delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("blog:like", slug=slug)
    return redirect('blog:detail', slug=slug)