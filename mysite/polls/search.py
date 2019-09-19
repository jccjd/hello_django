from django.http import HttpResponse
from django.shortcuts import render_to_response


def search_from(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'message is ---->' + request.GET['q']

    else:
        message = 'input form'

    return HttpResponse(message)


