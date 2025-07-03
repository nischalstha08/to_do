from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
<<<<<<< HEAD
        exclude = ["is_completed", "completed_at"]
=======
        fields = ["title", "details", "date"]
>>>>>>> 652cf96 (changes made to ui and also changed the edit and update)
