from django import forms

from apps.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'parent', 'explicit_url', 'named_url')

    def clean_explicit_url(self):
        return self.cleaned_data['explicit_url'] or None

    def clean_named_url(self):
        return self.cleaned_data['named_url'] or None
