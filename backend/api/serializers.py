from vacancy.models import (Busyness, Favorite, Skills,
                            Vacancy)
from rest_framework import serializers
from users.serializers import UserSerializer


class SkillsSerializer(serializers.ModelSerializer):
    """Сериализатор навыков."""
    class Meta:
        model = Skills
        fields = ('id', 'name',)

    def __str__(self):
        return self.name


class BusynessSerializer(serializers.ModelSerializer):
    """Сериализатор навыков."""
    class Meta:
        model = Busyness
        fields = ('id', 'name',)

    def __str__(self):
        return self.name


class VacancyViewSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра вакансий."""
    author = UserSerializer(read_only=True)
    skills = SkillsSerializer(
        many=True,
        read_only=True
    )
    busyness = BusynessSerializer(
        many=True,
        read_only=True
    )
    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = '__all__'

    def __str__(self):
        return self.name

    def get_is_favorited(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return Favorite.objects.filter(
            author=user,
            vacancy=obj
        ).exists()


class VacancyWriteSerializer(serializers.ModelSerializer):
    """Сериализатор добавления/обновления вакансий."""
    skills = serializers.PrimaryKeyRelatedField(
        queryset=Skills.objects.all(),
        many=True
    )
    busyness = serializers.PrimaryKeyRelatedField(
        queryset=Busyness.objects.all(),
        many=True
    )

    class Meta:
        model = Vacancy
        fields = (
            'skills', 'busyness',
            'name', 'text', 'salary',
            'company_name'
        )

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(
            author=self.context.get('request').user,
            company_name=validated_data.pop('company_name'),
            name=validated_data.pop('name'),
            text=validated_data.pop('text'),
            salary=validated_data.pop('salary')
        )
        busyness = validated_data.pop('busyness')
        vacancy.busyness.set(busyness)
        skills = validated_data.pop('skills')
        vacancy.skills.set(skills)
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.salary = validated_data.get(
            'salary', instance.salary
        )
        busyness = validated_data.pop('busyness')
        instance.busyness.set(busyness)
        skills = validated_data.pop('skills')
        instance.skills.set(skills)
        instance.save()
        return instance


class VacancyInListSerializer(serializers.ModelSerializer):
    """Сериализатор вакансий в списке."""
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'salary',)


class FavoriteSerializer(VacancyInListSerializer):
    """Сериализатор избранных вакансий."""
    class Meta:
        model = Favorite
        fields = ('author', 'vacancy')

    def validate(self, data):
        author = data['author']
        vacancy = data['vacancy']
        action = self.context['action']
        vacancy_in_favorites = Favorite.objects.filter(
            vacancy=vacancy,
            author=author
        )
        if action == 'remove':
            if not vacancy_in_favorites:
                raise serializers.ValidationError(
                    detail='Данной вакансии нет в избранном.')
            vacancy_in_favorites.delete()
        elif action == 'add':
            if vacancy_in_favorites:
                raise serializers.ValidationError(
                    detail='Вакансия уже добавлена в избранное.')
        return data
