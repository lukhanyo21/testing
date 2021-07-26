from django import forms


class UploadForm(forms.Form):
    contrast = forms.CharField(max_length=5)
    brightness = forms.CharField(max_length=5)
    file = forms.FileField()