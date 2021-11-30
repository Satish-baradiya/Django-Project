from django.shortcuts import render
from django.http import HttpResponse
from .models import NewTodo

# Create your views here.


def index(request):
    return render(request, "todo/index.html", {
        "todo": NewTodo.objects.all(),
    })


def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        todo = NewTodo.objects.create(title=title, description=description)
        todo.save()
        return render(request, "todo/index.html",{
            "todo":NewTodo.objects.all(),
        })

    return render(request, "todo/add.html")

def remove(request):
    return HttpResponse("Deleted")