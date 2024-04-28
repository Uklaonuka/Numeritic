from django import forms
from .models import *


class SignInForm(forms.Form):
    login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Пароль'}))


class AddItemForm(forms.Form):
    Name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Обращение'}))
    Complaint = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Жалобы'}))
    Temperature = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Температура'}))
    Recommendations = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Рекомендации'}))
    Analysis = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'placeholder': 'Анализы'}))
    Anamnesis = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Анамнез'}))
    Diagnosis = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Диагноз'}))
    Mkb = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Код МКБ-10'}), required=False)


class EddUserForm(forms.Form):
    First_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    Last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    Surname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    Email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'type': 'email'}))
    Sex = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Пол'}))
    Date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Адрес проживания'}))
    Login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    Password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'type': 'password'}))
    Confirm_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Подтвердите пароль', 'type': 'password'}))


class EditUserForm(forms.Form):
    First_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}), required=False)
    Last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Имя'}), required=False)
    Surname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}), required=False)
    Email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'type': 'email'}), required=False)
    Sex = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Пол'}), required=False)

    Address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Адрес проживания'}), required=False)
    Login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Логин'}), required=False)
    Password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Старый пароль', 'type': 'password'}), required=False)
    New_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Новый пароль', 'type': 'password'}), required=False)
    Confirm_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Подтвердите пароль', 'type': 'password'}), required=False)


class RestoreForm(forms.Form):
    login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Пароль'}))
    new_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Подтвердите пароль'}))


class OrderTalon(forms.Form):
    talon = forms.ModelChoiceField(queryset=Talons.objects.filter(Id_of_patient = 0))
