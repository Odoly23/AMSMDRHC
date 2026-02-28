from django.urls import path
from . import views

urlpatterns = [
    path('Pajina-Distribuisaun.html/', views.dash_d, name="dist-dash"),
]