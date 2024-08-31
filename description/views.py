from django.shortcuts import render
from description.forms import DoctorForm, CompanyForm, CompanyModeratorForm, DoctorModeratorForm
from description.models import Doctors, Company
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class DoctorsListView(ListView):
    model = Doctors
    context_object_name = 'doctors'


class DoctorsDetailView(DetailView):
    model = Doctors


class DoctorsCreateView(CreateView):
    model = Doctors
    form_class = DoctorForm
    success_url = reverse_lazy("description:doctor_list")


class DoctorsUpdateView(UpdateView):
    model = Doctors
    form_class = DoctorForm
    success_url = reverse_lazy("description:doctor_list")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return DoctorForm
        if user.has_perm("description.can_edit_specialization") and user.has_perm("description.can_edit_photo") and user.has_perm("description.can_edit_description"):
            return DoctorModeratorForm
        raise PermissionDenied


class DoctorsDeleteView(DeleteView):
    model = Doctors
    success_url = reverse_lazy("description:doctor_list")


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy("description:companydescription_list")


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy("description:companydescription_list")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return CompanyForm
        if user.has_perm("description.can_edit_heading") and user.has_perm("description.can_edit_description") and user.has_perm("description.can_edit_image"):
            return CompanyModeratorForm
        raise PermissionDenied


def about_the_company(request):
    return render(request, 'description/about_the_company.html')
