from django.db import models


class Services(models.Model):
    service_name = models.CharField(max_length=300, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["service_name", "price"]
        permissions = [
            ("can_edit_price", "Может менять цену"),
            ("can_edit_description", "Может менять описание")
        ]

    def __str__(self):
        return f"{self.service_name}"


class Description(models.Model):
    description_title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, verbose_name="Описание")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"
        permissions = [
            ("can_edit_description_title", "Может менять заголовок"),
            ("can_edit_description", "Может менять описание"),
        ]

    def __str__(self):
        return f"{self.description_title}"


class ServicesCatalog(models.Model):

    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Название услуги", default=None)

    class Meta:
        verbose_name = "Услуга из каталога"
        verbose_name_plural = "Услуги из каталога"

    def __str__(self):
        return f"{self.service}"
