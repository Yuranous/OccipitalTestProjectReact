import logging

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from backend.models import Task, Commentary
from backend.serializers import TaskListSerializer, TaskSerializer, TranslationAddSerializer


class TaskListView(ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()


class TaskForTranslationView(ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.filter(status=Task.Status.CREATED)


class TaskForReviewView(ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.filter(status=Task.Status.WAITING_REVIEW)


class TaskView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskOnTranslationView(APIView):
    def get(self, request, pk, **kwargs):
        try:
            logging.debug(f'Статус задачи по ключу {pk} будет изменен на ON_TRANSLATION')
            task = Task.objects.get(pk=pk)
            task.change_status_to_on_translation()
            task.translator = request.user.translator
            task.save()
            return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class TaskToReviewView(APIView):
    def get(self, request, pk, **kwargs):
        try:
            logging.debug(f'Статус задачи по ключу {pk} будет изменен на WAITING_REVIEW')
            task = Task.objects.get(pk=pk)
            task.change_status_to_waiting_review()
            task.save()
            return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class TaskOnReviewView(APIView):
    def get(self, request, pk, **kwargs):
        try:
            logging.debug(f'Статус задачи по ключу {pk} будет изменен на ON_REVIEW')
            task = Task.objects.get(pk=pk)
            task.change_status_to_on_review()
            task.reviewer = request.user.reviewer
            task.save()
            return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class TaskOnReTranslationView(APIView):
    def get(self, request, pk, **kwargs):
        try:
            logging.debug(f'Статус задачи по ключу {pk} будет изменен на ON_RE_TRANSLATION')
            task = Task.objects.get(pk=pk)
            task.change_status_to_on_re_translation()
            task.save()
            return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class TaskDoneView(APIView):
    def get(self, request, pk, **kwargs):
        try:
            logging.debug(f'Статус задачи по ключу {pk} будет изменен на DONE')
            task = Task.objects.get(pk=pk)
            task.change_status_to_done()
            task.save()
            return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class TranslationAddView(UpdateAPIView):
    serializer_class = TranslationAddSerializer

    def put(self, request, **kwargs):
        try:
            serializer = TranslationAddSerializer(data=request.data)
            if serializer.is_valid():
                task = Task.objects.get(pk=serializer.data['task_id'])
                task.translation = serializer.data['translation']
                task.save()
                return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)


class CommentaryAddView(UpdateAPIView):
    serializer_class = TranslationAddSerializer

    def put(self, request, **kwargs):
        try:
            serializer = TranslationAddSerializer(data=request.data)
            if serializer.is_valid():
                task = Task.objects.get(pk=serializer.data['task_id'])
                task.commentary_set.add(Commentary(serializer.data['commentary']))
                task.save()
                return Response({'result': 'OK'}, HTTP_200_OK)
        except:
            return Response({'result': 'Failed'}, HTTP_401_UNAUTHORIZED)
