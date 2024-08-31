from catalog.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Appointment

from django.forms import ModelForm


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class AppointmentForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Appointment
        fields = ("name", "phone_number", "name_service")

