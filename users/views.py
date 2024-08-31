from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
import secrets

from users.forms import UserRegisterForm, AppointmentForm
from users.models import User, Appointment

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(21)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class AppointmentListView(ListView):
    model = Appointment

    def get_queryset(self):
        # Получение текущего пользователя
        current_user = self.request.user
        # Фильтрация объектов по пользователю, который их создал
        return Appointment.objects.filter(user=current_user)


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("users:appointment_list")

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.user = self.request.user
        appointment.save()
        return super().form_valid(form)


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("users:appointment_list")


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("users:appointment_list")
