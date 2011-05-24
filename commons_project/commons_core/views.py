from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext, loader
from commons_core.models import *

def index(request):
    latest_app_list = App.objects.all
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'latest_app_list': latest_app_list,
    })
    return HttpResponse(t.render(c))


def appindex(request):
    app_list = App.objects.all
    t = loader.get_template('appindex.html')
    c = RequestContext(request, {
        'app_list': app_list,
    })
    return HttpResponse(t.render(c))

def depindex(request):
    dep_list = Deployment.objects.all
    t = loader.get_template('depindex.html')
    c = RequestContext(request, {
        'dep_list': dep_list,
    })
    return HttpResponse(t.render(c))

def depdetail(request, dep_id):
    n = Deployment.objects.get(pk=dep_id)
    return render_to_response("depdetail.html", {'dep':n }, context_instance=RequestContext(request))
   

#def detail(request, app_id):
#    return HttpResponse("You're looking at app %s." % app_id)

def detail(request, app_id):
    n = App.objects.get(pk=app_id)
    q = request.GET.get('q', n.name)
    jxs = Deployment.objects.filter(app=app_id)
    results = GoogleSearch.fetch(q)
    return render_to_response("detail.html", {'results':results,'app':n, 'jurisdictions':jxs}, context_instance=RequestContext(request))

# Jurisdictions

def j_index(request):
    j = Jurisdiction.objects.all()
    return render_to_response('templates/j_index.html', {'jurisdiction_list': j},
                             context_instance=RequestContext(request))

def j_detail(request, j_id):
    j = Jurisdiction.objects.get(pk=j_id)
    return render_to_response("templates/j_detail.html",
                              {'jurisdiction':j,},
                              context_instance=RequestContext(request))
