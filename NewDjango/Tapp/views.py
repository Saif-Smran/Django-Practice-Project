from django.shortcuts import render

# Create your views here.
def all_Tapp(request):
    return render(request, 'Tapp/all_Tapp.html')
