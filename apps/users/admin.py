from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = [
        'first_name',
        'last_name',
        'user__username',
        'user__email',
    ]
    list_display = [
        'user',
        'id',
        'last_name',
        'first_name',
        'middle_name',
    ]
