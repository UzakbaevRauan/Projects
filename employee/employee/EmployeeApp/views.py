from django.shortcuts import render
from EmployeeApp.models import Person,Job_titles
import requests 

# Create your views here.
def index(request):
    context={
        'persons':Person.objects.all(),
        'job_titles':Job_titles.objects.all(),

    }
    return render(request,'index.html',context)


def index(request,job_title_id= None):
    if job_title_id==None:
        persons = Person.objects.all()
    elif job_title_id >1 and job_title_id <7:
        job_title = Job_titles.objects.get(id=job_title_id)
        persons = Person.objects.filter(job_title=job_title)
    else:   
        persons = Person.objects.all()
    context={
        'persons':persons,
        'job_titles':Job_titles.objects.all(),

    }
    return render(request,'index.html',context)

def contact(request,person_id= None):
    if person_id:
        persons = Person.objects.filter(id=person_id)
    else:   
        persons = Person.objects.all()
    context={
        "persons":persons
    }
    return render(request,"contact.html",context)


def sort_by_age(request):
    sorted_people=reversed(Person.objects.order_by('age'))
    context={
     'persons':sorted_people,
     'job_titles':Job_titles.objects.all(),
    }
    return render(request,'index.html',context)

def search(request):
    query = request.GET.get('query') 
    results = Person.objects.filter(first_name=query) 
    context={
        'persons': results,
        'job_titles':Job_titles.objects.all(),
        }

    return render(request, 'index.html', context)


