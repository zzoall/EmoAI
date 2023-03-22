from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["birth_date"]
        
    def signup(self, request, user):
        user.birth_date = self.cleaned_data["birth_date"]
        user.save()
