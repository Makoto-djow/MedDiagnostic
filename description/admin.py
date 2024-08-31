from django.contrib import admin
from description.models import Doctors, Company


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lastname", "patronymic")
    search_fields = ("id", "name", "lastname", "patronymic")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "heading")
    search_fields = ("id", "heading")
