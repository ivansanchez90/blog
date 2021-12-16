from django.urls import path
from .views import (
    home,
    generales,
)
urlpatterns = [
    path('',home, name = 'index'),
    path('generales/',generales, name = 'generales'),

]