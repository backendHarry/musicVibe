from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class MediaFiles(models.Model):
	user_for_files = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	files = models.FileField(upload_to='media')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'MediaFile'
		verbose_name_plural = 'MediaFiles'

#my model for my user files uploaded by users