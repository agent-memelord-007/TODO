from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

class Tasks(models.Model):
    task_name=models.CharField(max_length=50)
    creation_datetime=models.DateTimeField(default=timezone.now)
    task_time=models.DateField(default=datetime.date.today())
    
    def __str__(self):
        return f"{self.task_name}   |   {self.task_time}"

    def get_absolute_url(self):
        return reverse("home")

    class Meta:
        verbose_name_plural="Tasks"