# Generated by Django 4.2.2 on 2024-08-29 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_servicescatalog"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="avatar",
        ),
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Token"
            ),
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя клиента")),
                (
                    "phone_number",
                    models.CharField(
                        max_length=21, verbose_name="Номер телефона клиента"
                    ),
                ),
                (
                    "name_service",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="catalog.services",
                        verbose_name="Название услуги",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        help_text="Укажите пользователя",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Пользователь",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись на прием",
                "verbose_name_plural": "Записи на прием",
                "permissions": [
                    ("can_edit_name", "Может менять имя"),
                    ("can_edit_phone_number", "Может менять номер телефона"),
                ],
            },
        ),
    ]
