from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from commons_core.models import App
from commons_core.models import *

def index(request):
    latest_app_list = App.objects.all
    t = loader.get_template('index.html')
    c = Context({
        'latest_app_list': latest_app_list,
    })
    return HttpResponse(t.render(c))



#def detail(request, app_id):
#    return HttpResponse("You're looking at app %s." % app_id)

def detail(request, app_id):
    n = App.objects.get(pk=app_id)
    q = request.GET.get('q', n.name)
    jxs = Deployment.objects.filter(app=app_id)
    results = GoogleSearch.fetch(q)
    return render_to_response("detail.html", {'results':results,'app':n, 'jurisdictions':jxs})