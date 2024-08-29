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
    path("description/list", DoctorsListView.as_view(), name="doctor_list"),
    path("description/<int:pk>/", DoctorsDetailView.as_view(), name="doctor_detail"),
    path("description/create", DoctorsCreateView.as_view(), name="doctor_create"),
    path("description/<int:pk>/update/", DoctorsUpdateView.as_view(), name="doctor_update"),
    path("description/<int:pk>/delete", DoctorsDeleteView.as_view(), name="doctor_delete"),

    path("company_list/", CompanyListView.as_view(), name="company_list"),
    path("company_create/", CompanyCreateView.as_view(), name="company_create"),
    path("company_update/<int:pk>/", CompanyUpdateView.as_view(), name="company_update"),

    path('', about_the_company, name='about_the_company'),
]
