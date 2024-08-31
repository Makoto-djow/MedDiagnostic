from django.contrib.auth.models import AbstractUser
from django.db import models


from catalog.models import Services

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone_number = models.CharField(max_length=21, verbose_name="Номер телефона клиента")
    name_service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name="Название услуги", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Укажите пользователя", related_name="Пользователь", default=None)

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"
        permissions = [
            ("can_edit_name", "Может менять имя"),
            ("can_edit_phone_number", "Может менять номер телефона"),
        ]

    def __str__(self):
        return f"{self.name}"


# class Diagnostic(models.Model):
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, verbose_name="Запись", help_text="Укажите запись")
#     result = models.TextField(max_length=1000, verbose_name="Результат диагностики")
#
#     class Meta:
#         verbose_name = "Запись на прием"
#         verbose_name_plural = "Записи на прием"
#         permissions = [
#             ("can_edit_name", "Может менять имя"),
#             ("can_edit_phone_number", "Может менять номер телефона"),
#         ]
#
#     def __str__(self):
#         return f"{self.name}"
