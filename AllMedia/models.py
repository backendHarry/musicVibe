from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class MediaFiles(models.Model):
    user_for_files = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    files = models.FileField(upload_to='media')
    
    class Meta:
        verbose_name = 'MediaFile'
        verbose_name_plural = 'MediaFiles'

    def __str__(self):
        return self.name

#my model for my user files uploaded by users
