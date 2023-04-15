from django.urls import include, path

from .views.admin import (AdminPolls, AdminPollById,
                          AdminQuestions, AdminQuestionById)
from .views.user import Polls, PollById, PollsByUser

app_name = 'tests'

urlpatterns = [
    path('polls/', Polls.as_view()),
    path('polls/<int:id>', PollById.as_view()),
    path('pollsByUser/<int:id>', PollsByUser.as_view()),
    path('admin/', include([
        path('polls/', AdminPolls.as_view()),
        path('polls/<int:id>/', AdminPollById.as_view()),
        path('polls/<int:id>/questions/', AdminQuestions.as_view()),
        path('polls/<int:pollId>/questions/<int:questionId>/', AdminQuestionById.as_view())
    ]))
]
