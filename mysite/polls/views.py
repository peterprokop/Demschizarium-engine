from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll
from django.http import Http404

#from django.template import Context, loader
from mysite.polls.models import Poll
#from django.http import HttpResponse

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/poll_detail.html', {
            'object': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
