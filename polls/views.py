from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .models import Question, Choice


def questions(request):
    q = Question.objects.all()
    return render(request, 'polls/questions.html', {'ques': q})


def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    c = Choice.objects.filter(question=q)
    return render(request, 'polls/detail.html', {'ques': q, 'opt': c})


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = Choice.objects.get(question=question, pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'ques': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print(selected_choice)
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return redirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    q = Question.objects.get(pk=question_id)
    c = Choice.objects.filter(question=q)
    return render(request, 'polls/results.html', {'question': q, 'choices': c})
