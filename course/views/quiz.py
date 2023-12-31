from django.shortcuts import render, redirect
from django.http import JsonResponse
from course.models import Quiz, Question, Answer, Result
from course.models import Course
from django.db.models import F, Q, Count
from myapp.models import User


def quiz_list_view(request, course):
    user = request.user
    course = Course.objects.get(name=course)
    # Filter quizzes that the user has not attempted more than quiz_chances times
    quizzes = Quiz.objects.filter(
        course=course
    ).annotate(
        result_count=Count('result', filter=Q(result__user=request.user))
    ).filter(
        result_count__lt=F('quiz_chances')
    )
    
    if not quizzes.exists():
        user.has_preference = True
        user.save()
        return redirect('dashboard')
    else:
        filtered_quizzes = []
        for quiz in quizzes:
            if quiz.question_set.exists():  # Check if the quiz has questions
                filtered_quizzes.append(quiz)
        
        context = {
            'quizzes': filtered_quizzes,
            'course': course,
        }
        
        return render(request, 'learning_styles/quiz_list.html', context)


def quiz_view(request, pk, course):
    quiz = Quiz.objects.get(pk=pk)
    course = Course.objects.get(name=course)
    
    context = {'obj': quiz, 'course': course, 'page':'quiz_page' }
    return render(request, 'learning_styles/quiz.html', context)
    


def get_data_view(request, pk, course):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk, course):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        
        # save completion time from response data
        completionTime = float(data_["completionTime"][0])

        # remove csrfmiddlewaretoken and completionTime, and returns the list of questions
        data_.pop('csrfmiddlewaretoken')
        data_.pop('completionTime')

        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        save_result = Result.objects.create(quiz=quiz, user=user, score=score_, completion_time=completionTime)
        save_result.save()
        
        if score_ >= quiz.required_score_to_pass:
            if quiz.name == "Reading/Writing Learner":
                user.is_read_write_learner = True
            if quiz.name == "Kinesthetic Learner":
                user.is_kinesthetic_learner = True
            if quiz.name == "Auditory Learner":
                user.is_auditory_learner = True
            if quiz.name == "Visual Learner":
                user.is_visual_learner = True
            user.save()
                
            

        return redirect('quiz_list_view', course="LEARNING STYLE")
        