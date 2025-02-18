from django.forms import  ModelForm

from translations.models import Slug


class SlugForm(ModelForm):
    class Meta:
        model = Slug
        exclude = ['code']