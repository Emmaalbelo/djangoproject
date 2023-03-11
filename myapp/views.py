from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# get_object_or_404 #en caso de que llamemos a una seccion que no existente, devuelve 404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
# request (petición)


def index(request):
    title = 'Django course!!'
    return render(request, "Index.html", {'title': title})
# motores de plantilla / templates son modulos que prosesan html.


def about(request):
    username = "Emmaalbelo"
    return render(request, "About.html", {'username': username})


def hello(request, username):
    return HttpResponse('<h2>Hello world %s</h2>' % username)


def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse (projects, safe=False)
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects})


def Tasks(request):  # antes teniamos un segundo parametro 'title'
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # task = Task.objects.get(title=title)
    # return HttpResponse ('task: %s' % task.title) #%s se usa para concatenar
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {'tasks': tasks})


def create_task(request):
    # Task.objects.create(title=request.GET['title'], description=request.GET ["description"], projectkey=2)
    # return render(request, "create_task.html", {"form": CreateNewTask()})
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(title=request.POST["title"],
                            description=request.POST["description"], project_id=2)
        return redirect('tasks')


def create_projects(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('/project/')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render (request, "projects/detail.html", {
        'project': project,
        'tasks': tasks})