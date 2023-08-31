from django.shortcuts import render, redirect
from myapp.models import User
from course.models import Quiz, Course


def learnerHome(request):
    
    return render(request, "learning_styles/learner_home.html")



def classForm(request):
    user = request.user
    if request.method == 'POST':
        
        class_level = request.POST.get('class_level')
        math_grade = request.POST.get('math_grade')
        math_strength = request.POST.get('math_strength')
        
        # Update the fields of the user object
        user.class_level = class_level
        user.math_grade = math_grade
        user.math_strength = math_strength
        
        # Save the changes
        user.save()
        return redirect('quiz_list_view', course="LEARNING STYLE")
    return render(request, "learning_styles/class_form.html")

