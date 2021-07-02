from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.RoomCategories)
admin.site.register(models.RoomRentals)
admin.site.register(models.Rooms)
admin.site.register(models.ServiceTypes)
admin.site.register(models.Services)
admin.site.register(models.Staff)
admin.site.register(models.Status)
