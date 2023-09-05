from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


def login_view(request):
    context = {
        'form': AuthenticationForm(request)
    }

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logado com sucesso')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Login invalido')

    return render(request, 'contact/login.html', context)


def register(request):
    context = {
        'form': RegisterForm()
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Criado com sucesso')
            return redirect('contact:login')

    return render(request, 'contact/register.html', context)


@login_required(login_url='contact:login')
def update_view(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario atualizado com sucesso')
            return redirect('contact:update_view')

    return render(
        request,
        'contact/update.html',
        {
            'form': form
        }
    )
