from django.db import models
import django_pipes
#defines the data models for the application
#for anything that we need to store data about.

class App(models.Model):
    name = models.TextField()
    ssid = models.IntegerField(default=0)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Jurisdiction(models.Model):
    name = models.TextField()
    ssid = models.IntegerField(default=0)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Deployment(models.Model):
    name = models.TextField()
    description = models.TextField()
    jurisdiction = models.ForeignKey(Jurisdiction)
    app = models.ForeignKey(App)

    def __unicode__(self):
        return self.name

# Create your models here.
class GoogleSearch(django_pipes.Pipe):
    uri = "http://ajax.googleapis.com/ajax/services/search/web"

    @staticmethod
    def fetch(q):
        resp = GoogleSearch.objects.get({'v':1.0, 'q':q})
        if resp and hasattr(resp, "responseData") and hasattr(resp.responseData, "results"):
            return resp.responseData.results