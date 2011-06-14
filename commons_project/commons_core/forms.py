from django import forms

from models import Jurisdiction
from models import App

class EditJurisdictionForm(forms.ModelForm):
	"""Edit the Jurisdiction"""
	class Meta:
		model = Jurisdiction
		exclude = ('sso',)

class EditApplicationForm(forms.ModelForm):
    """Edit the Application"""
    class Meta:
        model = App
        exclude = ('ssp',)