from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic.base import View

from main.models import Message, Children


class MessageHome(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'main/dashboard/message/message_home.html', {
            'childrens': request.user.institution_set.all().first().children_set.all()
        })


class MessageAPI(LoginRequiredMixin, View):
    def get(self, request):
        child_id = request.GET.get('id')
        if child_id is not None:
            msg_data = []
            msg_set = get_list_or_404(Message, children=get_object_or_404(Children, pk=child_id))
            for msg in msg_set:
                msg_data.append({
                    "id": msg.id,
                    "datetime": msg.date,
                    "from_parent": msg.children.is_parent(msg.sender),
                    "text": msg.text
                })

            return JsonResponse(
                msg_data
                , safe=False)
        return JsonResponse({
            "adsdadasd": "dupa"
        })

    def post(self, request):
        child = get_object_or_404(Children, pk=request.POST.get('id'))
        msg_text = request.POST.get('text')
        if msg_text is not None or msg_text != '':
            msg = Message.objects.create(children=child, sender=request.user, text=msg_text)
            JsonResponse({
                'msg': msg.id
            })
        return JsonResponse(request.POST)
