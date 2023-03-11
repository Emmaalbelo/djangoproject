from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    #path('tasks/<str:title>', views.tasks),
    path('tasks/', views.Tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_projects, name='create_project')
    
]

'''
podemos crear nombres internamente para asignarles a nuestras URL's, de este modo, cuando hagamos un cambio en la URL, no sera
necesario actualizar todo el codigo.
    ejemplo inicial:
    path('', views.index),
    asignandole un name:
    path('', views.index, name='index'),

'''