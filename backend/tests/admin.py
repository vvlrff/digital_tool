from django.contrib import admin
from .models import Question, Answer, Poll, Option, Submission


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'poll',
        'text',
        'max_points',
    )


class PollAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'startDate',
        'finishDate',
    )


class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'index',
        'text',
        'points',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'submission',
        'question',
        'choice',
    )
    list_filter = ('submission',)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'poll',
        'submitTime',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Answer, AnswerAdmin)
