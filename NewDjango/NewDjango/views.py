from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django! <br> Welcome to Django web development Project. <br> Enjoy your stay!  </br> You are at home page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, Django! <br> Welcome to Django web development Project. <br> Enjoy your stay!  </br> You are at about page.")

def contact(request):
    return HttpResponse("Hello, Django! <br> Welcome to Django web development Project. <br> Enjoy your stay!  </br> You are at contact page.")

