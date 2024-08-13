from django.contrib import admin
from .models import Meal


class MenuMealAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    search_fields = ("name", "description")
    list_filter = ("status", )


admin.site.register(Meal, MenuMealAdmin)