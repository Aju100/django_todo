from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, "todo.html", {"all_items": all_todo_items})


def addTodo(request):

    addedContent = request.POST["content"]
    new_item = TodoItem(content=addedContent)
    new_item.save()
    return HttpResponseRedirect("/todo/")


def deleteTodo(request, todo_id: int):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect("/todo/")
