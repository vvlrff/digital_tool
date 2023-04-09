from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    """Админ-панель пользователя."""
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
    )
    fieldsets = (
        ('Default_Fields', {'fields': (
            'username',
            'first_name',
            'last_name'
        )}),
        ('Customs_Fields', {'fields': (
            'role',
            'email'
        )}),
    )
    list_filter = ('email', 'username', 'role')
    search_fields = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
