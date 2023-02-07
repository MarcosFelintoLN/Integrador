from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import *



class UserCreation_Form(UserCreationForm):
    password1 = forms.CharField(
    label=_("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder":"Digite sua Senha"}),
    help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
    label=_("Password confirmation"),
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder":"Digite Novamente"}),
    strip=False,
    help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email', 'genero', 'course','periodo','turno', 'password1', 'password2', 'image']
        widgets = {
            'username': forms.TextInput(attrs={
            "class":"",
            "type":"text",
            "placeholder":"Digite a sua Matricula",
            "id":"firstname",
            "name":"firstname"
            }),
          
            'first_name': forms.TextInput(attrs={
            "class":"",
            "type":"text",
            "placeholder":"Digite o seu nome",
            "id":"firstname",
            "name":"firstname"    
            }),
            
            'first_name': forms.TextInput(attrs={
            "class":"",
            "type":"text",
            "placeholder":"Digite o seu nome",
            "id":"firstname",
            "name":"firstname"    
            }),
            
            'last_name': forms.TextInput(attrs={
            "id":"lastname",
            "type":"text",
            "name":"lastname",
            "placeholder":"Digite seu sobrenome",
            }),
            
            'course': forms.Select(attrs={
            "class":"cursedesign",
            "id":"number",
            "type":"option",
            "placehouder":"Seu Curso",
            "name":"number"
            }),
            
            'genero': forms.Select(attrs={
            "class":"genredesign"
            }),
            
            'periodo': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            
            'turno': forms.Select(attrs={
            "id":"number",
            "name":"selection",
            "class":"genredesign"
            }),
            
            }
        
class UserChange_Form(UserChangeForm):
    username = forms.CharField(help_text="",disabled=True, widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'course']

class PasswordChange_Form(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        required=True,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )      

class CompeticaoForm(ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
            "class":"campo",
            "type":"text",
            }),
        }

class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome','genero_modalidade','competicao1']
        widgets = {
            'nome': forms.TextInput(attrs={
            "class":"campo",
            "type":"text",
            }),
            
            'genero_modalidade': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            'competicao1': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
        }

class EquipeForm(ModelForm):
    class Meta:
        model = Equipes
        fields = ['nome','curso_equipe','turno','periodo','participantes','modalidade_equipe']
        widgets = {
            'nome': forms.TextInput(attrs={
            "class":"campo",
            "type":"text",
            }),
            
            'curso_equipe': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            'turno': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            'periodo': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            'modalidade_equipe': forms.Select(attrs={
            "name":"selection",
            "class":"genredesign"
            }),
            
        }