from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    '''Admin View for Choices'''

    list_display = ('choice','is_answer')


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    '''Admin View for Questions'''

    list_display = ('questions','question_type')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    '''Admin View for Answer'''

    list_display = ('answer','answer_to')


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    '''Admin View for Form'''

    list_display = ('form','code')

@admin.register(Responses)
class ResponsesAdmin(admin.ModelAdmin):
    '''Admin View for Responses'''

    list_display = ('response_to','response_code','responder')

    