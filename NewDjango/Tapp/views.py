from django.shortcuts import render
from .models import TapVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_Tapp(request):
    tapps = TapVarity.objects.all()
    return render(request, 'Tapp/all_Tapp.html', {'tapps': tapps})

def tapp_detail(request, tapp_id):
    tapp = get_object_or_404(TapVarity, pk=tapp_id)
    return render(request, 'Tapp/tap_detail.html', {'tapp': tapp})
