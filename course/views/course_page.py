from django.shortcuts import render, redirect
from myapp.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from myapp.forms import UserForm
from datetime import datetime
from django.utils import timezone

def dashboard(request):
    current_time = timezone.now()
    context = {
        'current_time': current_time
    }
    return render(request, "course_page/dashboard.html", context)


def courses(request):
    
    return render(request, "course_page/courses.html")

def chatMessage(request):
    
    return render(request, "course_page/message.html")


def passQuestions(request):
    
    return render(request, "course_page/pass_questions.html")


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