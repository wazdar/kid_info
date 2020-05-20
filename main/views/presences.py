import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from main.models import Institution, Presences
from main.forms import ChildrenAddForm
from main.models import Children


class KidsPresencesView(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self, request):
        if request.user.user_type != 1:
            childrens = Children.objects.filter(institution=request.user.institution_set.all()[0])
            return render(request, 'main/dashboard/presences/presences_home.html', {
                'childrens': childrens,
            })

        else:
            children = Children.objects.filter(mother=request.user) | Children.objects.filter(father=request.user)
            return render(request, 'main/dashboard/presences/presences_parent_home.html', {
                'children': children.first(),
            })


class KidsPresencesSetView(LoginRequiredMixin, View):
    def post(self, request):
        child = get_object_or_404(Children, pk=request.POST.get('id'))
        presence = request.POST.get('presence') in ['true']
        date_start = datetime.datetime.strptime(request.POST.get('date_start'), '%Y-%m-%d')
        date_end = datetime.datetime.strptime(request.POST.get('date_end'), '%Y-%m-%d') if request.POST.get(
            'date_end') else date_start + datetime.timedelta(days=1)

        for a in Presences.objects.raw('SELECT * FROM main_presences WHERE %s BETWEEN date_start AND date_end OR %s = date_start OR %s = date_end', [date_start.date(), date_start.date(), date_start.date()]):
            print(a)

        # https://stackoverflow.com/questions/32248375/select-the-highest-difference-value-between-two-columns
        #Presences.objects.create(children=child, date_start=date_start, date_end=date_end, is_present=presence)

        return JsonResponse({
            'status': 'ok'
        })


class KidsPresencesGetView(LoginRequiredMixin, View):
    def post(self, request):
        child = get_object_or_404(Children, pk=request.POST.get('id'))
        presences = []
        for presence in child.presences_set.all():
            presences.append({
                'start': presence.date_start,
                'end': presence.date_end if presence.date_end else None,
                'rendering': 'background',
                'allDay': 'true',
                'color': '#21ff37' if presence.is_present else '#ff6161'
            })

        return JsonResponse(presences, safe=False)
