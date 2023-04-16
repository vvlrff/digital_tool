from django.db import models


class Poll(models.Model):
    """Тест"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    startDate = models.DateField()
    finishDate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'


class Question(models.Model):
    """Вопрос"""
    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    max_points = models.FloatField()

    class Meta:
        verbose_name = 'Вопрос'

    def __str__(self):
        return self.text


class Option(models.Model):
    """Вариант ответа"""
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    text = models.CharField(max_length=100)
    points = models.FloatField()

    class Meta:
        verbose_name = 'Вариант ответа'

    def __str__(self):
        return self.text


class Submission(models.Model):
    """Заполненный опрос"""
    user_id = models.IntegerField(db_index=True)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    submitTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заполненный опрос'


class Answer(models.Model):
    """Ответ на вопрос"""
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice = models.ForeignKey('Option', on_delete=models.CASCADE,
                               null=True, default=1)

    class Meta:
        verbose_name = 'Ответ на вопрос'
