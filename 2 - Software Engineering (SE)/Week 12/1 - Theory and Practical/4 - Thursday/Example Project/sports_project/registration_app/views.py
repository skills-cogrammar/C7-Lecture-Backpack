from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from .models import Registration
from .forms import RegisterForm, SportRegisterForm
from django.contrib.auth.decorators import permission_required


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']
            if password == password_conf:
                new_user = User()
                new_user.username = form.cleaned_data['username']
                new_user.set_password(password)
                new_user.save()
                if request.POST["account_type"] == 'admin':
                    group = Group.objects.get(name='Admin')
                else:
                    group = Group.objects.get(name='Basic')
                new_user.groups.add(group)
                login(request, new_user)
                return redirect('registrants')
    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form_type': 'Register', 'form':form, 'path': 'create_user'})
        

def logout_user(request):
    logout(request)
    return redirect('login')


def registrants(request):
    if request.user and request.user.is_authenticated:
        registrants = Registration.objects.all()
        return render(request, 'registration/registrants.html',
                      context={'registrants':registrants, 'user': request.user})
    return redirect('login')    


@permission_required('registration_app.add_registration', login_url='registrants')
def sport_registration(request):
    if request.user and request.user.is_authenticated and request.user.has_perm('registration_app.add_registration'):
        if request.method == 'POST':
            registration_form = SportRegisterForm(request.POST)
            if registration_form.is_valid():
                new_registration = Registration.objects.create(
                    user = request.user.username,
                    sport = registration_form.cleaned_data['sport'],
                    team_name = registration_form.cleaned_data['team_name']
                )
                new_registration.save()
                return redirect('registrants')
        form = SportRegisterForm()
        return render(request, 'registration/registration.html', context={'form':form})
    return redirect('login')


def delete_registration(request, id):
    registration = Registration.objects.get(pk=id)
    registration.delete()
    return redirect('registrants')

