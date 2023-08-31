from django.shortcuts import render, redirect
from myapp.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from myapp.forms import UserForm
from datetime import datetime
from django.utils import timezone
from course.models import Course, Resource
from myapp.models import User
from urllib.parse import urlencode
from django.http import StreamingHttpResponse

def dashboard(request):
    current_time = timezone.now()
    context = {
        'current_time': current_time
    }
    return render(request, "course_page/dashboard.html", context)


def courses(request, pk):
    
    current_time = timezone.now()
    user = User.objects.get(id=pk)
    courses = Course.objects.filter(class_level=user.class_level)
    context = {
        'courses':courses,
        'current_time': current_time
    }
    return render(request, "course_page/courses.html", context)

def chatMessage(request):
    context ={
    'page': 'chat-message'
    }
    return render(request, "course_page/message.html", context)


def passQuestions(request, pk):
    current_time = timezone.now()
    user = User.objects.get(id=pk)
    courses = Course.objects.filter(class_level=user.class_level)
    resources = Resource.objects.filter(course__in=courses)
    
    context = {
        'pdf_files':resources,
        'current_time': current_time
    }
    
    return render(request, "course_page/pass_questions.html", context)


# Preview pdf
def previewPdf(request, pk):
    file = Resource.objects.get(id=pk)
    # pdf is streamed in chunks, rather than loading entire file
    def file_iterator():
        with open(file.file.path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                yield chunk
    # use StreamingHttpResponse to load pdf content
    response = StreamingHttpResponse(
        file_iterator(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(
        urlencode({'': file.file.name}))
    return response


def updateProfile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('update-profile', pk=user.id)
    else:
        form = UserForm(instance=user, user=request.user)

    context = {'form':form, 'page':'update'}
    
    return render(request, "course_page/update_profile.html", context)