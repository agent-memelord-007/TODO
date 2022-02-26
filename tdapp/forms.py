from django.forms import ModelForm, TextInput, Textarea, DateTimeField
from django.contrib.admin import widgets
from .models import Tasks
from .widgets import DTInput

class Add_Task(ModelForm):
    class Meta:
        model=Tasks
        fields=["task_name", "task_time"]
        widgets={
            "task_name":TextInput(attrs={"class":"input","placeholder":"Name of task"}),
            "task_time":DTInput()
        }
