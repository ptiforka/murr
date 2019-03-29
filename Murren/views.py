from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import MurrenRegisterForm


def count_murren(request):
    count = User.objects.count()
    return render(request, 'Murren/count_murren.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = MurrenRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = MurrenRegisterForm()
    return render(request, 'registration/singup.html', {
        'form': form
    })