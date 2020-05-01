from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'text',
        'author__username',
        'author__email',
    ]
    list_display = [
        'author',
        'id',
        'title',
        'text',
        'image',
        'is_active',
    ]
