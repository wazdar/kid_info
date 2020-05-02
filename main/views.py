from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View




class HomePageView(View):
    def get(self, request):
        return render(request, 'main/home_page_view.html', {})
class HomePageView2(View):
    def get(self, request):
        return render(request, 'main/home_page_view2.html', {})


class UserLoginView(View):
    def get(self, request):
        return render(request, 'main/login_register.html', {})

    def post(self, request):
        pass
        # form = UserLoginForm(request.POST)
        # if form.is_valid():
        #     user = authenticate(request, **form.cleaned_data)
        #     if user is not None:
        #         login(request, user)
        #         return redirect(request.GET.get('next', '/'))

