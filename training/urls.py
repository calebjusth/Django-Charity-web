from django.urls import path
from . import views

urlpatterns =[
    path('', views.trainings, name="training"),
    path('students_registraion/', views.studentpage, name='student_form'),
    path('registered_successfully/', views.registeredpage, name='registered')
]