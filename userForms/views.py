from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from scheduler.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from students.models import Student


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        if 'f1' in request.POST:                                     
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Login Successful for {username}')
                role = user.is_staff
                if role:
                   return redirect('home-mentor')
                else:
                   return redirect('home-student')
            else:
                messages.warning(request, 'Invalid Credentials!! Please Try to Submit Again')
                return render(request, 'userForms/register.html')
        else:
            messages.error(request, 'Form Not Submitted Properly')
            return render(request, 'userForms/register.html')
    else:
        return render(request, 'userForms/register.html')
    


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.all().get(username=username)
            student = Student(name = user.username, ref = user)
            student.save()
            messages.success(request, f'Account Successfully created for {username}')
            return redirect('login-view')
    else:
        form = RegisterForm()
    return render(request, 'userForms/new_user.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('login-view')