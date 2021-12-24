from django import forms
from .models import Comment, Post, User
from django.contrib.auth.forms  import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content', )