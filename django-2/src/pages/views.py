from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args)
    print(request.user)
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context ={
        "my_text": "hello oluwatosin", 
        "my_number": 123,
        "my_list": [123, "abc", "xyz", "good"]
    }
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})