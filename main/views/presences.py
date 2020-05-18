from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from main.models import Institution
from main.forms import ChildrenAddForm
from main.models import Children


class KidsPresencesView(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self,request):
        if request.user.user_type != 1:
            childrens = Children.objects.filter(institution=request.user.institution_set.all()[0])

        return render(request, 'main/dashboard/presences/presences_home.html', {
            'childrens': childrens,
        })
