from django.contrib import admin

from todo.models import Tasks
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    search_fields=("task",)

# Register your models here.
admin.site.register(Tasks,TaskAdmin)
