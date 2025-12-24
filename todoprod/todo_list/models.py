from django.db import models

# Create your models here.

class ToDoItem(models.Model):

    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = 'id',
        verbose_name = 'ToDo item'


    def __str__(self):
        return self.title