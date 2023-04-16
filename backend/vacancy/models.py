from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Skills(models.Model):
    """Модель навыков."""

    name = models.CharField(
        verbose_name='Название навыка',
        max_length=100
    )

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Busyness(models.Model):
    """Модель типа занятости."""

    name = models.CharField(
        verbose_name='Тип занятости',
        max_length=100
    )

    class Meta:
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель вакансий."""

    author = models.ForeignKey(
        User,
        verbose_name='Автор вакансии',
        on_delete=models.CASCADE,
        related_name='vacancy'
    )
    company_name = models.CharField(
        'Название компании',
        max_length=200,
        help_text='Введите название компании',
    )
    name = models.CharField(
        'Название вакансии',
        max_length=200,
        help_text='Введите название вакансии',
    )
    text = models.TextField(
        verbose_name='Описание вакансии',
        help_text='Текстовое описание вакансии'
    )
    skills = models.ManyToManyField(
        Skills,
        related_name='skills',
        verbose_name='Навыки'
    )
    salary = models.PositiveIntegerField(
        verbose_name='Размер заработной платы',
        help_text='Введите размер заработной платы',
        validators=[
            MinValueValidator(1)]
    )
    busyness = models.ManyToManyField(
        Busyness,
        related_name='vacancy',
        verbose_name='Тип занятости'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-pub_date']


class Favorite(models.Model):
    """Модель избранных вакансий."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Автор'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Избранная вакансия'
    )

    class Meta:
        verbose_name = 'Избранная вакансия'
        verbose_name_plural = 'Избранные вакансии'
        ordering = ['author']
