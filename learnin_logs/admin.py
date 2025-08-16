from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

#Register Topic with the admin file
admin.site.register(Topic)

#Register Entry with the admin file
admin.site.register(Entry)

