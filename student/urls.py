from django.urls import path
from . import views

urlpatterns =[
    path('students/', student_ListCreate)
]