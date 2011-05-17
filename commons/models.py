from django.db import models

class App(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Jurisdiction(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Deployment(models.Model):
    name = models.TextField()

    jurisdiction = models.ForeignKey(Jurisdiction)
    app = models.ForeignKey(App)

    def __unicode__(self):
        return self.name
