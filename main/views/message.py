from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from main.models import Institution


class MessageHome(View):
    pass