from django.db import models
# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)
    class Meta:  
        db_table = "todo"