from django import forms
from django.contrib.auth.models import User
from .models import CollaboratorRole, Document


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AddCollaboratorForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    role = forms.ChoiceField(choices=[('Editor', 'Editor'), ('Commenter', 'Commenter'), ('Viewer', 'Viewer')], required=True)

    class Meta:
        fields = ['collaborator', 'role']

class DocumentEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']


