from django.contrib import admin
from .models import TodoListItem


class todoappAdmin(admin.ModelAdmin):
    list_display = ('content',)


# Register your models here.
admin.site.register(TodoListItem, todoappAdmin)
