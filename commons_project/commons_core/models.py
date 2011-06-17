from django.db import models
from django.forms import ModelForm
import django_pipes
from filer.fields.image import FilerImageField
from userena.models import UserenaBaseProfile
from filer.fields.file import FilerFileField

#defines the data models for the application
#for anything that we need to store data about.

class App(models.Model):
    """Describes an application or product."""
    name = models.CharField(max_length=100)
    # Must use name of model instead of model itself since
    # SSProduct has not been defined yet.
    ssp = models.ForeignKey('SSProduct', blank=True, null=True)
    screenshots = models.ManyToManyField('Screenshot', blank=True, null=True)
    description = models.TextField()
    dependencies = models.ManyToManyField("self", through='Dependency',
                                          symmetrical=False,
                                          related_name='dependents')
    features = models.ManyToManyField('Feature', blank=True, null=True)
    def __unicode__(self):
        return self.name

class Dependency(models.Model):
    """Describes a dependency relationship between two products"""
    from_app = models.ForeignKey(App, related_name='from_apps')
    to_app = models.ForeignKey(App, related_name='to_apps')
    type = models.ForeignKey('DependencyType', blank=True, null=True)
    
class Screenshot(models.Model):
    """ Screenshots associated with Apps """
    name = models.CharField(max_length=100)
    image = FilerImageField(null=True, blank=True)
    def __unicode__(self):
        return self.name
    
class Feature(models.Model):
    """ Features associated with an App """
    name = models.CharField(max_length=100)
    feature = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class Jurisdiction(models.Model):
    """A jurisdiction, such as a city, county, state, or 
    perhaps more specifically a department."""
    name = models.CharField(max_length=100)
    sso = models.ForeignKey('SSOrganization', blank=True, null=True)
    description = models.TextField()
    parent = models.ForeignKey('self', related_name='children', blank=True,
                               null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.name

class Deployment(models.Model):
    """A deployment of an App at a Jurisdiction, for example 
    EAS at San Francisco."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    jurisdiction = models.ForeignKey(Jurisdiction)
    app = models.ForeignKey(App)

    def __unicode__(self):
        return self.name
        
class DeploymentForm(ModelForm):
    class Meta:
        model = Deployment
        fields = ('name', 'description', 'jurisdiction')
    
class SSOrganization(models.Model):
    """An organization in Shortstack."""
    ssid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="")
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
    """A product in Shortstack."""
    ssid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="")


class SSBudget(models.Model):
    orgid = models.ForeignKey(SSOrganization)
    year = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    
class SSDependency(models.Model):
    prodid = models.ForeignKey(SSProduct)
    dependencyid = models.IntegerField(default=0)
    type = models.ForeignKey('DependencyType')

class DependencyType(models.Model):
    name = models.CharField(max_length=30, default="", unique=True)
    def __unicode__(self):
        return self.name

# The custom Civic Commons Profile object we are using for this site
class CCProfile(UserenaBaseProfile):
    location = models.CharField(max_length=30, blank=True, null=True)
    affiliations = models.ManyToManyField(Jurisdiction, related_name="users",
                                          blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, default='')
    usesapps = models.ManyToManyField(App, related_name='users', blank=True, null=True)
    contributestoapps = models.ManyToManyField(App, related_name='contributors',
											   blank=True, null=True)

# TODO: need to find out how SS is currently storing "used_by" data when it
# comes time to write the API for inserting data into ShortStack. Currently
# we have a deployment object but maybe in SS this is kept track of via a
# one to many relationship between products and organizations..

# example snippet of accessing data from an API

class GoogleSearch(django_pipes.Pipe):
    uri = "http://ajax.googleapis.com/ajax/services/search/web"

    @staticmethod
    def fetch(q):
        resp = GoogleSearch.objects.get({'v':1.0, 'q':q})
        if resp and hasattr(resp, "responseData") and hasattr(resp.responseData, "results"):
            return resp.responseData.results
