from django.shortcuts import render
from django.http import HttpRequest

def login_page(r:HttpRequest):
    return render(request=r, template_name='login.html')

def inbox_page(r:HttpRequest):
    return render(request=r, template_name='inbox.html')

def index_page(r:HttpRequest):
    return render(request=r, template_name='index.html')


def about_templates_page(r:HttpRequest):
    return render(request=r, template_name='about-templatemo.html')

def projects_page(r:HttpRequest):
    return render(request=r, template_name='projects.html')

def settings_page(r:HttpRequest):
    return render(request=r, template_name='settings.html')

def analystics_page(r:HttpRequest):
    return render(request=r, template_name='analytics.html')
