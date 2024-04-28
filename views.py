from django.shortcuts import render


def index(request):
    return render(request, 'doctor/main.html')


def analysis(request):
    return render(request, 'doctor/analysis.html')


def patients(request):

    return render(request, 'doctor/patients.html')


def visits(request):
    return render(request, 'doctor/visits.html')


