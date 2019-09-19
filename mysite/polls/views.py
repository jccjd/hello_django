from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone
import datetime


#def index(request):
#
#    # there can use HttpResponse return html render is just a easy way
#
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#
#    return render(request, 'polls/index.html', context)
#
#
#
#
#from django.http import Http404
#from django.shortcuts import render, get_object_or_404
#def detail(request, question_id):
#
##    try:
##        question = Question.objects.get(pk=question_id)
##    except Question.DoesNotExist:
##        raise Http404("Question does not exist")
##    return render(request, 'polls/detail.html', {'question': question})
#
##    respose = "you look at the results %s."
##    return HttpResponse(respose % question_id)
#
#    #  get_object_or_404 still is a easy way to use return body and not use try except
#
#
#    question = get_object_or_404(Question, pk=question_id)
#
#    return render(request, 'polls/detail.html', {'question': question})
#
#
#def results(request, question_id):
#
#
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})
#
#   # return HttpResponse("you voting on question %s" % question_id)
#
#from django.urls import reverse
#from django.http import HttpResponseRedirect
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "you didn`t select_a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #return HttpResponse("you voting on Questions %s." % question_id)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It`is now %s.</body></html>" % now
    return HttpResponse(html)


