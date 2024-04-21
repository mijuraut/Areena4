from django.urls import path
from . import views

urlpatterns = [
    path('gladiator/', views.gladiator_detail, name='gladiator_detail'),
    path('', views.base, name='base'),
    path('api', views.api),  # Define the URL route for the game API
]