
from django.urls import path
from polls import views

app_name = "polls"

urlpatterns = [

    path('employee/',views.my_view),
    path('employee/job_title/<int:id>/', views.my_view, name='filter'),
    path('search/', views.search, name='search'),
    path('sort/', views.sort_by_birthday, name='sort_by_birthday'),
    path('employee/person/<int:person_id>/', views.contact, name='contact'),
]