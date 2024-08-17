from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signUp/", views.signUp, name="signUp"),
    path("adminHome/", views.adminHome, name="adminHome"),
    path("adminUpdate/", views.adminUpdate, name="adminUpdate"),
    path("customerHome/", views.customerHome, name="customerHome"), 
    path("customerCart/", views.customerCart, name="customerCart"),     
    path("feedback/", views.feedback, name="feedback"),    
]

