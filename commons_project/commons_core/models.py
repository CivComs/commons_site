from django.db import models
import django_pipes
#defines the data models for the application
#for anything that we need to store data about.

class App(models.Model):
    name = models.TextField()
# Must use name of model instead of model itself since SSProduct has not been defined yet
    ssid = models.ForeignKey('SSProduct')
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Jurisdiction(models.Model):
    name = models.TextField()
    ssid = models.ForeignKey('SSOrganization')
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
    
# Begin Def of Short Stack models here:
class SSOrganization(models.Model):
    ssid = models.IntegerField(default=0, unique=True)
    name = models.TextField(default="")
    ORG_CHOICES = (
        ("4", "City"),
        ("5", "Department"),
        ("6", "State"),
        ("7", "Federal Agency"),
        ("8", "County"),
        ("4,8", "City and County"),
        ("9", "Federal District"),
        ("4,9", "City and Federal District"),
        ("10", "Unincorporated Organized Territory"),
        ("11", "Unincorporated Unorganized Territory"),
    )
    type = models.CharField(max_length=20, choices=ORG_CHOICES)
    parentid = models.TextField(default="")
    parentname = models.TextField(default="")
    geolong = models.DecimalField(default=0, max_digits=10, decimal_places=4)
    geolat = models.DecimalField(default=0, max_digits=10, decimal_places=4)
    geoname = models.IntegerField(default=0)
    geoarea = models.DecimalField(default=0, max_digits=10, decimal_places=4)
    population = models.IntegerField(default=0)
    GOV_FORM_CHOICES = (
        ("1", "council-manager"),
        ("2", "strong mayor-council"),
        ("3", "weak mayor-council"),
        ("4", "commission"),
        ("5", "not a local government org type"),
    )
    govtype = models.CharField(max_length=1, choices=GOV_FORM_CHOICES)
        

class SSProduct(models.Model):
    ssid = models.IntegerField(default=0, unique=True)
    name = models.TextField(default="")


class SSBudget(models.Model):
    orgid = models.ForeignKey(SSOrganization, to_field = 'ssid')
    year = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    
class SSDependency(models.Model):
    prodid = models.ForeignKey(SSProduct, to_field = 'ssid')
    dependencyid = models.IntegerField(default=0)
    type = models.ForeignKey('DependencyType', to_field = 'name')

class DependencyType(models.Model):
    name = models.TextField(default="", unique=True)

# need to find out how SS is currently storing "used_by" data when it comes time to write the
# API for inserting data into ShortStack. Currently, we have a deployment object but
# maybe in SS this is kept track of via a one to many relationship between products and organizations..

# example snippet of accessing data from an API
class GoogleSearch(django_pipes.Pipe):
    uri = "http://ajax.googleapis.com/ajax/services/search/web"

    @staticmethod
    def fetch(q):
        resp = GoogleSearch.objects.get({'v':1.0, 'q':q})
        if resp and hasattr(resp, "responseData") and hasattr(resp.responseData, "results"):
            return resp.responseData.results