from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Profile


from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


from .forms import LoginForm
from .forms import ProfileForm



## MainPage##

def signup(request):
  # email = Profile.objects.get()
  # POST Request for a new user
  if request.method == 'POST':
    # Verify passwords
    if request.POST['password1'] == request.POST['password2'] and request.POST['password1'] != '':
      try:
        # If Username already exists, render form with error
        user = User.objects.get(username=request.POST['username'])
        return render(request, 'signup.html', {'error': 'Username already in use'})
      # If user does not exist, create and login new user then redirect to home
      except User.DoesNotExist:
        user = User.objects.create_user(
            request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
        profile = Profile.objects.create(
            user=user, email=request.POST['email'])
        auth.login(request, user)
        return redirect('index')

    else:
      return render(request, 'signup.html', {'error': 'Passwords do not match'})
  # GET request for empty sign up form
  else:
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)

        print("login POST request")

        if form.is_valid():
            e = form.cleaned_data['username']
            p = form.cleaned_data['password']

            print("form is valid: " + e)

            foundUser = auth.authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if foundUser:
                auth.login(request, foundUser)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'invalid', 'username': e})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('landing')

#### User ####

## user profile page ##
# @login_required


def user_info(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    #events = Event.objects.filter
    return render(request, 'user.html', {'profile': profile})


## edit ##

def user_edit(request, id):
  user = User.objects.get(id=id)
  profile = Profile.objects.get(user=user)
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        profile = form.save()
        return redirect('user_info', id=id)
  else:
    form = ProfileForm(instance=profile)
  return render(request, 'user_form.html', {'form': form})
