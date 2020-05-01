from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    deleted = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
    )
    middle_name = models.CharField(
        max_length=100,
        default='',
        verbose_name='Отчество',
        blank=True,
    )
    photo = models.ImageField(
        upload_to='%Y-%m-%d/avatars/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
