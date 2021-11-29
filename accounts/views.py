from django.shortcuts import render, redirect
from .forms import CreateUserForm, ConsultationForm
from django.contrib.auth import login, authenticate, logout
from .models import Medic, Consultation


def index(request):
    return render(request, 'index.html')


def login_screen(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def register_screen(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')


def medics_screen(request):
    data = Medic.objects.all()
    return render(request, 'medics.html', {'data': data})

def consultation_screen(request, id):
    form = ConsultationForm()
    medic = Medic.objects.get(id=id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            pause = form.save(commit=False)
            pause.user = request.user
            pause.medic = medic
            pause.save()
            return redirect('medics')

    return render(request, 'consultation.html', {'form': form, 'medic': medic})


def my_consults_screen(request):
    data = Consultation.objects.filter(user=request.user.id)
    return render(request, 'myConsults.html', {'data': data})
