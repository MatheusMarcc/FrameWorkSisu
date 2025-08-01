from django import forms
from django.contrib.auth.models import User
class FeedbackForm(forms.ModelForm):
    user=forms.CharField(widget=forms.HiddenInput)
    def clean_user(self):
        user=User.objects.get(id=self._request.user.id)
        return user


from .models import Curso
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']
