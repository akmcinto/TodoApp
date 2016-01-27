import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class TodoList(models.Model):
    list_title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
    list_user = models.ForeignKey(User)

    def __str__(self):
        return self.list_title

class Item(models.Model):
    item_text = models.CharField(max_length=250)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList)

    def __str__(self):
        return self.item_text
