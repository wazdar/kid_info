from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from main.models import Institution


class DashboardHomeView(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self, request):
        if request.user.user_type != 1:
            institution = Institution.objects.get(owner=request.user)
            return render(request, 'main/dashboard/dashboard_home.html', {
                'institution': institution,
                'child_count': institution.child_in_institution_today(),
            })
        else:
            return render(request, 'main/dashboard/dashboard_home.html', {

            })
