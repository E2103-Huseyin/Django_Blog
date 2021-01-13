from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HELLO WORLD")


# def home(request):
#     message = "hello world!"
#     context = {
#         "message": message
#     }
#     return render(request, "myblog/home.html", context)