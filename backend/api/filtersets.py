from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import (AllValuesMultipleFilter,
                                                   BooleanFilter, CharFilter,
                                                   ModelChoiceFilter)
from vacancy.models import Skills, Vacancy
from users.models import User


class SkillsSearchFilter(FilterSet):
    """Фильтрсет навыков."""
    name = CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Skills
        fields = ('name',)


class VacancySearchFilter(FilterSet):
    """Фильтрсет вакансий."""
    is_favorited = BooleanFilter(method='filter_is_favorited')
    tags = AllValuesMultipleFilter(field_name='tags__slug')
    author = ModelChoiceFilter(queryset=User.objects.all())

    def filter_is_favorited(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(favorite__author=user)
        return queryset

    class Meta:
        model = Vacancy
        fields = [
            'tags__slug',
            'author',
            'is_favorited',
        ]
