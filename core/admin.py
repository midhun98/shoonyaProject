from django.contrib import admin

from core import models

# Register your models here.

admin.site.register(models.Retreat)
admin.site.register(models.Booking)
admin.site.register(models.Tag)