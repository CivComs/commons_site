from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from commons.models import App

def index(request):
    latest_app_list = App.objects.all
    t = loader.get_template('index.html')
    c = Context({
        'latest_app_list': latest_app_list,
    })
    return HttpResponse(t.render(c))


def detail(request, app_id):
    return HttpResponse("You're looking at app %s." % app_id)
