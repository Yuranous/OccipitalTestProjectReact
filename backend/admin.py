from django.contrib import admin

from backend.models import Task, Translator, Reviewer

admin.site.register([Task, Translator, Reviewer])
