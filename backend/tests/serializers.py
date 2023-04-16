from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    """Тест"""
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    startDate = serializers.DateField()
    finishDate = serializers.DateField()


class QuestionSerializer(serializers.Serializer):
    """Вопрос"""
    id = serializers.IntegerField(required=False)
    text = serializers.CharField(max_length=300)
    max_points = serializers.FloatField()


class OptionSerializer(serializers.Serializer):
    """Вариант ответа"""
    id = serializers.IntegerField(required=False)
    index = serializers.IntegerField(required=False)
    text = serializers.CharField(max_length=100)
    points = serializers.FloatField()


class UserOptionSerializer(serializers.Serializer):
    """Вариант ответа для пользователя"""
    index = serializers.IntegerField()
    text = serializers.CharField(max_length=100)
    points = serializers.FloatField()


class SubmissionSerializer(serializers.Serializer):
    """Заполненный опрос"""
    id = serializers.IntegerField()
    submitTime = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')
