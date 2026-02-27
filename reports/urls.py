from django.urls import path
from . import views

urlpatterns = [
    path('Pajina-sumario.html/', views.tabs, name="tab-dash"),
]