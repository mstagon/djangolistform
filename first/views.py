from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from django import forms
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'first/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'first/question_detail.html', context)

def answer_create(request, question_id):
    """
     first 답변등록
     """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('first:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'first/question_detail.html', context)

def question_create(request):
    form = QuestionForm()
    return render(request, 'first/question_form.html', {'form': form})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('first:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'first/question_form.html', context)

