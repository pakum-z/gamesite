from django.contrib import admin
from main.models import GameInfo


@admin.register(GameInfo)
class GameInfoAdmin(admin.ModelAdmin):
	pass
