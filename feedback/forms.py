from .models import Feedback
from django import forms

from django.template.defaultfilters import slugify
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'



