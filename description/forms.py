from django.forms import ModelForm
from catalog.forms import StyleFormMixin
from description.models import Doctors, Company


class DoctorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Doctors
        fields = ("description", "specialization", "photo")


class CompanyForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Company
        fields = ("heading", "description", "image")
