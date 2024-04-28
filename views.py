from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
import datetime

def index(request):
    users = Users.objects.filter(pk = request.session['user_id'])
    user = users[0]
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            First_name = form.cleaned_data.get("First_name")
            Last_name = form.cleaned_data.get("Last_name")
            Surname = form.cleaned_data.get("Surname")
            Email = form.cleaned_data.get("Email")
            Address = form.cleaned_data.get("Address")
            Login = form.cleaned_data.get("Login")
            Password = form.cleaned_data.get("Password")
            New_password = form.cleaned_data.get("New_password")
            Confirm_password = form.cleaned_data.get("Confirm_password")

            if First_name != "":
                user.First_name = First_name
            if Last_name != "":
                user.Last_name = Last_name
            if Surname != "":
                user.Surname = Surname
            if Email != "":
                user.Email = Email
            if Address != "":
                user.Address = Address
            if Login != "":
                list = Users.objects.all()
                for i in list:
                    if Login == i.Login:
                        form.add_error(None, "Логин уже используется")
                        return render(request, 'administrator/main.html', {'user_data': user, 'form': form})
                user.Login = Login
            if New_password != "":
                if Password == user.Password:
                    if New_password == Confirm_password:
                        user.Password = New_password
                    else:
                        form.add_error(None, "Пароли не совпадают")
                        return render(request, 'administrator/main.html', {'user_data': user, 'form': form})
                else:
                    form.add_error(None, "Не вырный старый пароль")
                    return render(request, 'administrator/main.html', {'user_data': user, 'form': form})
            user.save()
            users = Users.objects.filter(pk=request.session['user_id'])
            user = users[0]
            form = EditUserForm()
            return render(request, 'administrator/main.html', {'form': form, 'user_data': user})
    else:
        form = EditUserForm()
        return render(request, 'administrator/main.html', {'form': form, 'user_data': user})

def index_p(request):
    users = Users.objects.filter(pk=request.session['user_id'])
    user = users[0]
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            First_name = form.cleaned_data.get("First_name")
            Last_name = form.cleaned_data.get("Last_name")
            Surname = form.cleaned_data.get("Surname")
            Email = form.cleaned_data.get("Email")
            Address = form.cleaned_data.get("Address")
            Login = form.cleaned_data.get("Login")
            Password = form.cleaned_data.get("Password")
            New_password = form.cleaned_data.get("New_password")
            Confirm_password = form.cleaned_data.get("Confirm_password")

            if First_name != "":
                user.First_name = First_name
            if Last_name != "":
                user.Last_name = Last_name
            if Surname != "":
                user.Surname = Surname
            if Email != "":
                user.Email = Email
            if Address != "":
                user.Address = Address
            if Login != "":
                list = Users.objects.all()
                for i in list:
                    if Login == i.Login:
                        form.add_error(None, "Логин уже используется")
                        return render(request, 'administrator/main_p.html', {'user_data': user, 'form': form})
                user.Login = Login
            if New_password != "":
                if Password == user.Password:
                    if New_password == Confirm_password:
                        user.Password = New_password
                    else:
                        form.add_error(None, "Пароли не совпадают")
                        return render(request, 'administrator/main_p.html', {'user_data': user, 'form': form})
                else:
                    form.add_error(None, "Не вырный старый пароль")
                    return render(request, 'administrator/main_p.html', {'user_data': user, 'form': form})
            user.save()
            users = Users.objects.filter(pk=request.session['user_id'])
            user = users[0]
            form = EditUserForm()
            return render(request, 'administrator/main_p.html', {'form': form, 'user_data': user})
    else:
        form = EditUserForm()
        return render(request, 'administrator/main_p.html', {'form': form, 'user_data': user})



def activ_p(request):
    list = Talons.objects.all()
    user_id = request.session['user_id']
    return render(request, 'administrator/activ_talons.html', {'list': list, 'user_id': user_id})

def analysis(request):
    list = Analysis.objects.all()
    return render(request, 'administrator/analysis.html', {'list': list})

def analysis_p(request):
    list = Analysis.objects.all()
    return render(request, 'administrator/analysis_p.html', {'list': list})

def visits(request):
    list = Talons.objects.all()
    user_id = request.session['user_id']
    return render(request, 'administrator/visits.html', {'list': list, 'user_id': user_id})


def patients(request):
    list = Users.objects.all()
    return render(request, 'administrator/patients.html', {'list': list})


def select_patient(request, patient_id):
    list = Items.objects.all()
    return render(request, 'administrator/selected_patient.html', {'patient_id': patient_id, 'list': list})


def select_item(request, item_id):
    list = Items.objects.get(pk=item_id)
    return render(request, 'administrator/selected_item.html', {'list': list})


def signin(request):
    request.session['user_id'] = 0
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            users = Users.objects.filter(Login = login, Password = password)
            if users:
                user = users[0]
                user_id = user.pk
                request.session['user_id'] = user_id
                user = Users.objects.get(pk=request.session['user_id'])
                form = EditUserForm()
                if user.Role == 1:
                    return render(request, 'administrator/main.html', {'user_data': user, 'form': form})
                else:
                    return render(request, 'administrator/main_p.html', {'user_data': user, 'form': form})
            else:
                form.add_error(None, "Пользователь не найден")
                return render(request, 'administrator/signin.html', {'form': form})
    else:
        form = SignInForm()
        return render(request, 'administrator/signin.html', {'form': form})

def additem(request, patient_id):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            Item = Items.objects.create(
            Name = form.cleaned_data.get("Name"),
            patient = patient_id,
            doctor = 5,
            DataTime = datetime.datetime.now().replace (microsecond=0),
            Complaint = form.cleaned_data.get("Complaint"),
            Temperature = form.cleaned_data.get("Temperature"),
            Recommendations = form.cleaned_data.get("Recommendations"),
            Analysis = form.cleaned_data.get("Analysis"),
            Anamnesis = form.cleaned_data.get("Anamnesis"),
            Diagnosis = form.cleaned_data.get("Diagnosis"),
            Mkb = form.cleaned_data.get("Mkb"))
            Item.save()
            list = Items.objects.all()
            return render(request, 'administrator/selected_patient.html', {'patient_id': patient_id, 'list': list})
    else:
        form = AddItemForm()
        return render(request, 'administrator/add_item.html', {'form': form, 'patient_id': patient_id})


def registr(request):
    if request.method == 'POST':
        form = EddUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("Login")
            access = False
            k = 0
            list = Users.objects.all()
            for i in list:
                if login == i.Login:
                    form.add_error(None, "Логин уже используется")
                    return render(request, 'administrator/signup.html', {'form': form})
            password = form.cleaned_data.get("Password")
            c_password = form.cleaned_data.get("Confirm_password")
            if (password == c_password and k ==0):
                new_user = Users.objects.create(
                    First_name = form.cleaned_data.get("First_name"),
                    Last_name = form.cleaned_data.get("Last_name"),
                    Surname = form.cleaned_data.get("Surname"),
                    Email = form.cleaned_data.get("Email"),
                    Sex = form.cleaned_data.get("Sex"),
                    Date_of_birth = form.cleaned_data.get("Date_of_birth"),
                    Login = login,
                    Password = password,
                    Role = 0,
                    Address = form.cleaned_data.get("Address"))
                new_user.save()
                form = SignInForm()
                return render(request, 'administrator/signin.html', {'form': form})
            else:
                form.add_error(None, "Пароли не совпадают")
                return render(request, 'administrator/signup.html', {'form': form})
    else:
        form = EddUserForm()
        return render(request, 'administrator/signup.html', {'form': form})


def order(request):
    if request.method == 'POST':
        form = OrderTalon(request.POST)
        if form.is_valid():
            talon = form.cleaned_data.get("talon")
            talon.Id_of_patient = request.session['user_id']
            talon.save()
            form = EditUserForm()
            return render(request, 'administrator/main_p.html', {'form': form})
    else:
        form = OrderTalon()

    return render(request, 'administrator/order_talon.html', {'form': form})


def restore(request):
    if request.method == 'POST':
        form = RestoreForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            first_name = form.cleaned_data.get("first_name")
            new_password = form.cleaned_data.get("new_password")
            password = form.cleaned_data.get("password")
            users = Users.objects.filter(Login=login, First_name=first_name)
            print(login, " + ", first_name, " + ", password, " + ", new_password)
            if users:
                user = users[0]
                if (password == new_password):
                    user.Password = password
                    user.save()
                    form = RestoreForm()
                    return render(request, 'administrator/signin.html', {'form': form})
                else:
                    form.add_error(None, "Пароли не совпадают")
                    return render(request, 'administrator/restore.html', {'form': form})
            else:
                form.add_error(None, "Пользователь не найден")
                return render(request, 'administrator/restore.html', {'form': form})
    else:
        form = RestoreForm()
        return render(request, 'administrator/restore.html', {'form': form})