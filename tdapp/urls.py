from django.urls import path
from .views import TaskView, Add_Task, Del_Task, Quick_View, Dead_View

urlpatterns=[
    path("",Quick_View.as_view(),name="home"),
    path("tasks",TaskView.as_view(),name="Tasks"),
    path("new_task",Add_Task.as_view(),name="New-Task"),
    path("delete/<int:pk>",Del_Task.as_view(),name="remove_task"),
    path("progress",Dead_View.as_view(),name="expired")
]