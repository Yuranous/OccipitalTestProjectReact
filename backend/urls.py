from django.urls import path

from backend.views import TaskListView, TaskView, TaskOnTranslationView, TaskToReviewView, TaskOnReviewView, \
    TaskOnReTranslationView, TaskDoneView, TranslationAddView, CommentaryAddView

urlpatterns = [
    path('task/list/', TaskListView.as_view()),

    path('task/<int:pk>/', TaskView.as_view()),
    path('task/<int:pk>/translate/', TaskOnTranslationView.as_view()),
    path('task/<int:pk>/to-review/', TaskToReviewView.as_view()),
    path('task/<int:pk>/re-translate/', TaskOnReTranslationView.as_view()),
    path('task/<int:pk>/review/', TaskOnReviewView.as_view()),
    path('task/<int:pk>/done/', TaskDoneView.as_view()),

    path('task/translation/', TranslationAddView.as_view()),
    path('task/commentary/', CommentaryAddView.as_view()),

]
