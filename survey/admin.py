from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Survey)
admin.site.register(SurveyQuestions)
admin.site.register(UserAnswers)
