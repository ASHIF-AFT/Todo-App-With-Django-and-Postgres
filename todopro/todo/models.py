from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
#python manage.py migrate todo

# After that we need to migrate our models


class Todo(models.Model):
    content= models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)# datetime.datetime.now()

# python manage.py makemigrations todo
# python manage.py sqlmigrate todo 0001  --> (sometime its may vary)
#python manage.py migrate todo