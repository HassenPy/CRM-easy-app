from django.contrib import admin
from .models import Subscriber
# Register your models here.


class Sub_Info(admin.ModelAdmin):
    list_display = ('user_rec', 'state', 'city')


admin.site.register(Subscriber, Sub_Info)
