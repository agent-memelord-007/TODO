from audioop import reverse
from django.shortcuts import render
from .models import Tasks
from django.views.generic import ListView, CreateView, DeleteView
from .forms import Add_Task
from django.urls import reverse_lazy
import datetime



class TaskView(ListView):
    model=Tasks
    template_name="tasks.html"



class Add_Task(CreateView):
    model=Tasks
    form_class=Add_Task
    template_name="new_task.html"

class Del_Task(DeleteView):
    model=Tasks
    template_name="remove_task.html"
    success_url=reverse_lazy("Tasks")

class Quick_View(ListView):
    model=Tasks
    template_name="tdapp.html"
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(task_time=datetime.date.today())
        return queryset


class Dead_View(ListView):
    model=Tasks
    template_name="Progress.html"
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(task_time__lt=datetime.date.today())
        return queryset