<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> 652cf96 (changes made to ui and also changed the edit and update)

# Create your views here.
from django.contrib import messages

from .forms import TodoForm
from .models import Todo
from django.utils import timezone

def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def edit(request, item_id):
    item = Todo.objects.get(id=item_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=item)

    page = {
        "form": form,
        "title": "Edit Task",
    }
    return render(request, 'todo/edit.html', page)

<<<<<<< HEAD

def toggle_status(request, item_id):
    """Toggle completion status for a Todo item."""
    item = Todo.objects.get(id=item_id)
=======
def toggle_status(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
>>>>>>> 652cf96 (changes made to ui and also changed the edit and update)
    item.is_completed = not item.is_completed
    if item.is_completed:
        item.completed_at = timezone.now()
    else:
        item.completed_at = None
    item.save()
<<<<<<< HEAD
    return redirect('todo')

=======
    return redirect('todo')
>>>>>>> 652cf96 (changes made to ui and also changed the edit and update)
