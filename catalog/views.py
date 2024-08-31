from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import (
    ServiceForm,
    ServiceModeratorForm,
    DescriptionForm,
    DescriptionModeratorForm,
    # ServicesCatalogForm
)
from catalog.models import (
    Services,
    Description,
    # ServicesCatalog
)
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
    services = Services.objects.all()
    descriptions = Description.objects.all()
    context = {
        'services': services,
        'descriptions': descriptions,
    }
    return render(request, 'catalog/main_page.html', context=context)


class DescriptionCreateView(CreateView):
    model = Description
    form_class = DescriptionForm
    success_url = reverse_lazy("catalog:main_page")


class DescriptionUpdateView(UpdateView):
    model = Description
    form_class = DescriptionForm
    success_url = reverse_lazy("catalog:main_page")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return DescriptionForm
        if user.has_perm("catalog.can_edit_heading") and user.has_perm("catalog.can_edit_description") and user.has_perm("catalog.can_edit_image"):
            return DescriptionModeratorForm
        raise PermissionDenied

