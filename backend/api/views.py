from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from vacancy.models import Skills, Vacancy, Tag
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filtersets import SkillsSearchFilter, VacancySearchFilter
from .paginator import SixPagination
from .permissions import IsApplicantOrReadOnly
from .serializers import (FavoriteSerializer, SkillsSerializer,
                          VacancyInListSerializer, VacancyViewSerializer,
                          VacancyWriteSerializer,
                          TagSerializer)


class TagViewSet(ReadOnlyModelViewSet):
    """API тэгов."""
    queryset = Tag.objects.all()
    pagination_class = None
    serializer_class = TagSerializer


class SkillsViewSet(ReadOnlyModelViewSet):
    """API навыков."""
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SkillsSearchFilter


class VacancyViewSet(viewsets.ModelViewSet):
    """API вакансий"""
    queryset = Vacancy.objects.all().order_by('-id')
    permission_classes = (IsApplicantOrReadOnly,)
    pagination_class = SixPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancySearchFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return VacancyViewSerializer
        return VacancyWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def add_to_list(self, author, vacancy, serializer):
        serializer = serializer(
            data={'author': author.id, 'vacancy': vacancy.id},
            context={'action': 'add'}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(vacancy=vacancy, author=author)
        response_serializer = VacancyInListSerializer(vacancy)
        return Response(
            data=response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def remove_from_list(self, author, vacancy, serializer):
        serializer = serializer(
            data={'author': author.id, 'vacancy': vacancy.id},
            context={'action': 'remove'}
        )
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[IsAuthenticated]
    )
    def favorite(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        if request.method == 'POST':
            return self.add_to_list(
                request.user,
                vacancy,
                FavoriteSerializer
            )
        return self.remove_from_list(
            request.user,
            vacancy,
            FavoriteSerializer
        )
