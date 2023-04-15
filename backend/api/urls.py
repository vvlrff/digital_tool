from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()

router.register('skills', views.SkillsViewSet, basename='skills')
router.register('vacancy', views.VacancyViewSet, basename='vacancy')


urlpatterns = [
    path('', include(router.urls)),
]
