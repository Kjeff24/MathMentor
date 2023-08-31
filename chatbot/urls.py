from django.urls import path
from .views import predict

urlpatterns = [
    path('course-page/message/predict/', predict, name='predict'),
]