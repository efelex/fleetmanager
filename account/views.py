from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import UserProfileForm, UserCreatForm
# from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('YOu have been logged in '))

# Redirect to a success page.
            return redirect('index')
        else:
            messages.success(request, ('Error logging in please try agin ..'))

            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'account/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('YOu have been logged OUT '))
    return redirect('login')


def create_user(request):
    if request.method == 'POST':
        form = UserCreatForm(request.POST)
        # second form for user profile related data
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            # do not commit profile data right away
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, ('user created successfully '))
            return redirect('home')
    else:
        form = UserCreatForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'account/createuser.html', context)


def edit_profile(request):

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        # second form for user profile related data
        profile_form = UserProfileForm(
            request.POST, instance=request.user.profile)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile_form.save()

            messages.success(request, ('user updated successfully '))
            return redirect('editprofile')
    else:
        form = UserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'account/editprofile.html', context)
