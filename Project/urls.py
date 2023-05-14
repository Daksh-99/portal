from django.urls import path, include
from . import views
from django.contrib import admin
from .views import home, details
from .views import projviewset

urlpatterns = [
    path('home/', home, name='home'),
    path('details/<int:id>', details, name='details'),
    path('projlist/', projviewset.as_view({'get': 'list'}), name='alldetails'),
    path('personproj/<int:rollno>/',
         projviewset.as_view({'get': 'retrieve'}), name='personproj'),

]
