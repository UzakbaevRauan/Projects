
from django.urls import path

from EmployeeApp import views

app_name = "EmployeeApp"

urlpatterns = [
    path('employee',views.index, name="index"),
    path('employee/job_title/<int:job_title_id>/', views.index, name='filter'),
    path('employee/person/<int:person_id>/', views.contact, name='contact'),
    path('sort/', views.sort_by_age, name='sort_by_age'),
    path('search/', views.search, name='search'),
    
]
