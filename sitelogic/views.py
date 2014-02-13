from django.shortcuts import render_to_response
from django.template import RequestContext

def view_index(request):
    context = {}

    return render_to_response('sitelogic/index.html', context, context_instance=RequestContext(request))