from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from main.models import Children


class MainBillsView(View):
    def get(self, request):
        childrens = Children.objects.filter(institution=request.user.institution_set.all().first())
        return render(request, 'main/dashboard/bills/main_bills_view.html', {
            'childrens': childrens,
        })
