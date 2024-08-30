from django.contrib import admin
from catalog.models import (
    Services,
    Description,
    # ServicesCatalog
)

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "service_name", "price")
    search_fields = ("id", "service_name")


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "description_title")
    search_fields = ("id", "description_title")


# @admin.register(ServicesCatalog)
# class ServicesCatalogAdmin(admin.ModelAdmin):
#     list_display = ("id", "service")
#     search_fields = ("id", "service")

