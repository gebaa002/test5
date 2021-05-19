from django.urls import path
from . import views


urlpatterns = [
    path('',views.Projet1, name='projet1')

]