from django.urls import path
from description.apps import DescriptionConfig
from description.views import (
    DoctorsListView,
    DoctorsDetailView,
    DoctorsCreateView,
    DoctorsUpdateView,
    DoctorsDeleteView,
    about_the_company,

    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
)

app_name = DescriptionConfig.name

urlpatterns = [
    path("doctors/list", DoctorsListView.as_view(), name="doctor_list"),
    path("doctors/<int:pk>/", DoctorsDetailView.as_view(), name="doctor_detail"),
    path("doctors/create", DoctorsCreateView.as_view(), name="doctor_create"),
    path("doctors/<int:pk>/update/", DoctorsUpdateView.as_view(), name="doctor_update"),
    path("doctors/<int:pk>/delete", DoctorsDeleteView.as_view(), name="doctor_delete"),

    path("company/list", CompanyListView.as_view(), name="company_list"),
    path("company/create", CompanyCreateView.as_view(), name="company_create"),
    path("company/<int:pk>/update/", CompanyUpdateView.as_view(), name="company_update"),

    path('', about_the_company, name='about_the_company'),
]
