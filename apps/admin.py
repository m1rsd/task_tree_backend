from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Menu


# admin.site.register(Category)


@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    pass
