from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ServiceForm, ServiceModeratorForm, DescriptionForm, DescriptionModeratorForm, \
    ServicesCatalogForm
from catalog.models import Services, Description, ServicesCatalog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.forms import inlineformset_factory

class ServicesListView(ListView):
    model = Services


class ServicesDetailView(DetailView):
    model = Services


class ServicesCreateView(CreateView):
    model = Services
    form_class = ServiceForm
    success_url = reverse_lazy("catalog:service_list")


class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    form_class = ServiceForm
    success_url = reverse_lazy("catalog:service_list")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ServiceForm
        if user.has_perm("catalog.can_edit_price") and user.has_perm("catalog.can_edit_description"):
            return ServiceModeratorForm
        raise PermissionDenied

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ServiceFormset = inlineformset_factory(Services, ServicesCatalog, ServicesCatalogForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ServiceFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ServiceFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ServicesDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy("catalog:service_list")


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')


def base(request):
    return render(request, 'catalog/base.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'catalog/feedback.html')


def main_page(request):
    return render(request, 'catalog/main_page.html')


class DescriptionListView(ListView):
    model = Description
    context_object_name = 'main_description'


class DescriptionCreateView(CreateView):
    model = Description
    form_class = DescriptionForm
    success_url = reverse_lazy("catalog:description_list")


class DescriptionUpdateView(UpdateView):
    model = Description
    form_class = DescriptionForm
    success_url = reverse_lazy("catalog:description_list")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return DescriptionForm
        if user.has_perm("catalog.can_edit_heading") and user.has_perm("catalog.can_edit_description") and user.has_perm("catalog.can_edit_image"):
            return DescriptionModeratorForm
        raise PermissionDenied


class ServicesCatalogListView(ListView):
    model = ServicesCatalog
    context_object_name = 'servicesc_'


class ServicesCatalogDetailView(DetailView):
    model = ServicesCatalog


class ServicesCatalogCreateView(CreateView):
    model = ServicesCatalog
    form_class = ServicesCatalogForm
    success_url = reverse_lazy("catalog:servicescatalog_list")


class ServicesCatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = ServicesCatalog
    form_class = ServicesCatalogForm
    success_url = reverse_lazy("catalog:servicescatalog_list")


class ServicesCatalogDeleteView(DeleteView):
    model = ServicesCatalog
    success_url = reverse_lazy("catalog:servicescatalog_list")

