from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    login = models.CharField(max_length=255)
    password = models.CharField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    role = models.CharField()


class Manual(models.Model):
    command_name = models.CharField()
    cmd_description = models.TextField()


class Module(models.Model):
    module_name = models.CharField(max_length=255)


class Theory(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    theme_name = models.CharField(max_length=255)
    description = models.TextField()


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    condition = models.TextField()
    test_data = models.JSONField()


class Attempt(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    task_id = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now=True)
    source_file = models.TextField()
    state = models.BooleanField(default=False)
