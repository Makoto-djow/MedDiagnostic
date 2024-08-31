from django.db import models

NULLABLE = {"blank": True, "null": True}


class Doctors(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, **NULLABLE, verbose_name="Отчество (если есть)")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    specialization = models.CharField(max_length=250, verbose_name="Специализация")
    photo = models.ImageField(upload_to="description_media/photo", **NULLABLE, verbose_name="Фотография")

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ("lastname",)
        permissions = [
            ("can_edit_specialization", "Может менять специализацию"),
            ("can_edit_photo", "Может менять фото"),
            ("can_edit_description", "Может менять описание")
        ]

    def __str__(self):
        return f"{self.name}, {self.lastname}, {self.patronymic}"


class Company(models.Model):
    heading = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    image = models.ImageField(upload_to="description_media/image", verbose_name="Картинка")

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описания"
        permissions = [
            ("can_edit_heading", "Может менять заголовок"),
            ("can_edit_description", "Может менять описание"),
            ("can_edit_image", "Может менять картинку")
        ]

    def __str__(self):
        return f"{self.heading}"


