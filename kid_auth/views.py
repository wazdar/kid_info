from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'kid_auth/login_view.html', {'form': form})

    def post(self, request, **kwargs):
        form = LoginForm(request.POST)
        text = ''
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
            else:
                text = 'A sio, hackerze!'
        return render(
            request,
            'kid_auth/login_view.html',
            {'form': form, 'text': text},
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')