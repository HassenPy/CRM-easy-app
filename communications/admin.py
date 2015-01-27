from django.contrib import admin
from .models import Communication


class ComList(admin.ModelAdmin):
    list_display = ('subject', 'uuid')

admin.site.register(Communication, ComList)
