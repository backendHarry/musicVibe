from django import forms
from .models import MediaFiles

class MediaFilesForm(forms.ModelForm):
	class Meta:
		model = MediaFiles
		fields = ('files',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['files'].widget.attrs.update({
                    'class': 'hide-me',
                    'id': 'fileElem',
                    'style': 'display:none;',
                    'multiple': True,
                })

#forms for saving media files from user
