from django.urls import path
from .views import learning_styles, quiz


urlpatterns = [
    path('learner_home/', learning_styles.learnerHome, name='learner-home'),
    path('learner_home/class-form/', learning_styles.classForm, name='class-form'),
    path('learner_home/quiz/<course>/', quiz.quiz_list_view, name='quiz_list_view'),
    path('learner_home/quiz/<course>/<pk>/', quiz.quiz_view, name='quiz_view'),
    path('learner_home/quiz/<course>/<pk>/data/', quiz.get_data_view, name='quiz_view'),
    path('learner_home/quiz/<course>/<pk>/save/', quiz.save_quiz_view, name='save-view'),
    # path('learner_home/quiz/<class_level>/save/', quiz.save_quiz_view, name='save-view'),
]