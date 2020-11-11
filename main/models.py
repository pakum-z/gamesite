from django.db import models


class GameInfo(models.Model):
	name = models.CharField("Название", max_length=150)
	desc = models.TextField("Описание")
	zip_file = models.FileField("Архив с файлами игры", upload_to="game_files/")
	
	def __str__(self):
		return "Информация о проекте"
	
	class Meta:
		verbose_name = "Информация о проекте"
		verbose_name_plural = "Информация о проекте"
