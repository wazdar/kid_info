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


def set_presence(child, date, is_present):
    """
    Function to set present or create it.
    :return:
    """
    presences = Presences.objects.filter(date=date).first()
    if presences:
        presences.is_present = is_present
        presences.save()
    else:
        Presences.objects.create(children=child, date=date, is_present=is_present)


class KidsPresencesSetView(LoginRequiredMixin, View):
    def post(self, request):
        child = get_object_or_404(Children, pk=request.POST.get('id'))
        is_present = request.POST.get('presence') in ['true']
        date_start = datetime.datetime.strptime(request.POST.get('date_start'), '%Y-%m-%d')

        if not request.POST.get('date_end'):
            set_presence(child, date_start.date(), is_present)
        else:
            date_end = datetime.datetime.strptime(request.POST.get('date_end'), '%Y-%m-%d') if request.POST.get(
                'date_end') else date_start + datetime.timedelta(days=1)
            for n in range(int((date_end.date() - date_start.date()).days)):
                date = date_start + datetime.timedelta(n)
                set_presence(child, date.date(), is_present)

        return JsonResponse({
            'status': 'ok'
        })


class KidsPresencesGetView(LoginRequiredMixin, View):
    def post(self, request):
        child = get_object_or_404(Children, pk=request.POST.get('id'))
        presences = []
        for presence in child.presences_set.all():
            presences.append({
                'start': presence.date,
                'end': None,
                'rendering': 'background',
                'allDay': 'true',
                'color': '#21ff37' if presence.is_present else '#ff6161'
            })

        return JsonResponse(presences, safe=False)


class KidsAllPresencesGetView(LoginRequiredMixin, View):
    def post(self, request):
        return JsonResponse({'ok': 'ok'})
