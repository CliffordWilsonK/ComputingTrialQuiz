from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(pk=int(selected))
                if choice.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {
            'score': score, 'total': total, 'quiz': quiz
        })

    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': questions})
