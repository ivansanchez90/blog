from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
# class FormularioLogin(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(FormularioLogin, self).__init__(*args,**kwargs)
#         self.fhields['username'].widget.attrs['class'] = 'form-control'
#         self.fhields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
#         self.fhields['password'].widget.attrs['class'] = 'form-control'
#         self.fhields['password'].widget.attrs['placeholder'] = 'Contraseña'

# class FormularioUsuario(forms.ModelForm):
#     password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput(
#         attrs = {
#             'class': 'form-control',
#             'placeholder': 'Ingrese su contraseña...',
#             'id': 'password1',
#             'required': 'required',
#         }
#     ))

#     passwrod2 = forms.CharField(label = 'Contraseña de Confirmación', widget=forms.PasswordInput(
#         attrs = {
#             'class': 'form-control',
#             'placeholder': 'Ingrese nuevamente su contraseña...',
#             'id': 'password2',
#             'required': 'required',
#         }
#     ))

#     class Meta:
#         modelo = Autor
#         fields = ('email', 'username', 'nombres', 'apellidos')
#         widgets = {
#             'email' : forms.EmailInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder' : 'Correo Electrónico'
#                 }
#             ),
#             'nombres' : forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder' : 'Ingrese sus nombres'
#                 }
#             ),
#             'apellidos' : forms.TextInput(
#                 attrs = {
#                     'class': 'form-control',
#                     'placeholder' : 'Ingrese sus apellidos'
#                 }
#             ),
#             'username' : forms.TextInput(
#                 attrs= {
#                     'class': 'form-control',
#                     'placeholder' : 'Ingrese sus nombre de usuario'
#                 }
#             )
#         }
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}