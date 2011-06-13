from django import forms

from models import Jurisdiction

class EditJurisdictionForm(forms.ModelForm):
	"""Edit the Jurisdiction"""
	class Meta:
		model = Jurisdiction
		exclude = ('sso',)
