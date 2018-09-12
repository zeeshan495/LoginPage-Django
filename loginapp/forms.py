from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "user name",
                                                             "id": "form_username"}
                                                      ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "password",
                                                                 "id": "form_password"}
                                                          ))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "user name",
                                                             "id": "form_username"}
                                                      ))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control",
                                                           "placeholder": "your mail",
                                                           "id": "form_mail"}
                                                    )
                            )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "password",
                                                                 "id": "form_password"}
                                                          ))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "placeholder": "re-enter password",
                                                                 "id": "form_password"}
                                                          ))

    def clean_userName(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("password not match")
        return data