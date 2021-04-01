from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeView(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # String of HTML code
    return render(request, "home.html", {})

def contactView(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    
    return render(request, "contact.html", {})

def aboutView(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [123, 4323, 12313, "testing"]
    }
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, "about.html", my_context)

def socialView(request, *args, **kwargs):
    # return HttpResponse("<h1>Social Page</h1>")
    return render(request, "social.html", {})