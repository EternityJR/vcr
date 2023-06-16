from django.contrib import admin
from .models import Manual, User, Module, Theory, Task, Attempt

# Register your models here.
admin.site.register(Manual)
admin.site.register(User)
admin.site.register(Module)
admin.site.register(Theory)
admin.site.register(Task)
admin.site.register(Attempt)