from django.forms import ModelForm, BooleanField
from catalog.models import (
    Services,
    Description,
)


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class ServiceModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Services
        fields = ("description", "price")


class DescriptionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Description
        fields = '__all__'


class DescriptionModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Description
        fields = ("description_title", "description")
