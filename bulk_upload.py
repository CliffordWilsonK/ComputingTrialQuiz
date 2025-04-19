import django
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizzy.settings")
django.setup()

from quiz.models import Quiz, Question, Choice

def upload_questions():
    with open('data/questions_data.json') as file:
        questions_data = json.load(file)

    for item in questions_data:
        quiz, _ = Quiz.objects.get_or_create(title=item["topic"])
        question = Question.objects.create(quiz=quiz, question_text=item["text"])

        for option in item["options"]:
            is_correct = (option.strip().lower() == item["answer"].strip().lower())
            Choice.objects.create(question=question, choice_text=option, is_correct=is_correct)

    print("Bulk upload complete!")

if __name__ == "__main__":
    upload_questions()
