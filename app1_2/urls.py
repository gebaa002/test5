from django.urls import path
from . import views


urlpatterns = [
    path('',views.Projet2,name='projet2')

]