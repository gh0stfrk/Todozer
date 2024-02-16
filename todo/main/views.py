from django.shortcuts import render, HttpResponse
from django.template import loader
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


from main.models import Todo
from django.shortcuts import get_object_or_404


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('main/home.html')

    pending_todos = Todo.objects.filter(completed=False)
    completed_todos = Todo.objects.filter(completed=True)
    return HttpResponse(template.render(context={'todos': pending_todos, 'completed_todos': completed_todos}),)

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
            return HttpResponse("Item not found")
    else:
        return HttpResponse("Method not allowed")


@csrf_exempt
def delete_todo(request, item_id):
    if request.method == 'DELETE':
        try:
            todo_item = get_object_or_404(Todo, pk=item_id)
            todo_item.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse("Item not found")
    else:
        return HttpResponse("Method not allowed")
