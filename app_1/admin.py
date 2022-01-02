from django.contrib import admin

# Register your models here.
from .models import Message


class App1Admin(admin.ModelAdmin):
    pass

admin.site.register(Message, App1Admin)
