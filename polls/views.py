from django.shortcuts import render

# Create your views here.
from .models import Question,Choice


def questions(request):
    q = Question.objects.all()
    return render(request, 'polls/questions.html', {'ques': q})


def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    c = Choice.objects.get(question=q)
    return render(request, 'polls/detail.html', {'ques': q, 'opt': c})

def vote(request, question_id):
    question = (Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
