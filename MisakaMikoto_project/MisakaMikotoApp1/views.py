from django.shortcuts import render
from MisakaMikotoApp1.models import MisakaMikoto, Webpage, AccessRecord, users
from . import forms
from .forms import usersForm, UserForm, UserProfileInfoForm 

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    Webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': Webpage_list}
 
    return render(request, 'MisakaMikotoApp1/TheAdrian.html', context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])


    return render(request, 'MisakaMikotoApp1/form_page.html', {'form': form})

# this is a view for the users form
def user_form_view(request):
    form = usersForm()
    if request.method == 'POST':
        form = usersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Form Saved!')
            return index(request)
        else:
            print('Error Form Invalid')
    return render(request, 'MisakaMikotoApp1/TheAdrian.html', {'form': form})


def registration_view(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'MisakaMikotoApp1/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def register(request):
    return render(request, 'MisakaMikotoApp1/registration.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'MisakaMikotoApp1/login.html', {})
    
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))