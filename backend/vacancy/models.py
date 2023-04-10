from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Tag(models.Model):
    """Модель тэгов."""

    name = models.CharField(
        verbose_name='Название тега',
        max_length=50,
        unique=True
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код тега',
        max_length=8,
        unique=True
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug тега'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


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
    tags = models.ManyToManyField(
        Tag,
        related_name='vacancy',
        verbose_name='Теги вакансии'
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
