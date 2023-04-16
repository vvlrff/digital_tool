from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import Http404
from datetime import date

from .models import Poll, Submission, Answer, Option
from .serializers import (TestSerializer, QuestionSerializer,
                          UserOptionSerializer, SubmissionSerializer)


class Tests(APIView):
    def get(self, request):
        today = date.today()
        pollSet = Poll.objects.filter(startDate__lte=today,
                                      finishDate__gt=today)
        return Response(TestSerializer(pollSet, many=True).data)


class WriteInfoTest(APIView):
    def get(self, request, id):
        try:
            today = date.today()
            poll = Poll.objects.get(id=id)
            if poll.startDate > today or poll.finishDate < today:
                raise Poll.DoesNotExist()

            result = TestSerializer(poll).data
            result['questions'] = []
            for question in poll.question_set.all():
                questionDict = QuestionSerializer(question).data
                questionDict['options'] = UserOptionSerializer(
                            question.option_set.all(), many=True).data
                result['questions'].append(questionDict)

            return Response(result)

        except Poll.DoesNotExist:
            raise Http404()
        except Exception as ex:
            raise ParseError(ex)

    def post(self, request, id):
        try:
            poll = Poll.objects.get(id=id)
            user_id = request.data['user_id']

            def makeAnswer(question):
                answer = Answer(
                    question=question
                    )
                return answer

            answerList = [makeAnswer(question) for question in
                          poll.question_set.all()]
            if len(answerList) != poll.question_set.count():
                raise Exception('Not enough answers')

            submis = Submission(user_id=user_id, poll=poll)
            submis.save()
            for answer in answerList:
                answer.submission = submis
                answer.choice = Option(id=id)
                answer.save()

            return Response('Ответ принят')

        except Poll.DoesNotExist:
            raise Http404()
        except Exception as ex:
            raise ParseError(ex)


class ResultTest(APIView):
    def get(self, request, id):
        try:
            result = []
            for submission in Submission.objects.filter(
                                        user_id=id).order_by('submitTime'):
                submissionDict = SubmissionSerializer(submission).data
                submissionDict['poll_id'] = submission.poll_id
                submissionDict['answers'] = []
                for answer in submission.answer_set.all():
                    submissionDict['answers'].append({
                        'question': {
                            'id': answer.question_id,
                            'text': answer.question.text,
                        },
                        'answer': answer.choice.text,
                        'points': answer.choice.points
                    })

                result.append(submissionDict)
            return Response(result)

        except Exception as ex:
            raise ParseError(ex)
