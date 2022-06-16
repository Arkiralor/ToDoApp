from django.contrib import admin

from api.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'date_added', 'date_completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description', 'date_added')
    ordering = ('-date_added',)


