from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """Модель пользователя."""
    EMPLOYER = 'employer'
    APPLICANT = 'applicant'

    ROLE = (
        (APPLICANT, 'Соискатель'),
        (EMPLOYER, 'Работодатель'),
    )
    role = models.CharField('Роль',
                            max_length=35,
                            choices=ROLE,
                            default=APPLICANT
                            )
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

    @property
    def is_employer(self):
        return self.role == self.EMPLOYER

    @property
    def is_applicant(self):
        return self.role == self.APPLICANT


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
