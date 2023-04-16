from django.urls import path

from .views import Tests, WriteInfoTest, ResultTest

app_name = 'tests'

urlpatterns = [
    path('tests/', Tests.as_view()),
    path('tests/<int:id>/', WriteInfoTest.as_view()),
    path('employer/tests/<int:id>/', ResultTest.as_view()),
]
