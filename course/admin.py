from django.contrib import admin
from .models import Question, Answer, Quiz, Result, Course


# Display answers in tabular format in question
class AnswerInline(admin.TabularInline):
    """
    Admin inline class for displaying answers in tabular format within a question.
    """
    model = Answer
    

class QuestionAdmin(admin.ModelAdmin):
    """
    Admin model class for configuring the display of Question model in the admin interface.
    """
    inlines = [AnswerInline]
    
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)
admin.site.register(Course)