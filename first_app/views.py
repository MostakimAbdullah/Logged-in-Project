from django.shortcuts import render,redirect
from first_app.forms import user_signup
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = user_signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = user_signup()
    return render(request,'signup.html', {'form': form , 'type': 'SignUp'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passwrd = form.cleaned_data['password']
            user = authenticate(username=name, password=passwrd)
            messages.success(request,'Logged in successful')
            if user is not None:
                login(request, user)
                return redirect('profile')
                
    else:
        form = AuthenticationForm()
    return render(request, 'signup.html', {'form': form, 'type': 'Login'})

@login_required
def user_profile(request):
    return render(request, 'profile.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'password_change.html', {'form': form, 'type': 'Password_Change'})


def pass_reset(request):
    if request.method=='POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password reset successfully')
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'password_change.html', {'form': form, 'type': 'Password_Reset'})