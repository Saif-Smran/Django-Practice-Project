
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.all_Tapp, name='all_Tapp'),
    path('<int:tapp_id>/', views.tapp_detail, name='tapp_detail'),
]
