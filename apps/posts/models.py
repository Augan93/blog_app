from django.db import models
from apps.users.models import BaseModel
from django.contrib.auth.models import User


class Post(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    image = models.ImageField(
        upload_to='%Y-%m-%d/post_images/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


