from django.urls import path
from .views import login_page, inbox_page, index_page,analystics_page, about_templates_page,projects_page, settings_page

urlpatterns = [
    path('login/',login_page,name='login'),
    path('inbox/',inbox_page,name='inbox'),
    path('',index_page,name='index'),
    path('analytics/',analystics_page,name='analytics'),
    path('about/',about_templates_page,name='about'),
    path('projects/',projects_page,name='projects'),
    path('settings/',settings_page,name='settings')  
    
]