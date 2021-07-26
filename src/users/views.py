from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileForm


# Create your views here.
@login_required
def users(request):
    return HttpResponse("Hello users")


@login_required()
def edit_profile(request, id):
    context = {}

    profile = User.objects.get(pk=id)
    profile_form = ProfileForm(request.POST or None, instance=profile)

    if profile_form.is_valid():
        user = profile_form.save(commit=False)
        user.save()
        messages.success(request, 'Profile updated')
        return redirect('dashboard:dashboard')

    context['parent'] = 'My Profile'
    context['page'] = 'Update Profile'
    context['form'] = profile_form
    context['profile'] = id
    return render(request, 'users/update_profile.html', context)


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.staff_status = True
            user.save()
            login(request,user)
            messages.success(request, 'User created')
            return redirect('dashboard:dashboard')
    context['form'] = form
    return render(request, 'registration/signup.html', context)
