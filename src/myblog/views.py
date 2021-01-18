from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.

# def home(request):
#     return HttpResponse("HELLO WORLD")



def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list":qs
    }
    return render(request,"myblog/post_list.html", context)