from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext, loader
from django.core.urlresolvers import reverse
from commons_core.models import *
from forms import EditJurisdictionForm, EditApplicationForm
from django.forms import ModelForm


def index(request):
    latest_app_list = App.objects.all
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'latest_app_list': latest_app_list,
    })
    return HttpResponse(t.render(c))


def appindex(request):
    t = loader.get_template('categoryindex.html')
    c = RequestContext(request, {
    })
    return HttpResponse(t.render(c))

def catdetail(request, cat_id):
    app_list = App.objects.all
    t = loader.get_template('category.html')
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
   
def depadd(request, app_id):
    if request.method == 'POST':
        form = DeploymentForm(request.POST)
        if form.is_valid():
            deployment = form.save()
            deployment.app = App.objects.get(pk=app_id)
            deployment.save()
        redirect_to = reverse('deployment_detail', kwargs={'dep_id': deployment.pk})
        return redirect(redirect_to)
    else:
        app = App.objects.get(pk=app_id)
        jurlist = Jurisdiction.objects.all()
        form = DeploymentForm()
        stuff = {
            'app': app,
            'jurisdiction_list': jurlist,
            'form': form,
            }
        return render_to_response("depadd.html", stuff, context_instance=RequestContext(request))
        
def depedit(request, dep_id):
    if request.method == 'POST':
        # save deployment's app
        deployment = Deployment.objects.get(pk=dep_id)
        app = deployment.app
        form = DeploymentForm(request.POST,instance=deployment)
        if form.is_valid():
            deployment = form.save()
            # form doesn't include app, so app will get overwritten as blank.
            # so we add it back here
            deployment.app = app
            deployment.save()
        redirect_to = reverse('deployment_detail', kwargs={'dep_id': deployment.pk})
        return redirect(redirect_to)
    else:
        jurlist = Jurisdiction.objects.all()
        deployment = Deployment.objects.get(pk=dep_id)
        app = deployment.app
        form = DeploymentForm(instance=deployment)
        stuff = {
            'app': app,
            'jurisdiction_list': jurlist,
            'form': form,
            }
        return render_to_response("depadd.html", stuff, context_instance=RequestContext(request))
        
#def detail(request, app_id):
#    return HttpResponse("You're looking at app %s." % app_id)

def appdetail(request, app_id):
    n = App.objects.get(pk=app_id)
    q = request.GET.get('q', n.name)
    results = GoogleSearch.fetch(q)
    return render_to_response("detail.html", {'results':results,'app':n,},
                              context_instance=RequestContext(request))

def app_edit(request, app_id):
    """Form to edit an application"""
    a = App.objects.get(pk=app_id)
    form = EditApplicationForm(instance=a)
    if request.method == 'POST':
        form = EditApplicationForm(request.POST, instance=a)
        if form.is_valid():
            a = form.save()
            redirect_to = reverse('app_edit', kwargs={'app_id': app_id})
            return redirect(redirect_to)
    return render_to_response("app_edit.html",
                              {'app': a,
							   'form': form,},
                              context_instance=RequestContext(request))
# Jurisdictions

def j_index(request):
    j = Jurisdiction.objects.all()
    return render_to_response('j_index.html', {'jurisdiction_list': j},
                              context_instance=RequestContext(request))

def j_detail(request, j_id):
    j = Jurisdiction.objects.get(pk=j_id)
    return render_to_response("j_detail.html",
                              {'jurisdiction':j,},
                              context_instance=RequestContext(request))

def j_edit(request, j_id):
    """Form to edit the Jurisdiction"""
    j = Jurisdiction.objects.get(pk=j_id)
    form = EditJurisdictionForm(instance=j)
    if request.method == 'POST':
        form = EditJurisdictionForm(request.POST, instance=j)
        if form.is_valid():
            j = form.save()
            redirect_to = reverse('jurisdiction_edit', kwargs={'j_id': j_id})
            return redirect(redirect_to)
    return render_to_response("j_edit.html",
                              {'jurisdiction': j,
							   'form': form,},
                              context_instance=RequestContext(request))
