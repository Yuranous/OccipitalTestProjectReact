from django.contrib.auth.models import AbstractUser, User
from django.db import models


# class User(AbstractUser):
#     username = models.CharField(max_length=25, unique=True)
#     is_translator = models.BooleanField('translator status', default=False)
#     is_reviewer = models.BooleanField('reviewer status', default=False)


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True,
                                verbose_name='reviewer')


class Translator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True,
                                verbose_name='translator')


class Task(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 1
        ON_TRANSLATION = 2
        WAITING_REVIEW = 3
        ON_REVIEW = 4
        ON_RE_TRANSLATION = 5
        DONE = 6

    name = models.CharField(max_length=100)
    translation = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.CREATED, blank=True)

    created = models.DateField(auto_now_add=True, blank=True)
    deadline = models.DateField()

    translator = models.ForeignKey('Translator', blank=True, null=True, on_delete=models.PROTECT)
    text = models.TextField()

    reviewer = models.ForeignKey('Reviewer', blank=True, null=True, on_delete=models.PROTECT)

    def change_status_to_on_translation(self):
        self.status = self.Status.ON_TRANSLATION

    def change_status_to_waiting_review(self):
        self.status = self.Status.WAITING_REVIEW

    def change_status_to_on_review(self):
        self.status = self.Status.ON_REVIEW

    def change_status_to_on_re_translation(self):
        self.status = self.Status.ON_RE_TRANSLATION

    def change_status_to_done(self):
        self.status = self.Status.DONE


class Commentary(models.Model):
    text = models.TextField()
    task = models.ForeignKey('Task', verbose_name='commentaries', on_delete=models.CASCADE)
