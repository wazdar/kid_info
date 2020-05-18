from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from main.models import Institution
from main.forms import ChildrenAddForm
from main.models import Children


class KidsAddView(View):
    def get(self, request):
        form = ChildrenAddForm()
        return render(request, 'main/dashboard/kids/kids_add.html', {
            'form': form,
        })

    def post(self, request):
        form = ChildrenAddForm(request.POST)
        if form.is_valid():
            children = Children.objects.create(**form.cleaned_data, institution=request.user.institution_set.all()[0])

            return render(request, 'main/dashboard/kids/kids_add.html', {
                'form': form,
                'msg': f'dodano {children.first_name} {children.last_name}'
            })
        else:
            return render(request, 'main/dashboard/kids/kids_add.html', {
                'form': form,
            })


class DashboardKidsView(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self, request):
        if request.user.user_type != 1:
            childrens = Children.objects.filter(institution=request.user.institution_set.all()[0])

        else:
            childrens = Children.objects.filter(mother=request.user) | Children.objects.filter(father=request.user)

        return render(request, 'main/dashboard/kids/kids_home.html', {
            'childrens': childrens,
        })