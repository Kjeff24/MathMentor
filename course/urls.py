from django.urls import path
from .views import learning_styles, quiz, course_page


urlpatterns = [
    path('learner_home/', learning_styles.learnerHome, name='learner-home'),
    path('learner_home/class-form/', learning_styles.classForm, name='class-form'),
    path('learner_home/quiz/<course>/', quiz.quiz_list_view, name='quiz_list_view'),
    path('learner_home/quiz/<course>/<pk>/', quiz.quiz_view, name='quiz_view'),
    path('learner_home/quiz/<course>/<pk>/data/', quiz.get_data_view, name='quiz_view'),
    path('learner_home/quiz/<course>/<pk>/save/', quiz.save_quiz_view, name='save-view'),
    path('course-page/dashboard', course_page.dashboard, name='dashboard'),
    path('course-page/courses/<pk>/', course_page.courses, name='courses'),
    path('course-page/courses/lesson-plan/<pk>/', course_page.lessonPlan, name='lesson-plan'),
    path('course-page/courses/programme/<pk>/', course_page.courseContent, name='course-content'),
    path('course-page/message/', course_page.chatMessage, name='chat-message'),
    path('course-page/past-question/<pk>/', course_page.passQuestions, name='past-questions'),
    path('course-page/past-question/preview_pdf/<int:pk>/', course_page.previewPdf, name='preview_pdf'),
    path('course-page/update-profile/<pk>', course_page.updateProfile, name='update-profile'),
]