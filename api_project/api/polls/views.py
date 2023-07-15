from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Employee,Job_title
from datetime import datetime,date
from django.core.paginator import Paginator, Page

def my_view(request):
    with open('D:\project/file.json') as file:
        data = json.load(file)
        employees = []
        
        for item in data['items']:
            employee = Employee(
                id=item['id'],
                avatarUrl=item['avatarUrl'],
                firstName=item['firstName'],
                lastName=item['lastName'],
                userTag=item['userTag'],
                department=item['department'],
                position=item['position'],
                birthday=item['birthday'],
                phone=item['phone']
            )
            employee.save()
            employees.append(employee)



    employee_list = list()
    for employee in employees:
        employee_data = {
            'id': employee.id,
            'avatarUrl': employee.avatarUrl,
            'firstName': employee.firstName,
            'lastName': employee.lastName,
            'userTag': employee.userTag,
            'department': employee.department,
            'position': employee.position,
            'birthday': employee.birthday,
            'phone': employee.phone
        }
        employee_list.append(employee_data) 

    
    context = {
        'employees': employee_list,
        "job_titles":Job_title.objects.all(),
        
    }
    return render(request, 'index.html',context)

def my_view(request,id= None):

    link_clicked = False
    id = id
    if id==None or id ==1:
        persons = Employee.objects.all()
        link_clicked = True
    elif id >1 and id <7:
        persons = Employee.objects.filter(department=Job_title.objects.get(id=id).name)
        link_clicked = True
    else:   
        link_clicked = False
    
    context={
        'employees':persons,
        'job_titles':Job_title.objects.all(),
        'link_clicked':link_clicked,
        'id':id
        
    }
    return render(request,'index.html',context) 




def search(request):
    query = request.GET.get('query') 

    results = Employee.objects.filter(firstName__startswith=query) | Employee.objects.filter(lastName__startswith=query) 
  
    context={
        "query":query,
        'employees': results,
        'job_titles':Job_title.objects.all(),
        }

    return render(request, 'index.html', context)




def sort_by_birthday(request):
    sorted_people=Employee.objects.order_by('birthday')
    context={
     'employees':sorted_people,
     'job_titles':Job_title.objects.all(),
    }
    return render(request,'index.html',context)




def contact(request,person_id= None):
    if person_id:
        persons = Employee.objects.filter(id=person_id)
    else:   
        persons = Employee.objects.all()
        
    birthday_values = persons.values_list('birthday', flat=True)
    birthday_year = [birthday.year for birthday in birthday_values]
    birthday_month = [birthday.month for birthday in birthday_values]
    birthday_day = [birthday.day for birthday in birthday_values]

    birthday = date( int(birthday_year[0]), int(birthday_month[0]), int(birthday_day[0])) 
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1

    context={
        "employees":persons,
        "age":age,
        
    }
    return render(request,"contact.html",context)
