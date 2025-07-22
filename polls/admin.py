from django.contrib import admin
from polls.models import Question, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    search_fields = ('question_text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_filter = ('choice_text',)
    search_fields = ('choice_text',)
