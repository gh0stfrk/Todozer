from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from main.forms import AddTodo

from main.models import Todo
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger(__name__)


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('main/home.html')

    todo_form = AddTodo()

    pending_todos = Todo.objects.filter(completed=False)
    completed_todos = Todo.objects.filter(completed=True)
    return HttpResponse(template.render(context={'todos': pending_todos, 'completed_todos': completed_todos, 'form':todo_form}),)

@csrf_exempt
def mark_complete(request, item_id):
    if request.method == 'POST':
        try: 
            todo_item = get_object_or_404(Todo, pk=item_id)
            todo_item.completed = True
            todo_item.save()
            return HttpResponse(status=204)
        except:
            messages.error(request, message="Item not found")
            return JsonResponse({"msg": "Item not found"})
    else:
        return JsonResponse({"msg": "Method not allowed"})


@csrf_exempt
def delete_todo(request, item_id):
    if request.method == 'DELETE':
        try:
            todo_item = get_object_or_404(Todo, pk=item_id)
            todo_item.delete()
            return HttpResponse(status=204)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"msg": "Item not found", "error":e}, status=404)
    else:
        return JsonResponse({"msg": "Method not allowed"})

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        form = AddTodo(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Todo.objects.create(title=title, description=description)
            messages.success(request, message="Todo added successfully")
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)
