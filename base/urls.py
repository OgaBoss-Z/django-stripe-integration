from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('charge/', views.charge, name='charge'),
   path('success/<str:args>/', views.successMsg, name='success'),
]
