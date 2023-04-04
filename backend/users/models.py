from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(max_length=150, unique=True,
                                verbose_name='Логин')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField(max_length=254, unique=True,
                              verbose_name='Электронная почта')
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Аккаунт разрешён'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    @property
    def is_not_active(self):
        return (not self.is_active)
