from django.db import models

class ToDoItem(models.Model):
    
        title = models.CharField(max_length=200)
        completed = models.BooleanField(default=False)
 
        class Meta:
           app_label = 'todo'
    

        def __str__(self):
          return self.title
