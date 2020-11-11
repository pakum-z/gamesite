from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from main.models import GameInfo


# Главная страница
class HomePage(ListView):
	model = GameInfo
	queryset = GameInfo.objects.all()
	template_name = "main.html"
	extra_context = {
		"title": "Главная",
	}
