from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListsAdmin(admin.ModelAdmin):

    """ Lists Admin Definition """

    pass