from django.contrib import admin
from vacancy.models import (Busyness, Favorite, Skills,
                            Vacancy,)


class SkillsAdmin(admin.ModelAdmin):
    """Админ-панель навыков."""
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class VacancyAdmin(admin.ModelAdmin):
    """Админ-панель вакансий."""
    list_display = ('author', 'name', 'favorites')
    search_fields = ('author',)
    list_filter = ('author', 'name')
    empty_value_display = '-пусто-'

    def favorites(self, obj):
        favorite = Favorite.objects.filter(vacancy=obj)
        return favorite.count()


class BusynessAdmin(admin.ModelAdmin):
    """Админ-панель типа занятости."""
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    """Админ-панель избранных вакансий."""
    list_display = ('author', 'vacancy')
    empty_value_display = '-пусто-'


admin.site.register(Busyness, BusynessAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Vacancy, VacancyAdmin)
