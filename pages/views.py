from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
   # {{ % request.user%}}
   # return HttpResponse("<h1> Hellow World</>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hellow World about view </>")
    my_context = {
        "my_text":  "This is just some description about the application", "my_number": 123}
    return render(request, "about.html", my_context)
