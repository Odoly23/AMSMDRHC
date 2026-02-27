from django.urls import path
from . import views

urlpatterns = [
    path('Pajina-Dashboard.html/', views.dash, name="d-dash"),
]