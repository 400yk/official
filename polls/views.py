from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by("-pub_date")[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list' : latest_poll_list,
        })

    return HttpResponse(template.render(context))
    # A shortcut: 
    #context = {'latest_poll_list' : latest_poll_list}
    #return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll' : poll})
    #return HttpResponse("Detail: %s" %poll_id)

    # A shortcut:
    #poll = get_object_or_404(Poll, pk = poll_id)
    #return ...

def results(request, poll_id):
    return HttpResponse("Results: %s" %poll_id)

def vote(request, poll_id):
    return HttpResponse("Votings: %s" %poll_id)


